# Iteration 40 — full source reconciliation before the experiment cutoff

Checked 2026-10-25 14:58 UTC, before the scheduled 15:00 experiment cutoff.
Both source managers already declare their research final. This check records
that state; it does not claim that the clock has reached the cutoff.

Source revisions: Q1.4 `e8cf411460358ab14ffdb4769ada846406fd9497`;
Q2.2 `5a012a0bba87dbfbd5bbbfcb16c810ab91483bc9`.
Evidence pins remain `732f08c` / `91ffb2d`.
[Receipt](../results/source_freeze_i40.json), [recorded driver](source_freeze_i40_driver.py).

## Executed checks and findings

```bash
uv run python reviews/source_freeze_i40_driver.py
uv run python scripts/check_sources.py
uv run python scripts/number_coverage.py
uv run --group export python scripts/check_committed_export.py
```

- Q1.4: 552 tracked files at both revisions; 544 unchanged tree entries. The eight
  changed paths are director/status/review metadata, two merge-verification ledger
  rows and render-only HTML/PDF exports. REPORT.md and all scientific code, inputs,
  datasets, saved estimates and splits are unchanged.
- Q2.2: 1392 tracked files at both revisions; 1380 unchanged tree entries. Twelve
  changed paths are fully enumerated with old/new SHA256 hashes in the receipt.
  Its only renderer-code change replaces “2nd half” with “rounds 11–40” in a label;
  the corresponding PNG and exports were refreshed. The report adds exactly one
  I133 review-log line. The ledger, analysis code, datasets, labels, auditor caches,
  saved estimates and splits are unchanged. The refreshed reproduction receipt
  retains identical commands and output comparisons after removing timestamps,
  revision, input-hash inventory and elapsed times.
- All bundled source Git blobs match their pinned manifest hashes: 81 Q1.4 and
  77 Q2.2. Live source files also match the captured HEAD blobs. The only live-vs-pin
  drift is Q2.2 REPORT.md's single review line (76/77 match); Q1.4 matches 81/81.
- Both source worktrees were clean and their HEADs remained fixed through the
  successful check. Two earlier attempts rejected concurrent Q2.2 HEAD advances;
  both were inspected and added STATUS lines only. No source files were written.
- The merge's 179 protected manuscript/PDF/form/figure/evidence/replay/usage/lock
  files match `a924419` byte-for-byte. Independent `git diff --name-only` checks
  reproduce both source change lists; an independent merge `git diff --exit-code`
  confirms preservation.
- An in-memory added scientific-result path is rejected before receipt publication;
  the prior successful receipt remains unchanged. No source fixture was written.
- Current merged checks pass: 111 source assertions, 144 document bindings, 158
  evidence hashes; zero unclassified decimals; committed PDF text, slide placement,
  ten figure embeddings and portable-link checks. No PDF rebuild or usage refresh.
  The existing 47-test acceptance at `c3d2903` is historical, not rerun here.

## Honest diagnostic and scope

Q1.4's saved `merge_check.json` has zero JSON mismatches **and two quote misses**,
both expecting the source's double-rounded grid CI upper bound 0.81. The merged
replay gives 0.80, verified and disclosed since iterations 17/18 and confirmed by
Q1.4 I130/I146. This is not an all-green quote check. The current merged checker
passes against the unrounded replay. Q1.4 I152 and Q2.2 I160 independently cover
the current SUBMISSION SHA256 `96d0ed7b816d3b6217fcd5a006214515b9fd0f74dfba7229148a99b180b9327b`
with no open P1; this source inventory does not replace their scope judgment.

This is a provenance comparison, not a new scientific analysis, experiment,
held-out evaluation, source export, independent review or access check. Ignored
raw caches are outside the full tracked-tree comparison. Source clones and
historical Git objects are needed to rerun the driver; it is not a standalone
release dependency. After source HEADs advance, `--historical` checks the recorded
commits/baseline and marks that all live source/merge checking was omitted.

No new result or scope correction needs importing. Preserve the reviewed payload.
At 16:30 run `finalize.py`, commit/push its outputs, then package that clean HEAD
into a fresh external directory. Final source freshness/wording reviews remain the
source managers' scheduled task. Reader access or artifact transfer is still pending.
