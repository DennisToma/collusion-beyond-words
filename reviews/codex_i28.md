# Iteration 28 — independent scripted-gate replay review

Reviewed 2026-10-25 12:50 UTC; gpt-6.1-sol, reasoning effort high, read-only Codex CLI.
Scope: pending changes against merge HEAD `118344c`; no source-repo writes, experiments or auditor calls.

No actionable P1/P2 findings.

Independent verification completed:

- All 157 evidence blobs match `git show` at the pinned commits, including hashes and byte lengths. The previous 146 manifest entries and stored blobs are unchanged.
- Independently reaggregated all nine caches: 500 runs, 27,000 rows, and 666 saved numeric fields. All non-AUROC values match exactly; maximum AUROC difference is `1.1102230246251565e-16`. Exported event counts also match.
- Confirmed strict alpha, cached max-statistic run p-values, same-shock-family references, `1e-12` near-tie tolerance, leave-one-out controls, first-pair tie localization, Wilson intervals, and AUROC.
- The parity test reconstructs inputs independently and executes pinned source functions; its rank-based AUROC reference differs from the implementation’s pair-comparison estimator. Parity and malformed-input tests pass, including the 44-run boundary/tie fixture.
- Inspected the standalone test and executed the script entry point with absent sibling paths, capturing its write in memory. Output is byte-identical to `results/gate_q14.json`.
- Reproducibility prose accurately limits the work to saved-score/p-value reaggregation and excludes score, trajectory, and null generation or ground-truth validation.
- Scientific main text, references/appendices, and `SLIDES.md` are byte-unchanged. All eight slide PDF content streams are unchanged; submission PDF pages 1–10 have unchanged text.

No files were edited, and no models, detectors, markets, null draws, or new research evaluations were run.