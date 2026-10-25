"""Check committed PDF text, figure pixels and links without exporting or writing.

The existing export receipt binds the Markdown/PDF/exporter bytes; this also binds
current PNG pixels to the actual PDF images. No browser launch or model calls.
uv run --group export python scripts/check_committed_export.py
"""
import hashlib
import json
from pathlib import Path
import re

from pypdf import PdfReader

import export_pdf as export

ROOT = Path(__file__).resolve().parents[1]


def check_document(pdf, source, slides=False):
    if slides:
        parts = [s for s in re.split(r"(?m)^---\s*$", source) if s.strip()]
        if len(PdfReader(pdf).pages) != len(parts):
            raise ValueError("Committed slide page count differs from Markdown")
        missing = []
        for i, part in enumerate(parts):
            missing += export.check_pdf(pdf, export.text_fragments(part), f"committed slide {i+1}", i)
    else:
        missing = export.check_pdf(pdf, export.text_fragments(source), "committed report")
    if missing:
        raise ValueError(f"Committed PDF text differs from Markdown: {pdf.name}")
    return dict(figures=export.check_figures(pdf, source), links=export.check_links(pdf))


def main():
    receipt = json.loads((ROOT / "results/export_check.json").read_text())
    for name in ("SUBMISSION.md", "SLIDES.md", "SUBMISSION.pdf", "SLIDES.pdf", "scripts/export_pdf.py"):
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != receipt["sha256"][name]:
            raise ValueError(f"Stale export receipt: {name}")
    result = {name: check_document(ROOT / f"{name}.pdf", (ROOT / f"{name}.md").read_text(),
                                   slides=name == "SLIDES") for name in ("SUBMISSION", "SLIDES")}
    print(json.dumps(dict(ok=True, documents=result,
                         scope="Committed text, per-slide placement, actual figure pixels and portable link schemes; "
                               "no PDF rebuild or browser layout recheck."), indent=2))


if __name__ == "__main__":
    main()
