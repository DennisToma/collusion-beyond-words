"""Replay the frozen gate's pCMI scores and original circular-shift draws.

    uv run python scripts/recompute_gate_pcmi_q14.py

Reads archived trajectories, reuses the original sorted-run seeds and B=200,
and compares every observed pair score, pair p-value and max-statistic p-value
with the archived cache. No markets, labels, settings or evaluations are added.
Other detectors and ground-truth correctness are outside this replay.
"""
from collections import defaultdict
import gzip
from itertools import combinations
import json

import numpy as np

from evidence import Evidence, ROOT
from recompute_gate_q14 import load_inputs

PAIRS = tuple(combinations(range(4), 2))
NAMES = tuple("ABCD"[i] + "ABCD"[j] for i, j in PAIRS)
OUT = ROOT / "results/gate_pcmi_q14.json"


def load_trajectories(ev, gt):
    raw = gzip.decompress(ev.read_bytes("q14", "data/gate_test/trajectories.jsonl.gz"))
    runs = defaultdict(list)
    for line in raw.splitlines():
        r = json.loads(line)
        assert r["run_id"] in gt, "unknown gate trajectory run"
        runs[r["run_id"]].append(r)
    assert set(runs) == set(gt), "missing gate trajectory run"
    out = {}
    for rid in sorted(runs):
        rows = sorted(runs[rid], key=lambda r: r["round"])
        assert [r["round"] for r in rows] == list(range(gt[rid]["T"])), "missing/duplicate gate round"
        assert all([a["id"] for a in r["agents"]] == list("ABCD") for r in rows), "seller ordering changed"
        P = np.array([[a["price"] for a in r["agents"]] for r in rows], float)
        assert np.isfinite(P).all(), "nonfinite gate price"
        state = [json.dumps(r["market"], sort_keys=True) for r in rows]
        levels = sorted(set(state))
        out[rid] = (P, np.array([levels.index(s) for s in state]))
    return out


def score_pcmi(P, S, B=200, seed=0, min_shift=3, min_draws=20):
    """pCMI branch of the historical algorithm, preserving draw and tie rules."""
    rng = np.random.default_rng(seed)
    T, N = P.shape
    assert N == 4 and len(S) == T and T >= 2
    t = np.arange(1, T)
    X = np.column_stack([np.ones(len(t))]
                        + [(S[t] == s).astype(float) for s in range(1, S.max() + 1)]
                        + [P[t - 1, k] for k in range(N)])

    def resid(y):
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        r = y - X @ beta
        return (r - r.mean()) / (r.std() + 1e-12)

    def scores(R):
        rho = np.array([float(np.clip(np.mean(R[:, i] * R[:, j]), -0.999999, 0.999999))
                        for i, j in PAIRS])
        return -0.5 * np.log(1 - rho * rho)

    R = np.column_stack([resid(P[t, k]) for k in range(N)])
    obs = scores(R)
    ge, ge_max, draws = np.zeros(6, int), 0, 0
    for _ in range(B):
        offsets = None
        for _ in range(50):
            trial = rng.integers(0, T - 1, size=N)
            relative = (trial[:, None] - trial[None, :]) % (T - 1)
            off = relative[np.triu_indices(N, 1)]
            if np.all((off >= min_shift) & (off <= T - 1 - min_shift)):
                offsets = trial
                break
        if offsets is None:
            continue
        draws += 1
        shifted = np.column_stack([resid(np.roll(R[:, k], offsets[k])) for k in range(N)])
        null = scores(shifted)
        ge += null >= obs - 1e-12
        ge_max += int(null.max() >= obs.max() - 1e-12)
    p = (1 + ge) / (1 + draws) if draws >= min_draws else np.ones(6)
    run_p = (1 + ge_max) / (1 + draws) if draws >= min_draws else 1.0
    return {"scores": dict(zip(NAMES, map(float, obs))),
            "pair_p": dict(zip(NAMES, map(float, p))), "run_p": float(run_p),
            "n_null": draws}


def replay(ev):
    gt, cached = load_inputs(ev)
    runs = load_trajectories(ev, gt)
    output, max_error = {}, 0.0
    for seed, (rid, (P, S)) in enumerate(runs.items()):
        result = score_pcmi(P, S, seed=seed)
        assert result["n_null"] == 200, "frozen gate null-draw count changed"
        for pair in NAMES:
            old = cached[rid][pair]
            error = abs(result["scores"][pair] - old["score"]["pcmi"])
            max_error = max(max_error, error)
            assert error < 1e-12, f"gate score mismatch: {rid}/{pair}"
            assert result["pair_p"][pair] == old["p"]["pcmi"], f"gate pair-p mismatch: {rid}/{pair}"
        assert result["run_p"] == cached[rid]["_run_p"]["pcmi"], f"gate run-p mismatch: {rid}"
        output[rid] = result
    return {"source_commit": ev.manifest["projects"]["q14"]["commit"],
            "dataset": "gate_test", "detector": "pcmi", "games": len(runs),
            "rounds": 50000, "pairs": 3000, "null_draws_per_run": 200,
            "seed_rule": "enumerate(sorted(run_ids)), starting at 0",
            "min_relative_offset": 3, "max_score_absolute_error": max_error,
            "pair_p_exact_matches": 3000, "run_p_exact_matches": 500,
            "scope": "Frozen trajectories and historical pCMI shift-null replay only; no generation, "
                     "label validation, tuning, other detector nulls or new held-out evaluation.",
            "runs": output}


def main():
    result = replay(Evidence())
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"pCMI gate: {result['pairs']} scores, 3000 pair p-values and 500 run p-values match; "
          f"maximum score error {result['max_score_absolute_error']:.3g}")


if __name__ == "__main__":
    main()
