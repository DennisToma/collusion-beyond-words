Numerical values in the changed claims match the source JSON. Remaining issues:

- **P1 — [SLIDES.md:65](/home/factory/collusion/collusion-beyond-words/SLIDES.md:65): equivalence is unsupported.**  
  **Current:** “offered-but-never-delivered channels carry the same premium”  
  **Replace:** “offered-but-never-delivered channels show no resolved premium difference from delivered channels over rounds 2–12; this does not establish equivalence”  
  **Source key:** Q2.2 `results/analysis/placebo_llm_v3plc.json:windows.r2_12.placebo_minus_private_paired`; Q1.4 `REPORT.md:§5` explicitly rejects an equivalence interpretation.

- **P1 — [SLIDES.md:68](/home/factory/collusion/collusion-beyond-words/SLIDES.md:68): dropped estimation caveat.**  
  **Current:** “no frozen price flag reaches precision 0.25 (max 0.20; largely set by α = 0.05)”  
  **Replace:** “none of the tested frozen price flags reaches point-estimate precision 0.25 (maximum 0.20 [0.07, 0.54]; largely set by α = 0.05, not a bound on achievable precision)”  
  **Source key:** Q1.4 `results/eval/prevalence.json:[5].precision@0.01{,_ci}`. The interval includes values above 0.25.

- **P1 — [SUBMISSION.md:18](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:18): the Abstract’s blanket null suppresses an exception.**  
  **Current:** “**We detect no contemporaneous co-movement.**”  
  **Replace:** “**We find no robust contemporaneous co-movement signal across sets.** One base-Qwen3.6 set separates (0.71 [0.51, 0.88], uncorrected), but this does not replicate in the grid; small effects at T = 20 remain unexcluded.”  
  **Source keys:** Q1.4 `results/eval/claims_denominators.json:sets[set=llm_qb36_p2].pcmi{,_ci}`; `results/eval/e70_grid.json:amend2_by_model.qwen.pcmi{,_ci}`; `REPORT.md:P2.8, P2.14`.

- **P2 — [SUBMISSION.md:28](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:28): Abstract still omits the measurement window.**  
  **Current:** “gpt-6-luna markets *without* a channel price ≥ Nash + 2”  
  **Replace:** “gpt-6-luna markets *without* a channel have market-mean price minus cost-adjusted Nash ≥ 2 over rounds 11–40”  
  **Source key:** Q2.2 `results/analysis/p2_strong_classes_llm_p2strongF.json:n_tacit_high_none`; `REPORT.md:P2.7`.

- **P2 — [SUBMISSION.md:110](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:110): restore the removed arm qualifier.**  
  **Current:** “registered strict rule (E99-amend):”  
  **Replace:** “registered strict rule for the strong-framing arm (E99-amend):”  
  **Source:** Q2.2 `REPORT.md:P2.7, Implemented execution definitions` specifies arm-dependent floor cutoffs; `results/analysis/p2_strong_classes_llm_p2strongF.json:n_strict_executed` supports this arm’s 13/20.

- **P2 — [SLIDES.md:64](/home/factory/collusion/collusion-beyond-words/SLIDES.md:64): identify what the ratio compares.**  
  **Current:** “≈ two thirds of the channel's premium, rounds 2–12”  
  **Replace:** “≈ two thirds of the channel’s effect versus no channel on designated-pair-minus-rivals premium over rounds 2–12”  
  **Source key:** Q2.2 `results/analysis/p2_cue_llm_p2cue.json:H3_notes_over_private_r2_12`, derived from `paired.{notes-none,private-none}.prem_r2_12`.

No additional P1 in the full §6; its causal and proposed-pipeline qualifications are supported.
