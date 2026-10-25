# STATUS

## Current state (2026-10-25 08:45 UTC, merge iteration 1)
- Sources synced: Q1.4 `0e06c03`, Q2.2 `8b680ee` (both frozen since 07:30; check their "Changes after 08:00" logs each iteration).
- SUBMISSION.md v1: full paper (abstract bullets → refs → appendix with verbatim source tables A/B). Story: channel assignment (incl. its prompt cue) shows up as price *level*; no detected contemporaneous co-movement (pCMI at chance; lagged TE weakly above chance but below level and fires on shared policies); zero-shot auditor shows no resolved gain from public text (inverted for Qwen3.8, helps for luna executed games in E113); neither signal collusion-specific.
- Two adversarial reviews of v0 done and applied: Opus (25 items, `reviews/opus_v0.md`), codex gpt-6.1-sol (19 items, `reviews/codex_v0.md`).
- SOURCES.md: 49 rows, most ✔ against JSON (by me or by the Opus reviewer).
- figures/fig1–6 copied; captions checked against images.
- Next: (1) SUBMISSION.pdf via adapted Q1.4 `scripts/export_pdf.py` (markdown-it + playwright + pypdf); (2) SLIDES.md → SLIDES.pdf (≤ 8 slides); (3) final-claims review round 2 (codex + Opus) on v1 before 16:30; (4) re-check source "Changes after 08:00" logs.
- Risks: abstract still ~330 words (judges); appendix table B is long; Q1.4 judge labels have no cross-family check (stated).
- Not ours: `llm.py` had an uncommitted 78-line change at session start; it was swept into commit fbed25a by `git add -A`.

## Log
- 2026-10-25 08:05 UTC merge iter1: read PLAN/DIRECTION + both source REPORTs/STATUS; wrote SOURCES.md, SUBMISSION.md v0, REPORT.md pointer, figures fig1–6; spot-checked E70/E74/E44 mde JSON and Q2.2 claims table; launched codex + Opus adversarial reviews.
- 2026-10-25 08:45 UTC merge iter1: applied Opus review (P1: TE-only-above-chance false, board not in every Q1.4 arm, 'prices at chance' = LLM view not markup, Claude n 5+5, E133 framing; P2: level = assignment+cue, luna E113 gain +0.16 reported, inversion resolved only Qwen3.8, definitions box, label-check caveats, wording 2/5) and codex review (SALT construct, E72 n=52 composition, E133e comparator uses agreed price, soften 'nothing', prevalence scope, placebo not equivalence). SOURCES +13 rows.
