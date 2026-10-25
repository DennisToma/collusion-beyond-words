# Pinned source evidence

This bundle makes the merged submission's saved-value checks, all six figures and the Q2.2 rounding,
C21b sensitivity, historical locked-test and Q1.4 raw-grid replays independent of the source checkouts. It contains
146 exact git blobs from:

- [Q1.4 @ 732f08c11a765cd8500f4ef3c29fb630b309d5b2](https://github.com/DennisToma/collusion-14-infotheory/tree/732f08c11a765cd8500f4ef3c29fb630b309d5b2)
- [Q2.2 @ 91ffb2d4737a7537cdf9afe239a98e0d1061090b](https://github.com/DennisToma/collusion-22-say-vs-do/tree/91ffb2d4737a7537cdf9afe239a98e0d1061090b)

`manifest.json` records each original path, full source commit, uncompressed size and SHA256, storage
path, compression, and stored SHA256. JSON/JSONL files use deterministic gzip (`mtime=0`); decompression
returns the original bytes. Reports, split declarations and a few setup/label definitions accompany
the saved JSON. The strong-framing trajectories are included because Fig. 6 reads them. The file list
includes the explicit JSON paths cited in the provenance/report tables and all six renderers' inputs.
Iteration 24 added 22 blobs: the Q2.2 replays' raw inputs, cached audit scores/terms, grid snapshot and
original estimator/label code. The previous 76 blobs and both commit pins are unchanged. Iteration 25 adds nine more exact
Q2.2 blobs: `final_analysis.py`, `analyze_llm.py`, `llm_v3` labels and all six original LLM view
audit caches. All earlier 98 entries remain unchanged. The locked-test replay checks the six
run-AUROC estimates/CIs and eight contrasts against saved results, using exactly IDs 0030–0124
and the original seed-0, B=2000 paired class-stratified bootstrap. It reuses the frozen judge
labels; it does not re-audit, fit thresholds/fusion, compute pair endpoints, or create a new test evaluation.

Iteration 26 adds 39 exact Q1.4 blobs (146 total; previous 107 unchanged): sixteen cell
ground-truth/trajectory pairs, the original grid manifest and six original source files.
The raw-grid replay rebuilds 768 observed run scores for 192 games, then reproduces the
four pooled AUROC/CI triples, two paired level contrasts, markup contrast and per-cell AUROCs
with the original cell-by-arm bootstrap. Tests compare the loader, all 4608 per-pair scores
and full B=2000 bootstrap against original source functions. No null draws, flags or
judge/executed-label validation; no simulation or new evaluation.

Run from the repo root:

```bash
uv run python scripts/check_sources.py
uv run python scripts/recompute_unrounded_q22.py
uv run python scripts/recompute_c21b_floor.py
uv run python scripts/recompute_locked_test_q22.py
uv run python scripts/recompute_grid_q14.py
uv run python tests/test_reproduction.py
```

The checker verifies all bundle-file hashes. Its source assertions compare saved JSON values with
frozen expected values; separate document bindings extract selected report/slide numbers and compare
them with those same source values at each binding's declared rounding precision; reducing the printed
precision cannot widen tolerance. The bindings live in `results/document_bindings.json`. Changing
their surrounding wording requires updating the bindings and reviewing the new scope. Unbound
numbers and qualitative claims still require review.

`check_sources.py --live` checks all these files in source working trees instead. Those trees must
match the pinned commits, including REPORT.md: a later review-only report edit fails the strict hash
check even if every scientific input is unchanged. Use the default bundle for a stable release check.

To reconstruct the bundle, clone both source repos under `~/collusion/` (or set `BW_Q14_ROOT` and
`BW_Q22_ROOT`), ensure the pinned commits exist locally, then run:

```bash
uv run python scripts/snapshot_evidence.py
```

This reads `git show <full-commit>:<path>` and writes only this repo. The source working tree and any
later commits do not affect the snapshot. It refuses a pinned-blob hash mismatch. No network access,
model calls, new metrics, refitting or experiment runs are involved.

The bundle supports **checking saved results**, not rebuilding every experimental result from raw
trajectories. Full generators, caches, labels and registration history remain in the source repos.
The Q1.4 grid and all three Q2.2 replays reproduce their committed outputs byte-identically, and the release tests compare
C21b's per-run fields with the original pinned source function in all eight floor/window settings.
Source modules are retained for inspection; the replay scripts never import their model-calling
terms loader. All six figures can be regenerated from this bundle (Fig. 1/2/3/5 re-rendered with larger text only; Fig. 5 reads the pinned Q2.2 `llm_v3plc`/`llm_v3rep` ground truth + trajectories and asserts its per-round means equal the saved `placebo_llm_v3plc.json`). The reports retained
here preserve their original source-relative paths.
