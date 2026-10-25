# codex gpt-6.1-sol (high, read-only) review of iteration-19 diff — 2026-10-25 ~12:00 UTC

Scope: number_coverage.py non-result categories + 2 release tests; E84 trivial-floor wording.

- **P2** number_coverage.py: the bare `0\.5 = chance` alternative matched nearby text without referencing the
  marked token. Reviewer verified that inserting `0.5 = chance; AUROC 0.73 [0.61, 0.85]` passed with all three
  result decimals classified as chance levels. The docstring's "cannot enter unbound" was therefore an overclaim.
  → FIXED: alternative removed; import-time assertion that every alternative contains the marked token;
  docstring reworded ("whitelist written for the current text"); regression test added with the reviewer's exact
  case (now UNCLASSIFIED, exit 1).
- E84 wording matches `p2_behaviour.classes(min_floor=12)`. Other coverage contexts are correctly categorised.
