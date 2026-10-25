"""Verify and package the committed release without changing the author checkout.

Run after finalize.py, committing its outputs first:
  uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-release

Requires the existing export dependencies and installed Chromium. Uses an extracted
Git archive, absent sibling roots and no model environment variables. Does not
refresh runner logs, rebuild the PDFs, submit files or change repository access.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time

import build_code_zip

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    "scripts/check_sources.py",
    "scripts/number_coverage.py",
    "scripts/check_template_numbers.py",
    "scripts/check_template_artifacts.py",
    "scripts/check_submission_compliance.py",
    "scripts/check_committed_export.py",
    "tests/test_reproduction.py",
    "tests/test_export.py",
    "tests/test_submission_compliance.py",
    "tests/test_packaging.py",
    "tests/test_template_artifacts.py",
)
UPLOADS = ("TEMPLATE_REPORT.pdf", "IMAGE.png", "SUBMISSION.pdf", "SLIDES.pdf", "SUBMISSION_FORM.md")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def local_environment():
    return {k: os.environ[k] for k in
            ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR", "PLAYWRIGHT_BROWSERS_PATH")
            if k in os.environ}


def git(repo, *args):
    return subprocess.check_output(["git", *args], cwd=repo, env=local_environment())


def clean_head(repo):
    if git(repo, "status", "--porcelain", "--untracked-files=all").strip():
        raise ValueError("Commit all changes before packaging; the worktree must be clean")
    return git(repo, "rev-parse", "HEAD^{commit}").decode().strip()


def tree_files(repo, revision):
    files = {}
    for row in git(repo, "ls-tree", "-rz", revision).split(b"\0"):
        if not row:
            continue
        info, raw_path = row.split(b"\t", 1)
        mode, kind, oid = info.decode().split()
        path = raw_path.decode()
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise ValueError(f"Release supports regular tracked files only: {path}")
        parts = PurePosixPath(path).parts
        if PurePosixPath(path).is_absolute() or any(p in {"..", ".git"} for p in parts):
            raise ValueError(f"Unexpected tracked path: {path}")
        data = git(repo, "cat-file", "blob", oid)
        files[path] = dict(sha256=sha(data), bytes=len(data), mode=mode)
    return files


def verify_archive(archive, files):
    """Check every member before extraction, including omissions and duplicates."""
    seen = set()
    with tarfile.open(archive, "r:gz") as packed:
        for member in packed:
            parts = PurePosixPath(member.name).parts
            if (not parts or parts[0] != "beyond-words" or
                    PurePosixPath(member.name).is_absolute() or
                    any(p in {"..", ".git"} for p in parts)):
                raise ValueError(f"Unsafe archive member: {member.name}")
            if member.isdir():
                continue
            relative = "/".join(parts[1:])
            if not member.isfile() or relative not in files or relative in seen:
                raise ValueError(f"Unexpected/duplicate archive member: {member.name}")
            expected = files[relative]
            data = packed.extractfile(member).read()
            mode = int(expected["mode"], 8) & 0o777
            if len(data) != expected["bytes"] or sha(data) != expected["sha256"] or member.mode != mode:
                raise ValueError(f"Archive differs from Git: {relative}")
            seen.add(relative)
    if seen != files.keys():
        raise ValueError(f"Archive omits tracked files: {sorted(files.keys() - seen)}")


def verify_extracted(root, files):
    if (root / ".git").exists():
        raise ValueError("Extracted release contains .git")
    for path, expected in files.items():
        target = root / path
        if (target.is_symlink() or not target.is_file() or
                sha(target.read_bytes()) != expected["sha256"] or
                target.stat().st_mode & 0o777 != int(expected["mode"], 8) & 0o777):
            raise ValueError(f"Extracted file differs from Git: {path}")


def check_environment(scratch):
    # Browser selection is not a model credential. HOME is retained for a normal
    # Playwright install; this does not constitute OS/filesystem isolation.
    env = local_environment()
    env.update(BW_Q14_ROOT=str(scratch / "absent-q14"),
               BW_Q22_ROOT=str(scratch / "absent-q22"),
               MPLCONFIGDIR=str(scratch / "matplotlib"), PYTHONDONTWRITEBYTECODE="1")
    return env


def run_checks(root, logs, env):
    logs.mkdir()
    rows = []
    for i, script in enumerate(CHECKS, 1):
        print(f"[{i}/{len(CHECKS)}] {script}", flush=True)
        log = logs / f"{i:02d}-{Path(script).stem}.log"
        start = time.monotonic()
        with log.open("w") as output:
            result = subprocess.run([sys.executable, script], cwd=root, env=env,
                                    stdout=output, stderr=subprocess.STDOUT)
        if result.returncode:
            raise ValueError(f"Release check failed: {script}\n{log.read_text()}")
        rows.append(dict(script=script, exit_code=result.returncode,
                         elapsed_seconds=round(time.monotonic() - start, 3),
                         log=f"logs/{log.name}", log_sha256=sha(log.read_bytes())))
    return rows


def package(repo, output):
    repo, output = Path(repo).resolve(), Path(output).resolve()
    if output == repo or repo in output.parents:
        raise ValueError("Package output must be outside the repository")
    if output.exists():
        raise ValueError("Package output already exists; choose an unused directory")
    revision = clean_head(repo)
    files = tree_files(repo, revision)
    if not all(path in files for path in (*UPLOADS, *CHECKS, "uv.lock")):
        raise ValueError("Committed revision is missing release files/checks")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Nothing is advertised as ready until every check passes. The temporary
    # extraction is kept out of the finished upload directory and then removed.
    with tempfile.TemporaryDirectory(prefix=".bw-package-", dir=output.parent) as temp:
        scratch = Path(temp)
        ready = scratch / "ready"
        ready.mkdir()
        archive = ready / f"beyond-words-{revision[:12]}.tar.gz"
        subprocess.run(["git", "-c", "tar.umask=0022", "archive", "--format=tar.gz", "--prefix=beyond-words/",
                        f"--output={archive}", revision], cwd=repo, env=local_environment(), check=True)
        verify_archive(archive, files)
        with tarfile.open(archive, "r:gz") as packed:
            packed.extractall(scratch / "extracted", filter="data")
        extracted = scratch / "extracted/beyond-words"
        verify_extracted(extracted, files)
        rows = run_checks(extracted, ready / "logs", check_environment(scratch))
        verify_extracted(extracted, files)
        for path in UPLOADS:
            shutil.copyfile(extracted / path, ready / path)
        code_zip = ready / "submission_code.zip"
        code_receipt = build_code_zip.build(repo, code_zip)
        artifacts = {p.name: dict(sha256=sha(p.read_bytes()), bytes=p.stat().st_size)
                     for p in (archive, code_zip, *(ready / name for name in UPLOADS))}
        compliance = json.loads((extracted / "results/submission_compliance.json").read_text())
        receipt = dict(
            revision=revision, checked_at_utc=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            ok=True, tracked_files_verified=len(files), files=files, artifacts=artifacts, commands=rows,
            python=sys.version, uv_lock_sha256=files["uv.lock"]["sha256"], compliance=compliance,
            code_zip=code_receipt,
            scope="Committed archive matches Git; all listed checks pass without .git, with absent sibling roots "
                  "and no model environment variables passed. Existing Python/browser on the same VM; HOME retained, "
                  "no OS sandbox. No PDF rebuild, runner-log refresh, new dependency install, experiment, "
                  "submission, transfer or access grant. Receipt/logs/checksums are outside the archive.")
        (ready / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        (ready / "HANDOFF.md").write_text(
            f"# Beyond Words handoff\n\nVerified committed revision: `{revision}`.\n\n"
            "Upload `TEMPLATE_REPORT.pdf` as the primary report, `IMAGE.png` as the project image, "
            "and `submission_code.zip` in the Project code field; use `SUBMISSION_FORM.md` for form fields. "
            "Upload `SUBMISSION.pdf` and `SLIDES.pdf` as optional supplements if the form permits them. "
            "Check local file integrity with `sha256sum -c SHA256SUMS` in this directory. "
            "The archive extracts to `beyond-words/`; its README gives reproduction instructions.\n\n"
            "`receipt.json` records Git file hashes and the checks run from the extraction; `logs/` holds "
            "their outputs. These verification files accompany the archive. "
            "No form was submitted, archive transferred or reader access granted. "
            "If finalization or other edits change the release, commit them and package again into a new directory.\n")
        paths = sorted(p for p in ready.rglob("*") if p.is_file())
        (ready / "SHA256SUMS").write_text("".join(
            f"{sha(p.read_bytes())}  {p.relative_to(ready).as_posix()}\n" for p in paths))
        # Detect a concurrent author/runner commit or edit before publishing.
        if clean_head(repo) != revision:
            raise ValueError("HEAD changed while packaging; retry after committing the final release")
        ready.rename(output)
    print(f"PACKAGE OK: {output}\nrevision: {revision}", flush=True)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        package(ROOT, args.output_dir)
    except (ValueError, OSError, subprocess.CalledProcessError, tarfile.TarError) as error:
        raise SystemExit(f"PACKAGE FAILED: {error}") from error


if __name__ == "__main__":
    main()
