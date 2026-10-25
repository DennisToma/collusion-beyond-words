"""Build submission_code.zip (the form's "Project code" upload) from committed HEAD.

  uv run python scripts/build_code_zip.py [--out /var/tmp/submission_code.zip]

Layout: beyond-words/ = git archive of this repo's HEAD; sources/*.tar.xz = git archives of
the two source repos at the evidence pins (evidence/manifest.json), minus files > 5 MB and
rendered HTML (listed in the README).
Fails if the worktree is dirty, the zip exceeds 25 MB, or a secret pattern matches.
"""
import argparse
import io
import hashlib
import json
import lzma
import os
import re
import subprocess
import tarfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SIB = ROOT.parent
SOURCES = {  # name -> (local checkout, pinned commit from evidence/manifest.json)
    "q14-infotheory": (SIB / "collusion-14-infotheory", "732f08c11a765cd8500f4ef3c29fb630b309d5b2"),
    "q22-say-vs-do": (SIB / "collusion-22-say-vs-do", "91ffb2d4737a7537cdf9afe239a98e0d1061090b"),
}
MAX_FILE = 5_000_000
MAX_ZIP = 25_000_000
# patterns assembled from parts so this file does not match itself
SECRET = re.compile(b"sk-" + rb"[A-Za-z0-9_-]{20,}|API_KEY\s*=\s*[A-Za-z0-9_-]{16,}|" + b"PRIVATE" + b" KEY-----")

README = """# Beyond Words — submission code archive

Layout
- `beyond-words/` — the merged submission repo at commit {head}: TEMPLATE_REPORT/SUBMISSION sources,
  figure scripts, release checks and `evidence/` (158 exact files pinned from the two source repos,
  SHA256 in `evidence/manifest.json`).
- `sources/q14-infotheory-{q14}.tar.xz` — git archive of the Q1.4 prices-only market and
  information-theoretic detectors at `{q14}` (unpack: `tar -xJf ...`).
- `sources/q22-say-vs-do-{q22}.tar.xz` — git archive of the Q2.2 say-vs-do market and text/action
  auditors at `{q22}`.

Replay the saved calculations, regenerate all seven figures and the project image in
temporary copies, and check the documented numeric bindings and primary PDF (no model
calls, no API keys or browser installation needed; numeric coverage limits are in README):

    cd beyond-words && uv run --group export python scripts/finalize.py --no-export

The source repos each have their own reproduce section (Q1.4 REPORT §6; Q2.2 REPORT Appendix E).
The repository https://github.com/DennisToma/collusion-beyond-words will be made public after the
submission deadline.

Excluded: tracked files over 5 MB (scripted positive-control trajectories that the generators
re-create from their seeds) and rendered HTML reports (the .md sources and PDFs are included; the exporters re-create HTML):
{excluded}
"""


def git(repo, *args):
    # Keep caller Git overrides/credentials out of both release and source reads.
    env = {key: os.environ[key] for key in ("PATH", "HOME", "LANG", "LC_ALL", "TMPDIR") if key in os.environ}
    return subprocess.check_output(["git", *args], cwd=repo, env=env)


def filtered_files(repo, rev):
    """Expected regular-file bytes, read independently from the committed Git archive."""
    with tarfile.open(fileobj=io.BytesIO(git(repo, "archive", "--format=tar", rev))) as packed:
        return {m.name: packed.extractfile(m).read() for m in packed
                if m.isfile() and m.size <= MAX_FILE and not m.name.endswith(".html")}


def verify_code_zip(path, repo, revision, sources):
    """Reject stale, omitted, extra or corrupted committed files, including inside sources/."""
    if path.stat().st_size > MAX_ZIP:
        raise ValueError("zip exceeds 25 MB")
    counts = {}
    with zipfile.ZipFile(path) as zf:
        if zf.testzip() is not None or len(zf.namelist()) != len(set(zf.namelist())):
            raise ValueError("Corrupt or duplicate ZIP member")
        expected = filtered_files(repo, revision)
        expected_names = {"beyond-words/" + name for name in expected} | {"README.md"}
        for name, data in expected.items():
            if zf.read("beyond-words/" + name) != data:
                raise ValueError(f"ZIP differs from committed release: {name}")
        counts["beyond-words"] = len(expected)
        for name, (source_repo, pin) in sources.items():
            member = f"sources/{name}-{pin[:7]}.tar.xz"
            expected_names.add(member)
            expected_source = {f"{name}/{p}": data for p, data in filtered_files(source_repo, pin).items()}
            with tarfile.open(fileobj=io.BytesIO(zf.read(member)), mode="r:xz") as packed:
                members = [m for m in packed if not m.isdir()]
                if (len(members) != len(expected_source) or len({m.name for m in members}) != len(members)
                        or any(not m.isfile() or m.name not in expected_source for m in members)):
                    raise ValueError(f"Source archive membership mismatch: {name}")
                for m in members:
                    if packed.extractfile(m).read() != expected_source[m.name]:
                        raise ValueError(f"Source archive differs from pin: {m.name}")
            counts[name] = len(expected_source)
        if set(zf.namelist()) != expected_names or revision not in zf.read("README.md").decode():
            raise ValueError("ZIP membership or README revision mismatch")
    return dict(revision=revision, bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(), files=counts,
                source_pins={name: pin for name, (_, pin) in sources.items()})


def add_archive(zf, repo, rev, prefix, excluded):
    tar = tarfile.open(fileobj=io.BytesIO(git(repo, "archive", "--format=tar", rev)))
    n = 0
    for m in tar.getmembers():
        if not m.isfile():
            continue
        if m.size > MAX_FILE or m.name.endswith(".html"):
            excluded.append(f"- `{prefix}{m.name}` ({m.size / 1e6:.1f} MB)")
            continue
        data = tar.extractfile(m).read()
        if SECRET.search(data):
            raise SystemExit(f"secret pattern in {prefix}{m.name}")
        zf.writestr(prefix + m.name, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        n += 1
    return n


def add_source_tarball(zf, repo, rev, name, excluded):
    """Filtered git archive as one .tar.xz (xz dedups the many near-identical JSONL files)."""
    src = tarfile.open(fileobj=io.BytesIO(git(repo, "archive", "--format=tar", f"--prefix={name}/", rev)))
    buf = io.BytesIO()
    n = 0
    with tarfile.open(fileobj=buf, mode="w") as dst:
        for m in src.getmembers():
            if m.isfile():
                if m.size > MAX_FILE or m.name.endswith(".html"):
                    excluded.append(f"- `sources/{m.name}` ({m.size / 1e6:.1f} MB)")
                    continue
                data = src.extractfile(m).read()
                if SECRET.search(data):
                    raise SystemExit(f"secret pattern in sources/{m.name}")
                dst.addfile(m, io.BytesIO(data))
                n += 1
            elif m.isdir():
                dst.addfile(m)
    zf.writestr(f"sources/{name}-{rev[:7]}.tar.xz", lzma.compress(buf.getvalue(), preset=9 | lzma.PRESET_EXTREME),
                compress_type=zipfile.ZIP_STORED)
    return n


def build(repo, out, sources=None):
    repo, out = Path(repo), Path(out)
    sources = SOURCES if sources is None else sources
    if git(repo, "status", "--porcelain").strip():
        raise ValueError("Commit all changes before building ZIP; worktree is dirty")
    head = git(repo, "rev-parse", "HEAD").decode().strip()
    manifest = json.loads(git(repo, "show", f"{head}:evidence/manifest.json"))
    project_keys = {"q14-infotheory": "q14", "q22-say-vs-do": "q22"}
    if any(pin != manifest["projects"][project_keys[name]]["commit"] for name, (_, pin) in sources.items()):
        raise ValueError("Source archive pins differ from the committed evidence manifest")
    excluded = []
    tmp = out.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w") as zf:
        counts = {"beyond-words": add_archive(zf, repo, head, "beyond-words/", excluded)}
        for name, (source_repo, rev) in sources.items():
            counts[name] = add_source_tarball(zf, source_repo, rev, name, excluded)
        zf.writestr("README.md", README.format(
            head=head, q14=sources["q14-infotheory"][1][:7], q22=sources["q22-say-vs-do"][1][:7],
            excluded="\n".join(sorted(set(excluded))) or "- none"))
    receipt = verify_code_zip(tmp, repo, head, sources)
    if git(repo, "rev-parse", "HEAD").decode().strip() != head or git(repo, "status", "--porcelain").strip():
        raise ValueError("Release changed while building ZIP")
    os.replace(tmp, out)
    print(f"{out}: {receipt['bytes'] / 1e6:.1f} MB, files {counts}, excluded {len(set(excluded))}")
    return receipt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "submission_code.zip"))
    build(ROOT, Path(ap.parse_args().out))


if __name__ == "__main__":
    main()
