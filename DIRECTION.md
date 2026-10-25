# DIRECTION — APART TEMPLATE + JUDGE READABILITY (set by Dennis 16:40 UTC) — OVERRIDES the freeze hold. Top priority.
Judges score the written report (Evaluation Rubric) in ~10–20 min each. Our science is strong; our prose is too dense.
Official template text (structure + guidance): `/var/tmp/template_structure.txt` — follow it exactly.

Produce **`TEMPLATE_REPORT.md`** (+ `TEMPLATE_REPORT.pdf` via the existing exporter) that maps 1:1 onto the template:
Title · Authors (Dennis Toma — Independent; "With Apart Research") · Abstract (150–250 words) · 1. Introduction (problem,
why it matters, threat model, **numbered "Our main contributions are:" list**, 3 items) · 2. Related Work · 3. Methods ·
4. Results (numbered Figures/Tables with self-contained captions, ≥ 1 figure) · 5. Discussion and Limitations (with
Limitations + Future Work subsections) · 6. Conclusion · Code and Data (links) · Author Contributions · References
(Author, Year, Title, Venue, URL/DOI) · Appendix (incl. **Limitations and Dual-Use / Ethical Considerations**, extended
tables, prompts) · **LLM Usage Statement** (honest: autonomous Claude Opus 5.5 / Codex gpt-6.1-sol agents ran experiments
and drafted under Dennis's direction; all numbers regenerate from code; Dennis reviewed the final claims).
Footnote on the title: "Research conducted at the AI Collusion Research Sprint, October 2026".

**Readability rules (the four judge risks):**
1. **Page 1 must land in 2 minutes.** Abstract in plain language, then **Figure 1 on page 1/2**: a two-panel figure —
   (a) one real channel game vs one real no-channel game (price per round, pair vs rivals), (b) AUROC bars level vs pCMI
   vs text across the main sets. Caption states the headline in one sentence.
2. **Recommended length ~4 pages main text** (hard max 8) excluding references/appendix: Intro+Related ≈1p,
   Methods+Results ≈2.5p, Discussion ≈0.5p. Move everything else to the appendix.
3. **Main text has no experiment IDs (E44, P2.8 …), no repo jargon, few CIs** — at most one bracketed CI per key number;
   other CIs go to appendix tables. Define AUROC once in words. Short sentences. Hedging only where it changes meaning.
4. **Frame the negative results as positive contributions** (confident, not defensive): (i) a validated
   information-theoretic detector + a map of exactly when it fails; (ii) evidence that LLM price collusion is a *level*, not
   co-movement or words, across 9 sets / 7 models / a 192-game grid; (iii) a sharp boundary: text auditing works when the
   collusive act is verbal (SALT 0.87) and fails when it is a price; (iv) a warning for benchmarks: channel ≠ collusion
   (prompt cue ≈ 2/3, tacit high pricing); removing safety training does not increase it. End with a concrete
   recommendation for deployers (cheap model-matched level screen → escalate to chat/LLM audit).
5. Keep every number identical to the frozen sources (no new analysis); keep SOURCES mapping and run the existing checks.
6. Also produce `IMAGE.png` (project image for the form: the Figure 1 panel (a), 1600×900, legible) and update
   `SLIDES.pdf` to ≤ 8 slides in the same plain style (slide 1 = headline + Figure 1).
7. Adversarial review by an Opus subagent focused on: does page 1 land for a non-specialist judge; any overclaim; template
   compliance. Apply, rebuild, commit, push. Deadline 18:30 UTC (extend the hard stop to 19:00 UTC for this repo only).

# DIRECTION — SUBMISSION COMPLIANCE (set by Dennis 13:35 UTC) — OVERRIDES the freeze hold. Top priority.
Apart's official rules (sprint page Guidelines) that the current SUBMISSION violates:
1. **Main text ≤ 8 pages**, not counting references and appendices (strong projects 4–8). Current main text ≈ 10 pp → cut.
   Move detail (extra tables, robustness rows, per-family breakdowns) to appendices; keep the positive control in main text.
2. **Abstract 150–250 words** (current ≈ 330+). Rewrite to ≤ 250 words; the glossary moves out of the abstract (put it in §3 or an appendix).
3. **Author names and affiliations**: "Dennis Toma — Independent" (Dennis will edit if needed).
4. **Required appendix "Limitations and Dual-Use / Ethical Considerations"**: what the result does and doesn't show; whether
   this work could make real collusion easier to carry out or harder to detect (e.g., it documents that price-level screens are
   model/prompt dependent and that text audits miss price-only coordination — say how a defender should use that; no new attack
   capability: agents were never instructed to collude; abliterated models were used only as sellers in a sandbox). Merge the
   existing Limitations section into it or keep §7 short and put the full version in the appendix.
5. **Recommended structure**: Introduction, Related Work, Methodology (models, prompts, environments, seeds, metrics), Results,
   Discussion, Limitations/Ethics appendix, References. Report variance/seeds/baselines; include the positive control.
6. **Disclosures**: (a) AI-assistance statement (the project was run by autonomous AI research agents — Claude Opus 5.5 managers,
   Codex gpt-6.1-sol reviewers/fallback, worker models — under Dennis's direction; all numbers regenerate from code in the repos);
   (b) pre-existing code: the official starter repo (poseidon-research/collusion_hackathon: double auction, trust-breaking,
   literature) and any adapted code are labelled as pre-existing in README and report; everything else was written during the sprint.
7. **References**: every reference must be real and correctly cited — run one check: each entry has authors, year, title, venue/arXiv
   id that you can verify from the sources' cited files or the starter `literature/` list. Remove anything you cannot verify.
   Fabricated references are a disqualification risk.
8. Keep all numbers identical (no new analysis). Rebuild SUBMISSION.pdf (≤ 25 MB) + SLIDES.pdf with finalize.py; run the source
   checks; adversarial review (Opus subagent) of ONLY the new abstract + ethics appendix + cuts; commit + push.
9. Also write `SUBMISSION_FORM.md`: project title (unique), a ≤ 150-word summary for the form, tracks to tick
   (Track 1 Markets and Collusion: Q1.4; Track 2 Detection and Audit: Q2.2), team name suggestion, and the list of files to upload.
Deadline for this: 17:30 UTC (hard stop 18:00 unchanged).

# DIRECTION

Start with PLAN.md: sync both source repos, draft SUBMISSION.md skeleton with current numbers, then iterate as Phase 2 results land (sources stop experiments at Sun 15:00 UTC).
