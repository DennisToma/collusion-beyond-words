# Adversarial review of SUBMISSION.md v0 (Opus subagent, 2026-10-25)

Scope: SUBMISSION.md + SOURCES.md checked against the source repos at the synced commits
(Q1.4 `0e06c03`, Q2.2 `8b680ee`, both still HEAD). Line numbers refer to SUBMISSION.md v0.
Values verified directly in JSON are marked [JSON]. Severity: P1 = wrong / mis-attributed / untraceable
number; P2 = overclaim or dropped caveat; P3 = clarity.

## Numbers verified correct [JSON]
These all match: N2 and N4 (claims_denominators.json `sets[*].ml/pcmi/pcmi_ci`), N3 (e74 `main_sets.llm_g56l_p2.level_minus_pcmi`
= 0.03 [−0.27, 0.33]; `llm_qb36_p2` 0.218 [0.027, 0.436]), N5 (long_power `prefix.60.pcmi` 0.3375 [0.1775, 0.5175],
`pair_markup` 0.9425 [0.86, 0.9975]), N6 (`mde.60.by_q.0.1` 0.794 [0.704, 0.884]; `mde.20.by_q.0.1` 0.622; `mde.60.observed_C_comove_excess`),
N7 (p2_partc `E64_pooled.all sets.pcmi.executed` 0.422 [0.328, 0.532], 48 vs 101), N8 (e70_grid `pooled_auroc`, `level_vs_pcmi`),
N9, N11 (e73), N12 (e72 `a_pair_naming`, `c_execution`), N13 (gate_test `metrics.pcmi.B` 0.14, `B+shared_policy` surrogate 0.04;
`te.A+legit_cooperation` 1.0), N14 (costasym_test `A/costasym`), N15 (prevalence.json max precision@0.01 = 0.202), N19.
Also M1, M2, M3, M4, M6 (Qwen −0.236 [−0.372, −0.09]), M7, M9 (p2_cue `paired`, para2 0.236 [−0.318, 0.814]), M10, M11, M12, M13, M14
(p2_aware `aware.agreement_y` [0, 10]), and M15 (label_xfam.json, binary 115/115). The problems below are about attribution,
framing and dropped caveats, not arithmetic.

## Findings (most severe first)

1. **P1 — "only dependence statistic above chance" is false (L155–156).** It says: "The only dependence statistic above
   chance is lagged TE in the grid". But Q1.4 `results/eval/e74_paired_diff.json : main_sets.*.te` has TE = 0.809
   (deepseek, `llm_ds_p2`) and 0.907 (base Qwen3.8, `llm_qb_p2`). Q1.4 REPORT P2.9(c) reports deepseek TE 0.81 [0.62, 0.96],
   i.e. above chance. Level − TE is unresolved in 3/9 main sets (`summary.k_level_minus_te_ci_above_0` = 6 of 9; e.g. `llm_qb_p2`
   +0.056 [−0.067, +0.213]). Fix: "lagged TE is above chance in the grid (0.62) and in some main sets (deepseek 0.81 [0.62, 0.96]);
   it is below level in the grid and in 6/9 sets". This also weakens "not dependence" in the merged narrative (item 2).

2. **P2 — The merged narrative is not supported as worded (L15, L54, L137, L232–234, title of §5.2).** "Collusion shows up in
   price level, not dependence or public words" goes beyond the evidence in three ways.
   - *Level ≠ collusion.* All AUROCs score channel *assignment*. §5.4 itself says an unread notepad gives 65% of the premium,
     the undelivered placebo gives +1.23, and delivery is unresolved (+0.38 [−0.41, +1.18]). Q1.4 takeaway (4) says level
     screens detect "a pair singled out by the prompt, not delivered coordination" (P2.10: notepad named 11/15 vs private 12/15).
     Q1.4's own market has no placebo arm (L258). What is shown is that *channel assignment, including its prompt cue,* shows up
     as a level.
   - *Dependence.* The finding is "no detected *contemporaneous* co-movement". Lagged TE is above chance (item 1). At T = 20
     (most sets, all of E70) pCMI detects the planted q = 0.1 move at only 0.62 [0.52, 0.71].
   - *Words.* See items 3, 5 and 6.

   Suggested wording: "the private channel (and its prompt cue) shows up as a higher price level; we detect no contemporaneous
   co-movement, and a zero-shot auditor gains nothing from public text."

3. **P1 — "A public message board exists in every arm" is false for Q1.4 (L90–91).** Q1.4 `sim/llm_market.py` has `--public`
   off by default (L375). REPORT §4.3.1 lists `llm_pilot` as "public board off". The deepseek board arm was a separate
   experiment (E59, P2.9e: "+0.70 … no board → board"). Only E70 has the board on. The sentence comes from Q2.2's one-minute
   box ("the public board exists in all arms"), which is true only for Q2.2. Consequence: the "words" half of the narrative
   rests on Q2.2's markets plus E70, not on Q1.4's 9 main sets.

4. **P1/P2 — "prices alone are at chance (0.52 [0.41, 0.64])" contradicts Q1.4 on the same games (L186).** 0.52 is Q2.2's
   *LLM action-view auditor*, unstratified (`p2_e1_audit.json : pooled_auroc_channel_vs_none_descriptive.action_qwen` =
   [0.524, 0.411, 0.639]). On the same 96 Qwen games, Q1.4's max-pair markup scores 0.757 (`e70_grid.json :
   amend2_by_model.qwen.market_level`; level − pCMI +0.295 [0.146, 0.441]). A merged report that promotes the level screen
   cannot say "prices alone are at chance" there. Write "the LLM reading prices is at chance (0.52), although the markup
   statistic is not (0.76)".

5. **P2 — Only the negative side of the E113 cross-application is quoted, so "text helps only where…" is overclaimed (L25,
   L186–187).** In the luna cells of the same grid, combined − action is +0.073 [−0.021, +0.17] (`p2_e1_audit.json :
   amend3.luna_stratified_combined_minus_action_noise`). On executed games it is **+0.161 [+0.051, +0.277]**, a resolved
   *gain* (`e113_secondary.json : stratified.executed_vs_A.luna_combined_minus_action`; this is the same registered secondary
   whose Qwen −0.30 is quoted). Q2.2 also reports E116 text 0.61 [0.37, 0.85] within channel pairs and E116b Qwen-abliterated
   0.73 [0.43, 0.99] (both exploratory). Either report the luna side or drop "only".

6. **P2 — The inversion claims drop their CI caveat and over-generalise the mechanism (L23–24, L173–176, L183–185).**
   - Q2.2's merge block says the text AUROC CI lies below 0.5 "only for the two Qwen-3.8 arms". Claude 0.22 [0.00, 0.52]
     (5 + 5 runs) and deepseek 0.36 [0.20, 0.52] are not resolved inversions.
   - The invite mechanism (0.40 vs 0.88) is Qwen3.8 base only (`e132_inversion.json : sets['Qwen3.8 base'].arms.*.invite_rate_pooled`).
     For deepseek (1.000 vs 0.999) and Claude (0.875 vs 1.0) the invite rates do not differ, so it explains nothing there.
   - An inverted AUROC of 0.15 means the text *is* informative with the opposite sign. "Public messages add nothing" is a
     statement about a zero-shot auditor's orientation, not about the words. Say so.

7. **P2 — Execution definitions are not "stated where used", although L95–96 promises it.** Q2.2's merge block says: "Do not quote
   … any executed count without its definition". Unlabelled uses:
   - L18–19 and L149 (Q1.4 rule; 13–78/149 under 27 variants, pooled pCMI 0.343–0.531, E71 — dropped);
   - L187 (Q1.4 E70 rule, computed after the primary was read);
   - L205 "13/20 channel pairs keep their agreement" (Q2.2 strict rule, E99-amend; 10–16/20 one-at-a-time, `p2_strict_sensitivity.json`, C29);
   - L212 (E84 follow rule);
   - L191 "held" (E133 rule);
   - L227: the joint statement juxtaposes 13/20 (Q2.2 strict, re-scored by Q1.4 as E66) with 5/20 (Q1.4 rule, E65) in one
     sentence, without saying so.

   Add a three-row definitions box in §3 and tag each count.

8. **P2 — Label validation is overstated (L93–95, L247–248).** Binary agreement in `results/label_xfam.json` is degenerate:
   both judges say y = 1 for all of `llm_v3` (70/70) and `llm_v3rep` (15/15), and y = 0 for all of `llm_v3fp` (16) and
   `llm_v3mon` (14). Agreement is fixed by dataset membership. The 3-class kappa is 0.328 (`llm_v3`) and 0.375 (`llm_v3rep`).
   A second check (E84d, REPORT_APPENDIX.md:750) has Claude matching sol on agreed yes/no in only **25/30**, on floor in 23/30,
   and reading 18/21 "not-kept" agreements as opening-round-only. That bears directly on "14/50 kept" (L212). Also, all 115
   chats are Q2.2's; Q1.4's 149 + 96 judge labels have no cross-family check.

9. **P2 — Q2.2's test is "locked but not fully blind" (L99–101, L168).** Q2.2 REPORT.md:652 lists "four disclosed exposures
   (iteration-3 interim, premium choice, shuffle smoke test, early TF-IDF fit)", and `data/SPLITS.md`:15 an interim Δ_hybrid
   on 24 test runs. The premium was chosen post hoc after v1 (claims C05). Figure 4's headline ("a one-line price statistic ranks
   highest") rests on that post-hoc choice. Add one clause.

10. **P2 — The abstract drops qualifiers that the body or sources keep (L26–29).**
    - "65%" needs its CI [0.34, 1.32]. The registered H3 rule did not hold (`p2_cue_verdict_llm_p2cue.json : H3_amended.held`
      = false), so the notepad share is not resolved.
    - "19/20 no-channel markets" is gpt-6-luna only; Q1.4 E65 abliterated Qwen with memory is tacit-high in 0/20
      (claims_denominators.json `llm_strong_qa.tacit` [0, 20]).
    - "no flag reaches precision 0.25" needs "point-estimate" (L210 has it; Q1.4 notes upper CIs up to 0.68). It is also
      largely mechanical: at α = 0.05 with TPR = 1, FPR ≈ 0.04 gives precision 0.20 (`prevalence.json` maximum 0.202). It
      covers only scripted, llm_v1 and llm_v3 settings.

11. **P2 — The prompt-wording robustness failure is dropped (L15–17, L145).** In claims_denominators.json, wording group:
    C − A CI > 0 in only **2/5** wordings; level > pCMI 4/5; markup AUROC 0.31 (template) and 0.47 (noreason) (Q1.4 takeaway 1).
    "9/9" holds for main sets under one prompt family. In addition, L201–202 quotes only the paraphrase that shrinks the
    premium (+0.24, `p2_cue_llm_p2para2.json`). The other paraphrase gives **+1.79 [1.20, 2.43]** (`p2_cue_llm_p2para1.json`),
    both with 10 + 10 runs, not 15.

12. **P1 — E133 is mis-framed (L191–194).** The 0.94 is the *no-chat* LLM (E133d; `e133e_attr.json :
    b_llm_E133d_minus_raw.rule_score` = [0.057, 0.019, 0.103]), yet the sentence opens with "With privileged access to the
    private chat". The data are Q1.4's E70 grid (78 agreed games, 48 held / 30 not). The target is held-vs-not *among agreed
    games*, not channel vs none. Say both.

13. **P2 — The joint statement drops Q1.4's own qualifier (L222–228).** Q1.4's copy continues: "In our sets with spillover the
    relative pair_level screen loses power rather than failing outright: AUROC 0.75–0.80 vs market level 0.85–0.94". It also
    gives the provenance of the luna numbers (Q2.2 arm re-scored as E66) and the Qwen numbers (E65, T = 40). Without these,
    "fail under market-wide spillover" overclaims for Q1.4's data. "As the first sentence predicts" is a post hoc
    rationalisation and should be labelled as such.

14. **P2 — TE's scripted false-positive profile is omitted (L133–134).** `gate_test.json : metrics.te` flags shared_policy in
    0.90 (A) and 0.98 (B) of runs, independent_high_price in 0.62, and finds the planted pair in only 0.22 (C). Because lagged
    TE is the one LLM dependence signal above chance, readers need to know it fires on shared policies. That is a plausible
    reading of the E70 TE signal, which sits in *non-executed* games.

15. **P1 — SOURCES M6 traces the executed-only −0.30 to the wrong file.** In `p2_e1_audit.json` the field
    `secondary_executed_vs_no_channel.provenance.state` is "unavailable". The number is in `e113_secondary.json :
    stratified.executed_vs_A.qwen_combined_minus_action` = −0.304 [−0.443, −0.165] (7 cells). The 0.52 key is
    `pooled_auroc_channel_vs_none_descriptive.action_qwen`.

16. **P1 — SOURCES rows without a file:key, though the claims tables give exact keys.**
    - N18 → `eval/e68_cda.json`
    - M5 → `analysis/e132_inversion.json : sets['Qwen3.8 base'].arms.{channel,no_channel}.invite_rate_pooled`
    - M10 → `analysis/p2_strong_classes_llm_p2strongF.json : n_strict_executed, n_tacit_high_none`
    - M11 → `analysis/p2_behaviour.json : datasets.llm_v3.class_counts.{followed,not_followed}`
    - M13 → `analysis/p2_asym.json : conditions.{highcost,quality,none_ref_p2cue}.premium_flags` and
      `analysis/p2_prevalence.json : llm_v3_test.detectors.premium['precision@0.05']` (0.237)
    - M14 → `analysis/p2_aware.json : by_condition.{aware,aware_all}.agreement_y`
    - M15 → path is `results/label_xfam.json` (not under `analysis/`)
    - M16 → `analysis/p2_replace_sol.json : arms.private.O4_reagreement_floor_ge13.repl, O6_market_excess_ge2.repl`
    - M9's ratio CI [0.34, 1.32] is not a key in `p2_cue_llm_p2cue.json`; it appears only in Q2.2 REPORT.md:145. Name the
      generating script or mark it as text-only.

17. **P1 — Table 2 n for Claude (L173).** "10" is 5 + 5 runs (claims C08: 5 Claude controls). Write "5 + 5" like the Qwen
    rows. The tiny n is why its CI reaches 0.00–0.52.

18. **P1 (minor) — Model and market counts (L13, L80, L87–89).**
    - "7 seller models" is Q1.4's count. The merged study also uses Claude Sonnet and gpt-6.1-sol sellers, plus a mimo arm
      (`p2_strong_eval_llm_p2mimo.json`).
    - "Q2.2 market: 12 rounds" is not universal: P2.7 strong framing is T = 40 (Fig. 6 caption).
    - L98 "locked seeds (1001/1002)": the P2.4 cost-asymmetry test uses seed 2003 (`costasym_test.json : seed0`).

19. **P2 — Provenance of E74's "declared" status (L17, L146).** Q1.4 REPORT.md:849 says the E74 declaration and results
    "first appear together in commit 45679ff; git does not independently establish their order". "Paired difference CI > 0 in
    8/9" is an abstract headline, so add "(declaration order unverified)", or present it as robustness rather than declared.

20. **P2 — Statistics framing in the abstract (L16–17).** "beat pCMI in 9/9" compares point estimates (Q1.4: "higher
    point-estimate run AUROC"). The interval claim is 8/9, with per-set CIs uncorrected. The locked-test contrast (L22) uses
    judge labels, while the replications use channel-condition labels. Note the switch, or say the two coincide on test (all
    50 private test runs are judged y = 1, `p2_behaviour.json`).

21. **P2 — Independent reimplementation scope (L112).** The 422/424 cells cover only `llm_v1`, `llm_long` and `llm_long_first20`
    (`reimpl/compare.json : scores`), not the nine P2 main sets. Say "on the v1 datasets" (Q1.4 §6 separately verifies 9,490
    saved score cells against the frozen implementation).

22. **P3 — Unfinished draft markers will hurt with judges (L8, L291–294 in v0).** Remove or resolve "Draft v0 … numbers not
    yet independently re-verified". The "Appendix — To be filled" placeholder was being filled while this review ran (the
    working copy now has verbatim tables A/B; L1–289 are unchanged, so the line numbers above still apply). Note that the
    verbatim Q1.4 table repeats "no frozen flag reaches precision 0.25" without "point-estimate" (see item 10). SOURCES.md now
    has 22/36 rows ✔; the keys in items 15–16 can close most of the rest.
23. **P3 — The abstract is too dense for hackathon judges (L12–30).** It runs to about 300 words with pCMI, SALT, Nash + 2, TE
    and seven CIs. Lead with three plain bullets ("a private channel raises price levels; we detect no co-movement; a zero-shot
    auditor gets nothing from public text, and neither signal is collusion-specific"), then numbers. Define AUROC and "level"
    once, and add a one-line glossary for E-numbers or remove them from the main text (E70, E113, E133e, P2.x appear without
    definition).

24. **P3 — Figure/text mismatch (L168 vs L181–182).** Figure 4(a)'s "fresh replication" is n = 30 (`llm_v3rep` only) and shows
    text 0.67 and combined 0.62. The text quotes the pooled n = 90 contrast. Say in the caption that the pooled n = 90 contrast
    is not plotted, or plot it.

25. **P3 — Structure.** §5.5 is a verbatim quote block whose two quoted sentences are hard to parse out of context. Move it to
    §6 and paraphrase it with the definitions. §5.4's "Prompt wording alone moves no-channel markup −0.19 to +2.56" (Q1.4,
    P2.7) sits inside a Q2.2-sourced bullet without attribution. Tag the project per bullet, as elsewhere.
