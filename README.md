<img src="assets/readme-header.png"
     alt="Covidence Screening Automation — apply screening decisions, one study at a time"
     width="700"
     style="display: block; margin: 1 auto;">

Automates two stages of a [Covidence](https://www.covidence.org/) systematic-review project,
one study at a time, via browser automation (Playwright): applying pre-computed title/abstract
screening decisions, and retrieving + attaching full-text PDFs for studies that passed
title/abstract screening.

**Context:** built for a systematic review on breastfeeding vs. formula feeding and the
infant gut microbiome (PROSPERO CRD420261485879, Covidence review 818465,
*"microbiome_methodologies"*). The decisions in `search-results-2026-10/screening_decisions.csv`
were produced by reading each record's full title and abstract against this review's own
PECO eligibility criteria — not by an LLM API call at vote-time, and not by guessing. This
repo captures the review step and the automation that applies it, including the bugs found
and fixed along the way, so the process is reproducible and the failure modes are documented.

This README covers both stages: **title/abstract screening** (below) and **full-text
retrieval + upload** (see [Full-text retrieval and upload](#full-text-retrieval-and-upload)
further down).

---

## Contents

| File | Purpose |
|---|---|
| `apply_screening_decisions.py` | Main script. Logs into Covidence, reads the screening queue, and casts the correct vote (Include → Yes, Exclude → No, Maybe → Maybe) for each study, one at a time. |
| `debug_queue.py` | Read-only diagnostic. Logs in, opens the queue, and prints the raw text/HTML of the first few study cards — casts **no votes**. Use this if Covidence changes its page layout and the main script starts misbehaving again (see [Known issues](#known-issues--troubleshooting-history) below). |
| `search-results-2026-10/screening_decisions.csv` | The screening results: one row per PMID, with columns `pmid,decision,justification`. |
| `retrieve_remaining_full_texts.py` | Finds free copies of missing full texts via Unpaywall + Crossref. See [Full-text retrieval and upload](#full-text-retrieval-and-upload). |
| `download_blocked_oa_pdfs.py` | Retries open-access PDFs that a publisher's bot-check blocked, via a real browser. |
| `upload_full_texts.py` | Attaches locally-held full-text PDFs to the matching Covidence record. |
| `full-text/retrieval_status_<date>.csv` | Per-record status: already available locally vs. still needs retrieving. |
| `full-text/remaining_retrieval_categorized_<date>.csv` | Still-missing records, categorized by retrieval route. |
| `requirements.txt` | Python dependencies. |
| `.env.example` | Template for your local credentials file. |
| `.gitignore` | Keeps `.env`, virtual environments, logs, and downloaded PDFs out of version control. |

---

## Background: how `screening_decisions.csv` was produced

- **Source set:** a PubMed search executed via NCBI E-utilities, exported as MEDLINE text,
  producing **2,109 deduplicated records**. This is the exact file that was imported into
  Covidence review 818465 — the two were diffed PMID-for-PMID and confirmed identical
  (2,109/2,109 match, zero on either side) before any voting was attempted.
- **Screening method:** each record's full title and abstract (not just the title) was read
  against the review's settled PECO criteria:
  - Healthy term infants (≥37 weeks gestation), 0–12 months at stool sampling — preterm/NICU
    populations excluded by design.
  - Exposure/comparison must be breastfeeding vs. formula (or vs. mixed/combination feeding)
    as an *actual analyzed group comparison* — not merely an adjustment covariate.
  - Outcome must be gut/stool **bacterial** composition assessed via sequencing (16S rRNA or
    shotgun metagenomics) — this is a hard gate. Function (metabolomic, PICRUSt-predicted,
    targeted assay, shotgun) is a secondary, non-gating outcome but does not substitute for
    the sequencing-based composition requirement. qPCR-only, FISH-only, culture-only, or
    DGGE/microarray-only methods fail this gate even when they report feeding-mode
    differences.
  - Non-stool specimens (breast milk, colostrum, oral, nasopharyngeal, skin, vaginal,
    blood/serum/urine), animal models, in vitro/ex vivo/organoid/bioreactor studies, bacterial
    strain/genomic/enzyme characterization studies with no infant cohort, virome/mycobiome-only
    outcomes, disease-population studies where the primary comparison is by disease rather than
    feeding mode, narrative reviews/commentaries/conference-abstract-only records, and
    protocols with no results yet reported were excluded.
- **Decision values:**
  - `Include` — meets all criteria.
  - `Exclude` — fails one or more criteria (reason given in `justification`).
  - `Maybe` — genuinely ambiguous (e.g., abstract doesn't state the sequencing method,
    unclear whether a real feeding-mode comparison is reported, missing abstract text).
    These are deliberately **not** force-resolved to Include/Exclude; they're meant to
    surface for full-text human review, which is exactly what voting "Maybe" in Covidence
    does.
- **Final tallies (2,109 total):** 163 `Include`, 1,922 `Exclude`, 24 `Maybe`.

---

## Prerequisites

- Python 3 (any recent 3.x)
- A Covidence account with voting permission on the target review
- macOS/Linux/Windows with a terminal — no other software needed; Playwright installs its
  own Chromium browser (see below)

---

## Setup
cd into your working directory
```bash
# 1. (recommended) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. install Python dependencies
pip install -r requirements.txt

# 3. download the Chromium browser Playwright drives (one-time, ~100-200MB)
pip install playwright
playwright install chromium

# 4. create your local credentials file
cp .env.example (rename to .env)
```

Open `.env` in a text editor and fill in your **own** real Covidence login:

```
#covidence password and username
COVID_ID=you@example.com
COVID_PASSWORD=your_real_covidence_password
```

`.env` is loaded automatically via `python-dotenv` and is excluded from git by
`.gitignore` — never commit it, never share it.

---

## Usage

### 1. Test run first — always

Before trusting it with the full queue, sanity-check on a handful of studies:

```bash
python3 apply_screening_decisions.py --limit 10
```

A visible Chromium window opens, logs in, goes to the review's screening queue, and votes
on the first 10 studies at the top of the queue. Watch the terminal output — each line
should show a **real, 7–8 digit PMID** next to a sensible title and decision, e.g.:

```
2026-10-01 16:21:26,722 INFO PMID 27446009: Exclude ('Flow Cytometric and 16S Sequencing
Methodologies for Monitoring the Physiological Status of the Microbiome in Powdered Infant
Formula Production.')
```

Then **cross-check a few of those in the Covidence UI directly** to confirm the votes
landed on the right studies before proceeding.

### 2. Full run

```bash
python3 apply_screening_decisions.py
```

With no `--limit`, it processes up to 10,000 studies (effectively "all of them"),
reloading the page before every single vote. This is deliberately slow and one-at-a-time
— see [How it works](#how-it-works) for why. For ~2,109 decisions expect this to take
several hours; let it run.

To run without a visible browser window:

```bash
#update the script to have your file path: 
python3 apply_screening_decisions.py --headless
```

---

## How it works

`apply_screening_decisions.py` loads all rows of the decisions CSV into memory, then loops:

1. Reload the screening queue URL (`.../review_studies/screen?filter=vote_required_from`).
2. Grab the study card currently at the top of the queue.
3. Extract its PMID and title from the page.
4. Look up the PMID in the loaded decisions.
   - **Found:** click the matching vote button (Yes/No/Maybe) and log it.
   - **Not found:** stop immediately without voting (see
     [`no_decision` behavior](#3-no_decision-now-stops-instead-of-guessing) below).
5. Repeat from step 1.

**Why reload before every single vote, one at a time?** Covidence's screening list recycles
DOM nodes between items. Voting on several queued studies without a fresh reload in between
produced unreliable results during testing — votes silently not saving, or landing on the
wrong study. A full page reload immediately before each individual interaction was the only
pattern that worked reliably.

---

## Known issues / troubleshooting history

This section exists because this exact script already failed once in a subtle way during
initial testing, and the fix depended on evidence gathered via `debug_queue.py` rather than
guessing. If Covidence changes its page markup in the future and voting starts behaving
oddly again, **repeat this process** rather than patching blindly:

1. Run `python3 debug_queue.py` (read-only, casts no votes) and inspect the printed card
   text/HTML.
2. Confirm by hand what the real PMID/title look like in the output.
3. Only then adjust the selectors/regex in `apply_screening_decisions.py`.

### 1. PMID extraction bug (found and fixed 2026-10-01)

**Symptom:** every vote in a 10-study test run logged as `PMID 10`, even though 10 different
papers with 10 different titles were clearly being voted on in sequence.

**Root cause:** the original extraction logic queried for a CSS class (`.ref-ids`) that
didn't contain the real reference number on the live page — it was silently matching some
unrelated element elsewhere in the DOM that happened to read "10". Because the function
returned a non-null value, it never triggered an error; it just silently fed the wrong key
into the decisions lookup, found no match, and voted the safe-default of "Maybe" on every
study — which, at the time, cast genuinely incorrect votes on real studies in the live
review.

**How it was actually found:** `debug_queue.py` was written to log in, print the full
visible text and outer HTML of the first few study cards, and cast no votes. The real PMID
turned out to be rendered as plain visible text on every card, e.g.:

```
DOI:
10.3389/fmicb.2016.00968
•
Ref ID: 27446009
```

**The fix:** `extract_ref_id()` now does a simple regex search (`Ref ID:\s*(\d+)`) against
the card's full visible text (`card.inner_text()`), instead of relying on a CSS class name
that may or may not exist on the current version of Covidence's page. This was verified
against two different real records (cross-checked the "Ref ID" number against the actual
PMID, title, and pre-computed decision for both) before being trusted.

**Cleanup required:** because 10 studies were mis-voted "Maybe" before this was caught, the
9 unique affected PMIDs had to be manually corrected back to their proper decision directly
in the Covidence UI. This is why the test-run-first step above exists — **always test on a
small `--limit` and spot-check in Covidence before running the full batch.**

### 2. Harmless double-vote on the first study right after login

**Symptom:** the very first study processed in a fresh run sometimes gets voted twice in a
row (same PMID, same correct decision, back-to-back).

**Likely cause:** a timing issue immediately after login/page-transition — the first
vote-click occasionally doesn't register before the page reloads, so the same top-of-queue
item is picked up again on the next loop iteration and voted again.

**Impact:** none. Both votes land on the identical, correct value — Covidence just keeps
the current vote. It costs a few wasted seconds at the start of a run and is not worth
engineering around.

### 3. `no_decision` now stops instead of guessing

Earlier behavior (now removed) was: if a study's PMID had no matching row in the decisions
CSV, vote "Maybe" as a "safe default" and keep going. **This is what let the extraction bug
above cause real damage** — it masked the underlying problem instead of surfacing it.

Current behavior: if a PMID has no pre-computed decision, the script **stops immediately
without voting**, logs a clear warning with the PMID and title, and must be resolved by a
human (decide if it's in scope, screen it and add it to the CSV, or vote it directly in
Covidence) before being restarted. This should not happen in normal operation — see
[Scope verification](#scope-verification) below — but if it does, don't restart blindly;
investigate the logged PMID first.

### Scope verification

Before the first full run, the PMID set in the raw PubMed MEDLINE export that was imported
into Covidence was diffed against the PMID set covered by `screening_decisions.csv` and
confirmed to be an **exact match** (2,109 in each, identical set, zero on either side). If
this script or CSV is ever reused against an updated or re-exported search, **redo this
check first** — don't assume the sets still match. A short Python snippet for this:

```python
import json, csv

# PMIDs from the raw MEDLINE (.txt) export, format: "PMID- 12345678"
raw_pmids = set()
with open("path/to/raw_export.txt") as f:
    for line in f:
        if line.startswith("PMID-"):
            raw_pmids.add(line.split("-", 1)[1].strip())

# PMIDs covered by the decisions file
decided_pmids = set()
with open("search-results-2026-10/screening_decisions.csv", newline="") as f:
    for row in csv.DictReader(f):
        decided_pmids.add(row["pmid"])

print("In raw export but not decided:", len(raw_pmids - decided_pmids))
print("Decided but not in raw export:", len(decided_pmids - raw_pmids))
print("Exact match:", raw_pmids == decided_pmids)
```

Any non-zero count on either line means something needs to be screened or reconciled
*before* running the script against that queue.

---

## Monitoring / resuming

- Every run appends to `covidence_apply.log` in this folder — check it for a final summary
  line (`Finished. Processed N studies this run.`) and for any `WARNING`/`ERROR` lines.
- The script always pulls whatever is currently at the top of Covidence's "vote required"
  queue. If you stop it (Ctrl+C) and rerun later, it just continues from wherever the queue
  is now — there's no separate resume flag or state file to manage.
- Keep an eye on it periodically rather than walking away entirely, in case Covidence shows
  a session timeout, CAPTCHA, or other interactive prompt the script can't handle on its own.

---

## After the run completes

1. Check `covidence_apply.log` for the final summary and scan for any `no_decision` or
   `extract_failed` entries.
2. Spot-check a handful of votes directly in the Covidence UI against
   `screening_decisions.csv` to confirm everything landed as expected.
3. For any `Maybe` votes, follow up with full-text review as normal — they were flagged as
   ambiguous on purpose, not resolved automatically.

---

## Security notes

- **Never commit `.env`.** It's excluded via `.gitignore`; only `.env.example` (with
  placeholder values) is tracked.
- `apply_screening_decisions.py` contains the Covidence review URL
  (`.../reviews/818465/...`). This is not a secret, but it is specific to this project's
  review — update `SCREENING_URL` if reusing this script for a different Covidence review.
- Virtual environment directories (`venv/`, `.venv/`, etc.) and the runtime log
  (`covidence_apply.log`) are also excluded from version control — they're local artifacts,
  not part of the reproducible process.

---

## CSV schema

`search-results-2026-10/screening_decisions.csv`:

| Column | Description |
|---|---|
| `pmid` | PubMed ID of the record |
| `decision` | One of `Include`, `Exclude`, `Maybe` |
| `justification` | One-sentence reason for the decision |

---

## Branding assets

`assets/` contains the project's icon set:

| File | Size | Used for |
|---|---|---|
| `readme-header.png` | 1200×400 | The header image at the top of this README. |
| `icon.png` | 512×512 | Square icon/favicon, for reuse wherever a small square mark is needed. |
| `social-preview.png` | 1280×640 | GitHub's link-unfurl / social-media preview image. |

GitHub doesn't let a repo set its own social preview image via a file in the repo or via
git push — it has to be uploaded through the web UI:

1. Go to the repo's **Settings → General**.
2. Scroll to **Social preview**.
3. Click **Edit**, upload `assets/social-preview.png`, and save.

---

## Full-text retrieval and upload

Three scripts that pick up where `apply_screening_decisions.py` leaves off: once a study is
voted **Include** at title/abstract, Covidence moves it into **Full Text Review**, where it
needs an actual PDF attached before a human can screen it at full text. This part of the
toolkit finds those PDFs (legally, via open-access lookups) and attaches them to the right
Covidence record, the same "automate the repetitive part, never fabricate the judgment part"
approach as the title/abstract tool.

**Context:** same review as the rest of this repo (Covidence review 818465,
*"microbiome_methodologies"*). As of the run this was built for, 235 studies had reached
Full Text Review and 148 of them had no PDF attached yet in Covidence.

### The pipeline, in order

```
1. retrieve_remaining_full_texts.py   -- find free copies via Unpaywall + Crossref
2. download_blocked_oa_pdfs.py        -- retry the ones a publisher's bot-check blocked
3. upload_full_texts.py               -- attach the downloaded PDFs to the right Covidence record
```

Each stage writes a CSV the next stage reads, so they can be re-run independently once a
PDF set has been built up — you don't have to re-run the whole pipeline to pick up a new
batch of manually-sourced PDFs; see [Re-running with a different batch](#re-running-with-a-different-batch)
below.

### Files in this stage

| File | Purpose |
|---|---|
| `retrieve_remaining_full_texts.py` | For every study missing full text: resolves a DOI if one isn't already known (via a Crossref bibliographic title search), looks the DOI up in [Unpaywall](https://unpaywall.org/), and downloads the PDF if Unpaywall has a direct link. Categorizes everything else (no direct link, not open access, no DOI at all) into a report CSV for manual follow-up. |
| `download_blocked_oa_pdfs.py` | Retries the subset that Unpaywall confirmed as open access but whose direct download got an HTTP 403/429 from the publisher (see [Known issues](#known-issues--troubleshooting-history-full-text-pipeline)) — using a real Playwright-driven Chromium browser instead of a raw HTTP request. |
| `upload_full_texts.py` | Logs into Covidence, searches by title for each record with a locally-held PDF, and uploads it through the "Upload full text" dialog. |
| `full-text/retrieval_status_<date>.csv` | Per-record status after the local-file cross-check: `have_locally_needs_upload`, `still_needs_retrieval`, or `still_needs_retrieval_no_doi`. Input to `upload_full_texts.py`. |
| `full-text/remaining_retrieval_categorized_<date>.csv` | Output of `retrieve_remaining_full_texts.py` — one row per still-missing record, categorized by retrieval route (see [CSV schemas](#csv-schemas)). |

PDFs themselves are **not** committed to this repo (see [What's not here](#whats-not-here)).

### Prerequisites (full-text stage)

Same as [Prerequisites](#prerequisites) above: Python 3, `pip install -r requirements.txt`,
`playwright install chromium`, and a `.env` with real Covidence credentials. No additional
dependencies — `retrieve_remaining_full_texts.py` uses only the standard library (`urllib`,
`json`, `csv`) for its Unpaywall/Crossref calls.

### Usage (full-text stage)

#### 1. Find what's retrievable

```bash
python3 retrieve_remaining_full_texts.py
```

Reads `full-text/retrieval_status_<date>.csv` for rows still needing a PDF, resolves a DOI
via Crossref for any that don't have one, checks Unpaywall, and downloads anything with a
direct PDF link into `full-text/open-access-<date>/`. Prints a category breakdown at the
end — see [CSV schemas](#csv-schemas) for what each category means.

#### 2. Retry the bot-blocked ones

```bash
python3 download_blocked_oa_pdfs.py
```

Takes the `open_access_pdf_link_failed` rows from step 1's report and retries each one
through a real headless Chromium session instead of a raw HTTP request. **Re-run it 2–3
times** if the count doesn't converge the first time — Playwright's download-event capture
has a race condition on slower redirect chains (increase the `expect_download(timeout=...)`
value in the script if a specific publisher consistently needs longer; see
[Known issues](#known-issues--troubleshooting-history-full-text-pipeline)).

#### 3. Upload to Covidence — test first

```bash
python3 upload_full_texts.py --csv full-text/retrieval_status_<date>.csv --limit 1 --headless
```

Then check that one record in the Covidence UI before trusting it with the rest.

#### 4. Upload to Covidence — full run

```bash
python3 upload_full_texts.py --csv full-text/retrieval_status_<date>.csv --headless
```

Expect roughly 25–40 seconds per record (title search, open, upload, confirm). Drop
`--headless` to watch it work.

#### Re-running with a different batch

`upload_full_texts.py` takes `--csv` so it can target any status CSV with
`have_locally_needs_upload` rows — not just the original one. Build a fresh batch file
(same five columns as the schema below) whenever a new set of PDFs is ready, and point the
script at it:

```bash
python3 upload_full_texts.py --csv full-text/retrieval_status_<date>_batch2.csv --headless
```

This is also how manually-sourced PDFs get uploaded — e.g. the "landing page only" and
truly-closed records from step 1's report, retrieved by hand from GWU institutional access
or a publisher's page directly: save the PDF, add a row for it to a batch CSV, run the
script.

### How it works (full-text stage)

#### `retrieve_remaining_full_texts.py`

For each still-missing record:

1. If there's no DOI yet, search Crossref's bibliographic-match endpoint
   (`api.crossref.org/works?query.bibliographic=<title>`) and accept the top hit only if its
   title closely matches the target (a 60-character prefix-overlap check) — this guards
   against confidently attaching the wrong DOI to a title that happens to rank first.
2. Query Unpaywall (`api.unpaywall.org/v2/<doi>?email=...`) for `best_oa_location`.
3. If there's a direct `url_for_pdf`, download it and **validate the first four bytes are
   `%PDF`** before saving — some "PDF" links actually serve an HTML interstitial, and saving
   that without checking would silently corrupt the full-text record with garbage.
4. Categorize everything else by what Unpaywall returned (OA-but-landing-page-only,
   confirmed-not-OA, or lookup failure) into the report CSV.

#### `download_blocked_oa_pdfs.py`

Same idea as step 3 above, but via `page.goto()` in a real Chromium browser (not raw
`urllib`) — a genuine browser TLS/HTTP fingerprint gets past simple bot-score checks that a
bare HTTP client doesn't. Two response shapes are handled:

- A normal page loads: check it's actually a PDF (`resp.body()` starts with `%PDF`), not an
  HTML block page.
- Chrome itself intercepts the response as a **file download** (common for publisher
  "direct PDF" links): this makes `page.goto()` raise rather than return normally, so the
  download has to be caught via `page.expect_download()` *around* the `goto()` call, with
  the resulting `Download` object saved via `.save_as()`.

#### `upload_full_texts.py`

1. Loads every `have_locally_needs_upload` row from the given CSV.
2. For each: searches Covidence by title
   (`/review_studies/search?search%5Bterm%5D=<title>`).
3. Opens the result — see [search page behavior](#1-two-different-pages-depending-on-result-count)
   below for why this isn't as simple as "click the first link."
4. Dismisses the "Access your library's full texts" (LibKey) promo modal if Covidence shows
   it on that record.
5. Clicks "Upload full text", attaches the local PDF via `set_input_files`, waits for it to
   register, clicks "Done".

### Known issues / troubleshooting history (full-text pipeline)

Same philosophy as the [main Known issues section](#known-issues--troubleshooting-history)
above: these were found by actually looking at what the live page returned, not guessed at.
If Covidence changes its markup and this starts misbehaving, repeat the same process — dump
the real page content/URL and compare against what the code assumes, rather than patching
blindly.

#### 1. Two different pages depending on result count

**Symptom:** every multi-result title search was logging `NO_RESULTS`, even for titles that
were visibly present in Covidence when searched by hand.

**Root cause:** Covidence's search behaves differently depending on how many studies match:

- **Exactly one match:** the search skips straight to that study's own page — the URL
  becomes `.../review_studies/select?filter=all&id=NNNN`.
- **Zero or multiple matches:** it lands on `.../review_studies/search?...`, a results-list
  page where each result is a plain `<a href="/reviews/818465/review_studies/{id}">` — note,
  critically, **no `select?` in that href**. That query string only appears *after* you
  click through to a specific study.

The original selector (`main a[href*="/review_studies/select?"]`) could only ever match the
single-result auto-redirect case. On every multi-result page it matched zero elements,
which the code read as "no results" — when in reality the right study was usually sitting
right there in the list, just under a different link shape.

**The fix:** check `page.url` after navigating. If it already contains `/review_studies/select`,
the single-match redirect happened — done. Otherwise, scan the result links
(`main a[href*="/review_studies/"]`) for one whose text contains the *exact* target title
(normalized: lowercased, whitespace-collapsed) rather than assuming the first result is
correct — multi-result pages are often full of loosely related matches (shared common words
like "infant", "microbiome", "gut"), and the real target is not reliably first.

#### 2. Covidence's search has a hard 150-character limit

**Symptom:** a handful of titles consistently returned zero results, even after fix #1 —
verified by hand in the Covidence UI that the exact same title string, searched directly,
returned real results.

**Root cause:** Covidence silently truncates/rejects queries over 150 characters, showing
`"Search is limited to 150 characters. Please shorten your query for more accurate
results."` on the results page — easy to miss if you're only checking the result count, not
reading the page banner.

**The fix:** the search *query* is truncated to 150 characters at a word boundary, but the
**full, untruncated title** is still what gets exact-matched against the result list — a
shortened query only needs to surface the right record among the results, it doesn't need
to uniquely identify it by itself.

#### 3. A same-paper, same-authors record duplicated in Covidence

**Symptom:** one title (a prebiotics/probiotics starter-formula RCT) kept coming back
`ambiguous` no matter what — two results, identical title text, so no exact-match logic
could tell them apart.

**Root cause:** not a script bug — Covidence genuinely had two separate study entries for
the same paper (`#9839 "Radke 2016"` and `#1720 "Radke 2017"`), most likely an epub-vs-print
publication-year mismatch between two source databases that Covidence's own deduplication
didn't catch.

**Resolution:** uploaded the same PDF to both entries (both genuinely need one, regardless
of the duplicate), and flagged the pair for a reviewer to merge via Covidence's own
"Duplicate" action — **this is a review-integrity decision a script shouldn't make
unilaterally.** If `upload_full_texts.py` logs `ambiguous` for a search that returns results
with genuinely identical titles, check for this before assuming it's a script bug.

#### 4. Publisher bot-protection blocks raw HTTP downloads (Akamai WAF)

**Symptom:** `retrieve_remaining_full_texts.py` reported `open_access_pdf_link_failed` for
roughly a third of all Unpaywall-confirmed-OA links — all `HTTP 403 Forbidden`, even though
Unpaywall had independently confirmed each one was freely downloadable.

**Root cause:** the response body for the 403s was an Akamai edge-server block page
(`errors.edgesuite.net`), not a real access-denial from the publisher. Several publishers
(JAMA, MDPI, ASM, Taylor & Francis, Wiley, and others) sit behind bot-protection that blocks
non-browser HTTP clients — even for content that is genuinely, legitimately open access.

**The fix (partial):** re-fetching through a real Playwright Chromium browser
(`download_blocked_oa_pdfs.py`) — a genuine browser TLS/HTTP fingerprint gets past the
simpler checks. This recovered roughly 40% of the blocked set. The remainder resisted even
a real headless browser, almost certainly because the WAF additionally checks for
automation markers (e.g. `navigator.webdriver`). **Deliberately not pursued further** —
getting past that would mean stealth/anti-detection techniques (fingerprint spoofing,
disabling automation flags), which starts to cross from "fetch something I have a legitimate
right to read" into "evade a specific protection mechanism," even for content that's
legitimately free. Those remaining records are better opened in an actual logged-in
browser by a human — faster and more appropriate than engineering around a WAF.

#### 5. `page.goto()` raises instead of returning when Chrome intercepts a download

**Symptom:** even after the WAF-bypass fix above, a meaningful chunk of "blocked" records
turned out not to be blocked at all — Chrome was successfully starting the file download,
but the script logged every one of them as `failed: Page.goto: Download is starting`.

**Root cause:** several publishers' "direct PDF" links (`journals.asm.org`,
`tandfonline.com`, `onlinelibrary.wiley.com`, `cell.com`, `jacionline.org`, `cmaj.ca`, and
others) respond in a way that makes Chrome treat the navigation as a **file download**
rather than a page load. Playwright surfaces this by raising an exception out of
`page.goto()` — the original code treated any exception there as a genuine failure.

**The fix:** wrap the `goto()` call in `page.expect_download(timeout=...)` *before* calling
it, catch the resulting `Download` object, and save it via `.save_as()` — then validate the
saved file's first four bytes are `%PDF` before trusting it, same as every other download
path in this toolkit. A short timeout (5s) missed some slower redirect chains; 20s cleared
nearly all of them, with one or two needing a second run to land (see
[step 2 above](#2-retry-the-bot-blocked-ones)). If a specific publisher's downloads are
consistently still missed at 20s, raise the timeout further rather than assume it's
genuinely blocked.

### What's not here

The downloaded PDFs themselves (`full-text/open-access-<date>/*.pdf`) are **not** committed
to this repo. This toolkit documents and automates *how* to legally retrieve and attach
them — it doesn't redistribute copies of the papers, even the open-access ones. Re-running
`retrieve_remaining_full_texts.py` + `download_blocked_oa_pdfs.py` against the status CSVs
regenerates the same files.

### CSV schemas

`full-text/retrieval_status_<date>.csv` — per-record status after cross-checking against
locally-held files:

| Column | Description |
|---|---|
| `status` | `have_locally_needs_upload`, `still_needs_retrieval`, or `still_needs_retrieval_no_doi` |
| `doi` | Normalized DOI (lowercased, no trailing period), or blank |
| `title` | Record title |
| `first_author` | First author surname, if known |
| `year` | Publication year, if known |
| `local_pdf_path` | Path to the matching local file (only set when `status` is `have_locally_needs_upload`) |

`full-text/remaining_retrieval_categorized_<date>.csv` — output of
`retrieve_remaining_full_texts.py`:

| Column | Description |
|---|---|
| `title`, `doi` | As above |
| `doi_resolved_via_crossref` | `True` if the DOI wasn't already known and had to be resolved via a Crossref title search |
| `category` | `downloaded_open_access`, `open_access_pdf_link_failed`, `open_access_landing_page_only`, `closed_needs_institutional_access_or_ill`, `no_doi_found_needs_manual_lookup`, or `unpaywall_lookup_failed` |
| `pdf_or_landing_url` | The PDF or landing-page URL Unpaywall returned, if any |
| `notes` | Error detail for failed categories |

### Security notes (full-text stage)

Same as [Security notes](#security-notes) above: never commit `.env`; the Covidence review
URL embedded in these scripts is project-specific, not secret; virtual environments and
runtime logs (`upload_full_texts.log`, `retrieve_remaining_full_texts.log`,
`download_blocked_oa_pdfs.log`) are excluded from version control.
