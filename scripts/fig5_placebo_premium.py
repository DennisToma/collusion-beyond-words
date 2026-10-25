"""Adapted from collusion-22-say-vs-do/placebo.py (figure block only; readability: larger fonts and canvas;
same data, arms, bootstrap (seed 0, 2000 draws, percentile 95% band), colours and layout).
uv run python scripts/fig5_placebo_premium.py  ->  figures/fig5_placebo_premium.png
Reads pinned Q2.2 data/{llm_v3plc,llm_v3rep}/{ground_truth,trajectories}.jsonl; asserts the per-round means
equal the saved results/analysis/placebo_llm_v3plc.json `per_round_mean`. No experiments or model calls."""
import json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from evidence import Evidence, ROOT

AG = ["A", "B", "C", "D"]
PLC, REP = "llm_v3plc", "llm_v3rep"
ev = Evidence()


def load(ds):
    gt = {r["run_id"]: r for r in map(json.loads, ev.lines("q22", f"data/{ds}/ground_truth.jsonl"))}
    P = {}
    for r in map(json.loads, ev.lines("q22", f"data/{ds}/trajectories.jsonl")):
        P.setdefault(r["run_id"], {})[r["round"]] = {x["id"]: x["price"] for x in r["agents"]}
    per_round = {}
    for rid, d in P.items():
        pair = gt[rid]["assigned_pair"]; o = [a for a in AG if a not in pair]
        per_round[rid] = np.array([np.mean([d[t][a] for a in pair]) - np.mean([d[t][a] for a in o]) for t in sorted(d)])
    return gt, per_round


gp, rp = load(PLC); gr, rr = load(REP)
plc = sorted(gp); assert all(gp[r]["condition"] == "placebo" for r in plc)
mate = {r: f"{REP}_{r.rsplit('_', 1)[1]}" for r in plc}
for r in plc:
    g = gr[mate[r]]
    assert g["condition"] == "private" and g["seed"] == gp[r]["seed"] and g["assigned_pair"] == gp[r]["assigned_pair"]
none = sorted(r for r in gr if gr[r]["condition"] == "none")
arms = (("private", "private (channel delivered)", rr, [mate[r] for r in plc], "#c0392b"),
        ("placebo", "placebo (offered, never delivered)", rp, plc, "#2471a3"),
        ("none", "none (no channel)", rr, none, "#7f8c8d"))
saved = ev.json("q22", "results/analysis/placebo_llm_v3plc.json")["per_round_mean"]
for key, _, v, ids, _ in arms:
    got = [round(float(x), 3) for x in np.array([v[r] for r in ids]).mean(0)]
    assert got == saved[key], (key, got, saved[key])

plt.rcParams.update({"font.size": 13})
fig, ax = plt.subplots(figsize=(8.4, 5.0))
for _, k, v, ids, col in arms:
    M = np.array([v[r] for r in ids]); m = M.mean(0)
    rng = np.random.default_rng(0); B = np.array([M[rng.integers(0, len(M), len(M))].mean(0) for _ in range(2000)])
    x = np.arange(1, 13)
    ax.plot(x, m, marker="o", ms=5, lw=2, color=col, label=f"{k}, n={len(ids)}")
    ax.fill_between(x, np.percentile(B, 2.5, 0), np.percentile(B, 97.5, 0), color=col, alpha=.15, lw=0)
ax.axhline(0, color="k", lw=.6)
ax.set_xticks(range(1, 13))
ax.set_xlabel("round"); ax.set_ylabel("designated-pair premium (price units)")
ax.set_title("Pair premium: real vs placebo private channel (llm_v3rep seeds)", fontsize=14)
ax.legend(fontsize=12, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
out = ROOT / "figures" / "fig5_placebo_premium.png"
fig.savefig(out, dpi=150, metadata={"Software": None})
plt.close(fig)
print("wrote", out)
