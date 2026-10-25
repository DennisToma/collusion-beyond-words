"""Author-machine finalizer rehearsal; changes only an external archive extraction.

Run with the iteration-42 export-enabled Python. Uses current runner logs and
the existing locked environment/browser, not a new install or experiment.
The scratch directory must not exist unless --verify-existing is given to
inspect a completed run without repeating it. A successful receipt remains external;
copy it into results only after inspecting its changed-file list and log.
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
SCRATCH = Path("/var/tmp/bw-i44-finalizer-rehearsal")
ENVIRONMENT = Path("/var/tmp/bw-iteration42-release/.venv")
BROWSER = Path("/var/tmp/bw-i42-browser")
REVISION = "04c3da99850d015638bdb2e98a1447ffbfab6610"
sys.path.insert(0, str(ROOT / "scripts"))
import finalize
import package_release as package


def sha(data):
    return hashlib.sha256(data).hexdigest()


def normal_text(text):
    return " ".join(text.split())


def main():
    assert sys.argv[1:] in ([], ["--verify-existing"]), "Usage: finalizer_rehearsal_i44.py [--verify-existing]"
    verify_existing = bool(sys.argv[1:])
    revision = REVISION
    production_revision = package.git(ROOT, "rev-parse", "HEAD^{commit}").decode().strip()
    production_before = {name: (ROOT / name).read_bytes()
                         for name in package.tree_files(ROOT, production_revision)}
    files = package.tree_files(ROOT, revision)
    before = {name: package.git(ROOT, "show", f"{revision}:{name}") for name in files}
    assert (ENVIRONMENT.parent / "uv.lock").read_bytes() == before["uv.lock"]
    assert Path(sys.executable).parent == ENVIRONMENT / "bin"
    assert BROWSER.is_dir()
    archive = SCRATCH / "input.tar.gz"
    if not verify_existing:
        SCRATCH.mkdir()
        subprocess.run(["git", "-c", "tar.umask=0022", "archive", "--format=tar.gz",
                        "--prefix=beyond-words/", f"--output={archive}", revision],
                       cwd=ROOT, env=package.local_environment(), check=True)
    package.verify_archive(archive, files)
    extracted = SCRATCH / "beyond-words"
    if not verify_existing:
        with tarfile.open(archive) as packed:
            packed.extractall(SCRATCH, filter="data")
        package.verify_extracted(extracted, files)
        (extracted / ".venv").symlink_to(ENVIRONMENT, target_is_directory=True)
    assert not (extracted / ".git").exists()
    env = package.check_environment(SCRATCH)
    env.update(PLAYWRIGHT_BROWSERS_PATH=str(BROWSER), UV_OFFLINE="1")
    log = SCRATCH / "finalize.log"
    elapsed = None
    if not verify_existing:
        start = time.monotonic()
        with log.open("w") as output:
            result = subprocess.run([sys.executable, "scripts/finalize.py"], cwd=extracted,
                                    env=env, stdout=output, stderr=subprocess.STDOUT)
        elapsed = round(time.monotonic() - start, 3)
        if result.returncode:
            raise RuntimeError(log.read_text())
    assert log.read_text().rstrip().endswith("FINALIZE OK")
    commands = re.findall(r"^\$ (.+)$", log.read_text(), re.M)
    assert len(commands) == 10, commands
    suites = [int(n) for n in re.findall(r"^Ran (\d+) tests in", log.read_text(), re.M)]
    assert suites == [26, 9, 9, 3], suites
    after = {name: (extracted / name).read_bytes() for name in before}
    changed = sorted(name for name in before if before[name] != after[name])
    allowed = {"SUBMISSION.md", "REPORT.md", "results/process_log_summary.json",
               "SUBMISSION.pdf", "SLIDES.pdf", "results/export_check.json",
               "results/submission_compliance.json", "results/source_check.json",
               "results/reproduction_check.json"}
    assert set(changed) <= allowed, changed
    # Receipt changes must be the expected document/PDF hashes and PDF size only.
    for name in ("results/source_check.json", "results/reproduction_check.json",
                 "results/export_check.json", "results/submission_compliance.json"):
        old, new = json.loads(before[name]), json.loads(after[name])
        hashes = "document_sha256" if "document_sha256" in old else "sha256"
        for artifact in ("SUBMISSION.md", "SUBMISSION.pdf", "SLIDES.pdf"):
            if artifact in new[hashes]:
                assert new[hashes][artifact] == sha(after[artifact])
                new[hashes][artifact] = old[hashes][artifact]
        if "submission_pdf_bytes" in new:
            assert new["submission_pdf_bytes"] == len(after["SUBMISSION.pdf"])
            new["submission_pdf_bytes"] = old["submission_pdf_bytes"]
        assert old == new, name
    for name, pattern in (("SUBMISSION.md", finalize.SUB_RE), ("REPORT.md", finalize.REP_RE)):
        old, n_old = pattern.subn("USAGE-SNAPSHOT", before[name].decode())
        new, n_new = pattern.subn("USAGE-SNAPSHOT", after[name].decode())
        assert n_old == n_new == 1 and old == new, name
    pdfs = {}
    for name in ("SUBMISSION.pdf", "SLIDES.pdf"):
        old, new = PdfReader(io.BytesIO(before[name])), PdfReader(io.BytesIO(after[name]))
        assert len(old.pages) == len(new.pages)
        usage_pages, stream_changes = [], []
        for i, (p, q) in enumerate(zip(old.pages, new.pages), 1):
            p_text, q_text = normal_text(p.extract_text()), normal_text(q.extract_text())
            p_norm, p_n = finalize.SUB_RE.subn("USAGE-SNAPSHOT", p_text)
            q_norm, q_n = finalize.SUB_RE.subn("USAGE-SNAPSHOT", q_text)
            assert p_n == q_n and p_norm == q_norm, (name, i)
            if p_n:
                usage_pages.append(i)
            if p.get_contents().get_data() != q.get_contents().get_data():
                stream_changes.append(i)
        assert set(stream_changes) <= set(usage_pages), (name, stream_changes)
        if name == "SLIDES.pdf":
            normal_dates = lambda raw: re.sub(rb"/(CreationDate|ModDate)\s*\(D:[^)]*\)",
                                              rb"/\1 (normalised)", raw)
            assert normal_dates(before[name]) == normal_dates(after[name])
        pdfs[name] = dict(pages=len(new.pages), usage_pages=usage_pages,
                          changed_content_pages=stream_changes,
                          text_identical_except_usage=True,
                          committed_sha256=sha(before[name]), rebuilt_sha256=sha(after[name]))
    # Neither the rehearsal nor its tests may mutate the production tracked payload.
    assert all((ROOT / name).read_bytes() == data for name, data in production_before.items())
    assert package.git(ROOT, "rev-parse", "HEAD^{commit}").decode().strip() == production_revision
    receipt = dict(ok=True, revision=revision,
        checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        elapsed_seconds=elapsed, tracked_files_checked=len(files),
        input_archive_sha256=sha(archive.read_bytes()),
        command="python scripts/finalize.py", completion_marker="FINALIZE OK",
        verification_resumed=verify_existing, test_suites=suites, tests_passed=sum(suites),
        log=str(log), log_sha256=sha(log.read_bytes()),
        commands=commands,
        changed_archive_paths=changed, all_other_tracked_bytes_unchanged=True,
        markdown_identical_except_usage=True, production_tracked_bytes_unchanged=True,
        production_revision=production_revision,
        pdfs=pdfs, compliance=json.loads(after["results/submission_compliance.json"]),
        usage_before=json.loads(before["results/process_log_summary.json"]),
        usage_after=json.loads(after["results/process_log_summary.json"]),
        environment=dict(python=sys.version, executable=sys.executable, browser=str(BROWSER),
                         uv_lock_sha256=sha(before["uv.lock"]), uv_offline=True),
        scope="Full author-machine finalizer using current machine-local runner logs in a Git archive "
              "without .git; existing iteration-42 dependencies/browser on the same VM, no new install. "
              "No production refresh, new experiment, model call, new scientific analysis, submission, "
              "transfer or access grant. Counts are a rehearsal snapshot, not the later 16:30 snapshot.")
    (SCRATCH / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"REHEARSAL OK: {SCRATCH / 'receipt.json'}", flush=True)


if __name__ == "__main__":
    main()
