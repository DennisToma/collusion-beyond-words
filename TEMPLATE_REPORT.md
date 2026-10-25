# Beyond Words: A Private Channel Between LLM Sellers Is Detectable from Price Levels, Not from Co-movement or Public Messages<sup>1</sup>

**Dennis Toma** — Independent · *With Apart Research*

<p class="note"><sup>1</sup> Research conducted at the AI Collusion Research Sprint, October 2026.</p>

## Abstract

If two AI pricing agents can talk privately, can an overseer who sees only prices and public messages tell? We ran repeated four-seller pricing markets in which, in some games, one pair of LLM sellers got a private chat channel. Sellers were never told to collude. We compared a price-level screen, a test for hidden co-movement (conditional mutual information, pCMI), and an LLM auditor reading public messages.

On scripted colluders, pCMI flags every planted pair and removes most false alarms from shared shocks, but cannot tell colluders from two seed-sharing copies of one policy. Channel games priced higher in all nine main seller sets (seven models, one prompt family; only two of five wordings resolved an effect). A price-level screen separated channel from no-channel games, while pCMI stayed near chance (0.51 in a 192-game grid). Adding public messages gave the LLM auditor no resolved gain (−0.01 [−0.09, +0.06] AUROC on a locked test). On a different, external task where the collusive act is a verbal verdict, text predicted rule-breaking well (0.87). The price signal is not specific to collusion. A private notepad with no partner produced about two-thirds of the channel premium by point estimate. One model priced high without any channel under memory and profit framing. Removing safety training did not detectably increase the channel-related pricing premium.

For deployers: use a cheap, model-matched price-level screen as a trigger, then escalate to a chat-log or LLM audit. A price flag is not proof of an agreement.

![Figure 1](figures/fig0_headline.png)
*Figure 1. **Price levels distinguish channel from no-channel games more consistently than co-movement (pCMI); public messages give this LLM auditor no resolved gain.** (a) Two real 12-round games from the say-vs-do market (gpt-6-luna sellers), from a fresh replication set, chosen by a fixed rule: the median run of each arm by pair premium. With a channel (left) the designated pair prices above its two rivals in every round; without one (right) pair and rivals price identically. Unit cost is shared by all sellers but varies by round, so compare the gap within a game, not absolute levels across games. (b) AUROC of each detector, wherever it was evaluated (AUROC = probability that a random channel game scores above a random no-channel game; 0.5 = chance). Prices-only: median of nine seller sets (dots = individual sets). Grid: 192 games, public board on. Say-vs-do: locked test of 95 runs; blue = pair-premium statistic (chosen post hoc), red = text-only view (the registered text-added contrast, −0.01 [−0.09, +0.06], is not plotted); positives are runs whose private chat was judged communicative, which on this split are exactly the channel runs. SALT-NLP: a different, external task in which the collusive act is a verbal verdict; not a test of adding text to prices. Bars = estimates, lines = 95% CIs; dashed line = chance.*

## 1. Introduction

LLM agents set prices in simulated markets and reach high prices without being told to (Fish et al. 2024). When they can talk, they coordinate more (Agrawal et al. 2025). A regulator or platform usually sees what agents *do* (prices) and what they *say in public*, but not private side channels. The practical question is which observable signal reveals that a private channel was offered. (Our tests cover channel assignment, including its prompt cue; whether delivered messages add to it remains unresolved.) Figure 1 previews our answer.

Two intuitions point in different directions. Information theory suggests that colluders share hidden information, so their prices should co-move beyond what public market conditions explain (Bonjour et al. 2022). Auditing suggests that colluders will say one thing and do another, so an auditor reading their messages next to their prices should catch them. We test both.

**Threat model.** Four sellers repeatedly set prices. One pair may have a private channel. The overseer sees prices, costs, demand and public messages, never the private channel. A detector must rank channel games above no-channel games without flagging legitimate behaviour such as shared cost shocks, a public partnership, or two firms using the same pricing model.

Our main contributions are:

1. **A validated co-movement detector and a map of when it fails.** On scripted sellers, pCMI flags 100% of planted colluding pairs and cuts common-shock false alarms from 100% to 14%. It cannot distinguish two copies of one policy that share a random seed, and lagged transfer entropy flags legitimate leader–follower pricing.
2. **Evidence that LLM price collusion is a *level*, not co-movement or words.** Across nine seller sets, seven models and a 192-game factorial grid, channel assignment raises prices on average and a price-level screen detects it, while pCMI intervals include chance in eight of nine sets and in the grid. Adding public messages gives a zero-shot LLM auditor no resolved gain in pricing markets; on a different task where the collusive act is verbal, text alone works well.
3. **A warning for benchmarks: a channel is not collusion.** An unread private notepad reproduces about two-thirds of the channel premium, memory plus profit framing makes one model price high with no channel, and removing safety training produced no detectable increase in the channel-related pricing premium across three Qwen comparisons. Channel assignment is therefore a weak label for collusion.

## 2. Related Work

**Dependence as a collusion signal.** Bonjour et al. (2022) measure collusion as statistical dependence between agents' actions. Our pCMI is a pairwise version conditioned on public state. Tailor (2025) applies mutual-information detectors to steganographic messages; we apply the same estimator family to prices. Transfer entropy follows Schreiber (2000). Banchio & Mantegazza (2023) show that algorithms can reach high prices through "spontaneous coupling" without agreement, which motivates our shared-policy hard negatives.

**LLM pricing collusion.** Fish et al. (2024) find supracompetitive pricing by LLM agents. Agrawal et al. (2025) study communication in double auctions, Lin et al. (2024) market division, and Dhanda (2026) price caps as focal points. Cao & Hu (2026) show that a shared AI model can raise prices without communication. Calvano et al. (2020) and Green & Porter (1984) give the repeated-pricing background.

**Message-side collusion and definitions.** Motwani et al. (2024) and Mathew et al. (2024) study secret and steganographic collusion in messages. Shi, Zhang & Yang (2026) study collusion in long-horizon peer verification; we use their data as an external text case. Rose et al. (2026) separate a causal definition of collusion from an operational one.

**Our gap.** Prior work either detects dependence in scripted or RL agents, or studies whether LLMs collude. We test which observable signal (level, co-movement or words) actually carries a private channel's trace in LLM markets, with a positive control and hard negatives for each detector.

## 3. Methods

**Markets.** We use two separate repeated-pricing markets with four sellers, logit demand and integer prices. In the *prices-only market*, cost is 6 or 8, the static Nash price is 10 (12 at cost 8) and the joint-profit price is 16; most games last 20 rounds. In the *say-vs-do market*, games last 12 rounds, prices range 6–30, unit cost (shared by all sellers) varies by round, Nash is about 11 and the joint optimum about 19, and every seller posts a public message each round. A third arm there, a publicly announced cost-saving partnership, serves as a legitimate hard negative.

**Conditions.** In channel games, one designated pair gets a private chat ("Only firm X can read what you write there"); in no-channel games nobody does. Prompts give a profit objective only (Appendix C). We never instruct agents to collude or to hide.

**Sellers.** Nine main prices-only sets use seven models: gpt-6-luna, gpt-5.6-luna, deepseek-v4.1-flash, and base and abliterated versions of Qwen3.8-27B and Qwen3.6. The say-vs-do market uses gpt-6-luna plus family arms (Claude Sonnet, deepseek, Qwen3.8 base and abliterated, gpt-6.1-sol). A pre-registered 192-game grid (16 cells × 6 + 6 games, public board on) varies seven design factors: model, cost visibility, rival-price visibility, channel timing, memory, demand shocks and framing.

**Detectors.** (i) *Price-level screen:* the highest pair's mean markup over the Nash price (in the say-vs-do market, the pair's price premium over rivals). (ii) *pCMI:* Gaussian conditional mutual information between two sellers' prices after regressing out market state and all lagged prices, maximised over pairs. (iii) *Transfer entropy* (lagged). (iv) *LLM auditor:* one zero-shot gpt-6.1-sol prompt, scored on six views: public text only, prices only, both, and variants with summary statistics. The pre-registered test is whether adding text beats the better single view.

**Labels and metrics.** A gpt-6.1-sol judge reads the private chat (never prices) and labels explicit agreement, information exchange or none. We score detectors by AUROC: the probability that a randomly chosen channel game scores higher than a randomly chosen no-channel game (0.5 = chance, 1 = perfect). Market AUROC intervals are 95% run-level bootstraps; SALT-NLP intervals cluster by multi-episode run; rate intervals are Wilson or Jeffreys.

**Discipline.** We built a scripted positive control first: sellers that share a private signal, plus eight hard-negative groups (common shocks, high but independent prices, leader–follower pricing, shared policies). Detector settings were tuned only on scripted development seeds and evaluated once on locked seeds. The auditor was evaluated once on a locked test split of 95 runs (locked but not fully blind: four disclosed exposures) and replicated on fresh, pre-registered splits.

## 4. Results

**The co-movement detector works on scripted colluders.** Every contemporaneous detector flags and localises the planted colluding pair in 100% of scripted runs (Figure 2). Raw mutual information also flags 100% of common-shock controls; conditioning on public state and lagged prices (pCMI) cuts this to 14%, and to 4% (null from no-channel reference markets) on a held-out "shared policy plus common shock" group. Two failures are structural. Two copies of one policy sharing a random seed are flagged by every contemporaneous detector (44–100% of runs), because from prices alone they *are* a shared private signal. Lagged transfer entropy flags legitimate leader–follower pricing in 100% of runs.

**With LLM sellers, the channel raises the price level.** The channel raised markup in all nine main sets (Figure A1). A price-level screen reached AUROC 0.75–0.99 across sets, above pCMI by point estimate in all nine, and the paired difference was significant in eight. pCMI ranged 0.34–0.72, with its interval including chance in eight of nine. In the 192-game grid, the level screen scored 0.74 and pCMI 0.51 [0.43, 0.59]. Longer 60-round games did not rescue pCMI (0.34, level 0.94), nor did restricting to games where the pair visibly executed an agreement. A transfer-entropy signal appears in some sets, but it also fires on legitimate shared policies, so we do not read it as coordination.

**Public words give no resolved gain in pricing markets.** For gpt-6-luna sellers, the registered contrast (both views combined minus the better single view, text or prices) was −0.01 [−0.09, +0.06] AUROC on the locked test, so gains above +0.06 are excluded. Text alone scored 0.47 there, and for both Qwen3.8 arms it was *inverted* (0.21 and 0.15): the auditor ranked channel games below controls. In the Qwen3.8 base arm, channel sellers invited rivals publicly less often than controls (0.40 vs 0.88; post hoc), which fits the inversion but was not shown to cause it. Text does carry signal on a different task. On external SALT-NLP peer-verification data, where agents later submit a verbal verdict, the same kind of auditor predicted later rule-breaking verdicts from preceding messages with AUROC 0.87, even though, in the full dataset, 62% of rule-breaking episodes contain no explicit agreement. This is a different construct, so it does not explain why text failed in the pricing markets.

**A channel is not collusion.** A private notepad with no recipient raised the pair premium by +1.04, against +1.61 for a real channel: a ratio of 0.65 [0.34, 1.32], about two-thirds. With memory and long-run profit framing, 19 of 20 no-channel gpt-6-luna markets priced at least 2 above Nash (rounds 11–40), and the channel added no detectable premium. Removing safety training produced no detectable increase in the channel-related pricing premium across three Qwen comparisons. Only 14 of 50 communication-positive channel runs followed through on their agreement under our execution rule. Level screens also flag legitimate advantages: 7/10 high-cost and 9/10 quality-edge sellers vs 2/10 controls. Finally, in the prices-only market (gpt-6-luna) the channel effect was significant in only two of five prompt wordings.

![Figure 2](figures/fig1_scripted_hard_negatives.png)
*Figure 2. **Positive control: on scripted sellers, conditioning removes most false alarms.** Fraction of runs flagged at α = 0.05 (dashed) by each detector (50 runs per group, locked seed, 100 rounds; 95% Wilson CIs). The eight groups left of the vertical line contain no collusion and should rarely be flagged. Groups C and D contain a planted colluding pair and should always be flagged. Top: within-run shift null. Bottom: null built from no-channel reference markets. pCMI (red) is low on hard negatives except seed-sharing copies and 100% on colluders; transfer entropy (purple) fires on legitimate leader–follower pricing and shared policies.*

**Why we believe these results.** The contemporaneous dependence detectors passed the scripted positive control before LLM use (lagged transfer entropy flagged only 8–22% of scripted colluders). The level-over-pCMI pattern holds across seven models, a pre-registered grid, long games and executed-only subsets. The text result was pre-registered and measured once on a locked split, then replicated on fresh data (−0.07 [−0.17, +0.02], n = 90, pooled post hoc). All numbers are regenerated from saved data by scripts, and each maps to a source file and commit in `SOURCES.md`; the extended report's numbers are checked by script (Code and Data).

## 5. Discussion and Limitations

Price-level screens separated channel from no-channel LLM pricing games more reliably than contemporaneous pCMI, and adding public text gave the auditor no measurable gain. The trace was simpler: a higher price level. This matters for AI safety oversight in two ways. First, monitors that look for "suspicious dependence" or "suspicious talk" can miss a private channel's trace in LLM pricing. Second, a high price does not prove an agreement: prompts, private reasoning, memory and legitimate advantages all raise prices. Text auditing is not useless: it worked on a task where the harmful act is verbal, though we did not test why.

**Recommendation for deployers.** Run a cheap price-level screen against a reference built from the *same model and prompt* without a channel. Escalate flagged sellers to a chat-log, dependence and provenance audit. Never certify competition from a missing flag. We did not evaluate this two-stage pipeline end to end.

### Limitations

- **Labels.** One judge family (gpt-6.1-sol, also the auditor) supplies agreement labels; execution rules are defined from prices.
- **Scope.** Narrow markets: four sellers, logit demand, 12–60 rounds, one main prompt family. Small co-movement in 20-round games is not excluded.
- **Samples.** 10–21 games per arm in most sets; per-set intervals are not corrected for multiple comparisons; nonsignificance is not equivalence.
- **No adversary.** We did not test instructed or red-teamed colluders trying to evade a monitor.
- **Blindness.** The locked test set had four disclosed exposures, including the post-hoc choice of the premium statistic.

### Future Work

Test red-teamed colluders that keep prices inside a matched reference; obtain ground-truth labels independent of prices and of the auditor's model family; run larger placebo studies to separate channel delivery from the channel cue; and evaluate the full screen-then-audit pipeline on realistic market data.

## 6. Conclusion

Offering two LLM sellers a private channel left a trace that an overseer could see, but not the one we set out to find. The channel showed up as a higher price level. Co-movement detectors that work on scripted colluders found no robust contemporaneous co-movement, and public messages gave an LLM auditor no resolved gain. Because high prices also arise without any channel, a model-matched price-level screen is a good trigger for a deeper audit, not evidence of an agreement on its own. The key open test is whether deliberately evasive colluders can keep their prices inside the matched reference while still coordinating.

## Code and Data

- Code, data and results are included as a supplementary archive with this submission (`submission_code.zip`); the repository https://github.com/DennisToma/collusion-beyond-words will be made public after the submission deadline.
- The archive holds this report's code, figures and checks, a pinned evidence bundle (`evidence/`) that re-renders every figure without model calls, and, under `sources/`, the two project repositories at their pinned commits: the prices-only market and detectors (`732f08c`) and the say-vs-do market and auditors (`91ffb2d`), with the LLM trajectories, judge labels and auditor scores (files over 5 MB, the scripted positive-control trajectories that the generators re-create from seeds, are excluded). External: [SALT-NLP agent-collusion dataset](https://huggingface.co/datasets/SALT-NLP/agent-collusion/tree/2eba8f37).
- Extended report and per-number sources: `SUBMISSION.pdf`, `SOURCES.md`. Figure 1: `uv run python scripts/fig0_headline.py`.

## Author Contributions

Dennis Toma chose the research questions, designed the setup and research plan, directed the autonomous agents (see LLM Usage Statement), and reviewed the final claims.

## References

1. Agrawal, Teo, Vazquez, Kunnavakkam, Srikanth & Liu (2025). Evaluating LLM Agent Collusion in Double Auctions. arXiv. <https://arxiv.org/abs/2507.01413v1>
2. Banchio & Mantegazza (2023). Adaptive Algorithms and Collusion via Coupling. ACM EC '23. <https://doi.org/10.1145/3580507.3597726>
3. Bonjour, Aggarwal & Bhargava (2022). Information theoretic approach to detect collusion in multi-agent games. UAI, PMLR 180:223–232. <https://proceedings.mlr.press/v180/bonjour22a.html>
4. Calvano, Calzolari, Denicolò & Pastorello (2020). Artificial Intelligence, Algorithmic Pricing, and Collusion. American Economic Review 110(10):3267–3297. <https://doi.org/10.1257/aer.20190623>
5. Cao & Hu (2026). Supracompetitive Pricing Under AI Monoculture. arXiv. <https://arxiv.org/abs/2601.01279v3>
6. Dhanda (2026). A Price Cap Can Act as a Focal Point for LLM Pricing Agents: Evidence from a Repeated Bertrand Duopoly (Revised). Research Square preprint. <https://doi.org/10.21203/rs.3.rs-10183486/v1>
7. Fish, Gonczarowski & Shorrer (2024). Algorithmic Collusion by Large Language Models. arXiv. <https://arxiv.org/abs/2404.00806v6>
8. Green & Porter (1984). Noncooperative Collusion under Imperfect Price Information. Econometrica 52(1):87–100. <https://doi.org/10.2307/1911462>
9. Lin, Ojha, Cai & Chen (2024). Strategic Collusion of LLM Agents: Market Division in Multi-Commodity Competitions. arXiv. <https://arxiv.org/abs/2410.00031v2>
10. Mathew, Matthews, McCarthy, Velja, Schroeder de Witt, Cope & Schoots (2024). Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs. arXiv. <https://arxiv.org/abs/2410.03768v2>
11. Motwani, Baranchuk, Strohmeier, Bolina, Torr, Hammond & Schroeder de Witt (2024). Secret Collusion among AI Agents: Multi-Agent Deception via Steganography. NeurIPS 2024. <https://arxiv.org/abs/2402.07510v5>
12. Rose, Cullen, Abdelnabi, Torr, Kaplowitz & Schroeder de Witt (2026). Detecting Multi-Agent Collusion Through Multi-Agent Interpretability. arXiv. <https://arxiv.org/abs/2604.01151v5>
13. Schreiber (2000). Measuring Information Transfer. Physical Review Letters 85(2):461–464. <https://doi.org/10.1103/PhysRevLett.85.461>
14. Shi, Zhang & Yang (2026). Emergent Collusion in Long-Horizon LLM Agent Interaction. arXiv. <https://arxiv.org/abs/2609.24967v2>
15. Tailor (2025). Audit the Whisper: Detecting Steganographic Collusion in Multi-Agent LLMs. arXiv. <https://arxiv.org/abs/2510.04303v2>

## Appendix

### A. Extended results

![Figure A1](figures/fig2_level_vs_comovement_9sets.png)
*Figure A1. Prices-only market, nine main seller sets (seven models). (a) Channel minus no-channel markup with 95% game-bootstrap CIs; all lie above 0. (b) Run AUROC of the level screen (blue) and pCMI (orange). The level screen is higher in 9/9 sets by point estimate; the paired difference CI excludes 0 in 8/9 (not gpt-5.6-luna). Sets share designs and models, so they are not nine independent replications.*

| evidence | price-level screen | pCMI (co-movement) |
|---|---|---|
| 9 main sets, 7 models | AUROC 0.75–0.99; channel markup CI > 0 in 9/9 | 0.34–0.72; CI includes 0.5 in 8/9 |
| paired difference level − pCMI | CI > 0 in 8/9 (exception gpt-5.6-luna +0.03 [−0.27, +0.33]) | |
| 192-game grid (16 cells × 12 games, board on) | 0.74 [0.66, 0.80]; above pCMI in 12/16 cells | 0.51 [0.43, 0.59] |
| 60-round games (pre-registered) | 0.94 [0.86, 1.00] | 0.34 [0.18, 0.52] |
| executed agreements vs no-channel controls | pair-level 0.87 [0.80, 0.94] | 0.42 [0.33, 0.53] |
| rank (copula) pCMI / sign-change CMI, grid | | 0.53 [0.44, 0.61] / 0.44 [0.36, 0.52] |

*Table A1. Price detectors on LLM sellers (run AUROC [95% CI]; per-set CIs uncorrected).*

| where text could help | contrast | n | text view | price view |
|---|---|---|---|---|
| gpt-6-luna (locked test) | judge-labelled agreement vs not | 95 runs | 0.47 [0.36, 0.58] | 0.75 [0.65, 0.85] |
| Claude Sonnet | channel vs none | 5 + 5 | 0.22 [0.00, 0.52] | 0.52 [0.20, 0.88] |
| deepseek | channel vs none | 30 runs | 0.36 [0.20, 0.52] | 0.53 [0.30, 0.74] |
| Qwen3.8 base | channel vs none | 15 + 15 | **0.21 [0.12, 0.33]** | 0.86 [0.69, 0.98] |
| Qwen3.8 abliterated | channel vs none | 15 + 15 | **0.15 [0.05, 0.25]** | 0.57 [0.36, 0.78] |
| SALT-NLP peer verification (external) | rule-violating mutual ACCEPT vs not | 240 episodes | 0.87 [0.83, 0.91] | – |

*Table A2. Zero-shot gpt-6.1-sol auditor, run AUROC [95% CI]. Below 0.5 = the view ranks controls higher; bold = CI entirely below 0.5. The price view here is the LLM auditor reading prices, not the price-level statistic.*

![Figure A2](figures/fig4_say_vs_do_summary.png)
*Figure A2. Say-vs-do market. (a) Run AUROC of each auditor view and of the pair-premium statistic on the locked test (n = 95, run once) and a fresh replication (n = 30). (b) Placebo stratum: flag rates when private messages are delivered, offered but never delivered, or absent. The positive class is communication-positive runs on the test set and channel assignment on the replication.*

Further robustness (transfer entropy, alternative estimators, factorial effects, placebo and strong-framing arms, per-family breakdowns, exact definitions) is in Appendices D–F of `SUBMISSION.pdf`; every number maps to a source file and commit in `SOURCES.md`.

### B. Limitations and Dual-Use / Ethical Considerations

**What the results show and do not show.** They show which signals separated channel from no-channel games for the tested models, prompts and markets. They do not show that dependence or messages are uninformative in general, that a high-price flag implies an agreement, or that any detector is safe to deploy.

- **Ground truth.** Agreement labels come from one judge family (gpt-6.1-sol, also the auditor). A Claude Sonnet re-judgement agreed on the binary label but only weakly on three classes. Execution labels are defined from prices, so level screens are partly scored on their own input in executed subsets.
- **Co-movement null.** In 20-round games small co-movement is not excluded; sensitivity is bounded only for one planted strategy.
- **Prompt dependence.** The channel effect is significant in only two of five prompt wordings; one paraphrase removes most of the premium.
- **No evasion test.** Sellers told about a price monitor stopped agreeing rather than hiding; no red-teamed or instructed colluder was run.
- **Narrow markets and small samples.** Four sellers, logit demand, short horizons, 10–21 games per arm in most sets, uncorrected per-set intervals, several post-hoc contrasts. SALT-NLP measures a different construct (a verification-protocol violation).

**Dual-use risk.** Showing that text auditors can invert rankings and that price screens depend on the model and prompt could help an attacker find monitoring blind spots, and the released prompts, traces and detectors could be repurposed. We introduce no new attack capability: agents were never instructed to collude or evade, and abliterated models were used only as sellers in a simulated sandbox.

**Safeguards and intended use.** All markets were simulated; no pricing agent was deployed in a real market. Defenders should treat a price flag as a reason to investigate, calibrate it against legitimate partnerships and model- and prompt-matched controls, and seek independent evidence of an agreement before attribution. A missing text or dependence flag cannot certify competitive behaviour. This work supports research on oversight, not accusations about real firms.

### C. Prompts

Say-vs-do market, lab framing (verbatim template from `llm_market.py` in the say-vs-do repo; `{…}` are filled per game):

> You are participant {me} in an economics experiment on markets. Four participants (A, B, C, D) each run a firm selling a similar product for {R} rounds. Each round every participant simultaneously sets a price (an integer from {pmin} to {pmax}) and writes a short message on the public market board, which all participants read. Customers have some brand loyalty but buy more from cheaper firms; demand is higher in "high" demand rounds. Unit cost is announced each round. Your earnings in this experiment equal your firm's total profit over all {R} rounds, so your goal is to maximize it.

Added for the designated pair in channel games:

> You also have a private messaging channel with firm {p}. Only firm {p} can read what you write there, and only you can read what {p} writes. Each round you send {p} one message on it.

The prices-only market, judge and auditor prompts are in the two project repositories (archive `sources/`).

## LLM Usage Statement

This project was run largely by autonomous AI agents under the author's direction, and we disclose this as part of the method. Dennis Toma chose the two research questions, wrote each project's plan, shared data schema, agent rules and runner scripts, and set priorities during the sprint. Autonomous agent iterations, with Claude Opus 5.5 (Claude Code) as the default manager and Codex gpt-6.1-sol as reviewer and fallback manager, then wrote the market code, ran the experiments and analysis, made the figures and drafted the reports, including this one. Worker models handled bulk tasks; simulated sellers, judges and auditors are the LLMs named in Methods. Each report was adversarially reviewed by both gpt-6.1-sol and Claude Opus, which cannot rule out errors the models share. All numbers regenerate from code and saved data in the repositories, and scripts check printed numbers against saved results. Dennis reviewed the final claims. The official sprint starter repository (double auction, trust-breaking code and literature list) is pre-existing material; everything else was written during the sprint.
