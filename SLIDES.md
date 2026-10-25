# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

**Dennis Toma** — Apart Research AI Collusion Sprint, 23–25 October 2026

Merged submission of two sprint projects:
- **Q1.4** — information-theoretic, prices-only detection (does collusion leave a *dependence* fingerprint?)
- **Q2.2** — say vs. do: does an LLM auditor gain from reading *public messages* on top of prices?

Shared setup: four LLM sellers in repeated logit-demand pricing markets; one pair is *offered* a private chat
channel (never told to collude). Can an auditor tell which markets had the channel?

Every number traces to a JSON file and commit in `SOURCES.md`.

---

## 1. Positive control: on scripted sellers, conditioning works

![Scripted hard negatives](figures/fig1_scripted_hard_negatives.png)

- Planted colluding pair: flagged and localised by every contemporaneous detector in 100% of runs.
- Conditioning on public state + lagged prices (pCMI) cuts common-shock false flags from 100% (raw MI) to 14%; held-out *shared policy + common shock*: 4% [1, 13].
- Structural limits: shared-seed copies of one policy look like collusion (44–100%); level screens false-flag unequal costs in 30/30.

---

## 2. With LLM sellers, the channel shows up as a price *level*

![Level vs co-movement](figures/fig2_level_vs_comovement_9sets.png)

- Markup over Nash rose in **9/9** main sets (7 seller models).
- Max-pair markup AUROC 0.75–0.99 vs pCMI 0.34–0.72; paired difference CI > 0 in 8/9.

---

## 3. No contemporaneous co-movement detected

| evidence | markup (level) | pCMI (co-movement) |
|---|---|---|
| E70 grid, 192 games, 7 factors | 0.74 [0.66, 0.81] | 0.51 [0.43, 0.59] |
| E44 long games, T = 60 (pre-registered) | 0.94 [0.86, 1.00] | 0.34 [0.18, 0.52] |
| executed agreements only (48/149) | pair-level 0.87 [0.80, 0.94] | 0.42 [0.33, 0.53] |

- Rank and discrete estimators: also at chance. At T = 60, pCMI would catch a planted shared ±1 move at q = 0.1 (0.79 [0.70, 0.88]); at T = 20 small co-movement is not excluded.
- Lagged TE weakly above chance in the grid (0.62 [0.54, 0.70]) but below level, and fires on shared policies.

---

## 4. Public words: no resolved gain for a zero-shot auditor

![Say vs do](figures/fig4_say_vs_do_summary.png)

- Combined − better single view: −0.01 [−0.09, +0.06] (locked test, n = 95); −0.07 [−0.17, +0.02] (fresh replications, pooled post hoc).
- Qwen3.8 text view is **inverted** (0.15–0.21, CI below 0.5): channel sellers invite rivals publicly *less*.
- Text works where the act *is* the talk (SALT-NLP negotiations, 0.87 [0.83, 0.91]) — a different construct.

---

## 5. Neither signal is specific to collusion

![Placebo](figures/fig5_placebo_premium.png)

- Unread private *notes-to-self* notepad: ≈ two thirds of the channel premium (ratio 0.65 [0.34, 1.32]); the premium is there from round 1, before any message is delivered.
- Memory + profit framing: 19/20 gpt-6-luna markets *without* a channel price ≥ Nash + 2.
- Prompt wording alone moves no-channel markup from −0.19 to +2.56; channel effect resolved in only 2/5 wordings.
- At 1% prevalence no frozen price flag reaches point precision 0.25.

---

## 6. Implications

- Channel assignment (including its prompt cue) is visible as **how high** prices are — not **how they move together**, and not in **what is said publicly**.
- Detectability by any price statistic is a property of the **(seller model × prompt)** pair (post-hoc synthesis).
- Practical reading: a cheap level screen against a **model- and prompt-matched** reference as a first-stage *audit trigger*; expensive audits (private logs, dependence statistics, provenance) only on flagged pairs. Not evaluated end to end.

---

## 7. Limitations and next steps

**Limitations:** one judge family for labels (gpt-6.1-sol); small samples (10–21 games per arm), uncorrected per-set CIs; narrow four-seller markets; no evasion test (monitor-aware sellers stopped agreeing rather than hiding); placebo leaves delivery unresolved.

**Next:**
1. Instructed / red-teamed colluders (coded public signals, gradual drift).
2. Ground truth independent of prices, judged by several model families.
3. Larger placebo study to isolate delivered coordination.
4. Mixed-family markets + provenance data for shared-model / shared-seed confounds.
5. End-to-end evaluation of the two-stage audit.
