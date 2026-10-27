"""
Fills Covidence's Quality Assessment (Custom Risk of Bias) judgements for a study from the
local "Section J: Risk of bias" block in extraction/20pct_sample_draft.md, instead of typing
each domain by hand through the browser.

!!! THIS SCRIPT WRITES REAL JUDGEMENTS ON THE LIVE, SHARED COVIDENCE REVIEW !!!
Read this whole docstring before running anything beyond --dry-run.

-----------------------------------------------------------------------------
Why this exists
-----------------------------------------------------------------------------
Doing study #1499's Data Extraction + Quality Assessment by hand via Claude-in-Chrome
browser-automation (22-23 Oct 2026) showed Quality Assessment was the expensive half: 12
domains, each a full click-cycle (expand panel -> Make/Edit judgement -> select radio -> type
reasoning -> Save -> screenshot to verify), plus every verification screenshot is a
vision-model call. This script separates judgment-forming (done once, locally, writing
Section J -- see extraction_pilot_3studies.md) from data-entry (this script, which is pure
transcription, no reasoning, no screenshots needed at all once confirmed).

-----------------------------------------------------------------------------
What's CONFIRMED (via live DOM inspection, 2026-10-23) vs NOT YET CONFIRMED
-----------------------------------------------------------------------------
Confirmed (inspected directly on study #1499, review 818465):
  - Quality Assessment page: https://app.covidence.org/studies/<study_id>/risk_of_bias_assessments
    Each domain is a `.panel` containing a `.panel-heading` with `a.title` (domain name text)
    and either `a.edit-judgement` (already judged) or `a.make-judgement` (not yet judged).
  - Clicking either opens `.editing-panel` with:
      - `input[type=radio][name=decision]`, id = "decision_" + judgment.lower().replace(" ","_")
        e.g. Moderate -> decision_moderate, No information -> decision_no_information,
        Some concerns -> decision_some_concerns, Not reported -> decision_not_reported,
        Yes -> decision_yes. Confirmed across all three scales used in this review
        (ROBINS-I: low/moderate/serious/critical/no_information; RoB 2: low/some_concerns/high;
        checklist: yes/no/not_reported).
      - `textarea[name=comments]` (class judgement_comments) for the reasoning text.
      - `button.save[type=submit]` (text "Save") and `a.cancel` (closes without saving).
  - A closed panel's `.actions.has-decision` div shows the CURRENT judgement label as plain
    text (e.g. "Moderate") when one exists -- used to detect already-filled vs conflicting
    vs empty before touching anything.
  - Resolving covidence_number -> study_id: the existing search mechanism (same URL pattern
    as vote_fulltext_decisions.py's search_and_open) returns result links of the form
    `/reviews/818465/review_studies/<study_id>` whose text starts with "#<covidence_number> -
    <title>" -- confirmed live for #1536 (Korpela 2018) resolving to study_id 1976367117.
  - The "Complete" button triggers a confirmation dialog ("We've noticed that you haven't
    assessed all domains...") whenever any of the 5 RoB2-or-ROBINS-I-whichever-doesn't-apply
    domains are left blank -- EXPECTED on every study (only one of the two tools ever
    applies), confirmed via "Confirm complete" button on #1499.

NOT yet confirmed -- this is the one real gap:
  - An actual WRITE (select radio + type + Save) has only been exercised manually through
    the browser UI (for #1499), never yet by this script. The read-only paths above (finding
    panels, reading existing judgement text, resolving study_id) are what --dry-run exercises
    and were confirmed working against #1499's already-complete assessment (every domain
    correctly detected as "already matches, skipping"). The write path itself needs its own
    first live test -- see "Required first step" below.

-----------------------------------------------------------------------------
Required first step -- do not skip
-----------------------------------------------------------------------------
    venv/bin/python3 fill_quality_assessment.py --dry-run --only-cns "#1499"
        Zero-risk rehearsal against the one study already fully assessed by hand. Every one
        of its 12 domains should report "already matches local draft -- skipping". If any
        domain reports a MISMATCH, something about the parsing or ID-mapping logic is wrong --
        fix it before trusting this on an unjudged study.

    venv/bin/python3 fill_quality_assessment.py --dry-run --only-cns "#1536"
        Rehearsal against the next calibration study -- confirms study_id resolution and
        Section J parsing for a study that doesn't have Section J written yet (expect
        "no Section J found for this study" until that's drafted).

    venv/bin/python3 fill_quality_assessment.py --only-cns "#1536" --limit-domains 1
        Once Section J exists locally for #1536: casts exactly ONE real domain judgement
        (the first one parsed), does not click Complete. Open that record in Covidence
        afterward and confirm the judgement + reasoning landed correctly before trusting
        the rest.

    venv/bin/python3 fill_quality_assessment.py --only-cns "#1536"
        Full run for one study: every domain in its local Section J, then Complete.

Setup (same as the rest of this project's scripts):
    venv/bin/python3 fill_quality_assessment.py ...
    (uses the existing .env -- COVID_ID / COVID_PASSWORD; --env-file for a second reviewer)
"""
import argparse
import csv
import logging
import os
import re
import sys
import urllib.parse

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

SIGN_IN_URL = "https://app.covidence.org"
REVIEW_ID = "818465"
DRAFT_MD = "extraction/20pct_sample_draft.md"
LOG_DIR = "fill_qa_logs"
PROGRESS_CSV = "extraction/_volume_progress.csv"

CN_PATTERN = re.compile(r"^#(\d+)")
STUDY_ID_PATTERN = re.compile(r"/review_studies/(\d+)")

# The only judgment words this review's three scales use. A table row is only treated as a
# real (domain, judgment, reasoning) triple if its middle column is exactly one of these --
# this is what lets one regex pass over Section J safely skip header rows, separator rows,
# and any left-blank template rows (e.g. the non-applicable RoB2 table on an observational
# study) without needing to track which sub-table a row belongs to.
KNOWN_JUDGMENTS = [
    "Low", "Moderate", "Serious", "Critical", "No information",
    "Some concerns", "High",
    "Yes", "No", "Not reported",
]

# Domain names unique to each tool -- used to infer which tool a study's Section J is using
# (from whichever domains were actually parsed) and, critically, to disambiguate
# "Selection of the reported result", the one domain name both ROBINS-I and RoB 2 share
# verbatim. Confirmed live 2026-10-23: a plain substring match against domain_name alone
# found the *RoB2* (unjudged) copy of that heading first, not the ROBINS-I (judged) one,
# because RoB2's domains render above ROBINS-I's on the page.
ROBINS_I_ONLY_DOMAINS = {
    "Confounding", "Selection of participants", "Classification of exposures",
    "Deviations from intended exposures", "Missing data", "Measurement of outcomes",
}
ROB2_ONLY_DOMAINS = {
    "Randomization process", "Deviations from intended interventions",
    "Missing outcome data", "Measurement of the outcome",
}
CHECKLIST_DOMAINS = {
    "Sample collection and storage method reported", "DNA extraction method reported",
    "Sequencing depth reported", "Negative/positive contamination controls reported",
    "Compositional-data handling reported",
}

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("fill_quality_assessment.log", mode="a")],
)
logger = logging.getLogger("fill_qa")


def decision_id(judgment: str) -> str:
    return "decision_" + judgment.strip().lower().replace(" ", "_")


def parse_section_j(md_path: str, covidence_number: str) -> list[tuple[str, str, str]]:
    """Returns [(domain_name, judgment, reasoning), ...] for one study's Section J block,
    or [] if that study has no Section J yet. Raises ValueError if the study heading itself
    isn't found at all (distinct from "found but no Section J written")."""
    with open(md_path, encoding="utf-8") as f:
        text = f.read()

    cn_digits = covidence_number.lstrip("#")
    study_heading = re.search(rf"^## #{cn_digits}\b.*$", text, re.MULTILINE)
    if not study_heading:
        raise ValueError(f"No '## #{cn_digits} ...' heading found in {md_path}")

    next_heading = re.search(r"^## #\d+", text[study_heading.end():], re.MULTILINE)
    study_block = text[study_heading.end():study_heading.end() + next_heading.start()] if next_heading \
        else text[study_heading.end():]

    section_j = re.search(r"^### J\. Risk of bias\s*$", study_block, re.MULTILINE)
    if not section_j:
        return []

    next_section = re.search(r"^(### |---)", study_block[section_j.end():], re.MULTILINE)
    j_block = study_block[section_j.end():section_j.end() + next_section.start()] if next_section \
        else study_block[section_j.end():]

    judgment_alt = "|".join(re.escape(j) for j in sorted(KNOWN_JUDGMENTS, key=len, reverse=True))
    row_pattern = re.compile(
        rf"^\|\s*([^|]+?)\s*\|\s*({judgment_alt})\s*\|\s*(.+?)\s*\|\s*$", re.MULTILINE
    )
    results = []
    for m in row_pattern.finditer(j_block):
        domain, judgment, reasoning = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        if domain.lower() in ("domain", "field"):  # header row
            continue
        results.append((domain, judgment, reasoning))
    return results


def login(page: Page) -> None:
    page.goto(SIGN_IN_URL, timeout=60000)
    page.fill('#session_email', os.environ["COVID_ID"])
    page.fill('#session_password', os.environ["COVID_PASSWORD"])
    page.click('input[name="commit"]')
    page.wait_for_load_state("networkidle", timeout=60000)
    page.wait_for_timeout(1500)
    if "sign in" in page.inner_text("body").lower():
        save_diagnostics(page, "login_failed")
        raise RuntimeError(
            "Login does not appear to have succeeded. Diagnostics saved as "
            "login_failed.png/.txt -- check COVID_ID/COVID_PASSWORD in the credentials file."
        )


def find_study_id(page: Page, title: str, expected_cn: str) -> str | None:
    """Resolves covidence_number -> Covidence's internal study_id via the same search
    mechanism vote_fulltext_decisions.py uses, but just reads the id out of the result
    link's href instead of clicking through -- one round trip instead of two.

    Two genuinely different URL shapes carry the id, confirmed live 2026-10-24:
      - A single unambiguous match redirects straight to a study page whose id is a QUERY
        STRING parameter, not a path segment -- e.g.
        ".../review_studies/included?filter=all&id=1976367261" (seen for an exact-title
        match) or ".../review_studies/select?filter=all&id=<n>" (vote_fulltext_decisions.py's
        confirmed pattern for the same single-match case on a different page). The earlier
        version of this function checked for this case but then did nothing with it (a
        leftover no-op), silently falling through to the link-scan below, which finds zero
        links on this kind of page (the match IS the page, there's nothing to click into) and
        incorrectly reports "not found" even though the id was sitting right in the URL.
      - Multiple/ambiguous matches land on a search RESULTS LIST page instead, whose links
        carry the id as a PATH segment -- ".../review_studies/<digits>" -- handled by the
        link-scanning loop below, matching by the "#<covidence_number>" prefix in each link's
        text (same approach as vote_fulltext_decisions.py's search_and_open).

    A "/" in the title breaks Covidence's search (confirmed live 2026-10-27 on #1215,
    "...short/branched chain fatty acids...": a query containing it returns either an
    explicit "No results found", or -- more dangerously -- a redirect that LOOKS like the
    single-match case (no "/search" in the resulting URL) but is actually Covidence falling
    back to the default-selected record in some other filtered list (e.g. "Irrelevant"),
    unrelated to the real study. Stripped out below before building the query.

    Because that fallback redirect is indistinguishable from a genuine single-match redirect
    by URL shape alone, the id it carries is verified against expected_cn in the page body
    before being trusted -- a wrong-list fallback won't contain it and falls through to the
    link-scan below instead (which correctly reports not-found rather than returning the
    id of an unrelated study)."""
    query = title.replace("/", " ")
    query = query if len(query) <= 150 else query[:150].rsplit(" ", 1)[0]
    url = (f"https://app.covidence.org/reviews/{REVIEW_ID}/review_studies/search"
           f"?search%5Bterm%5D={urllib.parse.quote(query)}")
    page.goto(url, timeout=60000)
    page.wait_for_load_state("networkidle", timeout=60000)

    if "/search" not in page.url and expected_cn in page.inner_text("body"):
        qs_match = re.search(r"[?&]id=(\d+)", page.url)
        if qs_match:
            return qs_match.group(1)
        path_match = STUDY_ID_PATTERN.search(page.url)
        if path_match:
            return path_match.group(1)

    links = page.locator('main a[href*="/review_studies/"]')
    count = links.count()
    if count == 0:
        return None
    hrefs = [links.nth(i).get_attribute("href") or "" for i in range(count)]
    texts = links.all_inner_texts()
    for href, text in zip(hrefs, texts):
        cn_match = CN_PATTERN.match(text.strip())
        if cn_match and f"#{cn_match.group(1)}" == expected_cn:
            id_match = STUDY_ID_PATTERN.search(href)
            if id_match:
                return id_match.group(1)
    return None


def save_diagnostics(page: Page, tag: str) -> None:
    safe_tag = re.sub(r"[^A-Za-z0-9_-]", "_", tag)
    page.screenshot(path=os.path.join(LOG_DIR, f"{safe_tag}.png"), full_page=True)
    with open(os.path.join(LOG_DIR, f"{safe_tag}.txt"), "w", encoding="utf-8") as f:
        f.write(page.inner_text("body"))


def infer_tool(rows: list[tuple[str, str, str]]) -> str | None:
    """Infers which tool (ROBINS-I or RoB2) a study's parsed Section J rows belong to, from
    whichever tool-specific domain names are actually present. Returns None if only
    checklist domains were parsed (shouldn't happen in practice -- every study with a
    Section J should have at least one tool-specific domain too)."""
    domains = {d for d, _, _ in rows}
    if domains & ROBINS_I_ONLY_DOMAINS:
        return "ROBINS-I"
    if domains & ROB2_ONLY_DOMAINS:
        return "RoB2"
    return None


def find_panel(page: Page, domain_name: str, tool_hint: str | None = None):
    """Returns the Playwright locator for the .panel whose heading contains domain_name,
    or None. Domain names in this review's 17 domains are specific enough that a substring
    match against the panel heading (which is prefixed "ROBINS-I (...) -- " / "RoB2 (...) -- "
    / "Checklist -- ") is unambiguous -- EXCEPT "Selection of the reported result", which
    ROBINS-I and RoB2 both use verbatim. When domain_name isn't a checklist domain, this
    also requires the heading to contain tool_hint ("ROBINS-I" or "RoB2"), which resolves
    that one collision; pass tool_hint from infer_tool() on the study's parsed rows.

    NOTE: the outer "Custom Risk of Bias" wrapper also carries class "panel" (as
    "panel summary-view"), so iterating page.locator(".panel") and then querying each
    one's .panel-heading descendant is ambiguous -- the wrapper's own .panel-heading query
    matches all 17 nested domain headings at once (confirmed live, 2026-10-23: a Playwright
    strict-mode violation listing 18 .panel-heading matches under panel .first). Searching
    .panel-heading elements directly first, then walking up to the parent .panel, sidesteps
    this since each heading (picked via .nth(i)) is unambiguous even though the panels
    containing them are nested."""
    headings = page.locator(".panel-heading")
    count = headings.count()
    for i in range(count):
        h = headings.nth(i)
        text = h.inner_text()
        if domain_name not in text:
            continue
        if domain_name not in CHECKLIST_DOMAINS and tool_hint is not None and tool_hint not in text:
            continue
        return h.locator("xpath=..")
    return None


def get_existing_judgment(panel) -> str | None:
    """Reads the current judgement label off a closed panel's badge, or None if unjudged."""
    badge = panel.locator(".panel-heading .actions.has-decision")
    if badge.count() == 0:
        return None
    text = badge.inner_text().strip()
    return text if text else None


def fill_one_domain(page: Page, domain_name: str, judgment: str, reasoning: str,
                     dry_run: bool, tool_hint: str | None = None) -> tuple[str, str]:
    """Returns (status, detail). status: 'filled' | 'already_matches' | 'skipped_dry_run' |
    'conflict' | 'panel_not_found' | 'failed'."""
    panel = find_panel(page, domain_name, tool_hint)
    if panel is None:
        return "panel_not_found", f"no panel heading contains {domain_name!r}" + \
            (f" (with tool hint {tool_hint!r})" if tool_hint else "")

    existing = get_existing_judgment(panel)
    if existing is not None:
        if existing == judgment:
            return "already_matches", f"already {judgment!r}"
        return "conflict", f"Covidence shows {existing!r}, local draft says {judgment!r}"

    if dry_run:
        return "skipped_dry_run", f"would set {judgment!r}"

    # A closed panel's contents (including the make/edit-judgement link) exist in the DOM but
    # are CSS-hidden until the panel is expanded by clicking its a.title header -- confirmed
    # live 2026-10-23: Playwright's actionability check correctly refuses to click a
    # not-visible element (raw JS .click() during earlier manual DOM inspection bypassed this
    # check, which is why that testing didn't surface the issue). Click the title first,
    # unconditionally -- toggling an already-open panel closed-then-this-click-reopens would
    # be wrong, so only click if the panel isn't already open.
    if "open" not in (panel.get_attribute("class") or ""):
        panel.locator(".panel-heading a.title").click()
        page.wait_for_timeout(300)

    edit_link = panel.locator("a.edit-judgement, a.make-judgement")
    if edit_link.count() == 0:
        return "panel_not_found", "no edit-judgement/make-judgement link on this panel"
    edit_link.first.click()
    page.wait_for_selector(".editing-panel textarea[name=comments]", timeout=10000)

    # The <input type=radio> itself is display:none (confirmed live 2026-10-23: bounding_box
    # is None, so even .check(force=True) can't compute a click point -- force=True skips
    # actionability CHECKS, it doesn't make an unrendered element clickable). Each radio has
    # an immediately-preceding <label for="decision_x"> that IS the real, visibly-styled
    # clickable control; clicking it toggles the hidden input via native label/input
    # association, same as a real user would.
    radio_id = decision_id(judgment)
    label = page.locator(f'label[for="{radio_id}"]')
    if label.count() == 0:
        save_diagnostics(page, f"{domain_name[:30]}_label_not_found")
        return "failed", f"label[for={radio_id}] not found -- diagnostics saved"
    label.click()
    checked = page.locator(f"#{radio_id}").is_checked()
    if not checked:
        save_diagnostics(page, f"{domain_name[:30]}_radio_not_checked")
        return "failed", f"clicked label[for={radio_id}] but input is still not checked -- diagnostics saved"

    textarea = page.locator(".editing-panel textarea[name=comments]")
    textarea.fill(reasoning)

    save_btn = page.locator(".editing-panel button.save")
    save_btn.click()
    page.wait_for_timeout(600)
    return "filled", f"set {judgment!r}"


def complete_assessment(page: Page, dry_run: bool) -> tuple[str, str]:
    if dry_run:
        return "skipped_dry_run", ""
    complete_btn = page.get_by_role("button", name="Complete", exact=True)
    if complete_btn.count() == 0:
        return "already_complete", "no Complete button visible (likely already Completed)"
    complete_btn.first.click()
    page.wait_for_timeout(800)
    confirm_btn = page.get_by_role("button", name="Confirm complete")
    if confirm_btn.count() > 0:
        confirm_btn.first.click()
        page.wait_for_timeout(800)
    return "completed", ""


def process_one_study(page: Page, covidence_number: str, title: str, limit_domains: int | None,
                       dry_run: bool, no_complete: bool, draft_md: str = DRAFT_MD) -> dict:
    counts = {"filled": 0, "already_matches": 0, "skipped_dry_run": 0, "conflict": 0,
              "panel_not_found": 0, "failed": 0}
    try:
        rows = parse_section_j(draft_md, covidence_number)
    except ValueError as e:
        logger.error(f"{covidence_number}: {e}")
        return {"status": "no_heading", "counts": counts}

    if not rows:
        logger.warning(f"{covidence_number}: no Section J found in {draft_md} -- nothing to do")
        return {"status": "no_section_j", "counts": counts}

    tool_hint = infer_tool(rows)
    if tool_hint is None:
        logger.warning(f"{covidence_number}: could not infer ROBINS-I vs RoB2 from parsed domains -- "
                        f"'Selection of the reported result' may match the wrong panel if present")

    study_id = find_study_id(page, title, covidence_number)
    if study_id is None:
        logger.error(f"{covidence_number}: could not resolve study_id via search")
        save_diagnostics(page, f"{covidence_number}_study_id_not_found")
        return {"status": "study_id_not_found", "counts": counts}
    logger.info(f"{covidence_number}: resolved study_id={study_id}, {len(rows)} domain(s) in Section J")

    qa_url = f"https://app.covidence.org/studies/{study_id}/risk_of_bias_assessments"
    page.goto(qa_url, timeout=60000)
    page.wait_for_load_state("networkidle", timeout=60000)

    filled_this_run = 0
    for domain_name, judgment, reasoning in rows:
        if limit_domains is not None and filled_this_run >= limit_domains:
            logger.info(f"{covidence_number}: --limit-domains {limit_domains} reached, stopping")
            break
        status, detail = fill_one_domain(page, domain_name, judgment, reasoning, dry_run, tool_hint)
        counts[status] = counts.get(status, 0) + 1
        logger.info(f"{covidence_number}: {domain_name!r} -> {status} ({detail})")
        if status == "filled":
            filled_this_run += 1
        if status == "conflict":
            logger.error(
                f"{covidence_number}: STOPPING this study -- {domain_name!r} conflict ({detail}). "
                f"Needs a human look before deciding whether to overwrite."
            )
            return {"status": "stopped_on_conflict", "counts": counts}
        if status == "failed":
            logger.error(f"{covidence_number}: STOPPING this study -- {domain_name!r} failed ({detail}).")
            return {"status": "stopped_on_failure", "counts": counts}

    all_filled_or_matched = all(
        counts.get(s, 0) == 0 for s in ("panel_not_found", "conflict", "failed")
    )
    if not no_complete and all_filled_or_matched and (limit_domains is None):
        status, detail = complete_assessment(page, dry_run)
        logger.info(f"{covidence_number}: complete_assessment -> {status} {detail}")

    return {"status": "done", "counts": counts}


MANIFEST_CSV = "extraction/_manifest.csv"


def load_titles(manifest_path: str) -> dict[str, str]:
    """covidence_number -> actual paper title, read from the manifest (NOT from the local
    draft's section headings, which only carry an author-year-country label like
    "Wopereis 2018 (Australia/Singapore/England/Ireland)" -- confirmed live 2026-10-24 that
    using that label as a search query can fail for common author surnames: "Wopereis" alone
    matched 286 loosely-related results and the real record (#1643) wasn't reliably among the
    ones actually inspected, where a rarer surname like "Korpela" or "Claassen-Weitz" happened
    to narrow the search enough to still work by luck."""
    titles = {}
    with open(manifest_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            titles[row["covidence_number"]] = row["title"]
    return titles


def run(only_cns: str | None, limit_domains: int | None, headless: bool, dry_run: bool,
        no_complete: bool, draft_md: str = DRAFT_MD) -> None:
    with open(draft_md, encoding="utf-8") as f:
        text = f.read()
    headings = re.findall(r"^## (#\d+) — (.+)$", text, re.MULTILINE)
    titles = load_titles(MANIFEST_CSV)
    studies = []
    for cn, heading_label in headings:
        if cn not in titles:
            logger.warning(f"{cn}: no entry in {MANIFEST_CSV} -- falling back to heading label {heading_label!r} as the search query")
        studies.append((cn, titles.get(cn, heading_label)))

    if only_cns:
        wanted = {c.strip() for c in only_cns.split(",") if c.strip()}
        studies = [(cn, title) for cn, title in studies if cn in wanted]
        missing = wanted - {cn for cn, _ in studies}
        if missing:
            logger.warning(f"--only-cns: {sorted(missing)} not found as '## #N -- ...' headings in {draft_md}")

    logger.info(f"Processing {len(studies)} studies from {draft_md}" + (" [DRY RUN]" if dry_run else ""))

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.set_default_timeout(25000)
        page.set_default_navigation_timeout(25000)
        try:
            login(page)
            for cn, title in studies:
                try:
                    result = process_one_study(page, cn, title, limit_domains, dry_run, no_complete, draft_md)
                    logger.info(f"{cn}: {result['status']} -- {result['counts']}")
                except Exception as e:
                    logger.error(f"{cn}: UNEXPECTED EXCEPTION -- {type(e).__name__}: {e}")
                    try:
                        save_diagnostics(page, f"{cn}_exception")
                    except Exception:
                        pass
        finally:
            browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fill Covidence Quality Assessment judgements from local Section J"
    )
    parser.add_argument("--only-cns", default=None,
                         help="Comma-separated covidence numbers to process, e.g. '#1499,#1536'. "
                              "Default: every study with a '## #N -- ...' heading in the draft file.")
    parser.add_argument("--limit-domains", type=int, default=None,
                         help="Cap how many domain judgements to actually write per study this run "
                              "(does not count already_matches/skipped). Omit for no cap. When set, "
                              "Complete is never clicked (the study is left in-progress on purpose).")
    parser.add_argument("--dry-run", action="store_true",
                         help="Navigate, parse, and compare only -- writes nothing, clicks nothing "
                              "except panel expand/collapse (no Save, no Complete).")
    parser.add_argument("--no-complete", action="store_true",
                         help="Never click Complete, even after every domain is filled/matches.")
    parser.add_argument("--headless", action="store_true", default=True)
    parser.add_argument("--no-headless", dest="headless", action="store_false")
    parser.add_argument("--env-file", default=".env")
    parser.add_argument("--draft-md", default=DRAFT_MD,
                         help=f"Path to the markdown file containing '## #N -- ...' headings and "
                              f"'### J. Risk of bias' blocks. Default: {DRAFT_MD} (the 20%% "
                              f"calibration sample). Pass a different file for volume work on other "
                              f"studies, e.g. extraction/volume_qa_draft.md.")
    args = parser.parse_args()

    load_dotenv(args.env_file)
    if "COVID_ID" not in os.environ or "COVID_PASSWORD" not in os.environ:
        print(f"Missing COVID_ID / COVID_PASSWORD in {args.env_file}.", file=sys.stderr)
        sys.exit(1)

    run(args.only_cns, args.limit_domains, args.headless, args.dry_run, args.no_complete, args.draft_md)
