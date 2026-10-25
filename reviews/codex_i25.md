# Iteration 25 — independent locked-test replay review

Reviewer: codex gpt-6.1-sol, high, read-only; iteration-25 implementation against HEAD d523c5b.
No experiments or auditor calls. Review output follows verbatim.

No actionable findings.

- [Replay calculation](/home/factory/collusion/collusion-beyond-words/scripts/recompute_locked_test_q22.py:40) matches the pinned source: IDs 0030–0124, 48 explicit + 2 information-exchange positives, 45 negatives, six cached run-score views, seed 0, B=2000, paired stratified sampling, and `max(text, action)` recomputed within each resample.
- Independent in-memory execution of the git-pinned analysis functions matched all six rounded AUROC estimates/CIs and eight contrasts. The replay regenerated [locked_test_q22.json](/home/factory/collusion/collusion-beyond-words/results/locked_test_q22.json) byte-identically.
- All nine added blobs match `git show 91ffb2d…:<path>` exactly. All earlier 98 manifest entries and project metadata remain unchanged against `HEAD`; all 107 stored blobs pass hash and size checks.
- [Parity tests](/home/factory/collusion/collusion-beyond-words/tests/test_reproduction.py:175) meaningfully execute original functions with an independent rank-sum AUROC calculation. Both added methods passed directly. An in-memory fixed-best-view mutation changes fixture contrasts, confirming that the fixture catches that regression.

Reviewed the documentation updates that arrived during the review: README, REPORT, SUBMISSION Reproducibility, SOURCES, and evidence README. They accurately describe saved-evidence reproduction and exclude new held-out evaluation, thresholds, fusion, and pair endpoints.

No files written, model calls, experiments, or other reviewers launched. The file-writing release suite was not rerun.

## Manager disposition

No actionable findings. The reviewer independently ran the original full B=2000 analysis in memory,
checked all nine new git blobs and previous 98 manifest entries, regenerated the output bytes,
and verified that the tied fixture rejects fixed best-single-view selection. No implementation
changes were needed. Full finalize/export and visual checks passed separately.
