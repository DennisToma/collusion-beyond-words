"""Check the director's submission requirements against the actual files.

uv run --group export python scripts/check_submission_compliance.py

Identity evidence is the saved starter-bibliography concordance plus the earlier
primary-source audit. This is not a fresh scientific review of the cited papers.
"""
import hashlib
import json
from pathlib import Path
import re

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
ETHICS = "### G. Limitations and Dual-Use / Ethical Considerations"


def section(text, heading, following):
    if text.count(heading + "\n") != 1:
        raise ValueError(f"Expected one {heading}")
    return text.split(heading + "\n", 1)[1].split(following, 1)[0].strip()


def word_count(text):
    # Explicit, reproducible convention: whitespace-delimited words, with link
    # destinations removed. The abstract contains no hidden glossary or lists.
    return len(re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text).split())


def check_markdown(report, form):
    abstract = section(report, "## Abstract", "\n## 1. Introduction")
    summary = section(form, "## Summary", "\n## Tracks to tick")
    assert 150 <= word_count(abstract) <= 250, "Abstract must have 150–250 words"
    assert 0 < word_count(summary) <= 150, "Form summary must have at most 150 words"
    assert "Dennis Toma — Independent" in report, "Missing author affiliation"
    main = report.split("\n## References\n", 1)[0]
    assert "figures/fig1_scripted_hard_negatives.png" in main, "Positive control must stay in main text"
    assert ETHICS in report, "Missing required ethics appendix"
    assert report.index(ETHICS) > report.index("\n## Appendix"), "Ethics must be in an appendix"
    for phrase in ("**Dual-use risk.**", "#### LLM usage statement", "#### Pre-existing code and data"):
        assert phrase in report, f"Missing {phrase}"
    assert "Track 1" in form and "Q1.4" in form and "Track 2" in form and "Q2.2" in form
    return {"abstract_words": word_count(abstract), "form_summary_words": word_count(summary)}


def main_pages(reader):
    # References must start a new page. Do not silently undercount a mixed page
    # containing the end of the conclusion followed by the references heading.
    pages = [p.extract_text() or "" for p in reader.pages]
    starts = [i for i, t in enumerate(pages) if t.strip().startswith("References\n")]
    if len(starts) != 1 or starts[0] == 0:
        raise ValueError("Expected exactly one fresh References page after the main text")
    if any(re.search(r"(?m)^References\s*$", t) for t in pages[:starts[0]]):
        raise ValueError("References share a page with main text")
    return starts[0]


def check_references(report):
    references = section(report, "## References", "\n## Appendix")
    entries = [line for line in references.splitlines() if line.startswith("- ")]
    metadata = json.loads((ROOT / "results/reference_metadata_i33.json").read_text())
    recorded = metadata["entries"]
    assert entries == [r["entry"] for r in recorded], "References changed since identity check"
    assert len(set(entries)) == len(entries) == 15, "Unexpected or duplicate references"
    primary_audit = (ROOT / "reviews/literature_i11.md").read_text()
    for entry in recorded:
        assert entry["identity_audit_row"] in primary_audit, "Missing primary identity evidence"
        assert re.search(r"\(\d{4}\)", entry["authors_year"]), "Missing year/authors"
        assert entry["title"] and re.search(r"https://(arxiv.org|doi.org|proceedings.mlr.press)/", entry["entry"])
        source = entry["starter_metadata"]
        if source:
            assert source["year"] in entry["authors_year"] and source["url"] in entry["entry"]
    return len(entries)


def main():
    report = (ROOT / "SUBMISSION.md").read_text()
    form = (ROOT / "SUBMISSION_FORM.md").read_text()
    result = check_markdown(report, form)
    result["verified_reference_entries"] = check_references(report)
    result["main_text_pages"] = main_pages(PdfReader(ROOT / "SUBMISSION.pdf"))
    assert result["main_text_pages"] <= 8, "Main text exceeds eight pages"
    result["total_report_pages"] = len(PdfReader(ROOT / "SUBMISSION.pdf").pages)
    result["slides"] = len(PdfReader(ROOT / "SLIDES.pdf").pages)
    assert result["slides"] <= 8
    result["submission_pdf_bytes"] = (ROOT / "SUBMISSION.pdf").stat().st_size
    assert result["submission_pdf_bytes"] <= 25_000_000, "Submission PDF exceeds 25 MB"
    # A standalone compliance command must reject a stale PDF too. The exporter
    # already binds the PDF, Markdown and exporter bytes in its receipt.
    export = json.loads((ROOT / "results/export_check.json").read_text())
    for name in ("SUBMISSION.md", "SLIDES.md", "SUBMISSION.pdf", "SLIDES.pdf", "scripts/export_pdf.py"):
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == export["sha256"][name], f"Stale export: {name}"
    result.update(ok=True, scope="Director's file/length/layout/disclosure checks and recorded reference identity concordance; not scientific validity.")
    result["sha256"] = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                        for name in ("SUBMISSION.md", "SUBMISSION_FORM.md", "SUBMISSION.pdf", "SLIDES.pdf",
                                     "results/reference_metadata_i33.json", "scripts/check_submission_compliance.py")}
    (ROOT / "results/submission_compliance.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
