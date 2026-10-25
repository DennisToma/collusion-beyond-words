# Iteration 44 — rehearse the remaining finalization step

2026-10-25 15:19–15:24 UTC. Rehearsed the full author-machine finalizer from
merged commit `04c3da99850d015638bdb2e98a1447ffbfab6610` in an external Git
archive extraction. Production manuscript, science, figures, PDFs and usage
snapshot remain frozen. No new experiment, held-out evaluation or model call.

The earlier distribution checks exercised committed artifacts and fresh PDF
exports, but did not refresh the author-only usage snapshot. This pass checks
that remaining transition with current runner logs before the scheduled 16:30
production finalizer. It reuses iteration 42's locked Python environment and
Chromium on the same VM, with UV offline mode, absent sibling-root overrides,
and no model environment variables passed. HOME remains available because the
usage refresh intentionally reads the author-machine runner logs. It is not
a fresh installation, remote-access check or operating-system sandbox.

## Commands and evidence

```bash
/var/tmp/bw-iteration42-release/.venv/bin/python reviews/finalizer_rehearsal_i44.py
```

The driver verifies the archive against all 275 tracked Git files, then runs
`python scripts/finalize.py` inside `/var/tmp/bw-i44-finalizer-rehearsal/beyond-words`.
The [complete command log](finalizer_rehearsal_i44.log) records **FINALIZE OK**:
ten commands, 47 passing tests (26 reproduction, 9 packaging, 9 export,
3 compliance), 111 source assertions, 144 document bindings, 158 evidence hashes
and zero unclassified decimals. The [receipt](../results/finalizer_rehearsal_i44.json)
records input/output hashes, every changed archive path and the log checksum.

The first post-run preservation check stopped because its allowlist omitted
`results/source_check.json` and `results/reproduction_check.json`. Inspecting
both diffs showed only their expected `SUBMISSION.md` hash updates. The driver
was corrected to allow those receipts while asserting that their only changes
are the document hash. It also verifies the export/compliance receipt hash
updates and PDF size, leaving every other receipt field identical. Verification
resumed against the completed run; no tests were repeated:

```bash
/var/tmp/bw-iteration42-release/.venv/bin/python reviews/finalizer_rehearsal_i44.py --verify-existing
```

The receipt explicitly records resumed verification and leaves elapsed time
unset rather than presenting the resumed check as a new finalizer execution.
The scratch directory must not be reused for a new run. The driver pins the
historical input revision; any future production finalizer uses current HEAD.

## Preservation and layout

The rehearsal refreshes the source-manager usage snapshot from 368 completed
iterations at 14:13 UTC to **382 at 15:12 UTC (243 Opus, 139 Codex)**. These are
rehearsal counts, not the later 16:30 production snapshot. The report and
manuscript are byte-identical after replacing exactly one usage statement in
each with a placeholder. Every other archived file remains byte-identical
except the PDFs and their hash/size receipts listed above.

Only report page 19's content stream changes; all page text is identical after
normalizing whitespace and that usage statement. The other report page streams
are identical. All eight slide content streams are identical, and slide PDF
bytes match after normalizing only CreationDate/ModDate metadata. Compliance
remains **6 main / 20 total report pages**, **234 abstract words**, **117 form
summary words**, **8 slides** and **15 verified references**. The rebuilt report
is 1,153,280 bytes. Page 19 was rasterized with `pdftoppm` and visually checked;
the refreshed usage statement fits and remains readable.

Before writing these notes, the driver also verifies that every tracked
production file still has its pre-rehearsal bytes and HEAD has not changed.
Only the driver, receipts, this note, STATUS, REPORT, SOURCES and ledger are
added/updated for this iteration. No rehearsal PDF or refreshed production
usage snapshot is imported.

## Source freshness and remaining action

Q1.4 stays `372f375`, Q2.2 stays `1ac4621`, both clean. Complete source diffs
from those iteration-43 revisions are empty; no import, repin or new scope
review is needed. No DIRECTION deviation: its compliance work is already done,
and this pass preserves all empirical estimates and reviewed scientific prose.

Hold until 16:30 unless a director instruction or substantive source change
arrives. Then run the production `uv run python scripts/finalize.py`, inspect
the usage-only/document-hash/PDF changes, commit and push. Package that clean
HEAD with `scripts/package_release.py` into an unused external directory and
check `SHA256SUMS`. Do not substitute this rehearsal extraction for that final
package. Submission is due ready by 17:30; hard stop is 18:00 UTC. Dennis still
needs to transfer the artifacts or arrange reader access.
