"""Reaggregate the historical scripted gate from frozen pair-score/p-value caches.

    uv run python scripts/recompute_gate_q14.py

No simulations, detector fitting, null draws or new held-out evaluation. Shift
tests reuse their archived max-statistic run p-values; surrogate p-values follow
the original same-shock-family ranking with leave-one-out clean controls. This
checks aggregation, not the score estimator, null generator or ground-truth truth.
"""
from collections import Counter
from itertools import combinations
import json

import numpy as np

from evidence import Evidence, ROOT

DETS = ("pearson", "pearson_diff", "mi", "cmi_state", "pcmi", "te",
        "ni_mi", "ni_cmi_state", "ni_pcmi")
P_DETS = DETS[:6]
PAIRS = tuple("".join(p) for p in combinations("ABCD", 2))
GROUPS = (("A", None), ("B", "common_shock"), ("C", None), ("D", None),
          ("A", "shared_policy"), ("A", "shared_seed"), ("A", "legit_cooperation"),
          ("A", "independent_high_price"), ("B", "shared_policy"), ("B", "shared_seed"))
ALPHA = 0.05
OUT = ROOT / "results/gate_q14.json"


def load_inputs(ev):
    rows = [json.loads(s) for s in ev.lines("q14", "data/gate_test/ground_truth.jsonl")]
    gt = {g["run_id"]: g for g in rows}
    assert len(gt) == len(rows) == 500, "missing/duplicate gate ground truth"
    assert set(gt) == {f"gate_test_{i:05d}" for i in range(500)}, "frozen gate cohort changed"
    for i in range(500):
        g = gt[f"gate_test_{i:05d}"]
        condition, hn = GROUPS[i // 50]
        assert (g["condition"], g["hard_negative"], g["seed"], g["T"]) == (
            condition, hn, 1001000000 + i, 100), "frozen gate design changed"
        assert g["private_channel_enabled"] == (condition in "CD")
        for key, present in (("assigned_pair", condition in "CD"), ("hn_pair", hn not in (None, "common_shock"))):
            pair = g[key]
            if present:
                assert isinstance(pair, list) and len(pair) == 2 and "".join(sorted(pair)) in PAIRS, "invalid gate pair"
            else:
                assert pair is None, "invalid gate pair"

    res = {rid: {p: {"score": {}, "p": {}} for p in PAIRS} | {"_run_p": {}} for rid in gt}
    for det in DETS:
        cache = [json.loads(s) for s in ev.lines("q14", f"results/{det}/gate_test.jsonl")]
        seen = set()
        for row in cache:
            rid, pair = row["run_id"], row["pair"]
            assert rid in gt and pair in PAIRS, "unknown gate run/pair"
            assert (rid, pair) not in seen, "duplicate gate score"
            seen.add((rid, pair))
            score = row["score"]
            assert isinstance(score, (int, float)) and not isinstance(score, bool) and np.isfinite(score), "nonfinite gate score"
            for field in ("p", "run_p"):
                p = row[field]
                if det in P_DETS:
                    assert isinstance(p, (int, float)) and not isinstance(p, bool) and np.isfinite(p) and 0 < p <= 1, "invalid gate p-value"
                    assert abs(p * 201 - round(p * 201)) < 1e-10, "gate p-value is not from B=200"
                else:
                    assert p is None, "NI detector unexpectedly has shift p-value"
            if det in res[rid]["_run_p"]:
                assert res[rid]["_run_p"][det] == row["run_p"], "inconsistent max-statistic run p-value"
            res[rid][pair]["score"][det] = score
            res[rid][pair]["p"][det] = row["p"]
            res[rid]["_run_p"][det] = row["run_p"]
        assert len(seen) == 3000, "missing gate pair scores"
    return gt, res


def wilson(events):
    x = np.asarray(events, float)
    n, ph, z = len(x), x.mean(), 1.96
    center = (ph + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [float(center - half), float(center + half)]


def surrogate_p(res, gt, det):
    maxima = {rid: max(res[rid][p]["score"][det] for p in PAIRS) for rid in res}
    reference = {f: [rid for rid, g in gt.items() if g["condition"] == f and
                     g.get("hard_negative") in (None, "common_shock")] for f in "AB"}
    out = {}
    for rid, g in gt.items():
        family = {"A": "A", "C": "A", "B": "B", "D": "B"}[g["condition"]]
        null = np.array([maxima[q] for q in reference[family] if q != rid])
        out[rid] = (1 + (null >= maxima[rid] - 1e-12).sum()) / (1 + len(null)) if len(null) else 1.0
    return out


def auroc(positive, negative):
    # Independent pair-comparison estimator; the original uses sklearn's ranks.
    diff = np.asarray(positive)[:, None] - np.asarray(negative)
    return float(((diff > 0) + 0.5 * (diff == 0)).mean())


def summarize(res, gt):
    groups = {}
    for rid, g in gt.items():
        key = g["condition"] + (f"+{g['hard_negative']}" if g.get("hard_negative") not in (None, "common_shock") else "")
        groups.setdefault(key, []).append(rid)
    metrics, counts = {}, {}
    for det in DETS:
        maxima = {rid: max(res[rid][p]["score"][det] for p in PAIRS) for rid in res}
        top = {rid: max(PAIRS, key=lambda p: res[rid][p]["score"][det]) for rid in res}
        sp = surrogate_p(res, gt, det)
        metrics[det], counts[det] = {}, {}
        for key, rids in groups.items():
            m, count = {"n": len(rids)}, {}
            events = {"surrogate_flag": [sp[r] < ALPHA for r in rids]}
            if det in P_DETS:
                events["flag"] = [res[r]["_run_p"][det] < ALPHA for r in rids]
            for name, e in events.items():
                m[name + "_rate"], m[name + "_ci"] = float(np.mean(e)), wilson(e)
                count[name] = sum(map(int, e))
            if key[0] in "CD":
                e = [top[r] == "".join(sorted(gt[r]["assigned_pair"])) for r in rids]
                m["top1"], m["top1_ci"] = float(np.mean(e)), wilson(e)
                count["top1"] = sum(map(int, e))
            if "+" in key and gt[rids[0]].get("hn_pair"):
                e = [top[r] == "".join(sorted(gt[r]["hn_pair"])) for r in rids]
                m["hn_pair_top1"] = float(np.mean(e))
                count["hn_pair_top1"] = sum(map(int, e))
            metrics[det][key], counts[det][key] = m, count
        pos = [maxima[r] for k in ("C", "D") for r in groups[k]]
        clean = [maxima[r] for k in ("A", "B") for r in groups[k]]
        all_neg = [maxima[r] for k in groups if k[0] in "AB" for r in groups[k]]
        metrics[det]["auroc_CD_vs_AB"] = auroc(pos, clean)
        metrics[det]["auroc_CD_vs_all_neg"] = auroc(pos, all_neg)
    return metrics, counts


def compare_saved(actual, expected):
    """All keys must match; AUROC ranks can differ in the final float bit."""
    assert actual.keys() == expected.keys(), "gate metric key mismatch"
    n = 0
    max_error = 0.0
    for k, a in actual.items():
        e = expected[k]
        if isinstance(a, dict):
            count, error = compare_saved(a, e)
            n += count
            max_error = max(max_error, error)
        else:
            av, ev = np.asarray(a), np.asarray(e)
            assert av.shape == ev.shape and np.isfinite(av).all() and np.isfinite(ev).all(), k
            error = float(np.max(np.abs(av - ev)))
            assert error <= 1e-14, (k, a, e)
            n += av.size
            max_error = max(max_error, error)
    return int(n), max_error


def replay(ev):
    gt, res = load_inputs(ev)
    saved = ev.json("q14", "results/eval/gate_test.json")
    assert saved["args"] == {"cmd": "both", "name": "gate_test", "n": 50, "T": 100,
                              "strength": 0.6, "type": "signal", "seed": 1001, "B": 200, "no_hn": False}
    metrics, counts = summarize(res, gt)
    n_metrics, error = compare_saved(metrics, saved["metrics"])
    # Rates and Wilson intervals are bit-identical; only rank-vs-comparison
    # AUROCs may differ by the final floating-point bit.
    for det in DETS:
        for key, value in metrics[det].items():
            if not key.startswith("auroc_"):
                assert value == saved["metrics"][det][key], (det, key)
    return {"q14_commit": ev.manifest["projects"]["q14"]["commit"],
            "n_games": len(gt), "n_detectors": len(DETS), "n_pair_score_rows": 27000,
            "group_sizes": dict(Counter(g["condition"] + (f"+{g['hard_negative']}" if g["hard_negative"] not in (None, "common_shock") else "") for g in gt.values())),
            "alpha": ALPHA, "shift_null_draws_archived": 200,
            "saved_numeric_fields_checked": n_metrics, "max_absolute_summary_error": error,
            "saved_result_matches": True,
            "saved_non_auroc_fields_match_exactly": True,
            "scope": "Reaggregation of archived pair scores and max-statistic run p-values, same-shock-family "
                     "surrogate ranking with leave-one-out controls, flags, Wilson intervals, localisation and AUROCs. "
                     "No score/trajectory or null-draw regeneration, ground-truth validation, tuning, simulations, "
                     "model calls or new held-out evaluation.",
            "metrics": metrics, "event_counts": counts}


if __name__ == "__main__":
    result = replay(Evidence())
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Q1.4 scripted gate replay: {result['n_games']} games, {result['n_pair_score_rows']} cached rows; "
          f"{result['saved_numeric_fields_checked']} fields match (max error {result['max_absolute_summary_error']})")
