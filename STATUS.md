# STATUS

## Current state (2026-10-25 ~09:30 UTC, merge iteration 2)
- Sources re-checked: Q1.4 `933de7a`, Q2.2 `22e71e9`. Neither has research changes since the freeze. Applied the P1s from their `merge_flags.md` (Q1.4 F1, Q2.2 114-4) and the P2s.
- **Round-2 adversarial reviews done and applied.** `reviews/opus_v1.md`: 0 numeric mismatches in ~60 checks, 2 P1 + 11 P2. `reviews/codex_v1.md`: 7 P1 + 9 P2; it overlaps with Opus on the luna-text and slide-conclusion items.
  Main changes: the E113 luna gain is no longer credited to text (silent cells +0.12). Q2.2 labels are *communication* labels (48 explicit + 2 info-exchange). Tacit-high window = rounds 11–40. The evasion claim is removed. The positive control is scoped. The glossary sits under the abstract and defines "executed". The sol seller arm is also inverted.
- Deliverables: SUBMISSION.md v1.2 + **SUBMISSION.pdf** (15 pp incl. appendix) and **SLIDES.md/SLIDES.pdf** (8 slides). Both are built by `scripts/export_pdf.py`, which runs checks (18/18 headings, 378/378 table cells, 8/8 slides, no overflow).
- Next: (1) re-check source `merge_flags.md` and "Changes after 08:00" each iteration until 15:00; (2) cheap final-claims codex review of the v1.2 diff before 16:30; (3) slide 6 auto-shrinks to 10.5pt, so trim its text; (4) finalize from 16:30.
- Risks: abstract still ~300 words. Fig. 4's axis label is corrected only in the caption. Q1.4 judge labels have no cross-family check (stated in the paper).
- Caution: other projects' codex managers run on this VM, so never `pkill -f "codex exec"` broadly.

## Log
- 2026-10-25 08:05 UTC merge iter1: read PLAN/DIRECTION + both source REPORTs/STATUS; wrote SOURCES.md, SUBMISSION.md v0, REPORT.md pointer, figures fig1–6; spot-checked E70/E74/E44 mde JSON and Q2.2 claims table; launched codex + Opus adversarial reviews.
- 2026-10-25 08:45 UTC merge iter1: applied Opus review (P1: TE-only-above-chance false, board not in every Q1.4 arm, 'prices at chance' = LLM view not markup, Claude n 5+5, E133 framing; P2: level = assignment+cue, luna E113 gain +0.16 reported, inversion resolved only Qwen3.8, definitions box, label-check caveats, wording 2/5) and codex review (SALT construct, E72 n=52 composition, E133e comparator uses agreed price, soften 'nothing', prevalence scope, placebo not equivalence). SOURCES +13 rows.
- 2026-10-25 09:00 UTC merge iter2: applied source merge flags (Q1.4 F1/F3, Q2.2 114-4/114-3); added scripts/export_pdf.py (adapted from Q1.4), SLIDES.md, SUBMISSION.pdf, SLIDES.pdf; fixed appendix C12 table row; launched round-2 codex + Opus reviews.
- 2026-10-25 09:30 UTC merge iter2: applied Opus + codex round-2 reviews of v1.1 + slides, all items. Spot-checked the evidence for luna silent cells, sol inversion, info_exchange labels, late=11 window, E70 factor levels and the logbook control. Trimmed the abstract; rebuilt the PDFs.
