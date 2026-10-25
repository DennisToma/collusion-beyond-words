"""Export SUBMISSION.md and SLIDES.md to PDF (no results recomputed). Adapted from Q1.4 scripts/export_pdf.py.

uv run --group export playwright install chromium   # once
uv run --group export python scripts/export_pdf.py

Writes SUBMISSION.html (single file, figures embedded), SUBMISSION.pdf (A4) and SLIDES.pdf
(one landscape page per slide; slides are separated by '---' lines in SLIDES.md).
Checks all Markdown text fragments, slide placement, figure pixels and portable links.
Slide text must fit inside the page padding at 14 pt or larger; figures shrink first.
"""
import base64
from collections import Counter
import hashlib
import html
import json
import re
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit

from markdown_it import MarkdownIt
from PIL import Image
from playwright.sync_api import sync_playwright
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/DennisToma/collusion-beyond-words/blob/main/"
MIN_SLIDE_PT = 14

CSS = """
:root { font-family: system-ui, sans-serif; color: #17243b }
body { margin: 0 } main { max-width: 1000px; margin: 24px auto; padding: 0 32px }
h1 { font-size: 26px; line-height: 1.25 } h2 { font-size: 21px; margin-top: 30px } h3 { font-size: 18px }
h1, h2, h3, h4 { break-after: avoid }
p, li { font-size: 15px; line-height: 1.5 }
img { display: block; max-width: 100%; height: auto; margin: 12px auto; break-inside: avoid }
pre { padding: 12px; background: #f2f5f9; white-space: pre-wrap; overflow-wrap: anywhere; font-size: 12px }
code { font-size: .88em; overflow-wrap: anywhere }
table { border-collapse: collapse; font-size: 12px; margin: 12px 0; font-variant-numeric: tabular-nums }
th, td { padding: 5px 7px; border: 1px solid #d7dfeb; text-align: left; vertical-align: top }
th { background: #f2f5f9 }
.note { font-size: 12px; color: #53647a }
@media print {
  @page { size: A4 portrait; margin: 15mm 13mm }
  main { margin: 0; padding: 0; max-width: none }
  p, li { font-size: 9.5pt; line-height: 1.35 } h1 { font-size: 17pt } h2 { font-size: 14pt } h3, h4 { font-size: 11pt }
  table { font-size: 7.5pt } tr { break-inside: avoid } thead { display: table-header-group }
  img { max-height: 115mm; object-fit: contain }
  h2.end-matter { break-before: page }
}
"""

SLIDE_CSS = """
:root { font-family: system-ui, sans-serif; color: #17243b }
body { margin: 0 }
@page { size: 297mm 167mm; margin: 0 }
section { width: 297mm; height: 167mm; padding: 9mm 13mm; box-sizing: border-box; overflow: hidden;
          page-break-after: always; break-after: page; font-size: 16pt }
h1 { font-size: 1.7em; margin: 0 0 .35em } h2 { font-size: 1.6em; margin: 0 0 .35em }
p, li { font-size: 1em; line-height: 1.3; margin: .2em 0 }
img { display: block; max-height: 100mm; max-width: 100%; margin: 2mm auto }
table { border-collapse: collapse; font-size: max(14pt, .8em); margin: 2mm 0 } th, td { padding: 2pt 5pt; border: 1px solid #d7dfeb }
th { background: #f2f5f9 } code { font-size: max(14pt, .88em) }
"""

# Keep readable text; use less figure height before accepting a smaller font.
# Bounds include the page's padding, which scrollHeight alone cannot enforce.
FIT_JS = """() => [...document.querySelectorAll('section')].map(s => {
  const minTextPt = () => {
    const sizes = [], walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      if (walker.currentNode.textContent.trim())
        sizes.push(parseFloat(getComputedStyle(walker.currentNode.parentElement).fontSize) * 0.75);
    }
    return Math.min(...sizes);
  };
  const bounds = () => {
    const box = s.getBoundingClientRect(), css = getComputedStyle(s);
    return {left: box.left + parseFloat(css.paddingLeft),
            right: box.right - parseFloat(css.paddingRight),
            top: box.top + parseFloat(css.paddingTop),
            bottom: box.bottom - parseFloat(css.paddingBottom)};
  };
  const outside = r => {
    const b = bounds();
    return r.width > 0 && r.height > 0 &&
      (r.left < b.left - 1 || r.right > b.right + 1 || r.top < b.top - 1 || r.bottom > b.bottom + 1);
  };
  const overflows = () => {
    if (s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1) return true;
    if ([...s.querySelectorAll('img')].some(i => outside(i.getBoundingClientRect()))) return true;
    const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      if (!walker.currentNode.textContent.trim()) continue;
      const range = document.createRange(); range.selectNodeContents(walker.currentNode);
      if ([...range.getClientRects()].some(outside)) return true;
    }
    return false;
  };
  let pt = 16, height = 100;
  for (height = 100; height >= 55; height -= 5) {
    for (const img of s.querySelectorAll('img')) img.style.maxHeight = height + 'mm';
    for (pt = 16; pt >= 14; pt -= 0.5) {
      s.style.fontSize = pt + 'pt';
      if (!overflows() && minTextPt() >= 14 - 0.01)
        return {font_pt: pt, min_text_font_pt: minTextPt(), image_max_height_mm: height, overflow: false};
    }
  }
  s.style.fontSize = '14pt';
  return {font_pt: 14, min_text_font_pt: minTextPt(), image_max_height_mm: 55, overflow: true};
})"""


def md():
    return MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")


def embed_images(body):
    def repl(m):
        src = m.group(1)
        path = ROOT / src
        if not path.is_file():
            raise FileNotFoundError(f"Missing figure: {path}")
        data = base64.b64encode(path.read_bytes()).decode()
        return f'src="data:image/png;base64,{data}"'
    return re.sub(r'src="(figures/[^"]+\.png)"', repl, body)


def portable_links(body):
    """Resolve repo-relative links for downloaded PDFs and the standalone HTML."""
    def repl(match):
        href = html.unescape(match.group(1))
        if href.startswith("#") or urlsplit(href).scheme or href.startswith("//"):
            return match.group(0)
        if href.startswith("/") or ".." in Path(urlsplit(href).path).parts:
            raise ValueError(f"Link is outside the repository: {href}")
        if not (ROOT / urlsplit(href).path).is_file():
            raise FileNotFoundError(f"Missing link target: {href}")
        return f'href="{html.escape(REPO_URL + href, quote=True)}"'
    return re.sub(r'href="([^"]+)"', repl, body)


def page(title, css, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{css}</style></head><body>{body}</body></html>\n')


def plain(s):
    """Markdown cell/heading -> text as it appears in the PDF (approx.)."""
    codes = re.findall(r"`([^`]*)`", s)
    s = re.sub(r"`[^`]*`", "\x00", s)
    s = s.replace("**", "").replace("\\*", "").replace("*", "")
    for c in codes:  # code spans keep literal '*'
        s = s.replace("\x00", c, 1)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return s.strip()


def norm(s):
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", s)).replace("−", "-").replace("–", "-")


def text_fragments(source):
    """Rendered text of each heading, paragraph, list item, table cell and code block.

    Use Markdown tokens rather than source punctuation: emphasis, links and list
    markers do not appear literally in the PDF. Images are verified separately.
    """
    fragments = []
    for token in md().parse(source):
        if token.type == "inline":
            text = "".join(c.content if c.type in ("text", "code_inline") else
                           " " if c.type in ("softbreak", "hardbreak") else ""
                           for c in token.children)
            if text.strip():
                fragments.append(text)
        elif token.type in ("fence", "code_block"):
            fragments.append(token.content)
    return fragments


def check_pdf(pdf, needles, label, page_index=None):
    reader = PdfReader(pdf)
    pages = reader.pages if page_index is None else [reader.pages[page_index]]
    text = norm("".join(p.extract_text() or "" for p in pages))
    missing = [n for n in needles if norm(n) and norm(n) not in text]
    if missing:
        print(f"[FAIL] {label}: {len(missing)}/{len(needles)} fragments not found verbatim in PDF text: {missing}")
    else:
        print(f"[ok] {label}: all {len(needles)} fragments found in PDF text")
    return missing


def pixel_digest(image):
    return hashlib.sha256(image.convert("RGB").tobytes()).hexdigest()


def check_figures(pdf, source):
    """Match the actual embedded PDF image pixels and multiplicities to Markdown."""
    expected = Counter()
    for token in md().parse(source):
        for child in token.children or []:
            if child.type == "image":
                with Image.open(ROOT / child.attrGet("src")) as img:
                    expected[(img.size, pixel_digest(img))] += 1
    actual = Counter((img.image.size, pixel_digest(img.image))
                     for p in PdfReader(pdf).pages for img in p.images)
    if expected != actual:
        raise ValueError(f"PDF figure pixels/count mismatch: {pdf.name}")
    print(f"[ok] {pdf.name}: {sum(expected.values())} figures match source pixels exactly")
    return sum(expected.values())


def check_links(pdf):
    uris = []
    for p in PdfReader(pdf).pages:
        for annotation in p.get("/Annots", []):
            obj = annotation.get_object()
            action = obj.get("/A", {})
            uri = action.get("/URI")
            if action.get("/S") in ("/Launch", "/GoToR") or (uri and urlsplit(uri).scheme not in ("https", "http", "mailto")):
                raise ValueError(f"Nonportable PDF link: {action}")
            if uri:
                uris.append(str(uri))
    return uris


def main():
    report_md = (ROOT / "SUBMISSION.md").read_text()
    body = portable_links(embed_images(md().render(report_md)))
    # Separate excluded references/appendices from the eight-page main-text limit.
    # This also makes the first References PDF page an unambiguous boundary.
    for heading in ("References", "Appendix — full tables"):
        body = body.replace(f"<h2>{heading}</h2>", f'<h2 class="end-matter">{heading}</h2>')
    note = ('<p class="note">Export of SUBMISSION.md (scripts/export_pdf.py); no results recomputed. '
            'Source paths refer to the repository.</p>')
    (ROOT / "SUBMISSION.html").write_text(page("SUBMISSION", CSS, f"<main>{note}{body}</main>"))

    slides_md = (ROOT / "SLIDES.md").read_text()
    slides = [s for s in re.split(r"(?m)^---\s*$", slides_md) if s.strip()]
    slide_html = "".join(f"<section>{portable_links(embed_images(md().render(s)))}</section>" for s in slides)

    with tempfile.TemporaryDirectory(prefix="bw-export-", dir="/var/tmp") as scratch, sync_playwright() as p:
        slides_file = Path(scratch) / "slides.html"
        slides_file.write_text(page("SLIDES", SLIDE_CSS, slide_html))
        b = p.chromium.launch()
        pg = b.new_page()
        pg.emulate_media(media="print")
        pg.goto((ROOT / "SUBMISSION.html").as_uri(), wait_until="load")
        validate_browser_images(pg)
        pg.pdf(path=str(ROOT / "SUBMISSION.pdf"), prefer_css_page_size=True, print_background=True)
        pg.goto(slides_file.as_uri(), wait_until="load")
        validate_browser_images(pg)
        fit = pg.evaluate(FIT_JS)
        print("slide base font (pt):", [f["font_pt"] for f in fit])
        overflow = [f["overflow"] for f in fit]
        if any(overflow):
            raise ValueError(f"Slides cannot fit at {MIN_SLIDE_PT} pt: {[i+1 for i,o in enumerate(overflow) if o]}")
        pg.pdf(path=str(ROOT / "SLIDES.pdf"), prefer_css_page_size=True, print_background=True)
        b.close()

    # checks: headings + table cells of the report, slide titles + page count of the deck
    heads = [plain(h) for h in re.findall(r"(?m)^#{2,4} (.+)$", report_md)]
    cells = []
    for line in report_md.splitlines():
        if line.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", line):
            cells += [plain(c.replace("\\|", "|")) for c in re.split(r"(?<!\\)\|", line.strip().strip("|")) if plain(c)]
    missing = check_pdf(ROOT / "SUBMISSION.pdf", heads, "SUBMISSION headings")
    missing += check_pdf(ROOT / "SUBMISSION.pdf", cells, "SUBMISSION table cells")
    n = len(PdfReader(ROOT / "SLIDES.pdf").pages)
    titles = [plain(re.search(r"(?m)^#{1,2} (.+)$", s).group(1)) for s in slides if re.search(r"(?m)^#{1,2} ", s)]
    print(f"[{'ok' if n == len(slides) else 'FAIL'}] deck: {n} PDF pages for {len(slides)} slides")
    if any(overflow):
        print(f"[FAIL] slides overflowing their page: {[i + 1 for i, o in enumerate(overflow) if o]}")
    missing += check_pdf(ROOT / "SLIDES.pdf", titles, "slide titles")
    fragments = text_fragments(report_md)
    missing += check_pdf(ROOT / "SUBMISSION.pdf", fragments, "SUBMISSION all text fragments")
    slide_fragment_counts = []
    if n == len(slides):
        for index, slide in enumerate(slides):
            slide_fragments = text_fragments(slide)
            slide_fragment_counts.append(len(slide_fragments))
            missing += check_pdf(ROOT / "SLIDES.pdf", slide_fragments, f"slide {index+1} all text on correct page", index)
    figure_counts = {"SUBMISSION.pdf": check_figures(ROOT / "SUBMISSION.pdf", report_md),
                     "SLIDES.pdf": check_figures(ROOT / "SLIDES.pdf", slides_md)}
    links = {name: check_links(ROOT / name) for name in ("SUBMISSION.pdf", "SLIDES.pdf")}
    print(f"SUBMISSION.pdf pages: {len(PdfReader(ROOT / 'SUBMISSION.pdf').pages)}")
    if missing or any(overflow) or n != len(slides):
        raise SystemExit("Export verification failed; inspect the diagnostics above")
    receipt = {"command": "uv run --group export python scripts/export_pdf.py", "ok": True,
               "submission_pages": len(PdfReader(ROOT / "SUBMISSION.pdf").pages),
               "slides": n, "headings": len(heads), "table_cells": len(cells),
               "submission_text_fragments": len(fragments), "slide_text_fragments": slide_fragment_counts,
               "slide_layout": fit, "minimum_slide_font_pt": MIN_SLIDE_PT,
               "figure_counts": figure_counts, "pdf_links": links,
               "sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                          for name in ("SUBMISSION.md", "SLIDES.md", "SUBMISSION.pdf", "SLIDES.pdf", "scripts/export_pdf.py")},
               "scope": "Text presence, per-slide placement, browser content bounds, embedded figure pixels and link schemes; not scientific validity or a guarantee of chart-label readability."}
    (ROOT / "results/export_check.json").write_text(json.dumps(receipt, indent=2) + "\n")


def validate_browser_images(pg):
    bad = pg.evaluate("() => [...document.images].filter(i => !i.complete || !i.naturalWidth || !i.naturalHeight).map(i => i.alt)")
    if bad:
        raise ValueError(f"Images did not load: {bad}")


if __name__ == "__main__":
    main()
