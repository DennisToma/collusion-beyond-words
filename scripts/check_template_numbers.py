"""Cross-check every decimal, percentage and fraction in TEMPLATE_REPORT.md against the script-bound SUBMISSION.md.

TEMPLATE_REPORT.md is a re-edit of SUBMISSION.md (whose result decimals are bound to saved source data
by results/document_bindings.json and scripts/number_coverage.py). A template number that does not occur
in SUBMISSION.md, or in a small whitelist of non-result values, fails this check.

    uv run python scripts/check_template_numbers.py   # -> results/template_number_check.json
"""
import json
import re
import sys

from document_checks import normalize
from evidence import ROOT

TOKEN = r"(?<![\w.])[+\-−]?\d+\.\d+%?|(?<![\w.])\d+%|(?<![\w./])\d+/\d+(?![\w/])"
# Non-result values: model versions, section/appendix numbers, design parameters stated in the text.
WHITELIST = {
    "5.5", "6.1", "5.6",  # model versions (Opus 5.5, gpt-6.1-sol, gpt-5.6-terra)
    "0.5",                # chance level
    "0.05",               # alpha
}


def canon(tok):
    return tok.replace("−", "-").lstrip("+")


def main():
    template = normalize((ROOT / "TEMPLATE_REPORT.md").read_text())
    submission = normalize((ROOT / "SUBMISSION.md").read_text())
    sub_tokens = {canon(m.group()) for m in re.finditer(TOKEN, submission)}
    rows, missing = [], []
    for m in re.finditer(TOKEN, template):
        tok = canon(m.group())
        ok = tok in sub_tokens or tok in WHITELIST
        ctx = template[max(0, m.start() - 50):m.end() + 20].replace("\n", " ")
        rows.append({"token": m.group(), "in_submission": tok in sub_tokens, "whitelisted": tok in WHITELIST})
        if not ok:
            missing.append({"token": m.group(), "context": ctx})
    # Stricter: every "estimate [lo, hi]" triple must occur verbatim (canonicalised) in SUBMISSION.md.
    ci = r"[+\-−]?\d*\.?\d+%? \[[+\-−]?\d*\.?\d+%?, ?[+\-−]?\d*\.?\d+%?\]"
    norm = lambda t: re.sub(r"\s+", "", t.replace("−", "-").replace("+", ""))
    sub_ci = {norm(m.group()) for m in re.finditer(ci, submission)}
    ci_rows = [m.group() for m in re.finditer(ci, template)]
    ci_missing = [t for t in ci_rows if norm(t) not in sub_ci]
    missing += [{"token": t, "context": "estimate+CI triple not verbatim in SUBMISSION.md"} for t in ci_missing]
    out = {"tokens": len(rows), "ci_triples": len(ci_rows), "unmatched": missing}
    (ROOT / "results/template_number_check.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"TEMPLATE_REPORT numeric tokens: {len(rows)}, CI triples: {len(ci_rows)}; unmatched in SUBMISSION.md: {len(missing)}")
    for x in missing:
        print(f"  {x['token']!r}: …{x['context']}…")
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
