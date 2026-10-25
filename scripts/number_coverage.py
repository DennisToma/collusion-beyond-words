"""List every decimal number in SUBMISSION.md (main text, before Reproducibility) and SLIDES.md
and say whether a document binding checks it against saved source data.

Unbound tokens are written with context so a reader can see exactly what is not
machine-checked (mostly chance levels, thresholds and model names).

    uv run python scripts/number_coverage.py   # -> results/number_coverage.json
"""
import json
import re

from document_checks import normalize
from evidence import ROOT

SLOT = r"([+-]?(?:\d+(?:\.\d+)?|\.\d+))(?!\d)"
TOKEN = r"(?<![\w.])[+-]?\d+\.\d+"


def main():
    bindings = json.loads((ROOT / "results/document_bindings.json").read_text())
    out = {}
    for doc in ("SUBMISSION.md", "SLIDES.md"):
        text = (ROOT / doc).read_text()
        if doc == "SUBMISSION.md":
            text = text.split("\n## Reproducibility")[0]
        text = normalize(text)
        spans = []
        for b in bindings:
            if b["document"] != doc:
                continue
            pattern = SLOT.join(re.escape(c) for c in normalize(b["template"]).split("{}"))
            for m in re.finditer(pattern, text):
                spans += [m.span(g) for g in range(1, m.lastindex + 1)]
        tokens = list(re.finditer(TOKEN, text))
        unbound = [{"token": m.group(), "context": text[max(0, m.start() - 70):m.end() + 20]}
                   for m in tokens if not any(s <= m.start() < e for s, e in spans)]
        out[doc] = {"decimal_tokens": len(tokens), "bound": len(tokens) - len(unbound), "unbound": unbound}
        print(f"{doc}: {len(tokens) - len(unbound)}/{len(tokens)} decimal tokens bound")
    (ROOT / "results/number_coverage.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
