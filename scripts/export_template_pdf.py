"""Export TEMPLATE_REPORT.md (Apart template version of the submission) to PDF; no results recomputed.
uv run --group export python scripts/export_template_pdf.py  ->  TEMPLATE_REPORT.html, TEMPLATE_REPORT.pdf
Reuses the SUBMISSION exporter's renderer and checks (all text fragments, figure pixels, portable links).
"""
import re

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

from export_pdf import (CSS, ROOT, check_figures, check_links, check_pdf, embed_images, md, page, portable_links,
                        text_fragments, validate_browser_images)

TEMPLATE_CSS = CSS + """
@media print { h2.end-matter { break-before: page } img { max-height: 105mm } }
blockquote { margin: 8px 0 8px 16px; padding-left: 10px; border-left: 3px solid #d7dfeb; color: #34465f }
"""


def main():
    source = (ROOT / "TEMPLATE_REPORT.md").read_text()
    body = portable_links(embed_images(md().render(source)))
    for heading in ("References",):
        body = body.replace(f"<h2>{heading}</h2>", f'<h2 class="end-matter">{heading}</h2>')
    (ROOT / "TEMPLATE_REPORT.html").write_text(page("Beyond Words", TEMPLATE_CSS, f"<main>{body}</main>"))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto((ROOT / "TEMPLATE_REPORT.html").as_uri(), wait_until="load")
        validate_browser_images(pg)
        pg.pdf(path=str(ROOT / "TEMPLATE_REPORT.pdf"), prefer_css_page_size=True, print_background=True)
        b.close()
    pdf = ROOT / "TEMPLATE_REPORT.pdf"
    fragments = [re.sub(r"<[^>]+>", "", f) for f in text_fragments(source)]
    missing = check_pdf(pdf, [f for f in fragments if f.strip()], "TEMPLATE_REPORT all text fragments")
    check_figures(pdf, source)
    check_links(pdf)
    reader = PdfReader(pdf)
    ref_page = next(i for i, pg_ in enumerate(reader.pages) if "References" in (pg_.extract_text() or "")
                    and "1. Agrawal" in (pg_.extract_text() or "").replace("\n", " ")) + 1
    print(f"TEMPLATE_REPORT.pdf pages: {len(reader.pages)}; main text = pages 1-{ref_page - 1}")
    if missing:
        raise SystemExit("Template export verification failed")


if __name__ == "__main__":
    main()
