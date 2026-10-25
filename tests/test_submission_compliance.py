"""Submission constraints fail closed, including actual PDF boundary detection."""
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_submission_compliance as compliance


class ComplianceChecks(unittest.TestCase):
    def test_current_markdown_and_reference_evidence(self):
        report = (ROOT / "SUBMISSION.md").read_text()
        form = (ROOT / "SUBMISSION_FORM.md").read_text()
        compliance.check_markdown(report, form)
        self.assertEqual(compliance.check_references(report), 15)
        with self.assertRaises(AssertionError):
            compliance.check_references(report.replace("Measuring Information Transfer", "Invented Transfer Paper"))

    def test_abstract_summary_and_required_appendix_are_enforced(self):
        report = (ROOT / "SUBMISSION.md").read_text()
        form = (ROOT / "SUBMISSION_FORM.md").read_text()
        abstract = compliance.section(report, "## Abstract", "\n## 1. Introduction")
        summary = compliance.section(form, "## Summary", "\n## Tracks to tick")
        for n in (149, 251):
            with self.assertRaises(AssertionError):
                compliance.check_markdown(report.replace(abstract, "word " * n, 1), form)
        for n in (150, 250):
            compliance.check_markdown(report.replace(abstract, "word " * n, 1), form)
        with self.assertRaises(AssertionError):
            compliance.check_markdown(report, form.replace(summary, "word " * 151, 1))
        with self.assertRaises(AssertionError):
            compliance.check_markdown(report.replace(compliance.ETHICS, "### G. Omitted"), form)

    def test_pdf_boundary_does_not_exclude_a_mixed_main_page(self):
        def reader(texts):
            return SimpleNamespace(pages=[SimpleNamespace(extract_text=lambda t=t: t) for t in texts])
        self.assertEqual(compliance.main_pages(reader(["main"] * 8 + ["References\nentry"])), 8)
        with self.assertRaises(ValueError):
            compliance.main_pages(reader(["main"] * 7 + ["Conclusion\nReferences\nentry"]))
        with self.assertRaises(ValueError):
            compliance.main_pages(reader(["main only"]))


if __name__ == "__main__":
    unittest.main()
