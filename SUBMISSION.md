# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

**Dennis Toma** — Apart Research AI Collusion Sprint, 23–25 October 2026

*Merged submission of two sprint projects: Q1.4 (information-theoretic, prices-only detection) and Q2.2
(auditing what agents say together with what they do). Every number below is taken from the frozen
source repos at the commits listed in [SOURCES.md](SOURCES.md), which maps each number to its JSON file.
Draft v0 (2026-10-25 08:30 UTC); numbers not yet independently re-verified are marked in SOURCES.md.*

## Abstract

When LLM pricing agents are given a private channel, can an auditor tell — from prices, from public
messages, or from both? We study four-seller repeated price markets with LLM sellers (7 seller models,
two market implementations) in which one pair is offered an unmonitored chat channel and is never told to
collude. **Prices: the channel shows up as a price level, not as co-movement.** The channel raised markup
over Nash in 9/9 main sets, and a simple max-pair markup screen beat a conditional-dependence detector
(pCMI) in 9/9 (AUROC 0.75–0.99 vs 0.34–0.72; paired difference CI > 0 in 8/9). pCMI stays at chance in a
192-game seven-factor grid (0.51 [0.43, 0.59]), at T = 60 (0.34 [0.18, 0.52], pre-registered), on executed
agreements only (0.42 [0.33, 0.53]) and with rank-based or discrete estimators, although on scripted
sellers it finds every planted pair and removes most common-shock and shared-policy false alarms.
**Words: public messages add nothing and can mislead.** A zero-shot LLM auditor reading prices plus public
messages does no better than its better single view (−0.01 [−0.09, +0.06], locked test, n = 95; −0.07
[−0.17, +0.02] on fresh replications); in families that talk publicly in every market, text ranks control
markets *above* channel markets (AUROC 0.15–0.36), and on Q1.4's Qwen grid adding text lowers AUROC
(combined − prices −0.24 [−0.37, −0.09]). Text helps only where the deal is the conversation (SALT negotiations, 0.87 [0.83, 0.91]).
**Neither signal is collusion-specific.** An unread private pricing notepad produces 65% of the
channel's premium; with memory and profit framing 19/20 *no-channel* markets price ≥ Nash + 2; level
screens false-flag 30/30 scripted markets with unequal costs; and at 1% prevalence no flag reaches
precision 0.25. Price statistics are therefore a cheap first-stage screen whose references must be matched
to the seller model and prompt, not a verdict.

## 1. Introduction

Algorithmic pricing agents built on LLMs reach supracompetitive prices without instruction (Fish et al.
2024) and change behaviour when they can communicate (Agrawal et al. 2025). Regulators and platform
operators will mostly see two things: the agents' *actions* (prices) and whatever they *say* in public.
Two natural detection strategies follow:

1. **Information theory on actions** (Q1.4). Colluders should share information beyond what public state
   explains, so their prices should be conditionally dependent (Bonjour et al. 2022). This promises a
   detector that is blind to the channel content and hard to evade by choosing words.
2. **Say + do auditing** (Q2.2). An LLM auditor reading both public messages and prices should catch
   inconsistencies between what agents say and what they do, and beat single-stream auditors.

We test both on the same family of LLM markets, cross-apply each project's detectors to the other's data,
and keep three label levels apart: *assigned opportunity* (channel offered), *verified agreement* (judge
reads the private chat) and *realised coordination* (prices follow the agreement).

**Contributions.**
- A prices-only conditional-dependence detector (pCMI, with shift and same-model surrogate nulls) that
  passes a scripted positive control and a hard-negative battery (common shocks, shared policies,
  legitimate leader–follower pricing), plus an honest map of what it cannot separate (shared random seeds).
- Evidence across 9 main LLM sets, a 192-game factorial grid and a pre-registered long-game test that LLM
  channel collusion appears as a **price level**, with no detected contemporaneous co-movement.
- A registered say-vs-do comparison showing that public text adds no resolved detection value, can be
  **inverted**, and helps only when the act happens in the conversation.
- Confound analyses (prompt artefacts, placebo, tacit high prices, cost asymmetry, prevalence) showing
  why any price screen is an audit trigger, not proof.

## 2. Related work

*Dependence as a collusion signal.* Bonjour et al. (2022) measure collusion as statistical dependence
between agents' actions; our pCMI is a conditioned pairwise version. Banchio & Mantegazza (2023) show
supracompetitive play from "spontaneous coupling" without agreement — the case our shared-shock and
shared-policy hard negatives target. Tailor (2025) applies mutual-information detectors to steganographic
message channels; we apply the same estimator family to actions. Transfer entropy follows Schreiber (2000).
*LLM pricing collusion.* Fish et al. (2024), Agrawal et al. (2025; double auctions), Lin et al. (2024;
market division expressed in actions, not messages), Dhanda (2026; price caps as focal points).
*Shared models.* Cao & Hu (2026) show supracompetitive prices from a shared LLM advisor without
coordination, motivating our same-model references. *Definitions.* Rose et al. (2026): communication within
a subgroup leading to actions harmful to outsiders; Calvano et al. (2020) and Green & Porter (1984) for
repeated-pricing benchmarks. *Message-side collusion.* Motwani et al. (2024) and Mathew et al. (2024) study
secret/steganographic collusion in messages; SALT-NLP negotiation data serve as our external text case.

## 3. Setup

**Markets.** Two four-seller repeated price markets with multinomial-logit demand, public cost and demand
shocks, and integer prices:
- *Q1.4 market* (`sim/market.py`): cost 6/8, static Nash price 10 (cost 8: 12), joint-profit optimum 16;
  T = 20 in most LLM sets (T = 40–60 in long-game sets).
- *Q2.2 market* (`llm_market.py`): 12 rounds, prices 6–30, static Nash ≈ 11, joint monopoly ≈ 19;
  arms `private` (pair has a channel), `none`, and `legit` (publicly announced cost-saving partnership,
  hard negative).
Each project also runs the other's data: Q1.4 scored Q2.2's `llm_v3` market; Q2.2 audited all 192 games
of Q1.4's E70 grid (E113).

**LLM sellers.** Q1.4's nine main sets use seven seller models: gpt-6-luna (main), gpt-5.6-luna,
deepseek-v4.1-flash, and base and abliterated (refusal-removed) Qwen3.8-27B and Qwen3.6. Q2.2's main market
uses gpt-6-luna and adds family arms (Claude Sonnet, deepseek, Qwen3.8 base/abliterated, gpt-6.1-sol). Profit-maximisation /
economics-lab framing after Fish et al. (2024); the channel pair is never instructed to collude. A public
message board exists in every arm.

**Labels.** A gpt-6.1-sol judge reads only the private chat (never prices) → explicit agreement /
information exchange / none; Claude Sonnet 5.5 re-judged 115 chats and agreed on the binary label in
115/115. *Executed* agreements are defined from prices (each project's own frozen rule, stated where
used); *tacit-high* = a no-channel market with second-half mean ≥ Nash + 2.

**Splits and discipline.** Scripted detector settings were tuned only on dev seeds and evaluated once on
locked seeds (1001/1002); no detector setting was tuned on LLM data. Q2.2's auditors are zero-shot with one
prompt per view, evaluated once on a locked test split (runs 0030–0124, n = 95) and replicated on fresh,
pre-registered splits. Most Phase 2 experiments were declared before their data existed; post-hoc analyses
are labelled.

## 4. Methods

**Price detectors (Q1.4, prices only).** Per pair: |Pearson|, plug-in MI, CMI given public state, and
**pCMI** = −½ log(1 − ρ²) of residuals after regressing each seller's price on state dummies and all four
lagged prices; transfer entropy (TE, lagged, max over directions). Two nulls: a circular-shift null
(B = 200, relative offsets ≥ 3 rounds), and a **same-model surrogate null** ranking the run's max-pair
score against no-channel games of the same model and shock family. Level screens: *max-pair markup* over
the per-round Nash price and *pair_level* (pair mean minus rivals). An independent reimplementation agreed
on 422/424 run × statistic cells to < 1e-9.

**Auditors (Q2.2).** One zero-shot gpt-6.1-sol auditor, same task text, six views: `text` (public messages
+ public facts), `action` (prices, costs, demand, profit), `action_stats` (+ computed pair-statistics
table), `combined` (text ∪ action), `combined_stats`, `structured`. Registered primary contrast:
Δ_hybrid = AUROC(combined) − max(AUROC(text), AUROC(action)).

**Statistics.** Run-level AUROC with class-stratified game bootstrap 95% CIs; Wilson intervals for flag
rates; Jeffreys for precision. CIs are per-set and uncorrected for multiplicity unless stated.

## 5. Results

### 5.1 On scripted sellers, conditioning works (positive control)

![Scripted hard negatives](figures/fig1_scripted_hard_negatives.png)
*Figure 1 (Q1.4 §4.1, locked seed 1001, 50 runs per group). Run-level flag rates at α = 0.05.*

Every contemporaneous detector flags and localises the planted pair in 100% of runs. Raw MI flags 100%
of common-shock controls; conditioning on public state and lagged prices (pCMI) cuts this to 14% under the
shift null and, for the held-out *shared policy + common shock* hard negative, 4% [1, 13] under the
same-model surrogate null. Two failure modes are structural: two copies of one policy sharing a random
seed are flagged by every contemporaneous detector (44–100%) — from price data they *are* a private shared
signal — and lagged TE flags legitimate public leader–follower pricing in 100% of runs. Level screens fail
elsewhere: unequal private costs are false-flagged in 30/30 scripted markets (pCMI 4/30).

### 5.2 With LLM sellers, the channel shows up as a price level, not co-movement

![Level vs co-movement](figures/fig2_level_vs_comovement_9sets.png)
*Figure 2 (Q1.4 P2.13). Nine main sets, seven seller models: channel − no-channel markup and run AUROC
with game-bootstrap 95% CIs.*

| evidence | max-pair markup (level) | pCMI (co-movement) | source |
|---|---|---|---|
| 9 main sets, 7 models | AUROC 0.75–0.99; C − A > 0 in 9/9 | 0.34–0.72; CI ∋ 0.5 in 8/9 | N1–N4 |
| paired Δ level − pCMI | CI > 0 in 8/9 (exception gpt-5.6-luna +0.03 [−0.27, +0.33]) | | N3 |
| E70 grid, 16 cells × 7 factors, 192 games | 0.74 [0.66, 0.81]; level > pCMI in 12/16 cells | 0.51 [0.43, 0.59] | N8 |
| E44 long games, T = 60 (pre-registered) | 0.94 [0.86, 1.00] | 0.34 [0.18, 0.52] | N5 |
| executed agreements only (48/149) | (inflated by construction) | 0.42 [0.33, 0.53] | N7 |
| rank (copula) pCMI / sign-change CMI, E70 | | 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52] | N11 |

The null is not an estimator artefact (rank-based and discrete estimators are also at chance) and not a
pure power failure at T = 60: observed co-move excess is +0.004 [−0.007, +0.015], whereas pCMI detects a
planted shared ±1 move at per-round rate q = 0.1 with AUROC 0.79 [0.70, 0.88]. At T = 20 (most sets) the
same planting gives only 0.62 [0.52, 0.71], so small co-movement is not excluded there. The only dependence
statistic above chance is lagged TE in the grid (0.62 [0.54, 0.70], declared secondary), still below level
(+0.12 [+0.01, +0.22]); exploratory follow-up suggests it sits in channel games whose agreement was *not*
executed (0.73 vs 0.49, post hoc). The one pCMI exception (base Qwen3.6, 0.71 [0.51, 0.88]) did not
replicate in the grid's Qwen cells.

![E70 grid](figures/fig3_e70_grid.png)
*Figure 3 (Q1.4 P2.14). Registered 16-cell grid (E70), per-cell channel effect and detector AUROCs (cell
estimates are descriptive).*

### 5.3 Public words add nothing — and can point the wrong way

![Say vs do](figures/fig4_say_vs_do_summary.png)
*Figure 4 (Q2.2). (a) Run AUROC of each auditor view and of the one-line pair-premium statistic, locked test (n = 95, run once) and fresh replication (n = 30). (b) Placebo stratum (15 matched seeds): flag rates when private messages are delivered vs offered but never delivered vs no channel.*

| where text could help | contrast | n | text view | action view |
|---|---|---|---|---|
| luna, base framing (locked test) | judge-labelled y = 1 vs 0 | 95 runs | 0.47 [0.36, 0.58] | 0.75 [0.65, 0.85] |
| Claude Sonnet (talks publicly) | private vs none | 10 | 0.22 [0.00, 0.52] | 0.52 [0.20, 0.88] |
| deepseek (talks publicly) | private vs none | 30 | 0.36 [0.20, 0.52] | 0.53 [0.30, 0.74] |
| Qwen3.8 base | private vs none | 15 + 15 | 0.21 [0.12, 0.33] | 0.86 [0.69, 0.98] |
| Qwen3.8 abliterated | private vs none | 15 + 15 | 0.15 [0.05, 0.25] | 0.57 [0.36, 0.78] |
| SALT-NLP negotiation (external; deal struck in chat) | executed vs not | 240 episodes | 0.87 [0.83, 0.91] | – |

*Table 2 (Q2.2 P2.0, `results/analysis/p2_say_vs_do.md`). AUROC < 0.5 = the view ranks controls higher.*

The registered contrast shows no resolved gain from adding public text: combined − better single view
−0.01 [−0.09, +0.06] (locked test, n = 95), −0.07 [−0.17, +0.02] on pooled fresh replications (n = 90,
pooling post hoc); gains above +0.06 / +0.02 are excluded at 95%. Text is *inverted* in families that
invite rivals publicly in every market: Qwen channel sellers, who can coordinate in private, invite rivals
publicly *less* (invite rate 0.40 vs 0.88 in controls; post hoc). Cross-applied to Q1.4's Qwen grid, where
prices alone are at chance (0.52 [0.41, 0.64]), adding text lowers AUROC (combined − action −0.24
[−0.37, −0.09]; −0.30 [−0.44, −0.17] on executed games). The exception is SALT, a bilateral negotiation
where the agreement *is* the conversation; even there, 62% of executed deals were never stated explicitly
(P(said | executed) = 0.385).

With privileged access to the private chat (E133, n = 78, exploratory), say–do consistency forecasts later
execution (AUROC 0.77) but adds nothing beyond early price stability (0.855); an LLM reading the early log
beats the best raw early-price rule (0.94 vs 0.885, Δ +0.06 [+0.02, +0.10], post hoc), with no evidence that
its edge comes from public messages.

### 5.4 Neither signal is specific to collusion

- **Prompt artefact.** In a six-arm study (15 matched seeds), a private *notes-to-self* pricing notepad with
  no recipient raises the pair premium +1.04 [+0.65, +1.42] vs +1.61 [+0.92, +2.35] for the real channel
  (ratio 0.65 [0.34, 1.32]); an offered-but-never-delivered placebo gives +1.23 [+0.76, +1.85]; delivery
  itself (private − placebo, +0.38 [−0.41, +1.18]) is unresolved. A terse paraphrase of the instructions
  shrinks the premium to +0.24 [−0.32, +0.81]. Figure 5 shows the earlier placebo stratum: delivered and
  undelivered channels track each other from round 1.
- **Tacit high prices.** With memory and profit framing, 19/20 *no-channel* gpt-6-luna markets price
  ≥ Nash + 2; 13/20 channel pairs keep their agreement, but the channel adds no detectable price, so channel
  labels stop being ground truth (Figure 6). Prompt wording alone moves no-channel markup from −0.19 to
  +2.56.
- **Legitimate asymmetry.** Scripted unequal costs: level screens false-flag 30/30. LLM cost/quality edges:
  premium flags 7/10 and 9/10 (controls 2/10).
- **Prevalence.** At 1% prevalence no frozen price flag reaches point-estimate precision 0.25 (Q1.4); the
  premium screen's precision is 0.24 at 5% prevalence (Q2.2).
- **Labels disagree.** Only 14/50 judge-labelled test agreements are kept under the follow rule.

![Placebo](figures/fig5_placebo_premium.png)
*Figure 5 (Q2.2, `llm_v3rep` seeds). Designated-pair premium per round: delivered channel (n = 15) vs offered-but-never-delivered placebo (n = 15) vs no channel (n = 10). The premium is present before any message is delivered (round 1) and the two channel arms are indistinguishable.*

![Strong framing](figures/fig6_strong_framing_tacit.png)
*Figure 6 (Q2.2 P2.7, `llm_p2strongF`, T = 40). Memory + profit framing: market-mean price − Nash by behaviour class; 19 tacit-high no-channel markets sit with the 13 executed channel pairs.*

### 5.5 Joint statement (verbatim in both source reports)

> "Detectability of LLM collusion by any price statistic is a property of the (seller model × prompt)
> pair. Relative screens survive a shared model but fail under market-wide spillover; absolute screens
> need model- and prompt-matched references." "With memory and a profit objective, gpt-6-luna sellers
> raise prices market-wide without any channel (19/20 no-channel markets ≥ Nash + 2); agreements are then
> often kept (13/20) but add no detectable price, so channel labels stop being ground truth. Abliterated
> Qwen with memory differs (channel adds +2.13 [1.28, 3.00]; 5/20 executed), as the first sentence
> predicts."

## 6. Discussion and implications

The two projects started from opposite bets — that collusion leaves a statistical fingerprint in actions,
and that it leaves a semantic one in words — and reached the same conclusion: in these markets, LLM
channel collusion is visible mainly as **how high** prices are, not in **how they move together** or in
**what is said publicly**. This is good news for cheap screening (a markup screen is simple and
interpretable) and bad news for attribution (a high level has many innocent causes: wording, model,
memory, legitimate cost advantages, market-wide tacit pricing).

A practical reading is a two-stage design: an always-on level screen against a **model- and
prompt-matched** reference as the first stage, with expensive audits (dependence statistics, private-log
review, provenance checks for shared seeds) only on flagged pairs. We have not evaluated this pipeline end
to end, and our evidence does not support recommending a particular architecture; it does support that a
flag is an audit trigger, not a verdict.

## 7. Limitations

- **Ground truth.** Labels come from one judge family (gpt-6.1-sol, also the auditor; Claude agrees
  115/115 on binary labels); execution labels are defined from prices, so level screens are partly scored
  on their own input on executed subsets.
- **Scope of the co-movement null.** At T = 20 small co-movement is not excluded; sensitivity is bounded
  only for the planted ±1 strategy. Below-chance pCMI in some sets is unexplained.
- **No evasion test.** Monitor-aware sellers stopped agreeing (0/10, 0/10) rather than hiding; no red-teamed
  or instructed colluder was run.
- **Small samples, many comparisons.** 10–21 games per arm in most LLM sets; per-set CIs are uncorrected;
  E70's per-cell estimates are descriptive; some contrasts (pooled replication, E133e, E72) are post hoc.
- **Narrow markets.** Four sellers, logit demand, short horizons; one external double auction (E68) is
  inconclusive (chat raises asks only +0.39 [+0.06, +0.69]); SALT is a different construct.
- **Placebo.** Q1.4's own market has no placebo arm; Q2.2's placebo cannot separate delivery from offer.

## 8. Future work

1. Instructed / red-teamed colluders (coded public signals, gradual drift) to test evasion.
2. Ground truth independent of prices and of the condition, judged by more than one model family.
3. A larger placebo study with simultaneous pre-play to isolate delivered coordination.
4. Mixed-family markets and provenance data for the shared-model / shared-seed confound.
5. End-to-end evaluation of the two-stage audit against legitimate partnerships and tacit markets.

## Reproducibility

Code, data and per-claim JSON live in the source repos (commits in [SOURCES.md](SOURCES.md)); each has a
reproduce section (Q1.4 REPORT §6; Q2.2 REPORT Appendix E, `verify_phase2.py`: 31/31 commands re-run
from cache with 0 LLM calls). Figures in `figures/` are copies of the source figures.

## References

- Agrawal et al. (2025). Evaluating LLM Agent Collusion in Double Auctions. arXiv:2507.01413.
- Banchio & Mantegazza (2023). Adaptive Algorithms and Collusion via Coupling. ACM EC '23. arXiv:2202.05946.
- Bonjour et al. (2022). Information-Theoretic Approach to Detect Collusion in Multi-Agent Games. UAI 2022, PMLR 180.
- Calvano, Calzolari, Denicolò & Pastorello (2020). Artificial Intelligence, Algorithmic Pricing, and Collusion. AER 110(10).
- Cao & Hu (2026). Supracompetitive Pricing Under AI Monoculture. arXiv:2601.01279.
- Dhanda (2026). A Price Cap Can Act as a Focal Point for LLM Pricing Agents. Preprint.
- Fish et al. (2024). Algorithmic Collusion by Large Language Models. arXiv:2404.00806.
- Green & Porter (1984). Noncooperative Collusion under Imperfect Price Information. Econometrica 52(1).
- Lin et al. (2024). Strategic Collusion of LLM Agents: Market Division in Multi-Commodity Competitions. arXiv:2410.00031.
- Mathew et al. (2024). Hidden in Plain Text: Steganographic Collusion in LLMs. arXiv:2410.03768.
- Motwani et al. (2024). Secret Collusion among AI Agents: Multi-Agent Deception via Steganography. NeurIPS 2024.
- Rose et al. (2026). Detecting Multi-Agent Collusion Through Multi-Agent Interpretability. arXiv:2604.01151.
- Schreiber (2000). Measuring Information Transfer. PRL 85(2).
- Tailor (2025). Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs. arXiv:2510.04303.

## Appendix — full tables

To be filled from the source claims tables (Q1.4 `results/eval/claims_denominators.md`, Q2.2
`results/analysis/claims_denominators.md`) and Q1.4's Phase-2-at-a-glance table.
