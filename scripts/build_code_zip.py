"""Build submission_code.zip (the form's "Project code" upload) from committed HEAD.

  uv run python scripts/build_code_zip.py [--out /var/tmp/submission_code.zip]

Layout: beyond-words/ = git archive of this repo's HEAD; sources/*.tar.xz = git archives of
the two source repos at the evidence pins (evidence/manifest.json), minus files > 5 MB and
rendered HTML (listed in the README).
Fails if the worktree is dirty, the zip exceeds 25 MB, or a secret pattern matches.
"""
import argparse
import io
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

Regenerate every figure and check every printed number (no model calls, no API keys needed):

    cd beyond-words && uv run python scripts/finalize.py --no-export

The source repos each have their own reproduce section (Q1.4 REPORT §6; Q2.2 REPORT Appendix E).
The repository https://github.com/DennisToma/collusion-beyond-words will be made public after the
submission deadline.

Excluded: tracked files over 5 MB (scripted positive-control trajectories that the generators
re-create from their seeds) and rendered HTML reports (the .md sources and PDFs are included; the exporters re-create HTML):
{excluded}
"""


def git(repo, *args):
    return subprocess.check_output(["git", *args], cwd=repo)


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "submission_code.zip"))
    out = Path(ap.parse_args().out)
    if git(ROOT, "status", "--porcelain").strip():
        raise SystemExit("commit first: worktree is dirty")
    head = git(ROOT, "rev-parse", "--short", "HEAD").decode().strip()
    excluded = []
    tmp = out.with_suffix(".tmp")
    with zipfile.ZipFile(tmp, "w") as zf:
        counts = {"beyond-words": add_archive(zf, ROOT, "HEAD", "beyond-words/", excluded)}
        for name, (repo, rev) in SOURCES.items():
            counts[name] = add_source_tarball(zf, repo, rev, name, excluded)
        zf.writestr("README.md", README.format(
            head=head, q14=SOURCES["q14-infotheory"][1][:7], q22=SOURCES["q22-say-vs-do"][1][:7],
            excluded="\n".join(sorted(set(excluded))) or "- none"))
    os.replace(tmp, out)
    size = out.stat().st_size
    with zipfile.ZipFile(out) as zf:
        assert zf.testzip() is None
    print(f"{out}: {size / 1e6:.1f} MB, files {counts}, excluded {len(set(excluded))}")
    if size > MAX_ZIP:
        raise SystemExit("zip exceeds 25 MB")


if __name__ == "__main__":
    main()
