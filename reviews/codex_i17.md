# codex gpt-6.1-sol (high, read-only) review of iter17 double-rounding diff f5e91e5..b1a92f6

Final findings (raw transcript 237 KB not kept):

- **P1 — [SUBMISSION.md:484](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:484):** Appendix E1 still prints grid market-level AUROC `0.74 [0.66, 0.81]`. Independent replay of `e70_grid.py` gives upper bound `0.8047092013888888`, which rounds to **0.80**. This contradicts the corrected main table and slides.

- **P3 — [SUBMISSION.md:435](/home/factory/collusion/collusion-beyond-words/SUBMISSION.md:435):** “Five printed values” should say **five claims** or **six numeric values**: E65 changes both its estimate and lower endpoint; four other numbers change.

All corrected estimates independently match the source code/data. Replay seeds, B, and resampling order match. No other stale occurrences for these claims were found; the disclosure’s substantive rounding explanation is accurate.

## Resolution
- P1 fixed: Appendix A E1 row now 0.74 [0.66, 0.80]; header notes the single deviation from verbatim; new binding (139) rejects 0.81 there.
- P3 fixed: disclosure says 'Five claims (six numbers)'.
