"""Verify the actual primary upload against its Markdown, figures and template rules.

No browser, model calls or scientific reanalysis. The exporter writes a byte-bound
receipt; this command rechecks it and the committed PDF without rebuilding.
"""
import hashlib
import json
from pathlib import Path
import re

from PIL import Image
from pypdf import PdfReader

import export_pdf as export
from check_submission_compliance import main_pages, section, word_count

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = "results/template_artifact_check.json"
HEADINGS = (
    "Abstract", "1. Introduction", "2. Related Work", "3. Methods", "4. Results",
    "5. Discussion and Limitations", "6. Conclusion", "Code and Data",
    "Author Contributions", "References", "Appendix", "LLM Usage Statement",
)


def check_markdown(source, form):
    headings = re.findall(r"(?m)^## (.+)$", source)
    if headings != list(HEADINGS):
        raise ValueError("Template headings are missing, duplicated or out of order")
    # The headline figure follows the abstract before Introduction. Its caption
    # is not part of the abstract word count.
    abstract = section(source, "## Abstract", "\n## 1. Introduction").split("\n![", 1)[0].strip()
    summary = section(form, "## Summary", "\n## Tracks to tick")
    if not 150 <= word_count(abstract) <= 250 or not 0 < word_count(summary) <= 150:
        raise ValueError("Abstract or form-summary word limit violated")
    intro = section(source, "## 1. Introduction", "\n## 2. Related Work")
    if "Our main contributions are:" not in intro or re.findall(r"(?m)^(\d+)\. ", intro) != ["1", "2", "3"]:
        raise ValueError("Expected three numbered contributions")
    for phrase in ("Dennis Toma", "Independent", "With Apart Research",
                   "Research conducted at the AI Collusion Research Sprint, October 2026",
                   "### Limitations", "### Future Work",
                   "### B. Limitations and Dual-Use / Ethical Considerations"):
        if phrase not in source:
            raise ValueError(f"Missing template requirement: {phrase}")
    main = source.split("\n## References\n")[0]
    if re.search(r"\b(?:E\d+|P2\.\d+)\b", main):
        raise ValueError("Experiment IDs in primary main text")
    if "figures/fig1_scripted_hard_negatives.png" not in main:
        raise ValueError("Scripted positive control omitted from main text")
    return dict(abstract_words=word_count(abstract), form_summary_words=word_count(summary))


def artifact_hashes(source):
    figures = re.findall(r"!\[[^]]*\]\(([^)]+)\)", source)
    names = ("TEMPLATE_REPORT.md", "TEMPLATE_REPORT.pdf", "SUBMISSION_FORM.md", "IMAGE.png",
             "scripts/export_template_pdf.py", "scripts/export_pdf.py", "scripts/check_template_artifacts.py", *figures)
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in names}


def check_template(require_receipt=True, expected_source=None):
    source = (ROOT / "TEMPLATE_REPORT.md").read_text()
    if expected_source is not None and source != expected_source:
        raise ValueError("Primary Markdown changed during export")
    result = check_markdown(source, (ROOT / "SUBMISSION_FORM.md").read_text())
    hashes = artifact_hashes(source)
    if hashes["TEMPLATE_REPORT.md"] != hashlib.sha256(source.encode()).hexdigest():
        raise ValueError("Primary Markdown changed during verification")
    if require_receipt:
        saved = json.loads((ROOT / RECEIPT).read_text())
        if hashes != saved["sha256"]:
            raise ValueError("Stale primary export receipt: source, PDF, image or exporter changed")
    pdf = ROOT / "TEMPLATE_REPORT.pdf"
    fragments = [re.sub(r"<[^>]+>", "", f) for f in export.text_fragments(source)]
    if export.check_pdf(pdf, fragments, "primary template report"):
        raise ValueError("Primary PDF text differs from Markdown")
    result["text_fragments"] = len(fragments)
    result["figures"] = export.check_figures(pdf, source)
    export.check_links(pdf)
    reader = PdfReader(pdf)
    result.update(main_text_pages=main_pages(reader), total_pages=len(reader.pages), pdf_bytes=pdf.stat().st_size)
    if result["main_text_pages"] > 8 or result["pdf_bytes"] > 25_000_000:
        raise ValueError("Primary report exceeds page or file-size limit")
    with Image.open(ROOT / "figures/fig0_headline.png") as img:
        headline = (img.size, export.pixel_digest(img))
    if not any((img.image.size, export.pixel_digest(img.image)) == headline
               for page in reader.pages[:2] for img in page.images):
        raise ValueError("Headline Figure 1 is absent from pages 1–2")
    with Image.open(ROOT / "IMAGE.png") as img:
        img.verify()
    with Image.open(ROOT / "IMAGE.png") as img:
        if img.size != (1600, 900):
            raise ValueError("Project image must be 1600×900")
    if artifact_hashes(source) != hashes:
        raise ValueError("Primary artifacts changed during verification")
    result.update(ok=True, sha256=hashes,
                  scope="Primary PDF text/figure pixels/links, template structure and lengths, page limits, "
                        "early headline placement and project image format; not scientific validity.")
    return result


if __name__ == "__main__":
    print(json.dumps(check_template(), indent=2))
