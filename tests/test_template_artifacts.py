"""Primary-upload acceptance and failure checks; copies only, no experiments."""
import contextlib
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_template_artifacts as template


class TemplateChecks(unittest.TestCase):
    def test_current_primary_artifacts(self):
        with contextlib.redirect_stdout(io.StringIO()):
            result = template.check_template()
        self.assertTrue(result["ok"])
        self.assertLessEqual(result["main_text_pages"], 8)
        self.assertEqual(result["figures"], 4)

    def test_structure_disclosures_and_abstract_limits(self):
        source = (ROOT / "TEMPLATE_REPORT.md").read_text()
        form = (ROOT / "SUBMISSION_FORM.md").read_text()
        abstract = template.section(source, "## Abstract", "\n## 1. Introduction").split("\n![", 1)[0].strip()
        for n in (149, 251):
            with self.assertRaises(ValueError):
                template.check_markdown(source.replace(abstract, "word " * n, 1), form)
        for n in (150, 250):
            template.check_markdown(source.replace(abstract, "word " * n, 1), form)
        for old, new in (("## LLM Usage Statement", "## Omitted"),
                         ("3. **A warning", "4. **A warning"),
                         ("### B. Limitations and Dual-Use / Ethical Considerations", "### B. Omitted"),
                         ("## 4. Results", "## 4. Results\n\nE123 result.")):
            self.assertIn(old, source)
            with self.assertRaises(ValueError):
                template.check_markdown(source.replace(old, new, 1), form)

    def test_stale_pdf_source_figure_and_image_fail_closed(self):
        source = (ROOT / "TEMPLATE_REPORT.md").read_text()
        names = template.artifact_hashes(source).keys()
        with tempfile.TemporaryDirectory(prefix="bw-template-test-", dir="/var/tmp") as tmp:
            root = Path(tmp)
            for name in (*names, template.RECEIPT):
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, root / name)
            with patch.object(template, "ROOT", root), patch.object(template.export, "ROOT", root):
                for name in ("TEMPLATE_REPORT.md", "TEMPLATE_REPORT.pdf", "IMAGE.png", "figures/fig0_headline.png"):
                    target = root / name
                    original = target.read_bytes()
                    target.write_bytes(original + b"\nchanged")
                    with self.assertRaisesRegex(ValueError, "Stale primary export receipt"):
                        template.check_template()
                    target.write_bytes(original)

    def test_concurrent_source_or_artifact_changes_are_rejected(self):
        source = (ROOT / "TEMPLATE_REPORT.md").read_text()
        with self.assertRaisesRegex(ValueError, "Markdown changed during export"):
            template.check_template(require_receipt=False, expected_source=source + "\nold snapshot")
        hashes = template.artifact_hashes(source)
        with patch.object(template, "artifact_hashes", side_effect=[hashes, {**hashes, "IMAGE.png": "changed"}]):
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaisesRegex(ValueError, "artifacts changed"):
                template.check_template(require_receipt=False)

    def test_headline_and_project_image_regenerate_byte_exact_without_siblings(self):
        with tempfile.TemporaryDirectory(prefix="bw-headline-test-", dir="/var/tmp") as tmp:
            root = Path(tmp)
            for name in ("scripts", "evidence"):
                shutil.copytree(ROOT / name, root / name, ignore=shutil.ignore_patterns("__pycache__"))
            (root / "figures").mkdir()
            env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG") if k in os.environ}
            env.update(BW_Q14_ROOT=str(root / "absent-q14"), BW_Q22_ROOT=str(root / "absent-q22"),
                       MPLCONFIGDIR=str(root / "mpl"))
            result = subprocess.run([sys.executable, "scripts/fig0_headline.py"], cwd=root, env=env,
                                    capture_output=True, text=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for name in ("figures/fig0_headline.png", "IMAGE.png"):
                self.assertEqual((root / name).read_bytes(), (ROOT / name).read_bytes(), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
