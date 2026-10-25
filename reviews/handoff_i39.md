# Iteration 39 — verified committed handoff

Acceptance target: `c3d2903842fa6b84d8e03dc352e65a52f175f060`; completed 2026-10-25T14:45:24Z.
[Receipt](../results/release_package_i39.json), [Codex review/follow-up](codex_i39.md).
This is release verification only; no experiment, model-based scientific judgment,
new held-out evaluation, PDF rebuild or usage-count refresh.

## Executed command

```bash
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/bw-i33-browser uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-i39-c3d2903-handoff
```

The command was run from a clean production checkout after committing/pushing the
review fixes. All 264 tracked files match Git (bytes and modes) in the
archive and after all eight checks in an extraction without `.git`. The archive is
`beyond-words-c3d2903842fa.tar.gz` (6880649 bytes, SHA256 `70965cb1b3d1a3e20e50f3cfb614c1148e5386e36be35444b6a07f0b38592055`).
The receipt inventories every tracked file and the upload artifacts; full logs and
SHA256SUMS accompany it in the output directory. `sha256sum -c SHA256SUMS` verifies
the archive, both PDFs, form, receipt, handoff note and all eight check logs.

## What passed

- 111 source assertions, 144 document bindings, 158 evidence hashes; no failures.
- No unclassified decimal in either manuscript or slides.
- Committed-PDF checks: 504 report text fragments and all slide fragments on their
  correct pages; six report and four slide figures match current PNG pixels; links
  have portable schemes. This does not launch a browser or rerun layout fitting.
- 26 reproduction, 9 export, 3 compliance and 9 packaging tests (47 total).
- Existing compliance: 234-word abstract, 117-word form summary, 6 main / 20 total
  report pages, 1,153,269-byte report, 8 slides, 15 recorded reference identities.
- All tracked extraction bytes/modes remain identical after the checks. The author
  checkout stays clean, and its HEAD remains unchanged before publishing the output.
- Packaging fixtures reject dirty/staged/untracked/concurrent changes, archive
  omission/corruption/duplicates/unsafe members and check failures. Actual export
  fixtures reject an updated source PNG with an unchanged PDF. Foreign Git-variable
  fixtures preserve the foreign repository's HEAD, index, config and worktree.

The recorded interpreter/environment is existing, not a fresh dependency/browser
installation. HOME is retained on the same author VM, with no OS/filesystem sandbox.
All packaging Git subprocesses and verification commands use an environment
allowlist; no model environment variables are passed. Source root overrides point
to nonexistent paths. No network acquisition/access check or submission/transfer
is performed. Chromium is used only by the existing export-failure fixtures.

## Scientific preservation

The following read-only comparison exits zero with no differences:

```bash
git diff --exit-code 2da601d c3d2903 -- SUBMISSION.md SUBMISSION.pdf SLIDES.md SLIDES.pdf SUBMISSION_FORM.md figures evidence results/unrounded_q22.json results/c21b_floor.json results/locked_test_q22.json results/grid_q14.json results/gate_q14.json results/gate_pcmi_q14.json results/process_log_summary.json uv.lock
```

Only the export-test receipt's test-code hash changes; the test count stays nine.
The earlier iteration-38 receipt remains the evidence for deleting/rebuilding all
six calculations and six figures and comparing rebuilt PDF text/streams/date-normalised
bytes. This new packager checks the committed artifacts and adds direct current-PNG
concordance; it does not claim a new PDF rebuild.

## Review and handoff

The initial read-only Codex critic found two P2s (no P1): committed PNG/PDF concordance
was missing, and fixture Git inherited redirecting variables. Both were fixed and
regression-tested. Its follow-up reports no remaining actionable P1/P2. The critic
used nonmutating/in-memory probes; it could not run write-dependent suites under its
read-only sandbox. The manager ran the full acceptance recorded here.

The target archive predates this acceptance receipt/note. For handoff, package the
notes commit from clean HEAD into a fresh external directory; the external receipt
records that exact revision. At 16:30 run the author-machine finalizer, commit/push
its outputs and package that HEAD again. Reader access or artifact transfer is still
required; producing these files does not submit a form or grant repository access.
