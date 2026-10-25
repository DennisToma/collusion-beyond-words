# Fallback iteration 6 — primary-upload handoff

Verified committed release: `7c7be5e15e0cd205d9fbb1d95870fb195bd0016c`.

Command:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-fallback-i6-verified
cd /var/tmp/bw-fallback-i6-verified
sha256sum -c SHA256SUMS
```

All 11 commands / 53 tests pass in an extracted Git archive without `.git`, with absent sibling
roots and no model environment variables passed to checks. All 295 tracked files retain their Git
bytes/modes after the checks. All 20 handoff checksums pass. The code ZIP is 24,124,969 bytes,
with 294 merged files and 550/1387 source files. Both source archives match the existing frozen
pins and every included regular file matches its Git bytes; 8 oversized/HTML files are excluded.
The code ZIP is scanned for secret patterns before publication.

Receipt: `results/release_package_fallback_i6.json`. It describes this tested implementation
commit and predates these notes. No scientific file, report/PDF, figure or upload form changes
in the notes commit. The external handoff's own receipt records its exact revision.

Package the final notes commit too (same existing environment and source Git checkouts):

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-fallback-i6-final
cp /var/tmp/bw-fallback-i6-final/submission_code.zip submission_code.zip
cd /var/tmp/bw-fallback-i6-final
sha256sum -c SHA256SUMS
```

Primary uploads: `TEMPLATE_REPORT.pdf`, `IMAGE.png`, `submission_code.zip`; form fields in
`SUBMISSION_FORM.md`. Optional: extended `SUBMISSION.pdf`, `SLIDES.pdf`.
Existing Python/browser on the same author VM, not another installation or OS-portability test.
No submission, transfer or repository-visibility change was performed. Dennis must upload the files.
