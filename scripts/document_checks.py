"""Extract selected printed claims and compare each directly with its saved source value.

Bindings use literal surrounding text with {} numeric slots. Every matching
occurrence is checked, including duplicate mentions. A missing binding fails.
This deliberately does not certify unbound numbers or semantic scope.
"""
from decimal import Decimal, ROUND_HALF_UP
import json
import re
import unicodedata

from evidence import ROOT


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(str.maketrans({"−": "-", "–": "-", "—": "-"}))
    text = text.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


SLOT = r"([+-]?(?:\d+(?:\.\d+)?|\.\d+))(?!\d)"


def binding_matches(text, binding):
    """Return matches in the declared section, retaining full-document offsets."""
    start, end = 0, len(text)
    if "section" in binding:
        first, last = map(normalize, binding["section"])
        if text.count(first) != 1 or text.count(last) != 1:
            return []
        start = text.index(first) + len(first)
        end = text.index(last)
        if end < start:
            return []
    pattern = SLOT.join(re.escape(x) for x in normalize(binding["template"]).split("{}"))
    return list(re.compile(pattern).finditer(text, start, end))


def check_documents(source_checks, documents, bindings=None):
    lookup = {f"{c['row']}:{c['what']}": c["got"] for c in source_checks}
    texts = {name: normalize(path.read_text()) for name, path in documents.items()}
    if bindings is None:
        bindings = json.loads((ROOT / "results/document_bindings.json").read_text())
    results = []
    for binding in bindings:
        source = lookup[binding["source_check"]]
        source = source if isinstance(source, list) else [source]
        indices = binding.get("indices", list(range(len(source))))
        expected = [Decimal(str(source[i])) * Decimal(str(binding.get("scale", 1))) for i in indices]
        template = normalize(binding["template"])
        chunks = template.split("{}")
        digits = binding["digits"]
        if len(chunks) - 1 != len(expected) or len(digits) != len(expected):
            raise ValueError(f"Numeric slot/source length mismatch: {binding}")
        matches = binding_matches(texts[binding["document"]], binding)
        extracted = []
        ok = bool(matches)
        if "expected_matches" in binding:
            ok = ok and len(matches) == binding["expected_matches"]
        for match in matches:
            printed = match.groups()
            extracted.append(list(printed))
            for actual, value, precision in zip(printed, expected, digits):
                decimal = Decimal(actual)
                # Precision is part of the reviewed binding. Deriving it from the
                # edited document would let a change such as 0.43 -> 0 pass.
                rounded = value.quantize(Decimal(1).scaleb(-precision), rounding=ROUND_HALF_UP)
                ok = ok and decimal == rounded
        results.append({**binding, "source_values": [str(v) for v in expected],
                        "printed_values": extracted, "matches": len(matches), "ok": bool(ok)})
    return results
