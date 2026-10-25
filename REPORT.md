# REPORT

The primary submission is **[TEMPLATE_REPORT.md](TEMPLATE_REPORT.md) / [TEMPLATE_REPORT.pdf](TEMPLATE_REPORT.pdf)**;
**[SUBMISSION.md](SUBMISSION.md)** is the extended report. Number provenance: [SOURCES.md](SOURCES.md).

Iteration 18 (2026-10-25 18:29 UTC) reran the exact integrity-verification command in
[final handoff notes](reviews/handoff_i16.md): all recorded archive, log, artifact,
checksum, root-upload and scientific-payload checks pass. This verifies the existing
acceptance described below; its 57 tests were not rerun. Only STATUS/REPORT closure
notes change, outside the fixed accepted ZIP. The user's explicit 18:00 UTC hard stop
takes precedence over DIRECTION's local extension; research remains stopped.

Iteration 16 confirms that the final iteration-15 upload package **completed at
18:10:47 UTC** for release revision `7ba00f1afeb08489e53587b91241fa218c48e8e3`.
All **11 successful acceptance-command logs**, **311 Git-matching tracked files**,
**20 sidecar checksums**, recorded artifact hashes and root upload copies verify.
The final ZIP is **24,246,215 bytes**, SHA256
`4380a0774f58aae2c48842c4e7d988b40b77985ccd5438bf71f76454b25da17f`.
[Completed acceptance receipt](results/release_package_i15.json), with the verification
command in [final handoff notes](reviews/handoff_i16.md). This checks the existing
same-VM acceptance; it does not rerun its 57 tests. Integrity checks also confirm
**158 stored evidence blobs**, **176 preserved scientific files** and **eight accepted
manuscript/upload artifacts** against their recorded hashes.

Research remains stopped at the user's explicit 18:00 UTC deadline. The accepted
release is fixed at the revision above; this iteration adds only closure notes and
the completed receipt. These later administrative files are outside that ZIP.
No further packaging is pending: repeatedly packaging each receipt's own notes would
create another revision without changing the submission. Scientific estimates,
manuscripts, PDFs, figures, source pins and the usage snapshot remain unchanged.

Dennis must upload root `TEMPLATE_REPORT.pdf`, `IMAGE.png` and `submission_code.zip`;
use `SUBMISSION_FORM.md` for form fields. The identical verified copies, logs,
`receipt.json` and `SHA256SUMS` are in `/var/tmp/bw-final-i15` on the author VM.
Optional supplements: `SUBMISSION.pdf` and `SLIDES.pdf`. No upload has been performed here.

Fallback iteration 7 closes the primary report's numerical-context gap. The source checker now
validates **65 section/table-scoped primary bindings (135 numeric slots)** directly against frozen
source values; it requires exact occurrence counts and fixed precision. Table headers and row
identities are checked alongside values. The numeric inventory covers the scientific main text
and appendices A–B, including ethics: **142 tokens, zero unclassified**, alongside the global
**160-token / 26-CI-triple** membership check. Integer-only and qualitative claims still require review.
Commands: `uv run python scripts/check_sources.py` and `uv run python scripts/check_template_numbers.py`.

`uv run python scripts/finalize.py` passes **14 commands / 57 tests** (30 reproduction, 10 packaging,
9 export, 3 compliance, 5 primary-artifact), with **120 source assertions / 144 extended-report and
slide bindings / 65 primary bindings / 158 evidence hashes**. Four new regression checks reject
endpoint, detector, count, header and row-label swaps, deleted/duplicate claims, every primary
numeric-slot mutation, and unsupported results in the ethics appendix or beside non-results.
The [independent review and follow-up](reviews/codex_fallback_i7.md) closed two P2 findings and
report no remaining actionable issue within scope. [Finalizer log](reviews/finalize_fallback_i7.txt).

[Preservation receipt](results/primary_preservation_fallback_i7.json) from
`uv run --group export python reviews/verify_preservation_fallback_i7.py` confirms **176** scientific,
manuscript and image files unchanged, including the primary Markdown and all six scientific replay outputs;
the original 111 source assertions and 144 bindings are identical. Primary PDF and slide content streams
are unchanged; only extended-report pages 19–20 change (provenance/test counts and usage snapshot), and
both were visually inspected. No empirical estimate or evidence pin changed. No experiment, new
held-out evaluation, simulation or auditor call. Clean committed archive acceptance of `77ab10d` passes **11 commands / 57 tests**, preserves all
**302 tracked files** and verifies **20 handoff checksums**. The **24,181,531-byte ZIP** includes
301 merged and 550/1387 pinned source files, checked against Git. [Receipt](results/release_package_fallback_i7.json),
[handoff and final-notes package commands](reviews/handoff_fallback_i7.md). The final package's own receipt
records its exact notes-HEAD revision outside Git; root `submission_code.zip` is copied from it.
Same existing author-VM environment; no new installation, transfer, submission or access change.
Dennis still must upload the primary PDF, project image and final code ZIP. Earlier notes are historical.

Fallback iteration 6 closes the primary-upload release gap. `finalize.py` now exports and checks the
template PDF as well as the extended report/slides. `check_template_artifacts.py` checks the actual PDF
text, four figure pixel matches, template structure, 150–250-word abstract, main-text limit, early headline
placement and 1600×900 project image, bound to file hashes. The handoff stages `TEMPLATE_REPORT.pdf`,
`IMAGE.png`, `submission_code.zip`, form and optional supplements. ZIP validation compares all included
merged/source files with their committed Git bytes and verifies both pins against the evidence manifest.
The new checks supplement the existing numerical checks; they do not certify scientific interpretation.

Applied source managers' final P1 wording corrections (Q1.4 `48662dc`, Q2.2 `05e588a`, supplied patch I179):
abliteration did not detectably increase the **channel-related pricing premium**, rather than absolute
prices; Discussion/slide 1 now say that adding public text gave no resolved gain, preserving Qwen's
inverted text rankings. Verified against pinned Q1.4 `p2_partc.json` and Q2.2 table C23; no estimate changed.
The primary abstract is 246 words. Full finalization passes **14 commands / 53 tests**
(26 reproduction, 10 packaging, 9 export, 3 compliance, 5 primary-upload), with **111 source
assertions / 144 bindings / 158 evidence hashes**, zero unclassified decimals, 147 primary PDF
text fragments and four pixel-exact figures. Main text remains 6 of 10 pages; slides remain 8.
The new image regeneration is byte-exact and page 1 was visually checked.
Clean-HEAD acceptance of `7c7be5e` passes **11 commands / 53 tests**, preserves all **295 tracked
files**, and verifies all **20 handoff checksums**. The **24,124,969-byte ZIP** contains 294 merged
and 550/1387 pinned source files, all checked against Git. [Receipt](results/release_package_fallback_i6.json),
[handoff commands and final-notes package](reviews/handoff_fallback_i6.md). This is the existing
same-VM environment; no new installation, experiment, model evaluation, submission or access grant.
[Independent Codex review](reviews/codex_fallback_i6.md): no remaining findings after fixing
Git-environment isolation and concurrent-export snapshot checks. Earlier notes below are historical.
Figures: `figures/fig1–fig6` (all six regenerate standalone from the pinned evidence bundle; Fig. 1, 2 and 3 re-rendered from pinned Q1.4 JSON by `scripts/fig1_hard_negatives.py` / `scripts/fig2_level_vs_comovement.py` / `scripts/fig3_e70_grid.py`, and Fig. 5 from pinned Q2.2 trajectories by `scripts/fig5_placebo_premium.py` (per-round means asserted equal to the saved `placebo_llm_v3plc.json`), all with larger text only — same data, groups and encodings; Fig. 4 regenerated by `scripts/fig4_say_vs_do.py` from Q2.2 JSON with a corrected axis label; Fig. 6 by `scripts/fig6_strong_framing.py` with the tacit-high window label corrected from "2nd half" to rounds 11–40, matching `p2_strong_eval.py --late 11`). This repo runs no new experiments.

- **Primary (Apart template, judge-readable): [TEMPLATE_REPORT.md](TEMPLATE_REPORT.md) / [TEMPLATE_REPORT.pdf](TEMPLATE_REPORT.pdf)** (iter50, per DIRECTION 16:40; headline Figure 1 `figures/fig0_headline.png` + `IMAGE.png` from `scripts/fig0_headline.py`; Opus review `reviews/opus_template_i50.md`, all items applied). Extended version with all appendices:
- PDF: **[SUBMISSION.pdf](SUBMISSION.pdf)**; slides (8): **[SLIDES.pdf](SLIDES.pdf)** from [SLIDES.md](SLIDES.md).
- Iteration 49 (2026-10-25 15:50 UTC) confirms unchanged release bytes: **179 protected
  hashes**, five export hashes and the saved finalizer-log checksum pass.
  Q1.4 `13e8b09` / Q2.2 `07d986e` are clean and unchanged since iteration 48.
  No suites or exports repeated; reviewed artifacts and usage snapshot stay frozen.
  Production finalization/clean-HEAD packaging remain due **16:30 UTC**;
  artifact transfer or reader access remains pending.
- Iteration 47 preserves the reviewed release at 15:45 UTC. Sources
  `13e8b09` / `8a725af` are clean; their complete advances from iteration 45
  change STATUS notes only. Read-only assertions pass for all **179 protected
  release hashes**, all five export hashes and the saved finalizer-rehearsal log
  checksum. DIRECTION is unchanged. No suites, export, usage refresh or scientific
  analysis repeated. This bounded iteration ends early under the freeze;
  production finalization and packaging of clean committed HEAD remain due at
  **16:30 UTC**, ready by 17:30. Artifact transfer or reader access remains pending.
- Iteration 45 preserves the freeze at 15:28 UTC. Q1.4 advances to `77e8fc1`
  with STATUS notes only; Q2.2 remains `1ac4621`, both clean. Read-only checks
  confirm the protected release hashes, both committed PDF hashes and the
  iteration-44 log checksum against their existing receipts. No suites or
  exports repeated; no manuscript, scientific artifact or usage snapshot changed.
  The production finalizer and clean-HEAD package remain due at 16:30 UTC;
  reader transfer/access is still pending.
- Iteration 44 rehearses the complete 16:30 finalizer in an external archive
  of `04c3da9`, using current author-machine runner logs and the existing locked
  environment/browser. All **10 commands / 47 tests** pass; **111/144/158**
  source/binding/hash checks pass with zero unclassified decimals. Only the usage
  snapshot/statement, PDF metadata/page 19 and their hash/size receipts change; scientific
  prose, every other report page stream and all slide streams are preserved.
  Production manuscript, science, PDFs and usage snapshot remain frozen.
  [Receipt](results/finalizer_rehearsal_i44.json), [log and scope](reviews/finalizer_rehearsal_i44.md).
  This is a same-VM rehearsal, not the scheduled production finalization or a new
  install. Hold until 16:30, then finalize, commit/push and package clean HEAD;
  reader access or artifact transfer remains pending.
- Iteration 43 checks the existing exact-notes-commit handoff of `8df26e5`:
  all 274 archived files match Git bytes/modes, the three upload files match
  Git, all eight successful check logs retain their recorded hashes, and all
  14 sidecar checksums pass. Fresh source/document, decimal-coverage,
  committed-PDF and compliance checks pass; source changes since iteration 42's
  recorded revisions are STATUS lines only. No scientific or reviewed artifact
  changed. [Procedure and final notes-commit package command](reviews/handoff_i43.md).
  This reuses the existing handoff and environment; it is not a new installation
  or a rerun of its 47-test acceptance. Finalize/repackage at 16:30 remains due;
  reader access or archive transfer is still pending.
- Iteration 42 verifies the frozen post-compliance release `e64ff45` from a fresh
  authorized remote clone, new locked dependencies and newly downloaded Chromium.
  All **8 commands / 47 tests** pass; **269 archive files** retain Git bytes/modes;
  source checks remain **111/144/158**, with zero unclassified decimals.
  Both PDFs also rebuild with identical text, content streams and bytes except
  date metadata (6 main / 20 total report pages; 8 slides). Production manuscript,
  science, figures, PDFs and usage snapshot remain unchanged. A post-15:00 source
  reconciliation passes; Q1.4's later `372f375` adds STATUS lines only, Q2.2 stays
  `5a012a0`. [Source receipt](results/source_freeze_i42.json),
  [package receipt](results/release_package_i42.json),
  [fresh export receipt](results/fresh_export_i42.json),
  [commands and handoff](reviews/handoff_i42.md). Same author VM; no experiment,
  model call, new scientific analysis, submission or access grant. Package clean
  HEAD after these notes, then repeat after the scheduled 16:30 finalizer.
- Iteration 40 reconciles the full tracked source trees before the 15:00 experiment
  cutoff; both managers already declare research final. No new result needs importing:
  Q1.4 has 544/552 unchanged tree entries, Q2.2 1380/1392; all remaining paths are
  enumerated metadata/exports or the known figure-label correction. All 158 bundled
  pin hashes match; live drift is only Q2.2's single report review-log line. The
  179 protected merged release files retain their `a924419` bytes. Current numeric,
  coverage and committed-PDF checks pass (111/144/158; zero unclassified decimals).
  Q1.4's saved source checker has two disclosed rounding-related quote misses,
  despite zero JSON mismatches; it is not an all-green quotes check.
  [Receipt](results/source_freeze_i40.json), [command and scope](reviews/source_freeze_i40.md).
  Manuscript/PDFs and scientific estimates remain frozen; no experiment or new analysis.
- Iteration 39 adds [verified release packaging](scripts/package_release.py) for the
  final handoff. After committing finalizer outputs, the README command checks the
  exact committed archive without `.git` and prepares both PDFs, form text, the
  code/evidence archive, logs and checksums outside the repository. Nine packaging
  tests cover corruption/omissions, dirty or concurrent edits and failed checks;
  the finalizer now runs them. A direct committed-PDF check also compares text,
  slide placement, embedded figure pixels and links against the current sources.
  Full acceptance of pushed commit `c3d2903` passes **8/8 commands and 47 tests**
  (26 reproduction + 9 export + 3 compliance + 9 packaging); all **264 tracked
  archive files** retain Git bytes/modes after checking. [Receipt](results/release_package_i39.json),
  [procedure](reviews/handoff_i39.md), [critic/follow-up](reviews/codex_i39.md).
  The critic's two P2s (stale embedded figures; inherited fixture Git variables)
  are fixed and regression-tested; follow-up has no actionable P1/P2. The manager
  ran the full suites; the read-only critic used nonmutating probes.
  Reviewed manuscript, science, figures, PDFs and usage snapshot are unchanged.
  Existing environment/browser on the same VM; no new install, PDF rebuild,
  access grant, transfer, experiment or scientific analysis. Package the notes
  commit and any later finalizer edits from clean HEAD for the actual handoff.
- Iteration 38 verifies the **post-compliance release `2add728`** from an extracted
  archive without `.git`, with nonexistent sibling-root overrides and no model
  environment variables passed. [Receipt](results/reviewer_archive_i38.json),
  [procedure/driver](reviews/distribution_i38.md). All 257 archived files match Git;
  six calculation JSONs and six figures rebuild byte-identically. **111 source
  assertions / 144 bindings / 158 hashes, 26 reproduction + 9 export + 3 compliance
  tests pass**, with no unclassified decimals. Both rebuilt PDFs match committed
  page text/content streams and full bytes after date-metadata normalisation
  (6 main / 20 total report pages; 8 slides; abstract 234 words). Production
  manuscript, scientific artifacts, PDFs and usage snapshot remain unchanged.
  This reuses iteration 33's locked environment/browser on the same VM; it is
  not a fresh install or new access check. The local archive has the current
  scientific payload; package the final HEAD to include this verification note
  and any later finalize edits. Reader access or archive transfer remains pending.
- Iteration 34: second independent critic (Codex gpt-6.1-sol, read-only; [record](reviews/codex_i34.md)) of the compliance cut: 0 P1, 3 P2 wording fixes applied (abstract names the registered combined-minus-better-single-view estimand; TE scoped to grid vs two main sets; §6 says "no resolved benefit; small gains remain possible"). No number changed; references and disclosures raised no finding. Full finalize passes.
- Iteration 33b follows the director's new submission-compliance override (`2cf7c7d`).
  **Main text: 6 pages; abstract: 234 words; form summary: 117 words; PDF: 1,153,269 bytes**
  (20 pages including references/appendices; references start on page 7; slides remain 8).
  Definitions, detailed tables/figures, extended interpretation and disclosures move to appendices;
  the scripted positive control and core comparisons remain in the main text. Added the required
  **Limitations and Dual-Use / Ethical Considerations** appendix, author affiliation, explicit
  pre-existing-code and AI-assistance disclosures, and [SUBMISSION_FORM.md](SUBMISSION_FORM.md).
  [Compliance receipt](results/submission_compliance.json); full `finalize.py` passes, including
  **111/144/158 source/binding/hash checks, 26 reproduction tests, 9 export tests and 3 new
  compliance tests**. Decimal coverage includes relocated scientific prose (248/281 report,
  55/61 slide; all other 33 + 6 are declared non-results). Five new bindings check repeated claims;
  the primary abstract has a separate scoped binding so its deletion cannot be hidden by the
  extended summary. [Preservation audit](results/compliance_preservation_i33.json): all 111 source
  assertion objects, the previous 139 bindings, all six scientific replay JSONs, all six figures
  and the evidence manifest are identical to `089ffb0`; no empirical estimate changed.
  All 15 reference identities checked (14 starter CSV matches plus Schreiber's primary audit);
  [record](results/reference_metadata_i33.json). Independent Opus review plus follow-up:
  **0 open P1/P2**, seven wording/structure fixes applied ([review](reviews/opus_compliance_i33.md)).
  Both source managers also report 0 P1; Q2.2's five optional scope nits applied. All 20 PDF pages
  visually inspected, with abstract and ethics checked at detail. Usage snapshot refreshed by
  finalize to **361 = 233 Opus + 128 Codex** source-repo manager iterations by 13:45 UTC.
  No experiments, simulations, auditor/judge calls or new test-set evaluation. The historical
  `c1e7fdd` clone/archive receipt below predates this editorial revision; package the final HEAD.
- Iteration 33a verified the then-current `c1e7fdd` release before the compliance revision, including iteration 30's archived pCMI
  null replay, from an authorized GitHub clone with fresh locked dependencies and Chromium.
  All six replay JSONs and all six figures rebuild byte-identically; checks pass:
  **111 source assertions, 139 document bindings, 158 evidence hashes, 26 reproduction
  tests, 9 export tests, 0 unclassified decimals**. Both PDFs match the committed page text,
  content streams and full bytes after date-metadata normalisation (17 pp / 8 slides).
  [Receipt](results/distribution_check_i33.json), [procedure and recorded driver](reviews/distribution_i33.md).
  **Handoff limitation:** anonymous HTTPS cloning failed (exit 128), and anonymous GitHub
  page/API requests returned HTTP 404; both source-repo pages also returned 404. This does
  not establish the visibility setting, but a reader needs repository access or an author-supplied
  archive. README now gives an archive command and distinguishes acquisition from execution.
  A local archive of the tested release (6,815,414 bytes; all 244 tracked files matched)
  passes the source/coverage checks, all 26 reproduction tests, PDF export and all 9 export
  tests without `.git`, reusing the fresh clone's Python/browser installation.
  [Archive receipt](results/reviewer_archive_i33.json); no transfer or access grant performed.
  PDF links use GitHub URLs that require access; the export tests verify URL structure, not
  remote availability. No visibility changes, new experiments or model calls; manuscript,
  scientific results, figures, PDFs and usage-count snapshot preserved.
- Iteration 30 extends the scripted-gate check to raw pCMI scores and the historical shift null.
  Command: `uv run python scripts/recompute_gate_pcmi_q14.py` → `results/gate_pcmi_q14.json`.
  From 50,000 archived rounds (500 markets), **all 3000 observed pair scores match exactly,
  all 3000 pair p-values match, and all 500 max-statistic run p-values match**. The replay
  preserves original sorted-run seeds, B=200, relative offsets ≥3, re-residualisation,
  the 1e-12 tie tolerance and the finite-draw rule. One exact source blob added (158 total;
  earlier 157 entries unchanged). Three added release checks cover standalone byte parity,
  the unmodified original full scorer on ten group representatives and constant/short-draw
  fixtures, and malformed trajectories/wrong cached p-values. This replays frozen calculations;
  no new markets, settings, labels, auditor calls or held-out estimates. Other detector nulls
  and ground-truth correctness remain outside the replay. Scientific results and slides unchanged.
  Reviewer-supplied nonconstant and tiny-score fixtures now explicitly detect removal of the
  fewer-than-20-draw fallback and 1e-12 tie tolerance; the original constant fixtures could not.
  [Independent Codex review](reviews/codex_i30.md) ran the unmodified original full scorer
  on all 500 games: every score, pair/run p-value and valid-draw count matches exactly.
  No open P1/P2. All checks pass (111/139/158, 26/26 reproduction, 9/9 export);
  PDFs remain 17 pp / 8 slides, with changed report pages 11–13 visually inspected.
- Iteration 29 verifies the expanded release from a fresh GitHub clone of `731de19`, with a
  new virtualenv installed via `uv sync --locked --all-groups --no-cache`, nonexistent sibling
  paths, no model environment variables passed to the verification commands, and a fresh
  Chromium download. Deleted and rebuilt all five replay JSONs and all six figures: each is
  byte-identical to the committed artifact. The commands listed below pass in that clone:
  **111/111 source checks, 139/139 bindings, 157 evidence hashes, 0 unclassified decimals,
  23/23 reproduction tests and 9/9 export tests**. Both PDFs have identical page text and
  content streams; their bytes match after normalising CreationDate/ModDate metadata
  (17 pp / 8 slides). Only those dates and the corresponding export-receipt PDF hashes change
  in the clone; production PDFs and every scientific artifact remain untouched.
  [Machine receipt](results/distribution_check.json), [procedure and comparison code](reviews/distribution_i29.md).
  This checks distribution on the author VM, not an independent operating system or new experiments.
- Iteration 28 reaggregates the scripted positive-control gate from 27,000 archived pair-score/p-value
  rows (500 markets, nine detectors). Command: `uv run python scripts/recompute_gate_q14.py`
  → `results/gate_q14.json`. All 666 saved summary values reproduce (largest floating-point
  difference 1.1e-16); flag rates, Wilson intervals and localisation rates match exactly.
  The replay preserves strict α thresholding, cached max-statistic shift p-values, and
  leave-one-out surrogate ranking against clean controls from the same shock family.
  Both planted groups retain pCMI detection and localisation in 50/50 runs each;
  shared-policy + common-shock false flags remain 6/50 (shift) and 2/50 (surrogate).
  Eleven exact pinned blobs added (157 total; previous 146 unchanged). Three release
  checks cover standalone byte parity, original-function parity on the entire cohort and
  boundary/tie fixtures, and malformed cache/cohort rejection. This verifies aggregation
  of saved evidence; no score/trajectory or shift-null regeneration, ground-truth validation,
  simulations, model judgments or new held-out evaluation. Scientific estimates and slides unchanged.
  [Independent Codex review](reviews/codex_i28.md): no actionable P1/P2; all blobs,
  summary values and event counts independently verified. Full finalize passes
  (111/139/157, 23/23 reproduction + 9/9 export). PDFs remain 17 pp / 8 slides;
  changed report pp11–14 inspected, pp1–10 and all slide content unchanged.
- Iteration 26 checks Q1.4’s central E70 grid from the archived raw trajectories.
  Command: `uv run python scripts/recompute_grid_q14.py` → `results/grid_q14.json`.
  All **768 run scores match exactly** (four detectors × 192 games; 3840 rounds).
  The original seed-0 B=2000 cell-by-arm bootstrap reproduces all four pooled AUROC/CI
  triples, both paired level contrasts, the markup contrast and all per-cell AUROCs.
  Added 39 exact Q1.4 blobs (146 total; earlier 107 unchanged). Three new release checks
  compare all 4608 per-pair scores, cohort loading and the full grid/paired bootstrap with
  original source functions, regenerate the output without sibling paths, and reject
  duplicate ground truth, missing/duplicate rounds, reordered sellers and nonfinite prices.
  This verifies saved calculations; null calibration, permutation flags, judge/executed
  labels and factor/model/spillover estimands are outside the replay. No scientific
  estimates or interpretations change; no simulations, model calls or new test evaluation.
  [Independent Codex review](reviews/codex_i26.md): no actionable P1/P2; independently verified
  all pinned blobs, original scores and full bootstrap draw order. Full finalize passes
  (111/139/146, 20/20 reproduction + 9/9 export); PDFs 17 pp / 8 slides, pp11–13 inspected.
- Iteration 25 independently replays the historical Q2.2 locked-test run scores from pinned
  judge labels and all six original LLM auditor caches. Every selected run-AUROC estimate/CI and
  all eight contrasts match the saved seed-0, B=2000 analysis exactly; primary
  **−0.0127 [−0.0913, +0.0642]**, still **−0.01 [−0.09, +0.06]** when printed. Exactly 95 test
  IDs (50 positive, 45 negative), paired class-stratified resampling and better-single-view
  selection within each draw; no fitting or model calls. Nine added exact blobs (107 total;
  previous 98 unchanged). A source-function parity test checks the real cohort and a tied
  calculator fixture with an independent rank-sum AUROC; incomplete, duplicate, nonfinite
  and wrong-auditor audit inputs are rejected. This reproduces saved evidence, not another
  held-out evaluation; it reuses the frozen labels and covers only the six run-score views
  and eight contrasts, excluding pair endpoints, fusion and thresholds.
  Command: `uv run python scripts/recompute_locked_test_q22.py` → `results/locked_test_q22.json`.
  [Independent Codex review](reviews/codex_i25.md): no actionable findings; full original B=2000
  replay and evidence provenance independently verified. Full finalize passes (111/139/107,
  17/17 reproduction + 9/9 export); PDFs remain 17 pp / 8 slides, changed pp11–12 visually inspected.
- Iteration 24 closes the remaining sibling-dependent replay gap: both Q2.2 rounding and C21b sensitivity
  scripts now use pinned evidence only. Added 22 exact Q2.2 blobs (98 total; earlier 76 unchanged), plus
  SciPy for the source Spearman estimator. All unrounded numeric values exactly match the earlier replay;
  C21b's output is byte-identical and retains the same five executed run IDs per arm in every setting.
  Two new release tests delete/regenerate both outputs with absent sibling paths and compare all C21b
  per-run fields with the pinned original source function (eight settings, 30 runs each). No experiments,
  model judgments or scientific-result changes. Applied Q2.2 I145's optional wording correction:
  below-threshold floors do not count as followed; no such cases occurred in the locked test.
  [Independent Codex review](reviews/codex_i24.md): no P1/P2; one nonblocking test-reference mapping
  blind spot fixed. Full finalize pipeline passes, with the report still 17 pages and the deck 8 slides.
- Iteration 20 fresh-clone release check (GitHub `d1cc435` → /var/tmp, sibling paths disabled): 111/111 source checks, 139/139 bindings, 76 hashes; 0 unclassified decimals; all six figure scripts byte-identical; 11/11 reproduction + 9/9 export tests; PDF rebuild gives 17 pp / 8 slides with page text identical to the committed PDFs (only the CreationDate differs). README now lists the fig2/fig5 commands.
- Iteration 21 dated + test-bound the LLM-usage counts (refresh again at finalize).
- Iteration 16 added **§9 Conclusion** (no new numbers) and an **LLM usage statement**. The human author seeded plan, schema, rules and LLM helper. Autonomous agents did the market code, experiments, analysis and writing: 414 source-repo manager iterations by 2026-10-25 17:16 UTC (257 Opus, 157 gpt-6.1-sol; refreshed iter28 — earlier 323 was an undated snapshot), from `scripts/process_log_summary.py` → `results/process_log_summary.json`, which reads machine-local runner logs. Codex review: 1 P1 (Conclusion overstated "without any agreement") and 3 P2 wording fixes, all applied ([record](reviews/codex_i16.md)).
- Iteration 11 scientific scope corrections: [primary-literature/code audit](reviews/literature_i11.md)
  verifies the bibliography and corrects the SALT explanation: preceding messages predict separately
  submitted verdicts; the detected act does not occur in the auditor-visible chat. The report and slides
  now include the saved no-accept/reject-substring sensitivity **0.75 [0.66, 0.84], n = 117** (M35),
  explicitly a selected subset rather than a causal ablation. No result was recomputed. Added the missing
  Shi/Zhang/Yang paper and linked/versioned references; distinguished Rose's causal/operational criteria;
  corrected Cao & Hu to no communication between sellers; headlines now allow the Qwen pCMI exception.
  [Codex](reviews/codex_i11.md) and [Opus](reviews/opus_i11.md) final rechecks have no open P1/P2.
- Rebuild: `uv run --group export playwright install chromium` (once), then
  `uv run --group export python scripts/export_pdf.py`. [Export receipt](results/export_check.json):
  **504/504 report text fragments, 55/55 slide fragments on the correct pages, and 10/10 embedded
  figures with exact source pixels**; legacy checks (26 headings, 378 cells, 8 titles) also pass.
  Slide body/table/code text fits at **≥14 pt** (busy slides previously shrank below that floor); chart labels
  remain raster text and can be smaller. Repository links now use absolute GitHub URLs instead of local `file://` paths;
  repository access is required (iteration 33 access check). These checks verify text presence and layout constraints, not scientific scope.
- Export failure checks: `uv run --group export python tests/test_export.py` passes **9/9**:
  deleted prose, text on the wrong slide, missing/broken/substituted figures, local-file links,
  overflow into page padding, horizontal overflow, and text below the font floor are rejected.
  Receipt: `results/export_test.json`. Existing scientific estimates are unchanged. Iteration 10 fixed a Markdown
  line wrap: `+ public facts` no longer accidentally starts a list in Methods.
- TEMPLATE_REPORT check: `uv run python scripts/check_template_numbers.py` confirms that all 160 numeric tokens and all 26 estimate+CI triples in TEMPLATE_REPORT.md occur in SUBMISSION.md, whose numbers are bound to source data (0 unmatched; finalize.py runs it). The 3/3 Qwen wording is now written as three comparisons; the estimate is unchanged. This remains token/triple membership, not a context-specific binding of every template claim.
- Saved-value/document check: `uv run python scripts/check_sources.py` passes **111/111 source assertions,
  144/144 document bindings, and 158 evidence-file hash checks**. The document bindings extract
  printed numbers from SUBMISSION.md and SLIDES.md and compare them directly with saved source values,
  using half-up rounding. Iteration 14 extended them to Tables 1–2 and §5.2–5.4: `scripts/number_coverage.py` reports 248/281
  decimals across the report main text and relocated scientific appendices D–G and 55/61 in the slides bound (was 58/254, 36/61; 208/254 after iteration 14). Most unbound tokens are
  chance levels, α, thresholds and model/section numbers. Iteration 15 pinned the last cited source files (Q1.4 `eval/llm_ds_p2.json`; Q2.2 `p2_cue_llm_p2para{1,2}.json`, `p2_logbook.json`) and bound the paraphrase arms, weather notepad and deepseek TE CI. Iteration 17 found **five double-rounded claims (six numbers)**: the sources saved a 3-dp tie (x.xx5) and printed it again at 2 dp. The unrounded values were recomputed with the sources' own estimators. E65 and the grid CI are replayed inside `check_sources.py` from pinned data, after pinning the E65 trajectories (76 files); the 3 Q2.2 values come via `scripts/recompute_unrounded_q22.py`. Each recompute must reproduce the stored 3-dp values exactly. Corrected: E65 +2.14 [1.29, 3.00] (was +2.13 [1.28, 3.00]), grid level 0.74 [0.66, 0.80] (was 0.81), E113 executed −0.30 [−0.44, −0.16] (was −0.17), Qwen3.8-base no-channel Spearman −0.40 (was −0.41), Fig. 6 action 0.57 (was 0.58; exactly 142/247). These are disclosed in SUBMISSION Reproducibility; no conclusion changes. Every bound tie value has now been checked, and E65 is now bound; the remaining unbound decimals (33 report, 6 slide) are all machine-classified as non-results (chance level, α, design parameter, threshold, section number, model version, one illustration); since iteration 19 `number_coverage.py` fails on any unbound decimal outside these categories, which two new release tests check (`results/number_coverage.json`). Bindings do not verify qualitative scope. Receipt:
  `results/source_check.json`. The earlier 44-check script compared only saved JSON with hard-coded
  expected values; iteration 9 corrects its overstated description and adds actual document checks.
- Standalone reproduction: [evidence/](evidence/README.md) bundles 158 exact source files at Q1.4 `732f08c`
  / Q2.2 `91ffb2d`, with full commit IDs and SHA256 provenance. No sibling clones or model credentials
  are needed for the checks and the rendering of all six figures. This verifies saved evidence; full experimental
  regeneration still requires the source repos and their caches.
- Release checks: `uv run python tests/test_reproduction.py` passes **26/26** in an independent copy with
  nonexistent source paths. All six regenerated figures reproduce byte-identically; edited report/slide values, a
  missing binding, incorrect rounding or reduced precision, a corrupt bundle file, and a changed live source are
  rejected. The Q1.4 grid/gate/pCMI-null and all three Q2.2 replay outputs also regenerate byte-identically. Receipt: `results/reproduction_check.json`.
- Finalize: `uv run python scripts/finalize.py` (author machine; reads runner logs) refreshes the LLM-usage counts in SUBMISSION/REPORT and runs every check above plus the PDF export, stopping at the first failure. Iter22: FINALIZE OK.
- Reviews (`reviews/`): codex v0–v3, i11, i14, i16, i17, i18 and Opus v0–v2, i11, i18 adversarial reviews, plus a judge-style presentation review (`judge_v0.md`, applied in v1.4) and a codex + Opus scope review of the v1.4 diff (`codex_v3.md`, applied in v1.5).
- Reproduction implementation review: [codex_reproduction_i9.md](reviews/codex_reproduction_i9.md), one
  precision bug fixed; no open P1/P2. All 66 source blobs then in the bundle (now 158) independently checked against the pinned commits.
