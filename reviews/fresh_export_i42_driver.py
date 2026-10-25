"""Historical iteration-42 PDF rebuild from the verified preflight archive.

Run with the fresh clone's export-enabled Python after the commands recorded in
handoff_i42.md. Refuses to reuse its scratch directory. Never changes production
artifacts, refreshes usage counts, calls models or generates new research data.
"""
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import time

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path("/var/tmp/beyond-words-i42-preflight")
SCRATCH = Path("/var/tmp/bw-i42-fresh-export")
CLONE = Path("/var/tmp/bw-iteration42-release")
BROWSER = Path("/var/tmp/bw-i42-browser")
REVISION = "e64ff45a794c8ce3325b271204efee179602f5ec"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    package = json.loads((PACKAGE / "receipt.json").read_text())
    assert package["ok"] and package["revision"] == REVISION
    subprocess.run(["sha256sum", "-c", "SHA256SUMS"], cwd=PACKAGE, check=True)
    assert Path(sys.executable).parent == CLONE / ".venv/bin"
    archive = PACKAGE / next(name for name in package["artifacts"] if name.endswith(".tar.gz"))
    assert (CLONE / "uv.lock").read_bytes() == (ROOT / "uv.lock").read_bytes()
    assert BROWSER.is_dir()
    SCRATCH.mkdir()
    with tarfile.open(archive) as packed:
        packed.extractall(SCRATCH, filter="data")
    extracted = SCRATCH / "beyond-words"
    assert not (extracted / ".git").exists()
    before = {p: (extracted / p).read_bytes() for p in package["files"]}
    assert all(sha(data) == package["files"][p]["sha256"] for p, data in before.items())
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    env.update(BW_Q14_ROOT=str(SCRATCH / "absent-q14"), BW_Q22_ROOT=str(SCRATCH / "absent-q22"),
               PLAYWRIGHT_BROWSERS_PATH=str(BROWSER), MPLCONFIGDIR=str(SCRATCH / "matplotlib"))
    rows = []
    for script in ("scripts/export_pdf.py", "scripts/check_committed_export.py",
                   "scripts/check_submission_compliance.py"):
        log = SCRATCH / f"{Path(script).stem}.log"
        start = time.monotonic()
        with log.open("w") as output:
            result = subprocess.run([sys.executable, script], cwd=extracted, env=env,
                                    stdout=output, stderr=subprocess.STDOUT)
        rows.append(dict(script=script, exit_code=result.returncode,
                         elapsed_seconds=round(time.monotonic() - start, 3), log_sha256=sha(log.read_bytes())))
        if result.returncode:
            raise RuntimeError(log.read_text())
        print(f"PASS: {script}", flush=True)
    after = {p: (extracted / p).read_bytes() for p in before}
    changed = sorted(p for p in before if before[p] != after[p])
    assert set(changed) <= {"SUBMISSION.pdf", "SLIDES.pdf", "results/export_check.json",
                            "results/submission_compliance.json"}, changed
    pdfs = {}
    for name in ("SUBMISSION.pdf", "SLIDES.pdf"):
        old, new = PdfReader(io.BytesIO(before[name])), PdfReader(io.BytesIO(after[name]))
        assert len(old.pages) == len(new.pages)
        assert [p.extract_text() for p in old.pages] == [p.extract_text() for p in new.pages]
        assert [p.get_contents().get_data() for p in old.pages] == [p.get_contents().get_data() for p in new.pages]
        normalise = lambda raw: re.sub(rb"/(CreationDate|ModDate)\s*\(D:[^)]*\)", rb"/\1 (normalised)", raw)
        assert normalise(before[name]) == normalise(after[name])
        pdfs[name] = dict(pages=len(new.pages), page_text_identical=True, content_streams_identical=True,
                          bytes_equal_except_pdf_dates=True, committed_sha256=sha(before[name]),
                          rebuilt_sha256=sha(after[name]))
    for name in ("results/export_check.json", "results/submission_compliance.json"):
        old, new = json.loads(before[name]), json.loads(after[name])
        for pdf in pdfs:
            assert new["sha256"][pdf] == sha(after[pdf])
            new["sha256"][pdf] = old["sha256"][pdf]
        assert old == new
    receipt = dict(ok=True, revision=REVISION,
        checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        archive_sha256=sha(archive.read_bytes()), package_receipt_sha256=sha((PACKAGE / "receipt.json").read_bytes()),
        tracked_files_verified=len(before), commands=rows, pdfs=pdfs, changed_archive_paths=changed,
        environment=dict(python=sys.version, executable=sys.executable, browser=str(BROWSER),
                         uv_lock_sha256=sha(before["uv.lock"]),
                         setup="New authorized clone, uv sync --locked --all-groups --no-cache and new Chromium download in iteration 42."),
        compliance=json.loads(after["results/submission_compliance.json"]),
        scope="Fresh dependency/browser installation on the same author VM. Only PDF date metadata and its receipt hashes change; all other tracked archive bytes preserved. No usage refresh, source write, experiment, new scientific analysis, model call, submission, transfer or access grant.")
    (SCRATCH / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"FRESH EXPORT OK: {SCRATCH / 'receipt.json'}", flush=True)


if __name__ == "__main__":
    main()
