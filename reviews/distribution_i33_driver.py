"""Recorded manager distribution check for iteration 33 (not a new critic).

Historical target and scratch paths are fixed below. Prepare a clean target clone and
fresh locked virtualenv as documented in distribution_i33.md before executing this
script. Access-check fields record the separate anonymous/SSH probes in that record;
this driver runs the scientific/export commands and checks all tracked artifact bytes.
Writes its receipt under /var/tmp; does not modify the production repository.
"""
import hashlib, io, json, os, re, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path('/var/tmp/bw-iteration33-release')
REV = 'c1e7fddaca131f0fefc8a7c5aa3cd7e27888db4a'
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
assert git('rev-parse', 'HEAD').decode().strip() == REV
paths = git('ls-files', '-z').decode().strip('\0').split('\0')
before = {p: git('show', f'HEAD:{p}') for p in paths}
env = {k: os.environ[k] for k in ('PATH', 'HOME', 'LANG', 'LC_ALL', 'TMPDIR') if k in os.environ}
env.update(BW_Q14_ROOT=str(ROOT / 'absent-q14'), BW_Q22_ROOT=str(ROOT / 'absent-q22'), MPLCONFIGDIR='/var/tmp/bw-i33-matplotlib', PLAYWRIGHT_BROWSERS_PATH='/var/tmp/bw-i33-browser')
assert not Path(env['BW_Q14_ROOT']).exists() and not Path(env['BW_Q22_ROOT']).exists()
replays = ['unrounded_q22', 'c21b_floor', 'locked_test_q22', 'grid_q14', 'gate_pcmi_q14', 'gate_q14']
scripts = ['recompute_' + p + '.py' for p in replays]
figures = sorted((ROOT / 'figures').glob('fig*.png'))
regenerated = ['results/' + p + '.json' for p in replays] + [str(p.relative_to(ROOT)) for p in figures]
for p in regenerated:
    (ROOT / p).unlink()
commands = [[str(ROOT / '.venv/bin/python'), 'scripts/' + p] for p in scripts]
commands += [[str(ROOT / '.venv/bin/python'), 'scripts/' + p] for p in ['fig1_hard_negatives.py', 'fig2_level_vs_comovement.py', 'fig3_e70_grid.py', 'fig4_say_vs_do.py', 'fig5_placebo_premium.py', 'fig6_strong_framing.py', 'check_sources.py', 'number_coverage.py']]
commands += [[str(ROOT / '.venv/bin/python'), 'tests/test_reproduction.py'], [str(ROOT / '.venv/bin/python'), '-m', 'playwright', 'install', 'chromium'], [str(ROOT / '.venv/bin/python'), 'scripts/export_pdf.py'], [str(ROOT / '.venv/bin/python'), 'tests/test_export.py']]
rows = []
logdir = Path('/var/tmp/bw-i33-command-logs'); logdir.mkdir()
for i, cmd in enumerate(commands):
    print(f'[{i+1}/{len(commands)}] {" ".join(cmd[1:])}', flush=True)
    start = time.monotonic()
    with (logdir / f'{i+1:02d}.log').open('w') as log:
        result = subprocess.run(cmd, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
    row = {'command': ['.venv/bin/python'] + cmd[1:], 'exit_code': result.returncode, 'elapsed_seconds': round(time.monotonic()-start, 3)}
    rows.append(row)
    if result.returncode:
        print((logdir / f'{i+1:02d}.log').read_text(), flush=True)
        raise SystemExit(result.returncode)
    print(f'  OK ({row["elapsed_seconds"]}s)', flush=True)
after = {p: (ROOT / p).read_bytes() for p in paths}
for p in regenerated:
    assert before[p] == after[p], p
changed = sorted(p for p in paths if before[p] != after[p])
assert set(changed) <= {'SUBMISSION.pdf', 'SLIDES.pdf', 'results/export_check.json'}, changed
sys.path.insert(0, str(ROOT / '.venv/lib/python3.12/site-packages'))
from pypdf import PdfReader
def normalise(data):
    return re.sub(rb'/(CreationDate|ModDate)\s*\(D:[^)]*\)', rb'/\1 (normalised)', data)
pdfs = {}
for name in ('SUBMISSION.pdf', 'SLIDES.pdf'):
    old, new = PdfReader(io.BytesIO(before[name])), PdfReader(io.BytesIO(after[name]))
    assert len(old.pages) == len(new.pages)
    assert [p.extract_text() for p in old.pages] == [p.extract_text() for p in new.pages]
    assert [p.get_contents().get_data() for p in old.pages] == [p.get_contents().get_data() for p in new.pages]
    assert normalise(before[name]) == normalise(after[name]), name
    pdfs[name] = {'pages': len(new.pages), 'page_text_identical': True, 'content_streams_identical': True, 'byte_identical_after_date_normalisation': True, 'committed_sha256': hashlib.sha256(before[name]).hexdigest(), 'rebuilt_sha256': hashlib.sha256(after[name]).hexdigest()}
old_receipt = json.loads(before['results/export_check.json'])
new_receipt = json.loads(after['results/export_check.json'])
for name in pdfs:
    assert new_receipt['sha256'][name] == hashlib.sha256(after[name]).hexdigest()
    new_receipt['sha256'][name] = old_receipt['sha256'][name]
assert new_receipt == old_receipt
read = lambda p: json.loads((ROOT / 'results' / p).read_text())
source, repro, export_tests, export, coverage = [read(p) for p in ['source_check.json', 'reproduction_check.json', 'export_test.json', 'export_check.json', 'number_coverage.json']]
receipt = {'checked_at_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), 'revision': REV, 'remote': 'https://github.com/DennisToma/collusion-beyond-words', 'clone': 'git clone --no-local gh-cbw:DennisToma/collusion-beyond-words.git /var/tmp/bw-iteration33-release', 'access_check': {'anonymous_https_clone_exit_code': 128, 'anonymous_web_status': 404, 'anonymous_api_status': 404, 'source_repo_web_status': {'Q1.4': 404, 'Q2.2': 404}, 'authenticated_ssh_clone_exit_code': 0, 'interpretation': 'Anonymous access unavailable in this check; authorized repository access or an author-supplied archive is required. Repository visibility was not queried successfully or changed.'}, 'dependency_install': 'uv sync --locked --all-groups --no-cache', 'uv_lock_sha256': hashlib.sha256(before['uv.lock']).hexdigest(), 'environment': {'fresh_virtualenv': True, 'python': subprocess.check_output([str(ROOT / '.venv/bin/python'), '--version'], env=env, text=True).strip(), 'fresh_browser_download': True, 'sibling_root_overrides': 'nonexistent paths', 'model_environment_variables': 'not passed', 'scope': 'Same author VM; no OS/filesystem sandbox. HOME unchanged.'}, 'commands': rows, 'deleted_and_regenerated_byte_identical': {p: hashlib.sha256(after[p]).hexdigest() for p in regenerated}, 'checks': {k: source[k] for k in ('n_checks','n_document_checks','n_evidence_files','n_fail','n_document_fail')}, 'unclassified_decimals': {p: coverage[p]['unbound_unclassified'] for p in ('SUBMISSION.md','SLIDES.md')}, 'reproduction_tests': repro, 'export_tests': export_tests, 'export': {k: export[k] for k in ('ok','submission_pages','slides','submission_text_fragments','slide_text_fragments','figure_counts')}, 'pdfs': pdfs, 'changed_tracked_paths': changed, 'all_other_tracked_files_byte_identical': True, 'retained_production_pdfs': True, 'scope': 'Distribution verification of frozen calculations, including the archived historical pCMI null replay. No new experiments, model calls, labels, settings or test evaluation; author-only runner-log refresh excluded.'}
Path('/var/tmp/bw-i33-distribution-check.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS: six replay JSONs, six figures, all tracked artifacts match except PDF dates and receipt PDF hashes.', flush=True)
