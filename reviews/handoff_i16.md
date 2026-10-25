# Iteration 16 — final accepted upload release

The user's explicit 18:00 UTC hard stop takes precedence over DIRECTION's local
extension. Research is complete. The iteration-15 package completed at
18:10:47 UTC for `7ba00f1afeb08489e53587b91241fa218c48e8e3`.
Its actual receipt is copied unchanged to `results/release_package_i15.json`.

The following command verifies the existing same-VM acceptance, including all
11 successful command-log hashes, 311 Git-matching archived files/modes, artifact
hashes, 20 checksums and root upload identity. It does not rerun the 57 tests.
It also checks 158 stored evidence blobs, 176 preserved scientific files and
eight accepted manuscript/upload artifacts against recorded hashes.

```bash
uv run --group export python - <<'PY'
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
import package_release as p
root = Path.cwd()
package = Path('/var/tmp/bw-final-i15')
r = json.loads((package / 'receipt.json').read_text())
assert r == json.loads((root / 'results/release_package_i15.json').read_text())
assert r['ok'] and len(r['commands']) == 11
revision = r['revision']
assert revision == '7ba00f1afeb08489e53587b91241fa218c48e8e3'
files = p.tree_files(root, revision)
assert r['files'] == files and r['tracked_files_verified'] == len(files) == 311
p.verify_archive(package / f'beyond-words-{revision[:12]}.tar.gz', files)
for row in r['commands']:
    assert row['exit_code'] == 0
    assert p.sha((package / row['log']).read_bytes()) == row['log_sha256']
for name, entry in r['artifacts'].items():
    data = (package / name).read_bytes()
    assert len(data) == entry['bytes'] and p.sha(data) == entry['sha256']
for name in (*p.UPLOADS, 'submission_code.zip'):
    assert (root / name).read_bytes() == (package / name).read_bytes(), name
lines = (package / 'SHA256SUMS').read_text().splitlines()
assert len(lines) == 20
for line in lines:
    digest, name = line.split('  ', 1)
    assert p.sha((package / name).read_bytes()) == digest, name
assert r['code_zip']['bytes'] == 24_246_215 < 25_000_000
manifest = json.loads((root / 'evidence/manifest.json').read_text())
entries = [entry for project in manifest['projects'].values()
           for entry in project['files'].values()]
assert len(entries) == 158
for entry in entries:
    assert p.sha((root / 'evidence' / entry['stored_path']).read_bytes()) == entry['stored_sha256']
hold = json.loads((root / 'results/release_hold_i11.json').read_text())
assert len(hold['preserved_files']) == 176 and len(hold['artifacts']) == 8
for path, digest in hold['preserved_files'].items():
    assert p.sha((root / path).read_bytes()) == digest, path
for path, entry in hold['artifacts'].items():
    assert p.sha((root / path).read_bytes()) == entry['sha256'], path
print('FINAL UPLOAD VERIFIED:', revision, len(files), 'files;', len(lines), 'checksums')
PY
```

The code ZIP is 24,246,215 bytes, SHA256
`4380a0774f58aae2c48842c4e7d988b40b77985ccd5438bf71f76454b25da17f`.
Upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png` and `submission_code.zip`, using
`SUBMISSION_FORM.md`. Optional supplements: `SUBMISSION.pdf`, `SLIDES.pdf`.
The package directory contains identical upload copies and its integrity records.

This iteration's closure notes and receipt are outside the fixed accepted release
ZIP. There is no pending package rebuild: another receipt-only notes commit does
not change the deliverable. Any future scientific or upload-artifact change would
require fresh acceptance. No experiment, evaluation, export, model call, usage
refresh, submission, transfer or repository visibility change occurred here.
Dennis still must submit the files.
