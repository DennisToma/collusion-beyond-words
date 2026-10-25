"""Handoff failures must not publish a package of stale or altered files.

Uses tiny temporary Git repositories and calculator scripts, never experiments.
uv run python tests/test_packaging.py
"""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import package_release as release


class PackagingChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="bw-package-test-", dir="/var/tmp")
        self.scratch = Path(self.temp.name)
        self.repo = self.scratch / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        self.git("config", "user.email", "fixture@example.invalid")
        self.git("config", "user.name", "Packaging fixture")
        self.git("config", "commit.gpgsign", "false")
        for path in (*release.CHECKS, *release.UPLOADS, "uv.lock", "results/submission_compliance.json"):
            target = self.repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("pass\n" if path.endswith(".py") else "{}\n")
        self.commit()
        self.output = self.scratch / "handoff"

    def tearDown(self):
        self.temp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.repo, stderr=subprocess.STDOUT,
                                       env=release.local_environment())

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-qm", "fixture")

    def test_package_matches_git_uploads_checksums_and_is_repeatable(self):
        receipt = release.package(self.repo, self.output)
        revision = self.git("rev-parse", "HEAD").decode().strip()
        self.assertEqual(receipt["revision"], revision)
        self.assertEqual(len(receipt["commands"]), len(release.CHECKS))
        self.assertEqual(receipt["tracked_files_verified"], len(receipt["files"]))
        self.assertEqual(json.loads((self.output / "receipt.json").read_text()), receipt)
        for path in release.UPLOADS:
            self.assertEqual((self.output / path).read_bytes(), self.git("show", f"HEAD:{path}"))
        for row in (self.output / "SHA256SUMS").read_text().splitlines():
            checksum, path = row.split("  ", 1)
            self.assertEqual(hashlib.sha256((self.output / path).read_bytes()).hexdigest(), checksum)
        archive = next(self.output.glob("*.tar.gz"))
        release.verify_archive(archive, release.tree_files(self.repo, revision))
        with tarfile.open(archive) as packed:
            self.assertTrue(all(".git" not in Path(p.name).parts for p in packed))
        other = self.scratch / "another"
        release.package(self.repo, other)
        self.assertEqual(archive.read_bytes(), (other / archive.name).read_bytes())
        self.assertFalse(self.git("status", "--porcelain").strip())
        self.assertFalse(list(self.scratch.glob(".bw-package-*")))

    def test_dirty_tracked_staged_and_untracked_files_are_rejected(self):
        for kind in ("tracked", "staged", "untracked"):
            with self.subTest(kind=kind):
                path = self.repo / ("extra" if kind == "untracked" else "SUBMISSION.pdf")
                path.write_text("pending finalization\n")
                if kind == "staged":
                    self.git("add", "SUBMISSION.pdf")
                with self.assertRaisesRegex(ValueError, "Commit all changes"):
                    release.package(self.repo, self.output)
                self.assertFalse(self.output.exists())
                self.git("reset", "--hard", "HEAD")
                if kind == "untracked":
                    path.unlink()

    def test_output_inside_repo_or_existing_directory_is_rejected(self):
        for output in (self.repo, self.repo / "handoff", self.scratch):
            with self.subTest(output=output), self.assertRaises(ValueError):
                release.package(self.repo, output)

    def test_modified_missing_extra_duplicate_and_unsafe_members_are_rejected(self):
        files = {"file": dict(sha256=release.sha(b"original"), bytes=8, mode="100644")}
        good = ("beyond-words/file", b"original", tarfile.REGTYPE, 0o644)
        bad_rows = (
            [(good[0], b"modified", good[2], good[3])], [],
            [good, ("beyond-words/extra", b"x", tarfile.REGTYPE, 0o644)], [good, good],
            [("beyond-words/../escape", b"x", tarfile.REGTYPE, 0o644)],
            [("beyond-words/.git/config", b"x", tarfile.REGTYPE, 0o644)],
            [(good[0], b"", tarfile.SYMTYPE, 0o644)],
            [(good[0], good[1], good[2], 0o755)],
        )
        for i, rows in enumerate(bad_rows):
            archive = self.scratch / f"bad-{i}.tar.gz"
            with tarfile.open(archive, "w:gz") as packed:
                for name, data, kind, mode in rows:
                    member = tarfile.TarInfo(name)
                    member.size, member.type, member.mode = len(data), kind, mode
                    packed.addfile(member, io.BytesIO(data))
            with self.subTest(i=i), self.assertRaises(ValueError):
                release.verify_archive(archive, files)

    def test_failed_check_publishes_no_package(self):
        (self.repo / release.CHECKS[0]).write_text("raise SystemExit(3)\n")
        self.commit()
        with self.assertRaisesRegex(ValueError, "Release check failed"):
            release.package(self.repo, self.output)
        self.assertFalse(self.output.exists())

    def test_concurrent_worktree_and_head_changes_are_rejected(self):
        def change(root, logs, env):
            (self.repo / "SUBMISSION.pdf").write_text("new finalization\n")
            if commit:
                self.commit()
            return []
        for commit in (False, True):
            with self.subTest(commit=commit), patch.object(release, "run_checks", side_effect=change):
                with self.assertRaisesRegex(ValueError, "Commit all changes|HEAD changed"):
                    release.package(self.repo, self.output)
            self.assertFalse(self.output.exists())
            self.git("reset", "--hard", "HEAD")

    def test_a_check_cannot_silently_modify_archived_release_files(self):
        def change(root, logs, env):
            (root / "SUBMISSION.pdf").write_text("altered PDF\n")
            return []
        with patch.object(release, "run_checks", side_effect=change):
            with self.assertRaisesRegex(ValueError, "Extracted file differs"):
                release.package(self.repo, self.output)
        self.assertFalse(self.output.exists())

    def test_export_ignore_and_symlink_are_not_silently_omitted(self):
        (self.repo / ".gitattributes").write_text("SUBMISSION.pdf export-ignore\n")
        self.commit()
        with self.assertRaisesRegex(ValueError, "Archive omits tracked"):
            release.package(self.repo, self.output)
        self.assertFalse(self.output.exists())
        (self.repo / "link").symlink_to("SUBMISSION.pdf")
        self.commit()
        with self.assertRaisesRegex(ValueError, "regular tracked files"):
            release.package(self.repo, self.output)

    def test_checks_do_not_receive_model_environment_variables(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "synthetic-test-only", "BW_Q14_ROOT": "/existing"}):
            env = release.check_environment(self.scratch)
            with patch.object(release.subprocess, "check_output", return_value=b"") as call:
                release.git(self.repo, "status", "--porcelain")
            self.assertNotIn("OPENAI_API_KEY", call.call_args.kwargs["env"])
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertFalse(Path(env["BW_Q14_ROOT"]).exists())
        self.assertFalse(Path(env["BW_Q22_ROOT"]).exists())
        foreign = self.scratch / "foreign"
        foreign.mkdir()
        def foreign_git(*args):
            return subprocess.check_output(["git", *args], cwd=foreign, env=release.local_environment(),
                                           stderr=subprocess.STDOUT)
        foreign_git("init", "-q")
        (foreign / "marker").write_text("foreign worktree must remain unchanged\n")
        foreign_git("add", "marker")
        foreign_git("-c", "user.name=Foreign fixture", "-c", "user.email=fixture@example.invalid",
                    "-c", "commit.gpgsign=false", "commit", "-qm", "foreign")
        paths = (".git/HEAD", ".git/index", ".git/config", "marker")
        before = {p: (foreign / p).read_bytes() for p in paths}
        foreign_head = foreign_git("rev-parse", "HEAD")
        with patch.dict(os.environ, dict(GIT_DIR=str(foreign / ".git"), GIT_WORK_TREE=str(foreign),
                                        GIT_INDEX_FILE=str(foreign / ".git/index"))):
            self.git("init", "-q")
            self.git("config", "fixture.guard", "isolated")
            self.git("reset", "--hard", "HEAD")
            self.git("commit", "--allow-empty", "-qm", "must be local")
        self.assertEqual({p: (foreign / p).read_bytes() for p in paths}, before)
        self.assertEqual(foreign_git("rev-parse", "HEAD"), foreign_head)


if __name__ == "__main__":
    unittest.main(verbosity=2)
