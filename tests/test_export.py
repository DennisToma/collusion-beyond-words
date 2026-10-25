"""Exercise export failures using tiny PDFs in /var/tmp; no source or experiment writes.

uv run --group export python tests/test_export.py
"""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import export_pdf as export


class ExportChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="bw-export-test-", dir="/var/tmp")
        cls.scratch = Path(cls.temp.name)
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.pg = cls.browser.new_page()
        cls.pg.emulate_media(media="print")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.temp.cleanup()

    def render(self, body, name="fixture", css=export.SLIDE_CSS):
        path = self.scratch / (name + ".html")
        path.write_text(export.page(name, css, body))
        self.pg.goto(path.as_uri(), wait_until="load")
        pdf = path.with_suffix(".pdf")
        self.pg.pdf(path=str(pdf), prefer_css_page_size=True)
        return pdf

    def test_deleted_body_and_wrong_slide_are_detected(self):
        pdf = self.render("<section><h2>First</h2><p>First result.</p></section>"
                          "<section><h2>Second</h2><p>Second result.</p></section>")
        # Titles alone pass even when a body claim is absent or on the wrong page.
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(export.check_pdf(pdf, ["First", "Second"], "titles"), [])
            self.assertEqual(export.check_pdf(pdf, ["Absent result."], "missing"), ["Absent result."])
            self.assertEqual(export.check_pdf(pdf, ["Second result."], "wrong page", 0), ["Second result."])
            self.assertEqual(export.check_pdf(pdf, ["Second result."], "right page", 1), [])

    def test_markdown_formatting_preserves_meaningful_text(self):
        source = "## Test\n\n**Result:** `pCMI` [link](https://example.com) −0.01.\n\n- Claim *one*.\n"
        fragments = export.text_fragments(source)
        self.assertEqual(fragments, ["Test", "Result: pCMI link −0.01.", "Claim one."])
        pdf = self.render("<section>" + export.md().render(source) + "</section>")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(export.check_pdf(pdf, fragments, "formatted"), [])

    def test_missing_or_broken_images_are_rejected(self):
        with self.assertRaises(FileNotFoundError):
            export.embed_images('<img src="figures/absent-i10.png">')
        self.render('<section><img alt="broken image" src="absent.png"></section>')
        with self.assertRaisesRegex(ValueError, "Images did not load"):
            export.validate_browser_images(self.pg)

    def test_missing_or_substituted_pdf_figure_is_rejected(self):
        source = "![Figure](figures/fig5_placebo_premium.png)"
        pdf = self.render("<section><p>No figure.</p></section>")
        with self.assertRaisesRegex(ValueError, "figure pixels/count mismatch"):
            export.check_figures(pdf, source)
        other = "![Other](figures/fig4_say_vs_do_summary.png)"
        pdf = self.render("<section>" + export.embed_images(export.md().render(other)) + "</section>")
        with self.assertRaisesRegex(ValueError, "figure pixels/count mismatch"):
            export.check_figures(pdf, source)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(export.check_figures(pdf, other), 1)

    def test_repo_links_become_portable_and_file_links_fail(self):
        body = export.portable_links('<a href="SOURCES.md">Sources</a>')
        self.assertIn(export.REPO_URL + "SOURCES.md", body)
        pdf = self.render("<section>" + body + "</section>")
        self.assertEqual(export.check_links(pdf), [export.REPO_URL + "SOURCES.md"])
        pdf = self.render('<section><a href="file:///var/tmp/SOURCES.md">Sources</a></section>')
        with self.assertRaisesRegex(ValueError, "Nonportable PDF link"):
            export.check_links(pdf)
        with self.assertRaises(FileNotFoundError):
            export.portable_links('<a href="absent-i10.md">Sources</a>')

    def test_figure_height_yields_before_font_floor(self):
        source = [s for s in (ROOT / "SLIDES.md").read_text().split("\n---\n") if s.strip()][4]
        self.render("<section>" + export.embed_images(export.md().render(source)) + "</section>")
        fit = self.pg.evaluate(export.FIT_JS)[0]
        self.assertFalse(fit["overflow"])
        self.assertGreaterEqual(fit["font_pt"], export.MIN_SLIDE_PT)
        self.assertLess(fit["image_max_height_mm"], 100)

    def test_excess_content_is_rejected_at_font_floor(self):
        self.render("<section><h2>Overfull slide</h2>" + "<p>Too much text.</p>" * 100 + "</section>")
        fit = self.pg.evaluate(export.FIT_JS)[0]
        self.assertTrue(fit["overflow"])
        self.assertEqual(fit["font_pt"], export.MIN_SLIDE_PT)

    def test_font_floor_includes_tables_and_code(self):
        self.render("<section><p>With <code>literal code</code>.</p>"
                    "<table><tr><td>Table cell</td></tr></table></section>")
        fit = self.pg.evaluate(export.FIT_JS)[0]
        self.assertFalse(fit["overflow"])
        self.assertGreaterEqual(fit["min_text_font_pt"], export.MIN_SLIDE_PT - .01)
        self.render('<section><p style="font-size:10pt">Too small.</p></section>')
        self.assertTrue(self.pg.evaluate(export.FIT_JS)[0]["overflow"])

    def test_padding_and_horizontal_overflow_are_detected(self):
        # Neither case must be allowed just because it is inside the page border.
        for style in ["position:absolute;bottom:0", "white-space:nowrap;width:2000px"]:
            text = "Off padding" if "bottom" in style else "Long " * 300
            self.render(f'<section style="position:relative"><p style="{style}">{text}</p></section>')
            self.assertTrue(self.pg.evaluate(export.FIT_JS)[0]["overflow"])


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ExportChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        receipt = {"command": "uv run --group export python tests/test_export.py",
                   "n_tests": result.testsRun, "n_fail": len(result.failures), "n_errors": len(result.errors),
                   "tests": unittest.defaultTestLoader.getTestCaseNames(ExportChecks),
                   "sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                              for name in ("scripts/export_pdf.py", "tests/test_export.py", "SLIDES.md")}}
        (ROOT / "results/export_test.json").write_text(json.dumps(receipt, indent=2) + "\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
