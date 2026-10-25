# Opus final-claims review of SUBMISSION v1.2 + SLIDES (2026-10-25 ~10:00 UTC, fresh subagent, read-only)

Verdict: no P1 (no wrong numbers, no CI-unsupported claims); all 6 figures present; sources unchanged since sync.

Applied (all evidence re-checked by the manager against source JSON):
- P2-1 §6 logbook control: term defined; premium +0.22 [+0.05, +0.40] vs +1.04 (Q2.2 `p2_logbook.json` paired.logbook-none.prem_r2_12).
- P2-2 Abstract: inversion range now covers both Qwen families (Qwen3.8 0.15–0.21; Qwen3.6 grid 0.32 [0.24, 0.42], `p2_e1_audit.json` text_qwen).
- P2-3 Glossary: C − A = mean all-seller markup over Nash (Q1.4); Q2.2 uses designated-pair premium.
- P3-1 mechanism: "consistent with, not shown to cause"; within-arm Spearman −0.41 [−0.83, +0.18] (`e132_inversion.json`).
- P3-2 removed repeated sentence (§5.3 E113 paragraph).
- P3-3 abstract: "at chance (all three CIs include 0.5)".
- P3-4 TE recall on scripted colluders 8–22% (`gate_test.json` te.C 0.22, te.D 0.08).
- P3-5 SALT 62% scoped to full dataset (5169 executed episodes, `salt_d1.json` E104_sayvsdo).

Numbers verified correct by the reviewer (JSON key + value quoted in its report): Q1.4 N1–N9, N13, N14, N18–N21,
N24–N29; Q2.2 M1–M7, M9, M12, M16, M19, M31; §3 market parameters.
