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
