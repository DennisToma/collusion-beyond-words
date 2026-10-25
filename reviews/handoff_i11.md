# Iteration 11 — final committed-revision handoff

The source freshness check is recorded in `results/release_hold_i11.json`:

```bash
uv run python reviews/verify_hold_i11.py
```

All 158 pinned evidence blobs match their source Git objects and bundled bytes;
176 scientific files retain the iteration-7 preservation hashes. Eight manuscript,
PDF, form and image files match accepted revision `77ab10d` exactly. Source advances
since the preceding handoff change only STATUS and Q2.2 review notes; both managers
declare zero open P1. Those notes were read, not treated as a new independent review.
No scientific estimate, manuscript, PDF, figure or usage snapshot changes.

After committing and pushing these notes, build the actual upload from that clean HEAD:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-final-i11
cp /var/tmp/bw-final-i11/submission_code.zip submission_code.zip
cd /var/tmp/bw-final-i11
sha256sum -c SHA256SUMS
```

The output directory must not already exist. Packaging requires all 11 release
commands to pass in an extracted archive with absent sibling paths; it verifies
committed files, source pins, ZIP members, the size limit and secret patterns.
The exact final revision, checks, archive size and hashes are recorded outside Git
in `/var/tmp/bw-final-i11/receipt.json`, avoiding a receipt that refers to itself.
This notes commit records the procedure and freshness result; its external receipt
is the authority for whether subsequent clean-HEAD packaging completed successfully.

Upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png` and `submission_code.zip`, using
`SUBMISSION_FORM.md` for the form. Optional supplements: `SUBMISSION.pdf`, `SLIDES.pdf`.
The root ZIP must match `/var/tmp/bw-final-i11/submission_code.zip`. The author still
needs to perform the upload; no transfer, submission or visibility change is made here.
