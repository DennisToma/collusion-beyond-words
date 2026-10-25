# Iteration 11 — independent scientific diff review

Reviewer: fresh-context **gpt-6.1-sol**, high reasoning, read-only. Reviewed SUBMISSION, SLIDES and README
changes against Q2.2 `salt_d1.py` at the pinned commit, the saved JSON, and primary literature. No files
edited, experiments run or simulated seller/auditor calls made. This is a claims review, not a new evaluation.

## Finding and resolution

**P2, fixed:** related work described Cao & Hu's shared-advisor result as occurring without coordination.
The primary v3 paper explicitly describes implicit coordination without communication between sellers.
Changed to “model supracompetitive prices from a shared AI advisor without communication between sellers.”
The reviewer re-read the corrected paragraph and confirmed the P2 resolved.

Primary evidence: [Cao & Hu v3, §1](https://arxiv.org/html/2601.01279v3).

## Final verification

The reviewer checked the final SALT sensitivity and the four new document bindings against
`E105_audit.auroc_no_verdict_words`: point `0.752089552238806`, CI
`[0.6583226334083009, 0.835771585845047]`, `n = 117`. The printed `0.75 [0.66, 0.84]` and sample size
are correct. Calling this a selected-subset comparison rather than a causal ablation is appropriate.

The source `PROMPT`, `render`, `report` and `cluster_boot` support separate communication/verdict phases,
message-only auditor input and a run-cluster bootstrap. The main SALT values, the original sample size
and the share without explicit agreement also match the pinned JSON.

Rose's causal versus operational distinction agrees with [v5 Definitions 4.7 and 4.7′](https://arxiv.org/html/2604.01151v5).
The “no robust contemporaneous co-movement” headlines are sufficiently qualified by the explicit
base-Qwen3.6 exception, failed grid replication and sensitivity limits.

Two small bookkeeping issues were reported and fixed: REPORT's check-count numerators and the missing
M35 provenance row. The optional precision-method scope suggestion was also applied: Methods now
attributes the printed Jeffreys precision interval specifically to Q1.4.

**Final reviewer conclusion: no open scientific P1/P2.** Numeric source checks, reproduction tests and
PDF checks are separate receipts; this review does not certify every unbound claim.
