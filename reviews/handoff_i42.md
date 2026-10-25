# Iteration 42 — post-cutoff handoff with a fresh installation

The experiment cutoff has passed. Preserve the reviewed manuscript and all
scientific artifacts; this iteration checks acquisition, installation and export.
No experiments, model calls, new scientific analysis or usage-count refresh.

## Source freshness

```bash
uv run python reviews/source_freeze_i40_driver.py --output results/source_freeze_i42.json
```

The post-15:00 live check passes on Q1.4 `e8cf411` / Q2.2 `5a012a0`, with the same
full tracked-tree reconciliation and 158 Git-pin hashes as iteration 40. All 179
protected release files match `a924419`. The new receipt differs from iteration
40 only in merge HEAD and timestamp. `--output` is the only change to the original
driver: its default remains unchanged and the historical receipt is preserved.
The known Q1.4 quote misses and sole Q2.2 report-metadata drift remain disclosed.

Q1.4 advanced during the release check to
`372f375e2ba2dd7d610a03ec4b114fa90a714ffa`; its complete diff from `e8cf411` adds
only two STATUS log lines (I156/I157), confirming unchanged manuscript/pin bytes.
Q2.2 remained at `5a012a0`; both worktrees were clean. This final metadata-only
addendum does not change the earlier receipt's recorded revision.

```bash
git -C ../collusion-14-infotheory diff e8cf411..372f375 --
git -C ../collusion-14-infotheory status --porcelain
git -C ../collusion-22-say-vs-do status --porcelain
```

## Executed fresh-clone acceptance

```bash
git clone gh-cbw:DennisToma/collusion-beyond-words.git /var/tmp/bw-iteration42-release
cd /var/tmp/bw-iteration42-release
uv sync --locked --all-groups --no-cache
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/bw-i42-browser uv run --group export playwright install chromium
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/bw-i42-browser uv run --group export python scripts/package_release.py --output-dir /var/tmp/beyond-words-i42-preflight
```

The newly authorized remote clone resolved to
`e64ff45a794c8ce3325b271204efee179602f5ec`. A new virtualenv installed all locked
dependencies; Chromium was downloaded into a new directory. The packager checks
an extraction without `.git`, with nonexistent sibling-root overrides and no model
environment variables passed. All eight commands and 47 tests pass (26
reproduction, nine export, three compliance, nine packaging). All 269 tracked
archive files retain Git bytes/modes. Source checks remain 111 assertions, 144
document bindings and 158 hashes, with zero unclassified decimals.

The exact external package receipt is copied to
[`results/release_package_i42.json`](../results/release_package_i42.json); it
records the archive and all file/log hashes. The 14 sidecar checksum entries pass.
This verifies the authorized clone; it does not repeat anonymous-access probes.

## Executed fresh-browser export

From the production repository, using the new clone's Python:

```bash
/var/tmp/bw-iteration42-release/.venv/bin/python reviews/fresh_export_i42_driver.py
```

The [recorded driver](fresh_export_i42_driver.py) verifies the preflight package's
checksums, extracts its archive into a new directory, rebuilds the two PDFs,
then runs committed-export and submission-compliance checks. Both PDFs have
identical page text, content streams and bytes after normalising only PDF date
metadata. The corresponding receipt hashes are the only other changed archive
content. All other tracked bytes, including manuscript, figures, evidence and
scientific results, remain identical. The report remains six main / 20 total
pages with a 234-word abstract; the deck has eight slides. Production artifacts
are untouched. [Receipt](../results/fresh_export_i42.json).

This is a fresh dependency/browser installation on the same author VM, not an
independent operating-system check. Package checks include replay/figure parity;
the extra browser pass rebuilds only the PDFs. Existing scientific validation
limitations, model/prompt scope and source-label dependence still apply.

## Exact notes-commit handoff

The preflight archive predates these receipts and notes. After committing and
pushing them, package the clean production HEAD into a fresh external directory:

```bash
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/bw-i42-browser /var/tmp/bw-iteration42-release/.venv/bin/python scripts/package_release.py --output-dir /var/tmp/beyond-words-i42-handoff
cd /var/tmp/beyond-words-i42-handoff
sha256sum -c SHA256SUMS
```

The external receipt identifies the exact notes commit, avoiding circular archive
hashes. At 16:30 run the author-machine `finalize.py`, commit/push its outputs,
then package that new clean HEAD again. This package is prepared before that
scheduled usage refresh. Reader access or artifact transfer remains Dennis's
handoff step; no submission, transfer or access grant was performed.
