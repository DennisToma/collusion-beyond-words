# PLAN — merged submission: "Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence"

This repo turns the two research repos into ONE Apart sprint submission. Sources (read-only):
`~/collusion/collusion-14-infotheory` (Q1.4) and `~/collusion/collusion-22-say-vs-do` (Q2.2) — their
REPORT.md, results/, figures/, EXPERIMENTS.tsv. They keep running until Sun 15:00 UTC; re-sync numbers
from their latest commits each iteration (record the source commit hashes in SOURCES.md).

## Deliverables (hard stop Sun 18:00 UTC; finalize-only from Sun 16:30)
1. `SUBMISSION.md` + `SUBMISSION.pdf`: Apart research-report format (≈ 6–10 pages main text):
   title, authors (Dennis Toma), abstract, introduction + related work (cite the papers the source repos
   cite; starter `literature/`), methods (shared market, LLM sellers, labels, detectors, auditors,
   nulls, splits), results (one coherent story: LLM collusion shows up in price level, not in dependence
   or in public words — or whatever the Phase 2 results say; update the story if Phase 2 changes it),
   robustness (prompt artifact, model families, prevalence/precision, adversarial), limitations,
   implications (cheap screen → expensive audit), future work, appendix with full tables.
2. `figures/`: 4–6 figures copied/regenerated from the source repos, consistent style.
3. `SLIDES.pdf`: ≤ 8 slides for a short presentation.
4. Every number traceable: a table in `SOURCES.md` mapping each number to source repo, file, commit.
5. Two adversarial reviews (codex gpt-6.1-sol AND an Opus subagent) of all claims vs source JSON; fix.

Never invent numbers; if sources disagree, say so and pick the more conservative reading.
