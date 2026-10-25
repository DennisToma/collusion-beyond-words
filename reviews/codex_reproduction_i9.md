# Iteration 9 — portable evidence and document-check review

Independent read-only adversarial review by `gpt-6.1-sol` (high reasoning), via a fresh-context Codex
subagent. Scope: the uncommitted iteration-9 evidence bundle, checker, document bindings, figure input
loaders and release tests. This is an implementation review; the scientific claims did not change.
No experiments, simulated-agent calls, new auditor calls or metric recomputation.

## Finding and resolution

**P2, fixed:** the first document-check implementation took rounding precision from the edited text.
Replacing the slide's `−0.01 [−0.09, +0.06]` with `0 [0, 0]` still passed: the source values rounded to
integers. The reviewer reproduced this with an edited slide file in `/var/tmp`.

Each binding now declares per-slot `digits` in `results/document_bindings.json`; the checker quantizes
the saved source value at that fixed precision. A document edit cannot enlarge the tolerance. The
reviewer reran the mutation: exit 1 with a failed document binding. The release suite covers both this
slide mutation and a Fig. 6 range changed from `0.43–0.58` to `0–1`, plus the half-up boundary at 0.575.

## Final reviewer verification

- No open P1/P2 findings after the precision fix.
- Baseline: 57 source assertions, 64 document bindings, 66 evidence hashes, all passing.
- All 66 uncompressed source hashes independently matched `git show <full-commit>:<path>` in the source repos.
- The default checker and both figure loaders read bundled evidence exclusively.
- Source repos were read only; reviewer scratch receipts were kept in `/var/tmp`.

The tests use an independent copy and nonexistent configured source paths. They do not impose an OS
filesystem sandbox; the reviewer also checked the loaders for hard-coded fallbacks. This verifies
selected numeric bindings and saved evidence, not unbound numbers or qualitative claim scope.
