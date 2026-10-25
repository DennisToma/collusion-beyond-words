# Iteration 12 — final upload handoff

The completed iteration-11 package at `/var/tmp/bw-final-i11` certifies `2fe0265`:
11 successful commands, 307 tracked files verified against Git, 20 valid checksums,
and root `submission_code.zip` identical to the packaged ZIP. All accepted report,
slide, image and form bytes remain unchanged. The refreshed source provenance receipt
is `results/release_hold_i11.json`; command: `uv run python reviews/verify_hold_i11.py`.

Commit and push the iteration-12 notes, then package that clean HEAD:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-final-i12
cp /var/tmp/bw-final-i12/submission_code.zip submission_code.zip
cd /var/tmp/bw-final-i12
sha256sum -c SHA256SUMS
```

The output directory must not already exist. The package command runs all 11 acceptance
commands in an extracted archive with absent sibling paths and no model environment,
verifies every committed archive file and ZIP member against Git and the source pins,
and checks the size limit and secret patterns. It publishes the output directory only
after success. The external `receipt.json` records the exact revision and completion;
these notes record the procedure, not a claim that an unbuilt package already passed.
The existing author-VM Python/browser installation is reused.

Upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png` and `submission_code.zip`; use
`SUBMISSION_FORM.md` for form fields. Optional supplements: `SUBMISSION.pdf`, `SLIDES.pdf`.
The root ZIP must match `/var/tmp/bw-final-i12/submission_code.zip`. No upload, transfer,
repository-visibility change, PDF rebuild, usage refresh or new experiment is performed.
