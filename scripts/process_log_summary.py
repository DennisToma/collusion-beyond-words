"""Summarise the autonomous-agent runner logs for the LLM-usage statement.

Reads ~/collusion/logs/{,p2/}<repo>.runner.log (machine-local, not in the repo) and
writes results/process_log_summary.json. Counts completed manager iterations per
repo, phase and backend ([opus] = Claude Opus 5.5 via `claude -p`, [codex-sol] =
codex gpt-6.1-sol fallback when the Claude quota was exhausted).
Usage: uv run python scripts/process_log_summary.py
"""
import json, re, sys
from collections import Counter
from pathlib import Path

LOGS = Path.home() / "collusion" / "logs"
REPOS = ["collusion-14-infotheory", "collusion-22-say-vs-do", "collusion-beyond-words"]
OUT = Path(__file__).resolve().parents[1] / "results" / "process_log_summary.json"


def summarise(path):
    if not path.exists():
        return None
    lines = path.read_text().splitlines()
    ends = [l for l in lines if " end rc=" in l]
    who = Counter(re.search(r"\[([a-z-]+)\]", l).group(1) for l in ends)
    starts = [l for l in lines if " start " in l]
    return {"completed_iterations": len(ends), "by_backend": dict(sorted(who.items())),
            "first_start": starts[0].split(" iter ")[0] if starts else None,
            "last_end": ends[-1].split(" iter ")[0] if ends else None}


def main():
    out = {"source": str(LOGS), "repos": {}}
    for r in REPOS:
        out["repos"][r] = {"phase1": summarise(LOGS / f"{r}.runner.log"),
                           "phase2": summarise(LOGS / "p2" / f"{r}.runner.log")}
    tot = Counter()
    for r in REPOS[:2]:
        for ph in ("phase1", "phase2"):
            s = out["repos"][r][ph]
            if s:
                tot.update(s["by_backend"])
    out["source_repos_total_by_backend"] = dict(sorted(tot.items()))
    out["source_repos_total"] = sum(tot.values())
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    sys.exit(main())
