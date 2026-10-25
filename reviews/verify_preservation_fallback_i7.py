"""Verify this release-only diff against its recorded baseline (author checkout).

uv run --group export python reviews/verify_preservation_fallback_i7.py
No experiments or new estimates. Requires baseline Git objects and export deps.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import finalize

BASELINE = subprocess.check_output(['git', 'rev-parse', '8e4ef25^{commit}'], cwd=ROOT,
                                  env={k: os.environ[k] for k in ('PATH', 'HOME') if k in os.environ}).decode().strip()


def original(path):
    return subprocess.check_output(['git', 'show', BASELINE + ':' + str(path)], cwd=ROOT,
                                   env={k: os.environ[k] for k in ('PATH', 'HOME') if k in os.environ})


def sha(data):
    return hashlib.sha256(data).hexdigest()


paths = [*Path(ROOT / 'evidence').rglob('*'), *Path(ROOT / 'figures').rglob('*.png')]
paths += [ROOT / p for p in ('TEMPLATE_REPORT.md', 'SLIDES.md', 'IMAGE.png')]
paths += [ROOT / 'results' / p for p in ('unrounded_q22.json', 'c21b_floor.json', 'locked_test_q22.json',
                                       'grid_q14.json', 'gate_q14.json', 'gate_pcmi_q14.json')]
files = []
for path in paths:
    if not path.is_file():
        continue
    relative = path.relative_to(ROOT).as_posix()
    old = original(relative)
    assert old == path.read_bytes(), relative
    files.append(dict(path=relative, sha256=sha(old)))
old_checks = json.loads(original('results/source_check.json'))
new_checks = json.loads((ROOT / 'results/source_check.json').read_text())
assert new_checks['checks'][:111] == old_checks['checks']
assert new_checks['document_checks'] == old_checks['document_checks']

old = original('SUBMISSION.md').decode()
expected = old.replace('passes 111 saved-source assertions and 144 bindings',
                       'passes 120 saved-source assertions and 144 bindings')
expected = expected.replace('passes 26 release checks', 'passes 30 release checks')
expected = expected.replace('numbers from this report and the slides, plus all bundle-file hashes.',
                            'numbers from this report and the slides, plus 65 section-scoped bindings for the primary report and all bundle-file hashes. The primary-report inventory covers decimals, percentages and fractions in its scientific sections; integer-only and qualitative claims still require review.')
assert finalize.SUB_RE.sub('<USAGE>', expected) == finalize.SUB_RE.sub('<USAGE>', (ROOT / 'SUBMISSION.md').read_text())

pdfs = {}
for name, allowed in [('TEMPLATE_REPORT.pdf', []), ('SLIDES.pdf', []), ('SUBMISSION.pdf', [19, 20])]:
    old = PdfReader(io.BytesIO(original(name)))
    new = PdfReader(ROOT / name)
    assert len(old.pages) == len(new.pages), name
    changed = [i + 1 for i, (p, q) in enumerate(zip(old.pages, new.pages))
               if p.get_contents().get_data() != q.get_contents().get_data()]
    assert changed == allowed, (name, changed)
    pdfs[name] = dict(pages=len(new.pages), changed_content_stream_pages=changed,
                      sha256=sha((ROOT / name).read_bytes()))
out = dict(baseline=BASELINE, preserved_files=files, n_preserved_files=len(files),
           unchanged_original_source_assertions=111, unchanged_original_document_bindings=144,
           extended_markdown_change='exact provenance-count paragraph and usage-snapshot replacements only',
           pdfs=pdfs, scope='Git bytes and PDF page streams; date metadata may differ. Not new analysis, model calls or scientific validation.')
(ROOT / 'results/primary_preservation_fallback_i7.json').write_text(json.dumps(out, indent=2) + '\n')
print(f"PASS: {len(files)} unchanged scientific/manuscript/image files; original 111/144 assertions/bindings unchanged; PDF streams as recorded")
