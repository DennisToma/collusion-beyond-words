# Codex gpt-6.1-sol (high, read-only) review of iteration-14 bindings — 2026-10-25

Prompt: /var/tmp/i14_prompt.txt (verbatim below). Outcome: 0 P1, 2 P2 (scope anchors), 1 P3 (duplicate) — all fixed; the two scope mutations it constructed are now rejected.

```
You are an adversarial reviewer. Repo: current directory (merged research submission). Iteration 14 added ~35 saved-source assertions to scripts/check_sources.py (block "Iteration 14" and the M15/N7/N23 lines after it) and ~65 document bindings appended to results/document_bindings.json (templates with {} numeric slots matched against SUBMISSION.md / SLIDES.md, see scripts/document_checks.py). The diff is at /var/tmp/i14.diff. Evidence JSON is readable via scripts/evidence.py (Evidence().json('q14'|'q22', 'results/...')), files under evidence/.
Check, for each new binding: (1) the JSON key really measures what the surrounding SUBMISSION/SLIDES sentence claims (right arm, right contrast direction, right window, right population) — numeric equality with a semantically wrong key is the main failure to hunt; (2) the template cannot silently match a different sentence; (3) sign handling (e.g. private - placebo computed as negated placebo-private with swapped CI) is correct. Report P1 (wrong mapping/claim), P2 (fragile), P3. Be concise; cite binding template + key. Do not edit files.
```

## Final answer

No P1 mapping or sign errors found across the 65 appended bindings and 35 source assertions. Two P2 findings:

- **P2 — Silent retargeting.** Template `a similar {} [{}, {}] appears` → `M31:luna silent executed`, key `e113_secondary.json → stratified.executed_vs_A.luna_silent_combined_minus_action_posthoc`. It anchors neither execution nor silent cells. In memory, I changed the intended estimate to `+0.25`, rephrased its prefix, and placed the original template/value in an unrelated sentence: **all document checks still passed**. Include the population and contrast in the template. [Binding](/home/factory/collusion/collusion-beyond-words/results/document_bindings.json:1028)

- **P2 — Arm identity unprotected.** Template `(n = 30) but {} [{}, {}] within` → `M33:Spearman within no-channel`, key `e132_inversion.json → sets["Qwen3.8 base"].spearman_text_vs_invite_rate_within_no_channel`. Changing the surrounding claim from “within the no-channel arm” to “within the channel arm” leaves **all document checks passing**. Bind through “no-channel arm.” [Binding](/home/factory/collusion/collusion-beyond-words/results/document_bindings.json:935)

**P3 — Diff only:** `pair-level {} [{}, {}] (not inflated)` → `N7:executed pair-level` was duplicated among the appended entries. That duplicate is already absent from the current file.

Sign handling is correct: `placebo-private.prem_r2_12 = [-0.379, -1.176, 0.412]` becomes private − placebo `[0.379, -0.412, 1.176]`, including swapped CI endpoints.

No files edited.
