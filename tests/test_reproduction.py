"""Release checks: portable verification, figure parity and deliberate bad inputs.

uv run python tests/test_reproduction.py

All mutations and figure runs use /var/tmp copies; sibling repos are never written.
Writes results/reproduction_check.json on success. No model calls or new metrics.
"""
import ast
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
        self.assertEqual(self.receipt["n_evidence_files"], 158)
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

    def test_q22_replays_reproduce_without_source_repos(self):
        # Remove the cached outputs: replays must regenerate them from evidence alone.
        for script, output in [("recompute_unrounded_q22.py", "unrounded_q22.json"),
                               ("recompute_c21b_floor.py", "c21b_floor.json"),
                               ("recompute_locked_test_q22.py", "locked_test_q22.json")]:
            path = self.copy / "results" / output
            path.unlink()
            result = subprocess.run([sys.executable, str(self.copy / "scripts" / script)],
                                    cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(path.read_bytes(), (ROOT / "results" / output).read_bytes())

    def test_locked_test_replay_parity_with_pinned_source_functions(self):
        import numpy as np
        from scipy.stats import rankdata
        import recompute_locked_test_q22 as portable

        ev = evidence.Evidence()
        tree = ast.parse(ev.read_bytes("q22", "final_analysis.py"))
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)
                     and n.name in ("metrics", "ci", "boot")]
        self.assertEqual({n.name for n in functions}, {"metrics", "ci", "boot"})
        original_views = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                              and any(isinstance(t, ast.Name) and t.id == "LLM_VIEWS" for t in n.targets))
        self.assertEqual(set(portable.VIEWS), set(original_views))
        original_auc_tree = ast.parse(ev.read_bytes("q22", "analyze_llm.py"))
        auc_function = [n for n in original_auc_tree.body if isinstance(n, ast.FunctionDef) and n.name == "auc"]
        pairs = next(ast.literal_eval(n.value) for n in original_auc_tree.body if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id == "PAIRS" for t in n.targets))

        def rank_auc(y, s):
            # Independent rank-sum definition in place of sklearn's roc_auc_score;
            # scipy's average ranks count score ties as one half.
            y = np.asarray(y, bool)
            p, n = int(y.sum()), int((~y).sum())
            return float((rankdata(s)[y].sum() - p * (p + 1) / 2) / (p * n))

        namespace = {"np": np, "roc_auc_score": rank_auc, "PAIRS": pairs, "LLM_VIEWS": original_views}
        exec(compile(ast.Module(body=auc_function + functions, type_ignores=[]),
                     "pinned/final_analysis.py", "exec"), namespace)
        ids, y, scores = portable.inputs(ev)
        # Construct the reference cohort/labels independently of the portable loader.
        constants = {t.id: ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                     for t in n.targets if isinstance(t, ast.Name) and t.id in ("DEV_MAX", "N_FROZEN")}
        source_ids = [f"llm_v3_{i:04d}" for i in range(constants["DEV_MAX"], constants["N_FROZEN"])]
        self.assertEqual(ids, source_ids)
        labs = {row["run_id"]: dict(row, y=int(row["agreement"] in ("explicit", "info_exchange")))
                for row in map(json.loads, ev.lines("q22", "data/llm_v3/labels.jsonl"))}
        self.assertEqual(y, {r: labs[r]["y"] for r in source_ids})
        original_scores = {v: {row["run_id"]: {"run": row["collusion_present"], "scores": row["scores"]}
                               for row in map(json.loads, ev.lines("q22", f"results/llm_auditor/llm_v3/gpt-6.1-sol/{v}_orig.jsonl"))}
                           for v in original_views}

        def compare(cohort, labels, source_scores, n_boot):
            actual = portable.compute(cohort, {r: labels[r]["y"] for r in cohort},
                                      {v: {r: source_scores[v][r]["run"] for r in cohort} for v in original_views}, n_boot)
            expected = namespace["boot"](cohort, source_scores, labels, n_boot)
            self.assertEqual(actual["point_ci"], {v: {"run_auroc": expected["point_ci"][v]["run_auroc"]}
                                                  for v in original_views})
            source_keys = {k for k in expected["contrasts"] if k.endswith(":run_auroc")}
            self.assertEqual(set(actual["contrasts"]), source_keys)
            self.assertEqual(actual["contrasts"], {k: expected["contrasts"][k] for k in source_keys})

        compare(ids, labs, original_scores, 31)
        # Calculator fixture with ties and frequent text/action rank reversals:
        # selecting the better single view only once would fail this check.
        cohort = [f"fixture_{i}" for i in range(8)]
        labels = {r: {"y": int(i < 4), "assigned_pair": ["A", "B"]} for i, r in enumerate(cohort)}
        rng = np.random.default_rng(41)
        source_scores = {v: {r: {"run": float(rng.integers(0, 5)), "scores": dict.fromkeys(pairs, 0)}
                             for r in cohort} for v in original_views}
        compare(cohort, labels, source_scores, 73)

    def test_locked_test_replay_rejects_missing_duplicate_or_invalid_inputs(self):
        import recompute_locked_test_q22 as portable

        ev = evidence.Evidence()
        target = "results/llm_auditor/llm_v3/gpt-6.1-sol/action_orig.jsonl"
        original_lines = ev.lines
        rows = portable.records(ev, target)
        invalid = dict(rows[0], collusion_present=float("nan"))
        wrong_model = dict(rows[0], model="different-auditor")
        for changed in (rows[:-1], rows + rows[:1], [invalid] + rows[1:], [wrong_model] + rows[1:]):
            def lines(project, path):
                return [json.dumps(row) for row in changed] if path == target else original_lines(project, path)
            with self.subTest(n_rows=len(changed), first_score=changed[0]["collusion_present"]):
                with patch.object(ev, "lines", side_effect=lines), self.assertRaises(AssertionError):
                    portable.inputs(ev)

    def test_c21b_per_run_parity_with_pinned_source_function(self):
        import numpy as np
        import recompute_c21b_floor as portable
        from recompute_unrounded_q22 import records, unique

        ev = evidence.Evidence()
        # Execute only the original pure analyse function, not source module imports or
        # its terms() loader (which can spend). Supply read-only cached terms instead.
        tree = ast.parse(ev.read_bytes("q22", "p2_strong.py"))
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "analyse"]
        self.assertEqual(len(functions), 1)
        mappings = [n.value for n in tree.body if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == "REQ" for t in n.targets)]
        self.assertEqual(len(mappings), 1)
        original_req = ast.literal_eval(mappings[0])
        datasets = ("llm_p2qwena", "llm_p2qwenb")
        self.assertEqual(portable.REQ, {ds: original_req[ds] for ds in datasets})
        original_root = self.scratch / "original-strong-inputs"
        for ds in datasets:
            for name in ("ground_truth", "trajectories"):
                rel = f"data/{ds}/{name}.jsonl"
                target = original_root / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(ev.read_bytes("q22", rel))
        namespace = {"np": np, "json": json, "Path": lambda p: original_root / p, "REQ": original_req,
                     "terms": lambda ds: unique(records(ev, f"data/{ds}/terms.jsonl")),
                     "jeffreys": lambda *args: None}  # interval summaries are not compared
        exec(compile(ast.Module(body=functions, type_ignores=[]), "pinned/p2_strong.py", "exec"), namespace)
        for ds in datasets:
            for floor in (12, 13):
                for late in (2, 11):
                    self.assertEqual(portable.analyse(ev, ds, floor, late),
                                     namespace["analyse"](ds, floor, late)["runs"])

    def test_grid_replay_reproduces_without_source_repos(self):
        output = self.copy / "results/grid_q14.json"
        output.unlink()
        result = subprocess.run([sys.executable, str(self.copy / "scripts/recompute_grid_q14.py")],
                                cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(output.read_bytes(), (ROOT / "results/grid_q14.json").read_bytes())

    def test_grid_parity_with_original_scores_cohort_and_bootstrap(self):
        import itertools
        import numpy as np
        import recompute_grid_q14 as portable

        ev = evidence.Evidence()

        def source_functions(path, names, namespace):
            tree = ast.parse(ev.read_bytes("q14", path))
            functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
            self.assertEqual({n.name for n in functions}, set(names))
            exec(compile(ast.Module(body=functions, type_ignores=[]), "pinned/" + path, "exec"), namespace)

        # The original detector module imports only stdlib + numpy, but execute
        # only its definitions/assignments to exclude even its read-only CLI.
        tree = ast.parse(ev.read_bytes("q14", "detectors/infotheory.py"))
        ns = {"np": np, "itertools": itertools}
        pure = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.Assign))]
        exec(compile(ast.Module(body=pure, type_ignores=[]), "pinned/detectors/infotheory.py", "exec"), ns)
        llm_tree = ast.parse(ev.read_bytes("q14", "experiments/llm_eval.py"))
        original_nash = next(ast.literal_eval(n.value) for n in llm_tree.body if isinstance(n, ast.Assign)
                             and any(isinstance(t, ast.Name) and t.id == "NASH" for t in n.targets))
        self.assertEqual(portable.NASH, original_nash)
        ns.update(json=json)
        source_functions("experiments/llm_eval.py", ("arrays", "add_level_scores"), ns)
        from datetime import datetime, timezone
        ns.update(datetime=datetime, timezone=timezone, Path=Path, math=__import__("math"))
        source_functions("scripts/e70_inputs.py", ("load_games",), ns)
        source_functions("scripts/e1_grid.py", ("cells",), ns)
        grid_tree = ast.parse(ev.read_bytes("q14", "scripts/e1_grid.py"))
        ns["FACTORS"] = next(ast.literal_eval(n.value) for n in grid_tree.body if isinstance(n, ast.Assign)
                             and any(isinstance(t, ast.Name) and t.id == "FACTORS" for t in n.targets))
        original_cells = ns["cells"]()
        self.assertEqual(original_cells, ev.json("q14", "data/llm_grid_p2_manifest.json")["cells"])
        original_root = self.scratch / "original-grid-inputs"
        original_games = []
        for cell in original_cells:
            directory = original_root / cell["cell"]
            directory.mkdir(parents=True)
            for name in ("ground_truth", "trajectories"):
                rel = f"data/llm_grid_p2_{cell['cell']}/{name}.jsonl"
                (directory / f"{name}.jsonl").write_bytes(ev.read_bytes("q14", rel))
            conds = ("B", "D") if cell["levels"]["shocks"] == "random" else ("A", "C")
            gt, rows, nbad = ns["load_games"](directory, cell["levels"]["model"], conditions=conds)
            self.assertEqual(portable.load_cell(ev, cell), (gt, rows, nbad))
            for rid, g in gt.items():
                P, S, _ = ns["arrays"](rows[rid])
                nash = np.array([original_nash[r["market"]["cost"]] for r in rows[rid]], float)
                score = ns["score_run"](P, S, B=0)
                ns["add_level_scores"](score, P, nash)
                expected_pairs = {p: {d: score[p]["score"][d] for d in portable.DETS} for p in ns["PAIR_NAMES"]}
                self.assertEqual(portable.pair_scores(P, S, nash), expected_pairs)
                channel = g["condition"] in "CD"
                ids = [a["id"] for a in rows[rid][0]["agents"]]
                rivals = [i for i in range(4) if not channel or ids[i] not in g["assigned_pair"]]
                original_games.append({"cell": cell["cell"], "run_id": rid, "channel": channel,
                                       "markup": float((P - nash[:, None]).mean()),
                                       "rival_markup": float((P[:, rivals] - nash[:, None]).mean()),
                                       "scores": {d: max(v[d] for v in expected_pairs.values()) for d in portable.DETS}})

        # Execute the original nested stats/auroc_strat functions (not main),
        # with independently reconstructed original scores and source cell signs.
        grid_tree = ast.parse(ev.read_bytes("q14", "scripts/e70_grid.py"))
        main = next(n for n in grid_tree.body if isinstance(n, ast.FunctionDef) and n.name == "main")
        functions = [n for n in main.body if isinstance(n, ast.FunctionDef) and n.name in ("stats", "auroc_strat")]
        self.assertEqual({n.name for n in functions}, {"stats", "auroc_strat"})
        original_dets = next(ast.literal_eval(n.value) for n in grid_tree.body if isinstance(n, ast.Assign)
                             and any(isinstance(t, ast.Name) and t.id == "DETS" for t in n.targets))
        self.assertEqual(portable.DETS, original_dets)
        ns.update(DETS=original_dets, sign={c["cell"]: c["signs"] for c in original_cells})
        exec(compile(ast.Module(body=functions, type_ignores=[]), "pinned/e70_grid.py", "exec"), ns)
        by = {c["cell"]: {v: [g for g in original_games if g["cell"] == c["cell"] and g["channel"] == v]
                          for v in (True, False)} for c in original_cells}
        rng = np.random.default_rng(0)
        points = ns["stats"](by)
        boots = []
        for _ in range(2000):
            sample = {c: {v: [a[v][i] for i in rng.integers(0, len(a[v]), len(a[v]))] for v in (True, False)}
                      for c, a in by.items()}
            boots.append(ns["stats"](sample))
        actual = portable.summarize(original_cells, original_games)
        for d in portable.DETS:
            self.assertEqual(actual["pooled_auroc_unrounded"][d],
                             [points[3][d], *map(float, np.quantile([b[3][d] for b in boots], [.025, .975]))])
        self.assertEqual(actual["pooled_C_minus_A"], [round(float(np.mean(list(points[0].values()))), 3),
                          *[round(float(x), 3) for x in np.quantile([np.mean(list(b[0].values())) for b in boots], [.025, .975])]])
        # Independent original paired-bootstrap implementation, also full B=2000.
        paired_tree = ast.parse(ev.read_bytes("q14", "scripts/e74_paired_diff.py"))
        for name in ("B", "SEED", "LEVEL", "OTHERS"):
            # The source declares these in tuple assignments.
            for node in paired_tree.body:
                if isinstance(node, ast.Assign):
                    target = node.targets[0]
                    names = [t.id for t in target.elts] if isinstance(target, ast.Tuple) else [target.id]
                    if name in names:
                        values = ast.literal_eval(node.value)
                        ns[name] = values[names.index(name)] if isinstance(target, ast.Tuple) else values
                        break
        source_functions("scripts/e74_paired_diff.py", ("strat_au", "paired"), ns)
        groups = [([dict(g["scores"]) for g in a[True]], [dict(g["scores"]) for g in a[False]]) for a in by.values()]
        expected = ns["paired"](groups)
        self.assertEqual(actual["paired_contrasts"], {k: expected[k] for k in actual["paired_contrasts"]})

    def test_grid_replay_rejects_malformed_completed_runs(self):
        import recompute_grid_q14 as portable

        ev = evidence.Evidence()
        cell = ev.json("q14", "data/llm_grid_p2_manifest.json")["cells"][0]
        base = "data/llm_grid_p2_c00/"
        paths = {name: base + name + ".jsonl" for name in ("ground_truth", "trajectories")}
        data = {name: [json.loads(x) for x in ev.lines("q14", path)] for name, path in paths.items()}
        original_lines = ev.lines
        wrong_sellers = json.loads(json.dumps(data["trajectories"][0]))
        wrong_sellers["agents"].reverse()
        nonfinite = json.loads(json.dumps(data["trajectories"][0]))
        nonfinite["agents"][0]["price"] = float("nan")
        for name, changed in (("ground_truth", data["ground_truth"] * 2),
                              ("trajectories", data["trajectories"][1:]),
                              ("trajectories", data["trajectories"] + data["trajectories"][:1]),
                              ("trajectories", [wrong_sellers] + data["trajectories"][1:]),
                              ("trajectories", [nonfinite] + data["trajectories"][1:])):
            with patch.object(ev, "lines", side_effect=lambda project, path: (
                    [json.dumps(r) for r in changed] if path == paths[name] else original_lines(project, path))):
                with self.assertRaises(AssertionError):
                    portable.load_cell(ev, cell)

    def test_gate_replay_reproduces_without_source_repos(self):
        path = self.copy / "results/gate_q14.json"
        path.unlink()
        result = subprocess.run([sys.executable, str(self.copy / "scripts/recompute_gate_q14.py")],
                                cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(path.read_bytes(), (ROOT / "results/gate_q14.json").read_bytes())

    def test_gate_replay_parity_with_pinned_source_functions(self):
        import itertools
        import numpy as np
        from scipy.stats import rankdata
        import recompute_gate_q14 as portable

        ev = evidence.Evidence()
        tree = ast.parse(ev.read_bytes("q14", "experiments/scripted.py"))
        constants = [n for n in tree.body if isinstance(n, ast.Assign)
                     and any(isinstance(t, ast.Name) and t.id in ("DETS", "P_DETS") for t in n.targets)]
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)
                     and n.name in ("wilson", "pairname", "surrogate_p", "evaluate")]
        self.assertEqual({n.name for n in functions}, {"wilson", "pairname", "surrogate_p", "evaluate"})
        detector_tree = ast.parse(ev.read_bytes("q14", "detectors/infotheory.py"))
        pair_constants = [n for n in detector_tree.body if isinstance(n, ast.Assign)
                          and any(isinstance(t, ast.Name) and t.id in ("AGENTS", "PAIRS", "PAIR_NAMES") for t in n.targets)]

        def rank_auc(y, s):
            y = np.asarray(y, bool)
            p, n = int(y.sum()), int((~y).sum())
            return float((rankdata(s)[y].sum() - p * (p + 1) / 2) / (p * n))

        ns = {"np": np, "itertools": itertools, "roc_auc_score": rank_auc}
        exec(compile(ast.Module(body=pair_constants + constants + functions, type_ignores=[]),
                     "pinned/experiments/scripted.py", "exec"), ns)
        self.assertEqual(portable.DETS, tuple(ns["DETS"]))
        self.assertEqual(portable.P_DETS, tuple(ns["P_DETS"]))
        self.assertEqual(portable.PAIRS, tuple(ns["PAIR_NAMES"]))
        # Reconstruct cached inputs independently, without the portable loader.
        gt = {g["run_id"]: g for g in map(json.loads, ev.lines("q14", "data/gate_test/ground_truth.jsonl"))}
        source_res = {r: {p: {"score": {}, "p": {}} for p in ns["PAIR_NAMES"]} | {"_run_p": {}} for r in gt}
        for det in ns["DETS"]:
            for row in map(json.loads, ev.lines("q14", f"results/{det}/gate_test.jsonl")):
                r, p = row["run_id"], row["pair"]
                source_res[r][p]["score"][det] = row["score"]
                source_res[r][p]["p"][det] = row["p"]
                source_res[r]["_run_p"][det] = row["run_p"]
        self.assertEqual(portable.load_inputs(ev), (gt, source_res))

        def compare(res, ground_truth):
            actual, counts = portable.summarize(res, ground_truth)
            expected = ns["evaluate"](res, ground_truth)
            for det in ns["DETS"]:
                self.assertEqual(portable.surrogate_p(res, ground_truth, det),
                                 ns["surrogate_p"](res, ground_truth, det))
            n, error = portable.compare_saved(actual, expected)
            self.assertGreater(n, 0)
            self.assertLessEqual(error, 1e-14)
            # Every exported numerator is bound to the reported rate and n.
            for det, groups in counts.items():
                for key, fields in groups.items():
                    for field, k in fields.items():
                        rate_key = field + "_rate" if field in ("flag", "surrogate_flag") else field
                        self.assertEqual(actual[det][key][rate_key], k / actual[det][key]["n"])
            return actual, counts

        actual, _ = compare(source_res, gt)
        self.assertEqual(portable.compare_saved(actual, ev.json("q14", "results/eval/gate_test.json")["metrics"])[0], 666)
        # Calculator fixture, not research data: exact alpha boundary, near-ties
        # across the 1e-12 comparison tolerance, score ties, shock-family matching,
        # leave-one-out and pair p-values that must never replace the run test.
        fixture_gt, fixture_res = {}, {}
        rows = [(f"{c}{i}", c, None, float(i + (100 if c == "B" else 0))) for c in "AB" for i in range(20)]
        rows += [("near", "C", None, 19 + 5e-13), ("clear", "C", None, 19 + 2e-12),
                 ("d", "D", None, 30.0), ("hn", "A", "shared_policy", 40.0)]
        for rid, condition, hn, score in rows:
            fixture_gt[rid] = {"condition": condition, "hard_negative": hn,
                               "assigned_pair": ["A", "C"] if condition in "CD" else None,
                               "hn_pair": ["A", "B"] if hn else None}
            fixture_res[rid] = {p: {"score": dict.fromkeys(ns["DETS"], score if p in ("AB", "AC") else -1),
                                   "p": dict.fromkeys(ns["P_DETS"], 0.001)} for p in ns["PAIR_NAMES"]}
            fixture_res[rid]["_run_p"] = dict.fromkeys(ns["P_DETS"], 0.04 if rid == "clear" else 0.05)
        _, counts = compare(fixture_res, fixture_gt)
        sp = portable.surrogate_p(fixture_res, fixture_gt, "pcmi")
        self.assertEqual(sp["A19"], 0.05)  # leave-one-out: 1/20, not 1/21
        self.assertEqual(sp["near"], 2 / 21)
        self.assertEqual(sp["clear"], 1 / 21)
        self.assertEqual(sp["d"], 1.0)  # D uses B's higher-scoring controls, not A's.
        self.assertEqual(counts["pcmi"]["A"]["surrogate_flag"], 0)  # strict < alpha
        self.assertEqual(counts["pcmi"]["C"], {"surrogate_flag": 1, "flag": 1, "top1": 0})

    def test_gate_replay_rejects_malformed_cache_and_cohort(self):
        import recompute_gate_q14 as portable

        ev = evidence.Evidence()
        gt_path = "data/gate_test/ground_truth.jsonl"
        score_path = "results/pcmi/gate_test.jsonl"
        gt = [json.loads(s) for s in ev.lines("q14", gt_path)]
        rows = [json.loads(s) for s in ev.lines("q14", score_path)]
        original_lines = ev.lines
        cases = [(gt_path, gt[:-1]), (gt_path, gt + gt[:1]),
                 (gt_path, [dict(gt[0], seed=0)] + gt[1:]),
                 (gt_path, [dict(gt[0], assigned_pair=["A", "B"])] + gt[1:]),
                 (score_path, rows[:-1]), (score_path, rows + rows[:1])]
        for field, value in (("score", float("nan")), ("score", float("inf")),
                             ("run_p", 0.0), ("run_p", 1.1), ("p", None),
                             ("run_p", 0.123), ("pair", "ZZ"), ("run_id", "unknown")):
            cases.append((score_path, [dict(rows[0], **{field: value})] + rows[1:]))
        inconsistent = [dict(r) for r in rows]
        inconsistent[1]["run_p"] = 1 / 201
        cases.append((score_path, inconsistent))
        ni_path = "results/ni_pcmi/gate_test.jsonl"
        ni = [json.loads(s) for s in ev.lines("q14", ni_path)]
        cases.append((ni_path, [dict(ni[0], run_p=0.1)] + ni[1:]))
        for path, changed in cases:
            with self.subTest(path=path, n_rows=len(changed), first=changed[0]):
                with patch.object(ev, "lines", side_effect=lambda project, p: (
                        [json.dumps(r) for r in changed] if p == path else original_lines(project, p))):
                    with self.assertRaises(AssertionError):
                        portable.load_inputs(ev)

    def test_gate_pcmi_replay_reproduces_without_source_repos(self):
        path = self.copy / "results/gate_pcmi_q14.json"
        path.unlink()
        result = subprocess.run([sys.executable, str(self.copy / "scripts/recompute_gate_pcmi_q14.py")],
                                cwd=self.scratch, env=self.env, capture_output=True, text=True, timeout=180)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(path.read_bytes(), (ROOT / "results/gate_pcmi_q14.json").read_bytes())

    def test_gate_pcmi_parity_with_original_null_and_loader(self):
        from collections import defaultdict
        import gzip
        import itertools
        import numpy as np
        import recompute_gate_pcmi_q14 as portable

        ev = evidence.Evidence()
        tree = ast.parse(ev.read_bytes("q14", "detectors/infotheory.py"))
        # Execute the unmodified original full score_run, not a pCMI-only rewrite.
        nodes = [n for n in tree.body if isinstance(n, (ast.Assign, ast.FunctionDef))]
        ns = {"np": np, "itertools": itertools, "defaultdict": defaultdict, "json": json}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), "pinned/infotheory.py", "exec"), ns)
        gt = {g["run_id"]: g for g in map(json.loads, ev.lines("q14", "data/gate_test/ground_truth.jsonl"))}
        trajectory = self.scratch / "gate-trajectories.jsonl"
        trajectory.write_bytes(gzip.decompress(ev.read_bytes("q14", "data/gate_test/trajectories.jsonl.gz")))
        original = ns["load_runs"](trajectory)
        actual = portable.load_trajectories(ev, gt)
        self.assertEqual(set(actual), set(original))
        for rid, (P, S) in actual.items():
            np.testing.assert_array_equal(P, original[rid]["P"])
            np.testing.assert_array_equal(S, original[rid]["S"])
        self.assertEqual(tuple(ns["PAIR_NAMES"]), portable.NAMES)

        def compare(P, S, seed, B=200):
            expected = ns["score_run"](P, S, B=B, seed=seed)
            result = portable.score_pcmi(P, S, B=B, seed=seed)
            self.assertEqual(result["n_null"], expected["_n_null"])
            self.assertEqual(result["run_p"], expected["_run_p"]["pcmi"])
            self.assertEqual(result["scores"], {p: expected[p]["score"]["pcmi"] for p in portable.NAMES})
            self.assertEqual(result["pair_p"], {p: expected[p]["p"]["pcmi"] for p in portable.NAMES})

        # One preselected run per original group, original index/seed and B=200.
        for seed in range(0, 500, 50):
            compare(*actual[f"gate_test_{seed:05d}"], seed)
        # Calculator fixtures: constant/perfectly tied prices, no valid offsets,
        # fewer than 20 draws, and enough draws for the exact 1e-12 tie rule.
        for T, B in ((7, 200), (30, 19), (30, 20), (30, 0)):
            compare(np.full((T, 4), 10.0), np.zeros(T, int), 37, B)

        # The reviewer found that all-constant fixtures alone could not detect
        # removal of the finite-draw fallback or the near-tie tolerance.
        P = np.random.default_rng(42).normal(size=(30, 4))
        S = np.zeros(30, int)
        compare(P, S, 37, 19)
        self.assertEqual(set(portable.score_pcmi(P, S, B=19, seed=37)["pair_p"].values()), {1.0})
        import inspect
        mutant = dict(portable.__dict__)
        exec(inspect.getsource(portable.score_pcmi).replace("if draws >= min_draws", "if True"), mutant)
        self.assertEqual(mutant["score_pcmi"](P, S, B=19, seed=37)["pair_p"]["AB"], 0.65)

        P = np.zeros((100, 4))
        for k in range(4):
            P[10 + 20 * k, k], P[20 + 20 * k, k] = 1, -1
        P[:, 1] += 1e-7 * P[:, 0]
        S = np.zeros(100, int)
        compare(P, S, 37)
        result = portable.score_pcmi(P, S, seed=37)
        self.assertTrue(0 < result["scores"]["AB"] < 1e-12)
        self.assertEqual((result["pair_p"]["AB"], result["run_p"]), (1.0, 1.0))
        mutant = dict(portable.__dict__)
        exec(inspect.getsource(portable.score_pcmi).replace(" - 1e-12", ""), mutant)
        changed = mutant["score_pcmi"](P, S, seed=37)
        self.assertEqual((changed["pair_p"]["AB"], changed["run_p"]), (9 / 201, 42 / 201))

    def test_gate_pcmi_rejects_malformed_trajectories_and_cache(self):
        import gzip
        import recompute_gate_pcmi_q14 as portable

        ev = evidence.Evidence()
        gt, _ = portable.load_inputs(ev)
        path = "data/gate_test/trajectories.jsonl.gz"
        raw = ev.read_bytes("q14", path)
        rows = [json.loads(s) for s in gzip.decompress(raw).splitlines()]
        wrong = json.loads(json.dumps(rows[0]))
        wrong["agents"].reverse()
        nonfinite = json.loads(json.dumps(rows[0]))
        nonfinite["agents"][0]["price"] = float("nan")
        cases = [rows[1:], rows + rows[:1], [wrong] + rows[1:], [nonfinite] + rows[1:],
                 [dict(rows[0], run_id="unknown")] + rows[1:]]
        for changed in cases:
            data = gzip.compress("\n".join(json.dumps(r) for r in changed).encode(), mtime=0)
            with patch.object(ev, "read_bytes", return_value=data):
                with self.assertRaises(AssertionError):
                    portable.load_trajectories(ev, gt)
        # A valid but wrong historical p-value must fail the raw replay, even
        # though it passes cache-format validation and the value is on the grid.
        original_lines = ev.lines
        cache_path = "results/pcmi/gate_test.jsonl"
        cache = [json.loads(s) for s in ev.lines("q14", cache_path)]
        cache[0]["p"] = (2 if cache[0]["p"] == 1 / 201 else 1) / 201
        with patch.object(ev, "lines", side_effect=lambda project, p: (
                [json.dumps(r) for r in cache] if p == cache_path else original_lines(project, p))):
            with self.assertRaisesRegex(AssertionError, "pair-p mismatch"):
                portable.replay(ev)

    def test_llm_usage_counts_match_process_log_summary(self):
        # the LLM-usage statement prints runner-log counts; they must equal the committed snapshot
        summary = json.loads((ROOT / "results/process_log_summary.json").read_text())
        text = " ".join((ROOT / "SUBMISSION.md").read_text().split())
        by = summary["source_repos_total_by_backend"]
        expected = (f"{summary['source_repos_total']} manager iterations had completed by "
                    f"{summary['source_repos_snapshot_utc']} ({by['opus']} Opus, {by['codex-sol']} gpt-6.1-sol;")
        self.assertIn(expected, text)
        self.assertEqual(summary["source_repos_total"], sum(by.values()))

    def test_finalize_rewrites_exactly_one_usage_sentence(self):
        # scripts/finalize.py must find exactly one LLM-usage sentence to refresh in each document
        sys.path.insert(0, str(ROOT / "scripts"))
        import finalize
        self.assertEqual(len(finalize.SUB_RE.findall((ROOT / "SUBMISSION.md").read_text())), 1)
        self.assertEqual(len(finalize.REP_RE.findall((ROOT / "REPORT.md").read_text())), 1)

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
                   "q22_replay_sha256": {p: sha(ROOT / "results" / p) for p in
                                         ("unrounded_q22.json", "c21b_floor.json", "locked_test_q22.json")},
                   "q14_replay_sha256": {p: sha(ROOT / "results" / p) for p in ("grid_q14.json", "gate_q14.json", "gate_pcmi_q14.json")},
                   "gate_pcmi_original_function_parity": {"group_representatives": 10, "null_draws_per_run": 200,
                                                          "calculator_fixtures": 6,
                                                          "finite_draw_and_tie_tolerance_mutations_rejected": True,
                                                          "full_historical_replay_runs": 500,
                                                          "source": "q14/detectors/infotheory.py:load_runs, score_run"},
                   "gate_original_function_parity": {"games": 500, "detectors": 9, "cached_pair_rows": 27000,
                                                     "saved_numeric_fields": 666, "calculator_fixture_runs": 44,
                                                     "source": "q14/experiments/scripted.py"},
                   "grid_original_function_parity": {"games": 192, "pairs_per_game": 6, "detectors": 4,
                                                     "grid_bootstraps": 2000, "paired_bootstraps": 2000,
                                                     "source": "q14/detectors/infotheory.py, scripts/e70_grid.py, scripts/e74_paired_diff.py"},
                   "locked_test_original_function_parity": {"real_cohort_bootstraps": 31,
                                                            "tied_fixture_bootstraps": 73,
                                                            "full_saved_result_bootstraps": 2000,
                                                            "source": "q22/final_analysis.py"},
                   "c21b_original_function_parity": {"settings": 8, "runs_per_setting": 30,
                                                     "source": "q22/p2_strong.py"},
                   "standalone": {k: ReproductionChecks.receipt[k] for k in
                                  ("n_checks", "n_document_checks", "n_evidence_files", "n_fail", "n_document_fail")},
                   "notes": "Independent copy, absent source paths; bad report/slide values, missing binding, "
                            "rounding edge, corrupt snapshot and changed live source rejected. All six figures and three "
                            "Q2.2 replay outputs regenerate byte-identically. C21b per-run fields match the pinned original "
                            "analyse function in all eight floor/window settings. Locked-test run metrics/contrasts match "
                            "pinned original functions on the real cohort and a tied calculator fixture; full B=2000 replay "
                            "matches all selected saved results. The Q1.4 raw-grid output regenerates byte-identically; "
                            "all pair scores, cohort loading and full bootstraps match original functions. "
                            "The scripted gate reaggregates all nine archived detector caches with original-function parity "
                            "and boundary/tie/leave-one-out calculator checks. A separate pCMI replay reconstructs all historical shift draws, scores and p-values from frozen trajectories, with original full-score-function parity on ten group representatives and constant/short fixtures; no markets are generated. "
                            "Malformed completed trajectories and missing, duplicate and invalid audit/cache inputs are rejected."}
        (ROOT / "results/reproduction_check.json").write_text(json.dumps(receipt, indent=2) + "\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
