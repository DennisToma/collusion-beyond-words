# STATUS

## Current state (2026-10-25 ~09:00 UTC, merge iteration 2)
- Sources re-checked: Q1.4 `933de7a`, Q2.2 `22e71e9` — no research changes since freeze; both posted `merge_flags.md`. Applied both P1s (Q1.4 F1 "not a pure power failure" → injection-specific sensitivity; Q2.2 E133 post-hoc caveat) + P2s F3, 114-3; Fig.5 caption / abstract items were already applied.
- SUBMISSION.md v1.1 + **SUBMISSION.pdf** (15 pp incl. appendix) + **SLIDES.md/SLIDES.pdf** (8 slides) built by `scripts/export_pdf.py`; checks pass (18/18 headings, 378/378 table cells, 8/8 slide titles, no overflow). Fixed a broken appendix row (C12, unescaped `|`).
- Round-2 adversarial reviews of v1.1 (SUBMISSION + SLIDES) launched: codex gpt-6.1-sol → `/var/tmp/cbw/codex_v1.md` (copy to `reviews/codex_v1.md`), Opus subagent. If this iteration ends before they land, next iteration: re-run them (they are read-only) and apply.
- Next: (1) apply round-2 reviews, rebuild PDFs; (2) shorten abstract (~330 words) for judges; (3) re-check source merge_flags each iteration until 15:00; (4) finalize from 16:30.
- Risks: abstract length; main text ~10 pp + long appendix B; Q1.4 judge labels have no cross-family check (stated).

## Log
- 2026-10-25 08:05 UTC merge iter1: read PLAN/DIRECTION + both source REPORTs/STATUS; wrote SOURCES.md, SUBMISSION.md v0, REPORT.md pointer, figures fig1–6; spot-checked E70/E74/E44 mde JSON and Q2.2 claims table; launched codex + Opus adversarial reviews.
- 2026-10-25 08:45 UTC merge iter1: applied Opus review (P1: TE-only-above-chance false, board not in every Q1.4 arm, 'prices at chance' = LLM view not markup, Claude n 5+5, E133 framing; P2: level = assignment+cue, luna E113 gain +0.16 reported, inversion resolved only Qwen3.8, definitions box, label-check caveats, wording 2/5) and codex review (SALT construct, E72 n=52 composition, E133e comparator uses agreed price, soften 'nothing', prevalence scope, placebo not equivalence). SOURCES +13 rows.
- 2026-10-25 09:00 UTC merge iter2: applied source merge flags (Q1.4 F1/F3, Q2.2 114-4/114-3); added scripts/export_pdf.py (adapted from Q1.4), SLIDES.md, SUBMISSION.pdf, SLIDES.pdf; fixed appendix C12 table row; launched round-2 codex + Opus reviews.
