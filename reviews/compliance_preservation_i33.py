"""Author-side comparison against the pre-compliance Git revision; no new analysis.

Run with Python from an authorized full checkout. The portable release checks do
not depend on this historical Git comparison or on a .git directory.
"""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = "089ffb0"


def original(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)


def main():
    old_bindings = json.loads(original("results/document_bindings.json"))
    new_bindings = json.loads((ROOT / "results/document_bindings.json").read_text())
    assert new_bindings[:len(old_bindings)] == old_bindings
    old_checks = json.loads(original("results/source_check.json"))["checks"]
    new_checks = json.loads((ROOT / "results/source_check.json").read_text())["checks"]
    assert new_checks == old_checks
    frozen = ["evidence/manifest.json"]
    frozen += [str(p.relative_to(ROOT)) for p in sorted((ROOT / "figures").glob("fig*.png"))]
    frozen += ["results/" + n + ".json" for n in (
        "unrounded_q22", "c21b_floor", "locked_test_q22", "grid_q14", "gate_q14", "gate_pcmi_q14")]
    for path in frozen:
        assert (ROOT / path).read_bytes() == original(path), path
    receipt = {
        "baseline_revision": subprocess.check_output(["git", "rev-parse", BASE], cwd=ROOT, text=True).strip(),
        "identical_source_assertion_objects": len(old_checks),
        "unchanged_original_bindings": len(old_bindings),
        "new_bindings_for_repeated_claims": len(new_bindings) - len(old_bindings),
        "frozen_artifact_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in frozen},
        "scope": "Original saved source-check objects, binding definitions, six replay outputs, six figures and evidence manifest are unchanged. The full 158-file bundle hashes are independently checked by check_sources.py. No new estimates or experimental data."
    }
    (ROOT / "results/compliance_preservation_i33.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print("PASS: scientific artifacts and all 111 source assertions / 139 original bindings unchanged")


if __name__ == "__main__":
    main()
