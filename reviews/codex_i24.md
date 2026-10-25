# Iteration 24 — independent portable-replay review

Reviewer: codex gpt-6.1-sol, high, read-only; current iteration-24 implementation against HEAD f6f10df.
No experiments or auditor calls. Review output follows verbatim.

No open P1/P2 issues in the reviewed chunk. The standalone replay claim is supported for the pinned bundle and locked environment.

Checks passed:

- All **22 new blobs** match read-only sibling `git show` at manifest commit `91ffb2d`; stored/decompressed hashes and sizes match. All 98 evidence entries verify.
- M6 matches the original row/cell order, population, paired scoring and seed-0, B=2000 bootstrap: **7 contributing cells**.
- M33 matches the original regex, nonempty-message denominator, sorted run order and bootstrap: **15 no-channel runs**.
- M34 matches the original AUROC: **142/247**, with **13 strict / 19 tacit-high** runs.
- C21b matches every original per-run field across both datasets and all eight settings, including executed identities: **5/15 throughout**.
- Every unrounded value matches HEAD exactly; only `q22_commit` changes.

One nonblocking validation blind spot: [tests/test_reproduction.py:192](/home/factory/collusion/collusion-beyond-words/tests/test_reproduction.py:192) supplies `portable.REQ` to the reference function, so that comparison cannot independently detect a mapping error. Minimal fix: extract the pinned source’s `REQ` assignment and compare it too. I independently checked the current mappings; they match.

Validation ran entirely in memory with bytecode disabled. I did not run the file-writing release suite, edit files, invoke models, or review the updating docs.

## Manager disposition

No P1/P2. Applied the nonblocking reference-mapping suggestion: the parity test now extracts the original REQ dictionary from the pinned source AST, compares the two selected dataset mappings explicitly, and supplies the original mapping to the reference function. Dataset selection is fixed independently of the portable mapping. Release checks are rerun after this change.
