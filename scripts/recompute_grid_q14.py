"""Replay E70's observed detector scores from the frozen Q1.4 trajectories.

    uv run python scripts/recompute_grid_q14.py

No simulation, judge calls, null draws, tuning or new held-out evaluation. The
linear design, standardisation, Gaussian CMI clipping, directional TE and two
level baselines follow the pinned source. Replays four run scores per game and
the original cell-by-arm bootstrap. Executed labels and permutation flags are
outside this replay. Original source functions are checked separately in tests.
"""
from collections import defaultdict
from itertools import combinations
import json

import numpy as np

from evidence import Evidence, ROOT

DETS = ("market_level", "pair_level", "pcmi", "te")
NASH = {6: 10, 8: 12}
PAIRS = tuple(combinations(range(4), 2))
OUT = ROOT / "results/grid_q14.json"


def load_cell(ev, cell):
    """Keep completed, correct-model games; preserve ground-truth insertion order.

    As in e70_inputs.load_games, orphan trajectory rows are ignored and wrong
    seller models excluded. Every retained game must contain all twenty rounds.
    """
    base = f"data/llm_grid_p2_{cell['cell']}"
    gt_rows = [json.loads(x) for x in ev.lines("q14", base + "/ground_truth.jsonl")]
    gt = {g["run_id"]: g for g in gt_rows}
    assert len(gt) == len(gt_rows), "duplicate ground truth"
    conditions = ("B", "D") if cell["levels"]["shocks"] == "random" else ("A", "C")
    for g in gt.values():
        assert g["condition"] in conditions and g["T"] == 20, "unexpected condition/horizon"
    bad = {rid for rid, g in gt.items() if set(g.get("model") or {}) != set("ABCD")
           or any(m != cell["levels"]["model"] for m in g["model"].values())}
    rows = defaultdict(list)
    for line in ev.lines("q14", base + "/trajectories.jsonl"):
        r = json.loads(line)
        if r["run_id"] in gt and r["run_id"] not in bad:
            rows[r["run_id"]].append(r)
    for rid in gt.keys() - bad:
        rs = rows[rid]
        rs.sort(key=lambda r: r["round"])
        assert [r["round"] for r in rs] == list(range(20)), "missing/duplicate round"
        for r in rs:
            assert [a["id"] for a in r["agents"]] == list("ABCD"), "seller ordering changed"
            assert all(np.isfinite(float(a["price"])) for a in r["agents"]), "nonfinite price"
    return {rid: g for rid, g in gt.items() if rid not in bad}, dict(rows), len(bad)


def arrays(rows):
    P = np.array([[a["price"] for a in r["agents"]] for r in rows], float)
    state = [json.dumps(r["market"], sort_keys=True) for r in rows]
    levels = sorted(set(state))
    S = np.array([levels.index(s) for s in state])
    nash = np.array([NASH[r["market"]["cost"]] for r in rows], float)
    return P, S, nash


def pair_scores(P, S, nash):
    """Observed scores only. Linear state + lag design, with no null calibration."""
    t = np.arange(1, len(P))

    def design(exclude=None):
        return np.column_stack([np.ones(len(t))]
                               + [(S[t] == s).astype(float) for s in range(1, S.max() + 1)]
                               + [P[t - 1, k] for k in range(4) if k != exclude])

    def resid(y, X):
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        r = y - X @ beta
        return (r - r.mean()) / (r.std() + 1e-12)

    def cmi(a, b):
        rho = float(np.clip(np.mean(a * b), -0.999999, 0.999999))
        return float(-0.5 * np.log(1 - rho * rho))

    X = design()
    R = np.column_stack([resid(P[t, k], X) for k in range(4)])
    result = {}
    for i, j in PAIRS:
        directional = []
        for a, b in ((i, j), (j, i)):
            Xb = design(exclude=a)
            directional.append(cmi(resid(P[t - 1, a], Xb), resid(P[t, b], Xb)))
        others = [k for k in range(4) if k not in (i, j)]
        result["ABCD"[i] + "ABCD"[j]] = {
            "market_level": float((P[:, [i, j]] - nash[:, None]).mean()),
            "pair_level": float(P[:, [i, j]].mean() - P[:, others].mean()),
            "pcmi": cmi(R[:, i], R[:, j]), "te": max(directional)}
    return result


def games_from_trajectories(ev):
    cells = ev.json("q14", "data/llm_grid_p2_manifest.json")["cells"]
    assert [c["cell"] for c in cells] == [f"c{i:02d}" for i in range(16)], "grid cell coverage"
    games, exclusions = [], {}
    for c in cells:
        gt, rows, nbad = load_cell(ev, c)
        exclusions[c["cell"]] = nbad
        # All six complete sweeps were retained in the historical analysis.
        conds = ("B", "D") if c["levels"]["shocks"] == "random" else ("A", "C")
        expected = {f"llm_grid_p2_{c['cell']}_{cond}_{s:03d}" for cond in conds for s in range(6)}
        assert set(gt) == expected, "frozen six-sweep cohort changed"
        for rid, g in gt.items():
            P, S, nash = arrays(rows[rid])
            scores = pair_scores(P, S, nash)
            channel = g["condition"] in ("C", "D")
            pair = ["ABCD".index(x) for x in g["assigned_pair"]] if channel else []
            rivals = [k for k in range(4) if k not in pair]
            games.append({"cell": c["cell"], "run_id": rid, "channel": channel,
                          "markup": float((P - nash[:, None]).mean()),
                          "rival_markup": float((P[:, rivals] - nash[:, None]).mean()),
                          "scores": {d: max(p[d] for p in scores.values()) for d in DETS}})
    assert len(games) == 192
    return cells, games, exclusions


def summarize(cells, games, n_boot=2000):
    """Original draw order: cell order, channel then control, six games per arm.

    Precomputing each cell's pairwise comparison matrix preserves ties and the
    original run draws while avoiding repeated score comparisons per bootstrap.
    """
    rng = np.random.default_rng(0)
    pool = {d: np.zeros(n_boot + 1) for d in DETS}
    markup = np.zeros((n_boot + 1, len(cells)))
    per_cell, matrices = {}, []
    for j, cell in enumerate(cells):
        arm = {v: [g for g in games if g["cell"] == cell["cell"] and g["channel"] == v]
               for v in (True, False)}
        assert all(len(a) == 6 for a in arm.values())
        M = {d: np.array([g["scores"][d] for g in arm[True]])[:, None]
             - np.array([g["scores"][d] for g in arm[False]]) for d in DETS}
        M = {d: (m > 0).astype(float) + 0.5 * (m == 0) for d, m in M.items()}
        p, q = (np.array([g["markup"] for g in arm[v]]) for v in (True, False))
        markup[0, j] = p.mean() - q.mean()
        for d in DETS:
            pool[d][0] += M[d].sum()
        per_cell[cell["cell"]] = {"d": round(float(markup[0, j]), 3),
                                  "auroc": {d: round(float(M[d].mean()), 3) for d in DETS}}
        matrices.append((M, p, q))
    for b in range(1, n_boot + 1):
        for j, (M, p, q) in enumerate(matrices):
            pi, qi = (rng.integers(0, 6, 6) for _ in range(2))
            markup[b, j] = p[pi].mean() - q[qi].mean()
            for d in DETS:
                pool[d][b] += M[d][np.ix_(pi, qi)].sum()

    pool = {d: a / (len(cells) * 36) for d, a in pool.items()}

    def triple(a):
        return [float(a[0]), *map(float, np.quantile(a[1:], [.025, .975]))]

    raw = {d: triple(a) for d, a in pool.items()}
    paired = {}
    for d in ("pcmi", "te"):
        a = pool["market_level"] - pool[d]
        v = triple(a)
        paired[f"level_minus_{d}"] = {"delta": round(v[0], 3), "ci": [round(x, 3) for x in v[1:]],
                                       "p_boot_le0": round(float((a[1:] <= 0).mean()), 4)}
    # Count wins using exact cell AUROCs, before the source's 3-dp rounding.
    wins = sum(M["market_level"].sum() > M["pcmi"].sum() for M, _, _ in matrices)
    ties = sum(M["market_level"].sum() == M["pcmi"].sum() for M, _, _ in matrices)
    return {"pooled_auroc": {d: {"auroc": round(a[0], 3), "ci": [round(x, 3) for x in a[1:]]}
                             for d, a in raw.items()},
            "pooled_auroc_unrounded": raw,
            "paired_contrasts": paired,
            "pooled_C_minus_A": [round(x, 3) for x in triple(markup.mean(axis=1))],
            "cells_C_minus_A_positive": int((markup[0] > 0).sum()),
            "cells_level_gt_pcmi": int(wins), "cells_level_ties_pcmi": int(ties),
            "per_cell": per_cell}


def replay(ev):
    cells, games, exclusions = games_from_trajectories(ev)
    saved = ev.json("q14", "results/eval/e70_grid.json")
    assert (saved["complete_sweeps"], saved["n_games"]) == (6, 192)
    assert exclusions == saved["excluded_model_mismatch"]
    assert [g["run_id"] for g in games] == [g["run_id"] for g in saved["games"]], "cohort/order mismatch"
    errors = {d: [] for d in DETS}
    for actual, original in zip(games, saved["games"]):
        for k in ("cell", "channel", "markup", "rival_markup"):
            assert actual[k] == original[k], (actual["run_id"], k)
        for d in DETS:
            error = abs(actual["scores"][d] - original["scores"][d])
            assert error <= 1e-12, (actual["run_id"], d, error)
            errors[d].append(error)
    summary = summarize(cells, games)
    assert summary["pooled_auroc"] == saved["pooled_auroc"]
    e74 = ev.json("q14", "results/eval/e74_paired_diff.json")["E70_pooled"]
    assert summary["paired_contrasts"] == {k: e74[k] for k in summary["paired_contrasts"]}
    assert summary["pooled_C_minus_A"] == [saved["primary"]["pooled_C_minus_A"], *saved["primary"]["pooled_ci"]]
    assert summary["cells_C_minus_A_positive"] == saved["primary"]["cells_d_pos"]
    assert summary["cells_level_gt_pcmi"] == saved["level_vs_pcmi"]["cells_level_gt_pcmi"]
    assert summary["cells_level_ties_pcmi"] == saved["level_vs_pcmi"]["ties"]
    for c, value in summary["per_cell"].items():
        assert value == {k: saved["per_cell"][c][k] for k in value}, c
    return {"q14_commit": ev.manifest["projects"]["q14"]["commit"],
            "n_games": len(games), "n_score_cells": len(games) * len(DETS),
            "n_rounds": len(games) * 20, "n_boot": 2000, "seed": 0,
            "excluded_model_mismatch": exclusions,
            "max_absolute_score_error": {d: max(v) for d, v in errors.items()},
            "saved_result_matches": True,
            "scope": "Observed four-detector run scores from frozen trajectories, grid cohort and "
                     "cell-by-arm bootstrap; no null draws/flags, judge or executed-label validation, "
                     "tuning or new experimental evaluation.",
            **summary, "games": games}


if __name__ == "__main__":
    result = replay(Evidence())
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Q1.4 raw grid replay: {result['n_games']} games, {result['n_score_cells']} scores; "
          f"max errors {result['max_absolute_score_error']}; all selected saved results match")
