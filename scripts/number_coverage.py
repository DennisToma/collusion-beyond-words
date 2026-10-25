"""List every decimal in the report's main text and relocated scientific appendices, and SLIDES.md
and say whether a document binding checks it against saved source data.

Unbound tokens are written with context so a reader can see exactly what is not
machine-checked. Each one must fall into a declared non-result category (chance level,
alpha, design parameter, threshold, section number, model version, illustration);
an unbound token that fits none of them fails the run. Each pattern must match the token
itself, not just nearby text; the categories are a whitelist written for the current text.

    uv run python scripts/number_coverage.py   # -> results/number_coverage.json
"""
import json
import re

from document_checks import normalize
from evidence import ROOT

SLOT = r"([+-]?(?:\d+(?:\.\d+)?|\.\d+))(?!\d)"
TOKEN = r"(?<![\w.])[+-]?\d+\.\d+"
# (category, regex over the 40 chars before the token + token + 12 chars after); ⟨⟩ marks the token
CATEGORIES = [
    ("chance level 0.5", r"(⟨0\.5⟩ = (chance|inverted)|(<|∋|include|below|includes) ⟨0\.5⟩)"),
    ("alpha", r"α = ⟨0\.05⟩"),
    ("section number", r"(§|### |Q1\.4 §)⟨\d\.\d⟩"),
    ("model version", r"(gpt-⟨\d\.\d⟩-|(Sonnet|Opus) ⟨\d\.\d⟩)"),
    ("design parameter (planted move rate)", r"rate q = ⟨0\.1⟩"),
    ("precision threshold", r"precision ⟨0\.25⟩"),
    ("illustration of the bound Qwen3.8 range 0.15-0.21", r"An AUROC of ⟨0\.15⟩ means"),
]
# Every alternative must contain the marked token, so nearby text alone cannot classify a number.
assert all(all("⟨" in alt for alt in re.split(r"\|(?![^()]*\))", rx.strip("()"))) for _, rx in CATEGORIES)


def main():
    bindings = json.loads((ROOT / "results/document_bindings.json").read_text())
    out = {}
    failed = False
    for doc in ("SUBMISSION.md", "SLIDES.md"):
        text = (ROOT / doc).read_text()
        if doc == "SUBMISSION.md":
            # The submission-compliance cut moves previously checked scientific prose
            # to D-G. Keep checking it there; legacy verbatim tables A-C and process /
            # reproducibility appendices remain outside this decimal inventory.
            text = (text.split("\n## References")[0] + "\n" +
                    text.split("\n### D. Extended summary, glossary and operational labels\n", 1)[1]
                    .split("\n### H. AI assistance and pre-existing material\n", 1)[0])
        text = normalize(text)
        spans = []
        for b in bindings:
            if b["document"] != doc:
                continue
            pattern = SLOT.join(re.escape(c) for c in normalize(b["template"]).split("{}"))
            for m in re.finditer(pattern, text):
                spans += [m.span(g) for g in range(1, m.lastindex + 1)]
        tokens = list(re.finditer(TOKEN, text))
        unbound = []
        for m in tokens:
            if any(s <= m.start() < e for s, e in spans):
                continue
            window = text[max(0, m.start() - 40):m.start()] + "⟨" + m.group() + "⟩" + text[m.end():m.end() + 12]
            cat = next((c for c, rx in CATEGORIES if re.search(rx, window)), None)
            unbound.append({"token": m.group(), "category": cat,
                            "context": text[max(0, m.start() - 70):m.end() + 20]})
        bad = [u for u in unbound if u["category"] is None]
        out[doc] = {"decimal_tokens": len(tokens), "bound": len(tokens) - len(unbound),
                    "unbound": unbound, "unbound_unclassified": len(bad)}
        print(f"{doc}: {len(tokens) - len(unbound)}/{len(tokens)} decimal tokens bound; "
              f"{len(unbound) - len(bad)} unbound are non-results; {len(bad)} unclassified")
        for u in bad:
            print("  UNCLASSIFIED", u["token"], "|", u["context"])
        failed = failed or bool(bad)
    (ROOT / "results/number_coverage.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    if failed:
        raise SystemExit("unbound decimal outside every non-result category")


if __name__ == "__main__":
    main()
