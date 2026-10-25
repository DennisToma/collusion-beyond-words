"""Release checks: portable verification, figure parity and deliberate bad inputs.

uv run python tests/test_reproduction.py

All mutations and figure runs use /var/tmp copies; sibling repos are never written.
Writes results/reproduction_check.json on success. No model calls or new metrics.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import evidence


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ReproductionChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="bw-release-", dir="/var/tmp")
        cls.scratch = Path(cls.temp.name)
        # No symlinks, source checkouts or credentials in this independent copy.
        cls.copy = cls.scratch / "standalone"
        cls.copy.mkdir()
        for name in ("scripts", "evidence", "figures", "results"):
            shutil.copytree(ROOT / name, cls.copy / name, ignore=shutil.ignore_patterns("__pycache__"))
        for name in ("SUBMISSION.md", "SLIDES.md"):
            shutil.copyfile(ROOT / name, cls.copy / name)
        cls.env = dict(os.environ, BW_Q14_ROOT=str(cls.scratch / "absent-q14"),
                       BW_Q22_ROOT=str(cls.scratch / "absent-q22"),
                       MPLCONFIGDIR=str(cls.scratch / "matplotlib"))
        cls.baseline = cls.run_checker()
        if cls.baseline.returncode:
            raise RuntimeError(cls.baseline.stdout + cls.baseline.stderr)
        cls.receipt = json.loads((cls.copy / "results/source_check.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    @classmethod
    def run_checker(cls, *arguments):
        return subprocess.run([sys.executable, str(cls.copy / "scripts/check_sources.py"), *arguments],
                              cwd=cls.scratch, env=cls.env, capture_output=True, text=True, timeout=30)

    def mutation(self, document, old, new):
        original = (ROOT / document).read_text()
        self.assertIn(old, original)
        modified = self.scratch / ("changed-" + document)
        modified.write_text(original.replace(old, new, 1))
        flag = "--submission" if document == "SUBMISSION.md" else "--slides"
        receipt = self.scratch / "mutation-receipt.json"
        result = self.run_checker(flag, str(modified), "--output", str(receipt))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        data = json.loads(receipt.read_text())
        self.assertEqual(data["n_fail"], 0)  # Saved source values alone still pass.
        self.assertGreater(data["n_document_fail"], 0)

    def test_standalone_sources_and_documents(self):
        self.assertEqual(self.receipt["source_mode"], "snapshot")
        self.assertEqual(self.receipt["n_evidence_files"], 76)
        self.assertEqual(self.receipt["n_checks"], 111)
        self.assertEqual(self.receipt["n_document_checks"], 139)
        self.assertEqual(self.receipt["n_fail"] + self.receipt["n_document_fail"], 0)

    def run_coverage(self):
        return subprocess.run([sys.executable, str(self.copy / "scripts/number_coverage.py")],
                              cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=30)

    def test_every_unbound_decimal_is_a_non_result(self):
        result = self.run_coverage()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads((self.copy / "results/number_coverage.json").read_text())
        self.assertEqual([data[d]["unbound_unclassified"] for d in ("SUBMISSION.md", "SLIDES.md")], [0, 0])

    def test_unbound_result_decimal_is_rejected(self):
        path = self.copy / "SUBMISSION.md"
        original = path.read_text()
        try:
            path.write_text(original.replace("### 5.3", "A new AUROC is 0.73 [0.61, 0.85].\n\n### 5.3", 1))
            result = self.run_coverage()
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("UNCLASSIFIED 0.73", result.stdout)
            # Review i19: a result placed next to "0.5 = chance" must not inherit that category.
            path.write_text(original.replace("(0.5 = chance;", "(0.5 = chance; AUROC 0.73 [0.61, 0.85];", 1))
            result = self.run_coverage()
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("UNCLASSIFIED 0.61", result.stdout)
        finally:
            path.write_text(original)

    def test_edited_primary_endpoint_is_rejected(self):
        self.mutation("SUBMISSION.md", "prices changes AUROC by −0.01", "prices changes AUROC by +0.09")

    def test_edited_slide_interval_is_rejected(self):
        self.mutation("SLIDES.md", "−0.01 [−0.09, +0.06]", "−0.01 [−0.09, +0.60]")

    def test_half_up_boundary_rejects_alternative_rounding(self):
        # Saved value 0.575 is a 3-dp tie; the exact value is 142/247 = 0.5749, so the report prints 0.57.
        # Half-up on the stored value (0.58, the double-rounded source print) must be rejected, as must
        # the earlier tolerance-only acceptance of either. Same for the grid CI (stored 0.805, exact 0.8047).
        self.mutation("SUBMISSION.md", "no resolved separation (AUROC 0.43–0.57,",
                      "no resolved separation (AUROC 0.43–0.58,")
        self.mutation("SLIDES.md", "| 0.74 [0.66, 0.80] |", "| 0.74 [0.66, 0.81] |")

    def test_reducing_precision_cannot_widen_tolerance(self):
        self.mutation("SUBMISSION.md", "no resolved separation (AUROC 0.43–0.57,",
                      "no resolved separation (AUROC 0–1,")
        self.mutation("SLIDES.md", "−0.01 [−0.09, +0.06]", "0 [0, 0]")

    def test_missing_binding_is_rejected(self):
        self.mutation("SUBMISSION.md", "prices changes AUROC by", "prices changes the score by")

    def test_corrupt_evidence_is_rejected(self):
        with patch.object(evidence, "ROOT", self.copy), patch.object(evidence, "MANIFEST", self.copy / "evidence/manifest.json"):
            bundle = evidence.Evidence()
            relative = "results/eval/e74_paired_diff.json"
            entry = bundle.manifest["projects"]["q14"]["files"][relative]
            path = self.copy / "evidence" / entry["stored_path"]
            original = path.read_bytes()
            try:
                path.write_bytes(original + b"corruption")
                with self.assertRaisesRegex(ValueError, "Stored evidence changed"):
                    bundle.json("q14", relative)
            finally:
                path.write_bytes(original)

    def test_live_mode_rejects_changed_source(self):
        source = self.scratch / "changed-live-source"
        path = source / "results/eval/e74_paired_diff.json"
        path.parent.mkdir(parents=True)
        path.write_text("{}")
        with patch.dict(os.environ, {"BW_Q14_ROOT": str(source)}):
            with self.assertRaisesRegex(ValueError, "Source evidence changed"):
                evidence.Evidence(live=True).json("q14", "results/eval/e74_paired_diff.json")

    def test_figures_reproduce_without_source_repos(self):
        for script, figure in [("fig1_hard_negatives.py", "fig1_scripted_hard_negatives.png"),
                               ("fig2_level_vs_comovement.py", "fig2_level_vs_comovement_9sets.png"),
                               ("fig3_e70_grid.py", "fig3_e70_grid.png"),
                               ("fig4_say_vs_do.py", "fig4_say_vs_do_summary.png"),
                               ("fig5_placebo_premium.py", "fig5_placebo_premium.png"),
                               ("fig6_strong_framing.py", "fig6_strong_framing_tacit.png")]:
            expected = sha(ROOT / "figures" / figure)
            (self.copy / "figures" / figure).unlink()
            result = subprocess.run([sys.executable, str(self.copy / "scripts" / script)],
                                    cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(sha(self.copy / "figures" / figure), expected)


    def test_llm_usage_counts_match_process_log_summary(self):
        # the LLM-usage statement prints runner-log counts; they must equal the committed snapshot
        summary = json.loads((ROOT / "results/process_log_summary.json").read_text())
        text = " ".join((ROOT / "SUBMISSION.md").read_text().split())
        by = summary["source_repos_total_by_backend"]
        expected = (f"{summary['source_repos_total']} manager iterations had completed by "
                    f"{summary['source_repos_snapshot_utc']} ({by['opus']} Opus, {by['codex-sol']} gpt-6.1-sol;")
        self.assertIn(expected, text)
        self.assertEqual(summary["source_repos_total"], sum(by.values()))

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReproductionChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        receipt = {"n_tests": result.testsRun, "n_fail": len(result.failures), "n_errors": len(result.errors),
                   "tests": unittest.defaultTestLoader.getTestCaseNames(ReproductionChecks),
                   "evidence_manifest_sha256": sha(ROOT / "evidence/manifest.json"),
                   "document_sha256": {p: sha(ROOT / p) for p in ("SUBMISSION.md", "SLIDES.md")},
                   "figure_sha256": {p: sha(ROOT / "figures" / p) for p in
                                     ("fig1_scripted_hard_negatives.png", "fig2_level_vs_comovement_9sets.png", "fig3_e70_grid.png",
                                      "fig4_say_vs_do_summary.png", "fig5_placebo_premium.png",
                                      "fig6_strong_framing_tacit.png")},
                   "standalone": {k: ReproductionChecks.receipt[k] for k in
                                  ("n_checks", "n_document_checks", "n_evidence_files", "n_fail", "n_document_fail")},
                   "notes": "Independent copy, absent source paths; bad report/slide values, missing binding, "
                            "rounding edge, corrupt snapshot and changed live source rejected. All six regenerated figures byte-identical."}
        (ROOT / "results/reproduction_check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
