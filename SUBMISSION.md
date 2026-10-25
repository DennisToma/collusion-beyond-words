# Beyond Words: Detecting AI-Agent Collusion Through Information Theory and Behavioral Evidence

**Dennis Toma** — Apart Research AI Collusion Sprint, 23–25 October 2026

*Merged submission of two sprint projects: Q1.4 (information-theoretic, prices-only detection) and Q2.2
(auditing what agents say together with what they do). Every number is taken from the frozen source repos
at the commits listed in [SOURCES.md](SOURCES.md), which maps each number to its JSON file and key.*

## Abstract

We put LLM sellers in four-seller repeated pricing markets, offer one pair a private chat channel (never
telling them to collude), and ask whether an auditor can tell — from prices, from public messages, or from
both. In short:

- **Being offered a private channel shows up as a higher price level.** Markup over the Nash price rose in
  all 9 of Q1.4's main sets (7 seller models; per-set CIs, uncorrected), and a simple max-pair markup screen
  had a higher point-estimate AUROC than a conditional-dependence detector in all 9 (0.75–0.99 vs 0.34–0.72; paired difference 95% CI > 0 in 8/9).
- **We find no robust contemporaneous co-movement.** (One base-Qwen3.6 set separates, 0.71 [0.51, 0.88], uncorrected; not replicated in the grid.) The dependence detector (pCMI), which flags and localises every
  pair in the scripted shared-signal positive control, is at chance in a 192-game seven-factor grid (0.51 [0.43, 0.59]), in
  pre-registered 60-round games (0.34 [0.18, 0.52]) and on agreements whose prices were kept ("executed", 48/149; 0.42 [0.33, 0.53]).
  Lagged dependence (transfer entropy) is weakly above chance in the grid but below level (§5.2).
- **A zero-shot LLM auditor shows no resolved gain from public messages.** Adding them to prices changes AUROC by
  −0.01 [−0.09, +0.06] (locked test, n = 95) and −0.07 [−0.17, +0.02] (fresh replications, post hoc
  pooling). In Qwen families that invite rivals publicly, the text view is *inverted* (AUROC 0.15–0.21,
  CI below 0.5). (Text did work on an external negotiation dataset where the detected act happens in the chat; §5.3.)
- **Neither signal is specific to collusion.** An unread private pricing notepad produces about two thirds
  of the channel's premium over rounds 2–12 (point ratio 0.65, CI [0.34, 1.32]); with memory and profit framing, 19/20
  gpt-6-luna markets *without* a channel price ≥ Nash + 2 (rounds 11–40); level screens also flag legitimate cost asymmetry.

Price-level screens could therefore serve as a cheap first-stage audit trigger (not evaluated end to end) whose reference must be matched to the
seller model and prompt — not evidence of an agreement.

*Glossary.* **AUROC**: probability that a random positive example scores above a random negative one, ties counting
half; the positive class (usually channel assignment) is stated per analysis (0.5 = chance; < 0.5 = inverted). **Level / max-pair markup**: the highest pair's mean price above the per-round Nash
price. **pCMI**: max-pair Gaussian conditional mutual information of prices given public state and all
sellers' lagged prices. **TE**: transfer entropy (lagged dependence). **Executed**: the judge found a private agreement *and* the pair's prices then followed it (Q1.4 rule, §3).
**Nash + 2**: a price at least 2 above the competitive (Nash) price. **C − A**: channel minus no-channel
arm. **E*nn* / P2.*n***: experiment / section IDs in the source repos (SOURCES.md).

## 1. Introduction

Algorithmic pricing agents built on LLMs reach supracompetitive prices without instruction (Fish et al.
2024) and change behaviour when they can communicate (Agrawal et al. 2025). An overseer will mostly see two
things: the agents' *actions* (prices) and what they *say* in public. Two detection strategies follow:

1. **Information theory on actions** (Q1.4). Colluders should share information beyond what public state
   explains, so their prices should be conditionally dependent (Bonjour et al. 2022). Such a detector is
   blind to message content: it does not inspect wording directly (resistance to strategic evasion was not tested).
2. **Say + do auditing** (Q2.2). An LLM auditor reading both public messages and prices should catch
   inconsistencies between what agents say and what they do, and beat single-stream auditors.

We test both on LLM pricing markets, cross-apply each project's detectors to the other's data, and keep
three label levels apart: *assigned opportunity* (channel offered), *verified agreement* (a judge reads the
private chat) and *realised coordination* (prices follow the agreement).

**Contributions.**
- A prices-only conditional-dependence detector (pCMI, with shift and same-model surrogate nulls) that
  passes a scripted positive control and a hard-negative battery (common shocks, shared policies,
  legitimate leader–follower pricing), plus a map of what it cannot separate (policy copies sharing a seed).
- Evidence across 9 main LLM sets, a 192-game factorial grid and a pre-registered long-game test that
  channel assignment shows up as a **price level**, with no detected contemporaneous co-movement.
- A registered say-vs-do comparison showing that public text gives a zero-shot auditor no resolved gain
  and can be **inverted**.
- Confound analyses (prompt artefacts, placebo, tacit high prices, cost asymmetry, prevalence) showing why
  a price flag is an audit trigger, not proof.


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

**Markets.** Two separate four-seller repeated price markets with multinomial-logit demand and integer prices; cost
and demand state are generally public, but Q1.4's E70 grid varies cost visibility and rival-price visibility. They are not one shared market; numbers are tagged with their project.
- *Q1.4 market* (`sim/market.py`): cost 6/8, static Nash price 10 (cost 8: 12), joint-profit optimum 16;
  T = 20 in most LLM sets (40–60 in long-game sets). The public message board is **off** by default; it is
  on only in the E70 grid and the E59 board arm.
- *Q2.2 market* (`llm_market.py`): 12 rounds (40 in the strong-framing arm), prices 6–30, static Nash ≈ 11,
  joint monopoly ≈ 19; arms `private` (pair has a channel), `none`, and `legit` (publicly announced
  cost-saving partnership, hard negative). A public board exists in every arm.

Cross-application: Q1.4 scored Q2.2's `llm_v3` market; Q2.2 audited all 192 games of Q1.4's E70 grid (E113).
The "words" results therefore rest on Q2.2's markets plus E70, not on Q1.4's nine main sets.

**LLM sellers.** Q1.4's nine main sets use seven seller models: gpt-6-luna (main), gpt-5.6-luna,
deepseek-v4.1-flash, and base and abliterated (refusal-removed) Qwen3.8-27B and Qwen3.6. Q2.2's main market
uses gpt-6-luna and adds family arms (Claude Sonnet, deepseek, Qwen3.8 base/abliterated, gpt-6.1-sol,
mimo). Profit-maximisation / economics-lab framing after Fish et al. (2024).

**Labels.** A gpt-6.1-sol judge reads only the private chat (never prices) → explicit agreement /
information exchange / none. Claude Sonnet 5.5 re-judged Q2.2's 115 chats and gave the same binary label in
115/115, but each dataset was single-class, the 3-class κ was only 0.33–0.38, and a second check (E84d)
agreed on agreed-yes/no in 25/30. Q1.4's judge labels have no cross-family check.

| term | rule | used for |
|---|---|---|
| executed (Q1.4) | judge-labelled agreement AND both pair firms ≥ agreed − 1 in ≥ ½ of post-agreement rounds AND second-half pair mean ≥ Nash + 2 | 48/149 executed games; E70 executed subsets. 27 variants give 13–78/149 (E71) |
| strict-executed (Q2.2) | registered strict rule for the strong-framing arm (E99-amend): judged agreement with floor F ≥ 13; ≥ 10 later rounds; both firms price ≥ F − 1 in ≥ ½ of those rounds; post-agreement pair mean excess over Nash ≥ 2 | 13/20 channel pairs (10–16/20 under one-at-a-time threshold changes) |
| kept / followed (Q2.2) | E84 follow rule on the locked test | 14/50 communication-positive runs |
| tacit-high (Q2.2) | strong-framing no-channel market whose mean price minus cost-adjusted Nash over rounds 11–40 is ≥ 2 (a price threshold, not verified coordination) | 19/20 strong-framing markets |

**Splits and discipline.** Q1.4 detector settings were tuned only on scripted dev seeds and evaluated once
on locked seeds; no setting was tuned on LLM data. Q2.2's auditors are zero-shot with one prompt per view,
evaluated once on a locked test split (runs 0030–0124, n = 95) — locked but not fully blind (four disclosed
exposures, including the post-hoc choice of the premium statistic) — and replicated on fresh,
pre-registered splits. Most Phase 2 experiments were declared before their data; post-hoc analyses are
labelled.

## 4. Methods

**Price detectors (Q1.4, prices only).** Per pair: |Pearson|, plug-in MI, CMI given public state, and
**pCMI** = −½ log(1 − ρ²) of residuals after regressing each seller's price on state dummies and all four
lagged prices; transfer entropy (TE, lagged, max over directions). Two nulls: a circular-shift null
(B = 200, relative offsets ≥ 3 rounds), and a **same-model surrogate null** ranking the run's max-pair
score against no-channel games of the same model and shock family. Level screens: *max-pair markup* over
the per-round Nash price and *pair_level* (pair mean minus rivals). An independent reimplementation agreed
on 422/424 run × statistic cells to < 1e-9 on the v1 datasets.

**Auditors (Q2.2).** One zero-shot gpt-6.1-sol auditor, same task text, six views: `text` (public messages
+ public facts), `action` (prices, costs, demand, profit), `action_stats` (+ computed pair-statistics
table), `combined` (text ∪ action), `combined_stats`, `structured`. Registered primary contrast:
Δ_hybrid = AUROC(combined) − max(AUROC(text), AUROC(action)), on communication labels (positive = explicit agreement or information exchange; on the locked test all 50
private runs are judged y = 1 — 48 explicit, 2 information exchange — so judge and channel labels coincide there).

**Statistics.** Run-level AUROC with class-stratified game bootstrap 95% CIs; Wilson intervals for flag
rates; Jeffreys for precision. CIs are per-set and uncorrected for multiplicity unless stated.

## 5. Results

### 5.1 On scripted sellers, conditioning works (positive control; Q1.4)

![Scripted hard negatives](figures/fig1_scripted_hard_negatives.png)
*Figure 1 (Q1.4 §4.1, locked seed 1001, 50 runs per group). Run-level flag rates at α = 0.05.*

Every contemporaneous detector flags and localises the planted pair in 100% of runs. Raw MI flags 100%
of common-shock controls; conditioning on public state and lagged prices (pCMI) cuts this to 14% under the
shift null and, for the held-out *shared policy + common shock* hard negative, 4% [1, 13] under the
same-model surrogate null. Two failure modes are structural: two copies of one policy sharing a random
seed are flagged by every contemporaneous detector (44–100%) — from price data they *are* a private shared
signal — and lagged TE flags legitimate public leader–follower pricing in 100% of runs and shared policies
in 90–98%, while finding the contemporaneous colluder in only 22%. Level screens fail elsewhere: unequal
private costs are false-flagged in 30/30 scripted markets (pCMI 4/30; locked seed 2003).

### 5.2 With LLM sellers, the channel shows up as a price level; no co-movement is detected (Q1.4)

![Level vs co-movement](figures/fig2_level_vs_comovement_9sets.png)
*Figure 2 (Q1.4 P2.13). Nine main sets, seven seller models: channel − no-channel markup and run AUROC
with game-bootstrap 95% CIs. Scores target channel assignment, not execution.*

| evidence | max-pair markup (level) | pCMI (co-movement) | source |
|---|---|---|---|
| 9 main sets, 7 models | AUROC 0.75–0.99 (point est. > pCMI in 9/9); C − A CI > 0 in 9/9 | 0.34–0.72; CI ∋ 0.5 in 8/9 | N1–N4 |
| paired Δ level − pCMI | CI > 0 in 8/9 (exception gpt-5.6-luna +0.03 [−0.27, +0.33]) | | N3 |
| E70 grid: 16-cell fractional factorial over 7 factors, 6 + 6 games per cell (192), board on | 0.74 [0.66, 0.81]; level > pCMI in 12/16 cells (point est.) | 0.51 [0.43, 0.59] | N8 |
| E44 long games, T = 60 (pre-registered) | 0.94 [0.86, 1.00] | 0.34 [0.18, 0.52] | N5 |
| executed channel games vs no-channel controls (48 executed of 149 labelled channel games, Q1.4 rule) | max-pair 0.99 (inflated by construction); pair-level 0.87 [0.80, 0.94] (not inflated) | 0.42 [0.33, 0.53] | N7 |
| rank (copula) pCMI / sign-change CMI, E70 | | 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52] | N11 |

*Table 1. Per-set CIs uncorrected. E74's paired differences were declared, but declaration and results
first appear in the same commit, so their order is not independently established.*

Neither rank-based nor discrete estimators detect co-movement that linear pCMI missed (both at chance,
though sign-CMI has little power in E70's sparse state strata). At T = 60 the observed co-move excess is
+0.004 [−0.007, +0.015], whereas pCMI detects a planted shared ±1 move at per-round rate q = 0.1 with
AUROC 0.79 [0.70, 0.88] — this is injection-specific sensitivity, not a general power bound. At T = 20 (most sets, all
of E70) the same planting gives only 0.62 [0.52, 0.71], so small co-movement is not excluded there, and the
check bounds sensitivity only to that planting. The one pCMI exception (base Qwen3.6, 0.71 [0.51, 0.88]) did
not replicate in the grid's Qwen cells.

*Lagged dependence is not excluded.* TE is weakly above chance in the grid (0.62 [0.54, 0.70], declared
secondary) and clearly above chance in some main sets (deepseek 0.81 [0.62, 0.96]; base Qwen3.8 0.91);
level beats TE (CI > 0) in 6/9 main sets and in the grid (+0.12 [+0.01, +0.22]). Because TE also fires on
shared policies in scripted markets, and in the grid its signal sits in channel games that did *not* meet the
execution rule (0.73, n = 52: 38 with a judged agreement, 14 without) rather than executed ones (0.49, n = 44;
post hoc, difference untested), we do not read it as evidence of coordination.

**Robustness to prompt wording is limited.** Across five wordings (6 + 6 games each, gpt-6-luna), the
channel effect C − A has CI > 0 in only 2/5, and no-channel markup ranges from −0.19 to +2.56 (P2.7). "9/9"
holds for the main sets under one prompt family.

![E70 grid](figures/fig3_e70_grid.png)
*Figure 3 (Q1.4 P2.14). Registered 16-cell grid (E70), per-cell channel effect and detector AUROCs (cell
estimates are descriptive).*

### 5.3 A zero-shot auditor shows no resolved gain from public words — and can read them the wrong way (Q2.2)

![Say vs do](figures/fig4_say_vs_do_summary.png)
*Figure 4 (Q2.2). (a) Run AUROC of each auditor view and of the one-line pair-premium statistic (chosen post
hoc after v1), locked test (n = 95, run once) and the first fresh replication (`llm_v3rep`, n = 30; the
pooled n = 90 contrast quoted in the text is not plotted). (b) Placebo stratum (15 matched seeds): flag
rates when private messages are delivered vs offered but never delivered vs no channel. The positive class
is communication-positive runs on the test set and channel assignment on the replication, not verified
coordination (figure regenerated by `scripts/fig4_say_vs_do.py` from Q2.2 JSON).*

| where text could help | contrast | n | text view | action view |
|---|---|---|---|---|
| luna, base framing (locked test) | judge-labelled y = 1 vs 0 | 95 runs | 0.47 [0.36, 0.58] | 0.75 [0.65, 0.85] |
| Claude Sonnet (talks publicly) | private vs none | 5 + 5 | 0.22 [0.00, 0.52] | 0.52 [0.20, 0.88] |
| deepseek (talks publicly) | private vs none | 30 runs | 0.36 [0.20, 0.52] | 0.53 [0.30, 0.74] |
| Qwen3.8 base | private vs none | 15 + 15 | **0.21 [0.12, 0.33]** | 0.86 [0.69, 0.98] |
| Qwen3.8 abliterated | private vs none | 15 + 15 | **0.15 [0.05, 0.25]** | 0.57 [0.36, 0.78] |
| SALT-NLP negotiation (external; act happens in chat) | rule-violating mutual ACCEPT vs not | 240 episodes | 0.87 [0.83, 0.91] | – |

*Table 2 (Q2.2 P2.0, `results/analysis/p2_say_vs_do.md`). AUROC < 0.5 = the view ranks controls higher;
bold = CI entirely below 0.5.*

The registered contrast shows no resolved gain from adding public text: combined − better single view
−0.01 [−0.09, +0.06] (locked test, n = 95), −0.07 [−0.17, +0.02] on pooled fresh replications (n = 90,
pooling post hoc); gains above +0.06 / +0.02 are excluded at 95%.

*Inversion.* An AUROC of 0.15 means the text carries information with the wrong sign for a zero-shot
auditor, not that words are uninformative. Among the families in Table 2, the inversion is resolved only for the two Qwen3.8 arms (post hoc, not interpreted in the Q2.2 report: a gpt-6.1-sol seller arm
with 0/7 private agreements also scores 0.17 [0.01, 0.41], 7 + 7 markets, so inversion need not involve an agreement). There,
channel sellers, who can coordinate in private, invite rivals publicly *less* (invite rate 0.40 vs 0.88 in
controls, Qwen3.8 base; post hoc); for deepseek and Claude invite rates do not differ and the mechanism is
not established.

*Cross-application to Q1.4's grid (E113, 192 games).* In the 8 Qwen cells the LLM auditor reading prices is
at chance (0.52 [0.41, 0.64]) — although Q1.4's markup statistic on the same games is not (0.76) — text is
inverted (0.32 [0.24, 0.42]), and adding text lowers AUROC (combined − action −0.24 [−0.37, −0.09]; −0.30
[−0.44, −0.17] on games executed under Q1.4's rule). In the luna cells combined − action is
+0.07 [−0.02, +0.17] overall and +0.16 [+0.05, +0.28] on executed games (registered secondary), but a
similar +0.12 [−0.08, +0.32] appears in the 3 luna cells with no public posts (post hoc), so the luna gain
cannot be credited to text. In these markets public text resolvedly hurt the auditor (Qwen); no gain could be
credited to text (the luna executed-game gain also appears in cells without public posts).

*External case (different construct).* In SALT-NLP bilateral negotiations, "executed" means a mutual ACCEPT
that violates a verification rule — an act inside the conversation, not a pricing deal. There a text auditor
reaches 0.87 [0.83, 0.91] (240 sampled episodes, 120 executed), even though 62% of executed episodes carry no
explicit agreement (P(said | executed) = 0.385). It shows that text can work when the act is in the talk; it
does not show that this is the only such condition.

*Forecasting execution (E133, exploratory, n = 78 agreed games from Q1.4's grid, 48 held / 30 not under
Q2.2's late-window rule).* With privileged access to the private chat, say–do consistency forecasts which
agreements are held (AUROC 0.77), but three hand-built say–do features in one logistic model add nothing
beyond early price stability (0.855); richer text features are untested. An LLM reading the
early public log *without* the private chat beats the best raw rule score (0.94 vs 0.885, Δ +0.06 [+0.02, +0.10], post hoc) — a compliance rule
that uses early prices *and* the privately judged agreed price — with no evidence that its edge comes from
public messages. This is the third analysis of the same 78 games; the rule score was fixed after E133c/d
were seen, the LLM prompt states the label rule, and the same model (gpt-6.1-sol) is Q1.4's label judge and
extracted the agreed price.

### 5.4 Neither signal is specific to collusion

- **Prompt artefact (Q2.2).** In a six-arm study (15 matched seeds), a private *notes-to-self* pricing
  notepad with no recipient raises the pair premium +1.04 [+0.65, +1.42] vs +1.61 [+0.92, +2.35] for the
  real channel (ratio 0.65 [0.34, 1.32]; the registered rule that the notepad is *not* the driver failed); an
  offered-but-never-delivered placebo gives +1.23 [+0.76, +1.85]; delivery itself (private − placebo, +0.38
  [−0.41, +1.18]) is unresolved. Two paraphrases of the instructions (10 + 10 runs each) give +1.79
  [+1.20, +2.43] and +0.24 [−0.32, +0.81]. Figure 5 shows the earlier placebo stratum: delivered and
  undelivered channels track each other from round 1. What the level screens detect is channel *assignment
  including its prompt cue*, not shown to be delivered coordination.
- **Tacit high prices (Q2.2; gpt-6-luna).** With memory and profit framing, 19/20 *no-channel* markets
  price ≥ Nash + 2; 13/20 channel pairs strict-execute, but the channel adds no detectable price, so channel
  labels stop being ground truth (Figure 6). This is model-specific: abliterated Qwen with memory (Q1.4 E65)
  is tacit-high in 0/20.
- **Prompt wording (Q1.4).** Wording alone moves no-channel markup from −0.19 to +2.56 (§5.2).
- **Legitimate asymmetry.** Scripted unequal costs: level screens false-flag 30/30 (Q1.4). LLM cost/quality
  edges: premium flags 7/10 and 9/10 vs controls 2/10 (Q2.2).
- **Prevalence.** At a hypothetical 1% prevalence none of the frozen, tested price flags reaches
  point-estimate precision 0.25 (Q1.4; maximum 0.20 [0.07, 0.54] on scripted MI/pCMI rows, ≤ 0.19 on LLM sets; this largely follows from α = 0.05; this is
  not a bound on achievable precision); the premium screen's
  point precision is 0.24 at 5% prevalence (Q2.2).
- **Labels disagree (Q2.2).** Only 14/50 communication-positive private test runs meet the E84 follow rule.

![Placebo](figures/fig5_placebo_premium.png)
*Figure 5 (Q2.2, `llm_v3rep` seeds). Designated-pair premium per round: delivered channel (n = 15) vs
offered-but-never-delivered placebo (n = 15) vs no channel (n = 10). The premium is present before any
message is delivered (round 1); placebo − private over rounds 2–12 is +0.03 [−0.54, +0.49] (no resolved
difference, not equivalence).*

![Strong framing](figures/fig6_strong_framing_tacit.png)
*Figure 6 (Q2.2 P2.7, `llm_p2strongF`, T = 40). Memory + profit framing: market-mean price − Nash by
behaviour class; 19 tacit-high no-channel markets sit with the 13 strict-executed channel pairs.*

## 6. Discussion and implications

The two projects started from opposite bets — that collusion leaves a statistical fingerprint in actions,
and that it leaves a semantic one in words — and converged: in these markets, channel assignment is visible
mainly as **how high** prices are, not in detected **contemporaneous co-movement** (lagged TE is weakly above chance), and a zero-shot auditor shows no
resolved gain from **what is said publicly** (small gains are not excluded). This is good news for cheap screening (a markup screen is simple and
interpretable) and bad news for attribution: a high level has many innocent causes (wording, model, memory,
legitimate cost advantages, market-wide tacit pricing), and private pricing deliberation can raise levels without delivered messages (Q2.2's logbook control
suggests merely singling out a pair is insufficient, subject to instruction-length and batch-timing confounds).

Both projects state jointly that **detectability of LLM collusion by any price statistic is a property of
the (seller model × prompt) pair**: relative screens (pair vs rivals) survive a shared model but lose power
under market-wide spillover (in Q1.4's spillover sets pair_level 0.75–0.80 vs market level 0.85–0.94), and
absolute screens need model- and prompt-matched references. With memory and a profit objective gpt-6-luna
sellers raise prices market-wide without any channel (19/20; Q2.2 arm, re-scored by Q1.4 as E66), so
channel labels stop being ground truth; abliterated Qwen with memory differs (channel adds +2.13 [1.28,
3.00]; 5/20 executed under Q1.4's rule; Q1.4 E65, T = 40). The joint statement is a post-hoc synthesis, not
a tested prediction.

A practical reading is a two-stage design: an always-on level screen against a **model- and
prompt-matched** reference as the first stage, with expensive audits (private-log review, dependence
statistics, provenance checks for shared models and seeds) only on flagged pairs. We have not evaluated this
pipeline end to end, and our evidence does not support recommending a particular architecture; it does
support that a flag is an audit trigger, not a verdict.

## 7. Limitations

- **Ground truth.** Agreement labels come from one judge family (gpt-6.1-sol, also the auditor); the
  cross-family check is weak (above). Execution labels are defined from prices, so level screens are partly
  scored on their own input on executed subsets.
- **Scope of the co-movement null.** At T = 20 small co-movement is not excluded; sensitivity is bounded
  only for the planted ±1 strategy. Below-chance pCMI in some sets is unexplained.
- **Prompt dependence.** The channel effect is resolved in only 2/5 Q1.4 wordings; one Q2.2 paraphrase
  removes most of the premium.
- **No evasion test.** Monitor-aware sellers stopped agreeing (0/10, 0/10) rather than hiding; no red-teamed
  or instructed colluder was run.
- **Small samples, many comparisons.** 10–21 games per arm in most LLM sets; per-set CIs are uncorrected;
  E70's per-cell estimates are descriptive; several contrasts (pooled replication, E133e, E72, E113 luna
  split) are post hoc or secondary.
- **Narrow markets.** Four sellers, logit demand, short horizons; one external double auction (E68) is
  inconclusive (chat raises asks only +0.39 [+0.06, +0.69]); SALT is a different construct.
- **Placebo.** Q1.4's own market has no placebo arm; Q2.2's placebo leaves delivery unresolved (private − placebo +0.38 [−0.41, +1.18]).

## 8. Future work

1. Instructed / red-teamed colluders (coded public signals, gradual drift) to test evasion.
2. Ground truth independent of prices and of the condition, judged by more than one model family.
3. A larger placebo study with simultaneous pre-play to isolate delivered coordination.
4. Mixed-family markets and provenance data for the shared-model / shared-seed confound.
5. End-to-end evaluation of the two-stage audit against legitimate partnerships and tacit markets.

## Reproducibility

Code, data and per-claim JSON live in the source repos (commits in [SOURCES.md](SOURCES.md)); each has a
reproduce section (Q1.4 REPORT §6; Q2.2 REPORT Appendix E, `verify_phase2.py`: 31/31 commands re-run
from cache with 0 LLM calls; it excludes sealed evaluations, E113/E115 data and SALT raw data). Figures in `figures/` are copies of the source figures. `SUBMISSION.pdf` and `SLIDES.pdf` are built by
`uv run --group export python scripts/export_pdf.py`.

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

### A. Q1.4 Phase 2 at a glance (verbatim from Q1.4 REPORT.md @ `0e06c03`; paths relative to Q1.4 `results/`)

[95% CI]: Wilson for k/n flag rates, Jeffreys for precision, class-stratified game bootstrap for AUROCs and
markup differences. "Precision 0.25" in the shared row is a point-estimate threshold (maximum 0.20).

| gap | question | key numbers | source (`results/…`) | § |
|---|---|---|---|---|
| shared | precision at realistic prevalence | at 1% prevalence no frozen flag reaches precision 0.25 (Jeffreys intervals for TPR/FPR) | `eval/prevalence.json` | P2.1 |
| shared | independent reimplementation | 422/424 run × statistic cells agree < 1e-9 (2 differ only in the ρ² cap); all 20 AUROCs identical; shift-null flags 4/21 vs 5/21 (Monte Carlo); no bug | `reimpl/compare.json` | P2.2 |
| 1 | prompt wording (5 wordings, 6 + 6 each) | channel C − A +0.69 (SE 0.17), Q p = 0.69; no-channel baseline −0.19 … +2.56; within-wording markup AUROC 0.66 [0.53, 0.78]; pCMI 0.44 [0.30, 0.58] | `eval/p2_variants.json` | P2.7 |
| 2 | long games (E44: T=60, 20 + 20, pre-registered) | **level, not short**: pCMI AUROC 0.34 [0.18, 0.52] at T=60 (0.52 at T=20); market level 0.94 [0.86, 1.00]; observed co-move excess +0.004 [−0.007, +0.015] < q = 0.1 planting (+0.13, pCMI 0.79); pair premium +0.70 → +0.23: rivals stay elevated while no-channel markets fall (spillover +2.24 of +2.47, rounds 51–60); executed 4/20, tacit 0/20 | `eval/long_power_llm_long_p2_T60.json`, `eval/spillover_llm_long_p2_T60.json` | P2.8 |
| 3 | same-model confound | mismatched reference: pCMI 52% false flags at α = 0.10 (exploratory; fresh matched pool 3/21); model-matched fresh pool at α = 0.05: pCMI 2/21 [3, 29]% false flags, markup and pair_level 0/21 [0, 16]%, but markup power 1/16 (prompt mismatch) | `eval/same_model.json`, `eval/matched_ref.json` | P2.3 |
| 4 | second seller family (deepseek, 15 + 15) | channel C − A +3.75 [2.77, 4.68] (luna +1.76; interaction +1.99 [0.90, 3.07]); AUROC markup 0.99, pair_level 1.00, pCMI 0.57 [0.36, 0.77]; rule HOLDS; judge: 15/15 agreements, 3/15 followed; public board alone (E59) +0.70 [0.23, 1.23], level screen false-flags 5/15 | `eval/p2_family.json` | P2.9 |
| 5 | coalition structure (scripted) | all-4 cartel: pair_level AUROC 0.26, 0.25 (A, B; 1/30, 0/30 flagged); markup, pCMI, TC 30/30 | `p2/coalition_test.json` | P2.4 |
| 6 | onset (scripted) | level CUSUM 0/30 false alarms, 30/30 detected, median delay 7–7.5 rounds; repeated-look pCMI 5/30 = 17% [7, 34] false | `p2/onset_test.json` | P2.4 |
| 7 | market model (N = 2/4/6, μ) | pooled pCMI control false flags 18/300 = 6.0% [3.8, 9.3]; 9/10 cells pass; s = 0.6 power 30/30 everywhere | `p2/market_test.json` | P2.5 |
| 8 | private cost asymmetry (hard negative) | pair_level and markup 30/30 false; pCMI 4/30 [5, 30]% (controls 1/30) | `p2/costasym_test.json` | P2.4 |
| 9 | bid rotation (exploration) | predictable rotation: pCMI 6/30, 2/30 (controls 5/30, 4/30); TE 13/30, 17/30; levels 30/30 | `p2/rotation_test.json` | P2.6 |
| extra | sibling's six channel arms | undelivered notepad (0/14 agreements): pair_level names the pair 11/15, AUROC vs none 0.89 [0.76, 0.98], as private 12/15, 0.91 | `eval/p2cue_ext.json` | P2.10 |
| D2 | external double auction (E68, qwen-3.6-35b, 15 + 15) | **inconclusive**: chat ask effect +0.39 [+0.06, +0.69] (≈2% of surplus); level AUROC 0.68 [0.46, 0.88], pCMI 0.60 [0.40, 0.80]; paid prices +2.61 vs +2.01; 18 parse failures in 14/30 runs | `eval/e68_cda.json` | P2.12 |
| C | executed collusion, abliteration, model generations, memory (E61–E67) | executed 48/149 C games over ten sets (E44 T=60: 4/20 [0.07, 0.41]); tacit-high (no channel) 1/144 under our framing for current models, but 9/10 for older gpt-5.6-luna and 19/20 under Q2.2's strong framing (E66) (markup AUROC falls to 0.75); abliterated − base (C − A): no detectable increase in 3/3 Qwen pairs (E61 −0.37 [−2.09, 1.36], E69 −0.65 [−1.97, 0.65], Q2.2, pair premium not C − A, −1.24 [−2.41, −0.03]); executed-only pooled pCMI 0.42 [0.33, 0.53] vs 0.52 non-executed (market_level on that subset is inflated by construction, 0.99; pair_level is not, 0.87 [0.80, 0.94]); E69 base Qwen3.6 is the one set with pCMI CI > 0.5 (0.71 [0.51, 0.88]; market level 0.93); E65 memory arm (T=40): markup 0.85, pCMI 0.49, declared executed-only pCMI test inconclusive (0.33 [0.02, 0.66], 5/20 executed; the pilot's 5/5 did not replicate); E66 (Q2.2 strong framing, gpt-6-luna, T=40): executed 13/20 but tacit 19/20 without a channel, so channel vs no-channel is 0.46 on pCMI and 0.44 on market level (nothing separates; declared test not evaluable); E67 stickiness screen: 1 of 3 confirmatory sets (E65 0.90; gpt-5.6-luna 0.46, E66 0.42), so the stickiness explanation of low pCMI is not supported; glm-5.2 dropped | `eval/p2_partc.json` | P2.11 |
| E1 | generality over 7 design factors (E70, 2^(7−3) grid, 16 cells × 6 + 6, registered) | channel C − A positive in 13 / 0 / 3 cells (pos / tie / neg; one-sided sign p = 0.011), pooled +0.98 [0.65, 1.29]; level > pCMI 12 / 1 / 3; pooled AUROC level 0.74 [0.66, 0.81], pCMI 0.51 [0.43, 0.59], TE 0.62 [0.54, 0.70] (declared secondary: confirmed); qwen pCMI exception not replicated 0.46 [0.35, 0.58]; largest main effects M (= model incl. ≈100% vs 4–10% public-board use) +0.79 [0.10, 1.44], cost +0.79 [0.12, 1.41] (descriptive); follow-up on M not confirmed: +1.07 [−0.20, +2.41] (12 + 12 per level) | `eval/e70_grid.json` | P2.14 |

### B. Q2.2 claims × denominators (verbatim from Q2.2 `results/analysis/claims_denominators.md` @ `8b680ee`, generated by `p2_claims.py`)

| id | claim | value (abstract text) | status | denominator / registration | source : key path |
|---|---|---|---|---|---|
| C01 | combined minus better single view, run-AUROC, locked test | -0.01 [-0.09, +0.06] | OK | n=95 runs (llm_v3 locked test split of 125 runs); registered primary contrast | `results/analysis/final_llm_v3_gpt-6.1-sol_test.json` : `contrasts['delta_hybrid[combined]:run_auroc']{delta,ci}; n_runs` |
| C02 | same contrast, two fresh replications pooled | -0.07 [-0.17, +0.02] | OK | n=90 runs (30 llm_v3rep + 60 llm_p2rep, label = channel condition); post hoc pooling of two registered splits | `results/analysis/p2_pool_rep.json` : `condition_label.contrasts['delta_hybrid[combined]']{delta,ci}; n; n_by_ds` |
| C03 | gains above +0.06 (test) / +0.02 (pooled) excluded at 95% (upper CI limits) | +0.06 / +0.02 | OK | upper 95% CI limit of C01 (n=95) and C02 (n=90); pooled is post hoc | `results/analysis/final_llm_v3_gpt-6.1-sol_test.json + results/analysis/p2_pool_rep.json` : `contrasts[...run_auroc].ci[1]; condition_label.contrasts['delta_hybrid[combined]'].ci[1]` |
| C04 | a computed pair-statistics table added to the action view gains on test (action_stats minus action) | +0.11 [+0.04, +0.18] | OK | n=95 runs, locked test; registered contrast family (delta_hybrid[action_stats] = action_stats - max(text, action)), not the primary endpoint. Corrected 2026-10-24 16:40: the abstract previously quoted structured (+0.08) | `results/analysis/final_llm_v3_gpt-6.1-sol_test.json` : `contrasts['action_stats-action:run_auroc']{delta,ci}` |
| C04b | adding text to the pair-statistics view does not gain (combined_stats minus action_stats) | -0.06 [-0.14, +0.01] | OK | n=95 runs, locked test; registered contrast family | `results/analysis/final_llm_v3_gpt-6.1-sol_test.json` : `contrasts['combined_stats-action_stats:run_auroc']{delta,ci}` |
| C04c | same pair-statistics gain on fresh data (action_stats minus better single view), two replications pooled | +0.00 [-0.06, +0.07] | OK | n=90 runs (30 llm_v3rep + 60 llm_p2rep, label = channel condition); post hoc pooling; added 2026-10-24 17:57 (iter26 review: test gain did not replicate) | `results/analysis/p2_pool_rep.json` : `condition_label.contrasts['delta_hybrid[action_stats]']{delta,ci}` |
| C05 | pair price premium AUROC, fresh replication | 0.94 [0.87, 0.99] | OK | n=60 runs (llm_p2rep: 30 private / 20 none / 10 legit); premium selected post hoc after v1; replication registered | `results/analysis/replication_llm_p2rep.json` : `point_ci.premium.run_auroc; n_runs; group_n` |
| C06 | unread pricing notepad premium as share of channel premium (rounds 2-12) | 65% (1.04/1.61) | OK | n=15 seeds per arm (llm_p2cue: notes vs none, private vs none, paired by seed); gpt-6-luna; registered arms, ratio is derived | `results/analysis/p2_cue_llm_p2cue.json` : `paired['notes-none'].prem_r2_12[0] / paired['private-none'].prem_r2_12[0]; n` |
| C07 | legitimate cost / quality edges flagged by premium vs controls | 7/10, 9/10 vs 2/10 | OK | 10 runs per condition (highcost, quality, plus 10 no-channel reference runs from llm_p2cue); gpt-6-luna; frozen dev threshold 0.667 | `results/analysis/p2_asym.json` : `conditions.{highcost,quality,none_ref_p2cue}.premium_flags` |
| C08 | text views flag every control (no-channel) market for Claude, deepseek, Qwen base+abliterated | 100% (5/5, 15/15, 15/15, 15/15) | OK | control (condition=none) markets: Claude 5, deepseek 15, Qwen-base 15, Qwen-abliterated 15; text view; families differ by model so cross-family comparison is associative; registered predictions (E95) for Claude/deepseek | `results/analysis/p2_family3way.json + results/analysis/p2_strong_eval_llm_p2qwena.json + results/analysis/p2_strong_eval_llm_p2qwenb.json` : `llm_p2{claude,ds}.views.text.flags_by_class.PUB; llm_p2qwen{a,b}.detectors.text.flags.none` |
| C09 | text-view run AUROC range across those control-flagging families (private vs none) | 0.15-0.36 | OK | run AUROC private vs none, text view: Claude n=10, deepseek n=30, Qwen-base n=30, Qwen-abl n=30 runs; TL;DR claim (not in abstract text) | `results/analysis/p2_family3way.json + results/analysis/p2_strong_eval_llm_p2qwen{a,b}.json` : `views.text.auroc_private_vs_none[0] (min,max over 4)` |
| C10 | SALT-NLP episodes | 8000 | OK | episodes = 7998 with valid judge label + 2 invalid-judge episodes; 800 runs; external data (SALT-NLP) | `results/analysis/salt_d1.json` : `E104_sayvsdo.n_episodes + n_invalid_judge; crosstab sum` |
| C11 | SALT distinct models | 10 | OK | distinct model names parsed from per_condition ids (main__X and cross_model__A__B); 16 conditions x 500 episodes | `results/analysis/salt_d1.json` : `E104_sayvsdo.per_condition[*].condition (parsed)` |
| C12 | share of executed SALT episodes with no explicit agreement (1 - P(said\|exec)) | 62% (P(said\|exec)=0.385) | OK | executed episodes n=5169 (1989 said + 3180 not said), 7998 judged; Qwen judge label for 'said'; episodes are clustered in 800 runs (check CI method in salt script) | `results/analysis/salt_d1.json` : `E104_sayvsdo.P_said_given_exec.est; crosstab.exec1_*` |
| C13 | test 'colluders' that keep their agreement | 14/50 | OK | n=50 judged-agreement private runs among the 95 llm_v3 test runs (14 followed + 36 not followed); behaviour labels registered (E84) | `results/analysis/p2_behaviour.json` : `datasets.llm_v3.class_counts.{followed,not_followed}; n` |
| C14 | strict-executed channel pairs (memory + profit objective) | 13/20 | OK | 20 channel markets (llm_p2strongF, seeds 9800000-9800019); strict rule fixed in registered amendment E99-amend; Jeffreys [0.43, 0.83] | `results/analysis/p2_strong_classes_llm_p2strongF.json` : `n_strict_executed` |
| C15 | no-channel markets that price >= Nash + 2 (tacit-high) | 19/20 | OK | 20 no-channel markets (paired seeds with C14); tacit-high rate >= 0.5 registered (E99amend); Jeffreys [0.79, 0.99] | `results/analysis/p2_strong_classes_llm_p2strongF.json` : `n_tacit_high_none` |
| C16 | paired excess private - none (market price over cost-adjusted Nash) | -0.44 [-1.84, +1.00] | OK | n=20 paired seeds; registered prediction E99_P3 (excess > 0) FAILED; unresolved | `results/analysis/p2_strongF_report_llm_p2strongF.json` : `E99_P3.paired_excess_private_minus_none; n_pairs` |
| C17 | private-plan LLM monitor AUROC, strict-executed vs tacit-high | 0.76 [0.55, 0.93] | OK | 13 strict-executed vs 19 tacit-high markets; EXPLORATORY (E103 plan view registered before plan calls, but classes defined post hoc); CI [0.55, 0.93] | `results/analysis/p2_strong_eval_llm_p2strongF.json` : `detectors.plan.auroc_strict_vs_tacit_high (== keyword file detectors.plan_view...); groups_n` |
| C18 | no-LLM count of plans naming the chat partner, same contrast | 0.82 [0.66, 0.96] | OK | 13 vs 19 markets; EXPLORATORY post hoc keyword detector (E111) K_dir; CI [0.66, 0.96] | `results/analysis/p2_plan_keyword_llm_p2strongF.json` : `detectors.K_dir.auroc_strict_vs_tacit_high; n_pos_strict; n_neg_tacit_high` |
| C19 | no plan uses agreement words | 0/13 strict, 0/19 tacit-high | OK | 13 strict + 19 tacit-high (+7 non-executed) markets; keyword K_terms; exploratory | `results/analysis/p2_plan_keyword_llm_p2strongF.json` : `runs_with_term_in_any_plan` |
| C20 | public-text view AUROC, strict-executed vs tacit-high (inverted) | 0.25 [0.08, 0.46] | OK | 13 vs 19 markets; EXPLORATORY (E99-x, added after generation began, before detector scores); CI [0.08, 0.46] | `results/analysis/p2_strong_eval_llm_p2strongF.json` : `detectors.text.auroc_strict_vs_tacit_high` |
| C21 | abliterated vs base Qwen: executed markets each arm; agreement at ceiling | 13/15; 13/15 | OK | 15 vs 15 private markets (llm_p2qwena vs llm_p2qwenb); execution diff 0.00 [-0.26, +0.26] Newcombe; agreement 15/15 both; registered (C3), predictions not supported | `results/analysis/p2_qwen_cmp.json` : `P2_executed_rate.abliterated; P2_executed_rate.base; P1_agreement_rate` |
| C22 | SALT-NLP: gpt-6.1-sol text auditor AUROC for execution | 0.87 [0.83, 0.91] | OK | n=240 sampled SALT episodes (120 executed; 79 tacit) audited by gpt-6.1-sol (E105); external data | `results/analysis/salt_d1.json` : `E105_audit.auroc{est,ci}; n; n_exec` |
| C21b | abliterated vs base Qwen: Q2.2 strict-executed each arm (lower-bound compliance) | 5/15; 5/15 | OK | 15 private markets per model; Q2.2 strict: F>=12, both pair prices>=F-1 in >=50% of later rounds, >=10 later rounds, post-agreement pair excess>=2; p2_strong.py via p2_strong_eval.py, not a +/-1 band or Q1.4 E70 rule | `results/analysis/p2_strong_classes_llm_p2qwena.json` : `n_strict_executed (qwena; qwenb)` |
| C23 | abliterated minus base Qwen: paired channel premium difference | -1.24 [-2.41, -0.03] | OK | 15 vs 15 private markets with matched none; bootstrap; registered P3 (abliterated >= base) not supported; bf16 vs FP8 serving confound | `results/analysis/p2_qwen_cmp.json` : `P3_paired_premium.diff_boot95` |
| C24 | E116 within channel: plan view AUROC strict-executed vs non-executed | 0.69 [0.44, 0.91] | OK | 13 strict vs 7 non-executed private markets (llm_p2strongF); exploratory, zero LLM calls, seed bootstrap | `results/analysis/p2_within_agree_llm_p2strongF.json` : `views.plan.auroc_strict_vs_nonexec` |
| C27 | E116b within agreement, Qwen abliterated / base: public text AUROC strict vs non-executed | 0.73 [0.43, 0.99]; 0.51 [0.25, 0.70] | OK | 5 strict vs 10 non-executed private markets per model (llm_p2qwena, llm_p2qwenb; 15/15 judged agreement each); exploratory, not pooled | `results/analysis/p2_within_agree_llm_p2qwen{a,b}.json` : `views.text.auroc_strict_vs_nonexec` |
| C25 | E112 participant replacement (luna newcomer), private arm: market excess replaced - original; re-agreement replaced; originals | +0.20 [-0.08, +0.62]; 16/20; 15/20 | OK | 20 paired private games replayed from llm_p2strongF, newcomer from round 21, rounds 21-40; registered E112, all 4 predictions held; none arm +0.16 [-0.27, +0.57] in P2.15 | `results/analysis/p2_replace.json` : `arms.private.O1_market_repl_minus_orig; arms.private.O4_reagreement_floor_ge13.{repl,orig}` |
| C28 | E115 participant replacement (gpt-6.1-sol newcomer), private arm: re-agreement replaced; markets >= Nash + 2 replaced | 0/20; 18/20 | OK | same 20 paired private games as E112, sol newcomer from round 21; registered E115, S1 failed, S2-S4 held; none arm 9/10 in P2.15 | `results/analysis/p2_replace_sol.json` : `arms.private.O4_reagreement_floor_ge13.repl; arms.private.O6_market_excess_ge2.repl` |
| C29 | E120 definition sensitivity (P2.7 body): strict-executed one-at-a-time range; full grid; tacit-high range | 10-16/20; 7-18/20; 17-20/20 | OK | llm_p2strongF, frozen judge terms, 81 threshold combinations; exploratory, zero LLM calls; registered 13/20 reproduced | `results/analysis/p2_strict_sensitivity.json` : `strict_range_one_at_a_time; strict_range_all; tacit_high[].k` |
| C30 | E112/E115 post-replacement executed counts under registered replacement O5 (not Q2.2 strict) | 15/20; 14/20; 0/20; 14/20 | OK | 20 paired private games per replacement arm; O5: judged post-r20 agreement F>=13, both pair prices>=F-1 in >=50% of later rounds, >=5 later rounds, post-agreement pair excess>=2; same rule for originals; REPORT P2.7/P2.15 | `results/analysis/p2_replace.json; results/analysis/p2_replace_sol.json` : `arms.private.O5_executed_after_r21.{repl,orig}` |
| C31 | E113 Qwen cell-stratified combined minus action / text AUROC | -0.24 [-0.37, -0.09]; -0.05 [-0.13, +0.03] | OK | 8 Qwen cells x 6 matched seeds x 2 arms = 96 games of Q1.4 E70's 192; channel assignment label; equal-cell mean of within-cell AUROC differences; game bootstrap within cell x arm, B=2000 seed=0; E113-amend3 registered before scores; shared Q1.4 data, not independent joint replication | `results/analysis/p2_e1_audit.json` : `amend3.qwen_stratified_combined_minus_{action,text}.{delta,ci,n_cells}` |
| C32 | E113 combined-minus-best-single cell signs: Qwen positive/tie/negative; all cells positive/tie/negative | 0/8; 0; 8; 4/16; 1; 11 | OK | 8 Qwen cells and all 16 Q1.4 E70 cells, 6 games per arm per cell; best-single max selection biases delta downward; ties count toward registered P1, so held P1 is weak confirmation | `results/analysis/p2_e1_audit.json` : `amend3.{qwen,all}_sign_counts; b_cells_combined_gt_best_single; b_P1_held` |
| C33 | E113 Qwen text inversion and flags in channel / no-channel arms | 0.32 [0.24, 0.42]; 48/48; 48/48 | OK | 96 games in 8 Qwen E70 cells (48 channel, 48 no-channel); unstratified pooled text AUROC and frozen dev threshold flags; game-bootstrap CI, not an independent replication of Q1.4 data | `results/analysis/p2_e1_audit.json` : `pooled_auroc_channel_vs_none_descriptive.text_qwen; a_text_flag_rate_by_arm_qwen.{1,0}` |
| C34 | E133e no-chat LLM minus best raw early-price rule score; oriented say-do gap and pair SD AUROC | +0.06 [+0.02, +0.10]; 0.77; 0.855 | OK | 78 Q1.4 E70 grid agreed games (48 held / 30 not); post hoc robustness declared before computing (E133e-reg); paired game bootstrap; 0 LLM calls | `results/analysis/e133e_attr.json` : `b_llm_E133d_minus_raw.rule_score; a_oriented_auroc_smaller_is_held.{say_do_gap,pair_sd_0_5}[0]` |
