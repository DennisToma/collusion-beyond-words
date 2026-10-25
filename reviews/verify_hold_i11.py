"""Read-only final source/payload freshness check; not an experiment.

Run on the author VM: uv run python reviews/verify_hold_i11.py
Requires sibling Git histories. Writes only results/release_hold_i11.json here.
"""
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_code_zip import git


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    manifest = json.loads((ROOT / "evidence/manifest.json").read_text())
    projects = {}
    baselines = {"q14": "0708b80", "q22": "f15abfd"}
    allowed = {"q14": {"STATUS.md"},
               "q22": {"STATUS.md", "results/analysis/merge_flags.md"}}
    for name, project in manifest["projects"].items():
        repo = ROOT.parent / project["repo"]
        head = git(repo, "rev-parse", "HEAD").decode().strip()
        require(not git(repo, "status", "--porcelain").strip(), f"Dirty source: {name}")
        baseline = git(repo, "rev-parse", baselines[name]).decode().strip()
        changed = git(repo, "diff", "--name-only", baseline, head).decode().splitlines()
        require(set(changed) <= allowed[name], f"Unreviewed source delta: {name}: {changed}")
        hashes = {}
        for path, entry in project["files"].items():
            original = git(repo, "show", f"{project['commit']}:{path}")
            stored = (ROOT / "evidence" / entry["stored_path"]).read_bytes()
            require(sha(original) == entry["sha256"], f"Pin mismatch: {name}/{path}")
            require(sha(stored) == entry["stored_sha256"], f"Stored mismatch: {name}/{path}")
            unpacked = gzip.decompress(stored) if entry["compression"] == "gzip" else stored
            require(unpacked == original, f"Evidence mismatch: {name}/{path}")
            hashes[path] = sha(original)
        status = git(repo, "show", f"{head}:STATUS.md").decode()
        require("P1 OPEN: 0" in status[:1000] or "P1 open: 0" in status[:1000],
                f"Source no longer declares zero open P1: {name}")
        projects[name] = dict(head=head, previous_handoff=baseline,
                              changed_paths=changed, pin=project["commit"],
                              pin_hashes=hashes, status_sha256=sha(status.encode()))
        require(git(repo, "rev-parse", "HEAD").decode().strip() == head,
                f"Source advanced during check: {name}")

    earlier = json.loads((ROOT / "results/primary_preservation_fallback_i7.json").read_text())
    preserved = {}
    for entry in earlier["preserved_files"]:
        digest = sha((ROOT / entry["path"]).read_bytes())
        require(digest == entry["sha256"], f"Scientific payload changed: {entry['path']}")
        preserved[entry["path"]] = digest
    accepted = git(ROOT, "rev-parse", "77ab10d").decode().strip()
    artifacts = {}
    for path in ("TEMPLATE_REPORT.md", "TEMPLATE_REPORT.pdf", "SLIDES.md", "SLIDES.pdf",
                 "SUBMISSION.md", "SUBMISSION.pdf", "SUBMISSION_FORM.md", "IMAGE.png"):
        data = (ROOT / path).read_bytes()
        require(data == git(ROOT, "show", f"{accepted}:{path}"), f"Accepted artifact changed: {path}")
        artifacts[path] = dict(sha256=sha(data), bytes=len(data))
    receipt = dict(ok=True, checked_at_utc=datetime.now(timezone.utc).isoformat(),
                   merge_input_head=git(ROOT, "rev-parse", "HEAD").decode().strip(),
                   accepted_artifact_revision=accepted, projects=projects,
                   preserved_files=preserved, artifacts=artifacts,
                   scope="Source tracked changes since the prior handoff are restricted to reviewed "
                   "status/review notes; every evidence blob matches its pin. Source status declares "
                   "zero open P1; this is not a new independent scope review. Scientific payload and "
                   "accepted upload bytes are unchanged. No experiments, model calls, exports or usage refresh.")
    (ROOT / "results/release_hold_i11.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(f"HOLD OK: {sum(len(p['pin_hashes']) for p in projects.values())} evidence pins; "
          f"{len(preserved)} preserved files; {len(artifacts)} accepted artifacts")


if __name__ == "__main__":
    main()
