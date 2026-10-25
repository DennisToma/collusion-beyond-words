# Opus submission-compliance review — iteration 33

Requested by DIRECTION commit `2cf7c7d`. Independent subordinate Claude CLI session,
model `claude-opus-5-5`; scoped to the new abstract, ethics appendix and main-text cuts.
No new scientific analysis or auditor call. Read/Glob/Grep permitted; one attempted Bash
query was denied, and the reviewer completed the review with read tools.

## Initial review (verbatim)

I found no P1 problems: nothing in the new text needs to block release. There are seven small P2 wording fixes. None of the new main text changes a number; the figures I spot-checked match the pre-compliance draft: 0.74/0.51, −0.01 [−0.09, +0.06], 0.65 [0.34, 1.32], 19/20 and the four exposures. I compared `/var/tmp/bw-i33-before-compliance.md` against the current `SUBMISSION.md` and checked the provenance claims against the source REPORTs and DIRECTION.md.

**Abstract (150–250 words; my hand count is about 225, so keep fixes short)**

What the abstract keeps correctly:
- **Prompt-family scope:** it says "seven seller models under one prompt family; only two of five wording variants".
- **pCMI positive control and exception:** it says the detector passed the scripted control, scored 0.51 [0.43, 0.59] in the grid, and that one model-specific separation did not replicate.
- **Text-versus-price null:** it reports the locked-test −0.01 [−0.09, +0.06] and scopes it to "the say-vs-do market".
- **External-task exception:** it is labelled "a different … task".
- **Exposures:** it mentions "disclosed test exposures".

Fixes:
- **P2-1 (overclaim, new wording)** — "A simple price-level screen outperformed contemporaneous conditional dependence by point estimate throughout." "Throughout" is not true. The level screen beats pCMI in only 12 of 16 grid cells. In E66 the level screen scores 0.44 and pCMI 0.46. The paired difference resolves in 8 of 9 sets, not 9. Change "throughout" to: "…by point estimate in all nine sets (paired CI resolved in eight) and in the pooled grid."
- **P2-2 (weakened caveat)** — "weak lagged dependence remains" can read as a leftover sign of coordination. The main text says TE also flags legitimate shared policies. Change to: "lagged dependence (TE) was weakly above chance but also flags legitimate shared policies."
- **P2-3 (new wording reads as causal)** — "The channel raised markup" credits the delivered channel, but the main text and §6 say the effect is "channel assignment, including its prompt cue". Write "Channel assignment (including its prompt cue) raised markup…".
- **P2-4 (missing qualifier)** — The −0.01 result needs "for a zero-shot gpt-6.1-sol auditor" right after "adding public messages to prices".
- **P2-5 (dropped interval and model scope)** — "about two thirds of the channel premium" has no CI, and the CI runs from 0.34 to 1.32. The no-channel high prices were seen only in gpt-6-luna. Write "(ratio 0.65 [0.34, 1.32])" and "memory plus profit framing yielded high no-channel gpt-6-luna prices". If words are tight, keep the CI and drop the gpt-6-luna note, which the main text already makes in §5.4.

**Appendix G (ethics):** honest, no regression. It names the misuse paths: exposing monitoring blind spots, and repurposing the released prompts, traces and detectors. It does not promise the artifacts cannot be reused ("does not eliminate reuse risk"). It says no evasion procedure was introduced and that the abliterated models were used only as sandbox sellers. It tells defenders how to act: a missing flag doesn't certify competition, and shared models need provenance checks. The limitation bullets are the old §7 word for word. The "author remains responsible" line is worded as responsibility, not as a claim that a human checked everything, which is consistent with H.

**Main-text cuts:** no crucial qualification is lost.
- Still in the main text:
  - the one judge family and the weak cross-family check (§3)
  - execution labels being defined from prices (§7)
  - the four test exposures (§3)
  - the 14/50 kept-agreement count (§5.4)
  - the delivery result being unresolved (§5.4)
  - small co-movement not being excluded at T = 20 (§5.2)
  - the two-stage audit never being evaluated (§6/§7)
- The detailed numbers live on intact in Appendices D–F.
- **P2-6 (cut hides a qualification)** — §5.2 now says TE is only "weakly above chance in the grid". The cut dropped that TE is clearly above chance in two main sets (deepseek 0.81 [0.62, 0.96]; base Qwen3.8 0.91). That cuts against the "no robust dependence" framing. Add: "and clearly above chance in two main sets (Appendix E)."
- Less important: §5.4 no longer says that in the strong-framing arm the channel adds no detectable price (−0.44 [−1.84, +1.00]). It's optional to restore it as "channel labels stop being ground truth there", since §5.4 already says the result "does not verify coordination".

**Disclosures and affiliation:** these check out.
- "Dennis Toma — Independent" comes from DIRECTION.md item 3 (Dennis's own instruction); the source REPORTs give no affiliation.
- Starter commit `d585a7b` for E68 is recorded in Q1.4 REPORT.md line 826.
- The trust-breaking arm was planned as an option in Q2.2 PLAN.md line 23 and dropped in Q2.2 REPORT.md lines 114 and 681, so "considered … dropped" is accurate.
- The iteration counts are unchanged from the earlier draft.
- **P2-7 (formatting, new)** — "### H. AI assistance and pre-existing material" is followed directly by "## LLM usage statement". The higher-level heading takes the usage statement and "Pre-existing code and data" out of Appendix H. Demote it to "#### LLM usage statement" and demote "### Pre-existing code and data" to "####".

**Already-disclosed source limitations (not regressions):** the old drafting note "whose sellers invite rivals publicly", now kept in Appendix D, conflicts with §F, where channel sellers invite *less*. It is inherited text, but it's worth aligning.

I did not estimate page count.

## Manager disposition

All seven P2s applied: restrict level dominance to the nine main sets; retain TE's
shared-policy caveat; name channel assignment and its prompt cue; identify the zero-shot
auditor; add the notepad ratio CI and no-channel seller model; restore clearly above-chance
TE in two main sets; make all disclosure headings subordinate to Appendix H.
The optional kept-count and strong-framing caveats are restored in the main text too.
Appendix D now says sellers *can* invite rivals publicly, consistent with Appendix F's
lower invitation rate in the channel arm. No estimate changed. The script's whitespace
word count is authoritative (216 after fixes), rather than the reviewer's hand estimate.


## Follow-up review (verbatim)

No P1 or P2 problems remain in the abstract, the ethics appendix or the cuts. All seven fixes are in the current `SUBMISSION.md`, and I found no new problems.

- **Abstract (lines 7–13):**
  - **Prompt cue:** it now says "Channel assignment, including its prompt cue, raised markup" and keeps the scope to one prompt family, with two of five wordings resolved.
  - **Level screen vs pCMI:** "throughout" is gone. It now reads "by point estimate in those nine sets; paired CIs resolved in eight".
  - **TE:** lagged TE now comes with the shared-policy false-positive caveat.
  - **pCMI:** the positive control and the 0.51 [0.43, 0.59] grid result are kept, and the exception is still described as "did not replicate".
  - **Text result:** the zero-shot gpt-6.1-sol auditor qualifier is present, and the result is still scoped to the say-vs-do market's locked test.
  - **External task:** still described as "different".
  - **Notepad and framing:** the notepad ratio has its CI (0.65, [0.34, 1.32]), and the no-channel high prices are limited to gpt-6-luna.
  - **Overall:** no claim is stronger than the evidence supports, and the numbers are unchanged.
- **§5.2 (line 133):** it now says TE is clearly above chance in two main sets (pointing to Appendix E) and is not read as evidence of coordination.
- **§5.4 (line 155):** it restores that the channel adds no detectable price in the strong-framing arm and that channel labels stop being ground truth there, and it gives the 14/50 count explicitly.
- **Headings:** Appendix G is titled as required. Under H, the LLM usage statement, pre-existing code and Reproducibility are now `####` subheadings, so they stay inside the appendix.
- **Inherited Appendix D wording (line 300):** the "invite rivals" phrase now reads "where sellers can invite rivals publicly". It no longer conflicts with Appendix F.

Optional cosmetic point: "pCMI" and "TE" appear in the abstract without being spelled out. Writing "conditional dependence (pCMI)" and "transfer entropy" would fix that for about 3 extra words, staying well under 250.

Manager: the optional acronym expansion is applied (Gaussian conditional mutual information and transfer entropy); the final abstract has 219 whitespace-delimited words. No open P1/P2.


## Source-scope handoffs

Q1.4 I146/I147 (`1ebf938`) and Q2.2 I155 (`e3fa1dc`) independently read the
compliance rewrite and report zero P1. Q1.4's optional dominance wording nit was
already fixed. All five optional Q2.2 nits are applied: Appendix D rule pointer,
Qwen3.8-base and post-hoc invitation wording, Qwen scope in the form, gpt-6-luna
scope on the headline contrast, and the cost-adjusted mean-price/window definition.
