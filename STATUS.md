# STATUS

## Current state (2026-10-25 ~10:10 UTC, merge iteration 4)
- Sources: Q1.4 `499c500`, Q2.2 `badcd8d` — both 0 open flags; no research changes since the 07:30 freeze.
- Deliverables: SUBMISSION.md v1.3 + SUBMISSION.pdf (15 pp) + SLIDES.pdf (8); export checks pass (18/18 headings, 378/378 cells, 8/8 slides).
- Reviews done: codex v0/v1/v2 + Opus v0/v1/v2. Opus v2 (final claims, fresh): 0 P1; 3 P2 + 5 P3 wording applied (Qwen3.6 inversion in abstract, C − A defined, logbook control explained, mechanism hedged, TE recall 8–22%, SALT 62% scoped).
- Next: (1) re-check source flags each iteration until 15:00 (only apply P1s); (2) finalize 16:30 = one export pass + push; hard stop 18:00. No further content changes planned unless a source posts a P1.
- Risks: abstract ~300 words (bullets; acceptable). Q1.4 judge labels lack cross-family check (stated). Never `pkill -f "codex exec"` broadly.

## Log
- 2026-10-25 10:10 UTC merge iter4: Opus final-claims review (reviews/opus_v2.md): 0 P1, 3 P2 + 5 P3 wording — all applied after own JSON check; ~45 numbers independently re-verified. PDFs rebuilt (18/18, 378/378, 8/8; 15 pp).
- 2026-10-25 09:55 UTC merge iter4: synced Q1.4 `499c500` / Q2.2 `badcd8d` — both 0 open flags, both verified codex_v2 replacements correct; no science change. Repo 7 MB tracked (.venv ignored). Launched fresh Opus final-claims review (reviews/opus_v2.md).
- 2026-10-25 09:45 UTC merge iter3: synced sources (Q1.4 0124252, Q2.2 71a0365); applied Q2.2 P1 flags 121-2, 123-1, 123-2; regenerated Fig. 4 with fixed axis label; trimmed slide 5; SOURCES M30/M31; rebuilt PDFs; launched codex_v2 review of v1.2 diff.
- 2026-10-25 10:00 UTC merge iter3: applied codex_v2 (3 P1, 3 P2); scoped prevalence max (scripted rows; LLM ≤ 0.19, own JSON check); re-trimmed slide 5; PDFs rebuilt (checks pass).
- 2026-10-25 08:05 UTC merge iter1: read PLAN/DIRECTION + both source REPORTs/STATUS; wrote SOURCES.md, SUBMISSION.md v0, REPORT.md pointer, figures fig1–6; spot-checked E70/E74/E44 mde JSON and Q2.2 claims table; launched codex + Opus adversarial reviews.
- 2026-10-25 08:45 UTC merge iter1: applied Opus review (P1: TE-only-above-chance false, board not in every Q1.4 arm, 'prices at chance' = LLM view not markup, Claude n 5+5, E133 framing; P2: level = assignment+cue, luna E113 gain +0.16 reported, inversion resolved only Qwen3.8, definitions box, label-check caveats, wording 2/5) and codex review (SALT construct, E72 n=52 composition, E133e comparator uses agreed price, soften 'nothing', prevalence scope, placebo not equivalence). SOURCES +13 rows.
- 2026-10-25 09:00 UTC merge iter2: applied source merge flags (Q1.4 F1/F3, Q2.2 114-4/114-3); added scripts/export_pdf.py (adapted from Q1.4), SLIDES.md, SUBMISSION.pdf, SLIDES.pdf; fixed appendix C12 table row; launched round-2 codex + Opus reviews.
- 2026-10-25 09:30 UTC merge iter2: applied Opus + codex round-2 reviews of v1.1 + slides, all items. Spot-checked the evidence for luna silent cells, sol inversion, info_exchange labels, late=11 window, E70 factor levels and the logbook control. Trimmed the abstract; rebuilt the PDFs.
