# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

Apart Research AI Collusion Sprint (23–25 Oct 2026) — Dennis Toma.

**Read first:** [SUBMISSION.pdf](SUBMISSION.pdf) (17 pp; source [SUBMISSION.md](SUBMISSION.md)) and
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
| `evidence/` | 158 exact source files at pinned commits, compressed where applicable; full hashes and paths in `manifest.json` |
| `scripts/check_sources.py` | 111 saved-source assertions, 139 bindings that extract printed numbers from the report/slides, and 158 evidence-file hash checks (→ `results/source_check.json`) |
| `scripts/number_coverage.py` | lists every decimal in the report main text and slides and whether a binding checks it; fails if an unbound decimal is not a declared non-result (→ `results/number_coverage.json`; 222/260 and 55/61, 0 unclassified) |
| `scripts/recompute_unrounded_q22.py` | replays 3 Q2.2 rounding corrections from pinned inputs with the source estimators/seeds → `results/unrounded_q22.json`; no sibling checkout needed |
| `scripts/recompute_c21b_floor.py` | replays C21b with two agreed-floor thresholds and two descriptive windows from pinned trajectories/cached terms → `results/c21b_floor.json`; no sibling checkout needed |
| `scripts/recompute_locked_test_q22.py` | replays the historical 95-run locked test from cached judge labels and six original LLM score views; eight run-AUROC contrasts match the saved B=2000 analysis, with no fitting or calls → `results/locked_test_q22.json` |
| `scripts/recompute_grid_q14.py` | rebuilds all 768 observed E70 run scores from 192 archived Q1.4 games, plus the frozen cell-by-arm bootstrap and paired level contrasts → `results/grid_q14.json`; no null draws or labels |
| `scripts/recompute_gate_q14.py` | reaggregates the scripted gate from 27,000 archived score/p-value rows (500 games, nine detectors): flags, Wilson intervals, localisation and AUROCs → `results/gate_q14.json`; no null draws or markets generated |
| `scripts/recompute_gate_pcmi_q14.py` | reconstructs the scripted gate’s pCMI scores and original B=200 shift-null draws from archived trajectories; all 3000 scores/pair p-values and 500 run p-values match → `results/gate_pcmi_q14.json` |
| `scripts/process_log_summary.py` | counts autonomous manager iterations per repo/backend from the machine-local runner logs for the LLM usage statement, with a snapshot timestamp (→ `results/process_log_summary.json`; not regenerable without those logs) |
| `tests/test_reproduction.py` | 26 checks: independent-copy reproduction, figure and replay parity, original-function parity for the Q1.4 grid and gate, C21b and the locked test, malformed trajectory/audit rejection, LLM-usage counts, and rejection of deliberately bad claims/evidence (→ `results/reproduction_check.json`) |
| `scripts/export_pdf.py` | builds both PDFs; checks text fragments, per-slide placement, figure pixels and portable links; fits slide text at ≥14 pt |
| `tests/test_export.py` | rejects missing prose, wrong-page text, missing/substituted figures, broken/local-file links and slide overflow; checks the font floor |
| `reviews/` | adversarial claim reviews (codex gpt-6.1-sol, Opus), presentation review, and a primary-literature/construct audit; dispositions recorded |
| `EXPERIMENTS.tsv`, `STATUS.md` | ledger of merge passes and iteration log |

## Reproduce this submission (no sibling repos or model credentials needed)

```bash
uv run python scripts/check_sources.py          # 111 source checks, 139 document bindings, 158 evidence hashes
uv run python scripts/number_coverage.py        # which printed decimals are machine-checked
uv run python scripts/recompute_unrounded_q22.py # exact saved rounding-correction replay
uv run python scripts/recompute_c21b_floor.py    # C21b floor/window sensitivity replay
uv run python scripts/recompute_locked_test_q22.py # historical locked-test run-AUROC replay
uv run python scripts/recompute_grid_q14.py      # observed E70 scores from raw frozen trajectories
uv run python scripts/recompute_gate_pcmi_q14.py # historical pCMI scores and shift-null replay
uv run python scripts/recompute_gate_q14.py      # scripted gate from archived scores/run p-values
uv run python scripts/fig1_hard_negatives.py     # byte-identical figures/fig1_*.png
uv run python scripts/fig2_level_vs_comovement.py # byte-identical figures/fig2_*.png
uv run python scripts/fig3_e70_grid.py           # byte-identical figures/fig3_*.png
uv run python scripts/fig4_say_vs_do.py          # byte-identical figures/fig4_*.png
uv run python scripts/fig5_placebo_premium.py    # byte-identical figures/fig5_*.png
uv run python scripts/fig6_strong_framing.py     # byte-identical figures/fig6_*.png
uv run python tests/test_reproduction.py        # standalone + bad-input checks, including all six figure scripts
uv run --group export playwright install chromium   # once
uv run --group export python scripts/export_pdf.py  # SUBMISSION.pdf + SLIDES.pdf
uv run --group export python tests/test_export.py   # deliberate export failure checks
uv run python scripts/finalize.py              # author machine only (reads runner logs): refresh LLM-usage counts, then all checks + export
```

Latest distribution check: a fresh GitHub clone of `731de19` with a new locked virtualenv and
Chromium download passed the scientific replay, figure, document and export commands available
at that revision, including both test suites. All five replay outputs and all six figures were deleted and
rebuilt byte-identically; both PDFs match apart from date metadata. See the
[receipt](results/distribution_check.json) and [procedure](reviews/distribution_i29.md).
This used the same VM with nonexistent sibling-root overrides; it does not establish
portability to a different operating system. The author-only log refresh was excluded. The pCMI shift-null replay added in iteration 30 is
covered by the current independent-copy checks, not that historical remote-clone receipt.

The export receipt is [results/export_check.json](results/export_check.json): all 492 report text
fragments and 55 slide text fragments are present (the latter on the correct slide), all 10 embedded
figures match the source pixels, and PDF links use public URLs. Slide body, table and code text is at
least 14 pt; Fig. 1 and 3 were re-rendered with larger chart text in iteration 12, but dense raster chart labels can still be smaller and are best inspected in the report or PNGs.
These checks establish text presence and the specified layout constraints, not scientific validity.
`results/export_test.json` records the 9 export failure checks.

The checker compares selected printed numeric claims with saved source values using half-up rounding;
it fails if a bound context disappears. It does **not** check every number or certify the meaning of
the prose; the adversarial reviews and [SOURCES.md](SOURCES.md) cover the wider claims.

The release checks run in an independent copy with source paths set to nonexistent directories. All six
regenerated figures (Fig. 1–6) and all three Q2.2 replay outputs reproduce byte-identically after deleting the
outputs. C21b's per-run fields also match the pinned original `p2_strong.analyse` in all eight settings;
strict execution uses all post-agreement rounds, independently of the descriptive late window.
The locked-test replay uses exactly IDs 0030–0124 (50 communication-positive, 45 negative), with the
original paired class-stratified bootstrap and better-single-view selection inside every resample.
It reproduces all six run-AUROC estimates/CIs and eight contrasts, including the primary
−0.0127 [−0.0913, +0.0642], exactly at the source's saved precision. It reuses the frozen judge labels;
this is reproduction of the historical result, not another held-out evaluation. The parity test executes
only original pure analysis functions, using an independent rank-sum AUROC calculation, on the real
cohort and a tied calculator fixture. Pair/localisation endpoints, fusion and thresholds are outside this replay.
The Q1.4 grid replay independently rebuilds 768 run scores from archived trajectories: all match
exactly, as do the four pooled AUROC/CI triples, both paired level contrasts, markup contrast and
per-cell AUROCs at the saved precision. All six pair scores per game and the full B=2000 bootstrap
match pinned original functions; malformed completed trajectories are rejected. Its output also
regenerates byte-identically without source checkouts. Null calibration, permutation flags and
executed labels are outside this replay; it is verification of saved evidence, with no new evaluation.
The scripted gate replay reaggregates all nine detectors from archived pair scores and max-statistic run
p-values for 500 markets. All 666 saved summary values reproduce (largest float difference 1.1e-16);
flag rates, Wilson intervals and localisation rates match exactly. It checks both null summaries, including
leave-one-out same-shock-family surrogate ranking. It does not regenerate scores, trajectories or shift-null
draws, or validate the synthetic ground truth. Three release checks add byte parity, original-function
parity (including alpha-boundary and near-tie calculator fixtures) and malformed-cache rejection.
A separate pCMI replay starts from archived gate trajectories and reconstructs the original 200
shift draws per run. All 3000 observed pair scores, 3000 pair p-values and 500 max-statistic
run p-values match exactly. Tests compare the unmodified full original scorer on ten group
representatives and constant/short-draw fixtures; malformed trajectories and wrong cached
p-values are rejected. This extends the gate aggregation check to pCMI's historical null;
other detector nulls, simulation and label correctness remain outside the replay.
The bundle pins Q1.4 `732f08c` and Q2.2 `91ffb2d`; see
[evidence/README.md](evidence/README.md) for its scope and rebuilding it from the exact git commits.
`uv run python scripts/check_sources.py --live` instead checks files in sibling clones under `~/collusion/`
(override with `BW_Q14_ROOT` / `BW_Q22_ROOT`). Use checkouts at the pinned commits: even later
review-only edits to a bundled REPORT.md fail this deliberately strict hash check. The default bundle
check remains stable when source metadata changes.

Re-running the **underlying experiments** requires the source repos and their datasets/caches: Q1.4 REPORT
§6 and Q2.2 REPORT Appendix E (`verify_phase2.py` re-runs 31/31 commands from cache with 0 LLM calls).
