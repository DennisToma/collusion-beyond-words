"""Record the iteration-40 source reconciliation; never write to source repos.

Author-machine provenance check, not an experiment or a standalone release test.
Requires the two source clones and their historical Git objects. Checks the
recorded source revisions, and requires live HEADs/worktrees to match them.
Unknown deltas fail; the explicit exceptions below were read by the manager.
Run: uv run python reviews/source_freeze_i40_driver.py
Use --output to record a later live check without overwriting the original receipt.
Later, use --historical to check the recorded commits without requiring the live
source/merge files to remain frozen; the receipt marks that reduced scope.
"""
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "q14": ("e8cf411460358ab14ffdb4769ada846406fd9497", {
        "DIRECTION.md": "director instructions",
        "STATUS.md": "handoff log",
        "EXPERIMENTS.tsv": "two merge verification rows, no experiment",
        "PRESENTATION.pdf": "render-only export",
        "REPORT.html": "render-only export",
        "REPORT.pdf": "render-only export",
        "results/reviews/merge_check.json": "merge check receipt; two known rounding quote misses",
        "results/reviews/merge_flags.md": "scope reviews; I152 covers current manuscript bytes",
    }),
    "q22": ("5a012a0bba87dbfbd5bbbfcb16c810ab91483bc9", {
        "DIRECTION.md": "director instructions",
        "STATUS.md": "handoff log; I160 covers current manuscript bytes",
        "README.md": "export freshness statement",
        "REPORT.md": "one I133 merge-review line, no scientific revision",
        "PRESENTATION.pdf": "render-only export",
        "REPORT.html": "render-only export",
        "REPORT.pdf": "render-only export",
        "data/handoff_exports.json": "rendering provenance receipt",
        "figures/p2_strong_llm_p2strongF.png": "render of corrected rounds 11–40 label",
        "p2_strongF_fig.py": "only rounds 11–40 label replaces 2nd half",
        "results/analysis/merge_flags.md": "scope-review history",
        "results/analysis/phase2_reproduction.json": "reproduction receipt; saved outputs unchanged",
    }),
}


def git(repo, *args):
    env = {k: os.environ[k] for k in ("PATH", "HOME", "LANG", "LC_ALL") if k in os.environ}
    env["GIT_OPTIONAL_LOCKS"] = "0"
    return subprocess.check_output(["git", *args], cwd=repo, env=env)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def tree(repo, rev):
    result = {}
    for entry in git(repo, "ls-tree", "-rz", rev).split(b"\0"):
        if entry:
            info, path = entry.split(b"\t", 1)
            result[path.decode()] = info.decode()
    return result


def blob(repo, rev, path):
    return git(repo, "show", f"{rev}:{path}")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--historical", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "results/source_freeze_i40.json")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "evidence/manifest.json").read_text())
    receipt = {"merge_head": git(ROOT, "rev-parse", "a924419" if args.historical else "HEAD").decode().strip(),
               "live_heads_and_worktrees_checked": not args.historical, "projects": {}}
    baseline = git(ROOT, "rev-parse", "a924419^{commit}").decode().strip()
    release_files = {"SUBMISSION.md", "SUBMISSION.pdf", "SLIDES.md", "SLIDES.pdf", "SUBMISSION_FORM.md",
                     "uv.lock", "results/process_log_summary.json", "results/unrounded_q22.json",
                     "results/c21b_floor.json", "results/locked_test_q22.json", "results/grid_q14.json",
                     "results/gate_q14.json", "results/gate_pcmi_q14.json"}
    protected = {}
    for path in tree(ROOT, baseline):
        if path in release_files or path.startswith(("figures/", "evidence/")):
            expected = blob(ROOT, baseline, path)
            if not args.historical:
                require((ROOT / path).read_bytes() == expected, f"Merge release changed: {path}")
            protected[path] = sha(expected)
    receipt["protected_merge_baseline"] = baseline
    receipt["protected_merge_files_sha256"] = protected
    for project, (revision, exceptions) in SOURCES.items():
        config = manifest["projects"][project]
        repo, pin = ROOT.parent / config["repo"], config["commit"]
        if not args.historical:
            require(git(repo, "rev-parse", "HEAD").decode().strip() == revision, f"{project}: HEAD changed")
            require(not git(repo, "status", "--porcelain", "--untracked-files=all").strip(), f"{project}: dirty source")
        git(repo, "merge-base", "--is-ancestor", pin, revision)
        old, new = tree(repo, pin), tree(repo, revision)
        changed = sorted(p for p in old.keys() | new.keys() if old.get(p) != new.get(p))
        require(set(changed) == exceptions.keys(), f"{project}: unreviewed or missing delta: {changed}")
        deltas = {}
        for path in changed:
            before, after = blob(repo, pin, path), blob(repo, revision, path)
            deltas[path] = {"reason": exceptions[path], "old_tree_entry": old[path], "new_tree_entry": new[path],
                            "old_sha256": sha(before), "new_sha256": sha(after)}
        bundle_drift = []
        for path, entry in config["files"].items():
            require(sha(blob(repo, pin, path)) == entry["sha256"], f"{project}/{path}: pin mismatch")
            current = blob(repo, revision, path)
            if not args.historical:
                require((repo / path).read_bytes() == current, f"{project}/{path}: live mismatch")
            if sha(current) != entry["sha256"]:
                bundle_drift.append(path)
        require(bundle_drift == (["REPORT.md"] if project == "q22" else []), f"{project}: unexpected pin drift")
        if project == "q14":
            prior, current = (blob(repo, rev, "EXPERIMENTS.tsv").splitlines() for rev in (pin, revision))
            require(current[:len(prior)] == prior and len(current) == len(prior) + 2, "Q1.4 ledger changed")
            require([row.split(b"\t")[1] for row in current[len(prior):]] ==
                    [b"I122-merge-check", b"I130-rounding-verify"], "Q1.4 new experiment row")
            check = json.loads(blob(repo, revision, "results/reviews/merge_check.json"))
            require(check["json_mismatches"] == [] and len(check["quotes_not_found"]) == 2 and
                    all("0.74 [0.66, 0.81]" in quote for quote in check["quotes_not_found"]), "Q1.4 check changed")
            diagnostics = {"source_check": check, "note": "Two quote misses use the source's double-rounded 0.81; merge replay gives 0.80. Not a clean quotes check; disclosed, reviewed, no open P1."}
        else:
            before, after = (blob(repo, rev, "REPORT.md").splitlines(keepends=True) for rev in (pin, revision))
            added = [line for line in after if line not in before]
            require(len(added) == 1 and added[0].startswith(b"- 2026-10-25 10:21 UTC:"), "Q2.2 report drift changed")
            require([line for line in after if line != added[0]] == before, "Q2.2 report other drift")
            before, after = (blob(repo, rev, "p2_strongF_fig.py") for rev in (pin, revision))
            require(before.replace(b"market mean, 2nd half", "market mean, rounds 11–40".encode()) == after,
                    "Q2.2 renderer calculation changed")
            prior, current = (json.loads(blob(repo, rev, "results/analysis/phase2_reproduction.json"))
                              for rev in (pin, revision))
            for item in (prior, current):
                for key in ("started_utc", "finished_utc", "git_head", "input_sha256"):
                    item.pop(key)
                for command in item["commands"]:
                    command.pop("seconds")
            require(prior == current, "Q2.2 reproduction outputs/commands changed")
            diagnostics = {"source_reproduction_saved_output_comparison": "identical after removing dates, git revision, input hash inventory and per-command elapsed seconds"}
        receipt["projects"][project] = {"repo": config["repo"], "pin": pin, "head": revision,
            "pin_tree_files": len(old), "head_tree_files": len(new), "unchanged_tree_files": len(new) - len(changed),
            "changed_files": deltas, "bundled_files": len(config["files"]), "bundled_live_drift": bundle_drift,
            "diagnostics": diagnostics}
        if not args.historical:
            require(git(repo, "rev-parse", "HEAD").decode().strip() == revision and
                    not git(repo, "status", "--porcelain", "--untracked-files=all").strip(), f"{project}: concurrent change")
    receipt["checked_at_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    receipt["scope"] = (("Historical Git commits only; all live source/merge checking omitted. " if args.historical else
        "Live HEADs/worktrees and bundled files checked. ") +
        "Read-only tracked source Git-tree and 158-file pin reconciliation, not a scientific reanalysis, "
        "new experiment, source export or independent claims review. Ignored/untracked experiment caches are outside Git-tree coverage; "
        "worktrees must have no reportable changes. Current zero-P1 judgment comes from recorded source scope reviews. "
        "Historical snapshots remain the evidence pins; no repin performed.")
    receipt["ok"] = True
    args.output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({p: {k: v for k, v in row.items() if k in
                         {"head", "unchanged_tree_files", "bundled_files", "bundled_live_drift"}}
                      for p, row in receipt["projects"].items()}, indent=2))


if __name__ == "__main__":
    main()
