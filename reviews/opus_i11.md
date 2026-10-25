# Iteration 11 — Opus scientific diff review

Reviewer: **claude-opus-5-5**, read-only CLI. Read tools explicitly allowed for the source directory;
no permission denials in the completed review. Intermediate candidate, before the final sensitivity
addition and all disposition edits. No experiments or simulated seller/auditor calls.

An earlier invocation could not read files and performed no review; it is not counted.

## Manager dispositions

- P2/1: added the no-accept/reject-word SALT sensitivity to report and slides, with sample size;
  selected-subset comparison, no causal ablation. The review's suggestion that verdict words *inflate*
  AUROC is not established by comparing these selected subsets, so that causal interpretation was
  not adopted. Source values have two new assertions and four document bindings (M35).
- P2/2: §5.2 heading already updated during the review; now consistently says no robust co-movement.
- P2/3: intermediate diff predated Cao correction; the final sentence was independently checked
  against primary v3 by manager and Codex, and the final diff includes it.
- P3/1–5: all addressed: abstract explicitly different task/no action-view comparison; peer verification
  terminology; CI methods scoped by analysis; frozen-source framing discrepancy disclosed; rule violation
  does not require incorrect task work. Source reports retained verbatim.
- Primary external literature was verified separately by manager and Codex. Opus had no web tools and
  its review does not independently validate external pages. Its source-code/JSON checks are independent.

## Original completed review

I found **0 P1, 3 P2 and 5 P3** issues. I read all four files; no edits and no experiments. To check numbers I also read `results/analysis/salt_d1.json` and the bundled `evidence/q14/REPORT.md` and `evidence/q22/REPORT.md`. I have no web access here, so I could not open the external papers (Rose v5, Cao & Hu v3, Lin, Shi/Zhang/Yang). Anything about what those papers say is unverified.

### P1
None.

### P2
1. **The verdict-word sensitivity check is left out of the SALT reframing.** The new text says "preceding messages predict later rule-breaking ACCEPT verdicts", and the slides add "no submitted verdicts shown". The phase separation itself is correct: `salt_d1.py:145-153` (PROMPT) and `render()` (`:163`) give the auditor only `r.communication`, followed by a separate ACCEPT/REJECT step.
   - The script also tests chats with no "accept"/"reject" words in them (`:259-262`). That AUROC falls from 0.875 to **0.752 [0.658, 0.836]** (`salt_d1.json` E105_audit.auroc_no_verdict_words). Only n = 117 of the 240 chats lack those words, with 50 executed.
   - So about half the sampled chats contain verdict words, which can include agents announcing what they will decide, and that inflates the headline 0.87.
   - The old caveat ("act happens in the chat") roughly covered this. The new wording drops it without adding the sensitivity result.
   - **Fix:** report 0.75 [0.66, 0.84] (n = 117) in §5.3 and ideally on the slide.
2. **The §5.2 heading still says "no co-movement is detected"** (`SUBMISSION.md:196`). That contradicts the new "no robust" headline and the base-Qwen3.6 exception stated in the same section (`:222`, 0.71 [0.51, 0.88]).
   - The exception wording is otherwise consistent everywhere. The grid's Qwen cells are qwen-3.6-35b at 0.46 [0.35, 0.58] (`evidence/q14/REPORT.md:22, :29`), and "different design, board on" supports "without grid replication".
3. **The patch doesn't match the working tree for Cao & Hu.** In the patch, `Cao & Hu (2026) show … shared LLM advisor without coordination` is unchanged context (patch line 100). The file now reads `model … shared AI advisor without communication between sellers` (`SUBMISSION.md:106-107`).
   - So the regenerated diff predates or omits the Cao & Hu fix, and this review did not cover that edit as a diff. The new wording fits the "no communication vs coordination" distinction.
   - Whether "model" (a theoretical framing) is accurate for Cao & Hu v3 is unverified, since I couldn't access the paper.

### P3
1. **The abstract's SALT clause lost its "different construct" caveat** (`SUBMISSION.md:37-38`). "Text did work…" sits inside a point headed "no resolved gain [from adding text]". §5.3 says "no test of text added to an action view"; the abstract should say so briefly too.
2. **"Repeated peer review"** (`:113`) reads like academic peer review. The script describes agents verifying each other's task work (`salt_d1.py:3-5`), so "repeated peer verification" fits better.
3. **The Statistics paragraph (`:169-171`) overstates how uniform the CI methods are.**
   - Q2.2 market AUROCs also use a seed bootstrap (C24), a within cell × arm bootstrap (C31) and Newcombe intervals (C21).
   - The k/n rates for C14/C15 use Jeffreys, not Wilson.
   - The SALT claim is correct: `cluster_boot` resamples `run_id`. That bootstrap is not class-stratified, and the sample was stratified by condition × label, which is fine but worth one clause.
4. **The bundled source now disagrees with the new framing.** `evidence/q22/REPORT.md:12, 20, 88` still says "negotiation, deal struck in chat". The submission says every number traces to those sources, so add a short note that the framing was revised after the source freeze.
5. **SALT's "collusion" is not Rose-style collusion.** 4331 of 5169 executed accepts are of correct work, and only 838 involve incorrect work (`salt_d1.json`). "Rule-breaking" is the right word. Don't let §2's Rose definition (which requires harmful actions) be read as describing SALT.

### Verified consistent
- **SALT figures:** AUROC 0.8749 [0.8305, 0.9146]; n = 240 with 120 executed; P(said | executed) = 0.3848, so 62% have no explicit agreement; 5169 = 838 + 4331. Table 2, §5.3, the slide and Appendix C10/C12/C22 all agree.
- **"No robust co-movement":** the wording matches across the README, TL;DR, Contributions, §6, the slide title and slide 6. All co-movement numbers are unchanged and match Table 1 and Appendix A. Slide 3's "separates once" matches 1 of 9 sets.
- **Rose et al.:** the 4.7 (causal) vs 4.7′ (operational) description is internally consistent with what you summarised, but I couldn't check it against the paper.
- **Unverified external claims:** Lin et al.'s "without a communication channel" and the Shi, Zhang & Yang arXiv ID 2609.24967v2 need checking against the papers.
- **Classic references:** the venue, volume and page details for Calvano, Green & Porter, Schreiber, Motwani, Mathew and Fish match my recollection.

## Final targeted recheck

I found no remaining P1 or P2 issues. This was a read-only review: I made no edits and did not run `check_sources.py`, so the bindings were checked by reading the code, not by running it.

**Numbers against the source**
- `salt_d1.json` `E105_audit.auroc_no_verdict_words` holds est 0.7521, CI [0.6583, 0.8358], n 117, n_exec 50. Rounded to two places that is 0.75 [0.66, 0.84], which matches SUBMISSION:296, SLIDES:58, M35 at `scripts/check_sources.py:144-146` and SOURCES M35. All three values are within the checker's ±0.005 tolerance (the widest gap is 0.0042), and n is checked exactly.
- In `salt_d1.py:report` (lines 259–262), the subset is defined by a case-insensitive `accept|reject` regex over the messages. The CI comes from `cluster_boot`, which resamples by `run_id`. So "bootstrap clustered by multi-episode run" (SUBMISSION:171-172) is accurate.
- The prompt and `render` (lines 145–165) show the auditor only sees the messages: no verdicts and no task results. The `harm` split (line 94: 838 harmful vs 4331 correct-work accepts) supports "the violation label does not require an incorrect task outcome."
- The counts add up. There are 59 `check()` calls and 68 bindings (64 + 4 M35). The four M35 bindings use fixed digits (2,2,2 and 0) and their templates match the printed text. The other JSON edits only change literal Unicode characters to `\u` escapes, which doesn't change their meaning.

**Wording**
- The subset result is called an "observational selected-subset comparison… not a causal ablation". It is never read as inflation of the 0.87.
- The "no robust" wording is now the same across TL;DR, abstract, contributions, §5.2 heading, conclusion, README and slides, including the section heading on slide 3.
- The abstract's SALT clause now says "different task; no action-view comparison." Table 2 uses "peer verification."
- The Statistics paragraph now covers the right methods for each analysis: class-stratified, matched-seed and stratum resampling, SALT run-clustered, Wilson/Jeffreys/Newcombe.
- The note that the report departs from the frozen source report is at SUBMISSION:299-301 and SOURCES:96-101.
- The Cao, Lin and Rose wording matches the facts you gave me. I did not verify the primary papers externally myself; that rests on the manager's and Codex's checks.

**P3 (optional)**
1. The regex matches substrings, so it also drops "accepted", "acceptable", "rejection" and so on. "Without words containing accept/reject" would be more exact than "without the words accept/reject".
2. You could report the subset's class split: 50 executed and 67 not executed out of 117.
3. The SALT bullet on slide 4 doesn't mark the subset as a selected subset or say it isn't causal. That's acceptable for a slide, but adding "(selected subset)" would cost little.

Manager disposition of final P3s: clarified case-insensitive accept/reject matching in the report and
substring matching/selected subset on the slide; updated the corresponding binding contexts. The
optional class split remains available in the source JSON rather than adding more numbers to the slide.
No open P1/P2.
