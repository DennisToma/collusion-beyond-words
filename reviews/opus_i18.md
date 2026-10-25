# Opus 5.5 subagent final judge review, iter18 (2026-10-25 ~12:00 UTC)

Same prompt as codex_i18. Result: 4 P1, 7 P2 and 3 P3. All P1s were stale process counts or overclaims in README/REPORT; SUBMISSION had no wrong number. Corrected iter17 values were consistent everywhere (no stale 2.13/0.81/−0.17/−0.41/0.58 except "was" values in REPORT). Counts (111/139/76, 222/260, 55/61, 17 pp, 8 slides) matched the receipts.

| # | sev | finding | action (iter18) |
|---|---|---|---|
| 1 | P1 | README "four figure scripts" / "four regenerated figures" vs six | fixed (six, Fig. 1–6) |
| 2 | P1 | REPORT "Fig. 1/3/4/6 rendering" | fixed (all six figures) |
| 3 | P1 | export counts 487 fragments / 19 headings stale | fixed (now 492 after the iter18 edits / 21) |
| 4 | P1 | REPORT "no real claim remains unbound" overclaims vs 222/260 | replaced with the 38/6 unbound decimals statement |
| 5 | P2 | Fig. 1 "right panels" (figure has rows) | fixed: "groups C and D right of the vertical line" |
| 6 | P2 | stacked semicolons in Prevalence bullet | split into sentences |
| 7 | P2 | logbook "so being singled out alone produces little" causal | "suggesting …; not a matched contrast" |
| 8 | P2 | "single-class" unclear | spelled out |
| 9 | P2 | abstract 9/9 omits one-prompt-family / 2/5 wordings scope | added to abstract item 1 |
| 10 | P2 | REPORT "All 66 source blobs" stale | "then in the bundle (now 76)" |
| 11 | P2 | Appendix B C21b F ≥ 12 vs §3 F ≥ 13 | recomputed (scripts/recompute_c21b_floor.py → results/c21b_floor.json): 5/15 per arm under both floors and both late windows; reading note added |
| 12 | P3 | TE on colluder groups "8–22%" vs figure 0 | text is the shift-null rate (gate_test.json te.C/D flag_rate 0.22/0.08); added "(0–20% under the surrogate null)" |
| 13 | P3 | "Both projects state jointly" | "Read together, the two projects suggest" |
| 14 | P3 | REPORT reviews list stale | updated |
