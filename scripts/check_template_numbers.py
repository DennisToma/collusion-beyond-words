"""Inventory primary-report decimals, percentages and fractions and require context coverage.

TEMPLATE_REPORT.md is a re-edit of SUBMISSION.md (whose result decimals are bound to saved source data
by results/document_bindings.json and scripts/number_coverage.py). A template number that does not occur
in SUBMISSION.md, or in a small whitelist of non-result values, fails this check.
In scientific sections, each token must also occur in a section-scoped binding or
a narrowly located non-result category. check_sources.py separately checks those
bindings against the frozen source values; this inventory does not replace it.
References, code metadata, prompts and process disclosures are outside contextual
coverage. Integer-only and qualitative claims still need human/source review.

    uv run python scripts/check_template_numbers.py   # -> results/template_number_check.json
"""
import hashlib
import json
import re
import sys

from document_checks import binding_matches, normalize
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


def check_numbers(template_source, submission_source, bindings):
    template = normalize(template_source)
    submission = normalize(submission_source)
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
    # Context coverage excludes references, code/archive metadata, prompts and
    # process disclosures. Every scientific decimal/percentage/fraction must be
    # a source slot, reviewed literal context, or a narrowly located non-result.
    ranges = [(template.index(normalize("## Abstract")), template.index(normalize("## Code and Data"))),
              (template.index(normalize("### A. Extended results")),
               template.index(normalize("### C. Prompts")))]
    matches = [m for b in bindings for m in binding_matches(template, b)]
    slots = [m.span(g) for m in matches for g in range(1, (m.lastindex or 0) + 1)]
    coverage = []
    for m in re.finditer(TOKEN, template):
        if not any(s <= m.start() < e for s, e in ranges):
            continue
        context = template[max(0, m.start()-45):m.start()] + "⟨" + m.group() + "⟩" + template[m.end():m.end()+18]
        # A fraction can contain a source slot for its numerator and a fixed,
        # reviewed denominator; the containing binding checks both positions.
        kind = next(("source_slot" for s, e in slots if s <= m.start() and m.end() <= e), None)
        if kind is None and any(x.start() <= m.start() and m.end() <= x.end() for x in matches):
            kind = "fixed_binding_context"
        if kind is None:
            for category, rx in (
                ("model version", r"(gpt-|Opus |Sonnet )⟨\d+\.\d+⟩"),
                ("chance level", r"⟨0\.5⟩ = chance|Below ⟨0\.5⟩|below ⟨0\.5⟩"),
                ("alpha", r"α = ⟨0\.05⟩"),
                ("confidence level", r"⟨95%⟩ (CIs?|Wilson CIs?|game-bootstrap|run-level bootstr)"),
            ):
                if re.search(rx, context):
                    kind = category
                    break
        coverage.append(dict(token=m.group(), category=kind, context=context))
    unclassified = [r for r in coverage if r["category"] is None]
    missing += [{"token": r["token"], "context": "no context binding: " + r["context"]} for r in unclassified]
    return {"tokens": len(rows), "ci_triples": len(ci_rows), "unmatched": missing,
            "context_coverage": coverage, "unclassified": len(unclassified)}


def main():
    template = (ROOT / "TEMPLATE_REPORT.md").read_text()
    submission = (ROOT / "SUBMISSION.md").read_text()
    binding_path = ROOT / "results/template_document_bindings.json"
    out = check_numbers(template, submission, json.loads(binding_path.read_text()))
    out.update(template_sha256=hashlib.sha256(template.encode()).hexdigest(),
               bindings_sha256=hashlib.sha256(binding_path.read_bytes()).hexdigest())
    (ROOT / "results/template_number_check.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"TEMPLATE_REPORT numeric tokens: {out['tokens']}, CI triples: {out['ci_triples']}; failures: {len(out['unmatched'])}; "
          f"context inventory: {len(out['context_coverage'])}, unclassified: {out['unclassified']}")
    for x in out['unmatched']:
        print(f"  {x['token']!r}: …{x['context']}…")
    sys.exit(1 if out['unmatched'] else 0)


if __name__ == "__main__":
    main()
