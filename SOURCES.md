# SOURCES — where every number in SUBMISSION.md comes from

Iteration 11 final handoff (2026-10-25): Q1.4 `f6e6b7922757bae5e99c0e866e1c335794ade40c` /
Q2.2 `d4f9b62744641ac1380e4dbd67b8042f149cdaa5`. Changes since the preceding handoff are
STATUS/review notes only; both sources explicitly accept the primary report's current
bytes at merge `77ab10d`, with zero open P1. All 158 evidence blobs still match the
original pins and bundled hashes; no repin or estimate change. Verification command:
`uv run python reviews/verify_hold_i11.py`; receipt `results/release_hold_i11.json`.

Fallback iteration 7 (2026-10-25 17:18 UTC): source handoffs read at Q1.4
`0708b800d6ec8168860e6f92a60c43f304733776` and Q2.2
`f15abfd6503a33850f3e32d3751f7e998f1c4133`; both explicitly accept merge
`7c7be5e` / `8e4ef25` with zero open P1. Scientific pins remain unchanged.
`results/template_document_bindings.json` maps 65 primary-report claims to the
same source checks used by the extended report, with named-section boundaries,
fixed precision and exactly one required occurrence; table bindings include column headers and row identities. `check_sources.py` checks
those mappings directly; `check_template_numbers.py` inventories the scientific
sections and rejects unbound decimals, percentages or fractions. Other integers,
qualitative interpretation, references and process disclosures remain outside that
inventory. This verifies frozen results; it creates no estimate or test evaluation.

| added source assertion | frozen source file/key | source pin |
|---|---|---|
| T1: colluder flag/localisation, shared-seed flag range, lagged-TE flag range | Q1.4 `results/eval/gate_test.json:metrics` (contemporaneous detectors; both historical nulls for shared seeds) | `732f08c` |
| T2: cells where level beats pCMI (12/16) | Q1.4 `results/eval/e70_grid.json:per_cell.*.auroc` | `732f08c` |
| T3: rule-breaking episodes without explicit agreement (62%, rounded) | Q2.2 `results/analysis/salt_d1.json:E104_sayvsdo.P_said_given_exec.est`, complement × 100 | `91ffb2d` |
| T4: followed / communication-positive (14/50) | Q2.2 `results/analysis/p2_behaviour.json:datasets.llm_v3.class_counts` | `91ffb2d` |
| T5: legitimate high-cost / quality / control premium flags | Q2.2 `results/analysis/p2_asym.json:conditions.{highcost,quality,none_ref_p2cue}.premium_flags` | `91ffb2d` |

Source repos (read-only). Both declared a research freeze at 2026-10-25 07:30 UTC; later edits are logged
in each REPORT.md under "### Changes after 08:00 (for the merge manager)".

Fallback iteration 6 (2026-10-25 17:04 UTC): read source handoffs at Q1.4 `48662dc` and
Q2.2 `05e588a`; applied Q2.2's `results/analysis/template_scope_fixes_i179.patch`, which also
contains Q1.4's remaining abliteration corrections. Pinned Q1.4 `results/eval/p2_partc.json`
confirms that the tested null is the channel-related premium, not absolute prices;
Q2.2 C23 in SUBMISSION names its paired channel-premium contrast. Discussion and slide 1
retain the no-resolved-text-added-gain result and allow inverted Qwen rankings. No new
estimate, dataset, evidence pin or scientific analysis. Older source-check notes below
record historical release states; the frozen evidence pins remain `732f08c` / `91ffb2d`.

Iteration 49 source re-check (2026-10-25 15:50 UTC): Q1.4
`13e8b09485dc8656a0e26010401f92e8f26f7667` / Q2.2
`07d986e8099d1db2c95fb267daa19162eff214ea` remain clean and unchanged since
iteration 48. Read-only assertions pass for 179 protected release hashes,
five export hashes, the saved i44 log checksum and unchanged DIRECTION.
No scientific import or repin; production finalization remains due 16:30 UTC.

Iteration 48 source re-check (2026-10-25 15:49 UTC): Q1.4
`13e8b09485dc8656a0e26010401f92e8f26f7667` unchanged; Q2.2
`07d986e8099d1db2c95fb267daa19162eff214ea` adds one STATUS line since
`8a725af`. Both clean. All 179 protected release hashes, five export hashes,
saved i44 log checksum and unchanged DIRECTION pass read-only assertions.
No scientific import or repin; scheduled 16:30 finalization remains pending.

Iteration 47 source re-check (2026-10-25 15:45 UTC): Q1.4
`13e8b09485dc8656a0e26010401f92e8f26f7667` / Q2.2
`8a725af3180f87a5e10a4c6b603fa85010563df8`, both clean. Complete tracked diffs from
`77e8fc1` / `1ac4621` add two / three STATUS lines only, respectively;
source scope flags and all scientific files are unchanged. All 179 protected
merged release hashes, five export hashes and the saved i44 log checksum pass
read-only assertions. DIRECTION unchanged; no scientific import or evidence repin.
Production finalization and clean-HEAD packaging remain scheduled for 16:30 UTC.

Iteration 45 source re-check (2026-10-25 15:28 UTC): Q1.4 `77e8fc1` /
Q2.2 `1ac4621`, both clean. Complete Q1.4 diff from `372f375` adds only
STATUS I158/I159 lines; Q2.2 is unchanged. No new scope flag, scientific import
or evidence repin; reviewed manuscript and production release hashes preserved.

Iteration 44 source re-check: Q1.4 `372f375` / Q2.2 `1ac4621`, both clean;
no source commit since iteration 43. The finalizer rehearsal changes usage
metadata only in an external archive; no scientific import or repin.
[Verification](reviews/finalizer_rehearsal_i44.md).

Iteration 43 source re-check: Q1.4 `372f375` / Q2.2 `1ac4621`.
Complete diffs from the iteration-42 receipt's `e8cf411` / `5a012a0` change
STATUS.md only (two lines per source). Both worktrees are clean; scientific
inputs, manuscript scope reviews and evidence pins are unchanged.
[Verification and commands](reviews/handoff_i43.md).

Iteration 42 post-15:00 live reconciliation: Q1.4
`e8cf411460358ab14ffdb4769ada846406fd9497` / Q2.2
`5a012a0bba87dbfbd5bbbfcb16c810ab91483bc9`; all source-tree classifications,
158 pin hashes and 179 protected merge-file hashes agree with iteration 40.
Q1.4 subsequently advanced to `372f375e2ba2dd7d610a03ec4b114fa90a714ffa`;
its complete diff adds STATUS I156/I157 lines only. Q2.2 is unchanged. No
scientific import, repin or scope correction. [Receipt](results/source_freeze_i42.json),
[commands and exact revision scope](reviews/handoff_i42.md). The fresh-clone
package/export receipts cover merged release `e64ff45`, preserving every
scientific estimate and the reviewed manuscript bytes.

Iteration 40 full source reconciliation (2026-10-25 14:58 UTC; before the 15:00
cutoff): Q1.4 `e8cf411460358ab14ffdb4769ada846406fd9497` / Q2.2
`5a012a0bba87dbfbd5bbbfcb16c810ab91483bc9`. Both managers declare research final.
All changes since the pins are accounted for across the complete tracked trees:
544/552 Q1.4 and 1380/1392 Q2.2 entries unchanged; remaining paths are enumerated
review/director metadata, export artifacts and the already-applied rounds-11–40
figure-label correction. No changed saved estimate, dataset, split, auditor cache
or scientific analysis code. All 158 bundled raw hashes match the source Git pins;
live drift remains only Q2.2 REPORT.md's I133 line. Source zero-P1 coverage remains
I152 / I160 on the current `96d0ed7b…` manuscript bytes. Q1.4's source receipt has
two known 0.81 quote misses, documented rather than described as passing quotes;
the merge's independent 0.80 replay/binding passes. No evidence re-pin.
[Receipt](results/source_freeze_i40.json), [procedure/limitations](reviews/source_freeze_i40.md).

Iteration 39 source re-check (2026-10-25 14:45 UTC): Q1.4
`e67993aad5495e7d0f1ce1a2d954cee2229fd7e3` / Q2.2
`e0e0772968e941eed794cb27c7232a6ce492c54e`. Changes since iteration 38
are handoff/director metadata only; the sources retain the reviewed manuscript
scope coverage and zero open P1. No scientific result or evidence pin changes.
Merge `c3d2903` passes verified packaging: 111/144/158 checks, no unclassified
decimals, 47 tests and 264 unchanged archive files. [Receipt](results/release_package_i39.json),
[procedure](reviews/handoff_i39.md). Manuscript, slides, PDFs, figures, evidence,
six scientific replay JSONs, usage snapshot and lockfile are identical to `2da601d`;
the export-test receipt changes only its extended test-code hash. No new estimate.
Handoff addendum (14:47 UTC): Q1.4 advanced to
`aadba97ed3860dc7e969a4251ebcd9a0c2a086c7` (I154; STATUS/DIRECTION only),
explicitly confirming no Q1.4 hunk at `c3d2903` and 81/81 pin hashes intact.
Q2.2 remains at `e0e0772`; no new scientific input or scope flag.

Iteration 38 source re-check (2026-10-25 14:27 UTC): Q1.4
`8625743a306ff1b1e26d709c9c7d0a9b557e5d58` / Q2.2
`f73f49ccc8644a92bab55caed3fdb43fa24e5d9e`; both report 0 open P1.
Q2.2 I160 explicitly covers iteration 34's Q2.2 wording. No source result or
evidence pin changed (`732f08c` / `91ffb2d`). The post-compliance merge release
`2add728` passes archive reproduction, export and compliance checks with 144
document bindings; [receipt](results/reviewer_archive_i38.json),
[procedure](reviews/distribution_i38.md). Production scientific artifacts and
reviewed manuscript/PDF bytes are unchanged.

Iteration 38 handoff addendum (2026-10-25 14:30 UTC): Q1.4 advanced to
`589afaccd0601186eca7d6ef1637e46f979417d1` during the check. Only STATUS and
merge_flags changed: I152 now explicitly reviews the `96d0ed7b…` manuscript
bytes from iteration 34, including its TE and conclusion wording, with 0 P1;
81/81 Q1.4 pin hashes remain intact. Q2.2 remains at `f73f49c` with the same
current-byte scope coverage. No scientific update or evidence re-pin.

Iteration 24 re-check (2026-10-25 12:03 UTC): Q1.4 `1202079` / Q2.2 `aeec94e`, unchanged since
iteration 23; both working trees clean, no new scope flags or scientific results. Evidence pins remain unchanged.
During the pass, sources advanced to Q1.4 `b34a34b` / Q2.2 `d805e96` (review metadata only, both
0 open P1). Q2.2 I145's optional kept-rule nit is applied: floors below 12 do not count as followed,
rather than being described as "trivially kept"; pinned `p2_behaviour.classes` assigns `trivial_floor`
before testing compliance, and the saved locked-test counts contain no such cases. No number changes.

Iteration 25 source re-check (2026-10-25 12:24 UTC): Q1.4 `b3aa70a` / Q2.2 `388d239`
(review metadata only, both 0 open P1). Q2.2 I146/I147 independently verified the new
locked-test replay against its saved JSON and reviewed its scope wording. All pinned scientific
inputs remain unchanged; the only pinned-file drift is the already-disclosed Q2.2 REPORT
review line. Evidence pins remain `732f08c` / `91ffb2d`.

Iteration 26 source re-check (2026-10-25 12:36 UTC): Q1.4 `b82ebbc` / Q2.2 `388d239`,
metadata only and 0 open P1. No new scientific inputs or results; the evidence pins remain unchanged.

Iteration 28 source re-check (2026-10-25 12:49 UTC): Q1.4 `29fefdd` / Q2.2 `388d239`.
Q1.4 advanced through I139/I140 (handoff metadata and render-only exports; scientific inputs
unchanged, 0 open P1); Q2.2 remains unchanged. All 157 bundled blobs independently match
`git show` at the existing pins; the previous 146 manifest entries are unchanged. Live Q1.4
export/director work is concurrent and is not an evidence re-pin.

Iteration 29 source re-check (2026-10-25 12:56 UTC): Q1.4 `29fefdd` / Q2.2 `371d8ec`.
Q2.2 I148/I149 add render-only exports and merge-scope metadata; REPORT and saved scientific
results remain unchanged. Both sources have 0 open P1; evidence pins remain unchanged.
The expanded merge release at `731de19` was independently cloned from GitHub and rebuilt
with fresh locked dependencies and Chromium, absent sibling-root overrides and no model
environment variables. All five replay outputs, all six figures and every tracked file
except the two PDFs and their export-receipt hashes reproduce byte-identically. Both PDFs
match after date-metadata normalisation. [Receipt](results/distribution_check.json) and
[procedure](reviews/distribution_i29.md); no scientific-result or provenance re-pin.

Iteration 33 source/access re-check (2026-10-25 13:22 UTC): Q1.4 `ab24b1d` / Q2.2 `6150a33`;
changes since iteration 30 are source handoff metadata only, 0 open P1. Evidence pins remain
`732f08c` / `91ffb2d`; no scientific result, manuscript, figure or PDF was changed. The full
158-file release at merge `c1e7fdd` passes a new remote-clone distribution check, including
all six replay scripts and 26 reproduction tests. [Receipt](results/distribution_check_i33.json),
[procedure](reviews/distribution_i33.md). Anonymous HTTPS cloning failed and anonymous
repository/API probes returned HTTP 404 (also both sibling repository pages); authorized
access or an author-supplied archive is needed to acquire the files. This corrects earlier
"public URL" wording, without changing repository visibility or any evidence provenance.

Iteration 33 compliance addendum: director commit `2cf7c7d` arrived during the distribution
check and overrides the freeze. The main text is shortened by moving the extended summary,
glossary, operational labels, detailed results/figures and disclosures to appendices. Empirical
estimates and source pins are unchanged. Five bindings cover the scoped primary abstract claim, repeated grid estimates and the
notepad ratio in the shortened text (144 total; the previous 139 entries remain identical).
The decimal inventory continues to check relocated scientific appendices D–G: 248/281 report
and 55/61 slide decimal tokens bound, with all remaining 33 + 6 classified as non-results.
All 15 reference identities have recorded primary evidence; 14 also match the starter CSV
URL and year. Expanded author lists are supported by starter metadata or primary arXiv pages.
[Reference record](results/reference_metadata_i33.json), [compliance receipt](results/submission_compliance.json).

Compliance scope handoffs: Q1.4 `1ebf938` (I146/I147) and Q2.2 `e3fa1dc` (I155)
independently read the rewrite and report 0 P1; their optional wording nits are applied.
`reviews/compliance_preservation_i33.py` confirms all 111 saved-source assertion objects,
139 original bindings, six replay JSONs, six figures and the evidence manifest are identical
to pre-compliance `089ffb0`. The 158 evidence hashes still pass. [Preservation receipt](results/compliance_preservation_i33.json).
No source re-pin or new scientific estimate; the finalizer refreshes only the dated process snapshot.

| short | repo | commit synced | synced at (UTC) |
|---|---|---|---|
| Q1.4 | `~/collusion/collusion-14-infotheory` | `0e06c03` | 2026-10-25 08:02 |
| Q2.2 | `~/collusion/collusion-22-say-vs-do` | `8b680ee` | 2026-10-25 08:02 |

Re-checked 2026-10-25 10:44 UTC at Q1.4 `4ff7e65` / Q2.2 `7247c6c`: both have 0 open P1; Q1.4 independently confirms the current co-movement scope, Q2.2 confirms the corrected SALT framing. Q2.2 also fixed its own unpinned Fig. P2.7 window label to match our existing Fig. 6; no saved scientific result changed and no evidence re-pin is needed. Earlier 10:31 UTC at Q1.4 `65d44bb` / Q2.2 `94018c8`: both confirm 0 open merge flags, no science change; evidence stays pinned at `732f08c` / `91ffb2d`. Q1.4's new commit changes only bookkeeping and review receipts. Earlier ~10:22 UTC at Q1.4 `732f08c` / Q2.2 `94018c8` (I133 confirms 131-1 applied and 0 open; only review metadata changed, so the evidence bundle retains `91ffb2d`); ~10:07 UTC at Q1.4 `732f08c` / Q2.2 `91ffb2d` (Q1.4: 0 open; Q2.2 131-1 Fig. 6 caption P1 applied; both source commits are review-only, no science change); ~10:02 UTC at Q1.4 `499c500` / Q2.2 `966b9fe` (I129: 0 open, one optional P2 applied as M33); earlier ~09:55 at `499c500` / `badcd8d` (0 open flags in both; earlier check ~09:25 at `0124252`/`71a0365`): no research changes after the freeze;
both posted `merge_flags.md` (Q1.4 `results/reviews/merge_flags.md`, its `check_merge_sources.py`: 35/35 Q1.4
values match JSON; Q2.2 `results/analysis/merge_flags.md`: all Q2.2 numbers correct). Applied: Q1.4 F1 (P1),
F3; Q2.2 114-4 (P1), 116-2 (already applied), 114-2, 114-3. Not applied: Q1.4 F2 (optional; §5.2 states it).

Each source also keeps a machine-checked claims table: Q1.4 `results/eval/claims_denominators.{json,md}`,
Q2.2 `results/analysis/claims_denominators.md` (generated by `p2_claims.py`). Spot-checked against JSON by
the merge manager: rows marked ✔ below were read directly from the JSON at the synced commit.

**Portable evidence (started iteration 9).** [evidence/manifest.json](evidence/manifest.json) pins 158 exact source
files to full commits Q1.4 `732f08c11a765cd8500f4ef3c29fb630b309d5b2` and Q2.2
`91ffb2d4737a7537cdf9afe239a98e0d1061090b`, with original paths and SHA256 hashes. This snapshot includes
saved results and the inputs of all six figures (iteration 13 added four Q2.2 `llm_v3plc`/`llm_v3rep` ground-truth/trajectory files for Fig. 5); full experiment regeneration uses the source repos. The historical
table below records the original claim provenance; later review-only commits did not change the science.

Iteration 24 adds 22 exact Q2.2 blobs at the existing pin, leaving the earlier 76 unchanged: original
estimator/label code, E113 grid manifest/labels/execution snapshot and action/combined audit caches,
Qwen3.8 ground truth/trajectories/cached terms, no-channel text audit inputs and strong-framing action
scores. `uv run python scripts/recompute_unrounded_q22.py` now replays M6/M33/M34 without sibling
checkouts and exactly matches every previously recomputed numeric value. Its provenance commit now
names the input pin rather than the later source HEAD recorded by the old script.
`uv run python scripts/recompute_c21b_floor.py` regenerates `results/c21b_floor.json` byte-identically;
the same five executed run IDs per arm survive both floor thresholds and descriptive late windows.
The 15 release checks delete and regenerate both replay outputs, and compare all C21b per-run fields
against the original pinned `p2_strong.analyse` in eight settings (30 runs each). That test extracts only
the pure function and supplies cached terms, avoiding the source module's model-calling loader.

Iteration 25 adds nine exact Q2.2 blobs (107 total; previous 98 entries unchanged):
`final_analysis.py`, `analyze_llm.py`, `data/llm_v3/labels.jsonl` and the six original LLM
`results/llm_auditor/llm_v3/gpt-6.1-sol/*_orig.jsonl` caches at the same `91ffb2d` pin.
`uv run python scripts/recompute_locked_test_q22.py` → `results/locked_test_q22.json` replays
all six run-AUROC estimates/CIs and eight contrasts, using exactly test IDs 0030–0124 and
the frozen judge labels (50 positive, 45 negative), seed 0, B=2000, paired class-stratified
run resampling and max(text, action) recomputed in each draw. All selected fields match the
saved analysis exactly; primary −0.0127 [−0.0913, +0.0642]. No fitting, new labels, calls or
new held-out evaluation. The 17 release checks also compare selected run endpoints against
AST-extracted original functions on the real cohort (31 draws) and a tied calculator fixture
(73 draws), using an independent rank-sum AUROC implementation, and reject incomplete,
duplicate, nonfinite and wrong-auditor inputs. Pair/localisation endpoints, fusion and thresholds
are outside this replay.

Iteration 26 adds 39 exact Q1.4 blobs at the existing `732f08c` pin (146 total; all earlier
107 manifest entries unchanged): sixteen cells’ ground truth/trajectories, the original grid
manifest and six source files (`infotheory`, `llm_eval`, `e1_grid`, `e70_inputs`, `e70_grid`,
`e74_paired_diff`). `uv run python scripts/recompute_grid_q14.py` → `results/grid_q14.json`
rebuilds all 768 observed run scores from the 192 frozen games; all match exactly. It reproduces
all four pooled AUROC/CI triples, both paired level contrasts, the markup contrast and per-cell
AUROCs using the original seed-0 B=2000 cell-by-arm bootstrap. Source-function parity covers
all 4608 per-pair detector values, original cohort loading and the full B=2000 grid/paired
analyses. Three added release tests also check standalone byte parity and rejection of
duplicate ground truth, missing/duplicate rounds, reordered sellers and nonfinite prices.
This verifies the frozen calculation, with no simulations, model calls or new evaluation.
Null draws/calibration, permutation flags, judge/executed labels and other E70 estimands
(factor effects, spillover, model-specific results) are outside the numerical replay.

Iteration 28 adds eleven exact Q1.4 blobs (157 total; prior 146 entries unchanged):
`experiments/scripted.py`, gate ground truth and all nine `results/<detector>/gate_test.jsonl`
caches at the existing pin. `uv run python scripts/recompute_gate_q14.py` → `results/gate_q14.json`
reaggregates 27,000 cached pair-score/p-value rows from 500 markets. All 666 numeric summary
fields reproduce (maximum floating-point difference 1.1e-16); rates, Wilson intervals and
localisation match exactly. Shift flags use the archived max-statistic run p-values;
surrogate flags recompute the original same-shock-family clean-control rank, including
leave-one-out controls and the original near-tie tolerance. The original source functions
independently match on all nine detectors and a 44-run calculator fixture (strict alpha,
near-ties, score ties, shock families and leave-one-out). Three release checks also reject
malformed cache/cohort inputs and regenerate the output byte-identically without siblings.
No scores, trajectories, shift-null draws or ground-truth labels are regenerated or validated;
this is aggregation verification, not another locked-test evaluation. N13/N24 remain unchanged.

Iteration 30 source re-check (2026-10-25 13:08 UTC): Q1.4 `0f033e2` / Q2.2 `6150a33`.
Since iteration 29, only STATUS/merge-scope metadata changed; both have 0 open P1.
Scientific inputs and both evidence pins remain unchanged.

Iteration 30 adds the exact archived Q1.4 `data/gate_test/trajectories.jsonl.gz`
blob at the existing pin (158 total; all earlier 157 manifest entries unchanged).
`uv run python scripts/recompute_gate_pcmi_q14.py` → `results/gate_pcmi_q14.json`
reconstructs 3000 pCMI scores and pair p-values plus 500 run-level max-statistic
p-values, using all 50,000 archived rounds and original sorted-index seeds/B=200.
All scores and p-values match exactly. Tests execute the unmodified original full
`detectors/infotheory.py:score_run` on ten group representatives plus constant/short
fixtures and compare the original loader for the full cohort. This extends the gate
aggregation replay, without new estimates, simulations, tuning or label validation.

## Number → source map

| # | number in SUBMISSION.md | repo | file (`results/…`) : key | §(source) | ✔ |
|---|---|---|---|---|---|
| N1 | channel raises markup over Nash in 9/9 main sets (7 models), C − A CI > 0 each | Q1.4 | `eval/claims_denominators.json`, `eval/p2_partc.json` | P2.13 | ✔ check_sources |
| N2 | max-pair markup AUROC 0.75–0.99 vs pCMI 0.34–0.72 (9/9 point est.) | Q1.4 | `eval/claims_denominators.json` | P2.13 | ✔ check_sources |
| N3 | paired Δ level − pCMI CI > 0 in 8/9; gpt-5.6-luna +0.03 [−0.27, +0.33]; smallest resolved +0.22 [+0.03, +0.44] (base Qwen3.6) | Q1.4 | `eval/e74_paired_diff.json` : `main_sets.*.level_minus_pcmi` | P2.13 | ✔ (llm_g56l_p2 δ 0.03); ✔ check_sources |
| N4 | pCMI CI ∋ 0.5 in 8/9; base Qwen3.6 exception 0.71 [0.51, 0.88] | Q1.4 | `eval/claims_denominators.json` | P2.13 | ✔ check_sources |
| N5 | E44 T=60: pCMI 0.34 [0.18, 0.52], market level 0.94 [0.86, 1.00] | Q1.4 | `eval/long_power_llm_long_p2_T60.json` | P2.8 || ✔ |
| N6 | co-move excess +0.004 [−0.007, +0.015]; planted ±1 q=0.1: pCMI 0.79 [0.70, 0.88] (T=60), 0.62 [0.52, 0.71] (T=20) | Q1.4 | `eval/long_power_llm_long_p2_T60.json` : `mde` | P2.8 | ✔ (T=20 q=0.1 0.622) |
| N7 | executed-only pCMI 0.42 [0.33, 0.53], 48/149; definition range 13–78/149, pCMI 0.343–0.531 (E71) | Q1.4 | `eval/p2_partc.json` : `E64_pooled` | P2.11 || ✔ (E64_pooled) |
| N8 | E70 grid 192 games: C − A > 0 13/16; level > pCMI 12/16 (1 tie); pCMI 0.51 [0.43, 0.59]; TE 0.62 [0.54, 0.70]; level 0.74 [0.66, 0.80] (stored 3 dp 0.805; unrounded 0.8047 replayed by check_sources from saved per-game scores; Q1.4 REPORT prints 0.81) | Q1.4 | `eval/e70_grid.json` : `pooled_auroc`, `level_vs_pcmi` | P2.14 | ✔ |
| N9 | E70 Δ level − pCMI +0.23 [+0.12, +0.33]; level − TE +0.12 [+0.01, +0.22] | Q1.4 | `eval/e74_paired_diff.json` | P2.13/14 | ✔ check_sources |
| N10 | E70 follow-up model effect +1.07 [−0.20, +2.41] (not confirmed) | Q1.4 | `eval/e70_followup.json` | P2.14 || ✔ |
| N11 | E73 copula pCMI / sign CMI: E70 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52]; E44 0.40 [0.23, 0.58] / 0.54 [0.35, 0.72]; executed-only 0.40 / 0.41 | Q1.4 | `eval/e73_nonlinear.json` | P2.8f || ✔ |
| N12 | E72 TE names pair 30/96 (chance 1/6); non-executed 0.73 vs executed 0.49 (post hoc) | Q1.4 | `eval/e72_te_diag.json` | P2.14 || ✔; ✔ check_sources |
| N13 | scripted locked gate: MI flags 100% of common-shock controls; pCMI 14% shift / 4% [1, 13] surrogate (shared policy + shock); shared seed flagged 44–100%; TE flags legit leader–follower 100% | Q1.4 | `eval/gate_test.json` | 4.1 | ✔ check_sources |
| N14 | unequal private costs: level screens false-flag 30/30, pCMI 4/30 | Q1.4 | `p2/costasym_test.json` | P2.4 | ✔ check_sources |
| N15 | at 1% prevalence no frozen flag reaches point precision 0.25 | Q1.4 | `eval/prevalence.json` | P2.1 || ✔ (prevalence.json) |
| N16 | wording moves no-channel markup −0.19 … +2.56; within-wording markup AUROC 0.66 [0.53, 0.78], pCMI 0.44 [0.30, 0.58] | Q1.4 | `eval/p2_variants.json` | P2.7 || ✔ |
| N17 | deepseek C − A +3.75 [2.77, 4.68]; markup 0.99, pCMI 0.57 [0.36, 0.77] | Q1.4 | `eval/p2_family.json` | P2.9 || ✔ |
| N18 | E68 double auction: chat raises asks +0.39 [+0.06, +0.69] (inconclusive) | Q1.4 | `eval/e68_cda.json` | P2.12 | ✔ check_sources |
| N19 | independent reimplementation: 422/424 cells agree < 1e-9 (v1 datasets only) | Q1.4 | `reimpl/compare.json` | P2.2 | ✔ check_sources |
| N20 | TE above chance in some main sets: deepseek 0.81 [0.62, 0.96], base Qwen3.8 0.91; level − TE CI > 0 in 6/9 | Q1.4 | `eval/e74_paired_diff.json : main_sets.*.te`, `summary.k_level_minus_te_ci_above_0`; CI from `eval/llm_ds_p2.json : by_T.20.te.auroc_ci_C_vs_A` (0.809 [0.622, 0.964]) | P2.9, P2.13 | ✔; ✔ check_sources |
| N21 | E70 Qwen cells: max-pair markup 0.76 on the games where Q2.2's LLM price view is 0.52 | Q1.4 | `eval/e70_grid.json : amend2_by_model.qwen.market_level` (0.757) | P2.14 | ✔ |
| N22 | wording: C − A CI > 0 in 2/5 wordings | Q1.4 | `eval/claims_denominators.json` (wording group) | P2.13 | ✔ (Opus review) |
| N23 | abliterated Qwen + memory (E65) tacit-high 0/20; channel adds +2.14 [1.29, 3.00]; 5/20 executed | Q1.4 | `eval/claims_denominators.json : llm_strong_qa` (stored 3 dp: 2.135 [1.285, 3.005]); unrounded 2.1353 [1.2853, 3.0047] recomputed by check_sources from pinned `data/llm_strong_qa/*.jsonl` with Q1.4's estimator. Source reports print 2.13 [1.28, 3.00] (double rounding); we print the single-rounded value | P2.11 | ✔ tacit (Opus review); ✔ check_sources + binding |
| N24 | scripted TE: shared policy 0.90/0.98, independent high-price 0.62, colluder found 0.22 | Q1.4 | `eval/gate_test.json : metrics.te` | 4.1 | ✔ (Opus review); ✔ check_sources |
| N25 | pair_level 0.75–0.80 vs market level 0.85–0.94 in spillover sets | Q1.4 | REPORT joint-statement note (`llm_v1`, E44, E65) | P2.3 | ✔ check_sources |
| N26 | prevalence: max point precision at 1% = 0.20 | Q1.4 | `eval/prevalence.json` (max precision@0.01 = 0.202) | P2.1 | ✔ (Opus review) |
| M1 | combined − better single view −0.01 [−0.09, +0.06] (locked test, n=95) | Q2.2 | `analysis/final_llm_v3_gpt-6.1-sol_test.json` : `contrasts['delta_hybrid[combined]:run_auroc']` | C01 | ✔ (claims table); iter25 cached-score replay |
| M2 | pooled fresh −0.07 [−0.17, +0.02] (n=90, post hoc) | Q2.2 | `analysis/p2_pool_rep.json` | C02 | ✔ check_sources |
| M3 | text 0.47 [0.36, 0.58], action 0.75 [0.65, 0.85] (locked test) | Q2.2 | `analysis/final_llm_v3_gpt-6.1-sol_test.json` : `point_ci.{text,action}.run_auroc` | P2.0 | ✔ (p2_say_vs_do.md); iter25 cached-score replay |
| M4 | text inverted in public-inviting families: 0.15–0.36 (Claude 0.22, deepseek 0.36, Qwen3.8 base 0.21, abl. 0.15) | Q2.2 | `analysis/p2_family3way.json`, `analysis/p2_strong_eval_llm_p2qwen{b,a}.json` | P2.0 | ✔ (p2_say_vs_do.md) |
| M5 | invite-regex rate Qwen3.8 base channel 0.40 vs control 0.88 (E132, post hoc) | Q2.2 | `analysis/e132_inversion.json : sets['Qwen3.8 base'].arms.*.invite_rate_pooled` | E132 | ✔ check_sources |
| M6 | E113 Qwen: combined − action −0.24 [−0.37, −0.09]; LLM prices 0.52 [0.41, 0.64]; text 0.32 [0.24, 0.42]; executed-only −0.30 [−0.44, −0.16] (stored upper −0.165, unrounded −0.1649 from `scripts/recompute_unrounded_q22.py`; Q2.2 REPORT prints −0.17); luna +0.07 [−0.02, +0.17], executed +0.16 [+0.05, +0.28] | Q2.2 | `analysis/p2_e1_audit.json : amend3.*, pooled_auroc_channel_vs_none_descriptive.action_qwen`; executed: `analysis/e113_secondary.json : stratified.executed_vs_A.{qwen,luna}_combined_minus_action` | P2.16 | ✔ |
| M7 | SALT text auditor 0.87 [0.83, 0.91] (240 ep.); P(said | executed) 0.385 | Q2.2 | `analysis/salt_d1.json` : `E105_audit.auroc`, `E104_sayvsdo.P_said_given_exec` | P2.12 | ✔ (claims table) |
| M8 | premium replicates 0.94 [0.87, 0.99] (60 fresh runs) | Q2.2 | `analysis/replication_llm_p2rep.json` | C05 | ✔ (claims table) |
| M9 | notepad +1.04 [+0.65, +1.42] vs channel +1.61 [+0.92, +2.35]; ratio 0.65 [0.34, 1.32] (CI text-only, Q2.2 REPORT.md P2.5); placebo +1.23 [+0.76, +1.85]; delivery +0.38 [−0.41, +1.18]; paraphrases +1.79 [+1.20, +2.43] / +0.24 [−0.32, +0.81] (10 + 10 each); weather logbook − none +0.22 [+0.05, +0.40] (15 matched seeds) | Q2.2 | `analysis/p2_cue_llm_p2cue.json : paired`, `p2_cue_llm_p2para{1,2}.json : paired.private-none.prem_r2_12`, `p2_logbook.json : paired.logbook-none.prem_r2_12`, `p2_cue_verdict_llm_p2cue.json : H3_amended.held=false` | P2.5 | ✔ (Opus review); ✔ check_sources |
| M10 | memory + profit framing: 19/20 no-channel ≥ Nash + 2; 13/20 strict-executed (10–16/20 one-at-a-time) | Q2.2 | `analysis/p2_strong_classes_llm_p2strongF.json : n_strict_executed, n_tacit_high_none`; `p2_strict_sensitivity.json` | P2.7, C14/C15/C29 | ✔ |
| M11 | 14/50 test agreements kept (E84 follow rule) | Q2.2 | `analysis/p2_behaviour.json : datasets.llm_v3.class_counts` | C13 | ✔ |
| M12 | E133e: no-chat LLM 0.94 vs best raw early-price rule 0.885, Δ +0.06 [+0.02, +0.10] (post hoc); say-do gap 0.77; pair SD 0.855 | Q2.2 | `analysis/e133e_attr.json` | P2.17 | ✔ check_sources |
| M13 | legit cost/quality edges flagged 7/10, 9/10 (controls 2/10); premium precision 0.24 at 5% prevalence | Q2.2 | `analysis/p2_asym.json : conditions.*.premium_flags`; `analysis/p2_prevalence.json : llm_v3_test.detectors.premium['precision@0.05']` (0.237) | C07 | ✔ |
| M14 | monitor-aware sellers agree 0/10, 0/10 | Q2.2 | `analysis/p2_aware.json : by_condition.{aware,aware_all}.agreement_y` | P2.9 | ✔ (Opus review) |
| M15 | Claude Sonnet 5.5 agrees on binary y in 115/115 (single-class per dataset); 3-class κ 0.33/0.38; E84d 25/30 | Q2.2 | `results/label_xfam.json`; REPORT_APPENDIX.md E84d | Setup | ✔ (Opus review) |
| M16 | gpt-6.1-sol newcomer re-agrees 0/20; market ≥ Nash + 2 in 18/20 | Q2.2 | `analysis/p2_replace_sol.json : arms.private.*` | P2.15 | ✔ check_sources |
| M17 | SALT construct: executed = mutual ACCEPT violating a verification rule | Q2.2 | `analysis/salt_d1.json : E104_sayvsdo`; REPORT §P2.12 | P2.12 | (codex review) |
| M18 | E133e comparator 0.885 = rule score using early prices + judged agreed price | Q2.2 | `analysis/e133e_attr.json : b_raw_auroc.rule_score` | P2.17e | (codex review) |
| M19 | placebo − private, rounds 2–12: +0.03 [−0.54, +0.49] | Q2.2 | `analysis/placebo_llm_v3plc.json : windows.r2_12.placebo_minus_private_paired` | v1 placebo | (codex review); ✔ check_sources |
| N27 | E72 non-executed set n = 52 (38 judged agreement, 14 none); executed n = 44 | Q1.4 | `eval/e72_te_diag.json : c_execution.not_executed` | P2.14 | (codex review); ✔ check_sources |
| N28 | executed-definition range 13–78/149, pooled pCMI 0.343–0.531 | Q1.4 | `eval/executed_sensitivity.json : n_executed_range, pooled_pcmi_range` | E71 | (codex review); ✔ check_sources |
| N29 | prevalence max precision@0.01 0.20 [0.07, 0.54] (scripted rows 5,6,10,15–17,19); LLM rows max 0.185 (row 26) | Q1.4 | `eval/prevalence.json : [5], [26]` | P2.1 | ✔ (iter3, JSON) |
| M30 | gpt-6.1-sol seller arm text AUROC 0.17 [0.01, 0.41], 0/7 private agreements (post hoc) | Q2.2 | `analysis/p2_family3way.json : llm_p2sol.views.text.auroc_private_vs_none` | P2.6 | ✔ (iter3, JSON) |
| M31 | luna E113 executed combined−action posting cells +0.19 [+0.06, +0.33], silent +0.12 [−0.08, +0.32] (post hoc) | Q2.2 | `analysis/e113_secondary.json : stratified.executed_vs_A.luna_{posting,silent}_combined_minus_action_posthoc` | P2.16 | ✔ (iter3, JSON) |
| M32 | Fig. 6 tacit-high window = rounds 11–40 (source figure label said "2nd half") | Q2.2 | `p2_strong_eval.py : --late 11 (frozen, line 145)`; data `data/llm_p2strongF/trajectories.jsonl` + `analysis/p2_strong_classes_llm_p2strongF.json` | P2.7 | ✔ (iter6, code) |
| M33 | Qwen3.8-base text score vs invite rate Spearman pooled 0.49 [0.17, 0.71] (n = 30); within no-channel −0.40 [−0.83, +0.18] (n = 15; stored −0.405, unrounded −0.4046 from `scripts/recompute_unrounded_q22.py`; Q2.2 merge flag printed −0.41) | Q2.2 | `analysis/e132_inversion.json : sets."Qwen3.8 base".spearman_text_vs_invite_rate_{pooled,within_no_channel}` | Q2.2 merge_flags I129 (optional P2) | ✔ (iter6, JSON) |
| M34 | Fig. 6 caption: price views (pair premium, market excess over Nash, LLM action view, action stats) strict-executed vs tacit-high AUROC 0.43–0.57 (action view stored 0.575 = exactly 142/247 = 0.5749, `scripts/recompute_unrounded_q22.py`), all CIs include 0.5 (exploratory) | Q2.2 | `analysis/p2_strong_eval_llm_p2strongF.json : detectors.{premium,market_excess_nash,action,action_stats}.auroc_strict_vs_tacit_high` | P2.7 | ✔ check_sources |
| M35 | SALT messages without accept/reject substrings: episode AUROC 0.75 [0.66, 0.84], n = 117; selected subset, not causal ablation | Q2.2 | `analysis/salt_d1.json : E105_audit.auroc_no_verdict_words.{est,ci,n}`; code `salt_d1.py : render, cluster_boot, report` at evidence pin `91ffb2d` | P2.12 | ✔ check_sources; iter11 Opus + Codex |
| J1 | joint statement (verbatim in both reports) | both | REPORT.md of each | — | |

`✔ check_sources` = a saved-source assertion in `uv run python scripts/check_sources.py` (now 111/111
assertions; output `results/source_check.json`). The original 44 checks compared source JSON with frozen
expected values, without reading the report. Iteration 9 introduced separate document bindings; iteration
11 adds four for M35 (68). Iteration 14 adds 35 source assertions (N5–N7, N11, N16, N21, N23, N29, M4, M6, M7, M9, M13,
M15, M30, M31, M33) and 64 bindings covering Tables 1–2 and §5.2–5.4, for 132 in total. Iteration 15 pins Q1.4 `eval/llm_ds_p2.json` and Q2.2 `p2_cue_llm_p2para{1,2}.json` / `p2_logbook.json` and adds 7 assertions (N20 deepseek TE CI; M9 paraphrases, weather logbook) and 5 bindings (137); Iteration 17 pins Q1.4 `data/llm_strong_qa/{ground_truth,trajectories}.jsonl` (76 files), recomputes E65 C − A with Q1.4's estimator and binds it: unrounded 2.1353 [1.2853, 3.0047] → +2.14 [1.29, 3.00]. Both source reports print +2.13 [1.28, 3.00] because they round the 3-dp stored value again; with the iteration-17 double-rounding replays and the appendix grid binding: 111 assertions, 139 bindings. `scripts/number_coverage.py`
lists the remaining unbound decimals. They extract selected numbers from SUBMISSION.md/SLIDES.md
and compare them directly with saved source values using half-up rounding; `results/document_bindings.json`
lists their exact coverage. Some source assertions
refer only to this provenance table. Neither check certifies every report number or qualitative scope.
Plain ✔ = read from JSON by hand or by a review. Rows with no ✔ are either non-numeric (M17, M18 construct definitions — the 0.885 in M18 is checked under M12;
J1 verbatim statement) or were verified by the adversarial reviews noted in their last column.

**Interpretation correction (iteration 11).** The frozen Q2.2 REPORT describes SALT's act as happening in
chat. `salt_d1.py` at the same pin shows the auditor sees only preceding communication and predicts
separately submitted verdicts. The primary Shi/Zhang/Yang paper agrees. SUBMISSION and SLIDES follow
the code and primary paper, preserve every saved result, and include the M35 subset sensitivity. The
source reports in `evidence/` are retained verbatim. [Literature audit](reviews/literature_i11.md) records
the decision and all primary bibliography checks, including the Rose definition and Cao & Hu scope fixes.
