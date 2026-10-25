- **P1 — §5.4, Figure 6:** “so price paths cannot separate them.”
  **Problem:** Overlapping class means and bootstrap bands do not establish that price paths cannot distinguish individual markets. Tested price views showed no resolved separation; impossibility was not tested.
  **Evidence:** [figure code](/home/factory/collusion/collusion-beyond-words/scripts/fig6_strong_framing.py), [source results](/home/factory/collusion/collusion-22-say-vs-do/results/analysis/p2_strongF_report_llm_p2strongF.json).
  **Replace with:** “Right panel: the no-channel tacit-high class (green) and strict-executed channel class (blue) have overlapping mean price paths and bootstrap bands; the tested price views show no resolved separation.”

- **P2 — TL;DR / slide takeaway:** “We detect no contemporaneous price co-movement” / “we detect no co-movement.”
  **Problem:** The TL;DR omits the base-Qwen3.6 exception; the slide also sweeps in lagged dependence, which was resolved above chance.
  **Evidence:** [main-set JSON](/home/factory/collusion/collusion-14-infotheory/results/eval/claims_denominators.json) (base-Qwen3.6 pCMI 0.71 [0.51, 0.88]); [grid JSON](/home/factory/collusion/collusion-14-infotheory/results/eval/e70_grid.json) (TE 0.62 [0.54, 0.70]).
  **Replace the respective clauses with:** “We detect no robust contemporaneous price co-movement” / “we detect no robust contemporaneous co-movement.”

- **P2 — Glossary:** “Locked test: a split frozen before any tuning and scored once.”
  **Problem:** “Scored once” overstates isolation: only the final frozen evaluation was run once; partial-test results had already informed adaptive analysis choices.
  **Evidence:** [source REPORT, Held-out discipline](/home/factory/collusion/collusion-22-say-vs-do/REPORT.md:658), [detailed disclosures](/home/factory/collusion/collusion-22-say-vs-do/REPORT_APPENDIX.md:815).
  **Replace with:** “**Locked test**: a fixed test split whose final evaluation was run once under a frozen configuration; here it was not fully blind (four disclosed exposures, §3).”

- **P2 — §5.3, forecasting summary:** “with the private chat, say–do features add nothing beyond early price stability.”
  **Problem:** Drops the restriction to three hand-built features in one logistic model. Appendix C retains it, but the new summary generalises the result.
  **Evidence:** [source REPORT §P2.17](/home/factory/collusion/collusion-22-say-vs-do/REPORT.md:407), [E133 JSON](/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e133_privileged.json).
  **Replace with:** “Briefly, three hand-built say–do features in one logistic model add nothing beyond early price stability; richer text features are untested, and there is no evidence that public messages add predictive value.”

- **P2 — §5.3, inversion:** “so the association comes from the arm difference.”
  **Problem:** Too categorical: pooled correlation plus an unresolved control-arm correlation does not attribute the entire association to arm differences. The source says “mainly between arms”; no within-channel correlation is reported.
  **Evidence:** [E132 JSON](/home/factory/collusion/collusion-22-say-vs-do/results/analysis/e132_inversion.json), [source interpretation](/home/factory/collusion/collusion-22-say-vs-do/REPORT_APPENDIX.md:857).
  **Replace with:** “so the pooled association does not establish a positive relationship within arms.”
