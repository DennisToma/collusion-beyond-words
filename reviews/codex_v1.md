Checked 40+ submission statistics and all slide statistics against Q1.4 `0e06c03` and Q2.2 `8b680ee`, including the plotted headline values. Most numbers match. Below are remaining issues; completed round-1 fixes are omitted. Evidence paths are relative to the named source repo.

1. **P1 — Positive communication labels are presented as agreements.** SUBMISSION.md:135, 272.  
   **Current:** “on judge labels”; “14/50 judge-labelled test agreements”.  
   **Replace:** “on communication labels (positive = explicit agreement or information exchange; locked-test positives: 48 explicit, 2 information exchange)”; “14/50 communication-positive private test runs meet the E84 follow rule”.  
   **Evidence:** Q2.2 `label_llm.py:primary label`; `data/llm_v3/labels.jsonl:llm_v3_0047, llm_v3_0089` are `info_exchange`, not explicit agreements.

2. **P1 — The newly added luna result does not establish that text helps.** SUBMISSION.md:233.  
   **Current:** “So public text can help or hurt depending on how the seller family talks; it is not uniformly useless.”  
   **Replace:** “Combined-view performance varies by seller family, but the luna gain cannot be attributed to text: silent cells also show a positive point-estimate difference.”  
   **Evidence:** Q2.2 `results/analysis/e113_secondary.json:stratified.executed_vs_A.luna_silent_combined_minus_action_posthoc` = +0.120 [−0.083, +0.324]; `REPORT.md:P2.16` explicitly withholds attribution to text.

3. **P1 — The new tacit-high definition uses the wrong window.** SUBMISSION.md:113; clarify the abbreviated claims at 30, 261–262 and SLIDES.md:63 too.  
   **Current:** “no-channel market whose second-half mean ≥ Nash + 2”.  
   **Replace:** “Q2.2 strong-framing no-channel market whose mean price minus cost-adjusted Nash over rounds 11–40 is ≥ 2”.  
   **Evidence:** Q2.2 `p2_strong.py:analyse` uses `late=11`; `p2_strong_eval.py:main` freezes that setting; `REPORT.md:P2.7` specifies rounds 11–40.

4. **P1 — The slide conclusion contradicts its own inverted text results.** SLIDES.md:71.  
   **Current:** “Channel assignment … is visible as **how high** prices are — not **how they move together**, and not in **what is said publicly**.”  
   **Replace:** “Channel assignment mainly separates price levels. We detect no contemporaneous dependence advantage; public text can rank channel markets below controls, and adding it gives no resolved gain in the base-market comparisons.”  
   **Evidence:** Q2.2 `results/analysis/p2_strong_eval_llm_p2qwena.json:detectors.text.auroc_private_vs_none` = 0.147 [0.051, 0.253]. Inversion demonstrates information, not absence of a signal.

5. **P1 — Evasion resistance is asserted without an evasion test.** SUBMISSION.md:44.  
   **Current:** “cannot be evaded by choosing words”.  
   **Replace:** “does not inspect wording directly; resistance to strategic evasion was not tested”.  
   **Evidence:** Q1.4 `REPORT.md:Limitations` states that there is no evasive-collusion arm; predictable rotation is a documented blind spot in §P2.6.

6. **P1 — “Every planted pair” overgeneralises the positive control.** SUBMISSION.md:18–19.  
   **Current:** “which finds every planted pair on scripted sellers”.  
   **Replace:** “which flags and localises every pair in the scripted shared-signal positive control (T = 100, strength 0.6)”.  
   **Evidence:** Q1.4 `results/eval/gate_test.json:args, metrics.pcmi.C`; `results/p2/rotation_test.json:summaries` and `REPORT.md:P2.6` report only 6/30 and 2/30 flags for predictable rotation.

7. **P1 — Figure 4 still labels its target as realised coordination.** SUBMISSION.md:200; SLIDES.md:50, embedded figure’s x-axis.  
   **Current:** “private-channel coordination vs not”.  
   **Replace:** “communication-positive vs negative (test); channel assignment vs controls (replication)”.  
   **Evidence:** Q2.2 `results/analysis/final_llm_v3_gpt-6.1-sol_test.json:endpoint`; `results/analysis/p2_behaviour.json:datasets.llm_v3.class_counts` distinguishes 14 followed from 36 not followed among the 50 positives.

8. **P2 — The new strict-executed definition remains a reference rather than a definition.** SUBMISSION.md:111.  
   **Current:** “registered strict rule (E99-amend) on the strong-framing arm”.  
   **Replace:** “judged agreement with floor F ≥ 13; ≥ 10 later rounds; both firms price ≥ F − 1 in ≥ ½ those rounds; post-agreement pair mean excess over Nash ≥ 2”.  
   **Evidence:** Q2.2 `REPORT.md:P2.7, Implemented execution definitions`; `p2_strong.py:analyse`.

9. **P2 — The slides drop estimator-power qualifications restored in the body.** SLIDES.md:43.  
   **Current:** “Rank and discrete estimators: also at chance. At T = 60, pCMI would catch a planted shared ±1 move…”  
   **Replace:** “Rank and discrete estimators also show no resolved separation; sparse state strata limit sign-CMI power. For one planted shared ±1 strategy at T = 60 and q = 0.1, pCMI AUROC is 0.79 [0.70, 0.88]; this is not a general sensitivity bound.”  
   **Evidence:** Q1.4 `results/eval/e73_nonlinear.json:E70, sensitivity_q0.1`; `REPORT.md:P2.8(f)`.

10. **P2 — The slide’s locked-test presentation omits disclosed exposure and statistic selection.** SLIDES.md:52, including the figure at 50.  
    **Current:** “(locked test, n = 95)”.  
    **Replace:** “(locked test, n = 95; not fully blind—four disclosed exposures; plotted premium statistic selected post hoc)”.  
    **Evidence:** Q2.2 `REPORT.md:Splits, blinding and disclosed exposures`; `results/analysis/claims_denominators.md:C05`. These caveats are present in the submission but absent from the standalone slides.

11. **P2 — The notepad ratio is juxtaposed with round 1 without identifying its actual window or metric.** SLIDES.md:62.  
    **Current:** “≈ two thirds of the channel premium (ratio 0.65 [0.34, 1.32])”.  
    **Replace:** “≈ two thirds of the channel’s effect on designated-pair-minus-rivals premium over rounds 2–12 (ratio 0.65 [0.34, 1.32])”.  
    **Evidence:** Q2.2 `results/analysis/p2_cue_llm_p2cue.json:H3_notes_over_private_r2_12, paired`.

12. **P2 — “Executed agreements only” obscures the negative class and denominator.** SLIDES.md:41; SUBMISSION.md:169.  
    **Current:** “executed agreements only (48/149)”.  
    **Replace:** “Executed channel games vs no-channel controls within each set (48 executed among 149 labelled channel games; Q1.4 rule)”.  
    **Evidence:** Q1.4 `results/eval/p2_partc.json:E64_pooled["all sets"]`; `results/eval/executed_sensitivity.json:caveat`. This is not executed versus unexecuted agreements.

13. **P2 — The universal public-cost description excludes part of E70.** SUBMISSION.md:86–87.  
    **Current:** “with multinomial-logit demand, public cost and demand shocks, and integer prices”.  
    **Replace:** “with multinomial-logit demand and integer prices; cost and demand state are generally public, but E70 varies cost visibility and rival-price visibility”.  
    **Evidence:** Q1.4 `data/llm_grid_p2_manifest.json:cells[*].levels.cost, cells[*].levels.rivals`; cost levels include `private` and `public`.

14. **P2 — The causal interpretation omits the pricing-content control.** SUBMISSION.md:291–292.  
    **Current:** “part of it is caused by the prompt that singles out the pair rather than by delivered messages”.  
    **Replace:** “private pricing deliberation can raise levels without delivered messages; the logbook control suggests that merely singling out a pair is insufficient, subject to instruction-length and batch-timing confounds”.  
    **Evidence:** Q2.2 `results/analysis/p2_logbook.json:paired`: logbook−none +0.218 [0.052, 0.400], logbook−notes −0.824 [−1.170, −0.452]; `REPORT.md:P2.5` supplies the confounds.

15. **P2 — The AUROC glossary omits ties and assumes one label construct.** SUBMISSION.md:63–64.  
    **Current:** “probability that a random channel market scores above a random control”.  
    **Replace:** “probability that a random positive example scores above a random negative example, with half credit for ties; the positive class is specified per analysis”.  
    **Evidence:** Q2.2 `p2_strong_eval.py:auroc` explicitly adds `0.5 * (p == n)`; the submission also evaluates execution and SALT labels.

16. **P2 — The slides’ sample-size range omits their smallest experiments.** SLIDES.md:79.  
    **Current:** “small samples (10–21 games per arm)”.  
    **Replace:** “small samples (often 5–21 games per arm; E70 has 6 per cell and arm)”.  
    **Evidence:** Q2.2 `results/analysis/claims_denominators.md:C08` gives five Claude controls; Q1.4 `results/eval/e70_grid.json:complete_sweeps` = 6.

---
## Merge-manager disposition (2026-10-25 ~09:25 UTC)
Evidence spot-checked for 1 (`labels.jsonl` 3 info_exchange rows), 3 (`p2_strong.py --late 11`; REPORT rounds 11–40), 13 (E70 manifest: cost private/public, rivals hidden/visible), 14 (`p2_logbook.json` paired; REPORT l.155–159).
All 16 applied: 2, 4, 16 overlapped with Opus round 2 (already applied); 7 handled by a caption note (figure is a source copy, axis not regenerated); 10 applied on slides (SUBMISSION §3 already states it).
