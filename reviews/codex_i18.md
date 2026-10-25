# codex gpt-6.1-sol (high, read-only) final judge review, iter18 (2026-10-25 ~12:00 UTC)

Prompt: /var/tmp/judge_prompt.txt (internal consistency, overclaim drift, clarity). All items applied (iter18) after checks against source JSON/code; 491→492 fragment count reflects the iter18 additions.

- **P1 — Agreement labels reappear incorrectly in the appendix.** [SUBMISSION.md:504](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:504)  
  **Current:** “test 'colluders' that keep their agreement”; “n=50 judged-agreement private runs”  
  **Conflict:** Lines 167–168 specify **48 explicit agreements and 2 information exchanges**; line 329 correctly says “communication-positive”.  
  **Replace respectively:** “communication-positive test runs meeting the E84 follow rule”; “n=50 communication-positive private runs”.

- **P1 — Appendix comparator again hides privileged information.** [SUBMISSION.md:525](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:525)  
  **Current:** “E133e no-chat LLM minus best raw early-price rule score; oriented say-do gap and pair SD AUROC”  
  **Conflict:** Lines 533–534 explicitly say this rule uses early prices **and the privately judged agreed price**.  
  **Replace:** “E133e no-chat LLM minus best raw agreement-informed compliance rule score; oriented say-do gap and pair SD AUROC”.

- **P1 — Export counts are stale.** [README.md:52](/home/factory/collusion/collusion-beyond-words/README.md:52), [REPORT.md:19](/home/factory/collusion/collusion-beyond-words/REPORT.md:19), [REPORT.md:20](/home/factory/collusion/collusion-beyond-words/REPORT.md:20)  
  **Current → replacement:** “all 487 report text” → “all 491 report text”; “487/487 report text fragments” → “491/491 report text fragments”; “legacy checks (19 headings, 378 cells, 8 titles)” → “legacy checks (21 headings, 378 cells, 8 titles)”.  
  **Conflicting places:** [export_check.json:8](/home/factory/collusion/collusion-beyond-words/results/export_check.json:8) records **491** fragments; [line 6](/home/factory/collusion/collusion-beyond-words/results/export_check.json:6) records **21** headings. Parsing the current Markdown also yields 491 fragments.

- **P1 — README still says four reproduced figures.** [README.md:46](/home/factory/collusion/collusion-beyond-words/README.md:46), [README.md:63](/home/factory/collusion/collusion-beyond-words/README.md:63)  
  **Current:** “including all four figure scripts”; “All four regenerated figures (Fig. 1, 3, 4, 6) reproduce byte-identically.”  
  **Conflict:** [SUBMISSION.md:436](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:436) says “all six regenerated figures byte-identically”; the reproduction test lists all six scripts.  
  **Replace respectively:** “including all six figure scripts”; “All six regenerated figures (Fig. 1–6) reproduce byte-identically.”

- **P2 — Two prominently plotted auditor views remain undefined.** [SUBMISSION.md:166](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:166)  
  **Current:** “`combined_stats`, `structured`.”  
  **Replace:** “`combined_stats` (combined + pair-statistics table), `structured` (combined_stats + stated-vs-actual price table).”  
  These definitions appear in the frozen Q2.2 report, but readers of Figure 4 currently have to guess.

- **P2 — The labels table references the follow rule without defining it.** [SUBMISSION.md:144](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:144)  
  **Current:** “E84 follow rule on the locked test”  
  **Replace:** “E84 rule: both pair firms price ≥ the judged agreed floor − 1 in ≥ ½ of later rounds (locked test)”  
  This supplies the missing meaning of the repeatedly cited “14/50”.

- **P2 — Figure 5’s shaded uncertainty is unexplained.** [SUBMISSION.md:332](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:332)  
  **Current:** “Designated-pair premium per round:”  
  **Replace:** “Mean designated-pair premium per round (shading: pointwise 95% bootstrap CIs across runs):”  
  Neither the PNG nor its current caption identifies the bands; the rendering script does.

- **P3 — Rounding disclosure retains the already-corrected counting ambiguity.** [REPORT.md:34](/home/factory/collusion/collusion-beyond-words/REPORT.md:34)  
  **Current:** “five double-rounded values”  
  **Conflict:** [SUBMISSION.md:435](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:435) correctly says “Five claims (six numbers)”; E65 changes two numbers.  
  **Replace:** “five double-rounded claims (six numbers)”.
