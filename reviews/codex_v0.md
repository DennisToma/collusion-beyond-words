Reading additional input from stdin...
OpenAI Codex v0.163.0
--------
workdir: /home/factory/collusion/collusion-beyond-words
model: gpt-6.1-sol
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a17216-17c6-74f2-a20f-8e66d5b93a73
--------
user
You are an adversarial reviewer. Read SUBMISSION.md and SOURCES.md in this repo. For every numeric claim in SUBMISSION.md, check it against the source JSON/REPORT in ~/collusion/collusion-14-infotheory (Q1.4) and ~/collusion/collusion-22-say-vs-do (Q2.2) at their current commits (read-only). Report: (P1) numbers that are wrong or mis-attributed, (P2) overclaims, wording that drops a caveat the source states (post hoc, uncorrected, point estimate, definition of executed), or claims about the merged story the data do not support, (P3) clarity issues. Give file:line and the exact source key for each. Be concise; list at most 25 items, most severe first.
codex
I’ll read both submission files, check every numeric claim against Q1.4 and Q2.2 at their current commits, and rank the discrepancies and caveat gaps.
exec
/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g 'SUBMISSION.md' -g 'SOURCES.md' -g '*REPORT*' -g '*.json' . /home/factory/collusion/collusion-14-infotheory /home/factory/collusion/collusion-22-say-vs-do" in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
/home/factory/collusion/collusion-beyond-words
/home/factory/collusion/collusion-22-say-vs-do/results/label_xfam.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_pool_rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_serendipity.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2qwena.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2qwenb.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_family3way.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/fp_prices.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/llm_v3_gpt-6.1-sol_orig.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/text_lr_inspect.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_c2older.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/evidence_llm_v3_gpt-6.1-sol_dev.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/replication_llm_v3rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2g56sol.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/phase2_reproduction.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/nolevel_view.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_within_agree_llm_p2strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/early_detection_llm_v3.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_replace_integrity.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_band.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/llm_v3_crossfamily_claude-sonnet-5-5.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2qwenb.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2mimo.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2g56sol.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/monitor_stratum_llm_v3mon.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_behaviour.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_pilot_interim.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/price_transitions.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_plan_calib.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_qwen_public.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/round1_effect_llm_v3.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/claims_denominators.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_asym.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/final_llm_v3_gpt-6.1-sol_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e113_secondary.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_e1_coverage.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2para2.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133c_llm.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_replace.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/round1_effect_llm_v3rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/evidence_sources.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_e1_audit.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_textlr.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/evidence_rounds_llm_v3_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2sol.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_qwen9_pilot.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_logbook.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_de.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133_privileged.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/cost_llm_v3.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/evidence_rounds_llm_v3rep_all.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e132_inversion.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_pilot_final.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/shuffle_llm_v3_gpt-6.1-sol_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/early_detection_llm_v3rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2mimo.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/incremental_llm_v3_gpt-6.1-sol_dev.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_pilot_luna_final.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_qwen_cmp.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/final_llm_v3_gpt-6.1-sol_dev.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_terms_xfam.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_verdict_llm_p2cue.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2strong_luna.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_eval_llm_p2strong_luna.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_qwen.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_qwen_strong.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_prevalence.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2claude.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/replication_llm_p2rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_within_agree_llm_p2qwena.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/markup_baseline.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strict_sensitivity.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strong_classes_llm_p2qwena.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/salt_d1.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_family_views.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/textsim_llm_v3_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2para1.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_say_vs_do.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strongF_public.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2cue.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_family.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strongF_report_llm_p2strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/matched_recall_llm_v3_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133e_attr.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_asym_nash.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_within_agree_llm_p2qwenb.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/incremental_llm_v3_gpt-6.1-sol_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133_cluster.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/hint_view.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/evidence_llm_v3_gpt-6.1-sol_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_replace_sol.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_cue_llm_p2ds.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/deterrence.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133d_noprivate_llm.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_replace_selftest.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/interim/p2_cue_llm_p2sol_4seeds.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/interim/p2_cue_llm_p2ds_10seeds.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/interim/p2_cue_llm_p2claude_5seeds.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/textsim_llm_v3_dev.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/mechanism_sources.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/fp_stratum_llm_v3fp.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_behaviour_p2rep.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/placebo_llm_v3plc.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_aware.json
/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_plan_keyword_llm_p2strongF.json
/home/factory/collusion/collusion-22-say-vs-do/results/llm_auditor/llm_v3/shuffle_donors_s1.json
/home/factory/collusion/collusion-22-say-vs-do/results/llm_auditor/llm_v3/shuffle_donors_s0.json
/home/factory/collusion/collusion-22-say-vs-do/results/llm_auditor/llm_v3/shuffle_donors_s2.json
/home/factory/collusion/collusion-14-infotheory/REPORT.pdf
/home/factory/collusion/collusion-14-infotheory/results/iteration27_publish_check.json
/home/factory/collusion/collusion-14-infotheory/results/p2_landing_check.json
/home/factory/collusion/collusion-14-infotheory/results/p2/validation.json
/home/factory/collusion/collusion-14-infotheory/results/p2/compatibility.json
/home/factory/collusion/collusion-14-infotheory/results/p2/onset_test.json
/home/factory/collusion/collusion-14-infotheory/results/p2/market_test.json
/home/factory/collusion/collusion-14-infotheory/results/p2/rotation_test.json
/home/factory/collusion/collusion-14-infotheory/results/p2/costasym_test.json
/home/factory/collusion/collusion-14-infotheory/results/p2/coalition_dev.json
/home/factory/collusion/collusion-14-infotheory/results/p2/costasym_dev.json
/home/factory/collusion/collusion-14-infotheory/results/p2/REPORT_codex.md
/home/factory/collusion/collusion-14-infotheory/results/p2/coalition_test.json
/home/factory/collusion/collusion-14-infotheory/results/p2/onset_dev.json
/home/factory/collusion/collusion-14-infotheory/results/p2/market_dev.json
/home/factory/collusion/collusion-14-infotheory/results/p2/rotation_dev.json
/home/factory/collusion/collusion-14-infotheory/results/release_audit_iter23_full.json
/home/factory/collusion/collusion-14-infotheory/results/release_audit_iter21_phase2.json
/home/factory/collusion/collusion-14-infotheory/results/e68_pipeline_check.json
./SUBMISSION.md
/home/factory/collusion/collusion-14-infotheory/results/dev/pcmi_design_seed11.json
/home/factory/collusion/collusion-14-infotheory/results/release_audit.json
/home/factory/collusion/collusion-14-infotheory/results/release_audit_initial_iter27.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c06.json
/home/factory/collusion/collusion-14-infotheory/results/eval/matched_ref.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_qb36_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e72_te_diag.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c15.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c11.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c12.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e67_sticky.json
/home/factory/collusion/collusion-14-infotheory/results/eval/same_model.json
/home/factory/collusion/collusion-14-infotheory/results/eval/p2_partc.json
/home/factory/collusion/collusion-14-infotheory/results/eval/spillover_llm_long_p2_T60.json
/home/factory/collusion/collusion-14-infotheory/results/eval/p2_public_llm_ds_p2pub.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_ds_p2pub.json
/home/factory/collusion/collusion-14-infotheory/results/eval/spillover_llm_long.json
/home/factory/collusion/collusion-14-infotheory/results/eval/long_power_llm_long_p2_T60.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c10.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v1_market_mean_ranges.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c03.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c13.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v3_premium.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_p2_noreason.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_qa_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c00.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c08.json
/home/factory/collusion/collusion-14-infotheory/results/eval/nonagreement_ext.json
/home/factory/collusion/collusion-14-infotheory/results/eval/gate_v2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/strongF_ext.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c10.json
/home/factory/collusion/collusion-14-infotheory/results/eval/gate_test.json
/home/factory/collusion/collusion-14-infotheory/results/eval/claims_denominators.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v3_diag.json
/home/factory/collusion/collusion-14-infotheory/results/eval/p2_variants.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e70_followup.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_mixed2_mixed.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_long.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c08.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v1_diag.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c13.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e44_decline.json
/home/factory/collusion/collusion-14-infotheory/results/eval/p2cue_ext.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c04.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_long_p2_T60.json
/home/factory/collusion/collusion-14-infotheory/results/eval/injection_mde.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e70_grid.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_strong_qa.json
/home/factory/collusion/collusion-14-infotheory/results/eval/preplay_offer.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c14.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c04.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_qb_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e68_cda.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c05.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c07.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_mixed_mixed.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_p2_v0.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c01.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e70_followup_declared.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e70_dry.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c14.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v1.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c02.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_mixed2_price_by_model.json
/home/factory/collusion/collusion-14-infotheory/results/eval/prevalence.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_p2_para.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e73_nonlinear.json
/home/factory/collusion/collusion-14-infotheory/results/eval/placebo_rep_ext.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c07.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c03.json
/home/factory/collusion/collusion-14-infotheory/results/eval/executed_sensitivity.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_pilot4.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e74_paired_diff.json
/home/factory/collusion/collusion-14-infotheory/results/eval/long_power_llm_long.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c01.json
/home/factory/collusion/collusion-14-infotheory/results/eval/spillover_llm_strong_qa.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c00.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c12.json
/home/factory/collusion/collusion-14-infotheory/results/eval/spillover_llm_ds_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/e70_followup_dry.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c11.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_ds_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_v3_ext.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c05.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c09.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_p2_template.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c02.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c09.json
/home/factory/collusion/collusion-14-infotheory/results/eval/p2_family.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_dry_c15.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_qa36_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/behaviour_split.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_grid_p2_c06.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_p2_order.json
/home/factory/collusion/collusion-14-infotheory/results/eval/llm_g56l_p2.json
/home/factory/collusion/collusion-14-infotheory/results/eval/spillover_llm_v1.json
/home/factory/collusion/collusion-14-infotheory/results/release_audit_iter27.json
/home/factory/collusion/collusion-14-infotheory/results/e70_pipeline_check.json
/home/factory/collusion/collusion-14-infotheory/results/checkpoint_iter26.json
/home/factory/collusion/collusion-14-infotheory/results/saved_scores_check.json
/home/factory/collusion/collusion-14-infotheory/results/sweeps/power_test.json
/home/factory/collusion/collusion-14-infotheory/results/sweeps/power.json
/home/factory/collusion/collusion-14-infotheory/results/reimpl/results.json
/home/factory/collusion/collusion-14-infotheory/results/reimpl/compare.json
/home/factory/collusion/collusion-14-infotheory/data/llm_grid_p2_manifest.json
/home/factory/collusion/collusion-14-infotheory/REPORT.md
/home/factory/collusion/collusion-14-infotheory/data/ext_q22_partc/p2_qwen9_pilot.json
/home/factory/collusion/collusion-14-infotheory/data/ext_q22_partc/p2_qwen_cmp.json
/home/factory/collusion/collusion-22-say-vs-do/results/salt/sample.json
/home/factory/collusion/collusion-22-say-vs-do/results/reimpl/reimpl_results.json
/home/factory/collusion/collusion-22-say-vs-do/REPORT.md
/home/factory/collusion/collusion-22-say-vs-do/REPORT_APPENDIX.md
/home/factory/collusion/collusion-22-say-vs-do/REPORT.pdf
/home/factory/collusion/collusion-22-say-vs-do/data/handoff_exports.json
./SOURCES.md
/home/factory/collusion/collusion-22-say-vs-do/data/evaluation_receipt.json
/home/factory/collusion/collusion-22-say-vs-do/data/ext_llm_grid_p2/snapshot_receipt.json
/home/factory/collusion/collusion-22-say-vs-do/data/ext_llm_grid_p2/grid_manifest.json
/home/factory/collusion/collusion-22-say-vs-do/data/audit_input_receipt.json
/home/factory/collusion/collusion-22-say-vs-do/data/verification_history/e117_initial.json
/home/factory/collusion/collusion-22-say-vs-do/data/artifact_manifest.json
/home/factory/collusion/collusion-22-say-vs-do/data/ext_llm_grid_p2_e70/e70_grid.json
/home/factory/collusion/collusion-22-say-vs-do/data/ext_llm_grid_p2_e70/SOURCE.json
/home/factory/collusion/collusion-22-say-vs-do/data/serendipity_e108/manifest.json
/home/factory/collusion/collusion-22-say-vs-do/REPORT.html
/home/factory/collusion/collusion-22-say-vs-do/data/ext_cda_d2/e68_cda.json
/home/factory/collusion/collusion-22-say-vs-do/data/ext_cda_d2/SOURCE.json
/home/factory/collusion/collusion-22-say-vs-do/data/p2_family3way_scope.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/llm_v3_lr_test.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/scripted_v1_lr.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/scripted_v2_gbm.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/scripted_v2_lr.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/llm_v3_lr_dev.json
/home/factory/collusion/collusion-22-say-vs-do/results/baselines/llm_v3_lr.json
/home/factory/collusion/collusion-14-infotheory/REPORT.html
/home/factory/collusion/collusion-14-infotheory/data/ext_llm_p2strongF/sibling_classes.json

exec
/bin/bash -lc 'for p in /home/AGENTS.md /home/factory/AGENTS.md /home/factory/collusion/AGENTS.md /home/factory/collusion/collusion-beyond-words/AGENTS.md /home/factory/collusion/collusion-14-infotheory/AGENTS.md /home/factory/collusion/collusion-22-say-vs-do/AGENTS.md; do if [ -f "$p" ]; then cat "$p"; fi; done; nl -ba SUBMISSION.md; nl -ba SOURCES.md' in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
     1	# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence
     2	
     3	**Dennis Toma** — Apart Research AI Collusion Sprint, 23–25 October 2026
     4	
     5	*Merged submission of two sprint projects: Q1.4 (information-theoretic, prices-only detection) and Q2.2
     6	(auditing what agents say together with what they do). Every number below is taken from the frozen
     7	source repos at the commits listed in [SOURCES.md](SOURCES.md), which maps each number to its JSON file.
     8	Draft v0 (2026-10-25 08:30 UTC); numbers not yet independently re-verified are marked in SOURCES.md.*
     9	
    10	## Abstract
    11	
    12	When LLM pricing agents are given a private channel, can an auditor tell — from prices, from public
    13	messages, or from both? We study four-seller repeated price markets with LLM sellers (7 seller models,
    14	two market implementations) in which one pair is offered an unmonitored chat channel and is never told to
    15	collude. **Prices: the channel shows up as a price level, not as co-movement.** The channel raised markup
    16	over Nash in 9/9 main sets, and a simple max-pair markup screen beat a conditional-dependence detector
    17	(pCMI) in 9/9 (AUROC 0.75–0.99 vs 0.34–0.72; paired difference CI > 0 in 8/9). pCMI stays at chance in a
    18	192-game seven-factor grid (0.51 [0.43, 0.59]), at T = 60 (0.34 [0.18, 0.52], pre-registered), on executed
    19	agreements only (0.42 [0.33, 0.53]) and with rank-based or discrete estimators, although on scripted
    20	sellers it finds every planted pair and removes most common-shock and shared-policy false alarms.
    21	**Words: public messages add nothing and can mislead.** A zero-shot LLM auditor reading prices plus public
    22	messages does no better than its better single view (−0.01 [−0.09, +0.06], locked test, n = 95; −0.07
    23	[−0.17, +0.02] on fresh replications); in families that talk publicly in every market, text ranks control
    24	markets *above* channel markets (AUROC 0.15–0.36), and on Q1.4's Qwen grid adding text lowers AUROC
    25	(combined − prices −0.24 [−0.37, −0.09]). Text helps only where the deal is the conversation (SALT negotiations, 0.87 [0.83, 0.91]).
    26	**Neither signal is collusion-specific.** An unread private pricing notepad produces 65% of the
    27	channel's premium; with memory and profit framing 19/20 *no-channel* markets price ≥ Nash + 2; level
    28	screens false-flag 30/30 scripted markets with unequal costs; and at 1% prevalence no flag reaches
    29	precision 0.25. Price statistics are therefore a cheap first-stage screen whose references must be matched
    30	to the seller model and prompt, not a verdict.
    31	
    32	## 1. Introduction
    33	
    34	Algorithmic pricing agents built on LLMs reach supracompetitive prices without instruction (Fish et al.
    35	2024) and change behaviour when they can communicate (Agrawal et al. 2025). Regulators and platform
    36	operators will mostly see two things: the agents' *actions* (prices) and whatever they *say* in public.
    37	Two natural detection strategies follow:
    38	
    39	1. **Information theory on actions** (Q1.4). Colluders should share information beyond what public state
    40	   explains, so their prices should be conditionally dependent (Bonjour et al. 2022). This promises a
    41	   detector that is blind to the channel content and hard to evade by choosing words.
    42	2. **Say + do auditing** (Q2.2). An LLM auditor reading both public messages and prices should catch
    43	   inconsistencies between what agents say and what they do, and beat single-stream auditors.
    44	
    45	We test both on the same family of LLM markets, cross-apply each project's detectors to the other's data,
    46	and keep three label levels apart: *assigned opportunity* (channel offered), *verified agreement* (judge
    47	reads the private chat) and *realised coordination* (prices follow the agreement).
    48	
    49	**Contributions.**
    50	- A prices-only conditional-dependence detector (pCMI, with shift and same-model surrogate nulls) that
    51	  passes a scripted positive control and a hard-negative battery (common shocks, shared policies,
    52	  legitimate leader–follower pricing), plus an honest map of what it cannot separate (shared random seeds).
    53	- Evidence across 9 main LLM sets, a 192-game factorial grid and a pre-registered long-game test that LLM
    54	  channel collusion appears as a **price level**, with no detected contemporaneous co-movement.
    55	- A registered say-vs-do comparison showing that public text adds no resolved detection value, can be
    56	  **inverted**, and helps only when the act happens in the conversation.
    57	- Confound analyses (prompt artefacts, placebo, tacit high prices, cost asymmetry, prevalence) showing
    58	  why any price screen is an audit trigger, not proof.
    59	
    60	## 2. Related work
    61	
    62	*Dependence as a collusion signal.* Bonjour et al. (2022) measure collusion as statistical dependence
    63	between agents' actions; our pCMI is a conditioned pairwise version. Banchio & Mantegazza (2023) show
    64	supracompetitive play from "spontaneous coupling" without agreement — the case our shared-shock and
    65	shared-policy hard negatives target. Tailor (2025) applies mutual-information detectors to steganographic
    66	message channels; we apply the same estimator family to actions. Transfer entropy follows Schreiber (2000).
    67	*LLM pricing collusion.* Fish et al. (2024), Agrawal et al. (2025; double auctions), Lin et al. (2024;
    68	market division expressed in actions, not messages), Dhanda (2026; price caps as focal points).
    69	*Shared models.* Cao & Hu (2026) show supracompetitive prices from a shared LLM advisor without
    70	coordination, motivating our same-model references. *Definitions.* Rose et al. (2026): communication within
    71	a subgroup leading to actions harmful to outsiders; Calvano et al. (2020) and Green & Porter (1984) for
    72	repeated-pricing benchmarks. *Message-side collusion.* Motwani et al. (2024) and Mathew et al. (2024) study
    73	secret/steganographic collusion in messages; SALT-NLP negotiation data serve as our external text case.
    74	
    75	## 3. Setup
    76	
    77	**Markets.** Two four-seller repeated price markets with multinomial-logit demand, public cost and demand
    78	shocks, and integer prices:
    79	- *Q1.4 market* (`sim/market.py`): cost 6/8, static Nash price 10 (cost 8: 12), joint-profit optimum 16;
    80	  T = 20 in most LLM sets (T = 40–60 in long-game sets).
    81	- *Q2.2 market* (`llm_market.py`): 12 rounds, prices 6–30, static Nash ≈ 11, joint monopoly ≈ 19;
    82	  arms `private` (pair has a channel), `none`, and `legit` (publicly announced cost-saving partnership,
    83	  hard negative).
    84	Each project also runs the other's data: Q1.4 scored Q2.2's `llm_v3` market; Q2.2 audited all 192 games
    85	of Q1.4's E70 grid (E113).
    86	
    87	**LLM sellers.** Q1.4's nine main sets use seven seller models: gpt-6-luna (main), gpt-5.6-luna,
    88	deepseek-v4.1-flash, and base and abliterated (refusal-removed) Qwen3.8-27B and Qwen3.6. Q2.2's main market
    89	uses gpt-6-luna and adds family arms (Claude Sonnet, deepseek, Qwen3.8 base/abliterated, gpt-6.1-sol). Profit-maximisation /
    90	economics-lab framing after Fish et al. (2024); the channel pair is never instructed to collude. A public
    91	message board exists in every arm.
    92	
    93	**Labels.** A gpt-6.1-sol judge reads only the private chat (never prices) → explicit agreement /
    94	information exchange / none; Claude Sonnet 5.5 re-judged 115 chats and agreed on the binary label in
    95	115/115. *Executed* agreements are defined from prices (each project's own frozen rule, stated where
    96	used); *tacit-high* = a no-channel market with second-half mean ≥ Nash + 2.
    97	
    98	**Splits and discipline.** Scripted detector settings were tuned only on dev seeds and evaluated once on
    99	locked seeds (1001/1002); no detector setting was tuned on LLM data. Q2.2's auditors are zero-shot with one
   100	prompt per view, evaluated once on a locked test split (runs 0030–0124, n = 95) and replicated on fresh,
   101	pre-registered splits. Most Phase 2 experiments were declared before their data existed; post-hoc analyses
   102	are labelled.
   103	
   104	## 4. Methods
   105	
   106	**Price detectors (Q1.4, prices only).** Per pair: |Pearson|, plug-in MI, CMI given public state, and
   107	**pCMI** = −½ log(1 − ρ²) of residuals after regressing each seller's price on state dummies and all four
   108	lagged prices; transfer entropy (TE, lagged, max over directions). Two nulls: a circular-shift null
   109	(B = 200, relative offsets ≥ 3 rounds), and a **same-model surrogate null** ranking the run's max-pair
   110	score against no-channel games of the same model and shock family. Level screens: *max-pair markup* over
   111	the per-round Nash price and *pair_level* (pair mean minus rivals). An independent reimplementation agreed
   112	on 422/424 run × statistic cells to < 1e-9.
   113	
   114	**Auditors (Q2.2).** One zero-shot gpt-6.1-sol auditor, same task text, six views: `text` (public messages
   115	+ public facts), `action` (prices, costs, demand, profit), `action_stats` (+ computed pair-statistics
   116	table), `combined` (text ∪ action), `combined_stats`, `structured`. Registered primary contrast:
   117	Δ_hybrid = AUROC(combined) − max(AUROC(text), AUROC(action)).
   118	
   119	**Statistics.** Run-level AUROC with class-stratified game bootstrap 95% CIs; Wilson intervals for flag
   120	rates; Jeffreys for precision. CIs are per-set and uncorrected for multiplicity unless stated.
   121	
   122	## 5. Results
   123	
   124	### 5.1 On scripted sellers, conditioning works (positive control)
   125	
   126	![Scripted hard negatives](figures/fig1_scripted_hard_negatives.png)
   127	*Figure 1 (Q1.4 §4.1, locked seed 1001, 50 runs per group). Run-level flag rates at α = 0.05.*
   128	
   129	Every contemporaneous detector flags and localises the planted pair in 100% of runs. Raw MI flags 100%
   130	of common-shock controls; conditioning on public state and lagged prices (pCMI) cuts this to 14% under the
   131	shift null and, for the held-out *shared policy + common shock* hard negative, 4% [1, 13] under the
   132	same-model surrogate null. Two failure modes are structural: two copies of one policy sharing a random
   133	seed are flagged by every contemporaneous detector (44–100%) — from price data they *are* a private shared
   134	signal — and lagged TE flags legitimate public leader–follower pricing in 100% of runs. Level screens fail
   135	elsewhere: unequal private costs are false-flagged in 30/30 scripted markets (pCMI 4/30).
   136	
   137	### 5.2 With LLM sellers, the channel shows up as a price level, not co-movement
   138	
   139	![Level vs co-movement](figures/fig2_level_vs_comovement_9sets.png)
   140	*Figure 2 (Q1.4 P2.13). Nine main sets, seven seller models: channel − no-channel markup and run AUROC
   141	with game-bootstrap 95% CIs.*
   142	
   143	| evidence | max-pair markup (level) | pCMI (co-movement) | source |
   144	|---|---|---|---|
   145	| 9 main sets, 7 models | AUROC 0.75–0.99; C − A > 0 in 9/9 | 0.34–0.72; CI ∋ 0.5 in 8/9 | N1–N4 |
   146	| paired Δ level − pCMI | CI > 0 in 8/9 (exception gpt-5.6-luna +0.03 [−0.27, +0.33]) | | N3 |
   147	| E70 grid, 16 cells × 7 factors, 192 games | 0.74 [0.66, 0.81]; level > pCMI in 12/16 cells | 0.51 [0.43, 0.59] | N8 |
   148	| E44 long games, T = 60 (pre-registered) | 0.94 [0.86, 1.00] | 0.34 [0.18, 0.52] | N5 |
   149	| executed agreements only (48/149) | (inflated by construction) | 0.42 [0.33, 0.53] | N7 |
   150	| rank (copula) pCMI / sign-change CMI, E70 | | 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52] | N11 |
   151	
   152	The null is not an estimator artefact (rank-based and discrete estimators are also at chance) and not a
   153	pure power failure at T = 60: observed co-move excess is +0.004 [−0.007, +0.015], whereas pCMI detects a
   154	planted shared ±1 move at per-round rate q = 0.1 with AUROC 0.79 [0.70, 0.88]. At T = 20 (most sets) the
   155	same planting gives only 0.62 [0.52, 0.71], so small co-movement is not excluded there. The only dependence
   156	statistic above chance is lagged TE in the grid (0.62 [0.54, 0.70], declared secondary), still below level
   157	(+0.12 [+0.01, +0.22]); exploratory follow-up suggests it sits in channel games whose agreement was *not*
   158	executed (0.73 vs 0.49, post hoc). The one pCMI exception (base Qwen3.6, 0.71 [0.51, 0.88]) did not
   159	replicate in the grid's Qwen cells.
   160	
   161	![E70 grid](figures/fig3_e70_grid.png)
   162	*Figure 3 (Q1.4 P2.14). Registered 16-cell grid (E70), per-cell channel effect and detector AUROCs (cell
   163	estimates are descriptive).*
   164	
   165	### 5.3 Public words add nothing — and can point the wrong way
   166	
   167	![Say vs do](figures/fig4_say_vs_do_summary.png)
   168	*Figure 4 (Q2.2). (a) Run AUROC of each auditor view and of the one-line pair-premium statistic, locked test (n = 95, run once) and fresh replication (n = 30). (b) Placebo stratum (15 matched seeds): flag rates when private messages are delivered vs offered but never delivered vs no channel.*
   169	
   170	| where text could help | contrast | n | text view | action view |
   171	|---|---|---|---|---|
   172	| luna, base framing (locked test) | judge-labelled y = 1 vs 0 | 95 runs | 0.47 [0.36, 0.58] | 0.75 [0.65, 0.85] |
   173	| Claude Sonnet (talks publicly) | private vs none | 10 | 0.22 [0.00, 0.52] | 0.52 [0.20, 0.88] |
   174	| deepseek (talks publicly) | private vs none | 30 | 0.36 [0.20, 0.52] | 0.53 [0.30, 0.74] |
   175	| Qwen3.8 base | private vs none | 15 + 15 | 0.21 [0.12, 0.33] | 0.86 [0.69, 0.98] |
   176	| Qwen3.8 abliterated | private vs none | 15 + 15 | 0.15 [0.05, 0.25] | 0.57 [0.36, 0.78] |
   177	| SALT-NLP negotiation (external; deal struck in chat) | executed vs not | 240 episodes | 0.87 [0.83, 0.91] | – |
   178	
   179	*Table 2 (Q2.2 P2.0, `results/analysis/p2_say_vs_do.md`). AUROC < 0.5 = the view ranks controls higher.*
   180	
   181	The registered contrast shows no resolved gain from adding public text: combined − better single view
   182	−0.01 [−0.09, +0.06] (locked test, n = 95), −0.07 [−0.17, +0.02] on pooled fresh replications (n = 90,
   183	pooling post hoc); gains above +0.06 / +0.02 are excluded at 95%. Text is *inverted* in families that
   184	invite rivals publicly in every market: Qwen channel sellers, who can coordinate in private, invite rivals
   185	publicly *less* (invite rate 0.40 vs 0.88 in controls; post hoc). Cross-applied to Q1.4's Qwen grid, where
   186	prices alone are at chance (0.52 [0.41, 0.64]), adding text lowers AUROC (combined − action −0.24
   187	[−0.37, −0.09]; −0.30 [−0.44, −0.17] on executed games). The exception is SALT, a bilateral negotiation
   188	where the agreement *is* the conversation; even there, 62% of executed deals were never stated explicitly
   189	(P(said | executed) = 0.385).
   190	
   191	With privileged access to the private chat (E133, n = 78, exploratory), say–do consistency forecasts later
   192	execution (AUROC 0.77) but adds nothing beyond early price stability (0.855); an LLM reading the early log
   193	beats the best raw early-price rule (0.94 vs 0.885, Δ +0.06 [+0.02, +0.10], post hoc), with no evidence that
   194	its edge comes from public messages.
   195	
   196	### 5.4 Neither signal is specific to collusion
   197	
   198	- **Prompt artefact.** In a six-arm study (15 matched seeds), a private *notes-to-self* pricing notepad with
   199	  no recipient raises the pair premium +1.04 [+0.65, +1.42] vs +1.61 [+0.92, +2.35] for the real channel
   200	  (ratio 0.65 [0.34, 1.32]); an offered-but-never-delivered placebo gives +1.23 [+0.76, +1.85]; delivery
   201	  itself (private − placebo, +0.38 [−0.41, +1.18]) is unresolved. A terse paraphrase of the instructions
   202	  shrinks the premium to +0.24 [−0.32, +0.81]. Figure 5 shows the earlier placebo stratum: delivered and
   203	  undelivered channels track each other from round 1.
   204	- **Tacit high prices.** With memory and profit framing, 19/20 *no-channel* gpt-6-luna markets price
   205	  ≥ Nash + 2; 13/20 channel pairs keep their agreement, but the channel adds no detectable price, so channel
   206	  labels stop being ground truth (Figure 6). Prompt wording alone moves no-channel markup from −0.19 to
   207	  +2.56.
   208	- **Legitimate asymmetry.** Scripted unequal costs: level screens false-flag 30/30. LLM cost/quality edges:
   209	  premium flags 7/10 and 9/10 (controls 2/10).
   210	- **Prevalence.** At 1% prevalence no frozen price flag reaches point-estimate precision 0.25 (Q1.4); the
   211	  premium screen's precision is 0.24 at 5% prevalence (Q2.2).
   212	- **Labels disagree.** Only 14/50 judge-labelled test agreements are kept under the follow rule.
   213	
   214	![Placebo](figures/fig5_placebo_premium.png)
   215	*Figure 5 (Q2.2, `llm_v3rep` seeds). Designated-pair premium per round: delivered channel (n = 15) vs offered-but-never-delivered placebo (n = 15) vs no channel (n = 10). The premium is present before any message is delivered (round 1) and the two channel arms are indistinguishable.*
   216	
   217	![Strong framing](figures/fig6_strong_framing_tacit.png)
   218	*Figure 6 (Q2.2 P2.7, `llm_p2strongF`, T = 40). Memory + profit framing: market-mean price − Nash by behaviour class; 19 tacit-high no-channel markets sit with the 13 executed channel pairs.*
   219	
   220	### 5.5 Joint statement (verbatim in both source reports)
   221	
   222	> "Detectability of LLM collusion by any price statistic is a property of the (seller model × prompt)
   223	> pair. Relative screens survive a shared model but fail under market-wide spillover; absolute screens
   224	> need model- and prompt-matched references." "With memory and a profit objective, gpt-6-luna sellers
   225	> raise prices market-wide without any channel (19/20 no-channel markets ≥ Nash + 2); agreements are then
   226	> often kept (13/20) but add no detectable price, so channel labels stop being ground truth. Abliterated
   227	> Qwen with memory differs (channel adds +2.13 [1.28, 3.00]; 5/20 executed), as the first sentence
   228	> predicts."
   229	
   230	## 6. Discussion and implications
   231	
   232	The two projects started from opposite bets — that collusion leaves a statistical fingerprint in actions,
   233	and that it leaves a semantic one in words — and reached the same conclusion: in these markets, LLM
   234	channel collusion is visible mainly as **how high** prices are, not in **how they move together** or in
   235	**what is said publicly**. This is good news for cheap screening (a markup screen is simple and
   236	interpretable) and bad news for attribution (a high level has many innocent causes: wording, model,
   237	memory, legitimate cost advantages, market-wide tacit pricing).
   238	
   239	A practical reading is a two-stage design: an always-on level screen against a **model- and
   240	prompt-matched** reference as the first stage, with expensive audits (dependence statistics, private-log
   241	review, provenance checks for shared seeds) only on flagged pairs. We have not evaluated this pipeline end
   242	to end, and our evidence does not support recommending a particular architecture; it does support that a
   243	flag is an audit trigger, not a verdict.
   244	
   245	## 7. Limitations
   246	
   247	- **Ground truth.** Labels come from one judge family (gpt-6.1-sol, also the auditor; Claude agrees
   248	  115/115 on binary labels); execution labels are defined from prices, so level screens are partly scored
   249	  on their own input on executed subsets.
   250	- **Scope of the co-movement null.** At T = 20 small co-movement is not excluded; sensitivity is bounded
   251	  only for the planted ±1 strategy. Below-chance pCMI in some sets is unexplained.
   252	- **No evasion test.** Monitor-aware sellers stopped agreeing (0/10, 0/10) rather than hiding; no red-teamed
   253	  or instructed colluder was run.
   254	- **Small samples, many comparisons.** 10–21 games per arm in most LLM sets; per-set CIs are uncorrected;
   255	  E70's per-cell estimates are descriptive; some contrasts (pooled replication, E133e, E72) are post hoc.
   256	- **Narrow markets.** Four sellers, logit demand, short horizons; one external double auction (E68) is
   257	  inconclusive (chat raises asks only +0.39 [+0.06, +0.69]); SALT is a different construct.
   258	- **Placebo.** Q1.4's own market has no placebo arm; Q2.2's placebo cannot separate delivery from offer.
   259	
   260	## 8. Future work
   261	
   262	1. Instructed / red-teamed colluders (coded public signals, gradual drift) to test evasion.
   263	2. Ground truth independent of prices and of the condition, judged by more than one model family.
   264	3. A larger placebo study with simultaneous pre-play to isolate delivered coordination.
   265	4. Mixed-family markets and provenance data for the shared-model / shared-seed confound.
   266	5. End-to-end evaluation of the two-stage audit against legitimate partnerships and tacit markets.
   267	
   268	## Reproducibility
   269	
   270	Code, data and per-claim JSON live in the source repos (commits in [SOURCES.md](SOURCES.md)); each has a
   271	reproduce section (Q1.4 REPORT §6; Q2.2 REPORT Appendix E, `verify_phase2.py`: 31/31 commands re-run
   272	from cache with 0 LLM calls). Figures in `figures/` are copies of the source figures.
   273	
   274	## References
   275	
   276	- Agrawal et al. (2025). Evaluating LLM Agent Collusion in Double Auctions. arXiv:2507.01413.
   277	- Banchio & Mantegazza (2023). Adaptive Algorithms and Collusion via Coupling. ACM EC '23. arXiv:2202.05946.
   278	- Bonjour et al. (2022). Information-Theoretic Approach to Detect Collusion in Multi-Agent Games. UAI 2022, PMLR 180.
   279	- Calvano, Calzolari, Denicolò & Pastorello (2020). Artificial Intelligence, Algorithmic Pricing, and Collusion. AER 110(10).
   280	- Cao & Hu (2026). Supracompetitive Pricing Under AI Monoculture. arXiv:2601.01279.
   281	- Dhanda (2026). A Price Cap Can Act as a Focal Point for LLM Pricing Agents. Preprint.
   282	- Fish et al. (2024). Algorithmic Collusion by Large Language Models. arXiv:2404.00806.
   283	- Green & Porter (1984). Noncooperative Collusion under Imperfect Price Information. Econometrica 52(1).
   284	- Lin et al. (2024). Strategic Collusion of LLM Agents: Market Division in Multi-Commodity Competitions. arXiv:2410.00031.
   285	- Mathew et al. (2024). Hidden in Plain Text: Steganographic Collusion in LLMs. arXiv:2410.03768.
   286	- Motwani et al. (2024). Secret Collusion among AI Agents: Multi-Agent Deception via Steganography. NeurIPS 2024.
   287	- Rose et al. (2026). Detecting Multi-Agent Collusion Through Multi-Agent Interpretability. arXiv:2604.01151.
   288	- Schreiber (2000). Measuring Information Transfer. PRL 85(2).
   289	- Tailor (2025). Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs. arXiv:2510.04303.
   290	
   291	## Appendix — full tables
   292	
   293	To be filled from the source claims tables (Q1.4 `results/eval/claims_denominators.md`, Q2.2
   294	`results/analysis/claims_denominators.md`) and Q1.4's Phase-2-at-a-glance table.
     1	# SOURCES — where every number in SUBMISSION.md comes from
     2	
     3	Source repos (read-only). Both declared a research freeze at 2026-10-25 07:30 UTC; later edits are logged
     4	in each REPORT.md under "### Changes after 08:00 (for the merge manager)".
     5	
     6	| short | repo | commit synced | synced at (UTC) |
     7	|---|---|---|---|
     8	| Q1.4 | `~/collusion/collusion-14-infotheory` | `0e06c03` | 2026-10-25 08:05 |
     9	| Q2.2 | `~/collusion/collusion-22-say-vs-do` | `8b680ee` | 2026-10-25 08:05 |
    10	
    11	Each source also keeps a machine-checked claims table: Q1.4 `results/eval/claims_denominators.{json,md}`,
    12	Q2.2 `results/analysis/claims_denominators.md` (generated by `p2_claims.py`). Spot-checked against JSON by
    13	the merge manager: rows marked ✔ below were read directly from the JSON at the synced commit.
    14	
    15	## Number → source map
    16	
    17	| # | number in SUBMISSION.md | repo | file (`results/…`) : key | §(source) | ✔ |
    18	|---|---|---|---|---|---|
    19	| N1 | channel raises markup over Nash in 9/9 main sets (7 models), C − A CI > 0 each | Q1.4 | `eval/claims_denominators.json`, `eval/p2_partc.json` | P2.13 | |
    20	| N2 | max-pair markup AUROC 0.75–0.99 vs pCMI 0.34–0.72 (9/9 point est.) | Q1.4 | `eval/claims_denominators.json` | P2.13 | |
    21	| N3 | paired Δ level − pCMI CI > 0 in 8/9; gpt-5.6-luna +0.03 [−0.27, +0.33]; smallest resolved +0.22 [+0.03, +0.44] (base Qwen3.6) | Q1.4 | `eval/e74_paired_diff.json` : `main_sets.*.level_minus_pcmi` | P2.13 | ✔ (llm_g56l_p2 δ 0.03) |
    22	| N4 | pCMI CI ∋ 0.5 in 8/9; base Qwen3.6 exception 0.71 [0.51, 0.88] | Q1.4 | `eval/claims_denominators.json` | P2.13 | |
    23	| N5 | E44 T=60: pCMI 0.34 [0.18, 0.52], market level 0.94 [0.86, 1.00] | Q1.4 | `eval/long_power_llm_long_p2_T60.json` | P2.8 | |
    24	| N6 | co-move excess +0.004 [−0.007, +0.015]; planted ±1 q=0.1: pCMI 0.79 [0.70, 0.88] (T=60), 0.62 [0.52, 0.71] (T=20) | Q1.4 | `eval/long_power_llm_long_p2_T60.json` : `mde` | P2.8 | ✔ (T=20 q=0.1 0.622) |
    25	| N7 | executed-only pCMI 0.42 [0.33, 0.53], 48/149; definition range 13–78/149, pCMI 0.343–0.531 (E71) | Q1.4 | `eval/p2_partc.json` : `E64_pooled` | P2.11 | |
    26	| N8 | E70 grid 192 games: C − A > 0 13/16; level > pCMI 12/16 (1 tie); pCMI 0.51 [0.43, 0.59]; TE 0.62 [0.54, 0.70]; level 0.74 [0.66, 0.81] | Q1.4 | `eval/e70_grid.json` : `pooled_auroc`, `level_vs_pcmi` | P2.14 | ✔ |
    27	| N9 | E70 Δ level − pCMI +0.23 [+0.12, +0.33]; level − TE +0.12 [+0.01, +0.22] | Q1.4 | `eval/e74_paired_diff.json` | P2.13/14 | |
    28	| N10 | E70 follow-up model effect +1.07 [−0.20, +2.41] (not confirmed) | Q1.4 | `eval/e70_followup.json` | P2.14 | |
    29	| N11 | E73 copula pCMI / sign CMI: E70 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52]; E44 0.40 [0.23, 0.58] / 0.54 [0.35, 0.72]; executed-only 0.40 / 0.41 | Q1.4 | `eval/e73_nonlinear.json` | P2.8f | |
    30	| N12 | E72 TE names pair 30/96 (chance 1/6); non-executed 0.73 vs executed 0.49 (post hoc) | Q1.4 | `eval/e72_te_diag.json` | P2.14 | |
    31	| N13 | scripted locked gate: MI flags 100% of common-shock controls; pCMI 14% shift / 4% [1, 13] surrogate (shared policy + shock); shared seed flagged 44–100%; TE flags legit leader–follower 100% | Q1.4 | `eval/gate_test.json` | 4.1 | |
    32	| N14 | unequal private costs: level screens false-flag 30/30, pCMI 4/30 | Q1.4 | `p2/costasym_test.json` | P2.4 | |
    33	| N15 | at 1% prevalence no frozen flag reaches point precision 0.25 | Q1.4 | `eval/prevalence.json` | P2.1 | |
    34	| N16 | wording moves no-channel markup −0.19 … +2.56; within-wording markup AUROC 0.66 [0.53, 0.78], pCMI 0.44 [0.30, 0.58] | Q1.4 | `eval/p2_variants.json` | P2.7 | |
    35	| N17 | deepseek C − A +3.75 [2.77, 4.68]; markup 0.99, pCMI 0.57 [0.36, 0.77] | Q1.4 | `eval/p2_family.json` | P2.9 | |
    36	| N18 | E68 double auction: chat raises asks +0.39 [+0.06, +0.69] (inconclusive) | Q1.4 | `eval/` E68 | P2.12 | |
    37	| N19 | independent reimplementation: 422/424 cells agree < 1e-9 | Q1.4 | `reimpl/compare.json` | P2.2 | |
    38	| M1 | combined − better single view −0.01 [−0.09, +0.06] (locked test, n=95) | Q2.2 | `analysis/final_llm_v3_gpt-6.1-sol_test.json` : `contrasts['delta_hybrid[combined]:run_auroc']` | C01 | ✔ (claims table) |
    39	| M2 | pooled fresh −0.07 [−0.17, +0.02] (n=90, post hoc) | Q2.2 | `analysis/p2_pool_rep.json` | C02 | |
    40	| M3 | text 0.47 [0.36, 0.58], action 0.75 [0.65, 0.85] (locked test) | Q2.2 | `analysis/final_llm_v3_gpt-6.1-sol_test.json` : `point_ci.{text,action}.run_auroc` | P2.0 | ✔ (p2_say_vs_do.md) |
    41	| M4 | text inverted in public-inviting families: 0.15–0.36 (Claude 0.22, deepseek 0.36, Qwen3.8 base 0.21, abl. 0.15) | Q2.2 | `analysis/p2_family3way.json`, `analysis/p2_strong_eval_llm_p2qwen{b,a}.json` | P2.0 | ✔ (p2_say_vs_do.md) |
    42	| M5 | invite-regex rate Qwen3.8 channel 0.40 vs control 0.88 (E132, post hoc) | Q2.2 | appendix E132 | TL;DR 3 | |
    43	| M6 | E113 Q1.4-grid Qwen: combined − action −0.24 [−0.37, −0.09]; prices 0.52 [0.41, 0.64]; text 0.32 [0.24, 0.42]; executed-only −0.30 [−0.44, −0.17] | Q2.2 | `analysis/p2_e1_audit.json` | P2.16 | |
    44	| M7 | SALT text auditor 0.87 [0.83, 0.91] (240 ep.); P(said | executed) 0.385 | Q2.2 | `analysis/salt_d1.json` : `E105_audit.auroc`, `E104_sayvsdo.P_said_given_exec` | P2.12 | ✔ (claims table) |
    45	| M8 | premium replicates 0.94 [0.87, 0.99] (60 fresh runs) | Q2.2 | `analysis/replication_llm_p2rep.json` | C05 | ✔ (claims table) |
    46	| M9 | notepad +1.04 [+0.65, +1.42] vs channel +1.61 [+0.92, +2.35]; ratio 0.65 [0.34, 1.32]; placebo +1.23 [+0.76, +1.85]; delivery +0.38 [−0.41, +1.18]; terse paraphrase +0.24 [−0.32, +0.81] | Q2.2 | `analysis/p2_cue_llm_p2cue.json`, `analysis/p2_cue_verdict_llm_p2cue.json` | P2.5 | |
    47	| M10 | memory + profit framing: 19/20 no-channel ≥ Nash + 2; 13/20 channel pairs strict-executed | Q2.2 | P2.7 (`p2_strong*` JSON) | P2.7 | |
    48	| M11 | 14/50 test agreements kept (E84 follow rule) | Q2.2 | P2.4 | P2.4 | |
    49	| M12 | E133e: no-chat LLM 0.94 vs best raw early-price rule 0.885, Δ +0.06 [+0.02, +0.10] (post hoc); say-do gap 0.77; pair SD 0.855 | Q2.2 | `analysis/e133e_attr.json` | P2.17 | |
    50	| M13 | legit cost/quality edges flagged 7/10, 9/10 (controls 2/10); premium precision 0.24 at 5% prevalence | Q2.2 | P2.10, `p2_prevalence` | P2.10 | |
    51	| M14 | monitor-aware sellers agree 0/10, 0/10 (vs 10/10 matched) | Q2.2 | P2.9 | P2.9 | |
    52	| M15 | judge cross-family check: Claude Sonnet 5.5 agrees on y in 115/115 chats | Q2.2 | `label_xfam.json` | Setup | |
    53	| M16 | gpt-6.1-sol newcomer re-agrees 0/20; market stays ≥ Nash + 2 in 18/20 | Q2.2 | P2.15 (E115) | P2.15 | |
    54	| J1 | joint statement (verbatim in both reports) | both | REPORT.md of each | — | |
    55	
    56	Rows without ✔ are copied from the source REPORT.md merge blocks (frozen 07:30) and are to be checked
    57	against JSON in the adversarial-review pass (PLAN deliverable 5).

exec
/bin/bash -lc "git -C /home/factory/collusion/collusion-14-infotheory log -1 --format='%H %s' && git -C /home/factory/collusion/collusion-14-infotheory status --short && git -C /home/factory/collusion/collusion-22-say-vs-do log -1 --format='%H %s' && git -C /home/factory/collusion/collusion-22-say-vs-do status --short" in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
0e06c0327481c3a143cc7f16c097d7e282964d41 iteration 104: honor research freeze; no merge requests
8b680eebaa11826b0b689d8e478d2636391e859c iter113: honor director freeze; no merge requests before 08:00 UTC

exec
/bin/bash -lc 'cat /home/factory/collusion/collusion-22-say-vs-do/results/analysis/claims_denominators.json' in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
[
 {
  "id": "C01",
  "claim": "combined minus better single view, run-AUROC, locked test",
  "expected": "-0.01 [-0.09, +0.06]",
  "denominator": "n=95 runs (llm_v3 locked test split of 125 runs); registered primary contrast",
  "note": "",
  "value": "-0.01 [-0.09, +0.06]",
  "source": "results/analysis/final_llm_v3_gpt-6.1-sol_test.json",
  "key_path": "contrasts['delta_hybrid[combined]:run_auroc']{delta,ci}; n_runs",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C02",
  "claim": "same contrast, two fresh replications pooled",
  "expected": "-0.07 [-0.17, +0.02]",
  "denominator": "n=90 runs (30 llm_v3rep + 60 llm_p2rep, label = channel condition); post hoc pooling of two registered splits",
  "note": "",
  "value": "-0.07 [-0.17, +0.02]",
  "source": "results/analysis/p2_pool_rep.json",
  "key_path": "condition_label.contrasts['delta_hybrid[combined]']{delta,ci}; n; n_by_ds",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C03",
  "claim": "gains above +0.06 (test) / +0.02 (pooled) excluded at 95% (upper CI limits)",
  "expected": "+0.06 / +0.02",
  "denominator": "upper 95% CI limit of C01 (n=95) and C02 (n=90); pooled is post hoc",
  "note": "",
  "value": "+0.06 / +0.02",
  "source": "results/analysis/final_llm_v3_gpt-6.1-sol_test.json + results/analysis/p2_pool_rep.json",
  "key_path": "contrasts[...run_auroc].ci[1]; condition_label.contrasts['delta_hybrid[combined]'].ci[1]",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C04",
  "claim": "a computed pair-statistics table added to the action view gains on test (action_stats minus action)",
  "expected": "+0.11 [+0.04, +0.18]",
  "denominator": "n=95 runs, locked test; registered contrast family (delta_hybrid[action_stats] = action_stats - max(text, action)), not the primary endpoint. Corrected 2026-10-24 16:40: the abstract previously quoted structured (+0.08)",
  "note": "",
  "value": "+0.11 [+0.04, +0.18]",
  "source": "results/analysis/final_llm_v3_gpt-6.1-sol_test.json",
  "key_path": "contrasts['action_stats-action:run_auroc']{delta,ci}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C04b",
  "claim": "adding text to the pair-statistics view does not gain (combined_stats minus action_stats)",
  "expected": "-0.06 [-0.14, +0.01]",
  "denominator": "n=95 runs, locked test; registered contrast family",
  "note": "",
  "value": "-0.06 [-0.14, +0.01]",
  "source": "results/analysis/final_llm_v3_gpt-6.1-sol_test.json",
  "key_path": "contrasts['combined_stats-action_stats:run_auroc']{delta,ci}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C04c",
  "claim": "same pair-statistics gain on fresh data (action_stats minus better single view), two replications pooled",
  "expected": "+0.00 [-0.06, +0.07]",
  "denominator": "n=90 runs (30 llm_v3rep + 60 llm_p2rep, label = channel condition); post hoc pooling; added 2026-10-24 17:57 (iter26 review: test gain did not replicate)",
  "note": "",
  "value": "+0.00 [-0.06, +0.07]",
  "source": "results/analysis/p2_pool_rep.json",
  "key_path": "condition_label.contrasts['delta_hybrid[action_stats]']{delta,ci}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C05",
  "claim": "pair price premium AUROC, fresh replication",
  "expected": "0.94 [0.87, 0.99]",
  "denominator": "n=60 runs (llm_p2rep: 30 private / 20 none / 10 legit); premium selected post hoc after v1; replication registered",
  "note": "",
  "value": "0.94 [0.87, 0.99]",
  "source": "results/analysis/replication_llm_p2rep.json",
  "key_path": "point_ci.premium.run_auroc; n_runs; group_n",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C06",
  "claim": "unread pricing notepad premium as share of channel premium (rounds 2-12)",
  "expected": "65% (1.04/1.61)",
  "denominator": "n=15 seeds per arm (llm_p2cue: notes vs none, private vs none, paired by seed); gpt-6-luna; registered arms, ratio is derived",
  "note": "",
  "value": "65% (1.04/1.61)",
  "source": "results/analysis/p2_cue_llm_p2cue.json",
  "key_path": "paired['notes-none'].prem_r2_12[0] / paired['private-none'].prem_r2_12[0]; n",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C07",
  "claim": "legitimate cost / quality edges flagged by premium vs controls",
  "expected": "7/10, 9/10 vs 2/10",
  "denominator": "10 runs per condition (highcost, quality, plus 10 no-channel reference runs from llm_p2cue); gpt-6-luna; frozen dev threshold 0.667",
  "note": "",
  "value": "7/10, 9/10 vs 2/10",
  "source": "results/analysis/p2_asym.json",
  "key_path": "conditions.{highcost,quality,none_ref_p2cue}.premium_flags",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C08",
  "claim": "text views flag every control (no-channel) market for Claude, deepseek, Qwen base+abliterated",
  "expected": "100% (5/5, 15/15, 15/15, 15/15)",
  "denominator": "control (condition=none) markets: Claude 5, deepseek 15, Qwen-base 15, Qwen-abliterated 15; text view; families differ by model so cross-family comparison is associative; registered predictions (E95) for Claude/deepseek",
  "note": "",
  "value": "100% (5/5, 15/15, 15/15, 15/15)",
  "source": "results/analysis/p2_family3way.json + results/analysis/p2_strong_eval_llm_p2qwena.json + results/analysis/p2_strong_eval_llm_p2qwenb.json",
  "key_path": "llm_p2{claude,ds}.views.text.flags_by_class.PUB; llm_p2qwen{a,b}.detectors.text.flags.none",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C09",
  "claim": "text-view run AUROC range across those control-flagging families (private vs none)",
  "expected": "0.15-0.36",
  "denominator": "run AUROC private vs none, text view: Claude n=10, deepseek n=30, Qwen-base n=30, Qwen-abl n=30 runs; TL;DR claim (not in abstract text)",
  "note": "",
  "value": "0.15-0.36",
  "source": "results/analysis/p2_family3way.json + results/analysis/p2_strong_eval_llm_p2qwen{a,b}.json",
  "key_path": "views.text.auroc_private_vs_none[0] (min,max over 4)",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C10",
  "claim": "SALT-NLP episodes",
  "expected": "8000",
  "denominator": "episodes = 7998 with valid judge label + 2 invalid-judge episodes; 800 runs; external data (SALT-NLP)",
  "note": "",
  "value": "8000",
  "source": "results/analysis/salt_d1.json",
  "key_path": "E104_sayvsdo.n_episodes + n_invalid_judge; crosstab sum",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C11",
  "claim": "SALT distinct models",
  "expected": "10",
  "denominator": "distinct model names parsed from per_condition ids (main__X and cross_model__A__B); 16 conditions x 500 episodes",
  "note": "",
  "value": "10",
  "source": "results/analysis/salt_d1.json",
  "key_path": "E104_sayvsdo.per_condition[*].condition (parsed)",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C12",
  "claim": "share of executed SALT episodes with no explicit agreement (1 - P(said|exec))",
  "expected": "62% (P(said|exec)=0.385)",
  "denominator": "executed episodes n=5169 (1989 said + 3180 not said), 7998 judged; Qwen judge label for 'said'; episodes are clustered in 800 runs (check CI method in salt script)",
  "note": "",
  "value": "62% (P(said|exec)=0.385)",
  "source": "results/analysis/salt_d1.json",
  "key_path": "E104_sayvsdo.P_said_given_exec.est; crosstab.exec1_*",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C13",
  "claim": "test 'colluders' that keep their agreement",
  "expected": "14/50",
  "denominator": "n=50 judged-agreement private runs among the 95 llm_v3 test runs (14 followed + 36 not followed); behaviour labels registered (E84)",
  "note": "",
  "value": "14/50",
  "source": "results/analysis/p2_behaviour.json",
  "key_path": "datasets.llm_v3.class_counts.{followed,not_followed}; n",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C14",
  "claim": "strict-executed channel pairs (memory + profit objective)",
  "expected": "13/20",
  "denominator": "20 channel markets (llm_p2strongF, seeds 9800000-9800019); strict rule fixed in registered amendment E99-amend; Jeffreys [0.43, 0.83]",
  "note": "",
  "value": "13/20",
  "source": "results/analysis/p2_strong_classes_llm_p2strongF.json",
  "key_path": "n_strict_executed",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C15",
  "claim": "no-channel markets that price >= Nash + 2 (tacit-high)",
  "expected": "19/20",
  "denominator": "20 no-channel markets (paired seeds with C14); tacit-high rate >= 0.5 registered (E99amend); Jeffreys [0.79, 0.99]",
  "note": "",
  "value": "19/20",
  "source": "results/analysis/p2_strong_classes_llm_p2strongF.json",
  "key_path": "n_tacit_high_none",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C16",
  "claim": "paired excess private - none (market price over cost-adjusted Nash)",
  "expected": "-0.44 [-1.84, +1.00]",
  "denominator": "n=20 paired seeds; registered prediction E99_P3 (excess > 0) FAILED; unresolved",
  "note": "",
  "value": "-0.44 [-1.84, +1.00]",
  "source": "results/analysis/p2_strongF_report_llm_p2strongF.json",
  "key_path": "E99_P3.paired_excess_private_minus_none; n_pairs",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C17",
  "claim": "private-plan LLM monitor AUROC, strict-executed vs tacit-high",
  "expected": "0.76 [0.55, 0.93]",
  "denominator": "13 strict-executed vs 19 tacit-high markets; EXPLORATORY (E103 plan view registered before plan calls, but classes defined post hoc); CI [0.55, 0.93]",
  "note": "",
  "value": "0.76 [0.55, 0.93]",
  "source": "results/analysis/p2_strong_eval_llm_p2strongF.json",
  "key_path": "detectors.plan.auroc_strict_vs_tacit_high (== keyword file detectors.plan_view...); groups_n",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C18",
  "claim": "no-LLM count of plans naming the chat partner, same contrast",
  "expected": "0.82 [0.66, 0.96]",
  "denominator": "13 vs 19 markets; EXPLORATORY post hoc keyword detector (E111) K_dir; CI [0.66, 0.96]",
  "note": "",
  "value": "0.82 [0.66, 0.96]",
  "source": "results/analysis/p2_plan_keyword_llm_p2strongF.json",
  "key_path": "detectors.K_dir.auroc_strict_vs_tacit_high; n_pos_strict; n_neg_tacit_high",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C19",
  "claim": "no plan uses agreement words",
  "expected": "0/13 strict, 0/19 tacit-high",
  "denominator": "13 strict + 19 tacit-high (+7 non-executed) markets; keyword K_terms; exploratory",
  "note": "",
  "value": "0/13 strict, 0/19 tacit-high",
  "source": "results/analysis/p2_plan_keyword_llm_p2strongF.json",
  "key_path": "runs_with_term_in_any_plan",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C20",
  "claim": "public-text view AUROC, strict-executed vs tacit-high (inverted)",
  "expected": "0.25 [0.08, 0.46]",
  "denominator": "13 vs 19 markets; EXPLORATORY (E99-x, added after generation began, before detector scores); CI [0.08, 0.46]",
  "note": "",
  "value": "0.25 [0.08, 0.46]",
  "source": "results/analysis/p2_strong_eval_llm_p2strongF.json",
  "key_path": "detectors.text.auroc_strict_vs_tacit_high",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C21",
  "claim": "abliterated vs base Qwen: executed markets each arm; agreement at ceiling",
  "expected": "13/15; 13/15",
  "denominator": "15 vs 15 private markets (llm_p2qwena vs llm_p2qwenb); execution diff 0.00 [-0.26, +0.26] Newcombe; agreement 15/15 both; registered (C3), predictions not supported",
  "note": "",
  "value": "13/15; 13/15",
  "source": "results/analysis/p2_qwen_cmp.json",
  "key_path": "P2_executed_rate.abliterated; P2_executed_rate.base; P1_agreement_rate",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C22",
  "claim": "SALT-NLP: gpt-6.1-sol text auditor AUROC for execution",
  "expected": "0.87 [0.83, 0.91]",
  "denominator": "n=240 sampled SALT episodes (120 executed; 79 tacit) audited by gpt-6.1-sol (E105); external data",
  "note": "",
  "value": "0.87 [0.83, 0.91]",
  "source": "results/analysis/salt_d1.json",
  "key_path": "E105_audit.auroc{est,ci}; n; n_exec",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C21b",
  "claim": "abliterated vs base Qwen: Q2.2 strict-executed each arm (lower-bound compliance)",
  "expected": "5/15; 5/15",
  "denominator": "15 private markets per model; Q2.2 strict: F>=12, both pair prices>=F-1 in >=50% of later rounds, >=10 later rounds, post-agreement pair excess>=2; p2_strong.py via p2_strong_eval.py, not a +/-1 band or Q1.4 E70 rule",
  "note": "",
  "value": "5/15; 5/15",
  "source": "results/analysis/p2_strong_classes_llm_p2qwena.json",
  "key_path": "n_strict_executed (qwena; qwenb)",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C23",
  "claim": "abliterated minus base Qwen: paired channel premium difference",
  "expected": "-1.24 [-2.41, -0.03]",
  "denominator": "15 vs 15 private markets with matched none; bootstrap; registered P3 (abliterated >= base) not supported; bf16 vs FP8 serving confound",
  "note": "",
  "value": "-1.24 [-2.41, -0.03]",
  "source": "results/analysis/p2_qwen_cmp.json",
  "key_path": "P3_paired_premium.diff_boot95",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C24",
  "claim": "E116 within channel: plan view AUROC strict-executed vs non-executed",
  "expected": "0.69 [0.44, 0.91]",
  "denominator": "13 strict vs 7 non-executed private markets (llm_p2strongF); exploratory, zero LLM calls, seed bootstrap",
  "note": "",
  "value": "0.69 [0.44, 0.91]",
  "source": "results/analysis/p2_within_agree_llm_p2strongF.json",
  "key_path": "views.plan.auroc_strict_vs_nonexec",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C27",
  "claim": "E116b within agreement, Qwen abliterated / base: public text AUROC strict vs non-executed",
  "expected": "0.73 [0.43, 0.99]; 0.51 [0.25, 0.70]",
  "denominator": "5 strict vs 10 non-executed private markets per model (llm_p2qwena, llm_p2qwenb; 15/15 judged agreement each); exploratory, not pooled",
  "note": "",
  "value": "0.73 [0.43, 0.99]; 0.51 [0.25, 0.70]",
  "source": "results/analysis/p2_within_agree_llm_p2qwen{a,b}.json",
  "key_path": "views.text.auroc_strict_vs_nonexec",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C25",
  "claim": "E112 participant replacement (luna newcomer), private arm: market excess replaced - original; re-agreement replaced; originals",
  "expected": "+0.20 [-0.08, +0.62]; 16/20; 15/20",
  "denominator": "20 paired private games replayed from llm_p2strongF, newcomer from round 21, rounds 21-40; registered E112, all 4 predictions held; none arm +0.16 [-0.27, +0.57] in P2.15",
  "note": "",
  "value": "+0.20 [-0.08, +0.62]; 16/20; 15/20",
  "source": "results/analysis/p2_replace.json",
  "key_path": "arms.private.O1_market_repl_minus_orig; arms.private.O4_reagreement_floor_ge13.{repl,orig}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C28",
  "claim": "E115 participant replacement (gpt-6.1-sol newcomer), private arm: re-agreement replaced; markets >= Nash + 2 replaced",
  "expected": "0/20; 18/20",
  "denominator": "same 20 paired private games as E112, sol newcomer from round 21; registered E115, S1 failed, S2-S4 held; none arm 9/10 in P2.15",
  "note": "",
  "value": "0/20; 18/20",
  "source": "results/analysis/p2_replace_sol.json",
  "key_path": "arms.private.O4_reagreement_floor_ge13.repl; arms.private.O6_market_excess_ge2.repl",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C29",
  "claim": "E120 definition sensitivity (P2.7 body): strict-executed one-at-a-time range; full grid; tacit-high range",
  "expected": "10-16/20; 7-18/20; 17-20/20",
  "denominator": "llm_p2strongF, frozen judge terms, 81 threshold combinations; exploratory, zero LLM calls; registered 13/20 reproduced",
  "note": "",
  "value": "10-16/20; 7-18/20; 17-20/20",
  "source": "results/analysis/p2_strict_sensitivity.json",
  "key_path": "strict_range_one_at_a_time; strict_range_all; tacit_high[].k",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C30",
  "claim": "E112/E115 post-replacement executed counts under registered replacement O5 (not Q2.2 strict)",
  "expected": "15/20; 14/20; 0/20; 14/20",
  "denominator": "20 paired private games per replacement arm; O5: judged post-r20 agreement F>=13, both pair prices>=F-1 in >=50% of later rounds, >=5 later rounds, post-agreement pair excess>=2; same rule for originals; REPORT P2.7/P2.15",
  "note": "",
  "value": "15/20; 14/20; 0/20; 14/20",
  "source": "results/analysis/p2_replace.json; results/analysis/p2_replace_sol.json",
  "key_path": "arms.private.O5_executed_after_r21.{repl,orig}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C31",
  "claim": "E113 Qwen cell-stratified combined minus action / text AUROC",
  "expected": "-0.24 [-0.37, -0.09]; -0.05 [-0.13, +0.03]",
  "denominator": "8 Qwen cells x 6 matched seeds x 2 arms = 96 games of Q1.4 E70's 192; channel assignment label; equal-cell mean of within-cell AUROC differences; game bootstrap within cell x arm, B=2000 seed=0; E113-amend3 registered before scores; shared Q1.4 data, not independent joint replication",
  "note": "",
  "value": "-0.24 [-0.37, -0.09]; -0.05 [-0.13, +0.03]",
  "source": "results/analysis/p2_e1_audit.json",
  "key_path": "amend3.qwen_stratified_combined_minus_{action,text}.{delta,ci,n_cells}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C32",
  "claim": "E113 combined-minus-best-single cell signs: Qwen positive/tie/negative; all cells positive/tie/negative",
  "expected": "0/8; 0; 8; 4/16; 1; 11",
  "denominator": "8 Qwen cells and all 16 Q1.4 E70 cells, 6 games per arm per cell; best-single max selection biases delta downward; ties count toward registered P1, so held P1 is weak confirmation",
  "note": "",
  "value": "0/8; 0; 8; 4/16; 1; 11",
  "source": "results/analysis/p2_e1_audit.json",
  "key_path": "amend3.{qwen,all}_sign_counts; b_cells_combined_gt_best_single; b_P1_held",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C33",
  "claim": "E113 Qwen text inversion and flags in channel / no-channel arms",
  "expected": "0.32 [0.24, 0.42]; 48/48; 48/48",
  "denominator": "96 games in 8 Qwen E70 cells (48 channel, 48 no-channel); unstratified pooled text AUROC and frozen dev threshold flags; game-bootstrap CI, not an independent replication of Q1.4 data",
  "note": "",
  "value": "0.32 [0.24, 0.42]; 48/48; 48/48",
  "source": "results/analysis/p2_e1_audit.json",
  "key_path": "pooled_auroc_channel_vs_none_descriptive.text_qwen; a_text_flag_rate_by_arm_qwen.{1,0}",
  "status": "OK",
  "in_report_abstract": true
 },
 {
  "id": "C34",
  "claim": "E133e no-chat LLM minus best raw early-price rule score; oriented say-do gap and pair SD AUROC",
  "expected": "+0.06 [+0.02, +0.10]; 0.77; 0.855",
  "denominator": "78 Q1.4 E70 grid agreed games (48 held / 30 not); post hoc robustness declared before computing (E133e-reg); paired game bootstrap; 0 LLM calls",
  "note": "",
  "value": "+0.06 [+0.02, +0.10]; 0.77; 0.855",
  "source": "results/analysis/e133e_attr.json",
  "key_path": "b_llm_E133d_minus_raw.rule_score; a_oriented_auroc_smaller_is_held.{say_do_gap,pair_sd_0_5}[0]",
  "status": "OK",
  "in_report_abstract": true
 }
]

exec
/bin/bash -lc "rg -n 'execut|pre.register|post.hoc|Joint|Detectability|13/20|19/20|0.39|0.94|0.34|0.42|422|nine|Seven|seven|1001|factor|1e-9' /home/factory/collusion/collusion-14-infotheory/REPORT.md" in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
7:- A private chat channel raised prices in all nine main sets (7 seller models).
9:- Even agreements that were actually executed show no detected co-movement: pCMI 0.42 [0.33, 0.53] on 48 executed games.
12:- Of the dependence statistics, only lagged dependence (TE, 0.62) is weakly above chance, still (barely) below level (paired Δ +0.12 [+0.01, +0.22]), and it sits mainly in channel games whose agreement was not executed (exploratory, untested split).
14:**Main claim (v1 + Phase 2).** In our LLM pricing markets, assigning a private channel shows up as a sustained price *level* (spreading to rivals in the gpt-6-luna sets), with no detected contemporaneous co-movement of prices: the channel raised markup over Nash in 9/9 sets (7 seller models; C − A CI > 0 in each), and max-pair markup had a higher point-estimate run AUROC than pCMI in 9/9 (0.75–0.99 vs 0.34–0.72), with the paired Δ level − pCMI CI > 0 in 8/9 sets (E74, declared, same games; per-set 95% CIs, uncorrected; unresolved only for gpt-5.6-luna, +0.03 [−0.27, +0.33]; smallest resolved Δ +0.22 [+0.03, +0.44], base Qwen3.6), while pCMI's CI includes 0.5 in 8/9. This holds at T=60 (pre-registered E44: pCMI 0.34 [0.18, 0.52]), and restricting to executed agreements does not raise pCMI (0.42 [0.33, 0.53], 48 executed games; the level is inflated by construction on that subset, P2.11). Level and co-movement screens fail in opposite places (unequal private costs: level screens false-flag 30/30 scripted markets, pCMI 4/30), and level screens need model- and prompt-matched references, because the no-channel baseline moves with wording and model and is tacit-high (defined below) for an older model (9/10) or under strong profit framing (19/20, Q2.2's arm). The scope is *detected* co-movement in these markets: at T=60 no co-move excess is detected (+0.004 [−0.007, +0.015]), where pCMI detects a planted shared ±1 move at q = 0.1 (AUROC 0.79 [0.70, 0.88]), but at T=20 (most sets, all of E70) the same planting gives only 0.62 [0.52, 0.71], so small co-movement is not excluded there; this bounds sensitivity to that planting, not to every collusive strategy (P2.8). The null is not specific to the linear-Gaussian estimator: a rank-based (copula) pCMI and a discrete sign-change CMI are also at chance on E70, E44 and the executed-only set (E73, declared robustness, P2.8). Lagged dependence is not excluded: in the registered 16-cell grid (E70, 192 games) transfer entropy is weakly above chance (0.62 [0.54, 0.70]; declared secondary hypothesis confirmed), though below max-pair markup (0.74 [0.66, 0.81]; paired Δ +0.12 [+0.01, +0.22], E74); in an exploratory follow-up (E72) TE names the channel pair in 30/96 games (chance 1/6), and the signal sits in non-executed channel games (0.73) rather than executed ones (0.49; post hoc, difference untested) (P2.14).
16:*Terms (used throughout).* C / A = channel / no-channel arm (matched seeds and prompt otherwise). C − A = difference in mean all-seller markup over the per-round Nash price. Max-pair markup (`market_level`; "level" / "market level" below) = the highest pair's mean price over Nash, a run-level score; pair_level = pair mean minus the other two sellers' mean. pCMI = max-pair Gaussian conditional MI of current prices given public state and all sellers' lagged prices; TE = max-pair, max-direction transfer entropy (lagged dependence, not signed following). Executed = judge-labelled agreement AND both pair firms ≥ agreed − 1 in ≥ ½ of post-agreement rounds AND second-half pair mean ≥ Nash + 2 (our implemented rule, not Q2.2's; 13–78/149 executed under 27 variants, E71). Tacit-high = a no-channel market whose second-half mean is ≥ Nash + 2 (a price threshold, not verified coordination). Co-move excess = the assigned pair's share of same-direction price moves minus the other five pairs' mean (P2.8); q = per-round probability of a planted shared ±1 move. Sign tests are one-sided.
19:Can a prices-only detector find colluding agents without accusing agents sharing a shock or model? We compare dependence statistics (MI, pCMI = Gaussian conditional MI given public state and lagged prices, transfer entropy TE) with price-level screens in a 4-seller price market. **Scripted sellers:** pCMI flags every planted shared-signal pair and cuts MI's common-shock false alarms from 100% to 14%; level screens fail where pCMI does not (unequal costs: 30/30 vs 4/30 false flags). **LLM sellers** (9 sets, 7 models, 10–21 games per arm): a private channel raised markup over Nash in 9/9 sets, but as a level: max-pair markup beat pCMI in 9/9 (AUROC point estimates 0.75–0.99 vs 0.34–0.72; paired difference CI > 0 in 8/9), and pCMI's CI included 0.5 in 8/9 (base Qwen3.6 exception, 0.71 [0.51, 0.88], not replicated in E70). Longer games (pre-registered, T=60: pCMI 0.34 [0.18, 0.52]), executed agreements only (48/149; pCMI 0.42 [0.33, 0.53]) and memory (inconclusive) revealed no co-movement. A 16-cell, seven-factor grid (E70, 192 games, public board on) is consistent: C − A positive in 13/16 cells, level > pCMI in 12/16 (point estimates), pooled pCMI 0.51 [0.43, 0.59]; only lagged TE is weakly above chance, 0.62 [0.54, 0.70]; a declared follow-up found no confirmed model effect. With gpt-6-luna the level spreads to rivals. Absolute screens need model- and prompt-matched references: wording moves no-channel markup −0.19 to +2.56; an older model or profit framing makes it tacit-high. Refusal-removed Qwen did not collude detectably more (3/3 pairs). In a double auction, chat barely raised asks (+0.39 [+0.06, +0.69]; detectors inconclusive). At 1% prevalence no flag's point-estimate precision reaches 0.25.
22:> Claim: channel assignment raises the market price level more reliably than detected co-movement (9/9 main sets, 7 models; paired Δ level − pCMI CI > 0 in 8/9 sets, all but gpt-5.6-luna +0.03 [−0.27, +0.33], E74 `eval/e74_paired_diff.json`; E70 grid: level > pCMI point estimate in 12/16 cells, 192 games, pooled pCMI 0.51 [0.43, 0.59], but lagged-dependence TE 0.62 [0.54, 0.70], weakly above chance, declared, below level by +0.12 [+0.01, +0.22] (E74), `eval/e70_grid.json`; exploratory E72 (`eval/e72_te_diag.json`): TE names the pair 30/96 vs chance 1/6, and the signal sits in non-executed channel games, 0.73 vs executed 0.49, post hoc, untested); base Qwen3.6's pCMI exception (0.71) did not meet the declared replication criterion in E70's qwen cells (0.46 [0.35, 0.58]; different design, board on). "Level" = max-pair markup over Nash; definitions in *Terms* under the main claim.<br>
23:> Long games: T=60, 20 channel + 20 controls, pCMI AUROC 0.34 [0.18, 0.52] versus market level 0.94 [0.86, 1.00] (P2.8, `eval/long_power_llm_long_p2_T60.json`).<br>
24:> Executed only (our rule in *Terms*, not Q2.2's; 13–78/149 under 27 variants, pooled pCMI 0.343–0.531, E71): 48/149 channel games across ten sets; pooled within-set pCMI versus their no-channel controls 0.42 [0.33, 0.53]; execution selects prices above Nash (P2.11, `eval/p2_partc.json` E64_pooled).<br>
26:> Estimator robustness (E73, declared, zero calls): rank-based copula pCMI and discrete sign-change CMI are also at chance (E70 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52]; E44 T=60 0.40 [0.23, 0.58] / 0.54 [0.35, 0.72]; executed-only 0.40 / 0.41) (P2.8f, `eval/e73_nonlinear.json`).<br>
27:> Figure to lift: `figures/phase2_headline.png` (nine main sets, game-bootstrap CIs; source/reproduction immediately below).<br>
28:> Joint statement: immediately below the figure. Shared inference: neither words nor co-movement establish execution here; Q2.2 E116's within-agreement text/plan intervals span chance, while our executed-only pCMI remains near chance against controls (different contrasts).<br>
29:> Do not quote as headline evidence: per-cell E70 AUROCs, E61's unreplicated exploratory A-arm effect, or E65's exploratory TE. E70's seven main effects are descriptive (resolution IV, 6 + 6 games per cell, no multiplicity control); the declared fresh-sample follow-up on model (12 + 12 per level): C − A +0.88 (gpt-6-luna) vs +1.96 (qwen-3.6-35b), difference +1.07 [−0.20, +2.41], not confirmed (`eval/e70_followup.json`), so no factor is shown to move the premium. E68 (external CDA) is an inconclusive external check: chat raises asks by only +0.39 [+0.06, +0.69] of a 20-unit surplus (15 + 15); quote it as such, not as support.
35:*Phase 2 overview: all nine P2.13 main sets (seven seller models), channel − no-channel markup and run AUROC with game-bootstrap 95% CIs. Scores target channel assignment, not execution; these sets share designs/models. Base Qwen3.6 is the pCMI exception (lower CI 0.507; not replicated in E70's design, P2.14). Regenerate from saved `p2_partc.json` and `claims_denominators.json`: `uv run python scripts/phase2_fig.py`.*
37:*Joint statement with Q2.2 (verbatim in both reports):* "Detectability of LLM collusion by any price statistic is a property of the (seller
38:model × prompt) pair. Relative screens survive a shared model but fail under market-wide spillover; absolute screens need model- and prompt-matched references." "With memory and a profit objective, gpt-6-luna sellers raise prices market-wide without any channel (19/20 no-channel markets ≥
39:Nash + 2); agreements are then often kept (13/20) but add no detectable price, so channel labels stop being ground truth. Abliterated Qwen
40:with memory differs (channel adds +2.13 [1.28, 3.00]; 5/20 executed), as the first sentence predicts." (luna numbers: Q2.2's strong-framing arm, re-scored here as E66 with 0 class mismatches; Qwen numbers: our E65, T = 40. In our sets with spillover the relative pair_level screen loses power rather than failing outright: AUROC 0.75–0.80 vs market level 0.85–0.94 in `llm_v1`, E44 and E65.)
44:`EXPERIMENTS.tsv` (E43–E74); most before their data exist, but some analyses (e.g. E60, E64, E67's exploratory sets, E71) reuse existing data and are labelled exploratory or post-hoc in their sections. No detector setting is tuned on any new dataset (`data/SPLITS.md`, "Phase 2"); each analysis is labelled confirmatory (declared before data) or exploratory in its section.
45:Status: all nine gaps are closed and Part C is final (E61–E67, E69; P2.11). **E70 factorial grid** (Part E1, 16 cells, 192 games, registered before data): channel markup positive in 13/16 cells, level > pCMI in 12/16, pCMI 0.51 [0.43, 0.59], base-Qwen pCMI exception not replicated (P2.14); its declared follow-up on factor M did not confirm a model effect (+1.07 [−0.20, +2.41], `eval/e70_followup.json`). Final and declared: E44 long games (**level, not short**, P2.8), E65 strong arm (inconclusive), E66 (not evaluable: 19/20 no-channel markets tacit-high), E69 (abliteration null replicates, −0.65 [−1.97, +0.65]). E68 (D2, external double auction): inconclusive; chat barely raises asks (+0.39 [+0.06, +0.69]). Dropped: glm-5.2 (0 complete games); the gpt-6-luna memory pilot is descriptive only.
53:| shared | independent reimplementation | 422/424 run × statistic cells agree < 1e-9 (2 differ only in the ρ² cap); all 20 AUROCs identical; shift-null flags 4/21 vs 5/21 (Monte Carlo); no bug | `reimpl/compare.json` | P2.2 |
55:| 2 | long games (E44: T=60, 20 + 20, pre-registered) | **level, not short**: pCMI AUROC 0.34 [0.18, 0.52] at T=60 (0.52 at T=20); market level 0.94 [0.86, 1.00]; observed co-move excess +0.004 [−0.007, +0.015] < q = 0.1 planting (+0.13, pCMI 0.79); pair premium +0.70 → +0.23: rivals stay elevated while no-channel markets fall (spillover +2.24 of +2.47, rounds 51–60); executed 4/20, tacit 0/20 | `eval/long_power_llm_long_p2_T60.json`, `eval/spillover_llm_long_p2_T60.json` | P2.8 |
64:| D2 | external double auction (E68, qwen-3.6-35b, 15 + 15) | **inconclusive**: chat ask effect +0.39 [+0.06, +0.69] (≈2% of surplus); level AUROC 0.68 [0.46, 0.88], pCMI 0.60 [0.40, 0.80]; paid prices +2.61 vs +2.01; 18 parse failures in 14/30 runs | `eval/e68_cda.json` | P2.12 |
65:| C | executed collusion, abliteration, model generations, memory (E61–E67) | executed 48/149 C games over ten sets (E44 T=60: 4/20 [0.07, 0.41]); tacit-high (no channel) 1/144 under our framing for current models, but 9/10 for older gpt-5.6-luna and 19/20 under Q2.2's strong framing (E66) (markup AUROC falls to 0.75); abliterated − base (C − A): no detectable increase in 3/3 Qwen pairs (E61 −0.37 [−2.09, 1.36], E69 −0.65 [−1.97, 0.65], Q2.2, pair premium not C − A, −1.24 [−2.41, −0.03]); executed-only pooled pCMI 0.42 [0.33, 0.53] vs 0.52 non-executed (market_level on that subset is inflated by construction, 0.99; pair_level is not, 0.87 [0.80, 0.94]); E69 base Qwen3.6 is the one set with pCMI CI > 0.5 (0.71 [0.51, 0.88]; market level 0.93); E65 memory arm (T=40): markup 0.85, pCMI 0.49, declared executed-only pCMI test inconclusive (0.33 [0.02, 0.66], 5/20 executed; the pilot's 5/5 did not replicate); E66 (Q2.2 strong framing, gpt-6-luna, T=40): executed 13/20 but tacit 19/20 without a channel, so channel vs no-channel is 0.46 on pCMI and 0.44 on market level (nothing separates; declared test not evaluable); E67 stickiness screen: 1 of 3 confirmatory sets (E65 0.90; gpt-5.6-luna 0.46, E66 0.42), so the stickiness explanation of low pCMI is not supported; glm-5.2 dropped | `eval/p2_partc.json` | P2.11 |
66:| E1 | generality over 7 design factors (E70, 2^(7−3) grid, 16 cells × 6 + 6, registered) | channel C − A positive in 13 / 0 / 3 cells (pos / tie / neg; one-sided sign p = 0.011), pooled +0.98 [0.65, 1.29]; level > pCMI 12 / 1 / 3; pooled AUROC level 0.74 [0.66, 0.81], pCMI 0.51 [0.43, 0.59], TE 0.62 [0.54, 0.70] (declared secondary: confirmed); qwen pCMI exception not replicated 0.46 [0.35, 0.58]; largest main effects M (= model incl. ≈100% vs 4–10% public-board use) +0.79 [0.10, 1.44], cost +0.79 [0.12, 1.41] (descriptive); follow-up on M not confirmed: +1.07 [−0.20, +2.41] (12 + 12 per level) | `eval/e70_grid.json` | P2.14 |
72:(4) **Level screens detect "a pair singled out by the prompt", not delivered coordination:** an undelivered notepad (0/14 agreements) is named 11/15 vs private 12/15 (P2.10); Q2.2 E77 finds notes-to-self yields 0.65 [0.34, 1.32] of the private premium (sibling result, not regenerated here). Deepseek pairs agree 15/15 but follow 3/15, and abandoned pairs still sit +3.23 above rivals (P2.9d). A public board alone raises deepseek no-channel markup by +0.70 [0.23, 1.23] and makes a frozen level screen flag 5/15 of those markets (P2.9e), so the reference must also match the board.
75:(7) **Long games do not rescue pCMI (E44, pre-registered, decisive for Q1.4).** At T=60, pCMI scores 0.34 [0.18, 0.52] (the declared rule rejects AUROC ≥ 0.65); its point estimate falls with game length (0.52 at T=20; change −0.18 [−0.40, +0.05], not significant), while the market level holds at 0.94. Channel pairs show no detectable co-move excess (+0.004 [−0.007, +0.015]), although pCMI separates a planted shared ±1 move at q = 0.1 in the same games (AUROC 0.79). In this set (gpt-6-luna, T=60) channel pairs show a sustained level and no detectable co-move excess (P2.8). pCMI does not detect the channel either when only *executed* agreements count (pooled pCMI 0.42 [0.33, 0.53], ten sets) and when sellers get memory (E65, T=40: markup AUROC 0.85, pCMI 0.49; declared executed-only test inconclusive, 0.33 [0.02, 0.66], n = 5 executed) (P2.11).
100:| 5 | …but as a level: level statistics beat pCMI | run AUROC markup 0.87 [0.78, 0.94] (`llm_v1`), pair_level 0.98 [0.95, 1.00] (`llm_v3`) vs pCMI 0.45 [0.32, 0.59], 0.52 [0.39, 0.64] | §4.3.3–4.3.7 |
103:| 8 | The first pair member's provisional price is above rivals' before it reads any partner message | `llm_v1` first-sender provisional price − rivals +0.94 [0.38, 1.59] vs whole game +0.45 [0.34, 0.57] (exploratory, descriptive) | §4.3.11 |
111:We build a 4-seller repeated differentiated-price market with public demand/cost shocks and ask whether pairwise dependence detectors that read **prices and public market state only** (no messages) can find colluding pairs without accusing sellers that merely share a shock or a policy. Detectors: |Pearson|, mutual information (MI), CMI given public state, Gaussian CMI given state **and all lagged prices** (pCMI), and lagged CMI (TE), each compared with two baselines: the same game with seller price series circularly shifted out of alignment (shift null) and comparable no-channel markets (control-surrogate null). **Scripted agents, locked test seeds (T=100, 50 runs/group):** every contemporaneous detector flags and localises a planted shared-signal pair in 100% of runs. Raw MI also flags 100% of markets whose independent sellers share a public shock. pCMI flags 14% of them under the shift null. The surrogate null (which uses those markets as its reference pool, so ≈5% there by construction) flags only 4% [1, 13] of held-out markets with a shared policy plus common shock, and 4% with a public leader-follower pair. Two confounds remain: policy copies that share their random seed (48–100% flagged by each contemporaneous detector in Table 4.1; 44% for differenced |Pearson|, §4.1), and lagged matching, where TE flags legitimate leader-follower pricing in 100% of runs. Dependence detects coordinated *variation*, not agreement. A constant high price (the tested stay-high setting) was not reliably localised by any of these estimators. **LLM sellers** (gpt-6-luna; our market `llm_v1`, 74 games, T=20; sibling market `llm_v3`, 125 runs, T=12): a private channel produces judge-verified agreements and raises markup over the competitive (Nash) price in `llm_v1` by +1.8 versus matched no-channel markets (C − A [1.2, 2.3], D − B [1.0, 2.5]), but the effect is mainly a **price level**. Level statistics separate channel from control runs (run AUROC: `llm_v1` markup 0.87 [0.78, 0.94]; `llm_v3` pair_level 0.98 [0.95, 1.00]). pCMI is not distinguishable from chance (`llm_v1` 0.45 [0.32, 0.59]; `llm_v3` 0.52 [0.39, 0.64]), and in an exploratory leave-one-run-out logistic model, adding it to markup gave no detectable improvement (−0.02 [−0.08, +0.01]). Longer games (T=50, 8 vs 8) did not meet the pre-declared rescue criterion (pCMI 0.45 [0.16, 0.75] vs markup 0.95; the CI cannot exclude moderate effects). In mixed gpt-6.1-sol/gpt-6-luna markets, no pCMI same-model excess over cross-model pairs was detected (+0.003 [−0.025, +0.032], 12 games; only large effects excluded). Supported claim: in these two markets at T=12–50, the private channel shows up mainly as a price level, which conditioned dependence measures are built to ignore; level statistics discriminate channel assignment far better than pCMI. Some coordinated variation is present (pair localisation on first differences in `llm_v3`; part of it also appears in placebo runs, §4.3.9), and whether pCMI fails because the effect is mostly a level or because of low power at short T is not fully settled. An exploratory injection check (§4.3.8) plants per-round shared ±1 price shocks (in 20% of rounds) into one pair of real LLM control games: pCMI detects them at T=50 (AUROC 0.93 [0.87, 0.98]) but only weakly at T=20 (0.63–0.66), and the real channel pairs show no statistically detected excess co-movement relative to rivals. That fits the level reading but does not settle it. Level screens separate channel *assignment* but are not collusion-specific (they rank legitimate public partnerships above controls, AUROC 0.75; in the sibling market an offered-but-undelivered placebo channel gave a similar premium, and pair_level named the pair about equally often, 13.5/15 vs 14/15, §4.3.9). In exploratory sibling monitor/firm-framing strata with no judge-labelled agreements, pair_level yielded 3.3/30 tie-averaged hits (chance expectation 5.0; §4.3.10); framing and agreement are confounded. In our own market, the first pair member to write pre-play already sets a provisional price above its rivals while writing its own first private message, before receiving any partner message (+0.94 [0.38, 1.59] vs whole-game premium +0.45; exploratory, descriptive, not a causal offer effect, §4.3.11).
175:battery and power sweeps reported as headline numbers use locked seeds 1001/1002, run once with the frozen
184:### 4.1 Positive control and hard negatives (scripted, LOCKED test seed 1001, T=100, s=0.6, 50 runs per group)
185:`uv run python -m experiments.scripted both --name gate_test --n 50 --T 100 --strength 0.6 --B 200 --seed 1001`
196:| shared policy, independent noise | 0.52 / 0.34 | 0.30 / 0.22 | 0.30 / 0.22 | 0.10 [.04,.21] / **0.04** [.01,.13] | 0.90 / 0.92 |
199:| shared seed + common shock | 1.00 / 0.72 | 1.00 / 0.86 | 0.90 / 0.80 | 0.94 [.84,.98] / 0.88 [.76,.94] | 0.02 / 0.02 |
321:| pCMI (state+lags) | 0.52 [0.39, 0.64] | 0.52 [0.39, 0.64] | 0.45 [0.31, 0.60] | 18/70 (p=0.036, 2 tied) | 18/70 (p=0.036, 2 tied) |
326:| markup over Nash (non-IT) | 0.94 [0.90, 0.98] | 0.94 [0.90, 0.98] | 0.40 [0.24, 0.56] | 63/70 (p=3.2e-41, 1 tied) | 63/70 (p=3.2e-41, 1 tied) |
328:Paired-bootstrap AUROC differences (private vs none): pcmi-pair_level -0.46 [-0.58, -0.33]; pcmi-market_level -0.43 [-0.55, -0.29]; mi-pair_level -0.39 [-0.50, -0.28]; te-pair_level -0.53 [-0.66, -0.40]; pair_level-market_level +0.03 [-0.00, +0.08]
334:the conditions almost perfectly (pair_level AUROC 0.98 [0.95, 1.00]) and names the right pair in 63/70 runs. pCMI, raw MI and TE have run-AUROC CIs that include 0.5 (pCMI 0.52 [0.39, 0.64]). Their differences to pair_level are −0.39 to −0.53, and every CI excludes 0.
372:| D pair channel + shocks | 16 | 10/15 [0.42, 0.85] (+1 n/a) | 5/16 [0.14, 0.56] | — |
379:rivals is modest: +0.48 [0.33, 0.64] (C), +0.42 [0.26, 0.59] (D), and the gap shrinks over the game (figure). In `llm_v3` the gap is pair-specific (pair_level ≈ markup
389:| MI (raw) | 0.50 [0.36, 0.64] | **0.20** [0.06, 0.37] | **0.82** [0.65, 0.94] | 5/16 / 3/16 |
390:| lagged CMI (TE) | 0.55 [0.42, 0.67] | 0.35 [0.18, 0.55] | 0.74 [0.57, 0.88] | 6/16 / 3/16 |
393:| max-pair markup over Nash (non-IT) | **0.87** [0.78, 0.94] | 0.94 [0.86, 1.00] | 0.87 [0.74, 0.97] | 15/16 / 12/16 |
395:*Standalone comparison* (paired bootstrap over runs): pCMI − markup −0.42 [−0.56, −0.27] (pooled), −0.47 [−0.65, −0.29]
397:negative in C vs A and include 0 in D vs B (−0.06 [−0.24, 0.14], −0.14 [−0.34, 0.06]).
434:| MI (= CMI\|state here: one state) | +0.040 [−0.005, +0.091] | 8/12 | 0.39 | 1/12, 3/12, 6/48 |
436:| \|Pearson\| | +0.038 [−0.023, +0.085] | 8/12 | 0.39 | 5/12, 6/12, 24/48 (raw \|r\| is not calibrated on trending prices) |
456:The pair-minus-rivals gap is only +0.42 [0.20, 0.65], and it shrinks over the game (which sellers follow whom is not tested).
460:| pCMI run AUROC C vs A | 0.39 | 0.39 | 0.38 | 0.36 | **0.45** [0.16, 0.75] |
461:| MI | 0.39 | 0.42 | 0.39 | 0.41 | 0.39 [0.09, 0.69] |
467:The declared rescue criterion (AUROC(pCMI, 50) ≥ 0.65 and ≥ AUROC(pCMI, 20) + 0.15) is not met: 0.45 vs 0.39. So no extra T=50 batch was
478:detector does not (0.45 and 0.52, standalone differences vs the best level statistic −0.42 and −0.46, CIs exclude 0). In
491:#### 4.3.8 Exploratory: how much coordinated variation could pCMI see in these games? (E30, post-hoc)
520:#### 4.3.9 Exploratory: replication and placebo in the sibling market (E32, post-hoc)
531:| MI (raw prices) | 11.0/15 | 7.0/15 | +0.27 [+0.00, +0.53]; p=0.22 | 0.65 [0.42, 0.85] | 0.48 [0.23, 0.73] | 0.63 [0.45, 0.82] |
533:| \|Pearson\| | 6.0/15 | 11.0/15 | −0.33 [−0.67, +0.00]; p=0.18 | 0.41 [0.19, 0.65] | 0.29 [0.08, 0.55] | 0.62 [0.42, 0.80] |
534:| MI first differences | 10.0/15 | 3.0/15 | +0.47 [+0.07, +0.80]; p=0.065 | 0.62 [0.38, 0.83] | 0.72 [0.49, 0.91] | 0.39 [0.23, 0.54] |
535:| \|Pearson\| first differences | 8.0/15 | 6.0/15 | +0.13 [−0.33, +0.60]; p=0.77 | 0.39 [0.16, 0.63] | 0.41 [0.17, 0.66] | 0.46 [0.25, 0.69] |
537:| markup over Nash (non-IT) | 14.0/15 | 13.5/15 | +0.03 [−0.17, +0.23]; p=1 | 0.82 [0.62, 0.96] | 0.78 [0.58, 0.94] | 0.47 [0.29, 0.64] |
543:MI on first differences names the pair in 10.0/15 private runs and 3.0/15 placebo runs (matched +0.47, bootstrap CI [+0.07, +0.80]). The exact sign-flip test gives p=0.065 (Bonferroni over the 8 contrasts ≈ 0.52), so the positive bootstrap CI is not confirmatory. At run level the same statistic actually scores placebo runs higher than private ones (AUROC 0.39 [0.23, 0.54]).
548:#### 4.3.10 Exploratory: channel offered but no agreement (sibling strata, E35, post-hoc)
553:Top-1 and p-values are computed as in §4.3.9 (tie-averaged hits; pair-label randomisation null; chance = n/6). Declared rule for pair_level on the pooled 30 runs: "offer-driven" supported if p < 0.05/8, contradicted if hits ≤ 30/6 + 2 = 7. Table p-values are unadjusted Monte Carlo upper-tail estimates; CIs are pointwise 95% bootstrap intervals. The ×8 correction applies to the declared pooled localisation criterion, not the AUROC intervals; this remains post-hoc exploration.
557:| pCMI (state+lags) | 3.0/14 (p=0.42) | 1.5/16 (p=0.85) | 4.5/30 (p=0.6) | 0.56 [0.29, 0.82] |
563:| pair_level (non-IT) | 2.0/14 (p=0.71) | 1.3/16 (p=0.87) | 3.3/30 (p=0.82) | 0.42 [0.15, 0.69] |
566:Reading. The declared heuristic labels this result "contradicted": pair_level yields 3.3/30 tie-averaged hits (chance expectation 5.0; upper-tail p=0.82), versus 13.5/15 placebo and 14/15 private (§4.3.9). This shows no detected above-chance localisation in these strata, rather than statistically refuting an offer effect. Within `llm_v3mon` the level statistics show no statistically detected separation between offered and no-channel markets (pair_level 0.42 [0.15, 0.69], n = 14 vs 6). No dependence statistic localises the pair either (all pooled p ≥ 0.09, unadjusted).
570:#### 4.3.11 Exploratory: is the pair premium in our market there before a partner message is read? (E39, post-hoc)
575:| (a1) **first sender's** provisional price − rivals' round-0 price (no partner message read) | +0.94 [0.38, 1.59] | +2.19 [0.56, 3.94] |
578:| (c) pair − rivals, whole game (§4.3.4) | +0.45 [0.34, 0.57] | +0.42 [0.20, 0.65] |
581:Reading. The declared rule's verdict is "offer cue present in our market" in both datasets, both for the declared pair mean and for the first sender alone ("offer cue" is the declared rule label and means "present before a partner message is read", not an offer effect separate from the seller's own proposal). The first pair member's provisional price is above its rivals' round-0 prices before it has received any partner message. That price is written in the same response as its own first private message, and it is typically the price that message proposes (e.g. "I propose we both start at 15 and avoid undercutting", provisional 15, `llm_v1_D_003`); the second sender matches it exactly in 27/32 games. So the premium does not require *reading* a partner's message, but this check does not separate it from the seller's own coordination attempt. Rivals' round-0 prices match those of control sellers (`llm_v1` C family: rivals 11.7, A sellers 11.7, pair provisional 12.8). The opening point estimates exceed the whole-game premium (in `llm_v1` the CIs of (b) and (c) overlap; no paired test), consistent with the premium shrinking over the game. This agrees in direction with the sibling's round-1 and placebo findings (§4.3.9, §4.4). It also agrees with the §4.3.9 point that received messages add no detected level signal: the second sender, who has read the first message, is at +0.97 [0.41, 1.62], and pair provisional minus own round-0 price is +0.14 [−0.03, 0.38]. It is a descriptive, exploratory result: it does not identify a causal channel-offer effect, does not tell how much of the whole-game premium the offer explains, and does not replace a placebo arm (a seller can anticipate coordination before reading anything). Caveats: post-hoc; small n (the `llm_long` CI is wide). The provisional and round prices are different decision tasks: the provisional price is requested with different wording ("price is provisional") and under the common cost without a private shock, while rivals' round-0 prices use the same public state plus their own private cost shock and no chat. The effect comes from a right tail of high openings. Per seller, provisional prices ≥ 14 occur in 8/32 C-pair and 18/32 D-pair prices in `llm_v1`, against 0/84 round-0 prices of A sellers and 34/84 of B sellers (cost-shocked, so D openings are less distinctive).
586:* (2) Signals that look for *how* agents coordinate add little on these short games: conditioned dependence (pCMI) does not resolve above-chance discrimination here (0.45 [0.32, 0.59], 0.52 [0.39, 0.64]), and the zero-shot text-only auditor is at chance there (0.47). The sibling's supervised text classifier (0.98, in-distribution) shows the text carries condition information, though not which cues it uses.
591:* How detectable LLM collusion is depends on the market and its framing. The pair-minus-rivals premium is +1.65 [1.38, 1.93] in the sibling's lab-framed market (private runs, 10th–90th percentile +0.66…+3.18; none +0.04, legit +0.05; `experiments/premium_llm_v3.py`). Here it is +0.45 [0.34, 0.57], and most of the effect is market-wide.
607:| sibling `llm_v3`, T=12 | pair_level (surrogate) | 45/70 | 1/20 (legit partnership) | 0.11 [0.03, 0.54] | 0.40 [0.13, 0.86] | 0.76 [0.42, 0.97] |
619:Per-run scores agree to < 1e-9 in 422 of 424 run × statistic cells (`llm_v1` T=20, all four conditions; `llm_long` T=50 and its 20-round prefix; pCMI, Miller–Madow MI,
635:| same-market bystander pairs | 0.57 [0.44, 0.71] | 0.55 [0.41, 0.69] | 0.56 [0.46, 0.66] | 0.94 [0.91, 0.97] | 0.61 [0.58, 0.69] |
673:| base (4, 3.0, 10) | A | 2/30, 2/30 | 30 / 30 / 30 | 30 / 28 / 25 | 19 / 9 / 4 | 0.85 [0.75, 0.94] / 0.85 |
674:| base (4, 3.0, 11) | B | 3/30, 1/30 | 30 / 30 / 30 | 30 / 26 / 21 | 16 / 19 / 13 | 0.81 [0.69, 0.91] / 0.94 |
681:| inelastic (4, 4.5, 12) | A | 1/30, 1/30 | 30 / 30 / 30 | 28 / 12 / 15 | 13 / 7 / 3 | 0.85 [0.75, 0.94] / 0.78 |
717:| order | 6/6 | −0.19 | 0.67 [−0.35, 1.59] | 0.78 [0.44, 1.00] | 0.86 [0.58, 1.00] | 0.39 [0.08, 0.75] |
718:| noreason | 6/6 | +1.97 | 0.78 [−0.24, 2.02] | 0.47 [0.11, 0.83] | 0.42 [0.07, 0.83] | 0.47 [0.12, 0.79] |
725:Reading. (a) **The channel effect is robust; its size in v1 is at the high end.** v0 replicates `llm_v1` (C − A 1.19 vs 1.76 in v1; markup AUROC C vs A 0.92 vs 0.94; the v1 headline 0.87 pools C+D vs A+B). Pooled over wordings the effect is about +0.7 price units.
727:Computed within wordings and pooled, the markup AUROC (C vs A) is 0.66 [0.53, 0.78], against 0.92 for v0 alone and 0.94 in v1.
735:**Verdict (pre-registered rule): level, not short.** pCMI run AUROC C vs A at T=60 is **0.34 [0.18, 0.52]**; the upper CI is below 0.65, so moderate effects are excluded. The rule's "too short" branch needed ≥ 0.65 with lower CI > 0.5 and a gain ≥ 0.15 over T=20.
736:(a) Prefix power (same games, T = 10…60): pCMI 0.48, 0.52 [0.34, 0.69], 0.47, 0.40, 0.34, 0.34. The point estimate falls with more rounds; the T=20 → 60 change, −0.18 [−0.40, +0.05] (paired game bootstrap, `scripts/e44_decline.py` → `results/eval/e44_decline.json`), is not significant. Max-pair markup stays at 0.92–0.94, market level at 0.92–0.94 (0.94 [0.86, 1.00] at T=60), pair_level 0.64–0.77. TE at T=60 is 0.50 [0.32, 0.68].
745:(f) *Is the null just the linear estimator? (E73, robustness declared before computing, zero calls; `uv run python scripts/e73_nonlinear.py` → `results/eval/e73_nonlinear.json`.)* Two estimators, one configuration each: copula pCMI (each seller's prices → normal scores, then the identical pCMI) and sign MI (Miller–Madow CMI of sign(Δp_i), sign(Δp_j) ∈ {−, 0, +} given the public state); max pair, run AUROC; linear point estimates and the E44/executed/planting CIs reproduce exactly (E70 CI to two decimals: a game-cluster bootstrap with a different draw order). Linear / copula / sign: E70 (192 games, pooled within cell) 0.51 [0.43, 0.59] / 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52]; E44 T=60 0.34 [0.18, 0.52] / 0.40 [0.23, 0.58] / 0.54 [0.35, 0.72]; executed-only (48 vs controls, ten sets) 0.42 [0.33, 0.53] / 0.40 [0.30, 0.50] / 0.41 [0.31, 0.50]. Planted shared ±1 move at q = 0.1 on the E44 controls (same plantings): T=20 0.62 / 0.65 / 0.58, T=60 0.79 / 0.84 / 0.81. *Reading (pre-committed branch):* a rank-based and a discrete sign-based CMI are also at chance, with planted-move sensitivity 0.65 / 0.58 at T=20 and 0.84 / 0.81 at T=60, so neither estimator detects co-movement that the linear pCMI missed. This is a failure to detect, not proof of absence: it bounds only these two configurations and this planting, at T=20 small co-movement is not excluded, and in many E70 games the public state splits the 19 transitions into several sparse strata where sign MI has little power. The planting (on E44 controls, which have a single state) does not test that sparse regime (codex review R62).
753:| gpt-6-luna (`llm_v1`) | 16/21 | +0.02 | +1.78 | 1.76 [1.22, 2.31] | 0.94 [0.86, 1.00] | 0.75 [0.55, 0.91] | 0.47 [0.28, 0.67] | 0.67 |
775:| pCMI | **6.0 (p = 0.03)** / 3.3 / 3.2 / 3.0 / 2.3 | 0.49 / 0.38 / 0.22 [0.06, 0.42] / 0.28 |
783:(b) **Our pCMI prediction partly fails.** pCMI localises the pair above chance only where messages are delivered *privately* (6/15, p = 0.03; ≤ 3.3/15 elsewhere, including neutral delivery with 14/14 agreements), but that p is uncorrected and does not survive Bonferroni over the 25 arm × detector cells. Its market-level AUROC vs none is *below* chance in both undelivered pair-prompt arms (notes 0.22 [0.06, 0.42], placebo 0.28 [0.11, 0.49]), i.e. those markets show less conditioned dependence than none markets. We had predicted top-1 at chance and AUROC CIs including 0.5 in every arm.
786:**P2.11 Part C: executed collusion, a refusal-removed seller, older models (E61–E67; declared before generation or computation; glm-5.2 dropped).**
787:`uv run python scripts/p2_partc.py [--run-eval] [--label]` → `results/eval/p2_partc.{json,md}` (asserts unique run_ids and contiguous rounds per dataset). Our implemented definitions (`p2_partc.py`; E70 uses the same rule in `e70_grid.py::executed`): **executed** = judge-labelled agreement AND both pair firms ≥ agreed − 1 in ≥ half the post-agreement rounds AND second-half pair mean ≥ Nash + 2 (no floor cutoff, no upper bound, one-sided); **tacit** (no channel) = market mean ≥ Nash + 2 over the second half. Q2.2's strict rule additionally requires an arm-specific floor and ≥ 10 post-agreement rounds (their P2.7 table, E129); counts are not pooled across projects. Jeffreys 95% CIs.
789:| seller (dataset, T) | n C/A | A markup | C − A markup | AUROC markup (market_level) | AUROC pCMI | agreement | executed (C) | tacit (A) |
791:| gpt-6-luna (`llm_v1`, 20) | 16/21 | +0.02 | +1.76 [1.22, 2.31] | 0.94 | 0.47 | 14/16 | 6/16 [0.17, 0.62] | 0/21 [0, 0.11] |
793:| gpt-6-luna (E44 `llm_long_p2_T60`, 60) | 20/20 | −0.27 | +1.88 [1.34, 2.44] | 0.94 | 0.34 | 18/20 | 4/20 [0.07, 0.41] | 0/20 [0, 0.12] |
798:| E65 Qwen3.8-27B abliterated + memory (`llm_strong_qa`, 40) | 20/20 | −2.01 | +2.13 [1.28, 3.00] | 0.85 | 0.49 | 19/20 | 5/20 [0.10, 0.46] | 0/20 [0, 0.12] |
799:| E69 Qwen3.6-35B **abliterated** (`llm_qa36_p2`, 20) | 15/15 | −0.42 | +2.12 [1.39, 2.85] | 0.96 | 0.41 | 13/15 | 7/15 [0.24, 0.71] | 0/15 [0, 0.15] |
803:(b) **E61, refusal removal:** abliterated − base difference in (C − A) markup = **−0.37 [−2.09, +1.36]** (−0.40 [−2.03, +1.35] without `llm_qb_p2_A_000`, a run that was duplicated by two writers and then deduplicated). Both versions agree in 15/15 C games and execute 8/15 vs 6/15. Removing refusals has no detectable effect on channel collusion here; the CI rules out increases above +1.36 and decreases below −2.09 markup units (15 + 15 games per model). It does raise *no-channel* prices: abliterated − base A markup +1.06 [0.38, 1.74] (exploratory, a contrast not in the E61 declaration; **not replicated in E69**, below). Qwen undercuts without a channel (A markup −1.5 / −2.5, below Nash). Cached replies are well-formed JSON whose reasoning deliberately undercuts for volume (1/2821 unparsable), so this is the model's behaviour, not a parsing artefact.
804:(b2) **E69, second Qwen pair (declared 14:24 before generation; Qwen3.6-35B-A3B MoE, same seeds and design as E61; computed once 17:20):** abliterated − base difference in (C − A) markup = **−0.65 [−1.97, +0.65]**: the CI includes 0, so the declared prediction (null replicates) holds. Secondary: A-arm abliterated − base +0.35 [−0.28, +0.96], so E61's exploratory no-channel increase does not replicate; executed 7/15 vs 3/15. 0 fallback games. The base set is the only one of our ten where pCMI's CI excludes 0.5 (0.71 [0.51, 0.88]; its non-executed games carry it, 0.73, executed 0.64 [0.27, 1.00], n = 3); market level is still higher (0.93).
807:| pair (market, serving abl. / base) | agreement | executed | (C − A) markup diff | A-arm markup diff |
815:(c) **E64, detectors on executed vs non-executed collusion** (each vs all A games of its set, pooled within set, game bootstrap): market level 0.99 [0.96, 1.00] vs 0.90 [0.85, 0.94]; pair_level 0.87 [0.80, 0.94] vs 0.86 [0.81, 0.91]; **pCMI 0.42 [0.33, 0.53] vs 0.52 [0.45, 0.60]** (48 executed / 101 not, ten sets incl. E65 and E69; eight sets before E69: 0.42 [0.31, 0.52], 38 executed; gpt-6-luna sets alone: pCMI 0.40 [0.26, 0.54]). The declared prediction (evaluated on the eight sets) is only partly met: market_level 0.98 ≥ 0.9 and pCMI 0.42 < 0.70, but pair_level is 0.84 [0.75, 0.92] (ten sets: 0.87 [0.80, 0.94]), below the declared 0.9. The market_level row is also **circular**: "executed" requires pair ≥ Nash + 2, which pushes the absolute level up by construction (pair_level, a relative statistic, is not forced). Caveat on pCMI: the executed rule selects games whose prices are held flat, which by itself limits co-movement; E67 finds no correlation between stickiness and pCMI (ρ +0.00 [−0.34, +0.37] in E65), so this selection does not appear to drive the result. The informative comparison is executed vs non-executed on pCMI: restricting to executed agreements does not raise pCMI (0.42 vs 0.52). The single exception is deepseek's 2 executed games (pCMI 0.97, n = 2). **Definition sensitivity (E71, exploratory; `uv run python scripts/executed_sensitivity.py`):** across 27 combinations of tolerated undercut {0,1,2}, followed fraction {1/3,1/2,2/3} and second-half pair margin over Nash {+1,+2,+3}, executed counts range **13–78/149** and pooled within-set pCMI AUROC **0.343–0.531** (no CI wholly above 0.5); baseline IDs, count and AUROC/CI reproduce exactly. This is a sensitivity range, not a CI; the original one-sided agreement-floor rule is retained, and contributing sets/weights change with the definition.
816:(d) **E63 memory-lever pilots** (full price history + whole chat every round, T=40, 5 + 5, judge labels only, no detector run): qwen abliterated executes 5/5 [0.62, 1] (C − A +6.54 [4.76, 7.71]); qwen base executes 3/5 [0.21, 0.91] (+4.03 [2.09, 6.05]). Memory makes execution the norm, so the abliterated arm was promoted to **E65** (20 + 20, T=40, new seed 65, declared rule on pCMI, executed C vs A; result in (f)). The gpt-6-luna memory pilot (`llm_strong_luna_pilot`, same design) executes 3/5 [0.21, 0.91] with C − A +1.54 [0.38, 2.57]; it is descriptive only and not promoted, because E65 is the promoted arm. glm-5.2 is **dropped**: 0 complete games after ~2.5 h, because the shared Go backend stopped answering (170 cached calls, last 13:23). Agents are never told to collude.
817:(e) **E67, price stickiness (declared before computation; `uv run python scripts/e67_sticky.py` → `results/eval/e67_sticky.{json,md}`).** Hypothesis: colluding pairs hold prices, which would give a dependence-free variance screen (Abrantes-Metz et al. 2006) and explain below-chance pCMI. Score = max over the 6 firm pairs of the share of second-half rounds in which both firms keep their price. **Confirmatory gpt-5.6-luna: fails**, AUROC C vs A 0.46 [0.30, 0.61], because every market is sticky (0.97 / 0.97). Exploratory sets (the director had already looked at three of them) split by the no-channel behaviour. Where sellers keep undercutting without a channel, the screen works: qwen abliterated 0.99, base 0.96, deepseek 0.84. It fails for gpt-6-luna: `llm_v1` 0.51; at E44 T=60 it is 0.35 [0.18, 0.52], because channel markets change prices *more* often than no-channel ones (0.81 vs 0.88). **The mechanism is not supported:** ρ(stickiness, pCMI run score) is ≥ 0 or its CI includes 0 in 10/11 sets (E44 +0.07 [−0.24, +0.37]); only the template wording gives −0.70. So below-chance pCMI is not explained by held prices. Stickiness is one more level-type statistic that works only when the no-channel reference moves. **Second confirmatory set, E65: works**, AUROC 0.90 [0.79, 0.97] (no-change 0.83 vs 0.46; qwen undercuts without a channel), and again ρ(stickiness, pCMI) = +0.00 [−0.34, +0.37] (mechanism not supported). Third confirmatory set, E66 (`ext_llm_p2strongF`): **fails**, 0.42 [0.26, 0.59] (ρ −0.21 [−0.50, +0.12]). Tally: **1 of 3 confirmatory sets**, the one where the no-channel reference moves.
818:(f) **E65, strongest executed-collusion arm (pre-registered 13:38: qwen abliterated, full memory, T=40, 20 + 20, seed 65; `uv run python scripts/p2_partc.py`).** Declared rule: "moves appear" iff pCMI AUROC(executed C vs A) ≥ 0.65 with lower CI > 0.5; "still a level" iff upper CI < 0.65; else inconclusive. **Verdict: inconclusive**: pCMI AUROC 0.33 [0.02, 0.66], n = 5 executed vs 20 A. The point estimate is below chance (as in E44 executed, 0.17, and qwen executed, 0.31/0.36), but the CI's upper end touches 0.66, so the rule cannot call it a level. The pilot did not replicate: execution fell from 5/5 (pilot, seed 61) to **5/20 [0.10, 0.46]** (agreement 19/20), and C − A markup from +6.54 to **+2.13 [1.28, 3.00]**. All C vs A (descriptive, frozen detectors, T=40): market_level 0.85 [0.71, 0.97], pair_level 0.80 [0.66, 0.93], pCMI 0.49 [0.30, 0.67], MI 0.52, Pearson 0.53; transfer entropy 0.71 [0.53, 0.87] is the only dependence statistic whose CI excludes 0.5 (exploratory, one of eight statistics, not declared, not corrected for multiplicity). Spillover (`scripts/spillover.py --name llm_strong_qa --block 10`) is market-wide again: non-pair sellers sit +1.54 [0.83, 2.25] above no-channel markets in rounds 31–40 vs the pair's +2.98. So memory and T=40 do not turn LLM channel collusion into a detectable coordinated move. It stays a level that spreads to the whole market.
819:(g) **E66, frozen detectors on Q2.2's strong-framing arm** (pre-registered 13:3x before any of its data was read; sibling `llm_p2strongF`, gpt-6-luna, full memory, T=40, 20 private-channel + 20 no-channel, snapshot `data/ext_llm_p2strongF` with SHA256SUMS; `uv run python scripts/strongF_ext.py` → `results/eval/strongF_ext.{json,md}`). Our copied class code matches the sibling's class file **run by run (40/40, 0 mismatches)**. Executed 13/20 [0.43, 0.83], but **tacit-high 19/20 [0.79, 0.99] without any channel** (market − Nash, second half: executed +5.63, no-channel +5.50). The declared primary contrast (executed vs competitive no-channel) has n = 1 competitive game, so the verdict is **not evaluable** (n < 3, descriptive only, as declared). Secondary contrasts: executed vs tacit-high no-channel pCMI 0.44 [0.23, 0.64], market level 0.51 [0.30, 0.73]; private vs none pCMI 0.46 [0.27, 0.64], market level 0.44 [0.26, 0.63], TE 0.61 [0.42, 0.79]. Executed markets sit no higher than matched no-channel markets (pair +0.65 [−0.74, +2.40]). When strong framing makes tacit collusion the norm, the channel adds no measurable price effect, and neither level nor dependence statistics separate the arms. This matches gpt-5.6-luna in (a): an action-only screen needs a competitive reference, and here none exists.
823:**Result (15 + 15, full declared set): declared verdict inconclusive.** The manipulation gate passes, barely: all-round mean ask − 80, comms − nocomms **+0.39 [+0.06, +0.69]** (seed-cluster bootstrap, 15 matched seeds), i.e. about 2% of the 20-unit surplus; both arms ask close to cost (+2.13 vs +1.74). Neither declared branch holds: level AUROC 0.68 [0.46, 0.88] (lower CI not > 0.5), pCMI 0.60 [0.40, 0.80] (upper CI not < 0.65). Asks are not paid prices (Serendipity S14 caution): second-half transaction prices sit +2.61 vs +2.01 above cost, AUROC 0.68 [0.46, 0.88] (every game traded). pCMI shift-null flags at α = 0.05: comms 10/15, nocomms 5/15; 5/15 controls is well above the nominal rate, so the null is not calibrated in this market (descriptive). Parse failures: 18 in 14/30 runs. Reading: with qwen-3.6-35b, the starter CDA's chat elicits only a tiny ask premium, too small for either detector family to separate at 15 + 15; detector discrimination is imprecisely estimated (level CI up to 0.88), so this is an inconclusive external check, not evidence for or against the level > dependence ordering.
827:| mean ask − 80, all rounds (manipulation check) | +2.13 / +1.74 | diff +0.39 [+0.06, +0.69] |
831:| te | 0.45 / 0.39 | 0.61 [0.40, 0.81] (n 15 + 15) |
834:**P2.13 Claims × denominators (DIRECTION directive 3; no new calls; `uv run python scripts/claims_denominators.py` → `results/eval/claims_denominators.{json,md}`).** One row per abstract claim: in how many LLM sets does it hold? *main* = the nine complete C-vs-A sets of P2.11 with ≥ 10 games per arm (`llm_long`, 8 + 8, excluded); *wording* = the five E43 wordings (6 + 6 each, gpt-6-luna). E66 is not a C-vs-A set (channel labels are not ground truth there). E70 adds (+ 13/16 cells with positive C − A point estimate; level > pCMI 12/16, P2.14); these are point-estimate counts, so they are not appended to the CI-based rows below.
846:| agreements executed in <= 50% of channel games | main | 8/9 | 7 | llm_qa_p2 |
853:| llm_v1 | gpt-6-luna | 21, 16 | 0.94 | 0.47 | 0.35 | +0.47 [+0.29, +0.65] | +0.59 [+0.35, +0.80] |
854:| llm_ds_p2 | deepseek-v4.1-flash | 15, 15 | 0.99 | 0.57 | 0.81 | +0.42 [+0.22, +0.64] | +0.18 [+0.03, +0.37] |
855:| llm_long_p2_T60 | gpt-6-luna | 20, 20 | 0.94 | 0.34 | 0.50 | +0.60 [+0.41, +0.79] | +0.45 [+0.26, +0.63] |
864:**P2.14 Factorial grid (E70, Part E1; registered 17:10 in `results/e1_registration.md` before any data; analysed once by `scripts/e70_post.sh` → `results/eval/e70_grid.{json,md}`, figure `uv run python scripts/e70_fig.py`).** 2^(7−3) resolution IV, 16 cells × 6 complete sweeps × (no-channel A + channel C) = 192 games, T = 20, four sellers, public board on; factors: model M (gpt-6-luna / qwen-3.6-35b), cost (private / public; substitutes for 2 vs 4 firms), rivals' prices (visible / hidden), channel timing (every round / opening only), memory (short / full), shocks (none / random), framing (base / + long-run sentence). 0 fallback/model-mismatch games.
865:**Design limits.** Main effects are clear of two-factor interactions, but two-factor interactions are aliased in groups of three (21 interactions on 7 columns): none is interpreted. 6 + 6 games per cell. The seven main effects below have no multiplicity control and are descriptive. M means "model including its board use": qwen posts on the public board in ≈100% of agent-rounds in both arms of every cell, and gpt-6-luna in 4% / 10% (no-channel / channel; per cell: no-channel 0–1% except c07 32%, channel 0% in c00/c01/c06 and 15–16% in the other five; table in `results/eval/e70_grid.md`).
867:**Detectors, pooled within cell** [game bootstrap]: market level 0.74 [0.66, 0.81], pair level 0.72 [0.65, 0.80], **pCMI 0.51 [0.43, 0.59]**, TE 0.62 [0.54, 0.70]. Declared secondary TE hypothesis (lower CI > 0.5): **confirmed**. TE is above chance (lower CI 0.54) while pCMI is not (their difference is not tested); TE still ranks below the level (paired Δ level − TE +0.12 [+0.01, +0.22]; level − pCMI +0.23 [+0.12, +0.33]; E74, P2.13). TE maximises over directions of a squared residual correlation, so this is channel-associated lagged dependence, not shown to be positive price following. **E72 TE diagnostic (exploratory, post hoc, zero LLM calls, frozen estimator; `uv run python scripts/e72_te_diag.py` → `results/eval/e72_te_diag.json`; wording branches pre-committed in STATUS before computing).** (a) TE's top pair is the assigned channel pair in 30/96 channel games (0.31 [0.23, 0.41], chance 1/6; the highest-priced pair names it 57/96), so unlike scripted level collusion (§3.3) TE weakly names the pair. (b) Timing is unresolved: re-run on rounds 1–10 or 11–20 alone, TE is at chance (0.46 [0.39, 0.54]; 0.49 [0.42, 0.58]; late − early +0.03 [−0.07, +0.14]), but 9 target rows per window leave ≈ 2–5 residual df, so the windows cannot localise it; with full-series residuals split at round 10, early 0.57 [0.49, 0.65] and late 0.54 [0.46, 0.61] are indistinguishable. Neither the "early only" nor the "sustained" branch fires. (c) TE's separation is concentrated in channel games that did not meet the execution rule (0.73 [0.64, 0.80] vs controls, n = 52: 38 with a judge-labelled agreement, 14 without) but not in executed ones (0.49 [0.38, 0.60], n = 44); post hoc split, difference not tested. Executed games are not flatter than controls (mean seller price SD 0.79 vs 0.83), while non-executed games are more volatile (1.14), so this TE signal may reflect unstable post-agreement dynamics rather than coordination; this is consistent with Q2.2 E133 (zero-call part, n = 78 of these agreed games, Q2.2's late-window execution rule, 48 held / 30 not; `e133_privileged.json`): agreements that are not held are volatile from the start (early pair price SD, rounds 0–5, 0.67 held vs 1.83 not held; AUROC for holding 0.15 [0.06, 0.24]), which gives lagged dependence something to detect. **Amendment 2a, qwen-cell pCMI replication of base Qwen3.6 (replicated iff lower CI > .5): 0.46 [0.35, 0.58], not replicated.** The P2.11 exception (0.71 [0.51, 0.88]) therefore does not generalise to E70's conditions (board on, factors varied, 6 + 6 per cell); the intervals overlap, so whether it is model-specific remains unresolved. Level − pCMI: luna +0.16 [+0.01, +0.29], qwen +0.29 [+0.15, +0.44]. Rival spillover +0.60 [+0.30, +0.91]; executed 44/96 channel games (P2.11 rule: judge agreement + behavioural follow-through, *Terms*).
868:**Declared follow-up (amendment 2c, decided automatically 22:36).** Model M and cost are the only factors whose main-effect CIs exclude 0 (uncorrected, descriptive); the largest |main effect| is M (+0.79 [0.10, 1.44]; cost +0.79 [0.12, 1.41], a near tie). Its CI excludes 0 but |effect| < 1, so the rule ran the follow-up: factor M, predicted sign +, 12 + 12 fresh-seed games (no-channel + channel) per model level, other factors at their low levels (`results/eval/e70_followup_declared.json`, saved before generation). **Result (FOLLOWUP_EXIT=0, 23:32; run once by `e70_post.sh`, 0 fallback games): not confirmed.** C − A is +0.88 with gpt-6-luna and +1.96 with qwen-3.6-35b; the model effect is +1.07 [−0.20, +2.41] (game-cluster bootstrap), and its CI includes 0, so the declared rule (CI excludes 0 in the predicted direction) fails. The point estimate has the predicted sign and a similar size to E70's +0.79, so this is underpowered rather than evidence of no model effect. Pre-commit (d) therefore applies: no factor's main effect is resolved, and E70's M and cost effects stay descriptive. Both levels still show a positive point-estimate channel premium (`results/eval/e70_followup.json`).
870:| factor | low → high | main effect on C − A markup [95% CI] |
877:| shocks | none → random | −0.34 [−0.96, 0.28] |
880:![E70 factorial grid](figures/e70_grid.png)
899:* No evasion test: the sibling's monitor-aware luna sellers stop agreeing (0/10, 0/10 vs 10/10 matched; Q2.2 P2.9) instead of hiding, so there is no evasive-collusion arm for dependence detectors. SALT-NLP (Q2.2 D1) has one ACCEPT/REJECT per agent and no action series, so pCMI/TE do not apply there (D1 dropped here); its P(said | executed) 0.385 [0.353, 0.416] (Q2.2 P2.12) is an external case of executed collusion mostly left unsaid, i.e. why action-only screens matter.
903:* Below-chance pCMI in several LLM sets (e.g. E44 0.34, template wording 0.17) is unexplained. E67 tested and rejected price stickiness (ρ ≈ 0 in 10/11 sets). A candidate is that competitive undercutting in no-channel markets leaves reaction co-movement that lagged conditioning does not remove, and coordinated levels lack it (untested).
913:`--phase2-recompute` first verifies saved per-run scores against the frozen implementation without permutation draws (`uv run python scripts/check_saved_scores.py > results/saved_scores_check.json`): 9,490/9,490 score cells across 16 finalized datasets reproduce exactly (`results/saved_scores_check.json`); this does not recheck permutation flags/CIs. It then adds a fixed list of finalized Phase 2 analyses: prevalence, reimplementation, same-model/matched-reference, prompt/model/board comparisons, external channel/strong-framing sets, Part C executed subsets, stickiness, long-game power/decay/spillover and denominators. Saved scores/labels are reused where normally read; same-model, external and long-power scripts also recompute statistics. This never analyses E68/E70, generates games, re-judges or reruns locked scripted experiments. Synthetic checks: `uv run python scripts/test_e70_pipeline.py --evidence` (20 tests; grid JSON byte-identical, existing follow-up fields exact; `results/e70_pipeline_check.json`) and `uv run python scripts/test_e68_pipeline.py --evidence` (D2 seed-bootstrap/gate/completion checks, actual generator with mocked LLM; frozen scores, AUROCs and permutation flags exact against pre-correction code; `results/e68_pipeline_check.json`). Saved-result manuscript fragments are rendered only after the registered analyses with `uv run python scripts/p2_landing.py e70 --part all` / `e68 --part all`; synthetic end-to-end checks (analysis → fragments → REPORT tables, including ties/interim/no-trade cases) run with `uv run python scripts/test_p2_landing.py --evidence` (`results/p2_landing_check.json`). E70 counts of positive point estimates must remain separate from P2.13's positive-CI claim.
919:`--core-eval` runs the frozen `llm_v1`, `llm_long`, `llm_mixed2` and external `llm_v3` evaluators and the existing trend/incremental diagnostics before the checks above. All seven additional JSON/Markdown outputs must match their saved bytes. The full historical audit **passed** at Sat 20:00 UTC: 41 commands, 62 byte-identical outputs, archived in `results/release_audit_iter23_full.json` (source `cea55dc`; no PDF export). The snapshot predates later pipeline/reporting changes and the refreshed deck/overview; this is not a full audit of newer source. No further release audit before Sun 16:30 UTC. These are reproducibility checks, not new estimator validation or detector tuning.
923:uv run python -m experiments.scripted both --name gate_test --n 50 --T 100 --strength 0.6 --B 200 --seed 1001  # §4.1 (locked)
952:uv run python scripts/p2_partc.py                       # P2.11 part C table + E64 executed-subset AUROCs (results/eval/p2_partc.{json,md})
983:* Banchio & Mantegazza (2023). Adaptive Algorithms and Collusion via Coupling. ACM EC '23. arXiv:2202.05946.

exec
/bin/bash -lc 'wc -l /home/factory/collusion/collusion-{14-infotheory,22-say-vs-do}/REPORT.md && cat /home/factory/collusion/collusion-14-infotheory/results/eval/claims_denominators.json' in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
   996 /home/factory/collusion/collusion-14-infotheory/REPORT.md
   736 /home/factory/collusion/collusion-22-say-vs-do/REPORT.md
  1732 total
{
 "sets": [
  {
   "set": "llm_v1",
   "group": "main",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    21,
    16
   ],
   "d": 1.756,
   "d_ci": [
    1.222,
    2.315
   ],
   "ml": 0.9434523809523809,
   "pl": 0.7485119047619048,
   "pcmi": 0.47470238095238104,
   "pcmi_ci": [
    0.28273809523809523,
    0.6666666666666666
   ],
   "executed": [
    6,
    16
   ],
   "tacit": [
    0,
    21
   ]
  },
  {
   "set": "llm_ds_p2",
   "group": "main",
   "models": [
    "deepseek-v4.1-flash"
   ],
   "n": [
    15,
    15
   ],
   "d": 3.749,
   "d_ci": [
    2.768,
    4.679
   ],
   "ml": 0.9911111111111112,
   "pl": 0.9955555555555556,
   "pcmi": 0.5733333333333334,
   "pcmi_ci": [
    0.35555555555555557,
    0.7733333333333333
   ],
   "executed": [
    2,
    15
   ],
   "tacit": [
    0,
    15
   ]
  },
  {
   "set": "llm_long_p2_T60",
   "group": "main",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    20,
    20
   ],
   "d": 1.879,
   "d_ci": [
    1.342,
    2.436
   ],
   "ml": 0.9425,
   "pl": 0.7737499999999999,
   "pcmi": 0.33749999999999997,
   "pcmi_ci": [
    0.17750000000000005,
    0.5175000000000001
   ],
   "executed": [
    4,
    20
   ],
   "tacit": [
    0,
    20
   ]
  },
  {
   "set": "llm_qa_p2",
   "group": "main",
   "models": [
    "qwen-abliterated"
   ],
   "n": [
    15,
    15
   ],
   "d": 2.967,
   "d_ci": [
    1.821,
    4.261
   ],
   "ml": 0.9511111111111111,
   "pl": 1.0,
   "pcmi": 0.52,
   "pcmi_ci": [
    0.2932222222222222,
    0.7422222222222223
   ],
   "executed": [
    8,
    15
   ],
   "tacit": [
    0,
    15
   ]
  },
  {
   "set": "llm_qb_p2",
   "group": "main",
   "models": [
    "qwen-base(aqueduct qwen-3.8-27b)"
   ],
   "n": [
    15,
    15
   ],
   "d": 3.337,
   "d_ci": [
    2.235,
    4.543
   ],
   "ml": 0.9622222222222222,
   "pl": 0.92,
   "pcmi": 0.4622222222222222,
   "pcmi_ci": [
    0.25333333333333335,
    0.6755555555555556
   ],
   "executed": [
    6,
    15
   ],
   "tacit": [
    0,
    15
   ]
  },
  {
   "set": "llm_g56l_p2",
   "group": "main",
   "models": [
    "gpt-5.6-luna"
   ],
   "n": [
    10,
    10
   ],
   "d": 1.438,
   "d_ci": [
    0.226,
    2.588
   ],
   "ml": 0.75,
   "pl": 0.795,
   "pcmi": 0.72,
   "pcmi_ci": [
    0.47000000000000003,
    0.92
   ],
   "executed": [
    4,
    10
   ],
   "tacit": [
    9,
    10
   ]
  },
  {
   "set": "llm_strong_qa",
   "group": "main",
   "models": [
    "qwen-abliterated"
   ],
   "n": [
    20,
    20
   ],
   "d": 2.135,
   "d_ci": [
    1.285,
    3.005
   ],
   "ml": 0.84875,
   "pl": 0.80375,
   "pcmi": 0.49,
   "pcmi_ci": [
    0.30000000000000004,
    0.6700624999999997
   ],
   "executed": [
    5,
    20
   ],
   "tacit": [
    0,
    20
   ]
  },
  {
   "set": "llm_qa36_p2",
   "group": "main",
   "models": [
    "qwen36-abliterated"
   ],
   "n": [
    15,
    15
   ],
   "d": 2.116,
   "d_ci": [
    1.39,
    2.848
   ],
   "ml": 0.9555555555555556,
   "pl": 0.9911111111111112,
   "pcmi": 0.40888888888888886,
   "pcmi_ci": [
    0.18222222222222223,
    0.6311111111111112
   ],
   "executed": [
    7,
    15
   ],
   "tacit": [
    0,
    15
   ]
  },
  {
   "set": "llm_qb36_p2",
   "group": "main",
   "models": [
    "qwen-3.6-35b"
   ],
   "n": [
    15,
    15
   ],
   "d": 2.762,
   "d_ci": [
    1.707,
    3.862
   ],
   "ml": 0.9288888888888889,
   "pl": 0.8777777777777778,
   "pcmi": 0.7111111111111111,
   "pcmi_ci": [
    0.5066666666666667,
    0.8844444444444444
   ],
   "executed": [
    3,
    15
   ],
   "tacit": [
    0,
    15
   ]
  },
  {
   "set": "wording:v0",
   "group": "wording",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    6,
    6
   ],
   "d": 1.1875000000000002,
   "d_ci": [
    0.4354166666666668,
    1.9354166666666663
   ],
   "ml": 0.9166666666666667,
   "pl": 0.8194444444444445,
   "pcmi": 0.5,
   "pcmi_ci": [
    0.16666666666666666,
    0.8333333333333335
   ],
   "executed": [
    null,
    null
   ],
   "tacit": [
    null,
    null
   ]
  },
  {
   "set": "wording:para",
   "group": "wording",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    6,
    6
   ],
   "d": 0.5270833333333335,
   "d_ci": [
    0.09578125000000004,
    0.9854166666666667
   ],
   "ml": 0.8055555555555556,
   "pl": 0.7500000000000001,
   "pcmi": 0.6666666666666667,
   "pcmi_ci": [
    0.3333333333333333,
    1.0
   ],
   "executed": [
    null,
    null
   ],
   "tacit": [
    null,
    null
   ]
  },
  {
   "set": "wording:template",
   "group": "wording",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    6,
    6
   ],
   "d": 0.4541666666666666,
   "d_ci": [
    -0.9979166666666663,
    2.622968749999999
   ],
   "ml": 0.3055555555555556,
   "pl": 0.3472222222222222,
   "pcmi": 0.16666666666666669,
   "pcmi_ci": [
    0.0,
    0.33333333333333337
   ],
   "executed": [
    null,
    null
   ],
   "tacit": [
    null,
    null
   ]
  },
  {
   "set": "wording:order",
   "group": "wording",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    6,
    6
   ],
   "d": 0.6729166666666665,
   "d_ci": [
    -0.3458854166666666,
    1.5895833333333331
   ],
   "ml": 0.7777777777777779,
   "pl": 0.8611111111111112,
   "pcmi": 0.38888888888888884,
   "pcmi_ci": [
    0.08333333333333333,
    0.75
   ],
   "executed": [
    null,
    null
   ],
   "tacit": [
    null,
    null
   ]
  },
  {
   "set": "wording:noreason",
   "group": "wording",
   "models": [
    "gpt-6-luna"
   ],
   "n": [
    6,
    6
   ],
   "d": 0.78125,
   "d_ci": [
    -0.23958333333333304,
    2.0208854166666663
   ],
   "ml": 0.4722222222222222,
   "pl": 0.4166666666666667,
   "pcmi": 0.4722222222222222,
   "pcmi_ci": [
    0.12499999999999997,
    0.7916666666666667
   ],
   "executed": [
    null,
    null
   ],
   "tacit": [
    null,
    null
   ]
  }
 ],
 "claims": [
  {
   "claim": "premium",
   "text": "channel raises markup (C - A CI > 0)",
   "group": "main",
   "k": 9,
   "K": 9,
   "models_where_holds": [
    "deepseek-v4.1-flash",
    "gpt-5.6-luna",
    "gpt-6-luna",
    "qwen-3.6-35b",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)",
    "qwen36-abliterated"
   ],
   "fails": []
  },
  {
   "claim": "premium",
   "text": "channel raises markup (C - A CI > 0)",
   "group": "wording",
   "k": 2,
   "K": 5,
   "models_where_holds": [
    "gpt-6-luna"
   ],
   "fails": [
    "wording:template",
    "wording:order",
    "wording:noreason"
   ]
  },
  {
   "claim": "pcmi_null",
   "text": "pCMI not above chance (AUROC CI includes 0.5 or lies below)",
   "group": "main",
   "k": 8,
   "K": 9,
   "models_where_holds": [
    "deepseek-v4.1-flash",
    "gpt-5.6-luna",
    "gpt-6-luna",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)",
    "qwen36-abliterated"
   ],
   "fails": [
    "llm_qb36_p2"
   ]
  },
  {
   "claim": "pcmi_null",
   "text": "pCMI not above chance (AUROC CI includes 0.5 or lies below)",
   "group": "wording",
   "k": 5,
   "K": 5,
   "models_where_holds": [
    "gpt-6-luna"
   ],
   "fails": []
  },
  {
   "claim": "level_beats_pcmi",
   "text": "market-level markup AUROC > pCMI AUROC",
   "group": "main",
   "k": 9,
   "K": 9,
   "models_where_holds": [
    "deepseek-v4.1-flash",
    "gpt-5.6-luna",
    "gpt-6-luna",
    "qwen-3.6-35b",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)",
    "qwen36-abliterated"
   ],
   "fails": []
  },
  {
   "claim": "level_beats_pcmi",
   "text": "market-level markup AUROC > pCMI AUROC",
   "group": "wording",
   "k": 4,
   "K": 5,
   "models_where_holds": [
    "gpt-6-luna"
   ],
   "fails": [
    "wording:noreason"
   ]
  },
  {
   "claim": "spill",
   "text": "pair_level AUROC <= market-level AUROC (spillover costs the relative screen)",
   "group": "main",
   "k": 5,
   "K": 9,
   "models_where_holds": [
    "gpt-6-luna",
    "qwen-3.6-35b",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)"
   ],
   "fails": [
    "llm_ds_p2",
    "llm_qa_p2",
    "llm_g56l_p2",
    "llm_qa36_p2"
   ]
  },
  {
   "claim": "spill",
   "text": "pair_level AUROC <= market-level AUROC (spillover costs the relative screen)",
   "group": "wording",
   "k": 3,
   "K": 5,
   "models_where_holds": [
    "gpt-6-luna"
   ],
   "fails": [
    "wording:template",
    "wording:order"
   ]
  },
  {
   "claim": "exec_minority",
   "text": "agreements executed in <= 50% of channel games",
   "group": "main",
   "k": 8,
   "K": 9,
   "models_where_holds": [
    "deepseek-v4.1-flash",
    "gpt-5.6-luna",
    "gpt-6-luna",
    "qwen-3.6-35b",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)",
    "qwen36-abliterated"
   ],
   "fails": [
    "llm_qa_p2"
   ]
  },
  {
   "claim": "no_tacit",
   "text": "no-channel markets rarely tacit-high (<= 10%)",
   "group": "main",
   "k": 8,
   "K": 9,
   "models_where_holds": [
    "deepseek-v4.1-flash",
    "gpt-6-luna",
    "qwen-3.6-35b",
    "qwen-abliterated",
    "qwen-base(aqueduct qwen-3.8-27b)",
    "qwen36-abliterated"
   ],
   "fails": [
    "llm_g56l_p2"
   ]
  }
 ],
 "note": "E66 (Q2.2 strong framing) is not a C-vs-A set here: channel labels are not ground truth there (tacit 19/20); see results/eval/strongF_ext.json"
}
exec
/bin/bash -lc "rg -n 'execut|pre.register|post.hoc|Joint|Detectability|13/20|19/20|31/31|0.855|0.885|0.77|0.94|0.24|115/115|six.arm|62%|0.385|14/50' /home/factory/collusion/collusion-22-say-vs-do/REPORT.md" in /home/factory/collusion/collusion-beyond-words
 succeeded in 0ms:
4:Phase 2 (from 2026-10-24 06:30 UTC) re-tests them. Results current 2026-10-25 04:45 UTC: P2.1–P2.17 final (P2.17 = E133/E133c/E133d/E133e, private say-vs-do forecast); E113 audited all 192 Q1.4 grid games and evaluated once. P2.7 distinguishes frozen execution rules; Q1.4 D2 is final and inconclusive (P2.12). E102 (strong-framing Qwen, 6 seeds) is descriptive. Exports: [README.md](README.md).*
8:- On Q1.4's Qwen grid adding text hurts: combined minus prices −0.24, and still −0.30 on games executed under Q1.4's rule.
10:- The price premium replicates (0.94 AUROC) but is partly a prompt effect: an unread notepad gives 65% of the channel's premium.
11:- High prices need no channel: with memory and profit framing, 19/20 no-channel markets price ≥ Nash + 2.
13:- All auditors read public messages and prices only; private chat is used for labels and in E133 (P2.17), where private say-do consistency forecasts late execution (say-do gap AUROC 0.77 oriented) but adds nothing beyond early price stability (0.855). An LLM forecasts beyond the best raw early-price rule (0.94 vs 0.885, Δ +0.06 [+0.02, +0.10], post hoc; E133e) with or without the private chat; we find no evidence that its edge comes from public messages (0.91 without vs 0.96 with posts; difference CI includes 0).
17:test, n = 95) and −0.07 [−0.17, +0.02] (fresh pooled post hoc, n = 90). In the base market, four gpt-6-luna sellers (one pair offered private chat) face zero-shot gpt-6.1-sol auditors reading text, prices, or both. In Q1.4's 8-cell Qwen-3.6 grid, where prices alone are at chance (pooled 0.52 [0.41, 0.64]), adding inverted text lowers AUROC (stratified Δ combined − action −0.24 [−0.37, −0.09]).
19:text auditors flag every control market (50/50). Qwen-grid text is inverted (pooled 0.32 [0.24, 0.42]; it flags every game in both arms). SALT-NLP text predicts execution (AUROC 0.87 [0.83,
21:Labels disagree: 14/50 test agreements are kept (E84 follow rule). With memory and profit framing, 13/20 channel pairs strictly execute, yet 19/20 no-channel markets price ≥ Nash + 2. A gpt-6.1-sol newcomer
22:re-agrees 0/20, yet 18/20 markets stay high. Abliterated Qwen shows no detectable execution difference from its base model (strict 5/15 both; 13/15 under the registered floor rule, diff 0 [−0.26, +0.26]; agreement at ceiling), with a
27:- *Answer:* adding public text to prices gives no resolved gain in our base market and two fresh replications, and lowers AUROC in the Qwen grid (P2.16), where text is inverted. The exception is SALT (0.87 [0.83, 0.91]), a negotiation where talk is the action. Scope: auditors read public messages and prices only. With private access (E133/E133e), say-do consistency forecasts execution (0.77) but adds nothing beyond early price stability (0.855); an LLM beats the best price rule (post hoc, +0.06 [+0.02, +0.10]), with no evidence its edge comes from messages.
28:- *Numbers:* combined − best single −0.01 [−0.09, +0.06] (locked test, 95 runs); −0.07 [−0.17, +0.02] (pooled fresh, 90 runs, post hoc); SALT text auditor 0.87 [0.83, 0.91] (240 episodes); public text run AUROC 0.15–0.36 in invite-in-control families (CI below 0.5 only for the two Qwen-3.8 arms); SALT 0.81 [0.75, 0.87] on executed episodes with no judged agreement; E133 hand say-do features Δ −0.05 [−0.09, −0.02] (n = 78, leave-cell-out CV); E133c LLM + private chat 0.93 vs a CV'd 2-feature price model 0.816 (+0.11 [+0.02, +0.21]); with − without chat −0.02 [−0.06, +0.01]; E133e no-chat LLM 0.942 vs raw rule score 0.885 (+0.057 [+0.019, +0.103]), vs raw pair SD 0.855 (+0.086 [+0.015, +0.169]); LLM in games with/without public posts 0.96 (n = 48) / 0.91 (n = 30).
29:- *E113 grid (16 Q1.4 cells, 192 games):* registered P1 held weakly (4/16 positive, 1 tie, 11 negative; max-selection bias). Qwen-3.6 cell-stratified Δ combined − action −0.24 [−0.37, −0.09], combined − text −0.05 [−0.13, +0.03] (estimand added in amend3, 20:35, after about half the games were audited but before any score was read); prices alone are at chance there (pooled 0.52 [0.41, 0.64]), so combined inherits the inverted text (pooled 0.32 [0.24, 0.42]; flags 48/48 in both arms); 0/8 Qwen cells positive. In the 5 luna cells with public posts (almost only in the channel arm) combined − action is +0.11 [−0.02, +0.24] (text view not audited there). On executed games only (Q1.4's E70 rule, registered secondary), Qwen text stays inverted (0.36 [0.26, 0.46]) and Δ combined − action is −0.30 [−0.44, −0.17]. This reuses Q1.4 E70 data, not an independent joint replication.
31:- *Do not quote:* E99-x plan 0.76 without E111 (no-LLM partner-name count 0.82); E116b Qwen strata (5 vs 10); the round-1 or pair premium as a detector (prompt-confounded, P2.5/P2.10); any executed count without its definition (strict / floor rule).
34:- (none yet; top, box and merge block frozen 07:30. Pre-freeze 06:50 edits: E133e wording "not via public messages" → "no evidence its edge comes from public messages"; "post hoc" added next to +0.06.)
38:1. *No resolved gain from public text in the base market and two fresh replications* (primary `combined` view: −0.01 test n = 95; −0.07 [−0.17, +0.02] pooled fresh n = 90). Bound: gains above +0.06 (test) and +0.02 (pooled) are excluded at 95% (pooling post hoc). Text alone ≈ chance (test 0.47; p2rep 0.45, n = 60). A computed pair-statistics table gains on test, +0.11 [+0.04, +0.18],
39:   but no resolved gain on fresh data, +0.00 [−0.06, +0.07] pooled n = 90; adding text to it shows no resolved gain, −0.06 [−0.14, +0.01] test. On the Q1.4 grid (P2.16), Qwen combined − action is −0.24 [−0.37, −0.09]; prices alone are at chance there (0.52) and text is inverted (pooled 0.32 [0.24, 0.42]).
40:2. *The premium replicates (0.94 [0.87, 0.99], 60 fresh runs: 30 private / 20 none / 10 legit) but is confounded* by the pricing notepad,
42:3. *Text can be inverted:* for families that invite rivals publicly in control markets too (Claude, deepseek, Qwen), text views rank controls *above* channel markets on point estimates (run AUROC 0.15–0.36; CI below 0.5 only for the two Qwen-3.8 arms, and for the Qwen-3.6 grid, P2.16, including executed games under Q1.4's E70 rule, 0.36 [0.26, 0.46]). Where a family talks decides what text can see: in our base market luna talks only in private (in Q1.4's grid it posts publicly in 5/8 cells, P2.16; under strong framing 43% of its no-channel public messages match a hold-price regex, P2.7, post hoc); Claude, deepseek and Qwen also in public (text views flag
43:   100% of their control markets). Mechanism (E132, post hoc): Qwen channel sellers still post every round but invite rivals publicly less often (invite-regex rate 0.40 vs 0.88 controls, Qwen3.8 base; 0.18 vs 0.29 Qwen-3.6 grid), and text scores track that rate (Spearman 0.41–0.74, CI > 0, three Qwen sets); for deepseek (regex saturated, 1.00 both arms) and Claude (n = 10) the mechanism is not established (appendix E132); gpt-6.1-sol proposed coordination in 0/7 private markets. SALT: P(said | executed) 0.385, yet a text auditor reaches 0.87 on 240 sampled episodes (120 executed; 0.81 without a judged agreement; P2.12), one external bilateral negotiation where chat is the main action channel.
44:4. *Labels disagree:* 14/50 test agreements are kept (E84 follow rule); on the kept label the premium falls to 0.80 [0.67, 0.90] (test) / 0.76 [0.64, 0.86]
46:5. *High prices need no channel:* with memory + profit framing 19/20 no-channel markets price ≥ Nash + 2 and 13/20 channel pairs are
47:   strict-executed; paired difference −0.44 [−1.84, +1.00] (P2.7). gpt-5.6-sol, mimo and Qwen price high even at base framing.
48:   In this one arm (n = 13 vs 19, exploratory), a monitor reading private plans separated executed from tacit (0.76 [0.55, 0.93]) where
50:   post hoc, not shown to be agreement) did not; a no-LLM partner-name count does comparably (0.82 [0.66, 0.96]) and no plan uses agreement words (a channel footprint). Within channel pairs
51:   (13 vs 7, E116, exploratory) no text or plan view resolves execution (plan 0.69 [0.44, 0.91], text 0.61 [0.37, 0.85]; low power); market excess separates partly by construction (0.78 [0.54, 0.96]) and action_stats inverts (0.18 [0.00, 0.42]).
55:7. *Practical:* premium precision 0.24 at 5% prevalence; legitimate cost/quality edges are flagged 7/10, 9/10 (controls 2/10). Screens
58:*Joint statement with Q1.4 (verbatim in both reports):* "Detectability of LLM collusion by any price statistic is a property of the (seller
59:model × prompt) pair. Relative screens survive a shared model but fail under market-wide spillover; absolute screens need model- and prompt-matched references." "With memory and a profit objective, gpt-6-luna sellers raise prices market-wide without any channel (19/20 no-channel markets ≥
60:Nash + 2); agreements are then often kept (13/20) but add no detectable price, so channel labels stop being ground truth. Abliterated Qwen
61:with memory differs (channel adds +2.13 [1.28, 3.00]; 5/20 executed), as the first sentence predicts." (Rescoped text, DIRECTION 15:50. The Qwen numbers in the quote are Q1.4's E65 arm, their market, T = 40;
62:this report's own Qwen comparison is P2.11. "Predicts" means "is consistent with". "Channel" = private channel; a public board exists in all arms. 13/20 = Q2.2 strict rule (P2.7); 5/20 = Q1.4's E65 rule, not comparable.)
64:## Phase 2 results (from 2026-10-24 06:30 UTC; v1 below frozen as git tag `v1-overnight`)
67:Phase 2 experiments and checks are E77–E133e (exceptions to pre-registration are marked where they occur, e.g. E104, E99-x); descriptive post-hoc analyses are marked (e.g. E93). New datasets are named `llm_p2*`. v1 numbers below are unchanged.
78:| luna, memory + profit framing, within channel pairs (E116, exploratory) | strict-executed vs not | 13 vs 7 markets | 0.61 [0.37, 0.85] | 0.33 [0.10, 0.59] | `p2_within_agree_llm_p2strongF.json : views.{text,action}.auroc_strict_vs_nonexec` |
79:| SALT-NLP negotiation, deal struck in chat (E105, external) | executed vs not | 240 episodes (120 executed) | 0.87 [0.83, 0.91] | – | `salt_d1.json : E105_audit.auroc (no separate action view: execution is the label)` |
85:| P2.1 | precision at realistic prevalence | premium precision at 5%: 0.24 [0.15, 0.43] test, 0.16 [0.09, 0.44] replication | `p2_prevalence.json` |
88:| P2.4 | labels by behaviour | 14/50 agreements kept; premium 0.80 [0.67, 0.90] on kept label; hybrid −0.03 [−0.14, +0.06] (test), −0.03 [−0.13, +0.06] (pooled fresh) | `p2_behaviour.json`, `p2_pool_rep.json` |
89:| P2.5 | prompt artifact? | notepad +1.04 [+0.65, +1.42] vs channel +1.61; weather notepad +0.22; terse wording +0.24 [−0.32, +0.81] vs +1.75 original wording (same 10 seeds) | `p2_logbook.json`, `p2_band.json` |
91:| P2.7 | executed (strong) collusion; older sellers | strict-executed 13/20 [0.43, 0.83] (10–16/20 varying one threshold at a time, 7–18/20 over all 81 combinations, E120) vs tacit-high 19/20 no-channel (17–20/20); executed vs tacit (exploratory): price-view CIs include 0.5, public text 0.25 (reverse), private-plan view 0.76 [0.55, 0.93] but no-LLM partner-name count 0.82 [0.66, 0.96] (E111; plans contain no agreement words); within channel pairs (E116, 13 vs 7) plan 0.69 [0.44, 0.91], action_stats 0.18 (inverted); older sellers: strict-executed gpt-5.6-sol 1/7, mimo 3/4 (floor rule 1/7, 4/4) | `p2_strongF_report_llm_p2strongF.json`, `p2_plan_keyword_llm_p2strongF.json`, `p2_within_agree_llm_p2strongF.json`, `p2_c2older.json`, `p2_strict_sensitivity.json` |
92:| P2.8 | second fresh replication (n = 60, registered) | premium 0.94 [0.87, 0.99] (confounded, P2.5/P2.10); hybrid −0.04 [−0.16, +0.08]; pooled n = 90 (post hoc) −0.07 [−0.17, +0.02] | `replication_llm_p2rep.json`, `p2_pool_rep.json` |
95:| P2.11 | abliterated vs base Qwen (C3) | agreement 15/15 both (ceiling); strict-executed 5/15 both; floor-rule executed 13/15 both (diff 0 [−0.26, +0.26]); premium diff −1.24 [−2.41, −0.03] (bf16 vs FP8 serving); no detectable increase in the respective metrics across 3 Qwen pairs incl. Q1.4 E61/E69; Qwen3.5-9B pair dropped at its registered pilot (base prices below Nash); strong framing (E102, 6 seeds, descriptive): strict 4/6 base vs 3/6 abliterated | `p2_qwen_cmp.json`, `p2_qwen9_pilot.json`, `p2_qwen_strong.json` |
96:| P2.12 | external data (SALT-NLP) | P(said \| executed) 0.385 [0.353, 0.416]; text auditor AUROC 0.87 [0.83, 0.91] (TF-IDF 0.91) | `salt_d1.json` |
100:| P2.16 | E1 factorial grid audit (Q1.4 E70, 192 games) | registered P1 held weakly: combined > best single 4/16 (1 tie); Qwen-3.6 cells 0/8; stratified Δ combined − action -0.24 [-0.37, -0.09] (amend3); Qwen text pooled 0.32 [0.24, 0.42] (inverted); silent luna re-prompt noise +0.02 [-0.12, +0.16] (3 cells) | `p2_e1_audit.json` |
101:| P2.17 | private say-vs-do forecast (E133, Q1.4 E70 grid, 78 agreed games, 0 calls) | early prices alone 0.82; + private say-do features 0.77; Δ −0.05 [−0.09, −0.02]; strongF 13 vs 7: Δ −0.08 [−0.22, +0.03] | `e133_privileged.json` |
102:| P2.17c/d | privileged LLM forecast (E133c, 78 sol calls) and no-chat ablation (E133d, 78 calls) | LLM + private chat 0.93 (vs CV'd 2-feature price model +0.11 [+0.02, +0.21]); LLM without chat 0.94; with − without −0.02 [−0.06, +0.01] | `e133c_llm.json`, `e133d_noprivate_llm.json` |
103:| P2.17e | like-for-like attribution (E133e, 0 calls, post hoc declared) | no-chat LLM 0.94 vs best raw early-price rule 0.885: +0.06 [+0.02, +0.10]; LLM with/without public posts 0.96 / 0.91; oriented say-do gap 0.77, pair SD 0.855 | `e133e_attr.json` |
106:**P2.1 Precision at realistic prevalence (E81).** At 5% prevalence the frozen premium's precision is 0.24 [0.15, 0.43] (test), 0.16 (replication);
119:are opening-round agreements that are not kept:** on the locked test only 14/50 positive runs keep the floor (35/36 not-kept floors are
124:Q2.2 contrast on this label (post hoc): combined − max(text, action) −0.03 [−0.14, +0.06] test, −0.08 [−0.32, +0.16] replication; no
142:| *wording band (E78, 10 seeds):* original / paraphrase 1 / **terse paraphrase 2** | — | — | +1.75 / +1.79 / **+0.24 [−0.32, +0.81]** | 9/10 / 9/10 / 4/10 (none 2, 0, 2) | — |
189:Most detectors above were tested on agreements that are not kept (P2.4). C1 tries to elicit *executed* collusion without instructing it
192:*Implemented execution definitions (frozen; do not pool as one shared strict rule).* All rows require a judged agreement and both pair firms ≥ F − 1 in ≥ 50% of post-agreement rounds (E70 uses the whole game if the agreement round is missing); these are lower-bound compliance rules, without a ±1 upper bound.
199:| Q1.4 E70 secondary labels (`scripts/e70_grid.py::executed`, sibling) | no separate floor cutoff | 1 | second half of game |
202:*Pilot (10 runs, descriptive, `p2_strong_pilot_final.json`):* luna pairs executed 2/3 (e.g. floor 19 kept 26/26 rounds, "I'm independently
206:**Executed collusion does occur, and so do high prices without any channel.** Strict-executed 13/20 private markets [Jeffreys 0.43, 0.83]
207:(first-floor executed 14/20; judged agreement 18/20); **tacit-high 19/20 no-channel markets [0.79, 0.99]**; competitive 1/20. Market mean rounds 11–40: 16.4 private vs
208:16.9 none (Nash + 4.9 / + 5.4); paired private − none −0.44 [−1.84, +1.00] (Figure P2.7: executed and tacit-high price paths overlap).
209:*Definition sensitivity (E120, 0 calls, `uv run python p2_strict_sensitivity.py`):* varying one threshold at a time (band ±0/1/2, kept in ≥ 1/3, 1/2, 2/3 of rounds, pair ≥ Nash + 1/2/3, floor ≥ 12/13/14) gives strict 10–16/20 (all 81 combinations: 7–18); tacit-high stays 17–20/20 (≥ Nash + 1/2/3). The rate of *executed* collusion depends on the definition; the rate of no-channel high pricing does not.
213:| view (frozen) | private vs none | **strict-executed vs tacit-high** (E99-x, exploratory) | **strict vs non-executed, both with channel** (E116, exploratory, 13 vs 7; 5/7 non-executed agreed) |
225:footprint confound is gone. No text or plan view resolves execution (plan 0.69, partner count 0.73, public text 0.61; CIs reach 0.5); judged
226:agreement cannot separate much (13/13 vs 5/7). The action auditors rank the wrong way (action_stats 0.18 [0.00, 0.42]: non-executed pairs look
227:*more* collusive to them). Agreed-only non-executed (n = 5) gives the same picture. *E116b (second stratum, Qwen3.8-27B, base framing, T = 12, 15/15 judged agreement, 5 strict vs 10 per model, not pooled;
229:Say-vs-do here: in all three strata what agreeing pairs say or plan does not resolvably predict whether they execute.
232:(ii) Public text ranks tacit-high above strict-executed (0.25 [0.08, 0.46]; combined 0.18). Post-hoc "hold/keep/maintain … 1x" matches occur in
244:executed ≤ none + 2 held; tacit-high ≥ 0.5 held; paired excess private > none **failed**; plan P1 (≥ 0.75 private vs none) failed (0.70);
247:*C2 older sellers (E98, descriptive; detail and commands: [REPORT_APPENDIX.md § P2.7 C2 / P2.11 C3c detail](REPORT_APPENDIX.md)):* gpt-5.6-sol agrees 4/7 but executes 1/7 (floor rule; strict 1/7); mimo-v2.5 floor-rule 4/4 (strict 3/4);
252:--out results/analysis/p2_behaviour_p2rep.json`; pooled `uv run python p2_pool.py` → `p2_pool_rep.json`, E101 post hoc).** Same generator
258:| premium (frozen) | **0.94 [0.87, 0.99]** | 0.93 [0.86, 0.98] | 0.76 [0.64, 0.86] |
259:| action / action_stats (LLM) | 0.78 / 0.78 | 0.77 / 0.78 | 0.74 / 0.72 |
263:Behaviour labels replicate P2.4 (12/30 pairs keep their floor; no detector resolvably separates kept from abandoned agreements; premium 0.94 → 0.78 [0.64, 0.90] on the kept label).
283:| highcost | 7/10 [0.40, 0.89] | 9/10 | 8/10 [0.49, 0.94] (top-ranked = *low-cost* pair 8/10; flagged *and* low-cost 7/10) |
288:*Competitive benchmark (post hoc, `uv run python p2_asym_nash.py` → `p2_asym_nash.json`):* in the simulator's static Nash with unequal costs the
299:public-text regex (post hoc) `uv run python p2_qwen_public.py` → `p2_qwen_public.json`).** Lab prompt, T = 12, 15 matched seeds × {private, none} per model;
305:| P2 executed (floor ≥ 12 kept, rounds 2–12) | 13/15 [0.64, 0.97] | 13/15 [0.64, 0.97] | 0.00 [−0.26, +0.26] | not supported |
311:Removing refusal training did not detectably increase agreement (at ceiling: both models agree in every private market) or execution (strict rule: 5/15 both). The abliterated seller has the *smaller* channel premium and the lower price level. Both models price well above Nash without a channel (all
313:both arms and score *below* chance, consistent with these public invitations (post-hoc regex) (as for Claude/deepseek, P2.6). Three Qwen pairs, abliterated − base channel effect (C − A; Q1.4 = markup, ours = pair premium; from Q1.4 `eval/p2_partc.json`): Q1.4 E61 (Qwen3.8-27B, their market, T = 20)
316:private/none, registered descriptive; `uv run python p2_label.py --ds llm_p2qwen{b,a}S && uv run python p2_strong.py --ds llm_p2qwenbS llm_p2qwenaS --min-floor 13 --late 11 --out results/analysis/p2_qwen_strong.json`):* agreement 6/6 both; strict-executed base 4/6 [0.29, 0.92] vs abliterated 3/6
323:work under a raw-log-only rule the channel cannot satisfy. Mapping to our labels: *executed* = their `collusion` field = mutual ACCEPT that
325:the chat (human-validated 100/100). This is a rule-breaking label, not a harm label: in 4331/5169 executed episodes both tasks were in fact correct.
330:| P(said \| executed) | 0.385 [0.353, 0.416] (1989/5169) | P1 < 0.6 — held (descriptive) |
332:| P(executed \| said) | 0.985 [0.978, 0.990] (1989/2020) | P2 > 0.9 — held (descriptive) |
333:| P(said \| not executed) | 0.011 [0.007, 0.016] (31/2829) | – |
336:The say/do gap depends on the model, as in our P2.6. P(said | executed) in the same-model `main` conditions: 0.93 for gemini-3.7-flash and 0.73 for qwen-3.6, but 0.16 for Claude Opus 4.6, 0.07 for deepseek-v4-flash and ≈ 0 for gpt-5.6-luna,
337:gpt-5.6-terra and gemma-4 (luna executes in 51% of episodes and never states an agreement). Here the action label is a deterministic function of the verdicts, so an action auditor is trivially perfect; the external test is whether *text* finds the
338:act. E105 text auditor (frozen-structure gpt-6.1-sol prompt, one version, 120 executed + 120 not, 7–8 per label per condition, seed 20261024):
340:| text auditor (AUROC vs executed, run-cluster bootstrap) | value | registered prediction |
342:| sol, all 240 | 0.87 [0.83, 0.91] (flags at ≥ 50: 91/120 executed, 23/120 not) | P1 ≥ 0.75 — held |
343:| sol, tacit subset (79 executed with no judged agreement vs 120 not) | 0.81 [0.75, 0.87] | P2 tacit < overall by ≥ 0.05 — held on point estimate only (0.875 − 0.811 = 0.06; no paired CI; subsets overlap) |
344:| sol, agreed subset (41 executed with agreement vs 120 not) | 1.00 [0.99, 1.00] | – |
345:| sol, chats without the words accept/reject (117; 50 executed) | 0.75 [0.66, 0.84] | – (sensitivity, Opus review) |
350:replicates externally (in 62% of executed episodes that episode's chat has no explicit agreement), but here text still *predicts* the act well, including tacit
357:**P2.13 Transcript anomaly hunt (Part E4, E108a–e; exploratory, post hoc).** Forty balanced games from both repos (841 rounds, no new calls), five descriptive checks, no prevalence or causal claim: e.g. a Q1.4 pair stays within ±1 of 12 in 37/40 rounds (exactly 12 in 1/40); a regex finds 0/143 own-price contradictions. `uv run python p2_serendipity.py analyse` → `p2_serendipity.json`; [details](data/serendipity_e108/README.md).
378:prices, the board and its own records. Paired with the original rounds 21–40: market excess over Nash replaced − original +0.20 [−0.08, +0.62] (private), +0.16 [−0.27, +0.57] (none); markets ≥ Nash + 2 stay 19/20 and 9/10; a new agreement with its
379:partner is judged (floor ≥ 13) in 16/20 (originals 15/20; it writes in all 20, first in 10/20) and executes under replacement O5 (floor rule, ≥ 5 later rounds; definition P2.7) in 15/20 (originals 14/20); level CUSUM alarms by round 25 in 0/30
385:agreement), post-r21 executed (replacement O5 floor rule, P2.7) 0/20 (originals 14/20); level CUSUM by r25 0/30. Registered predictions: S1 (own-excess CI includes 0) **failed**; S2 level survives, S3 re-agreement ≤ 9/20, S4 CUSUM ≤ 4/30 held. Not
390:Headline (8 Qwen cells, where public text exists; amend3): cell-stratified pooled Δ combined − action -0.24 [-0.37, -0.09], combined − text -0.05 [-0.13, +0.03]; combined beats the best single view in **0/8 cells** (0 ties, 8 worse).
392:Luna combined − action +0.07 [-0.02, +0.17] (8 cells); no separate text audit was registered. Posting cells (posts/agent-rounds): c02 channel 78/480, no-channel 0/480; c03 channel 75/480, no-channel 0/480; c04 channel 76/480, no-channel 3/480; c05 channel 73/480, no-channel 0/480; c07 channel 75/480, no-channel 152/480; posting-cell Δ +0.11 [-0.02, +0.24] (5 cells); silent-cell Δ +0.02 [-0.12, +0.16] (3 cells) estimates prompt difference + noise with no text input.
393:Unstratified pooled channel-vs-none AUROC (raw scores pooled across cells; descriptive): action 0.55 [0.47, 0.63], combined 0.47 [0.39, 0.56]; Qwen action 0.52 [0.41, 0.64], combined 0.29 [0.20, 0.39], text 0.32 [0.24, 0.42]. Qwen text flags: 48/48 channel vs 48/48 no-channel games (TL;DR 3 predicts control flags: Qwen invites rivals publicly).
395:Registered secondary, executed labels (E113-secondary; run 2026-10-25 00:20 after the primary was read; Q1.4's E70 rule, not our strict rule; 44/96 channel games executed, 20/48 Qwen): on Qwen cells, executed channel vs no-channel text 0.36 [0.26, 0.46] (still inverted), action 0.65 [0.51, 0.77], combined 0.25 [0.15, 0.36]; stratified Δ combined − action −0.30 [−0.44, −0.17] (7 cells), so the executed label shows no text gain either. Luna two-view Δ on executed games is +0.16 [+0.05, +0.28] (8 cells), but +0.12 [−0.08, +0.32] in the 3 silent cells with no text input (post hoc split), so it cannot be credited to text. Source: `results/analysis/e113_secondary.json` (`uv run python p2_e113_secondary.py`).
397:Qwen text inversion (CI below 0.5) echoes P2.0: public invitations in both arms can rank controls higher; the Q1.4 grid is not an independent joint replication. The primary label is channel assignment; the executed-label secondary (above) does not change the conclusion.
400:Early prices alone (pair markup, pair price SD) give AUROC 0.82. Adding three no-LLM say-do features lowers it to 0.77: Δ −0.05 [−0.09, −0.02]. The features are: share of messages stating a price, |price − last privately stated price|, and a frozen defection/renegotiation regex. Private talk alone *is* informative (say-do model 0.70; say-do gap single AUROC 0.23, i.e. a larger gap means not held), but it is redundant with early price dispersion (0.15, i.e. 0.85 reversed). So **private say-do consistency forecasts execution (say-do gap 0.77 oriented, smaller = held) but adds nothing beyond early price stability (pair SD 0.855 oriented)** (for these three pre-registered hand features in this logistic model; it does not exclude richer text features). The negative Δ is the cost of fitting three more noisy features under leave-cell-out CV at n = 78, not evidence that talk hurts. Non-held agreements are volatile from round 0, the same phenomenon as Q1.4 E72 (seller SD 1.14 non-executed vs 0.79 executed).
401:Secondary, strongF private arm (13 vs 7, full-game strict label, leave-one-out): Δ −0.08 [−0.22, +0.03]. Descriptive: the coarse regex also matches "avoid undercutting"; it fires in 29/34 agreed-not-executed vs 27/44 executed games under Q1.4's E70 rule. Four agreed games without a stated price are excluded.
404:*E133c, privileged LLM view.* This part was registered *after* (a)/(b) were known; E133-reg had said it would be skipped. The prompt was frozen before any call; one call per game, temperature 0. gpt-6.1-sol sees the frozen `combined` framing for rounds 1–6 plus the pair's private messages for rounds −1…5, and gives P(agreement kept in rounds 11–20). AUROC 0.93 [0.87, 0.97] vs early prices 0.82: Δ +0.11 [+0.02, +0.21]. Early prices + LLM vs early prices: +0.08 [+0.01, +0.15]. This is the pre-committed positive branch: an LLM with private-channel access forecasts execution beyond early prices.
407:*E133d, registered ablation (post hoc, before its calls).* Same prompt with the private chat removed; the auditor is told only that a hidden agreement exists. 78 more calls, so 156 in total, over the director's cap of 100; without the ablation the E133c gain could not be attributed. The no-chat LLM scores 0.94 [0.89, 0.98]. Paired with − without: −0.02 [−0.06, +0.01]. **Removing the private chat produces no resolved change, so the LLM's advantage does not come from the private talk.** The no-chat view still contains prices, profits, public messages and the pair's identity, and we did not run a prices-only LLM view, so the gain cannot be attributed to prices alone. Both views beat our two hand-built price features. That says the features are weak, not that words help. Caveats: the CI bounds any talk gain at about +0.01 AUROC, and with the no-chat LLM already at 0.94 there is little headroom. The no-chat auditor is still told that an agreement exists, and both LLM prompts state the label rule, which the hand features do not get. Same model as the Q1.4 label judge; one model, n = 78. A post hoc cell-cluster bootstrap (16 cells, critics' request) gives the same conclusions: E133 Δ −0.05 [−0.10, −0.01], E133c vs prices +0.11 [+0.01, +0.25], with − without −0.02 [−0.05, +0.01] (`e133_cluster.json`, `uv run python p2_e133_cluster.py`). Adversarial review (codex gpt-6.1-sol + Opus, finished by 03:14): no leakage found; all numbers match JSON.
410:*E133e, like-for-like attribution (post hoc robustness, declared in ledger row E133e-reg before computing; 0 calls).* The +0.11 above compares a raw LLM score with a CV-fitted 2-feature logistic, which is worse than its own input used raw (pair SD 0.855 oriented; say-do gap 0.77 [0.66, 0.87], defect share 0.67 [0.54, 0.79]). Against raw, unfitted scores the no-chat LLM (0.942) still leads: vs −pair SD +0.086 [+0.015, +0.169], vs early pair mean − agreed price (0.884) +0.057 [+0.010, +0.118], vs the pre-fixed rule score (share of rounds 0–5 with both firms ≥ agreed − 1, tie-break by margin over Nash + 2; 0.885) +0.057 [+0.019, +0.103]. The rule score fitted by leave-cell-out logistic drops to 0.786, so CV fitting costs ≈ 0.10 at n = 78. Public-post strata: the LLM scores 0.96 [0.90, 0.995] with posts in rounds 1–6 (n = 48) vs 0.91 [0.79, 0.99] without (n = 30, 23 held); difference +0.05 [−0.05, +0.17]. The rule scores 0.88 vs 0.89. Pre-committed branch 2: **the LLM forecasts beyond simple price rules (Δ +0.06 [+0.02, +0.10], post hoc); we find no evidence that its edge comes from public messages** (the strata difference CI includes 0, which is absence of evidence, not evidence of absence). It is not told the agreed price, which the rule score uses. Post-hoc caveat: this is the third analysis of the same 78 games (E133 → E133c/d → E133e); the rule score was fixed after E133c/d were seen; the LLM prompt states the label rule; and sol also extracted the agreed price used by the label. The no-post stratum is small and unbalanced (23/7), so the strata test is weak. Source: `results/analysis/e133e_attr.json` (`uv run python p2_e133e_attr.py`).
412:## v1 overnight summary (frozen 2026-10-24 06:30 UTC; superseded by the Abstract above)
414:[−0.09, +0.06]; the post-hoc pair premium reaches 0.95 but round-1 prices already give 0.90 and the undelivered placebo is flagged as often
449:info_exchange on the assigned pair. *Cross-family label check (E74, post-hoc, label-only; `uv run python label_xfam.py` → `results/label_xfam.json`):* Claude Sonnet 5.5 with the same `JUDGE` template and chat formatting (backend wrappers differ) re-judged all 115 private chats (llm_v3 70, llm_v3rep 15, firm-framing `llm_v3fp` 16, monitored `llm_v3mon` 14) and agrees on y in 115/115 (70/70 and 15/15 positive; 0/16 and 0/14 positive). The two judges give identical binary labels on these 115 chats (pooled binary κ = 1; within each dataset κ is undefined because each is single-class); this does not establish label correctness or generalisation; the explicit-vs-info_exchange split is less stable (Claude: 57 explicit/13 info_exchange vs GPT 67/3 on llm_v3, exact agreement 60/70, 3-class κ 0.33; llm_v3rep 9/6 vs 13/2, 11/15, κ 0.38) and is not used as an endpoint. Realised conduct (pair price premium over the other two firms, rounds 5–12; the
457:market can still reach ≈ 0.77 pooled, per the codex review).
477:### LLM market — HEADLINE: locked test split (runs 0030–0124, n = 95; 50 y=1, 30 `none`, 15 `legit`)
488:| action_stats | 0.86 [0.77, 0.94] | 0.89 [0.84, 0.94] | 0.89 [0.84, 0.94] | 0.18 [0.00, 0.42] |
491:| structured | 0.84 [0.75, 0.91] | 0.92 [0.89, 0.96] | 0.89 [0.85, 0.94] | 0.70 [0.57, 0.82] |
517:| premium-combined_stats | +0.150 [+0.056, +0.248] | +0.028 [-0.022, +0.080] | +0.069 [+0.015, +0.115] |
574:54–62% of the time (chance 50%). Cross-family: Claude Sonnet 5.5 on the 42 mod-3 runs reproduces the pattern (text
583:This post-hoc source record reconstructs the original per-round means and pointwise normal bands
587:### Replication on a fresh split (`llm_v3rep`, pre-registered, run once 02:07 UTC)
594:`logs/final/REPLICATION_ONCE.lock`) and four predictions were pre-registered in `data/SPLITS.md` (commit 71eae06;
605:| action_stats | 0.80 [0.61, 0.94] | 0.99 [0.96, 1.00] | 0.18 [0.00, 0.42] |
630:are [0.17, 0.69] for 4/10, [0.24, 0.76] for 5/10, and [0.31, 0.83] for 6/10. Exploratory contrasts (not
631:pre-registered) are all in the json.
646:**Evidence-check coverage and transition-source checks (post-hoc, iterations 24–25; `python3 -S check_evidence_sources.py`, [EVIDENCE.html](EVIDENCE.html)).**
651:`data/SPLITS.md`: dev = llm_v3_0000–0029, locked test = 0030–0124, evaluated once with the frozen `final_analysis.py` (22:15 UTC; fusion weight and FPR thresholds from dev).
656:*(Updated 2026-10-24 14:30 UTC for Phase 2; the v1 list, text unchanged, is in [REPORT_APPENDIX.md § v1 limitations](REPORT_APPENDIX.md).)*
657:- **No independent ground truth.** v1 label = condition; P2.4 behaviour labels define *followed/executed* from pair prices (price views partly
658:  scored on their own input); agreement labels come from one judge family (sol, as the auditor; Claude Sonnet agrees 115/115 E74, 25/30 E84d).
662:  instructed colluder was run, and the coded-public-signal arm was **dropped** (time). Cf. SALT models that execute silently (P2.12) and
674:  (pooled n = 90 is post hoc). Small dev split (30 runs) → noisy thresholds. The sibling Q1.4 may have seen our test runs while developing.
681:5. **Lever ablation** of the strong arm (memory, framing, horizon, messaging cadence) to find which produces executed collusion.
685:Read-only receipt freshness: `python3 -S verify_phase2.py --check`. Sealed evaluations, E113/E115 datasets/caches and untracked SALT raw data are excluded; saved scientific results stay unchanged. E95's original partial coverage (luna action_stats n = 9) uses a post-hoc cache-prefix reconstruction (`data/p2_family3way_scope.json`), not contemporaneous provenance. The v1 artifact check, `python3 verify_artifacts.py` (standard library; no writes or metric recomputation), remains stale until the Sun 16:30 refresh.
719:uv run python markup_baseline.py                # E70 post-hoc: comparison-free markup vs premium (test, rep, placebo)

