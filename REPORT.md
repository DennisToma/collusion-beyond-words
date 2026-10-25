# REPORT

The merged submission is **[SUBMISSION.md](SUBMISSION.md)** ("Beyond Words: Detecting AI-Agent Collusion
Through Information Theory and Behavioral Evidence"). Number provenance: [SOURCES.md](SOURCES.md).
Figures: `figures/fig1–fig6` (copies of source-repo figures). This repo runs no new experiments.

- PDF: **[SUBMISSION.pdf](SUBMISSION.pdf)**; slides (8): **[SLIDES.pdf](SLIDES.pdf)** from [SLIDES.md](SLIDES.md).
- Rebuild: `uv run --group export playwright install chromium` (once), then
  `uv run --group export python scripts/export_pdf.py` (renders, then checks every heading, table cell and
  slide title is present in the PDF text, and that no slide overflows).
