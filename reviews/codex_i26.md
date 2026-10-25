# Iteration 26 — independent raw-grid replay review

Reviewed 2026-10-25 12:38 UTC; gpt-6.1-sol, reasoning effort high, read-only Codex CLI.
Scope: pending changes against merge HEAD `979d17c`; no source-repo writes, experiments or auditor calls.

No actionable P1/P2 findings in the iteration26 diff.

Independently verified:

- All 146 bundled blobs match `git show` at their pins; all prior 107 manifest entries and stored blobs match HEAD.
- The cohort contains 192 games and 3,840 rounds.
- All 4,608 pair values and 768 run scores match exactly, including state/lag residualization, TE direction, level maxima and ties.
- The original seed-0, B=2000 cell-by-arm draw order reproduces all pooled AUROC/CI triples, markup results, per-cell AUROCs and paired contrasts.
- The in-memory replay produces byte-identical `grid_q14.json`.
- Original-function parity and malformed-input test bodies pass. Their reference functions are independent; the rejection tests do not mask replay errors.
- The reproducibility prose stays within the saved-evidence scope.

I made no file changes or commits and ran no experiments or model calls.