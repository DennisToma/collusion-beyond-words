"""Adapted from collusion-14-infotheory/scripts/e70_fig.py (readability only: larger fonts; same data,
ordering, encodings and layout).
uv run python scripts/fig3_e70_grid.py  ->  figures/fig3_e70_grid.png
Reads the pinned Q1.4 results/eval/e70_grid.json; no experiments or model calls."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from evidence import Evidence, ROOT

BLUE, ORANGE, INK, MUTED = "#2a78d6", "#eb6834", "#222222", "#888888"
r = Evidence().json("q14", "results/eval/e70_grid.json")
plt.rcParams.update({"font.size": 12})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw=dict(width_ratios=[1, 1.6]))

me = r["main_effects"]
fs = sorted(me, key=lambda f: me[f]["effect"])
for i, f in enumerate(fs):
    v = me[f]
    ax1.plot(v["ci"], [i, i], color=BLUE, lw=2, solid_capstyle="round")
    ax1.plot(v["effect"], i, "o", color=BLUE, ms=8, mec="white", mew=2)
ax1.axvline(0, color=MUTED, lw=1, ls="--")
ax1.set_yticks(range(len(fs)), [f"{f}\n{me[f]['low']} → {me[f]['high']}" for f in fs], fontsize=11)
ax1.set_xlabel("main effect on C − A markup\n(high − low level)")
p = r["primary"]
ax1.set_title(f"(a) factor main effects\npooled C − A {p['pooled_C_minus_A']:+.2f} "
              f"[{p['pooled_ci'][0]:.2f}, {p['pooled_ci'][1]:.2f}], {p['cells_d_pos']}/{p['cells']} cells > 0",
              fontsize=12, loc="left")

pc = r["per_cell"]
cs = sorted(pc, key=lambda c: pc[c]["d"])
x = range(len(cs))
ax2.axhline(.5, color=MUTED, lw=1, ls="--")
ax2.plot([i - .15 for i in x], [pc[c]["auroc"]["market_level"] for c in cs], "o", color=BLUE, ms=8, mec="white", mew=2,
         label="market-level markup")
ax2.plot([i + .15 for i in x], [pc[c]["auroc"]["pcmi"] for c in cs], "s", color=ORANGE, ms=8, mec="white", mew=2,
         label="pCMI")
ax2.set_xticks(list(x), [f"{c}\n{pc[c]['d']:+.1f}" for c in cs], fontsize=9.5)
ax2.set_xlabel("cell (ordered by C − A markup, shown below the cell id)")
ax2.set_ylabel("run AUROC, channel vs no-channel")
ax2.set_ylim(-.02, 1.02)
lv = r["level_vs_pcmi"]
ax2.set_title(f"(b) per cell (n = {pc[cs[0]]['n'][1]} + {pc[cs[0]]['n'][0]} games each)\nmarket level > pCMI in "
              f"{lv['cells_level_gt_pcmi']}/{lv['cells']} cells", fontsize=12, loc="left")
ax2.legend(frameon=False, fontsize=11, loc="lower right")
for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(colors=INK)
    ax.grid(axis="x" if ax is ax1 else "y", color="#e5e5e5", lw=.8)
    ax.set_axisbelow(True)
fig.tight_layout()
out = ROOT / "figures" / "fig3_e70_grid.png"
fig.savefig(out, dpi=150, metadata={"Software": None})
print("wrote", out)
