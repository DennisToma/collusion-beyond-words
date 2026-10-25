"""Headline Figure 1 of TEMPLATE_REPORT.md (+ IMAGE.png = panel a). Plots pinned source data only; no model calls.
uv run python scripts/fig0_headline.py  ->  figures/fig0_headline.png, IMAGE.png

(a) One real channel game and one real no-channel game from Q2.2's fresh replication (llm_v3rep, gpt-6-luna,
    12 rounds). Selection rule (fixed, not cherry-picked): within each arm, the run whose designated-pair premium
    (pair mean price minus rival mean price, all rounds) is the arm median (lower median if n is even).
(b) Run AUROC [95% CI] of a price-level screen, pCMI and a text-reading LLM auditor, wherever each was evaluated.
"""
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from evidence import Evidence, ROOT

BLUE, ORANGE, RED, GREY, INK = "#2a78d6", "#d86226", "#c0392b", "#8996a8", "#23334b"
ev = Evidence()

# ---------- (a) data
gt = {g["run_id"]: g for g in map(json.loads, ev.lines("q22", "data/llm_v3rep/ground_truth.jsonl"))}
runs = {}
for r in map(json.loads, ev.lines("q22", "data/llm_v3rep/trajectories.jsonl")):
    runs.setdefault(r["run_id"], []).append(r)


def series(rid):
    rows = sorted(runs[rid], key=lambda r: r["round"])
    pair = gt[rid]["assigned_pair"]
    p = np.array([[np.mean([a["price"] for a in r["agents"] if a["id"] in pair]),
                   np.mean([a["price"] for a in r["agents"] if a["id"] not in pair])] for r in rows])
    cost = [r["market"]["cost"] for r in rows]
    return p, cost


def median_run(cond):
    ids = sorted(rid for rid, g in gt.items() if g["condition"] == cond)
    prem = sorted((float(np.mean(series(rid)[0][:, 0] - series(rid)[0][:, 1])), rid) for rid in ids)
    return prem[(len(prem) - 1) // 2]


picked = {cond: median_run(cond) for cond in ("private", "none")}


def draw_a(axes, fs=13):
    for ax, cond, title in zip(axes, ("private", "none"),
                               ("Private channel offered to the pair", "No private channel")):
        prem, rid = picked[cond]
        p, cost = series(rid)
        x = np.arange(1, len(p) + 1)
        ax.plot(x, p[:, 0], "-o", color=BLUE, lw=2.6, ms=6, label="designated pair (mean of 2)")
        ax.plot(x, p[:, 1], "-s", color=GREY, lw=2.2, ms=5, label="the two rivals (mean)")
        ax.set_title(f"{title}\n(run {rid[-4:]}; pair premium {prem:+.1f})", fontsize=fs, loc="left")
        ax.set_xlabel("round", fontsize=fs)
        ax.set_xlim(.5, len(p) + .5)
        ax.set_xticks([1, 4, 8, 12])
        ax.set_ylim(10, 18)
        ax.tick_params(labelsize=fs - 1)
        ax.spines[["top", "right"]].set_visible(False)
        assert len(set(cost)) >= 1
    axes[0].set_ylabel("price (unit cost 5–8, same for all sellers)", fontsize=fs - 1)
    axes[0].legend(loc="upper left", bbox_to_anchor=(0, 1.0), fontsize=fs - 2, frameon=False)


# ---------- (b) data (all values read from pinned JSON)
claims = ev.json("q14", "results/eval/claims_denominators.json")
partc = ev.json("q14", "results/eval/p2_partc.json")
main = [partc[s["set"]] for s in claims["sets"] if s["group"] == "main"]
grid = ev.json("q14", "results/eval/e70_grid.json")["pooled_auroc"]
test = ev.json("q22", "results/analysis/final_llm_v3_gpt-6.1-sol_test.json")["point_ci"]
SALT = (0.87, 0.83, 0.91)  # Q2.2 P2.0 results/analysis/p2_say_vs_do.md (SUBMISSION Table 2; bound in SOURCES)

groups = []  # (label, [(kind, pt, lo, hi)])
lvl = [r["auroc_market_level"] for r in main]
pc = [r["auroc_pcmi"] for r in main]
groups.append(("Prices only:\n9 seller sets,\n7 models\n(median, dots = sets)",
               [("level", float(np.median(lvl)), None, None, lvl), ("pcmi", float(np.median(pc)), None, None, pc)]))
groups.append(("Prices + public\nboard: 192-game\nfactorial grid",
               [("level", grid["market_level"]["auroc"], *grid["market_level"]["ci"], None),
                ("pcmi", grid["pcmi"]["auroc"], *grid["pcmi"]["ci"], None)]))
groups.append(("Say-vs-do market:\nlocked test, 95 runs\n(blue = pair premium,\nchosen post hoc)",
               [("level", test["premium"]["run_auroc"][0], *test["premium"]["run_auroc"][1:], None),
                ("text", *test["text"]["run_auroc"], None)]))
groups.append(("External task\n(different):\nSALT-NLP peer\nverification", [("text", *SALT, None)]))
color = {"level": BLUE, "pcmi": ORANGE, "text": RED}
name = {"level": "price-level screen", "pcmi": "co-movement (pCMI)", "text": "LLM text auditor"}


def draw_b(ax, fs=13):
    w, seen = .26, set()
    for gi, (lab, bars) in enumerate(groups):
        offs = (np.arange(len(bars)) - (len(bars) - 1) / 2) * w
        for (kind, pt, lo, hi, dots), o in zip(bars, offs):
            ax.bar(gi + o, pt, w * .92, color=color[kind], label=None if kind in seen else name[kind])
            seen.add(kind)
            if lo is not None:
                ax.plot([gi + o] * 2, [lo, hi], color=INK, lw=1.6)
            if dots:
                ax.scatter(gi + o + np.linspace(-.08, .08, len(dots)), dots, s=14, color=INK, zorder=3)
            ax.text(gi + o, (hi if hi else max(dots) if dots else pt) + .02, f"{pt:.2f}", ha="center",
                    fontsize=fs - 2, color=INK)
    ax.axhline(.5, color=GREY, ls="--", lw=1)
    ax.text(-.45, .49, "chance", fontsize=fs - 2, color=GREY, va="top", ha="left")
    ax.set_xticks(range(len(groups)), [g[0] for g in groups], fontsize=fs - 2)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("AUROC (1 = perfect ranking, 0.5 = chance)", fontsize=fs - 1)
    ax.tick_params(axis="y", labelsize=fs - 1)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 1.0), ncol=3, frameon=False, fontsize=fs - 2)
    ax.spines[["top", "right"]].set_visible(False)


fig = plt.figure(figsize=(17, 7))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.9], wspace=.28)
a1, a2 = fig.add_subplot(gs[0]), fig.add_subplot(gs[1], sharey=None)
draw_a([a1, a2])
b = fig.add_subplot(gs[2])
draw_b(b)
fig.text(.01, .97, "(a) Two real 12-round games (gpt-6-luna; median run per arm)", fontsize=14, weight="bold")
fig.text(.47, .97, "(b) Which signal separates channel from no-channel games?", fontsize=14, weight="bold")
fig.subplots_adjust(left=.045, right=.985, top=.78, bottom=.2)
fig.savefig(ROOT / "figures" / "fig0_headline.png", dpi=150)

img = plt.figure(figsize=(16, 9), dpi=100)
i1, i2 = img.subplots(1, 2, sharey=True)
draw_a([i1, i2], fs=20)
img.suptitle("A private channel shows up as a price gap: the pair prices above its rivals",
             fontsize=26, weight="bold", x=.5, y=.97)
img.subplots_adjust(left=.07, right=.95, top=.78, bottom=.11, wspace=.22)
img.savefig(ROOT / "IMAGE.png", dpi=100)
print(json.dumps({k: v for k, v in picked.items()}), [(g[0].split(chr(10))[0], [(b_[0], round(b_[1], 3)) for b_ in g[1]]) for g in groups])
