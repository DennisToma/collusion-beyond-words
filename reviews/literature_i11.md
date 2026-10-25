# Iteration 11 — primary literature and construct audit

2026-10-25 UTC. Manager review of all bibliography entries and the claims they support, followed by
independent gpt-6.1-sol (high) and Opus reviews of the scientific diff. This is synthesis and claim
verification, with no new experiments, seller/auditor calls, tuning or metric recomputation.

## Scientific fixes

**SALT: corrected an unsupported mechanism explanation.** The previous abstract, Table 2, external-case
paragraph and slide 5 said the detected act happened in chat. In the primary paper, communication and
submitted verdicts are separate phases (§2 and Appendix H.1.3–H.1.4). In the source analysis, `render`
uses only the episode's `communication` field and `PROMPT` explicitly excludes verdicts and task results.
`report` evaluates those message-only scores against subsequent mutual-ACCEPT labels. The evidence
therefore supports predicting later rule-breaking verdicts from earlier messages. It does not establish
why this text auditor works better than in pricing markets, or that adding text improves an action
view. The source REPORT's P2.12 explanation was stronger; the merge deliberately follows the source
code and primary paper instead. No result or label was changed.

Pinned code: [Q2.2 salt_d1.py](https://github.com/DennisToma/collusion-22-say-vs-do/blob/91ffb2d4737a7537cdf9afe239a98e0d1061090b/salt_d1.py).
SHA256: `d11ca4a3af7356c29b0c922cda9738a2239159419d69c806c57bc41b9a67d6eb`.
Relevant functions: `render`, `audit`, `cluster_boot`, `report`; declaration: `PROMPT`.

```bash
git -C ../collusion-22-say-vs-do show 91ffb2d4737a7537cdf9afe239a98e0d1061090b:salt_d1.py | sha256sum
```

The no-accept/reject sensitivity is now retained with its sample size. Matching is case-insensitive
and includes substrings (e.g. inflected verdict words); this is a selected-subset comparison, not a
causal intervention on the text. Two source assertions and four document bindings check these values.

The source code and saved `salt_d1.json` also confirm that SALT's episode AUROC uses a bootstrap clustered
by multi-episode run. Methods now distinguishes that unit from the market game bootstrap. The omitted
Shi/Zhang/Yang paper and the source-data revision are now cited. The underlying violation is a verification
protocol violation; task outcomes are not independently required to be wrong by this label.

**Rose: separated the definition from its operational relaxation.** The causal criterion in Definition
4.7 and the observed-communication/harmful-action criterion in 4.7′ are different. The primary paper uses
the latter without requiring counterfactual causation. Related work now states the distinction.

**Cao & Hu: removed a false absence-of-coordination claim.** The independent Codex reviewer found the
pre-existing phrase “without coordination” in the revised related-work paragraph. The model produces
implicit coordination without communication between sellers. Changed to the latter and described the
result as a shared-AI-advisor model. Rechecked by the reviewer: no open P1/P2.

**Headlines: preserved the pCMI exception.** TL;DR, README and deck now say no *robust* contemporaneous
co-movement; slide 4 explicitly mentions the single base-Qwen3.6 separation and failed grid replication.
The abstract already disclosed it. This does not turn nonsignificance into equivalence.

## Bibliography checks

All entries below have a primary landing page or publisher-deposited metadata supporting identity and
the narrow claim retained in the report. Abstract-only checks do not validate a paper's methods or findings.
Original author-year conventions are retained; versioned preprint URLs identify the text checked.
No paper's numerical findings were added to the submission.

| citation | primary evidence checked | supported scope / correction |
|---|---|---|
| Agrawal 2025 | [arXiv v1](https://arxiv.org/abs/2507.01413v1), abstract | communication/model/pressure differences in seller double auctions |
| Banchio & Mantegazza 2023 | [ACM proceedings index](https://www.sigecom.hosting.acm.org/proceedings23.html), [publisher DOI](https://doi.org/10.1145/3580507.3597726), [revised preprint v5](https://arxiv.org/abs/2202.05946v5), abstract | EC title differs from revised arXiv title; both explicitly labelled; coupling mechanism remains supported |
| Bonjour 2022 | [PMLR](https://proceedings.mlr.press/v180/bonjour22a.html), abstract and citation | action-information dependence; corrected title spelling/capitalisation and completed authors/pages |
| Calvano 2020 | [AEA](https://www.aeaweb.org/articles?id=10.1257/aer.20190623), abstract and citation | repeated pricing with reward/punishment; our work uses Nash reference and does not test that mechanism |
| Cao & Hu 2026 | [v3 §1](https://arxiv.org/html/2601.01279v3) | shared-advisor theoretical model; no seller communication, not absence of coordination |
| Dhanda 2026 | [publisher-deposited Crossref record](https://api.crossref.org/works/10.21203/rs.3.rs-10183486/v1), title/author/date/abstract | price-cap focal-point finding; full revised title and DOI added; Research Square direct page inaccessible in this pass, full methods not re-reviewed |
| Fish 2024 | [arXiv v6](https://arxiv.org/abs/2404.00806v6), abstract | supracompetitive prices and prompt sensitivity; first-preprint year retained, revised year noted |
| Green & Porter 1984 | [author archive](https://authors.library.caltech.edu/records/4f2vn-4x241), abstract and [published PDF reprint](https://jeromemathis.fr/wp-content/uploads/2020/01/GreenPorter_ECA1984.pdf); [DOI](https://doi.org/10.2307/1911462) | noncooperative cartel enforcement; published PDF gives pages 87–100 (archive metadata's 84–100 is inconsistent) |
| Lin 2024 | [v2 §3/§4](https://arxiv.org/html/2410.00031v2) | Cournot market division with no direct communication; wording clarified |
| Mathew 2024 | [arXiv v2](https://arxiv.org/abs/2410.03768v2), abstract | steganographic communication under optimisation; restored full title |
| Motwani 2024 | [NeurIPS proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/861f7dad098aec1c3560fb7add468d41-Abstract-Conference.html), [arXiv v5](https://arxiv.org/abs/2402.07510v5), abstracts | secret/steganographic collusion; venue confirmed |
| Rose 2026 | [v5 §4.3](https://arxiv.org/html/2604.01151v5), Definitions 4.7 and 4.7′ | causal and operational constructs distinguished |
| Schreiber 2000 | [APS](https://doi.org/10.1103/PhysRevLett.85.461), [original preprint](https://arxiv.org/abs/nlin/0001042), abstracts/metadata | transfer entropy; DOI/pages added |
| Shi, Zhang & Yang 2026 | [v2 §2 and Appendix H](https://arxiv.org/html/2609.24967v2), [author repository](https://github.com/SALT-NLP/agent-collusion), [dataset](https://huggingface.co/datasets/SALT-NLP/agent-collusion) | omitted primary citation added; communication precedes verdict submission; source revision 2eba8f37 recorded in Q2.2 code/REPORT |
| Tailor 2025 | [arXiv v2](https://arxiv.org/abs/2510.04303v2), abstract | proposed information-theoretic auditing; kept as preprint, not an independently validated benchmark |

Metadata fallback for DOI records uses the registry's JSON API, e.g.:

```bash
curl --fail 'https://api.crossref.org/works/10.21203/rs.3.rs-10183486/v1'
```

## Independent review

- Codex gpt-6.1-sol, high, fresh context, read-only: one P2 (Cao & Hu, above); otherwise SALT, Rose,
  headline scope and saved numeric values checked. After correction the reviewer confirmed zero open
  P1/P2. Reviewer independently checked SALT source values and pinned code.
- Opus: see [opus_i11.md](opus_i11.md) for completed review and disposition. An initial invocation could
  not read source files (CLI read permissions; no scientific review performed); that attempt is not
  counted as a review. The corrected invocation explicitly permits only read tools and the source directory.

The selected numeric bindings and export checks remain necessary but do not validate these semantic
claims. This audit supplements them rather than claiming automated literature verification.
