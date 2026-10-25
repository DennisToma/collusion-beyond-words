# Fallback iteration 7 — verified numerical-context handoff

Implementation acceptance: `77ab10d38861d4b5434923f3b2abcb898f793dc6`.

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-fallback-i7-verified
cd /var/tmp/bw-fallback-i7-verified
sha256sum -c SHA256SUMS
```

All 11 commands / 57 tests pass in an extracted archive without `.git`, with nonexistent sibling
paths and no model environment variables passed. All 302 tracked files retain committed bytes/modes
and all 20 handoff checksums pass. The 24,181,531-byte code ZIP verifies 301 merged files plus
550/1387 source files against Git, and both source pins match the evidence manifest.
Receipt: `results/release_package_fallback_i7.json`. This receipt describes the implementation
commit before these notes. It is not a receipt for a later notes commit.

Run after committing/pushing these notes to include them in the actual final handoff:

```bash
uv run --group export python scripts/package_release.py --output-dir /var/tmp/bw-fallback-i7-final
cp /var/tmp/bw-fallback-i7-final/submission_code.zip submission_code.zip
cd /var/tmp/bw-fallback-i7-final
sha256sum -c SHA256SUMS
```

The final package's external `receipt.json` records its exact notes-HEAD revision and ZIP hash/size;
it stays outside Git to avoid a self-reference. The root `submission_code.zip` is ignored by Git
and must byte-match the final package. No further report, evidence, figure, source or PDF changes
are included in the notes commit.

Primary uploads: `TEMPLATE_REPORT.pdf`, `IMAGE.png`, `submission_code.zip`. Form text:
`SUBMISSION_FORM.md`. Optional: extended `SUBMISSION.pdf`, `SLIDES.pdf`.
This uses the existing author-VM Python/browser environment, not a fresh installation or an
OS-portability check. No submission, transfer or repository-visibility change was performed.
Dennis must upload the files.
