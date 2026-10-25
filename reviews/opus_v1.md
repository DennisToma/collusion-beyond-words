# Opus 5.5 adversarial review, round 2 (SUBMISSION v1.1 + SLIDES), 2026-10-25 ~09:00 UTC

~60 numbers checked against source JSON (Q2.2 M1–M3, Table 2, invite rates, E113 deltas, cue/placebo/paraphrase,
19/20, 13/20, asymmetry flags, precision 0.24, 14/50, 0/10, +0.03, 0.94; Q1.4 9-set ranges, E74 deltas, TE,
gate numbers, Qwen3.6 exception, E70 pooled): **0 numeric mismatches**.

| # | sev | where | issue | status |
|---|---|---|---|---|
| 1 | P1 | SUBMISSION §5.3 E113 luna | "+0.16 on executed … text can help" — silent luna cells (no public posts) show similar +0.12 [−0.08, +0.32] (`e113_secondary.json:stratified.executed_vs_A.luna_silent_combined_minus_action_posthoc`; Q2.2 REPORT l.398 "cannot be credited to text") | applied (verified JSON) |
| 2 | P1 | SLIDES §6 | "not how they move together, and not in what is said publicly" drops TE caveat, "mainly", and inverted Qwen text | applied |
| 3 | P2 | SUBMISSION §6 | "not in how they move together" → detected contemporaneous co-movement (+ TE caveat) | applied |
| 4 | P2 | abstract end | add "could serve … (not evaluated end to end)" | applied |
| 5 | P2 | §5.3 inversion | gpt-6.1-sol seller arm (0/7 private agreements) also inverted 0.17 [0.01, 0.41] (`p2_family3way.json:llm_p2sol`) | applied (verified JSON) |
| 6 | P2 | SLIDES §4 | invite rates measured on base arm only, post hoc (0.40 vs 0.88) | applied |
| 7 | P2 | SLIDES §5 | round-1 premium is from separate placebo run, not notepad study | applied |
| 8 | P2 | SLIDES §4 | SALT "text works where act is the talk" reintroduces removed framing | applied |
| 9 | P2 | SLIDES §7 | "10–21 games per arm" → "in most sets; 5+5 Claude; 6+6 per grid cell" | applied |
| 10 | P2 | SLIDES §5 | prevalence: add hypothetical, max 0.20, set by α | applied |
| 11 | clarity | abstract/slides | jargon before definition: glossary moved under abstract, "executed" + "Nash + 2" defined; terms line on title slide | applied |
| 12 | clarity | SLIDES §3 | E70/E44/q IDs → plain words | applied |
| 13 | clarity | abstract | too long: TE CI, SALT sentence, 30/30 moved to body refs | applied (≈320 → 300 words) |
