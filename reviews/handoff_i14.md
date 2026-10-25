# Iteration 14 — hard-stop upload handoff

Research is stopped at the user's 18:00 UTC deadline. Only closure of the unfinished
committed-revision handoff is performed. The iteration-13 package directory does not
exist; prior notes described intended work. The completed i12 handoff for `248db6e`
was reverified (11 successful command logs, 308 Git-matching files, all artifact hashes,
20 checksums and root ZIP identity). No scientific or upload artifact changed.

After committing/pushing these closure notes, run:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-final-i14
cp /var/tmp/bw-final-i14/submission_code.zip submission_code.zip
cd /var/tmp/bw-final-i14
sha256sum -c SHA256SUMS
```

Run each step only after the previous one succeeds. The existing packager verifies
all 11 acceptance commands in an extracted archive, committed Git bytes/modes, ZIP
membership and both frozen source pins, secret patterns and the 25 MB size limit.
The external receipt records actual completion, accepted revision and artifact hashes;
these notes describe the procedure and do not claim acceptance before it occurs.
The existing same-VM environment/browser is reused. No PDF rebuild, usage refresh,
experiment, model call, new analysis or scientific edit is performed.

Upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png` and `submission_code.zip`; use
`SUBMISSION_FORM.md` for form fields. Optional: `SUBMISSION.pdf`, `SLIDES.pdf`.
Root ZIP must match the final package. Dennis must submit the form; no upload,
transfer, repository-visibility change or access grant is performed here.
