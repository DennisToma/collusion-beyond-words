# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

Apart Research AI Collusion Sprint (23–25 Oct 2026) — Dennis Toma.

**Read first:** [SUBMISSION.pdf](SUBMISSION.pdf) (16 pp; source [SUBMISSION.md](SUBMISSION.md)) and
[SLIDES.pdf](SLIDES.pdf) (8 slides). One-line result: in our LLM pricing markets a private chat channel
shows up mainly as *higher prices*; we find no robust contemporaneous price co-movement, public messages give a
zero-shot LLM auditor no resolved gain, and high prices also arise without any channel — so a price flag
is a reason to audit, not evidence of an agreement.

This repo merges two sprint projects and runs **no new experiments**:

| project | repo (code, data, per-claim JSON) |
|---|---|
| Q1.4 prices-only (information-theoretic detection) | [collusion-14-infotheory](https://github.com/DennisToma/collusion-14-infotheory) |
| Q2.2 say-vs-do (text + action auditing) | [collusion-22-say-vs-do](https://github.com/DennisToma/collusion-22-say-vs-do) |

## What is here

| path | content |
|---|---|
| `SUBMISSION.md/.pdf` | the report (abstract, setup, methods, results with CIs, limitations, appendix tables) |
| `SLIDES.md/.pdf` | short presentation |
| `SOURCES.md` | every number in the report → source repo, JSON file/key, commit |
| `figures/` | Fig. 1–6; Fig. 1, 2 and 3 re-rendered from pinned Q1.4 JSON by `scripts/fig1_hard_negatives.py`, `scripts/fig2_level_vs_comovement.py`, `scripts/fig3_e70_grid.py`, Fig. 5 from pinned Q2.2 trajectories by `scripts/fig5_placebo_premium.py` (larger text only; same data and encodings), Fig. 4 and 6 by `scripts/fig4_say_vs_do.py`, `scripts/fig6_strong_framing.py` (label fixes) |
| `evidence/` | 76 exact source files at pinned commits, compressed where applicable; full hashes and paths in `manifest.json` |
| `scripts/check_sources.py` | 111 saved-source assertions, 139 bindings that extract printed numbers from the report/slides, and 76 evidence-file hash checks (→ `results/source_check.json`) |
| `scripts/number_coverage.py` | lists every decimal in the report main text and slides and whether a binding checks it (→ `results/number_coverage.json`; 222/260 and 55/61) |
| `scripts/recompute_unrounded_q22.py` | recomputes 3 Q2.2 values saved as 3-dp ties with Q2.2's own code (needs the Q2.2 checkout; run with its `.venv/bin/python`) → `results/unrounded_q22.json`, which `check_sources.py` checks against the pinned values |
| `scripts/process_log_summary.py` | counts autonomous manager iterations per repo/backend from the machine-local runner logs for the LLM usage statement (→ `results/process_log_summary.json`; not regenerable without those logs) |
| `tests/test_reproduction.py` | 9 checks: independent-copy reproduction, figure parity, and rejection of deliberately bad claims/evidence (→ `results/reproduction_check.json`) |
| `scripts/export_pdf.py` | builds both PDFs; checks text fragments, per-slide placement, figure pixels and portable links; fits slide text at ≥14 pt |
| `tests/test_export.py` | rejects missing prose, wrong-page text, missing/substituted figures, broken/local-file links and slide overflow; checks the font floor |
| `reviews/` | adversarial claim reviews (codex gpt-6.1-sol, Opus), presentation review, and a primary-literature/construct audit; dispositions recorded |
| `EXPERIMENTS.tsv`, `STATUS.md` | ledger of merge passes and iteration log |

## Reproduce this submission (no sibling repos or model credentials needed)

```bash
uv run python scripts/check_sources.py          # 111 source checks, 139 document bindings, 76 evidence hashes
uv run python scripts/number_coverage.py        # which printed decimals are machine-checked
uv run python scripts/fig1_hard_negatives.py     # byte-identical figures/fig1_*.png
uv run python scripts/fig3_e70_grid.py           # byte-identical figures/fig3_*.png
uv run python scripts/fig4_say_vs_do.py          # byte-identical figures/fig4_*.png
uv run python scripts/fig6_strong_framing.py     # byte-identical figures/fig6_*.png
uv run python tests/test_reproduction.py        # standalone + bad-input checks, including all four figure scripts
uv run --group export playwright install chromium   # once
uv run --group export python scripts/export_pdf.py  # SUBMISSION.pdf + SLIDES.pdf
uv run --group export python tests/test_export.py   # deliberate export failure checks
```

The export receipt is [results/export_check.json](results/export_check.json): all 487 report text
fragments and 55 slide text fragments are present (the latter on the correct slide), all 10 embedded
figures match the source pixels, and PDF links use public URLs. Slide body, table and code text is at
least 14 pt; Fig. 1 and 3 were re-rendered with larger chart text in iteration 12, but dense raster chart labels can still be smaller and are best inspected in the report or PNGs.
These checks establish text presence and the specified layout constraints, not scientific validity.
`results/export_test.json` records the 9 export failure checks.

The checker compares selected printed numeric claims with saved source values using half-up rounding;
it fails if a bound context disappears. It does **not** check every number or certify the meaning of
the prose; the adversarial reviews and [SOURCES.md](SOURCES.md) cover the wider claims.

The release checks run in an independent copy with source paths set to nonexistent directories. All four
regenerated figures (Fig. 1, 3, 4, 6) reproduce byte-identically. The bundle pins Q1.4 `732f08c` and Q2.2 `91ffb2d`; see
[evidence/README.md](evidence/README.md) for its scope and rebuilding it from the exact git commits.
`uv run python scripts/check_sources.py --live` instead checks files in sibling clones under `~/collusion/`
(override with `BW_Q14_ROOT` / `BW_Q22_ROOT`). Use checkouts at the pinned commits: even later
review-only edits to a bundled REPORT.md fail this deliberately strict hash check. The default bundle
check remains stable when source metadata changes.

Re-running the **underlying experiments** requires the source repos and their datasets/caches: Q1.4 REPORT
§6 and Q2.2 REPORT Appendix E (`verify_phase2.py` re-runs 31/31 commands from cache with 0 LLM calls).
