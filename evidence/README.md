# Pinned source evidence

This bundle makes the merged submission's saved-value checks and Fig. 1/3/4/6 rendering independent of
the source checkouts. It contains 74 exact git blobs from:

- [Q1.4 @ 732f08c11a765cd8500f4ef3c29fb630b309d5b2](https://github.com/DennisToma/collusion-14-infotheory/tree/732f08c11a765cd8500f4ef3c29fb630b309d5b2)
- [Q2.2 @ 91ffb2d4737a7537cdf9afe239a98e0d1061090b](https://github.com/DennisToma/collusion-22-say-vs-do/tree/91ffb2d4737a7537cdf9afe239a98e0d1061090b)

`manifest.json` records each original path, full source commit, uncompressed size and SHA256, storage
path, compression, and stored SHA256. JSON/JSONL files use deterministic gzip (`mtime=0`); decompression
returns the original bytes. Reports, split declarations and a few setup/label definitions accompany
the saved JSON. The strong-framing trajectories are included because Fig. 6 reads them. The file list
includes the explicit JSON paths cited in the provenance/report tables and the two renderers' inputs.

Run from the repo root:

```bash
uv run python scripts/check_sources.py
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
All six figures can be regenerated from this bundle (Fig. 1/2/3/5 re-rendered with larger text only; Fig. 5 reads the pinned Q2.2 `llm_v3plc`/`llm_v3rep` ground truth + trajectories and asserts its per-round means equal the saved `placebo_llm_v3plc.json`). The reports retained
here preserve their original source-relative paths.
