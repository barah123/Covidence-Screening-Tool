"""
Casts the 211 full-text-review decisions in
full-text/full_text_screening_decisions_2026-10-09.csv into Covidence's Full Text
Review voting queue (review 818465, "microbiome_methodologies").

!!! THIS SCRIPT CASTS REAL VOTES ON THE LIVE, SHARED COVIDENCE REVIEW !!!
Read this whole docstring before running anything beyond --dry-run.

-----------------------------------------------------------------------------
What's CONFIRMED (via read-only browser reconnaissance, 2026-10-10) vs. ASSUMED
-----------------------------------------------------------------------------
Confirmed:
  - Searching by title (same mechanism as replace_wrong_full_texts.py's
    search_and_open) lands directly on a single-record page
    (".../review_studies/select?filter=all&id=<n>") when there's exactly one
    match, showing exactly one card with its Include/Exclude buttons.
  - The buttons use the SAME component as the title/abstract screening stage:
    selector '[data-pendo-key="vote-button"]' inside
    '[class*="StudyListItem-module__card"]', and here they are literally
    labeled "Include" / "Exclude" (not Yes/No/Maybe).
  - Each card's Covidence study number appears as "#<digits>" at the very
    start of its text, matching the covidence_number column in the decisions
    CSV exactly (e.g. card text starts "#632 - Chen 2024...", CSV has "#632").

NOT confirmed -- this is the one real unknown:
  - What happens in the DOM right after clicking "Exclude". This review has a
    10-reason Full Text Exclusion Reasons list configured (set up earlier in
    this project), so Covidence almost certainly requires picking one before
    the exclusion commits -- but a live test click was correctly blocked by
    the auto-mode permission classifier as a write action on the shared
    review, so the exact UI (dialog? inline buttons? dropdown?) was never
    actually seen.

Because of that gap, click_exclude_with_reason() below tries several
plausible places Covidence might render the reason picker, matching by the
reason's exact text. ALWAYS, win or lose, it saves a screenshot and the full
page text to vote_fulltext_logs/ so you can see exactly what happened. If no
strategy finds a confident match, it stops the whole run rather than
guessing -- check the saved screenshot/text, and either adjust
REASON_CLICK_STRATEGIES below or finish that one vote by hand in Covidence
before re-running.

-----------------------------------------------------------------------------
Required first step -- do not skip
-----------------------------------------------------------------------------
    python3 vote_fulltext_decisions.py --dry-run
        Zero-risk rehearsal: logs in, searches for all 211 titles, confirms
        each lands on the expected covidence_number, but clicks nothing.
        Fix any "NOT FOUND" / "AMBIGUOUS" / "MISMATCH" rows this reports
        before going further.

    python3 vote_fulltext_decisions.py --limit 1
        Casts exactly one real vote (whichever decision is first in the CSV
        that --dry-run confirmed resolves cleanly). Open that record in
        Covidence's web UI afterward (its "History" tab shows exactly what
        was recorded) and confirm it's correct.

    python3 vote_fulltext_decisions.py --limit 1 --only-exclude
        Same, but forces the first row to try is an Exclude decision, since
        that's the code path with the real unknown. Check the saved
        screenshot in vote_fulltext_logs/ and the record's History tab in
        Covidence before trusting the reason that got selected.

    python3 vote_fulltext_decisions.py
        Full run, once you trust both paths.

Setup (same as the rest of this project's scripts):
    venv/bin/python3 vote_fulltext_decisions.py ...
    (uses the existing .env -- COVID_ID / COVID_PASSWORD)
"""
import argparse
import csv
import logging
import os
import re
import sys
import time
import urllib.parse

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

# Credentials are loaded from --env-file (default .env) inside __main__ below,
# not here at import time -- this lets a second reviewer (their own Covidence
# login) point at their own credentials file (e.g. .env.alaa) without
# touching or being overwritten by anyone else's .env in the same project
# checkout. Covidence tracks each reviewer's vote separately, so running
# this script again under a different login records that reviewer's own
# independent vote on each study -- it does not overwrite the first
# reviewer's vote or conflict with it, provided the decisions agree.

SIGN_IN_URL = "https://app.covidence.org"
REVIEW_ID = "818465"
DECISIONS_CSV = "full-text/full_text_screening_decisions_2026-10-09.csv"
LOG_DIR = "vote_fulltext_logs"

# NOTE: must be an EXACT class-token match (CSS `~=`), not a substring match
# (`*=`). A substring match also matches the card's own nested child wrapper
# "...StudyListItem-module__cardContent" (its class literally starts with
# "...StudyListItem-module__card"), which is the SAME single study rendered
# twice over -- confirmed live 2026-10-10: a genuinely single-match page
# always showed "2 cards" under the old `*=` selector, not a real ambiguity.
CARD_SELECTOR = '[class~="webpack-pages-StudyList-StudyListItem-StudyListItem-module__card"]'
VOTE_BUTTON_SELECTOR = '[data-pendo-key="vote-button"]'
CN_PATTERN = re.compile(r"^#(\d+)")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("vote_fulltext_decisions.log", mode="a")],
)
logger = logging.getLogger("vote_fulltext")


def load_decisions(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def login(page: Page) -> None:
    page.goto(SIGN_IN_URL, timeout=60000)
    page.fill('#session_email', os.environ["COVID_ID"])
    page.fill('#session_password', os.environ["COVID_PASSWORD"])
    page.click('input[name="commit"]')
    page.wait_for_load_state("networkidle", timeout=60000)


def norm_title(t: str) -> str:
    return re.sub(r"\s+", " ", t.strip().lower())


def search_and_open(page: Page, title: str, expected_cn: str) -> tuple[str, str]:
    """Returns (status, detail). status: 'opened' | 'no_results' | 'ambiguous'.

    Covidence's search only auto-redirects straight to a single record
    (URL contains "/review_studies/select") when there's exactly one match
    across the whole database. Otherwise it lands on a "Search results"
    list page using DIFFERENT markup than CARD_SELECTOR (a plain list of
    `main a[href*="/review_studies/"]` links).

    This review has a confirmed handful of DOI-duplicate record pairs (same
    paper imported twice under two different covidence numbers, e.g.
    #1720/#9839, #1948/#5430) where both copies carry an identical or
    near-identical title -- plain normalized-title matching can't tell them
    apart and reports a false "ambiguous". Each list link's text starts with
    "#<number> - Name Year" exactly like a single-record card does (same
    CN_PATTERN), so matching on the expected covidence_number directly,
    rather than on title text, resolves that cleanly. Title text is kept
    only as a secondary sanity check once a number match is found.
    """
    query = title if len(title) <= 150 else title[:150].rsplit(" ", 1)[0]
    url = (f"https://app.covidence.org/reviews/{REVIEW_ID}/review_studies/search"
           f"?search%5Bterm%5D={urllib.parse.quote(query)}")
    page.goto(url, timeout=60000)
    page.wait_for_load_state("networkidle", timeout=60000)

    if "/review_studies/select" in page.url:
        return "opened", page.url

    links = page.locator('main a[href*="/review_studies/"]')
    count = links.count()
    if count == 0:
        return "no_results", ""

    # A loose/common-word title can pull back dozens-to-hundreds of results
    # (Covidence's search isn't exact-phrase). Fetching each link's text one
    # at a time via .nth(i).inner_text() is a separate round-trip per result
    # and got observed taking 15+ minutes on a single row with ~100+ results.
    # all_inner_texts() fetches everything in one batch instead.
    link_texts = links.all_inner_texts()

    cn_matches = [i for i, text in enumerate(link_texts) if CN_PATTERN.match(text.strip()) and
                  f"#{CN_PATTERN.match(text.strip()).group(1)}" == expected_cn]
    if len(cn_matches) == 1:
        match_index = cn_matches[0]
    elif len(cn_matches) > 1:
        return "ambiguous", f"{count} results, {expected_cn} appears more than once"
    else:
        # Fall back to normalized-title substring matching for the (so far
        # unseen) case where the expected number genuinely isn't in this
        # result page at all.
        target = norm_title(title)
        title_matches = [i for i, text in enumerate(link_texts) if target in norm_title(text)]
        if len(title_matches) == 0:
            return "ambiguous", f"{count} results, neither {expected_cn} nor the title text matched any of them"
        if len(title_matches) > 1:
            return "ambiguous", f"{count} results, {expected_cn} not found and title text matches {len(title_matches)} of them"
        match_index = title_matches[0]

    links.nth(match_index).click()
    page.wait_for_load_state("networkidle", timeout=60000)
    return "opened", page.url


def get_single_card(page: Page):
    cards = page.query_selector_all(CARD_SELECTOR)
    return cards[0] if len(cards) == 1 else None


def extract_cn(card) -> str | None:
    m = CN_PATTERN.match(card.inner_text().strip())
    return f"#{m.group(1)}" if m else None


def get_current_vote(card) -> str | None:
    """Returns 'Include', 'Exclude', or None (not yet voted).

    CONFIRMED live 2026-10-10: once a record has been voted, the button that
    is NOT the current vote gets relabeled "Change vote to include" / "Change
    vote to exclude", while the button matching the current vote keeps its
    plain "Include"/"Exclude" label. Re-clicking a vote that's already set is
    a no-op (no reason-picker reappears for Exclude), so this check has to
    happen BEFORE attempting any click, not just on failure.
    """
    buttons = card.query_selector_all(VOTE_BUTTON_SELECTOR)
    texts = [b.inner_text().strip() for b in buttons]
    if any(t == "Change vote to include" for t in texts):
        return "Exclude"
    if any(t == "Change vote to exclude" for t in texts):
        return "Include"
    return None


def save_diagnostics(page: Page, tag: str) -> None:
    safe_tag = re.sub(r"[^A-Za-z0-9_-]", "_", tag)
    page.screenshot(path=os.path.join(LOG_DIR, f"{safe_tag}.png"), full_page=True)
    with open(os.path.join(LOG_DIR, f"{safe_tag}.txt"), "w", encoding="utf-8") as f:
        f.write(page.inner_text("body"))


def click_include(page: Page, card) -> tuple[bool, str]:
    buttons = card.query_selector_all(VOTE_BUTTON_SELECTOR)
    for b in buttons:
        if b.inner_text().strip() == "Include":
            b.click(force=True)
            return True, ""
    return False, "Include button not found on card"


# Reasons exactly as configured in Covidence's Full Text Exclusion Reasons list
# for this review (set up earlier in this project) -- must match verbatim.
KNOWN_REASONS = [
    "Not a primary research article",
    "No breastfed-vs-formula-fed comparison",
    "Supplement/probiotic is the exposure",
    "Wrong population",
    "Clinical condition defines the cohort",
    "Animal, in vitro, ex vivo, or gut-simulator model",
    "No infant stool sample",
    "No sequencing-based profiling",
    "Virome/phageome/plasmidome only",
    "Duplicate report of an already-included cohort",
]


def click_exclude_with_reason(page: Page, card, cn: str, reason: str) -> tuple[bool, str]:
    """Clicks Exclude, then tries to select `reason` from whatever picker UI
    appears. Always saves diagnostics. Returns (ok, note)."""
    buttons = card.query_selector_all(VOTE_BUTTON_SELECTOR)
    exclude_btn = next((b for b in buttons if b.inner_text().strip() == "Exclude"), None)
    if exclude_btn is None:
        return False, "Exclude button not found on card"

    exclude_btn.click(force=True)
    page.wait_for_timeout(1200)
    save_diagnostics(page, f"{cn}_after_exclude_click")

    # CONFIRMED live 2026-10-10: the reason picker is a native HTML <select>
    # (each <option>'s value AND visible text is the FULL criterion string,
    # e.g. "No breastfed-vs-formula-fed comparison (feeding mode not
    # reported, or no actual between-group contrast; ...)" -- our `reason`
    # column is just the short prefix, so match by substring). You cannot
    # .click() an <option> (Playwright: "Element is not visible") -- it has
    # to go through select_option() on the <select> itself. The <select> is
    # likely visually replaced by custom-styled UI, so actionability checks
    # are bypassed with force=True since we've confirmed via diagnostics
    # that the element is genuinely there, just not a plain visible control.
    selects = page.locator("select")
    for i in range(selects.count()):
        sel = selects.nth(i)
        options = sel.locator("option")
        for j in range(options.count()):
            opt_text = options.nth(j).inner_text().strip()
            if reason.lower() in opt_text.lower():
                sel.select_option(label=opt_text, force=True)
                page.wait_for_timeout(800)
                save_diagnostics(page, f"{cn}_after_reason_click")
                _maybe_click_confirm(page)
                return True, f"select_option matched {opt_text[:60]!r}"

    # Fallback strategies, in case a different record ever renders the
    # picker differently (dialog, or inline clickable options/buttons).
    dialog = page.locator('[role="dialog"]')
    if dialog.count() > 0:
        opt = dialog.get_by_text(reason, exact=False)
        if opt.count() > 0:
            opt.first.click(force=True)
            page.wait_for_timeout(800)
            save_diagnostics(page, f"{cn}_after_reason_click")
            _maybe_click_confirm(page)
            return True, "selected reason inside dialog"

    for el in card.query_selector_all('button, [role="option"], [role="radio"], label, li'):
        try:
            txt = el.inner_text().strip()
        except Exception:
            continue
        if txt and reason.lower() in txt.lower():
            el.click(force=True)
            page.wait_for_timeout(800)
            save_diagnostics(page, f"{cn}_after_reason_click")
            _maybe_click_confirm(page)
            return True, "selected reason inline in card"

    return False, (
        f"Could not find a UI element matching reason {reason!r} after clicking Exclude. "
        f"Diagnostics saved as {cn}_after_exclude_click.png/.txt in {LOG_DIR}/ -- inspect "
        f"those, then either fix REASON_CLICK_STRATEGIES in this script or finish this one "
        f"vote by hand in Covidence before re-running."
    )


def _maybe_click_confirm(page: Page) -> None:
    for label in ("Confirm", "Save", "Apply", "Done"):
        btn = page.get_by_role("button", name=label, exact=True)
        if btn.count() > 0:
            btn.first.click(force=True)
            page.wait_for_timeout(500)
            return


def process_one(page: Page, row: dict, dry_run: bool) -> tuple[str, str]:
    """Returns (status, detail). status: 'voted' | 'skipped_dry_run' |
    'already_voted' | 'vote_conflict' | 'no_results' | 'ambiguous' |
    'cn_mismatch' | 'failed'."""
    cn = row["covidence_number"]
    title = row["title"]
    decision = row["decision"]
    reason = row.get("exclusion_reason", "").strip()

    logger.info(f"{cn}: starting (title search)...")
    status, detail = search_and_open(page, title, cn)
    if status != "opened":
        logger.warning(f"{cn}: search {status.upper()} for title {title[:70]!r} ({detail})")
        return status, detail

    card = get_single_card(page)
    if card is None:
        n = len(page.query_selector_all(CARD_SELECTOR))
        logger.warning(f"{cn}: landed on select page but card count is {n} (expected 1)")
        return "ambiguous", f"landed on select page but card count is {n}"

    actual_cn = extract_cn(card)
    if actual_cn != cn:
        logger.error(f"{cn}: MISMATCH -- landed on card {actual_cn!r} instead. NOT voting.")
        return "cn_mismatch", f"expected {cn}, got {actual_cn}"

    if dry_run:
        logger.info(f"{cn}: [dry-run] would vote {decision}" + (f" ({reason})" if decision == "Exclude" else ""))
        return "skipped_dry_run", ""

    current = get_current_vote(card)
    if current is not None:
        if current == decision:
            logger.info(f"{cn}: already voted {decision} -- skipping (no action needed)")
            return "already_voted", ""
        logger.error(f"{cn}: VOTE CONFLICT -- currently voted {current!r}, decision says {decision!r}. NOT touching.")
        return "vote_conflict", f"currently {current}, decision says {decision}"

    if decision == "Include":
        ok, note = click_include(page, card)
        if not ok:
            return "failed", note
        page.wait_for_timeout(500)
        save_diagnostics(page, f"{cn}_after_include")
        logger.info(f"{cn}: voted Include ({title[:70]!r})")
        return "voted", ""

    if decision == "Exclude":
        if not reason:
            return "failed", "decision is Exclude but exclusion_reason column is empty"
        ok, note = click_exclude_with_reason(page, card, cn, reason)
        if not ok:
            logger.error(f"{cn}: {note}")
            return "failed", note
        logger.info(f"{cn}: voted Exclude / {reason!r} ({title[:70]!r}) -- {note}")
        return "voted", note

    return "failed", f"unrecognized decision value {decision!r}"


def run(limit: int, headless: bool, dry_run: bool, only_exclude: bool) -> None:
    rows = load_decisions(DECISIONS_CSV)
    logger.info(f"Loaded {len(rows)} decisions from {DECISIONS_CSV}")

    if only_exclude:
        rows = [r for r in rows if r["decision"] == "Exclude"]
        logger.info(f"--only-exclude: filtered to {len(rows)} Exclude rows")

    counts = {"voted": 0, "skipped_dry_run": 0, "already_voted": 0, "vote_conflict": 0,
              "no_results": 0, "ambiguous": 0, "cn_mismatch": 0, "failed": 0}
    unresolved = []  # (cn, status, detail) for no_results/ambiguous/cn_mismatch -- not fatal, just skipped

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        # Hard ceiling on EVERY playwright action (navigation and the implicit
        # auto-wait on locator methods like .click()/.count()/.inner_text(),
        # which otherwise default to their own 30s each and can silently chain
        # into a long stall with nothing logged in between). 25s is generous
        # for this app but short enough that a genuine hang surfaces fast.
        page.set_default_timeout(25000)
        page.set_default_navigation_timeout(25000)
        try:
            login(page)
            for row in rows:
                # In a real run, the limit caps actual votes cast. In --dry-run
                # there's nothing to limit -- the whole point is a full rehearsal
                # across every row, so --limit is ignored.
                if not dry_run and counts["voted"] >= limit:
                    break
                try:
                    status, detail = process_one(page, row, dry_run)
                except Exception as e:
                    cn = row["covidence_number"]
                    logger.error(f"{cn}: UNEXPECTED EXCEPTION -- {type(e).__name__}: {e}")
                    try:
                        save_diagnostics(page, f"{cn}_exception")
                    except Exception:
                        pass
                    if dry_run:
                        # Nothing was at risk -- note it and keep rehearsing
                        # the rest of the list rather than losing the whole run.
                        status, detail = "ambiguous", f"exception during dry-run: {e}"
                    else:
                        status, detail = "failed", f"exception: {e}"
                counts[status] = counts.get(status, 0) + 1
                if status == "already_voted":
                    continue  # cheap, expected on a re-run -- nothing to flag
                if status in ("no_results", "ambiguous", "cn_mismatch"):
                    unresolved.append((row["covidence_number"], status, detail))
                    continue  # not fatal -- move on to the next row
                if status == "vote_conflict":
                    logger.error(
                        f"STOPPING run: {row['covidence_number']} has a conflicting existing "
                        f"vote ({detail}). This needs a human look -- check the record in "
                        f"Covidence (another reviewer may have voted it, or a prior run cast "
                        f"the wrong decision) before deciding whether to change it."
                    )
                    break
                if status == "failed":
                    logger.error(
                        f"STOPPING run: {row['covidence_number']} failed ({detail}). "
                        f"Resolve this before re-running -- votes already cast this run "
                        f"are unaffected; just rerun to continue from here."
                    )
                    break
        finally:
            browser.close()

    logger.info(f"Finished. Counts: {counts}")
    if unresolved:
        logger.warning(f"{len(unresolved)} row(s) need manual attention (not voted):")
        for cn, status, detail in unresolved:
            logger.warning(f"  {cn}: {status} -- {detail}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cast full-text-review decisions into Covidence")
    parser.add_argument("--limit", type=int, default=10000, help="Max decisions to process this run")
    parser.add_argument("--headless", action="store_true", default=True, help="(default) no visible browser window")
    parser.add_argument("--no-headless", dest="headless", action="store_false", help="show the browser window")
    parser.add_argument("--dry-run", action="store_true", help="Navigate and verify only -- click nothing")
    parser.add_argument("--only-exclude", action="store_true",
                         help="Process only Exclude-decision rows (useful for testing the reason-picker path first)")
    parser.add_argument("--env-file", default=".env",
                         help="Path to the .env file holding COVID_ID / COVID_PASSWORD for whichever "
                              "reviewer is running this (default: .env). Use a separate file (e.g. "
                              ".env.alaa) for a second reviewer so it doesn't collide with anyone else's "
                              "credentials in the same project checkout.")
    args = parser.parse_args()

    load_dotenv(args.env_file)

    if "COVID_ID" not in os.environ or "COVID_PASSWORD" not in os.environ:
        print(f"Missing COVID_ID / COVID_PASSWORD in {args.env_file}. Create that file with your own "
              f"Covidence login (COVID_ID=you@example.com / COVID_PASSWORD=...).", file=sys.stderr)
        sys.exit(1)

    run(args.limit, args.headless, args.dry_run, args.only_exclude)
