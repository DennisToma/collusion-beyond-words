# Fallback iteration 7 — primary numerical-context review

2026-10-25 UTC. Two independent read-only `codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s read-only` passes.
Scope: shared document matcher, source checker, primary inventory, primary bindings and targeted regression tests.
The reviewer performed nonmutating probes; the manager ran the full write-producing release suites.
No new scientific evaluation, auditor call or experiment. The primary report and slides were not rewritten.

## Initial review (two P2; no P1)

Two P2 findings; no P1 findings.

1. **P2: Table headers can reverse the reported endpoints without failing validation.** [template_document_bindings.json:855](/home/factory/collusion/collusion-beyond-words/results/template_document_bindings.json:855) binds numeric cells without checking their column headers. Swapping Table A2’s `text view | price view` headers makes the locked result report text AUROC 0.75 and price AUROC 0.47. All 65 bindings and the numeric inventory still pass. Validate table headers and row identities alongside cell positions, and add a header-swap regression test. The new numeric-slot tests do not cover this.

2. **P2: Appendix B silently escapes contextual numeric coverage.** [check_template_numbers.py:57](/home/factory/collusion/collusion-beyond-words/scripts/check_template_numbers.py:57) stops appendix coverage before “Limitations and Dual-Use / Ethical Considerations,” although that section discusses scientific results. Adding an unsupported `The auditor achieved AUROC 0.74.` there passes both validators because the token occurs elsewhere in SUBMISSION. Extend coverage through Appendix B, excluding prompts separately, and add a regression test for an unbound result in that section.

Checks performed: verified all 158 frozen evidence files; independently checked all 43 source keys referenced by the primary bindings, using the existing saved replay output for unrounded grid values; confirmed all 65 primary and 144 existing document bindings pass. All 135 individual numeric-slot mutations were rejected. Checked source mappings, scaling, rounding, deletion/swap rejection, and diff whitespace. No discrepancies found in the currently bound printed values.

Limitations: no files modified, write-producing tests or CLI checks run, model calls, agents, new estimates, or experiments. Bootstrap provenance was not rerun. Integer-only and qualitative claims remain outside the inventory’s documented coverage. The working tree changed externally during review; I reread the latest scoped diff before finishing.

## Fixes and follow-up

Table A1/A2 bindings now begin at the exact column-header line and end at the corresponding caption.
The locked row's label and contrast are included in its binding. The inventory now continues through
Appendix B, stopping before the prompts. Failure tests cover both header swaps, locked-row relabeling
and an unsupported ethics-appendix result. No reported value changed.

No remaining actionable findings. Both prior P2s are closed within this follow-up’s scope.

- **Table identity:** A1/A2 header swaps now fail binding validation. Changes to the locked row’s label, contrast, or sample count also fail. All 65 baseline bindings matched exactly once. See [bindings](/home/factory/collusion/collusion-beyond-words/results/template_document_bindings.json:855).
- **Appendix B coverage:** Contextual coverage extends through B, ending before C’s prompts. In-memory decimal, percentage, and fraction insertions were rejected at B’s beginning, middle, and end. Relevant regression tests cover both fixes. See [coverage boundary](/home/factory/collusion/collusion-beyond-words/scripts/check_template_numbers.py:57).

Scope: the prior review and five named files only. Probes used synthetic source inputs and the report itself as the token-membership corpus; frozen-source correctness and actual SUBMISSION membership were not revalidated. Integer-only and qualitative claims remain outside numeric coverage. No files modified, write-producing CLI tests, experiments, model calls, or subagents.

Manager verification: `uv run python scripts/finalize.py` → FINALIZE OK, 14 commands / 57 tests
(30 reproduction + 10 packaging + 9 export + 3 compliance + 5 primary-artifact = 57).
120 frozen-source assertions, 144 extended-report/slide bindings, 65 primary bindings, 158 evidence hashes;
160 numeric tokens, 26 CI triples and 142 contextual tokens, zero unmatched/unclassified.
135 individual primary numeric-slot mutations are rejected. Both modified extended-report pages (19–20)
were visually inspected; primary report and slide page-content streams remain identical to baseline.
