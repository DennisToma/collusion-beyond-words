# Iteration 15 — completed handoff verification

The user's 18:00 UTC hard stop takes precedence over DIRECTION's local extension.
Research is stopped. This iteration records completed acceptance and closes the upload
handoff; it does not change scientific claims, manuscripts, exports or usage counts.

The iteration-14 handoff completed at 18:05:05 UTC for
`df7c051616716b971c74d3cfe4f44a17345d26b6`. Its actual receipt is preserved at
`results/release_package_i14.json`. The checks below passed against that package:
11 successful command logs, 309 Git-matching tracked files, all artifact hashes,
20 checksums and root upload identity. The code ZIP is 24,225,178 bytes, SHA256
`efcddb22a2c063d001af659815eb074fae9788f321a492f6b4ac66b6158c7406`.
This verifies an existing same-VM acceptance, rather than rerunning its 57 tests.

Reproduce the completed-package verification from the repo root on the author VM:

```bash
uv run --group export python - <<'PY'
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import package_release as p
root = Path.cwd()
package = Path('/var/tmp/bw-final-i14')
r = json.loads((package / 'receipt.json').read_text())
assert r == json.loads((root / 'results/release_package_i14.json').read_text())
assert r['ok'] and len(r['commands']) == 11
revision = r['revision']
files = p.tree_files(root, revision)
assert r['files'] == files and r['tracked_files_verified'] == len(files) == 309
p.verify_archive(package / f'beyond-words-{revision[:12]}.tar.gz', files)
for row in r['commands']:
    assert row['exit_code'] == 0
    assert p.sha((package / row['log']).read_bytes()) == row['log_sha256']
for name, entry in r['artifacts'].items():
    data = (package / name).read_bytes()
    assert len(data) == entry['bytes'] and p.sha(data) == entry['sha256']
for name in p.UPLOADS:
    assert (root / name).read_bytes() == (package / name).read_bytes(), name
lines = (package / 'SHA256SUMS').read_text().splitlines()
assert len(lines) == 20
for line in lines:
    digest, name = line.split('  ', 1)
    assert p.sha((package / name).read_bytes()) == digest, name
assert r['code_zip']['bytes'] == 24_225_178 < 25_000_000
print('I14 VERIFIED:', revision, len(files), 'files;', len(lines), 'checksums')
PY
uv run python reviews/verify_hold_i11.py
```

Root ZIP matched i14 during verification. It will be replaced with the final notes
revision's ZIP; the historical verification above deliberately checks i14's own ZIP
through its receipt/checksums instead of requiring root to stay on that revision.
The provenance checker again passed 158 pins, 176 preserved files and eight accepted
artifacts. No source science or accepted upload bytes changed.

After committing and pushing these notes, run each step only after success:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-final-i15
cp /var/tmp/bw-final-i15/submission_code.zip submission_code.zip
cd /var/tmp/bw-final-i15
sha256sum -c SHA256SUMS
```

The final external receipt records actual acceptance and the exact committed revision;
this procedure does not assert completion before it occurs. Packaging reruns the
existing acceptance in an extracted Git archive with absent sibling paths and verifies
the code ZIP against Git and frozen source pins. No PDF rebuild or new evaluation.
Upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png`, and `submission_code.zip`, using
`SUBMISSION_FORM.md`. Optional supplements: `SUBMISSION.pdf`, `SLIDES.pdf`.
Dennis still must submit; no upload, transfer or repository visibility change occurs here.
