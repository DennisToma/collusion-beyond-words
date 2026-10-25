# Iteration 29 — fresh-clone distribution verification

Manager verification, completed 2026-10-25 12:55 UTC; no new external critic or model call.
Target: GitHub `731de19fbb15a151470ce98365639ee7aa137b22` (iteration 28).
Receipt: [results/distribution_check.json](../results/distribution_check.json).

The previous GitHub-clone check covered the earlier 76-file bundle. The release now has 157
pinned files and additional Q1.4 grid/gate and Q2.2 replays. This pass checks that the expanded
release ships everything needed, rather than relying on the manager's existing virtualenv,
saved replay outputs, figure files or browser installation.

## Procedure

Cloned the actual remote (not a local working-tree copy):

```bash
git clone --no-local gh-cbw:DennisToma/collusion-beyond-words.git /var/tmp/bw-iteration29-release
cd /var/tmp/bw-iteration29-release
git checkout 731de19fbb15a151470ce98365639ee7aa137b22
uv sync --locked --all-groups --no-cache
```

`gh-cbw` is the author VM's SSH host alias. A public checkout can instead use
`https://github.com/DennisToma/collusion-beyond-words.git`.

The clone started clean. Its `.venv` was new; packages were downloaded from the lockfile.
The scientific/export commands inherited only PATH, HOME, LANG, LC_ALL and TMPDIR where
present, plus BW_Q14_ROOT/BW_Q22_ROOT pointing to nonexistent paths, a new MPLCONFIGDIR
and a new PLAYWRIGHT_BROWSERS_PATH under `/var/tmp`. No model environment variables were
passed. HOME was unchanged; this is an isolation of command inputs on the same VM, not an
OS sandbox or proof that author-machine configuration is inaccessible.

Deleted the five replay JSONs and six PNGs before running the 17 commands in the receipt.
All five replay scripts run first, then six figure scripts, check_sources, number_coverage,
test_reproduction, a fresh Chromium installation, export_pdf and test_export. Each command
exited successfully. The scripts are the ones documented in README; no experimental or
model-calling source scripts were executed. The machine-local process-log snapshot was
preserved, so the author-only finalize/log-refresh step was deliberately excluded.

## Results

- The five deleted replay outputs and six deleted figures rebuild byte-identically.
- Source/document/evidence checks: 111/139/157; no failed checks or unclassified decimals.
- Reproduction suite: 23 tests; export suite: 9 tests; no failures or errors.
- Export checks preserve 492 report fragments, all 55 slide fragments and 10 figure embeddings.
- Report: 17 pages. Slides: 8 pages. All page text and content streams match the committed PDFs.
- Normalising only CreationDate/ModDate makes the entire PDF byte sequences identical.
- Across all tracked paths, only the two PDF files and `results/export_check.json` change
  in the scratch clone. The export receipt changes only its two PDF hashes. Every other
  tracked file remains byte-identical. Production PDFs and receipts were retained.

The comparison below can be run inside the rebuilt clone with its `.venv/bin/python`.
It reads the committed Git blobs directly rather than comparing against a mutable
author-machine copy:

```python
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
from pypdf import PdfReader

def git(*args):
    return subprocess.check_output(["git", *args])

assert git("rev-parse", "HEAD").decode().strip() == "731de19fbb15a151470ce98365639ee7aa137b22"
paths = git("ls-files", "-z").decode().strip("\0").split("\0")
before = {p: git("show", f"HEAD:{p}") for p in paths}
after = {p: Path(p).read_bytes() for p in paths}
changed = {p for p in paths if before[p] != after[p]}
assert changed <= {"SUBMISSION.pdf", "SLIDES.pdf", "results/export_check.json"}

def normalise_dates(data):
    return re.sub(rb"/(CreationDate|ModDate)\s*\(D:[^)]*\)", rb"/\1 (normalised)", data)

for name in ("SUBMISSION.pdf", "SLIDES.pdf"):
    old, new = PdfReader(io.BytesIO(before[name])), PdfReader(io.BytesIO(after[name]))
    assert len(old.pages) == len(new.pages)
    assert [p.extract_text() for p in old.pages] == [p.extract_text() for p in new.pages]
    assert [p.get_contents().get_data() for p in old.pages] == [p.get_contents().get_data() for p in new.pages]
    assert normalise_dates(before[name]) == normalise_dates(after[name])

old_receipt = json.loads(before["results/export_check.json"])
new_receipt = json.loads(after["results/export_check.json"])
for name in ("SUBMISSION.pdf", "SLIDES.pdf"):
    assert new_receipt["sha256"][name] == hashlib.sha256(after[name]).hexdigest()
    new_receipt["sha256"][name] = old_receipt["sha256"][name]
assert new_receipt == old_receipt
print("All tracked artifacts match; only PDF dates and their receipt hashes differ.")
```

This is a distribution check of frozen evidence/calculations on the author VM. It does not
validate the source labels, rerun null draws, evaluate a new test split, or establish
reproducibility on another operating system. Scientific claims, estimates, manuscript,
slides, evidence pins and usage-count snapshot remain unchanged.
