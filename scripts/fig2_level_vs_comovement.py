"""Adapted from collusion-14-infotheory/scripts/phase2_fig.py (readability only: larger fonts; same data,
inclusion list, ordering, encodings and layout).
uv run python scripts/fig2_level_vs_comovement.py  ->  figures/fig2_level_vs_comovement_9sets.png
Reads the pinned Q1.4 results/eval/{claims_denominators,p2_partc}.json; no experiments or model calls."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from evidence import Evidence, ROOT

BLUE, ORANGE, INK = "#2a78d6", "#d86226", "#23334b"
ev = Evidence()
claims = ev.json("q14", "results/eval/claims_denominators.json")
partc = ev.json("q14", "results/eval/p2_partc.json")
ss = [s for s in claims["sets"] if s["group"] == "main"]
rows = [partc[s["set"]] for s in ss]
labels = [f"{r['label']}\nT={r['T']}; n={r['n_A']} + {r['n_C']}" for r in rows]
claim = {c["claim"]: c for c in claims["claims"] if c["group"] == "main"}
plt.rcParams.update({"font.size": 13})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8.6), sharey=True, gridspec_kw={"width_ratios": [1, 1.25]})
y = np.arange(len(rows))
for i, r in enumerate(rows):
    ax1.plot(r["C_minus_A_ci"], [i, i], color=INK, lw=2.2)
    ax1.plot(r["C_minus_A_markup"], i, "o", color=INK, ms=7)
    for metric, offset, color, marker in (("market_level", -.14, BLUE, "o"), ("pcmi", .14, ORANGE, "s")):
        ax2.plot(r[f"auroc_{metric}_ci"], [i + offset] * 2, color=color, lw=2)
        ax2.plot(r[f"auroc_{metric}"], i + offset, marker, color=color, ms=7,
                 label={"market_level": "Market-level markup", "pcmi": "pCMI"}[metric] if i == 0 else None)
    if i % 2 == 0:
        for ax in (ax1, ax2):
            ax.axhspan(i - .48, i + .48, color="#f3f6fa", zorder=-1)
ax1.axvline(0, color="#8996a8", ls="--", lw=1)
ax2.axvline(.5, color="#8996a8", ls="--", lw=1)
ax1.set_yticks(y, labels, fontsize=12)
ax1.set_ylim(len(rows) - .5, -.5)
ax1.set_xlabel("Channel − no-channel markup [95% CI]", fontsize=13)
ax2.set_xlabel("Run AUROC [95% CI]; 0.5 = chance", fontsize=13)
ax2.set_xlim(0, 1.02)
ax1.set_title(f"(a) Positive channel effect: {claim['premium']['k']}/{claim['premium']['K']} sets",
              fontsize=14, loc="left", pad=15)
ax2.set_title(f"(b) Level beats pCMI: {claim['level_beats_pcmi']['k']}/{claim['level_beats_pcmi']['K']} sets",
              fontsize=14, loc="left", pad=15)
ax2.legend(loc="lower left", bbox_to_anchor=(0, 1.045), ncol=2, frameon=False, fontsize=12)
for ax in (ax1, ax2):
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=12)
    ax.grid(axis="x", color="#dce3ed", lw=.7)
    ax.set_axisbelow(True)
fig.text(.02, .025, "Frozen P2.13 main sets; channel assignment is the target, not verified execution.\n"
         "Sets share designs/models; these are not nine independent replications.\n"
         "Base Qwen3.6 is the pCMI exception. Executed-only and strong-framing results are reported separately (P2.11).",
         fontsize=11, color=INK)
fig.subplots_adjust(left=.335, right=.98, bottom=.17, top=.9, wspace=.16)
out = ROOT / "figures" / "fig2_level_vs_comovement_9sets.png"
fig.savefig(out, dpi=160, facecolor="white", metadata={"Software": None})
plt.close(fig)
print("wrote", out)
