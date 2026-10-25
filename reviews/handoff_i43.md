# Iteration 43 — preserve the freeze and verify the exact handoff

Checked at 2026-10-25 15:13–15:15 UTC. The iteration-42 handoff already exists
at `/var/tmp/beyond-words-i42-handoff` and packages the actual notes commit
`8df26e5ec85234f99db0474a863ac556f2e8c35c`, rather than its earlier preflight
commit `e64ff45`. Remote `refs/heads/main` matches that revision at this check.

No experiment, new scientific analysis, model call, manuscript edit, PDF rebuild,
dependency install, usage-count refresh, submission, transfer or access grant.
The bounded verification ends early because the reviewed release is frozen;
the next scheduled change is the 16:30 finalizer.

## Executed checks

```bash
uv run python scripts/check_sources.py
uv run python scripts/number_coverage.py
uv run --group export python scripts/check_committed_export.py
uv run --group export python scripts/check_submission_compliance.py
git ls-remote origin refs/heads/main
```

All pass: 111 source assertions, 144 document bindings, 158 evidence hashes;
zero unclassified decimals; 504 report and 55 correctly placed slide fragments;
ten matching embedded figures. Compliance remains six main / 20 total report
pages, a 234-word abstract, a 117-word form summary and eight slides. These
commands leave every tracked file unchanged.

```bash
cd /var/tmp/beyond-words-i42-handoff
sha256sum -c SHA256SUMS
```

All 14 entries pass. From the repository root, the additional integrity check
below was run with `uv run --group export python -`. It verifies all 274
archive members against Git, the copied uploads, the eight recorded successful
command outputs and all recorded artifacts. It does not rerun the historical
47-test acceptance; the final package command below does.

```python
import json
import sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import package_release as p
root = Path.cwd()
handoff = Path('/var/tmp/beyond-words-i42-handoff')
receipt = json.loads((handoff / 'receipt.json').read_text())
head = p.clean_head(root)
assert receipt['revision'] == head
files = p.tree_files(root, head)
assert receipt['files'] == files
archive = next(handoff.glob('*.tar.gz'))
p.verify_archive(archive, files)
for name in p.UPLOADS:
    assert (handoff / name).read_bytes() == p.git(root, 'show', f'{head}:{name}')
assert receipt['ok'] is True
assert tuple(row['script'] for row in receipt['commands']) == p.CHECKS
assert all(row['exit_code'] == 0 and
           p.sha((handoff / row['log']).read_bytes()) == row['log_sha256']
           for row in receipt['commands'])
for name, expected in receipt['artifacts'].items():
    artifact = handoff / name
    assert p.sha(artifact.read_bytes()) == expected['sha256']
    assert artifact.stat().st_size == expected['bytes']
```

This exact-HEAD assertion applies to the recorded check before these notes.
The checked handoff's own receipt/checksums stay outside Git to avoid circular
archive hashes; iteration 42's tracked receipt still describes its preflight.

## Source freshness

```bash
git -C ../collusion-14-infotheory diff e8cf411..372f375 --
git -C ../collusion-22-say-vs-do diff 5a012a0..1ac4621 --
git -C ../collusion-14-infotheory status --porcelain
git -C ../collusion-22-say-vs-do status --porcelain
```

Both complete source diffs contain only two added STATUS lines; worktrees are
clean. Q1.4 I156/I157 and Q2.2 I166/I167 confirm unchanged merged scientific
bytes. No source import or repin is needed. Q1.4's two known source quote misses
and Q2.2's single pinned REPORT metadata difference remain as disclosed.

## Package this iteration's notes

After committing/pushing these notes, run from the clean repository root:

```bash
PLAYWRIGHT_BROWSERS_PATH=/var/tmp/bw-i42-browser /var/tmp/bw-iteration42-release/.venv/bin/python scripts/package_release.py --output-dir /var/tmp/beyond-words-i43-handoff
cd /var/tmp/beyond-words-i43-handoff
sha256sum -c SHA256SUMS
```

This runs the full eight-command acceptance on the new committed archive.
Its external `receipt.json` identifies the exact notes commit, avoiding another
tracked receipt/notes cycle. A successful package uses the existing locked
Python/browser on the same VM and preserves committed PDFs and usage counts.
At 16:30 run `uv run python scripts/finalize.py`, commit/push its outputs, then
package the new clean HEAD into an unused directory. Dennis still needs to
transfer the artifacts or arrange reader access.
