"""One-command finalize pass for the release (run at FINALIZE, Sun 16:30 UTC).

1. Refresh results/process_log_summary.json from the runner logs (the runners keep going
   after the evidence freeze, so the LLM-usage counts grow).
2. Rewrite the LLM-usage sentence in SUBMISSION.md and the matching REPORT.md line to the
   refreshed counts (the release test binds the SUBMISSION sentence to the JSON).
3. Run every release check: check_sources, number_coverage, reproduction and packaging
   tests, PDF export, export/compliance failure tests. Stop at the first failure (exit 1).

Commit the resulting outputs before running package_release.py for the final handoff.

Usage: uv run python scripts/finalize.py [--no-export]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SUB_RE = re.compile(r"\d+ manager iterations had completed by \d{4}-\d\d-\d\d \d\d:\d\d UTC "
                    r"\((\d+) Opus, (\d+)(\s+)gpt-6\.1-sol;")
REP_RE = re.compile(r"\d+ source-repo manager iterations by \d{4}-\d\d-\d\d \d\d:\d\d UTC "
                    r"\(\d+ Opus, \d+ gpt-6\.1-sol;")


def run(cmd):
    print("\n$ " + " ".join(cmd), flush=True)
    r = subprocess.run(cmd, cwd=ROOT)
    if r.returncode != 0:
        sys.exit(f"FINALIZE FAILED at: {' '.join(cmd)} (exit {r.returncode})")


def rewrite(path, pattern, make):
    text = path.read_text()
    new, n = pattern.subn(make, text)
    if n != 1:
        sys.exit(f"FINALIZE FAILED: expected exactly 1 LLM-usage sentence in {path.name}, found {n}")
    path.write_text(new)
    return text != new


def main():
    export = "--no-export" not in sys.argv[1:]
    run(["uv", "run", "python", "scripts/process_log_summary.py"])
    s = json.loads((ROOT / "results/process_log_summary.json").read_text())
    tot, ts, by = s["source_repos_total"], s["source_repos_snapshot_utc"], s["source_repos_total_by_backend"]
    assert tot == sum(by.values()) and set(by) <= {"opus", "codex-sol"}, by
    opus, sol = by.get("opus", 0), by.get("codex-sol", 0)
    changed = rewrite(ROOT / "SUBMISSION.md", SUB_RE,
                      lambda m: f"{tot} manager iterations had completed by {ts} ({opus} Opus,"
                                f" {sol}{m.group(3)}gpt-6.1-sol;")
    rewrite(ROOT / "REPORT.md", REP_RE,
            lambda m: f"{tot} source-repo manager iterations by {ts} ({opus} Opus, {sol} gpt-6.1-sol;")
    print(f"\nLLM-usage counts: {tot} by {ts} ({opus} Opus, {sol} gpt-6.1-sol); "
          f"SUBMISSION {'updated' if changed else 'unchanged'}")
    run(["uv", "run", "python", "scripts/check_sources.py"])
    run(["uv", "run", "python", "scripts/number_coverage.py"])
    run(["uv", "run", "python", "tests/test_reproduction.py"])
    run(["uv", "run", "python", "tests/test_packaging.py"])
    if export:
        run(["uv", "run", "--group", "export", "python", "scripts/export_pdf.py"])
        run(["uv", "run", "--group", "export", "python", "scripts/check_committed_export.py"])
        run(["uv", "run", "--group", "export", "python", "tests/test_export.py"])
        run(["uv", "run", "--group", "export", "python", "scripts/check_submission_compliance.py"])
        run(["uv", "run", "--group", "export", "python", "tests/test_submission_compliance.py"])
    print("\nFINALIZE OK" + ("" if export else " (export skipped)"))


if __name__ == "__main__":
    main()
