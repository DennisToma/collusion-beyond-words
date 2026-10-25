# STATUS

## Current state (2026-10-25 ~09:45 UTC, merge iteration 3)
- Sources: Q1.4 `0124252` (0 open flags), Q2.2 `71a0365` (3 P1 wording flags → all applied this iteration: 121-2 slide-6 recommendation, 123-1 E113 "nowhere helped", 123-2 sol inversion now marked post hoc / "need not"). No research changes since freeze.
- Fig. 4 regenerated (`scripts/fig4_say_vs_do.py`, same Q2.2 JSON) with a correct x-axis label; caption updated. Slide 5 trimmed (all slides ≥ 11pt now).
- SOURCES: +M30 (sol 0.17 [0.01, 0.41]) and M31 (luna posting/silent), both checked against JSON.
- Deliverables: SUBMISSION.md v1.2 + SUBMISSION.pdf (15 pp) + SLIDES.pdf (8); export checks pass (18/18 headings, 378/378 cells, 8/8 slides).
- In flight: codex gpt-6.1-sol review of the v1.2 diff → `reviews/codex_v2.md` (apply next iteration if it finished).
- Next: (1) apply codex_v2; (2) re-check source flags until 15:00; (3) finalize 16:30 (one export pass), hard stop 18:00.
- Risks: abstract ~300 words (bullets; acceptable). Q1.4 judge labels lack cross-family check (stated). Never `pkill -f "codex exec"` broadly.

## Log
- 2026-10-25 09:45 UTC merge iter3: synced sources (Q1.4 0124252, Q2.2 71a0365); applied Q2.2 P1 flags 121-2, 123-1, 123-2; regenerated Fig. 4 with fixed axis label; trimmed slide 5; SOURCES M30/M31; rebuilt PDFs; launched codex_v2 review of v1.2 diff.
- 2026-10-25 08:05 UTC merge iter1: read PLAN/DIRECTION + both source REPORTs/STATUS; wrote SOURCES.md, SUBMISSION.md v0, REPORT.md pointer, figures fig1–6; spot-checked E70/E74/E44 mde JSON and Q2.2 claims table; launched codex + Opus adversarial reviews.
- 2026-10-25 08:45 UTC merge iter1: applied Opus review (P1: TE-only-above-chance false, board not in every Q1.4 arm, 'prices at chance' = LLM view not markup, Claude n 5+5, E133 framing; P2: level = assignment+cue, luna E113 gain +0.16 reported, inversion resolved only Qwen3.8, definitions box, label-check caveats, wording 2/5) and codex review (SALT construct, E72 n=52 composition, E133e comparator uses agreed price, soften 'nothing', prevalence scope, placebo not equivalence). SOURCES +13 rows.
- 2026-10-25 09:00 UTC merge iter2: applied source merge flags (Q1.4 F1/F3, Q2.2 114-4/114-3); added scripts/export_pdf.py (adapted from Q1.4), SLIDES.md, SUBMISSION.pdf, SLIDES.pdf; fixed appendix C12 table row; launched round-2 codex + Opus reviews.
- 2026-10-25 09:30 UTC merge iter2: applied Opus + codex round-2 reviews of v1.1 + slides, all items. Spot-checked the evidence for luna silent cells, sol inversion, info_exchange labels, late=11 window, E70 factor levels and the logbook control. Trimmed the abstract; rebuilt the PDFs.
