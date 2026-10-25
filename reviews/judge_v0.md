# Judge review v0 — presentation and clarity (SUBMISSION.md, SLIDES.md, figures/)

Reviewer stance: an Apart judge with about 10 minutes. Numbers were not re-checked (six prior reviews did that).
No number is changed below, and no claim is widened or narrowed. Where a hedge moves, the destination is given.

**Overall.** The science reads as careful and honest, and the execution signal (positive control, hard
negatives, locked splits, pre-registration, cross-application) is strong. The main risk is presentation. A judge
will not find a one-sentence takeaway in the first screen. The abstract is four dense bullets with about 15
parentheticals and five terms used before they are defined (Nash, pCMI, executed, locked test, C − A). The
AI-safety relevance is implicit: §6 reads as competition economics. Figures 1 and 3 do not stand alone. Fixing
items 1–5 probably matters more than everything else together.

---

## P1 — fix before submission

### 1. Add a one-sentence takeaway in the first 5 lines (SUBMISSION.md, between line 3 and line 5)
**Problem.** Lines 1–7 contain the title, author and provenance note. The finding only starts at line 15, inside a
bullet. The title ("Beyond Words") hints that words fail but does not say what works.
**Insert after line 3:**
```markdown
> **TL;DR.** In our LLM pricing markets, offering two sellers a private chat channel shows up to an auditor
> mainly as *higher prices*. We detect no contemporaneous price co-movement, and reading public messages gives
> a zero-shot LLM auditor no resolved gain (for some models it is inverted). High prices also arise without any
> channel (prompt cues, memory, cost advantages), so in these markets a price flag is a reason to audit, not
> evidence of an agreement.
```
(Every clause here restates an existing abstract bullet with its hedge: "detect", "no resolved", "in our markets".)

### 2. Make the abstract readable: define terms inline, use numbered findings with bold headlines, and put shared caveats in one lead-in (lines 11–31)
**Problem.** Uncorrected-CI caveats repeat per bullet. "pCMI", "Nash", "executed" and "locked test" appear before the
glossary (line 33). Bullet 2 opens with a parenthetical exception before its main claim. Every hedge is kept below.
Only their order changes, plus one shared caveat line.
**Replace lines 11–31 with:**
```markdown
We put LLM sellers in four-seller repeated pricing markets, offer one pair a private chat channel (never
telling them to collude), and ask whether an auditor can tell which markets had the channel — from prices,
from public messages, or from both. AUROC is the auditor's ranking accuracy (0.5 = chance, < 0.5 = inverted);
per-set 95% CIs are uncorrected for multiplicity.

1. **The channel shows up as a higher price level.** Mean markup over the competitive (Nash) price was higher
   with the channel in all 9 main sets of the prices-only project (Q1.4; 7 seller models). A simple screen on
   the highest pair's markup had a higher point-estimate AUROC than a conditional-dependence detector (pCMI) in
   all 9 (0.75–0.99 vs 0.34–0.72; paired-difference CI > 0 in 8/9).
2. **We find no robust contemporaneous co-movement.** pCMI flags and localises every pair in a scripted
   shared-signal positive control. With LLM sellers it is at chance (all three CIs include 0.5) in a 192-game
   seven-factor grid (0.51 [0.43, 0.59]), in pre-registered 60-round games (0.34 [0.18, 0.52]) and on
   agreements whose prices were kept ("executed", 48/149; 0.42 [0.33, 0.53]). One base-Qwen3.6 set separates
   (0.71 [0.51, 0.88]) but did not replicate in the grid. Lagged dependence (transfer entropy) is weakly above
   chance in the grid but below the level screen (§5.2).
3. **Public messages give a zero-shot LLM auditor no resolved gain** (say-vs-do project, Q2.2). Adding them to
   prices changes AUROC by −0.01 [−0.09, +0.06] (locked test split, n = 95) and −0.07 [−0.17, +0.02] (fresh
   replications, pooled post hoc). In both Qwen families, whose sellers invite rivals publicly, the text-only
   view is *inverted* (Qwen3.8 arms 0.15–0.21; Qwen3.6 grid cells 0.32 [0.24, 0.42]; CIs below 0.5). Text did
   work on an external negotiation dataset where the detected act happens in the chat (§5.3).
4. **Neither signal is specific to collusion.** An unread private pricing notepad produces about two thirds of
   the channel's premium over rounds 2–12 (point ratio 0.65, CI [0.34, 1.32]). With memory and profit framing,
   19/20 gpt-6-luna markets *without* a channel price ≥ Nash + 2 (rounds 11–40). Level screens also flag
   legitimate cost asymmetry.

**Implication.** Price-level screens could serve as a cheap first-stage audit trigger (not evaluated end to end).
Their reference must be matched to the seller model and prompt, and a flag is not evidence of an agreement.
```
Hedges preserved: uncorrected per-set CIs, point-estimate vs paired CI 8/9, the Qwen3.6 exception and its
non-replication (moved after the main claim, still in the bullet), "all three CIs include 0.5", TE weakly above
chance, post hoc pooling, the SALT construct difference, the CI on 0.65, rounds 11–40, and "not evaluated end to end".

### 3. State the AI-safety implication explicitly (new paragraph at the end of §1, after line 54, plus one sentence in §6)
**Problem.** Nothing says why an AI-safety judge should care beyond antitrust. Apart's criterion (1) is scored
from this. The relevant safety point is that two natural *oversight* strategies were weak in these settings:
monitoring agents' public text, and statistical dependence tests on their actions. That is currently implicit.
**Insert after line 54:**
```markdown
**Why this matters for AI safety.** As LLM agents act for competing parties, overseers will often see only
their actions and their public messages, not private side channels. We test two natural monitoring strategies
on exactly those signals: a statistical detector of hidden coordination in actions, and an LLM monitor that
reads what agents say. In these markets neither recovered the side channel better than a crude outcome
statistic. The text monitor could be *misled* (inverted AUROC), and the outcome statistic also fired without
any channel. Sellers were never instructed to collude or to evade (§7), so these are results about naturally
arising behaviour in narrow markets, not about adversarial colluders.
```
**And in §6, append to the paragraph ending "…not a verdict." (line 308):**
```markdown
For multi-agent oversight more broadly, the same lesson applies within the tested settings: monitors of
agents' public text and dependence tests on their actions both need validation against matched no-collusion
references before a flag is read as coordination.
```

### 4. Explain "Q1.4 / Q2.2" once, then use readable names (line 5; section headings §5.1–5.4)
**Problem.** To an outsider, "Q1.4" and "Q2.2" are opaque codes, and the reader has to hold them in mind through
the whole paper. Line 5 explains the content but not that these are the sprint's open-question numbers.
**Replace lines 5–7 with:**
```markdown
*Merged submission of two sprint projects, named after the sprint's open-question numbers:* **Q1.4, the
prices-only project** (information-theoretic detection from prices alone), and **Q2.2, the say-vs-do project**
(auditing what agents say together with what they do). The two use separate markets, and each result is tagged
with its source project. Every number is taken from the frozen source repos at the commits listed in
[SOURCES.md](SOURCES.md), which maps each number to its JSON file and key.
```
**And change the headings:** "(Q1.4)" → "(prices-only, Q1.4)" in §5.1/§5.2 and "(Q2.2)" → "(say-vs-do, Q2.2)" in §5.3.
In body text, replace bare "luna" with "gpt-6-luna" (lines 232–234, Table 2 row 1).

### 5. Make Figure 1's caption stand alone (line 145)
**Problem.** The figure has 10 groups × 5 detectors × 2 nulls. The caption gives only the seed and α, so a judge
cannot tell which bars should be high.
**Replace line 145 with:**
```markdown
*Figure 1 (prices-only, Q1.4 §4.1; scripted sellers, locked seed 1001, T = 100, 50 runs per group; Wilson 95%
CIs). Fraction of runs each detector flags at α = 0.05 (dashed line). The eight groups left of the vertical line
contain **no** collusion and should be flagged rarely: independent sellers, common shocks, legitimate
leader–follower pricing and shared policies. The two groups on the right (C, D) contain a planted colluding pair
and should be flagged always. Top row: within-run circular-shift null. Bottom row: surrogate null built from
no-channel reference markets. Red (pCMI) is low on the hard negatives except shared-seed copies, and 100% on
collusion. Purple (lagged TE) fires on leader–follower and shared policies.*
```
Also add one in-text pointer in §5.1, line 147: "Every contemporaneous detector (Figure 1, right panels) flags…".

---

## P2 — clear improvements

### 6. Glossary: move it above the abstract bullets' first use, and add the missing aliases (lines 33–38)
**Problem.** The figures say "market-level markup" (Fig. 2/3 legends), the text says "max-pair markup", and the
appendix says "market level". These are the same statistic (Q1.4 `market_level`), but nothing says so. "C − A" does
not explain A. "Pair premium" (Q2.2) is never defined. "Locked test" is undefined at first use.
If item 2 is adopted, keep the glossary where it is (the abstract becomes self-contained). Either way, **replace lines 33–38 with:**
```markdown
*Glossary.* **AUROC**: probability that a random positive example scores above a random negative one, ties
counting half; the positive class (usually channel assignment) is stated per analysis (0.5 = chance; < 0.5 =
inverted). **Nash price**: the static competitive price; **Nash + 2**: at least 2 price units above it.
**Level / max-pair markup** (called "market-level markup" or `market_level` in figures and the appendix): the
highest pair's mean price above the per-round Nash price. **pair_level** (Q1.4) / **pair premium** (Q2.2): the
assigned pair's mean price minus the other two sellers' mean. **C − A**: difference in mean all-seller markup
over Nash, channel arm (C) minus no-channel arm (A) (Q1.4; Q2.2 contrasts use the pair premium). **pCMI**:
max-pair Gaussian conditional mutual information of prices given public state and all sellers' lagged prices
(contemporaneous co-movement not explained by public information). **TE**: transfer entropy (lagged
dependence). **Executed**: the judge found a private agreement *and* the pair's prices then followed it (Q1.4
rule, §3). **Locked test**: a split frozen before any tuning and scored once. **E*nn* / P2.*n* / N*n***:
experiment / section / claim IDs in the source repos and SOURCES.md.
```

### 7. Figure 2 caption: add the "point estimate" hedge that the panel title omits, and the legend alias (lines 159–160)
**Problem.** Panel (b) is titled "Level beats pCMI: 9/9 sets". The text carefully says "point estimate; paired CI > 0 in
8/9". A judge looking only at the figure gets the stronger reading.
**Replace lines 159–160 with:**
```markdown
*Figure 2 (prices-only, Q1.4 P2.13). Nine main sets, seven seller models. (a) Channel − no-channel markup (C − A)
with game-bootstrap 95% CIs; all lie above 0. (b) Run AUROC for the level screen ("market-level markup" =
max-pair markup, blue) and pCMI (orange); dashed line = chance. "9/9" in panel (b) is by point estimate; the paired
difference CI excludes 0 in 8/9 (not gpt-5.6-luna). Scores target channel assignment, not execution. Sets share
designs and models, so they are not nine independent replications.*
```

### 8. Figure 3 caption: explain cells, factors and the axis (lines 194–195), and reference it in the text
**Problem.** "c01…c15", the factor arrows and "C − A" are unexplained. The figure is placed after a paragraph that
does not mention it.
**Replace lines 194–195 with:**
```markdown
*Figure 3 (prices-only, Q1.4 P2.14). Registered 16-cell fractional-factorial grid (E70) over seven design
factors, 6 channel + 6 no-channel games per cell, public board on. (a) Main effect of switching each factor from
its low to its high level on the channel effect C − A, with 95% CIs (descriptive). (b) Per-cell run AUROC of the
level screen ("market-level markup", blue) and pCMI (orange). Cells are ordered by their C − A, printed under each
cell id. Level is above pCMI in 12/16 cells; pCMI scatters around chance. Cell estimates are descriptive.*
```
In the table row for E70 (line 166), append "(Figure 3)".

### 9. Split the "Inversion" paragraph (lines 223–227): one 110-word sentence holds four nested asides
**Problem.** The core claim (Qwen3.8 inversion, invite-rate mechanism, hedged) is hard to find. All hedges are kept below.
**Replace lines 223–227 with:**
```markdown
*Inversion.* An AUROC of 0.15 means the text carries information with the wrong sign for a zero-shot auditor,
not that words are uninformative. Among the families in Table 2, the inversion is resolved only for the two
Qwen3.8 arms. There, channel sellers, who can coordinate in private, invite rivals publicly *less* (invite rate
0.40 vs 0.88 in controls, Qwen3.8 base; post hoc). This is consistent with the inversion but not shown to cause
it: within the Qwen3.8-base no-channel arm, text score vs invite rate gives Spearman −0.41 [−0.83, +0.18].
For deepseek and Claude, invite rates do not differ.

Inversion need not involve an agreement: a gpt-6.1-sol seller arm with 0/7 private agreements also scores 0.17
[0.01, 0.41] (7 + 7 markets; post hoc, not interpreted in the Q2.2 report).
```

### 10. Move E133 (lines 243–251) to an "Exploratory" box or an appendix
**Problem.** This is the third analysis of the same 78 games. It carries five caveats and its own rule-score
construction, and it sits in the main results right before §5.4. It costs a judge about 90 seconds and does not
bear on any headline claim. Relocating it keeps every hedge.
**Replace lines 243–251 with a one-line pointer:**
```markdown
*Forecasting which agreements are kept (E133, exploratory, 78 games):* see Appendix C. Briefly, with the private
chat, say–do features add nothing beyond early price stability, and there is no evidence that public messages
add predictive value.
```
**Then add Appendix C** containing lines 243–251 verbatim, under the heading `### C. Exploratory: forecasting
execution (E133)`.

---

## P3 — polish

### 11. Internal dataset names in captions (Fig. 4 line 201, Fig. 5 line 277, Fig. 6 line 283)
Replace `llm_v3rep` with "first fresh replication (`llm_v3rep`)" and `llm_p2strongF` with "strong-framing arm
(`llm_p2strongF`)". Keep the identifiers for traceability, but lead with the plain name. In the Figure 6 caption,
add: "Dashed line = tacit-high threshold (Nash + 2). Right panel: the no-channel tacit-high class (green) overlaps
the strict-executed channel class (blue), so price paths cannot separate them."

### 12. SLIDES.md: add the takeaway to the title slide and trim slide 4's first bullet
- After SLIDES.md line 10, insert: `**Takeaway:** the channel shows up as *higher prices*; we detect no
  co-movement, and public messages give a zero-shot auditor no resolved gain, so a price flag is an audit trigger, not proof.`
- Slide 4, line 54: move "(four disclosed exposures, so not fully blind; plotted premium statistic chosen post
  hoc)" to a footnote line at the slide bottom: `*Locked test had four disclosed exposures (not fully blind);
  the plotted premium statistic was chosen post hoc.*` The bullet then reads: "Combined − better single view:
  −0.01 [−0.09, +0.06] (locked test, n = 95); −0.07 [−0.17, +0.02] (fresh replications, pooled post hoc)."
- Slide 6: add the safety framing as the first bullet: "Two natural oversight tools (dependence tests on
  actions, LLM monitors reading public text) did not recover the side channel better than a crude price
  statistic in these markets; the text monitor could be misled. Sellers were not adversarial."

---

**Not recommended:** do not shorten §3's label table or Appendix A/B. They are dense, but judges who check them
will value the denominators, and they sit after the narrative.
