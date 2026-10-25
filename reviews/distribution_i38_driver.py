"""Recorded iteration-38 archive verification; no experiments or model calls.

Run from the merged repository with its export-enabled Python environment. The
target revision and scratch directory are fixed to this historical check. Reuses
iteration 33's locked Python environment and browser; this is not a fresh install
or an independent operating-system check. Production artifacts are read only.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import time
from datetime import datetime, timezone

from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[1]
REV = "2add728"
SCRATCH = Path("/var/tmp/bw-i38-archive")
PYTHON = Path("/var/tmp/bw-iteration33-release/.venv/bin/python")
BROWSER = Path("/var/tmp/bw-i33-browser")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=REPO)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    revision = git("rev-parse", REV).decode().strip()
    paths = git("ls-tree", "-rz", "--name-only", revision).decode().rstrip("\0").split("\0")
    before = {p: git("show", f"{revision}:{p}") for p in paths}
    assert PYTHON.is_file() and BROWSER.is_dir()
    assert (PYTHON.parent.parent.parent / "uv.lock").read_bytes() == before["uv.lock"]
    SCRATCH.mkdir()  # Refuse to reuse an already-populated verification directory.
    archive = Path(f"/var/tmp/beyond-words-{REV}.tar.gz")
    subprocess.run(["git", "archive", "--format=tar.gz", "--prefix=beyond-words/",
                    f"--output={archive}", revision], cwd=REPO, check=True)
    with tarfile.open(archive) as packed:
        packed.extractall(SCRATCH, filter="data")
    root = SCRATCH / "beyond-words"
    assert not (root / ".git").exists()
    assert sorted(str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()) == sorted(paths)
    assert all((root / p).read_bytes() == before[p] for p in paths)
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    env.update(BW_Q14_ROOT=str(SCRATCH / "absent-q14"),
               BW_Q22_ROOT=str(SCRATCH / "absent-q22"),
               MPLCONFIGDIR=str(SCRATCH / "matplotlib"),
               PLAYWRIGHT_BROWSERS_PATH=str(BROWSER))
    assert not Path(env["BW_Q14_ROOT"]).exists() and not Path(env["BW_Q22_ROOT"]).exists()
    rows = []

    def run(script):
        cmd = [str(PYTHON), script]
        print(f"[{len(rows)+1}] {script}", flush=True)
        log = SCRATCH / f"{len(rows)+1:02d}.log"
        start = time.monotonic()
        with log.open("w") as output:
            result = subprocess.run(cmd, cwd=root, env=env, stdout=output, stderr=subprocess.STDOUT)
        rows.append(dict(command=cmd, exit_code=result.returncode,
                         elapsed_seconds=round(time.monotonic()-start, 3),
                         log_sha256=sha(log.read_bytes())))
        if result.returncode:
            print(log.read_text(), flush=True)
            raise SystemExit(result.returncode)
        print(f"  OK ({rows[-1]['elapsed_seconds']}s)", flush=True)

    # Validate the archived committed PDFs/receipts before changing any output.
    run("scripts/check_submission_compliance.py")
    assert (root / "results/submission_compliance.json").read_bytes() == before["results/submission_compliance.json"]
    replays = ["unrounded_q22", "c21b_floor", "locked_test_q22", "grid_q14", "gate_pcmi_q14", "gate_q14"]
    figures = sorted(p for p in paths if p.startswith("figures/fig") and p.endswith(".png"))
    regenerated = [f"results/{p}.json" for p in replays] + figures
    for path in regenerated:
        (root / path).unlink()
    for name in replays:
        run(f"scripts/recompute_{name}.py")
    for name in ("fig1_hard_negatives", "fig2_level_vs_comovement", "fig3_e70_grid",
                 "fig4_say_vs_do", "fig5_placebo_premium", "fig6_strong_framing"):
        run(f"scripts/{name}.py")
    for script in ("scripts/check_sources.py", "scripts/number_coverage.py", "tests/test_reproduction.py",
                   "scripts/export_pdf.py", "tests/test_export.py", "scripts/check_submission_compliance.py",
                   "tests/test_submission_compliance.py"):
        run(script)
    after = {p: (root / p).read_bytes() for p in paths}
    assert all(before[p] == after[p] for p in regenerated)
    changed = sorted(p for p in paths if before[p] != after[p])
    assert set(changed) <= {"SUBMISSION.pdf", "SLIDES.pdf", "results/export_check.json",
                            "results/submission_compliance.json"}, changed
    pdfs = {}
    for name in ("SUBMISSION.pdf", "SLIDES.pdf"):
        old, new = PdfReader(io.BytesIO(before[name])), PdfReader(io.BytesIO(after[name]))
        assert len(old.pages) == len(new.pages)
        assert [p.extract_text() for p in old.pages] == [p.extract_text() for p in new.pages]
        assert [p.get_contents().get_data() for p in old.pages] == [p.get_contents().get_data() for p in new.pages]
        normalise = lambda data: re.sub(rb"/(CreationDate|ModDate)\s*\(D:[^)]*\)", rb"/\1 (normalised)", data)
        assert normalise(before[name]) == normalise(after[name]), name
        pdfs[name] = dict(pages=len(new.pages), page_text_identical=True, content_streams_identical=True,
                          byte_identical_after_date_normalisation=True,
                          committed_sha256=sha(before[name]), rebuilt_sha256=sha(after[name]))
    # Receipts may differ only where they bind the two rebuilt PDF hashes.
    for name in ("results/export_check.json", "results/submission_compliance.json"):
        old, new = json.loads(before[name]), json.loads(after[name])
        for pdf in pdfs:
            assert new["sha256"][pdf] == sha(after[pdf])
            new["sha256"][pdf] = old["sha256"][pdf]
        assert old == new, name
    read = lambda name: json.loads(after[f"results/{name}.json"])
    source, repro, export, export_tests, compliance, coverage = [read(name) for name in
        ("source_check", "reproduction_check", "export_check", "export_test", "submission_compliance", "number_coverage")]
    assert all((REPO / p).read_bytes() == before[p] for p in paths), "Production tree changed during check"
    receipt = dict(
        checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), revision=revision,
        archive=str(archive), archive_sha256=sha(archive.read_bytes()), archive_bytes=archive.stat().st_size,
        tracked_files_verified=len(paths), no_git_directory=True, all_extracted_files_match_git_blobs=True,
        environment=dict(python=str(PYTHON), python_version=subprocess.check_output([str(PYTHON), "--version"], text=True).strip(),
                         uv_lock_sha256=sha(before["uv.lock"]), fresh_dependencies=False,
                         browser=str(BROWSER), fresh_browser=False, sibling_root_overrides="nonexistent paths",
                         model_environment_variables="not passed", scope="Same author VM; HOME unchanged; no OS/filesystem sandbox."),
        commands=rows, deleted_and_regenerated_byte_identical={p: sha(after[p]) for p in regenerated},
        checks={k: source[k] for k in ("n_checks", "n_document_checks", "n_evidence_files", "n_fail", "n_document_fail")},
        unclassified_decimals={p: coverage[p]["unbound_unclassified"] for p in ("SUBMISSION.md", "SLIDES.md")},
        reproduction_tests={k: repro[k] for k in ("n_tests", "n_fail", "n_errors")},
        export_tests={k: export_tests[k] for k in ("n_tests", "n_fail", "n_errors")},
        compliance_tests=dict(n_tests=3, exit_code=rows[-1]["exit_code"]),
        export={k: export[k] for k in ("ok", "submission_pages", "slides", "submission_text_fragments", "slide_text_fragments", "figure_counts")},
        compliance=compliance, pdfs=pdfs, changed_archive_paths=changed,
        all_other_archived_files_byte_identical=True, production_files_unchanged=True,
        scope="Verification of the post-compliance frozen release; no experiments, model calls, labels, settings or held-out evaluation. Runner-log refresh excluded. Archive not transferred; reader access not granted.")
    receipt_path = SCRATCH / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"PASS: {receipt_path}", flush=True)


if __name__ == "__main__":
    main()
