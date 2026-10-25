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
check("M34", "Fig.6 price views strict vs tacit-high: min/max point", [min(v[0] for v in pv), max(v[0] for v in pv)],
      [0.43, 0.58])
check("M34", "all price-view CIs include 0.5", all(v[1] < 0.5 < v[2] for v in pv), True)

# Further headline quantities, formerly checked only by the human/source reviews.
lc = cd["llm_long_p2_T60"]
check("N5", "T60 pCMI", [lc["pcmi"], *lc["pcmi_ci"]], [0.34, 0.18, 0.52])
ex = load(Q14, "eval/p2_partc.json")["E64_pooled"]["all sets"]
check("N7", "executed pCMI", [ex["pcmi"]["executed"]["auroc"], *ex["pcmi"]["executed"]["ci"]], [0.42, 0.33, 0.53])
check("N7", "executed counts", [ex["n_executed"], ex["n_executed"] + ex["n_not_executed"]], [48, 149], tol=0)
check("N7", "executed pair-level", [ex["pair_level"]["executed"]["auroc"], *ex["pair_level"]["executed"]["ci"]], [0.87, 0.80, 0.94])
grid = load(Q14, "eval/e70_grid.json")
for key, want in [("market_level", [0.74, 0.66, 0.81]), ("pcmi", [0.51, 0.43, 0.59]), ("te", [0.62, 0.54, 0.70])]:
    v = grid["pooled_auroc"][key]
    check("N8", "grid " + key, [v["auroc"], *v["ci"]], want)
test = load(Q22, "analysis/final_llm_v3_gpt-6.1-sol_test.json")
d = test["contrasts"]["delta_hybrid[combined]:run_auroc"]
check("M1", "locked combined - better single", [d["delta"], *d["ci"]], [-0.01, -0.09, 0.06])
check("M1", "locked n", test["n_runs"], 95, tol=0)
for key, want in [("text", [0.47, 0.36, 0.58]), ("action", [0.75, 0.65, 0.85])]:
    check("M3", "locked " + key, test["point_ci"][key]["run_auroc"], want)
classes = load(Q22, "analysis/p2_strong_classes_llm_p2strongF.json")
check("M10", "strong tacit-high count", classes["n_tacit_high_none"], [19, 20], tol=0)
check("M10", "strong strict-executed count", classes["n_strict_executed"], [13, 20], tol=0)

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
