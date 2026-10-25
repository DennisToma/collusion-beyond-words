# Iteration 38 — post-compliance archive verification

Manager verification completed at 2026-10-25 14:27 UTC; no external critic or model call.
Target: `2add72837dc6752a0d026d0fef748fbdde11aee6` (iteration 37).
[Receipt](../results/reviewer_archive_i38.json), [executed driver](distribution_i38_driver.py).

The earlier distribution/archive checks target `c1e7fdd`, whose manuscript predates
the compliance cut and iteration-34 wording fixes. This check closes that specific
gap while preserving the reviewed submission, slides, scientific outputs and PDFs.

## Procedure

The driver creates an archive directly from the target's Git tree, extracts it into
an unused directory and compares every extracted file with its original Git blob.
All 257 files match; the extraction has no `.git` directory. Archive:

```text
/var/tmp/beyond-words-2add728.tar.gz
6,864,329 bytes
SHA256 496139fc3894d9908e0f4c5e1ecf613bd9ffbbf1e9569990e0392e6643e29651
```

Executed from the production checkout:

```bash
/var/tmp/bw-iteration33-release/.venv/bin/python reviews/distribution_i38_driver.py
```

The historical driver fixes its scratch paths and refuses to reuse an existing
scratch directory. Its Python environment and Chromium installation are reused
from iteration 33; the environment's `uv.lock` is byte-identical to the target's.
Only PATH, HOME, LANG, LC_ALL and TMPDIR are inherited where present; sibling-root
overrides point to nonexistent paths, and no model environment variables are passed.
HOME is unchanged. This uses the same VM, with no OS or filesystem sandbox, and
does not claim a fresh dependency installation or a remote-clone/access check.

The archived committed PDFs first pass the compliance checker with the committed
receipt reproduced byte-for-byte. The driver then deletes and rebuilds all six
calculation JSONs and all six figure PNGs, runs the source/coverage checks and
reproduction tests, rebuilds both PDFs, and runs export and compliance checks/tests.
The author-only runner-log refresh is excluded to preserve the dated usage snapshot.
All 20 command exits, durations and log hashes are recorded in the receipt; full
command logs remain in `/var/tmp/bw-i38-archive/`.

## Results

- Source checks: 111 assertions, 144 document bindings, 158 evidence hashes; zero failures.
- Decimal coverage: zero unclassified decimals in either manuscript or slides.
- Tests: 26 reproduction, 9 export and 3 compliance tests pass.
- All six calculation outputs and six figures rebuild byte-identically.
- Both PDFs have identical page text, content streams and full bytes after
  normalising only CreationDate/ModDate. The report remains 20 pages (6 main),
  with 234 abstract words; the form summary is 117 words; the deck has 8 slides.
- Export preserves 504 report fragments, 55 slide fragments and all 10 embedded
  figures with exact source pixels. The report PDF remains 1,153,269 bytes.
- Only the scratch PDFs and their hash fields in the two scratch receipts change.
  All other archived files and all production files are byte-identical to the target.

No scientific estimate, label, setting, model judgment, held-out evaluation or
manuscript wording changes. At the archive-check start source heads were Q1.4
`8625743` / Q2.2 `f73f49c`, with zero open P1; evidence pins remain
`732f08c` / `91ffb2d`. During handoff Q1.4 advanced to `589afac` (review metadata
only): I152 explicitly scope-reads the current iteration-34 manuscript bytes
with zero P1 and confirms 81/81 Q1.4 pin hashes unchanged. Q2.2 I160 already
covers the same manuscript bytes.

## Handoff

The archive above contains the current reviewed manuscript and scientific payload,
but predates this verification note and its receipt. Package the final committed
HEAD with the README command to include subsequent documentation or finalize edits.
This pass does not transfer the archive, grant reader access, change visibility or
repeat the earlier anonymous-access probes. The recorded access limitation remains:
provide an archive or arrange repository access for judging. At 16:30 UTC run the
planned author-machine finalize pass; if it changes the usage snapshot/manuscript,
repackage that final commit rather than reusing this historical archive.
