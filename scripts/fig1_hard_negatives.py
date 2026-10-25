"""Adapted from collusion-14-infotheory/experiments/plot_sweeps.py:hard_negatives (readability only:
larger fonts, legend moved out of the bars; same data, groups, detectors, colours and layout).
uv run python scripts/fig1_hard_negatives.py  ->  figures/fig1_scripted_hard_negatives.png
Reads the pinned Q1.4 results/eval/gate_test.json (locked seed 1001); no experiments or model calls."""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from evidence import Evidence, ROOT

DETS = [("pearson", "|Pearson|", "#9e9e9e"), ("mi", "MI", "#1f77b4"), ("cmi_state", "CMI | state", "#2ca02c"),
        ("pcmi", "pCMI (CMI | state + lags)", "#d62728"), ("te", "lagged CMI (TE)", "#9467bd")]
GROUPS = ["A", "B", "A+independent_high_price", "A+legit_cooperation", "A+shared_policy",
          "B+shared_policy", "A+shared_seed", "B+shared_seed", "C", "D"]
LABELS = ["A indep.", "B common\nshock", "indep.\nhigh-price", "leader-\nfollower", "shared\npolicy\n(indep.\nnoise)",
          "shared\npolicy\n+ common\nshock", "shared\npolicy\n+ shared\nseed", "shared\nseed\n+ common\nshock",
          "C\ncollusion", "D\ncollusion\n+ common\nshock"]

m = Evidence().json("q14", "results/eval/gate_test.json")["metrics"]
plt.rcParams.update({"font.size": 12})
fig, axes = plt.subplots(2, 1, figsize=(12, 8.6), sharex=True)
w = 0.8 / len(DETS)
for ax, (pre, null) in zip(axes, [("", "within-run circular-shift null"),
                                  ("surrogate_", "control-surrogate null (no-channel reference markets)")]):
    for k, (det, lab, col) in enumerate(DETS):
        ys = [m[det][g][pre + "flag_rate"] for g in GROUPS]
        lo = [ys[i] - m[det][g][pre + "flag_ci"][0] for i, g in enumerate(GROUPS)]
        hi = [m[det][g][pre + "flag_ci"][1] - ys[i] for i, g in enumerate(GROUPS)]
        ax.bar(np.arange(len(GROUPS)) + (k - 2) * w, ys, w, yerr=[lo, hi], color=col, label=lab, capsize=2,
               error_kw={"lw": 1})
    ax.axhline(0.05, color="k", lw=0.8, ls="--")
    ax.axvline(7.5, color="k", lw=0.8)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("runs flagged at α = 0.05")
    ax.set_title(null, fontsize=13)
    ax.spines[["top", "right"]].set_visible(False)
axes[1].set_xticks(range(len(GROUPS)))
axes[1].set_xticklabels(LABELS, fontsize=11)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 0.94), frameon=False, fontsize=12)
fig.suptitle("Scripted market, locked test seed, T = 100, strength 0.6 (n = %d runs/group, Wilson 95%% CI)\n"
             "left of vertical line = no collusion (hard negatives); right = planted collusion" % m["pcmi"]["A"]["n"],
             fontsize=13, y=0.995)
fig.subplots_adjust(top=0.85, bottom=0.13, left=0.07, right=0.99, hspace=0.2)
out = ROOT / "figures" / "fig1_scripted_hard_negatives.png"
fig.savefig(out, dpi=160, metadata={"Software": None})
print("wrote", out)
