# Submission form

## Project title

Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

## Summary

Can an auditor detect a private channel between competing LLM sellers from prices, public messages, or both? We combine two sprint projects in separate simulated pricing markets. A simple price-level screen generally outperformed contemporaneous conditional-dependence detection, despite a successful scripted positive control. Adding public messages gave a zero-shot LLM auditor no resolved gain; some Qwen text views inverted the ranking. High prices also arose from an unread pricing notepad, prompt wording and memory with profit framing. We distinguish channel assignment, judged agreement and price-based execution, disclose limited test blindness, and retain the model-specific exceptions. The result supports matched price screens as possible audit triggers, with independent evidence needed for attribution. A two-stage audit remains an unevaluated proposal.

## Tracks to tick

- Track 1 — Markets and Collusion: Q1.4 (information-theoretic detection from prices).
- Track 2 — Detection and Audit: Q2.2 (what agents say versus what they do).

## Team and author

- Suggested team name: Beyond Words Lab.
- Author and affiliation: Dennis Toma — Independent.

## Files to upload

- `TEMPLATE_REPORT.pdf` — **primary report in the official Apart template** (≈ 4.5 pp main text; Figure 1 on page 1; from `TEMPLATE_REPORT.md` via `scripts/export_template_pdf.py`). Same numbers as SUBMISSION.
- `IMAGE.png` — project image for the form (1600×900; Figure 1 panel a; `scripts/fig0_headline.py`).
- `SUBMISSION.pdf` — extended report with all appendices (A–H) and per-number provenance; upload as supplementary material if the form permits, or keep in the repository.
- `SLIDES.pdf` — optional presentation supplement, if the form permits it.
- Code/evidence supplement, if permitted: create an archive of the final committed release with the README command. It includes the code, frozen evidence, provenance and reproduction instructions. Do not use the older `c1e7fdd` archive: its manuscript predates the compliance revision.
- Repository URL: `https://github.com/DennisToma/collusion-beyond-words`. Anonymous access failed in the recorded check; provide the archive or arrange reader access before relying on this URL for judging.

## Disclosures to retain

Autonomous AI research agents performed the implementation, experiments, analysis and drafting under Dennis's direction. Claude Opus managers, Codex reviewers/fallback managers and worker models are disclosed in Appendix H. The official sprint starter, adapted double-auction harness, external SALT-NLP data, literature resources and copied sprint-repo implementations are explicitly credited there and in README. Numbers are traceable to code and saved evidence within the documented reproduction scope.

## Before submitting

Run `uv run python scripts/finalize.py`. Its compliance receipt checks the abstract and form-summary lengths, main-text page limit, required ethics appendix, affiliation, references, PDF size and slide count. Upload the resulting PDFs and final code/evidence artifact. This file prepares the form; it does not submit it or grant repository access.
