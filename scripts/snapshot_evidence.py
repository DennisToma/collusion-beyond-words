"""Rebuild the evidence bundle from EXACT source git commits in evidence/manifest.json.

uv run python scripts/snapshot_evidence.py

Requires the source clones, but writes only to this repository. No experiments,
metrics, model calls or network access. gzip mtime=0 makes stored blobs deterministic.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess

from evidence import ROOT, MANIFEST


def main():
    manifest = json.loads(MANIFEST.read_text())
    for project, config in manifest["projects"].items():
        source = Path(os.environ.get(f"BW_{project.upper()}_ROOT",
                                    str(Path.home() / "collusion" / config["repo"])))
        for relative, entry in config["files"].items():
            raw = subprocess.check_output(["git", "-C", str(source), "show",
                                           f"{config['commit']}:{relative}"])
            digest = hashlib.sha256(raw).hexdigest()
            if entry.get("sha256") and entry["sha256"] != digest:
                raise ValueError(f"Pinned blob mismatch: {project}/{relative}")
            compression = "gzip" if relative.endswith((".json", ".jsonl")) else "none"
            stored = gzip.compress(raw, mtime=0) if compression == "gzip" else raw
            stored_path = f"{project}/{relative}" + (".gz" if compression == "gzip" else "")
            destination = ROOT / "evidence" / stored_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(stored)
            entry.update(sha256=digest, bytes=len(raw), compression=compression,
                         stored_path=stored_path, stored_bytes=len(stored),
                         stored_sha256=hashlib.sha256(stored).hexdigest())
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Copied {sum(len(p['files']) for p in manifest['projects'].values())} "
          "pinned source blobs into evidence/")


if __name__ == "__main__":
    main()
