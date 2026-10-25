"""Recompute unrounded values behind three Q2.2 numbers whose saved JSON is rounded to 3 dp on a tie
(x.xx5), so printing them at 2 dp would double-round. Uses Q2.2's own functions, seeds and cached data,
with only the round(..., 3) removed; no model calls. Reads the Q2.2 (and Q1.4) checkouts, writes only
results/unrounded_q22.json in this repo. check_sources.py then requires round(raw, 3) to equal the pinned
saved values and binds the printed numbers to the unrounded ones.

    PYTHONDONTWRITEBYTECODE=1 ~/collusion/collusion-22-say-vs-do/.venv/bin/python scripts/recompute_unrounded_q22.py

M6  E113 Qwen executed-only combined - action (p2_e113_secondary / p2_e1_audit.stratified_delta)
M33 Qwen3.8-base Spearman text vs invite rate, within no-channel (p2_e132_inversion.boot_spearman)
M34 Fig. 6 action view strict-executed vs tacit-high AUROC (p2_strong_eval.auroc; exact fraction)
"""
import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent.parent / "results" / "unrounded_q22.json"
Q22 = Path(os.environ.get("BW_Q22_ROOT", str(Path.home() / "collusion" / "collusion-22-say-vs-do")))
os.environ.setdefault("Q22_SIB", str(Path.home() / "collusion" / "collusion-14-infotheory"))
sys.dont_write_bytecode = True
sys.path.insert(0, str(Q22))
os.chdir(Q22)

import p2_e1_audit as A  # noqa: E402
import p2_e113_secondary as S2  # noqa: E402
import p2_e132_inversion as M  # noqa: E402
from p2_cue import auc  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402


def stratified_delta(rows, cids, a, b, B=2000):  # p2_e1_audit.stratified_delta without round(., 3)
    sub = {c: [x for x in rows if x["cell"] == c and a in x and b in x] for c in cids}
    sub = {c: R for c, R in sub.items() if {x["y"] for x in R} == {0, 1}}

    def md(S):
        d = []
        for R in S.values():
            neg = [x for x in R if x["y"] == 0]
            pos = [x for x in R if x["y"] == 1]
            d.append(auc([x[a] for x in neg], [x[a] for x in pos]) - auc([x[b] for x in neg], [x[b] for x in pos]))
        return float(np.mean(d))
    rng = np.random.default_rng(0)
    split = {c: ([x for x in R if x["y"] == 0], [x for x in R if x["y"] == 1]) for c, R in sub.items()}
    boots = []
    for _ in range(B):
        boots.append(md({c: [n[i] for i in rng.integers(0, len(n), len(n))] + [q[i] for i in rng.integers(0, len(q), len(q))]
                         for c, (n, q) in split.items()}))
    return [md(sub), float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))], len(sub)


def boot_spearman(x, y, B=2000):  # p2_e132_inversion.boot_spearman without round(., 3)
    x, y = np.asarray(x, float), np.asarray(y, float)
    rng = np.random.default_rng(0)
    b = []
    for _ in range(B):
        i = rng.integers(0, len(x), len(x))
        if np.ptp(x[i]) > 0 and np.ptp(y[i]) > 0:
            b.append(spearmanr(x[i], y[i])[0])
    return [float(spearmanr(x, y)[0]), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5)), len(x)]


out = {"q22_commit": subprocess.check_output(["git", "-C", str(Q22), "rev-parse", "HEAD"]).decode().strip()}

# M6 (e113_secondary.json : stratified.executed_vs_A.qwen_combined_minus_action)
games = {g["run_id"]: g for g in json.loads((S2.SNAP / "e70_grid.json").read_bytes())["games"]}
labs, S = A.load()
C = A.cells()
rows = []
for r, lab in labs.items():
    g, model = games[r], C[lab["cell"]]["levels"]["model"]
    x = {"cell": lab["cell"], "y": int(lab["channel"]), "executed": bool(g["executed"]) if lab["channel"] else None}
    for v in A.VIEWS:
        if v == "text" and not model.startswith("qwen"):
            continue
        if r in S[v] and S[v][r].get("collusion_present") is not None:
            x[v] = float(S[v][r]["collusion_present"])
    rows.append(x)
qids = sorted(c for c in C if C[c]["levels"]["model"].startswith("qwen"))
m6, n_cells = stratified_delta([x for x in rows if not x["y"] or x["executed"]], qids, "combined", "action")
out["M6_qwen_executed_combined_minus_action"] = {"value": m6, "n_cells": n_cells}

# M33 (e132_inversion.json : sets."Qwen3.8 base".spearman_text_vs_invite_rate_within_no_channel)
M.boot_spearman = boot_spearman
out["M33_qwen38_base_within_no_channel"] = {"value": M.one(M.SETS["Qwen3.8 base"])
                                            ["spearman_text_vs_invite_rate_within_no_channel"]}

# M34 (p2_strong_eval_llm_p2strongF.json : detectors.action.auroc_strict_vs_tacit_high[0])
ds = "llm_p2strongF"
cl = json.load(open(f"results/analysis/p2_strong_classes_{ds}.json"))["runs"]
sc = {x["run_id"]: x["collusion_present"] for x in map(json.loads, open(f"results/llm_auditor/{ds}/gpt-6.1-sol/action_orig.jsonl"))}
p = [sc[r] for r, c in cl.items() if c["class"] == "executed"]
n = [sc[r] for r, c in cl.items() if c["class"] == "tacit_high"]
fr = sum(Fraction(2 * (a > b) + (a == b), 2) for a in p for b in n) / (len(p) * len(n))
out["M34_action_strict_vs_tacit_high"] = {"value": float(fr), "fraction": f"{fr.numerator}/{fr.denominator}",
                                          "n_strict": len(p), "n_tacit_high": len(n)}

OUT.write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
