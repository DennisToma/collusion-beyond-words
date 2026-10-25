# Iteration 39 — handoff packaging review

Codex gpt-6.1-sol, high reasoning, read-only, 2026-10-25.
Initial code milestone: `ff29e31`; no manuscript or scientific change.
The read-only sandbox could inspect files and perform in-memory probes but could not
run the write-dependent suites under `/var/tmp`. Manager execution is recorded separately.

## Initial review (verbatim)

Two P2 findings; no P1 findings.

1. **P2 — Stale figures in committed PDFs can pass packaging.** [package_release.py:163](/home/factory/collusion/collusion-beyond-words/scripts/package_release.py:163) runs compliance and export tests, but never compares the committed PDFs’ embedded figures with the current PNGs. The export receipt hashes Markdown, PDFs and exporter code, excluding figure inputs. Regenerating figures and reproduction receipts without rebuilding PDFs can therefore pass. The packaging fixtures replace every check with `pass`, missing this case.

   **Fix:** Run the existing nonmutating `check_figures()` against both committed PDFs before publication, and add a regression where a regenerated figure accompanies an unchanged PDF. An in-memory probe confirmed compliance accepts an altered source image while direct PDF figure verification rejects it.

2. **P2 — Test Git commands can modify the author repository through inherited environment variables.** [test_packaging.py:43](/home/factory/collusion/collusion-beyond-words/tests/test_packaging.py:43) inherits `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE`. The newly integrated finalize test can consequently run fixture initialization, configuration, commits or resets against another repository. Production packaging now sanitizes its Git environment, but this helper still does not. A read-only probe confirmed it resolves the author repository despite a fixture working directory.

   **Fix:** Sanitize the fixture’s Git environment for every invocation. Add a regression with foreign Git environment variables and verify the foreign repository’s HEAD, index, configuration and worktree remain unchanged.

Full packaging tests were blocked: all nine failed during setup because `/var/tmp` is read-only in this sandbox. Existing receipts were inspected. No files were edited and no models were invoked.

## Manager response

Both P2 findings applied. `scripts/check_committed_export.py` now checks the actual
committed report/deck against current Markdown text, slide page placement/count, PNG
pixels and link schemes without rebuilding. The packager and finalizer invoke it.
Existing export tests now demonstrate that changing a source PNG while keeping the
PDF fixed is rejected, along with missing committed text and wrong slide count.

Every fixture Git invocation uses the same environment allowlist as production Git.
The regression deliberately sets foreign GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE, runs
fixture init/config/reset/commit and checks the foreign HEAD, index, config and worktree
remain unchanged. All nine packaging and nine export tests pass after the fixes.
No source evidence, manuscript, scientific result, figure, PDF or usage snapshot changed.
Full committed-package acceptance passes at `c3d2903`: 8/8 commands, 26 reproduction +
9 export + 3 compliance + 9 packaging tests, all 264 tracked files unchanged after
verification. See [receipt](../results/release_package_i39.json) and
[procedure](handoff_i39.md). The critic did not independently rerun those suites.


## Follow-up review (verbatim)

Both original P2 findings are fixed. No remaining actionable P1/P2 findings in the current changes.

- [Committed-export checker](/home/factory/collusion/collusion-beyond-words/scripts/check_committed_export.py:19) passes against current artifacts and runs from packaging and finalization. In-memory probes rejected changed source-image pixels with unchanged PDFs, missing text, wrong slide count and misplaced slide text.
- [Fixture Git helper](/home/factory/collusion/collusion-beyond-words/tests/test_packaging.py:43) uses the production environment allowlist. Read-only probes confirmed both helpers resolve the local checkout under foreign Git variables. The new regression checks foreign HEAD, index, config and worktree preservation.

No misleading acceptance claim or unsafe-write regression found. Receipt hashes match current files; committed-release acceptance remains explicitly pending.

Verification limits: no edits, models, browser rebuilds, write-dependent suites or full packaging run. The export check and mutation probes ran with a write-blocking audit hook. The manager’s 26+9+3+9 acceptance was not independently rerun.
