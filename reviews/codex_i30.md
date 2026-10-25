# Iteration 30 — independent raw-gate pCMI replay review

Reviewed 2026-10-25 13:09 UTC by an independent Codex subagent, against merge parent
`d8ebfabf89f00149aa8a21afec59e67da1318162`. Only this review file was edited by the reviewer.
No model/auditor calls, markets, tuning, new estimands or source-repo writes were performed.

No actionable P1/P2 findings. One nonblocking test weakness was found and fixed during review:
constant fixtures alone could not detect removal of the finite-draw fallback or near-tie tolerance.
The final test includes nonconstant fixtures and checks explicit mutant outcomes for both rules.

Independent verification:

- All 158 evidence blobs match `git show` at their pinned commits, including original bytes, SHA256
  and lengths. All prior 157 manifest entries and stored blobs are unchanged against the merge parent.
- All 500 reconstructed price matrices and market-state vectors equal the unmodified pinned original
  `load_runs` outputs element for element.
- Executed the **unmodified pinned original full `score_run` on all 500 games**, with sorted-index
  seeds 0–499 and B=200. This completed in 336.76 seconds. All 3000 observed pCMI scores, 3000 pair
  p-values, 500 max-statistic run p-values and 500 valid-draw counts equal the portable implementation
  exactly. Every game has 200 valid draws. Pair/run p-values also equal the archived caches exactly.
  This is broader than the ten group representatives retained in the routine release test.
- Independently executed the full portable replay without writing its output. Its JSON serialization
  is byte-identical to `results/gate_pcmi_q14.json`, and maximum observed-score/cache error is zero.
- Inspected the linear state-plus-all-lags design, residual centering/scaling, re-residualisation after
  circular shifting, sorted-run seed assignment, 50-attempt pairwise relative-offset rejection, shared
  shifts across six pairs, separate pair versus max-statistic p-values, inclusive `1e-12` near-ties,
  pseudocounts and the fewer-than-20 valid-draw fallback. All match the pinned source.
- The three new targeted tests pass. After the fixture fix, the original-function parity test passes
  again, including no-valid-offset/B=0/19/20 fixtures. Missing/duplicate rounds, reordered sellers,
  nonfinite prices, unknown run IDs and a valid-format but incorrect cached p-value are rejected.
- The nonconstant B=19 fixture uses `default_rng(42).normal(size=(30,4))`, zero state and seed 37.
  Correct pair p-values are all 1; removing the fallback gives AB p=0.65. The near-tie fixture uses
  balanced sparse impulses at rows `10+20*k` (+1) and `20+20*k` (-1) for column k, with column B
  additionally receiving `1e-7*A`, T=100, zero state and seed 37. AB's positive observed score is
  `4.99600361081323e-15`; correct AB/run p-values are 1. Removing the tolerance yields 9/201 and
  42/201 respectively. Both fixtures also compare against the unmodified original scorer.
- Reviewed README, REPORT, SUBMISSION, SOURCES and evidence README changes. They accurately limit
  this addition to frozen pCMI score/null replay, exclude other detectors' null validation and label
  correctness, and distinguish the earlier remote-clone receipt from the new replay. No scientific
  main-text estimate or slide wording changes are introduced. `git diff --check` passes.

Reviewed content SHA256:

| File | SHA256 |
|---|---|
| `scripts/recompute_gate_pcmi_q14.py` | `4c338a4170fd3a07be604190cf9556fc0d42b11c850921441a260570ff7e29a2` |
| `results/gate_pcmi_q14.json` | `92a1570b1a3e2336c336248b589fa9803c371588d9e4b2343ffb89f9b8dc018a` |
| `evidence/manifest.json` | `9ff5d8be1c1fc80daeb81ba761026ef081be0c8e03532da497e985769b5ba6ea` |
| `tests/test_reproduction.py` | `083d4d22d390b67800a8fbbf1c402c0b93e343673df10f8f2c300abf9f63b1ad` |

Reproduce the independent all-500 check from the merge-repo root with `uv run python` and the following
code. The AST extraction executes the original functions unchanged; it does not supply a rewritten
reference estimator. Scratch belongs under `/var/tmp`.

```python
import ast, gzip, itertools, json, pathlib, sys, tempfile
from collections import defaultdict
import numpy as np
sys.path.insert(0, "scripts")
from evidence import Evidence
import recompute_gate_pcmi_q14 as p

ev = Evidence()
ns = dict(np=np, itertools=itertools, json=json, defaultdict=defaultdict)
tree = ast.parse(ev.read_bytes("q14", "detectors/infotheory.py"))
nodes = [n for n in tree.body if isinstance(n, (ast.Assign, ast.FunctionDef))]
exec(compile(ast.Module(body=nodes, type_ignores=[]), "pinned/infotheory.py", "exec"), ns)
gt, cache = p.load_inputs(ev)
actual = p.load_trajectories(ev, gt)
with tempfile.TemporaryDirectory(dir="/var/tmp") as tmp:
    path = pathlib.Path(tmp) / "trajectories.jsonl"
    path.write_bytes(gzip.decompress(ev.read_bytes("q14", "data/gate_test/trajectories.jsonl.gz")))
    original = ns["load_runs"](path)
assert set(original) == set(actual)
for seed, (rid, d) in enumerate(sorted(original.items())):
    P, S = actual[rid]
    np.testing.assert_array_equal(P, d["P"])
    np.testing.assert_array_equal(S, d["S"])
    expected = ns["score_run"](d["P"], d["S"], B=200, seed=seed)
    result = p.score_pcmi(P, S, B=200, seed=seed)
    assert result["n_null"] == expected["_n_null"] == 200
    assert result["run_p"] == expected["_run_p"]["pcmi"] == cache[rid]["_run_p"]["pcmi"]
    for name in p.NAMES:
        assert result["scores"][name] == expected[name]["score"]["pcmi"]
        assert result["pair_p"][name] == expected[name]["p"]["pcmi"] == cache[rid][name]["p"]["pcmi"]
assert len(original) == 500
replayed = p.replay(ev)
assert replayed["max_score_absolute_error"] == 0
assert (json.dumps(replayed, indent=2) + "\n").encode() == p.OUT.read_bytes()
print("All 500 original full-scorer comparisons and output byte parity pass")
```

The provenance check iterated every manifest entry, compared `Evidence.read_bytes(project,path)`
with `git -C ../<repo> show <pinned-commit>:<path>`, checked stored/original byte lengths, and compared
all previous entries plus their stored bytes with `git show d8ebfab:evidence/manifest.json` and the
corresponding `git show d8ebfab:evidence/<stored_path>` blobs.
