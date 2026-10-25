"""Check saved source values AND numbers extracted from the report and slides.

The portable evidence bundle is the default; --live reads sibling checkouts and
requires their files to match the pinned evidence hashes. Document bindings cover
selected numeric claims, not every number or the meaning of surrounding prose.
Writes results/source_check.json and exits non-zero on any mismatch.

    uv run python scripts/check_sources.py
"""
import json
import argparse
import hashlib
import sys
from pathlib import Path
from evidence import Evidence, ROOT, MANIFEST
from document_checks import check_documents

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--live", action="store_true", help="Read pinned files from the sibling checkouts")
ap.add_argument("--submission", type=Path, default=ROOT / "SUBMISSION.md")
ap.add_argument("--slides", type=Path, default=ROOT / "SLIDES.md")
ap.add_argument("--output", type=Path, default=ROOT / "results/source_check.json")
args = ap.parse_args()
evidence = Evidence(live=args.live)
Q14, Q22 = "q14", "q22"
OUT = args.output

_cache = {}


def load(repo, rel):
    p = (repo, rel)
    if p not in _cache:
        _cache[p] = evidence.json(repo, "results/" + rel)
    return _cache[p]


checks = []


def check(row, what, got, want, tol=0.005):
    if isinstance(want, (list, tuple)):
        ok = len(got) == len(want) and all(abs(g - w) <= tol + 1e-9 for g, w in zip(got, want))
    elif isinstance(want, (int, float)) and not isinstance(want, bool):
        ok = abs(got - want) <= tol + 1e-9
    else:
        ok = got == want
    checks.append({"row": row, "what": what, "got": got, "want": want, "tol": tol, "ok": bool(ok)})


# ---------------- Q1.4 ----------------
cd = {s["set"]: s for s in load(Q14, "eval/claims_denominators.json")["sets"]}
main = [s for s in cd.values() if s["group"] == "main"]
check("N1", "main sets", len(main), 9)
check("N1", "main sets with C-A CI > 0", sum(s["d_ci"][0] > 0 for s in main), 9)
e74 = load(Q14, "eval/e74_paired_diff.json")
ms = e74["main_sets"]
check("N2", "markup AUROC range", [min(v["market_level"] for v in ms.values()),
                                   max(v["market_level"] for v in ms.values())], [0.75, 0.99])
check("N2", "pCMI AUROC range", [min(v["pcmi"] for v in ms.values()),
                                 max(v["pcmi"] for v in ms.values())], [0.34, 0.72])
check("N2", "point level > pCMI", e74["summary"]["point_level_gt_pcmi"], 9)
check("N3", "level-pCMI CI > 0", e74["summary"]["k_level_minus_pcmi_ci_above_0"], 8)
check("N3", "gpt-5.6-luna level-pCMI", [ms["llm_g56l_p2"]["level_minus_pcmi"]["delta"],
                                        *ms["llm_g56l_p2"]["level_minus_pcmi"]["ci"]], [0.03, -0.27, 0.33])
check("N3", "base Qwen3.6 level-pCMI", [ms["llm_qb36_p2"]["level_minus_pcmi"]["delta"],
                                        *ms["llm_qb36_p2"]["level_minus_pcmi"]["ci"]], [0.22, 0.03, 0.44])
check("N4", "pCMI CI contains 0.5", sum(s["pcmi_ci"][0] <= 0.5 <= s["pcmi_ci"][1] for s in main), 8)
check("N4", "base Qwen3.6 pCMI", [cd["llm_qb36_p2"]["pcmi"], *cd["llm_qb36_p2"]["pcmi_ci"]], [0.71, 0.51, 0.88])
check("N9", "E70 level-pCMI", [e74["E70_pooled"]["level_minus_pcmi"]["delta"],
                               *e74["E70_pooled"]["level_minus_pcmi"]["ci"]], [0.23, 0.12, 0.33])
check("N9", "E70 level-TE", [e74["E70_pooled"]["level_minus_te"]["delta"],
                             *e74["E70_pooled"]["level_minus_te"]["ci"]], [0.12, 0.01, 0.22])
check("N20", "level-TE CI > 0", e74["summary"]["k_level_minus_te_ci_above_0"], 6)
check("N20", "deepseek TE", ms["llm_ds_p2"]["te"], 0.81)
check("N20", "base Qwen3.8 TE", ms["llm_qb_p2"]["te"], 0.91)

g = load(Q14, "eval/gate_test.json")["metrics"]
check("N13", "MI flags common shock (B)", g["mi"]["B"]["flag_rate"], 1.0)
check("N13", "pCMI common shock, shift null", g["pcmi"]["B"]["flag_rate"], 0.14)
check("N13", "pCMI shared policy + shock, surrogate", [g["pcmi"]["B+shared_policy"]["surrogate_flag_rate"],
                                                       *g["pcmi"]["B+shared_policy"]["surrogate_flag_ci"]],
      [0.04, 0.01, 0.13])
check("N24", "TE shared policy (A, B)", [g["te"]["A+shared_policy"]["flag_rate"],
                                         g["te"]["B+shared_policy"]["flag_rate"]], [0.90, 0.98])
check("N24", "TE independent high price", g["te"]["A+independent_high_price"]["flag_rate"], 0.62)
check("N13", "TE legit leader-follower", g["te"]["A+legit_cooperation"]["flag_rate"], 1.0)

ca = load(Q14, "p2/costasym_test.json")["summaries"]["A/costasym"]
check("N14", "level false flags /30", round(ca["market_level_surrogate_flag"]["rate"] * ca["n"]), 30)
check("N14", "pCMI flags /30", round(ca["pcmi_flag"]["rate"] * ca["n"]), 4)

mc = load(Q14, "eval/e68_cda.json")["manipulation_check"]
check("N18", "E68 ask effect", [mc["diff"], *mc["ci"]], [0.39, 0.06, 0.69])
check("N18", "E68 verdict", load(Q14, "eval/e68_cda.json")["verdict"], "inconclusive")

sc = load(Q14, "reimpl/compare.json")["scores"]
check("N19", "reimpl cells agreeing < 1e-9", [sum(int(v["n_agree_1e9"]) for v in sc.values()),
                                              sum(int(v["n"]) for v in sc.values())], [422, 424], tol=0)

spill = [cd[k] for k in ("llm_v1", "llm_long_p2_T60", "llm_strong_qa")]
check("N25", "pair_level range (spillover sets)", [min(s["pl"] for s in spill), max(s["pl"] for s in spill)],
      [0.75, 0.80])
check("N25", "market level range (spillover sets)", [min(s["ml"] for s in spill), max(s["ml"] for s in spill)],
      [0.85, 0.94])

e72 = load(Q14, "eval/e72_te_diag.json")["c_execution"]
check("N27", "E72 non-executed n / judged yes / no", [e72["not_executed"]["n_C"],
                                                      e72["not_executed"]["judge_agreement_yes"],
                                                      e72["not_executed"]["judge_agreement_no"]], [52, 38, 14], tol=0)
check("N27", "E72 executed n", e72["executed"]["n_C"], 44, tol=0)
check("N12", "E72 TE non-exec vs exec", [e72["not_executed"]["auroc"], e72["executed"]["auroc"]], [0.73, 0.49])
es = load(Q14, "eval/executed_sensitivity.json")
check("N28", "executed n range", es["n_executed_range"], [13, 78], tol=0)
check("N28", "pooled pCMI range", es["pooled_pcmi_range"], [0.343, 0.531], tol=0.0005)

# ---------------- Q2.2 ----------------
pr = load(Q22, "analysis/p2_pool_rep.json")
d = pr["condition_label"]["contrasts"]["delta_hybrid[combined]"]
check("M2", "pooled fresh combined - better single", [d["delta"], *d["ci"]], [-0.07, -0.17, 0.02])
check("M2", "pooled n", pr["n"], 90, tol=0)
inv = load(Q22, "analysis/e132_inversion.json")["sets"]["Qwen3.8 base"]["arms"]
check("M5", "invite rate channel / control", [inv["channel"]["invite_rate_pooled"],
                                              inv["no_channel"]["invite_rate_pooled"]], [0.40, 0.88])
ee = load(Q22, "analysis/e133e_attr.json")
check("M12", "no-chat LLM vs rule score", [ee["b_raw_auroc"]["llm_E133d"][0], ee["b_raw_auroc"]["rule_score"][0]],
      [0.94, 0.885], tol=0.0025)
check("M12", "LLM - rule score", ee["b_llm_E133d_minus_raw"]["rule_score"], [0.06, 0.02, 0.10])
check("M12", "say-do gap / pair SD", [ee["a_oriented_auroc_smaller_is_held"]["say_do_gap"][0],
                                      ee["a_oriented_auroc_smaller_is_held"]["pair_sd_0_5"][0]], [0.77, 0.855],
      tol=0.0005)
rs = load(Q22, "analysis/p2_replace_sol.json")["arms"]["private"]
check("M16", "sol newcomer re-agrees", rs["O4_reagreement_floor_ge13"]["repl"], [0, 20], tol=0)
check("M16", "market >= Nash+2", rs["O6_market_excess_ge2"]["repl"], [18, 20], tol=0)
pl = load(Q22, "analysis/placebo_llm_v3plc.json")["windows"]["r2_12"]["placebo_minus_private_paired"]
check("M19", "placebo - private r2-12", pl, [0.03, -0.54, 0.49])

se = load(Q22, "analysis/p2_strong_eval_llm_p2strongF.json")["detectors"]
pv = [se[k]["auroc_strict_vs_tacit_high"] for k in ("premium", "market_excess_nash", "action", "action_stats")]
# Three Q2.2 values are stored at 3 dp on a tie (action 0.575, -0.165, -0.405). Their unrounded values come from
# scripts/recompute_unrounded_q22.py (portable replay of Q2.2's estimators) -> results/unrounded_q22.json;
# each must round to the pinned stored value, and the printed numbers are checked against the unrounded ones.
# The release tests delete and regenerate this file from the pinned inputs, requiring byte equality.
unr = json.loads((ROOT / "results/unrounded_q22.json").read_text())
act = unr["M34_action_strict_vs_tacit_high"]
check("M34", "action view unrounded matches stored 3 dp", round(act["value"], 3), se["action"]["auroc_strict_vs_tacit_high"][0], tol=1e-9)
check("M34", "action view strict n, tacit-high n", [act["n_strict"], act["n_tacit_high"]], [13, 19])
pv_raw = [v[0] for v in pv]
pv_raw[2] = act["value"]
check("M34", "Fig.6 price views strict vs tacit-high: min/max point", [min(pv_raw), max(pv_raw)],
      [0.43, 0.57])
check("M34", "all price-view CIs include 0.5", all(v[1] < 0.5 < v[2] for v in pv), True)

salt = load(Q22, "analysis/salt_d1.json")["E105_audit"]["auroc_no_verdict_words"]
check("M35", "SALT no-verdict-words AUROC", [salt["est"], *salt["ci"]], [0.75, 0.66, 0.84])
check("M35", "SALT no-verdict-words n", salt["n"], 117, tol=0)

# Further headline quantities, formerly checked only by the human/source reviews.
lc = cd["llm_long_p2_T60"]
check("N5", "T60 pCMI", [lc["pcmi"], *lc["pcmi_ci"]], [0.34, 0.18, 0.52])
ex = load(Q14, "eval/p2_partc.json")["E64_pooled"]["all sets"]
check("N7", "executed pCMI", [ex["pcmi"]["executed"]["auroc"], *ex["pcmi"]["executed"]["ci"]], [0.42, 0.33, 0.53])
check("N7", "executed counts", [ex["n_executed"], ex["n_executed"] + ex["n_not_executed"]], [48, 149], tol=0)
check("N7", "executed pair-level", [ex["pair_level"]["executed"]["auroc"], *ex["pair_level"]["executed"]["ci"]], [0.87, 0.80, 0.94])
grid = load(Q14, "eval/e70_grid.json")
# e70_grid.json stores AUROCs/CIs rounded to 3 dp (market-level upper CI 0.805), so printing them at 2 dp could
# double-round. Replay Q1.4's pooled stratified AUROC and game-cluster bootstrap (scripts/e70_grid.py: rng
# default_rng(0), B = 2000, resample within cell x arm) from the saved per-game scores, require it to reproduce
# every stored 3-dp value, and check the unrounded values (market-level upper CI 0.8047 -> 0.80, not 0.81).
import numpy as np  # noqa: E402
g_by = {c: {k: [x for x in grid["games"] if x["cell"] == c and x["channel"] == k] for k in (True, False)}
        for c in grid["per_cell"]}


def grid_auroc(byc, det):
    num = den = 0.0
    for v in byc.values():
        p = np.array([x["scores"][det] for x in v[True]], float)
        q = np.array([x["scores"][det] for x in v[False]], float)
        num += (p[:, None] > q[None]).sum() + .5 * (p[:, None] == q[None]).sum()
        den += len(p) * len(q)
    return float(num / den)


g_rng = np.random.default_rng(0)
g_boot = {det: [] for det in grid["pooled_auroc"]}
for _ in range(2000):
    bb = {c: {k: [v[k][i] for i in g_rng.integers(0, len(v[k]), len(v[k]))] for k in (True, False)}
          for c, v in g_by.items()}
    for det in g_boot:
        g_boot[det].append(grid_auroc(bb, det))
for key, want in [("market_level", [0.74, 0.66, 0.80]), ("pcmi", [0.51, 0.43, 0.59]), ("te", [0.62, 0.54, 0.70])]:
    v = grid["pooled_auroc"][key]
    raw = [grid_auroc(g_by, key), *(float(np.quantile(g_boot[key], q)) for q in (.025, .975))]
    check("N8", "grid replay matches stored 3 dp " + key, [round(x, 3) for x in raw], [v["auroc"], *v["ci"]], tol=1e-9)
    check("N8", "grid " + key, raw, want)
test = load(Q22, "analysis/final_llm_v3_gpt-6.1-sol_test.json")
d = test["contrasts"]["delta_hybrid[combined]:run_auroc"]
check("M1", "locked combined - better single", [d["delta"], *d["ci"]], [-0.01, -0.09, 0.06])
check("M1", "locked n", test["n_runs"], 95, tol=0)
for key, want in [("text", [0.47, 0.36, 0.58]), ("action", [0.75, 0.65, 0.85])]:
    check("M3", "locked " + key, test["point_ci"][key]["run_auroc"], want)
classes = load(Q22, "analysis/p2_strong_classes_llm_p2strongF.json")
check("M10", "strong tacit-high count", classes["n_tacit_high_none"], [19, 20], tol=0)
check("M10", "strong strict-executed count", classes["n_strict_executed"], [13, 20], tol=0)

# Iteration 14: remaining headline decimals in tables 1-2 and sections 5.2-5.4.
lp = load(Q14, "eval/long_power_llm_long_p2_T60.json")
m60 = lp["prefix"]["60"]["pair_markup"]
check("N5", "T60 max-pair markup", [m60[0], *m60[1]], [0.94, 0.86, 1.00])
obs = lp["mde"]["60"]["observed_C_comove_excess"]
check("N6", "T60 observed co-move excess", [obs["comove_excess_mean"], *obs["ci"]], [0.004, -0.007, 0.015],
      tol=0.0005)
for T, want in [("60", [0.79, 0.70, 0.88]), ("20", [0.62, 0.52, 0.71])]:
    q = lp["mde"][T]["by_q"]["0.1"]
    check("N6", f"T{T} planted q=0.1 pCMI", [q["auroc"], *q["ci"]], want)
e73 = load(Q14, "eval/e73_nonlinear.json")["E70"]
check("N11", "E70 copula pCMI / sign CMI", [e73["copula_pcmi"]["auroc"], *e73["copula_pcmi"]["ci"],
                                            e73["sign_mi"]["auroc"], *e73["sign_mi"]["ci"]],
      [0.53, 0.44, 0.61, 0.44, 0.36, 0.52])
var = load(Q14, "eval/p2_variants.json")["arms"]
check("N16", "wording no-channel markup min/max", [min(a["A_markup"] for a in var.values()),
                                                   max(a["A_markup"] for a in var.values())], [-0.19, 2.56])
check("N21", "E70 Qwen cells max-pair markup", grid["amend2_by_model"]["qwen"]["market_level"], 0.76)
prev = load(Q14, "eval/prevalence.json")
scripted = [r for r in prev if r["setting"].startswith("scripted")]
llm_rows = [r for r in prev if r["setting"].startswith("LLM") and r["precision@0.01"] == r["precision@0.01"]]
best = max(scripted, key=lambda r: r["precision@0.01"])
check("N29", "max scripted precision@0.01", [best["precision@0.01"], *best["precision@0.01_ci"]], [0.20, 0.07, 0.54])
check("N29", "max LLM precision@0.01", max(r["precision@0.01"] for r in llm_rows), 0.19)

f3 = load(Q22, "analysis/p2_family3way.json")
for key, name, want in [("llm_p2claude", "Claude", [0.22, 0.00, 0.52, 0.52, 0.20, 0.88]),
                        ("llm_p2ds", "deepseek", [0.36, 0.20, 0.52, 0.53, 0.30, 0.74])]:
    v = f3[key]["views"]
    check("M4", f"{name} text / action", [*v["text"]["auroc_private_vs_none"], *v["action"]["auroc_private_vs_none"]],
          want)
qw = {}
for s, name, want in [("b", "Qwen3.8 base", [0.21, 0.12, 0.33, 0.86, 0.69, 0.98]),
                      ("a", "Qwen3.8 abliterated", [0.15, 0.05, 0.25, 0.57, 0.36, 0.78])]:
    det = load(Q22, f"analysis/p2_strong_eval_llm_p2qwen{s}.json")["detectors"]
    qw[s] = det["text"]["auroc_private_vs_none"][0]
    check("M4", f"{name} text / action", [*det["text"]["auroc_private_vs_none"],
                                          *det["action"]["auroc_private_vs_none"]], want)
check("M4", "Qwen3.8 text arms min/max", [min(qw.values()), max(qw.values())], [0.15, 0.21])
check("M30", "sol seller arm text", f3["llm_p2sol"]["views"]["text"]["auroc_private_vs_none"], [0.17, 0.01, 0.41])
e1 = load(Q22, "analysis/p2_e1_audit.json")
pooled = e1["pooled_auroc_channel_vs_none_descriptive"]
check("M6", "E113 Qwen text", pooled["text_qwen"], [0.32, 0.24, 0.42])
check("M6", "E113 Qwen LLM action", pooled["action_qwen"], [0.52, 0.41, 0.64])
a3 = e1["amend3"]
for key, name, want in [("qwen_stratified_combined_minus_action", "Qwen combined - action", [-0.24, -0.37, -0.09]),
                        ("luna_stratified_combined_minus_action_noise", "luna combined - action", [0.07, -0.02, 0.17])]:
    check("M6", name, [a3[key]["delta"], *a3[key]["ci"]], want)
sec = load(Q22, "analysis/e113_secondary.json")["stratified"]["executed_vs_A"]
for key, name, want in [("qwen_combined_minus_action", "Qwen executed combined - action", [-0.30, -0.44, -0.17]),
                        ("luna_combined_minus_action", "luna executed combined - action", [0.16, 0.05, 0.28]),
                        ("luna_silent_combined_minus_action_posthoc", "luna silent executed", [0.12, -0.08, 0.32])]:
    got = [sec[key]["delta"], *sec[key]["ci"]]
    if key == "qwen_combined_minus_action":
        raw = unr["M6_qwen_executed_combined_minus_action"]
        check("M6", name + " unrounded matches stored 3 dp", [round(x, 3) for x in raw["value"]], got, tol=1e-9)
        got, want = raw["value"], [-0.30, -0.44, -0.16]
    check("M6" if "silent" not in key else "M31", name, got, want)
sd = load(Q22, "analysis/salt_d1.json")
check("M7", "SALT text auditor", [sd["E105_audit"]["auroc"]["est"], *sd["E105_audit"]["auroc"]["ci"]],
      [0.87, 0.83, 0.91])
check("M7", "SALT P(said | executed)", sd["E104_sayvsdo"]["P_said_given_exec"]["est"], 0.385, tol=0.0005)
cue = load(Q22, "analysis/p2_cue_llm_p2cue.json")
pc = cue["paired"]
check("M9", "notepad - none r2-12", pc["notes-none"]["prem_r2_12"], [1.04, 0.65, 1.42])
check("M9", "channel - none r2-12", pc["private-none"]["prem_r2_12"], [1.61, 0.92, 2.35])
check("M9", "notepad / channel ratio", cue["H3_notes_over_private_r2_12"], [0.65, 0.34, 1.32])
check("M9", "placebo - none r2-12", pc["placebo-none"]["prem_r2_12"], [1.23, 0.76, 1.85])
pp = pc["placebo-private"]["prem_r2_12"]
check("M9", "private - placebo r2-12", [-pp[0], -pp[2], -pp[1]], [0.38, -0.41, 1.18])
check("M13", "premium precision@0.05", load(Q22, "analysis/p2_prevalence.json")["llm_v3_test"]["detectors"]["premium"]
      ["precision@0.05"][0], 0.24)
sp = load(Q22, "analysis/e132_inversion.json")["sets"]["Qwen3.8 base"]
check("M33", "Spearman text vs invite pooled", sp["spearman_text_vs_invite_rate_pooled"], [0.49, 0.17, 0.71, 30])
raw = unr["M33_qwen38_base_within_no_channel"]["value"]
check("M33", "Spearman within no-channel unrounded matches stored 3 dp", [round(x, 3) for x in raw[:3]] + raw[3:],
      sp["spearman_text_vs_invite_rate_within_no_channel"], tol=1e-9)
check("M33", "Spearman within no-channel", raw, [-0.40, -0.83, 0.18, 15])

lx = load(Q22, "label_xfam.json")["datasets"]
check("M15", "3-class kappa llm_v3 / llm_v3rep", [lx["llm_v3"]["kappa_3class"], lx["llm_v3rep"]["kappa_3class"]],
      [0.33, 0.38])
check("N7", "executed max-pair markup (inflated)", ex["market_level"]["executed"]["auroc"], 0.99)
ds_te = load(Q14, "eval/llm_ds_p2.json")["by_T"]["20"]["te"]
check("N20", "deepseek TE C vs A with CI", [ds_te["auroc_C_vs_A"], *ds_te["auroc_ci_C_vs_A"]], [0.81, 0.62, 0.96])
for i in (1, 2):
    para = load(Q22, f"analysis/p2_cue_llm_p2para{i}.json")
    check("M9", f"paraphrase {i} n private/none", [para["n"]["private"], para["n"]["none"]], [10, 10])
    check("M9", f"paraphrase {i} private - none r2-12", para["paired"]["private-none"]["prem_r2_12"],
          [[1.79, 1.20, 2.43], [0.24, -0.32, 0.81]][i - 1])
lb = load(Q22, "analysis/p2_logbook.json")
check("M9", "logbook (weather) - none r2-12", lb["paired"]["logbook-none"]["prem_r2_12"], [0.22, 0.05, 0.40])
check("M9", "logbook matched seeds", lb["paired"]["logbook-none"]["n"], 15)
# Source JSON stores 2.135 [1.285, 3.005] (rounded to 3 dp); the source reports print 2.13 [1.28, 3.00]
# (double rounding). Recompute the unrounded values from the pinned E65 data with Q1.4's own estimator
# (scripts/p2_partc.py row + p2_variants.boot_diff, B = 10000, seed 0): 2.1353 [1.2853, 3.0047] -> 2.14 [1.29, 3.00].
sq = cd["llm_strong_qa"]
check("N23", "E65 abliterated+memory C - A (stored 3 dp)", [sq["d"], *sq["d_ci"]], [2.135, 1.285, 3.005], tol=1e-9)
import numpy as np  # noqa: E402
e65_gt = {g["run_id"]: g for g in map(json.loads, evidence.lines(Q14, "data/llm_strong_qa/ground_truth.jsonl"))}
e65_rows = {}
for line in evidence.lines(Q14, "data/llm_strong_qa/trajectories.jsonl"):
    r = json.loads(line)
    if r["run_id"] in e65_gt and all(m.startswith("qwen-abliterated") for m in (e65_gt[r["run_id"]].get("model") or {}).values()):
        e65_rows.setdefault(r["run_id"], []).append(r)
e65_by = {"A": [], "C": []}
for rid, rs in e65_rows.items():
    if e65_gt[rid]["condition"] in e65_by:
        e65_by[e65_gt[rid]["condition"]].append(float(np.mean(
            [np.mean([a["price"] for a in r["agents"]]) - {6: 10, 8: 12}[r["market"]["cost"]] for r in rs])))
rng = np.random.default_rng(0)
c_, a_ = np.asarray(e65_by["C"]), np.asarray(e65_by["A"])
boot = [rng.choice(c_, len(c_)).mean() - rng.choice(a_, len(a_)).mean() for _ in range(10000)]
e65 = [float(c_.mean() - a_.mean()), float(np.quantile(boot, .025)), float(np.quantile(boot, .975))]
check("N23", "E65 games A, C", [len(a_), len(c_)], [20, 20])
check("N23", "E65 recomputed matches stored 3 dp", [round(x, 3) for x in e65], [sq["d"], *sq["d_ci"]], tol=1e-9)
check("N23", "E65 abliterated+memory C - A", e65, [2.14, 1.29, 3.00])

document_checks = check_documents(checks, {"SUBMISSION.md": args.submission, "SLIDES.md": args.slides})
n_files = evidence.verify()
bad = [c for c in checks if not c["ok"]]
doc_bad = [c for c in document_checks if not c["ok"]]
commits = {p + "_commit": c["commit"] for p, c in evidence.manifest["projects"].items()}
receipt = {**commits, "source_mode": "live" if args.live else "snapshot", "n_evidence_files": n_files,
           "evidence_manifest_sha256": hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
           "document_bindings_sha256": hashlib.sha256((ROOT / "results/document_bindings.json").read_bytes()).hexdigest(),
           "n_checks": len(checks), "n_fail": len(bad), "checks": checks,
           "n_document_checks": len(document_checks), "n_document_fail": len(doc_bad),
           "document_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                               for name, path in {"SUBMISSION.md": args.submission, "SLIDES.md": args.slides}.items()},
           "document_checks": document_checks}
OUT.write_text(json.dumps(receipt, indent=1) + "\n")
for c in checks:
    print(("OK  " if c["ok"] else "FAIL"), c["row"], c["what"], c["got"], "want", c["want"])
for c in doc_bad:
    print("FAIL document", c)
print(f"{len(checks) - len(bad)}/{len(checks)} source checks; "
      f"{len(document_checks) - len(doc_bad)}/{len(document_checks)} document bindings; "
      f"{n_files} evidence hashes ({receipt['source_mode']}) -> {OUT}")
sys.exit(1 if bad or doc_bad else 0)
