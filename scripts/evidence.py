"""Read the pinned, portable source evidence; never run experiments or model calls."""
import gzip
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "evidence" / "manifest.json"


class Evidence:
    def __init__(self, live=False):
        self.manifest = json.loads(MANIFEST.read_text())
        self.live = live
        self.read_files = set()

    def read_bytes(self, project, relative):
        entry = self.manifest["projects"][project]["files"][relative]
        if self.live:
            name = self.manifest["projects"][project]["repo"]
            root = Path(os.environ.get(f"BW_{project.upper()}_ROOT",
                                       str(Path.home() / "collusion" / name)))
            raw = (root / relative).read_bytes()
        else:
            stored = (ROOT / "evidence" / entry["stored_path"]).read_bytes()
            if hashlib.sha256(stored).hexdigest() != entry["stored_sha256"]:
                raise ValueError(f"Stored evidence changed: {project}/{relative}")
            raw = gzip.decompress(stored) if entry["compression"] == "gzip" else stored
        if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
            raise ValueError(f"Source evidence changed: {project}/{relative}")
        self.read_files.add((project, relative))
        return raw

    def json(self, project, relative):
        return json.loads(self.read_bytes(project, relative))

    def lines(self, project, relative):
        return self.read_bytes(project, relative).decode().splitlines()

    def verify(self):
        for project, config in self.manifest["projects"].items():
            for relative in config["files"]:
                self.read_bytes(project, relative)
        return len(self.read_files)
