# Iteration 33 — current-release distribution and reviewer handoff

Manager verification, 2026-10-25; no external critic or model call.
Historical target: `c1e7fddaca131f0fefc8a7c5aa3cd7e27888db4a` (iteration 32).
Receipts: [distribution](../results/distribution_check_i33.json),
[archive](../results/reviewer_archive_i33.json).

The iteration-29 remote-clone receipt predates the raw pCMI/shift-null replay and
the 158th evidence file. This pass checks the current release and whether a reader
can acquire it, rather than repeating an unchanged historical acceptance check.

## Access finding

An anonymous clone, with Git's system/global configuration disabled and prompts
disabled, failed with exit 128: `could not read Username for 'https://github.com'`.
Anonymous requests to the merged repository page and GitHub API repository endpoint
returned HTTP 404. Both sibling repository pages also returned 404. The configured
SSH clone succeeded. `gh repo view --json visibility,isPrivate,url` could not run
because the CLI has no authenticated session; we therefore do not infer or claim
the visibility setting. No visibility or permission changes were made.

This limits earlier wording about "public URLs": the export checker verifies URL
structure and the absence of local file links, not anonymous remote availability.
The iteration-29 procedure's suggestion of an anonymous HTTPS checkout is not
supported by this check. README and REPORT now say that readers need repository
access or an author-supplied archive. Once acquired, the evidence bundle does not
need sibling clones or model credentials. The PDFs remain self-contained for
reading; following their GitHub links requires access.

## Fresh remote-clone procedure

```bash
git clone --no-local gh-cbw:DennisToma/collusion-beyond-words.git /var/tmp/bw-iteration33-release
cd /var/tmp/bw-iteration33-release
git checkout --detach c1e7fddaca131f0fefc8a7c5aa3cd7e27888db4a
uv sync --locked --all-groups --no-cache
```

`gh-cbw` is the author's authorized SSH host alias. These commands require an
unused destination and access to the repository; another authorized checkout
method can substitute for the clone command.

The exact [verification driver](distribution_i33_driver.py) records the executed
commands, compares outputs to Git blobs at the target, and generates the receipt.
Run it with Python after the setup above; its scratch constants are fixed to this
historical run. Use fresh matplotlib/browser directories for a fresh-install
check. Access fields in that driver record the separately performed probes above;
they are not live permission queries.

The verification commands inherited only PATH, HOME, LANG, LC_ALL and TMPDIR where
present, plus absent sibling-root overrides and fresh matplotlib/browser paths.
HOME was unchanged; no model environment variables were passed. This is the same
author VM, not an OS or filesystem sandbox. The driver downloaded Chromium into
the new browser directory. It deleted all six replay JSONs and six figure PNGs
before reconstruction, then ran every scientific/export command in the receipt.
It deliberately excluded the machine-local runner-log refresh.

All commands passed: 111 source assertions, 139 document bindings, 158 evidence
hashes, no unclassified decimals, 26 reproduction tests and 9 export tests. All
six deleted replay outputs and all six figures rebuild byte-identically. Both
PDFs retain identical page text, content streams and complete bytes after
normalising only CreationDate/ModDate (17 report pages, 8 slides). The export
preserves 492 report fragments, 55 slide fragments and 10 figure embeddings.
Only the two PDFs and their hashes in the export receipt change in the scratch
clone. Every other tracked path is byte-identical; production PDFs were retained.

## Archive handoff check

Created a local archive of the same tested revision:

```bash
git archive --format=tar.gz --prefix=beyond-words/ --output=/var/tmp/beyond-words-c1e7fdd.tar.gz c1e7fddaca131f0fefc8a7c5aa3cd7e27888db4a
sha256sum /var/tmp/beyond-words-c1e7fdd.tar.gz
```

The compressed archive is 6,815,414 bytes. SHA256:
`e0b98aec5182d0bd504c9a67ed9f606c9ae90e7cc69411cb07cc4624e032687b`.
Extracted it into `/var/tmp/bw-i33-archive`; all 244 tracked files match the
target's Git blobs and there is no `.git` directory. From that extraction,
check_sources, number_coverage, all 26 reproduction tests, PDF export and all
9 export tests pass. This second check reused the fresh clone's Python environment
and browser, with absent sibling roots and no model environment variables.

The archive contains the tested frozen submission, slides, evidence and code at
`c1e7fdd`; it predates this access note and its receipts. It is available locally
for the author to transfer. This iteration did not transfer files, publish a new
location or grant reader access. README includes a command to package a later
HEAD after any final metadata changes.

## Scope

This verifies distribution and the historical calculations, including replay of
the archived pCMI null. It adds no markets, settings, labels, model judgments or
held-out evaluation. Ground-truth validity, other detector nulls and portability
to another operating system remain outside this check. Scientific estimates,
manuscript, figures, PDFs, evidence pins and the dated usage snapshot are unchanged.
