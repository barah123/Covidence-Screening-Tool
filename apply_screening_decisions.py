"""
Applies pre-computed title/abstract screening decisions to Covidence, one study at a
time. Adapted from a reused Covidence-automation template (originally built for an
unrelated review, "Retinal Hemorrhage Patterns in Abusive vs. Non-Abusive Head Trauma
in Children", Covidence review 520996) — only the browser-automation scaffolding is
reused here. Decisions themselves come from screening_decisions.csv (produced by
reading each record's full abstract against this review's own PECOS criteria), not
from an LLM call, so no Gemini / API key dependency is needed.

Why one-at-a-time with a reload before every single vote: Covidence's screening list
recycles DOM nodes between items, and voting on several queued studies without a
fresh reload in between produced unreliable results during testing (votes silently
not saving, or landing on the wrong study). A full page reload immediately before
each single interaction was the only pattern that worked reliably.

Setup:
    pip install playwright pandas python-dotenv
    playwright install chromium

    Create a .env file (see .env.example) with your own Covidence login:
        COVID_ID=you@example.com
        COVID_PASSWORD=your_password

Usage:
    python3 apply_screening_decisions.py --decisions search-results-2026-10/screening_decisions.csv
    python3 apply_screening_decisions.py --limit 50          # process only 50 studies, then stop
    python3 apply_screening_decisions.py --headless          # no visible browser window
"""
import argparse
import logging
import os
import re
import sys
import time

import pandas as pd
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page, Browser, Playwright, ElementHandle

load_dotenv()

SIGN_IN_URL = "https://app.covidence.org"
SCREENING_URL = "https://app.covidence.org/reviews/818465/review_studies/screen?filter=vote_required_from"

DECISION_TO_VOTE = {"Include": "Yes", "Exclude": "No", "Maybe": "Maybe"}

CARD_SELECTOR = '[class*="StudyListItem-module__card"]'
TITLE_SELECTOR = 'h3[class*="StudyReference-module__title"]'
VOTE_BUTTON_SELECTOR = '[data-pendo-key="vote-button"]'

# The real PMID is rendered as visible text on the card, e.g. "Ref ID: 27446009",
# not inside a dedicated CSS-classed element. Confirmed against live Covidence
# markup on 2026-10-01 (see debug_queue.py) -- the previous '.ref-ids' selector
# did not match the intended element and silently extracted an unrelated "10"
# from elsewhere on the page.
REF_ID_PATTERN = re.compile(r"Ref ID:\s*(\d+)")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("covidence_apply.log", mode="a")],
)
logger = logging.getLogger("covidence_apply")


def load_decisions(path: str) -> dict:
    df = pd.read_csv(path, dtype={"pmid": str})
    df = df.set_index("pmid")
    return df.to_dict(orient="index")


def login(page: Page) -> None:
    page.goto(SIGN_IN_URL, timeout=60000)
    page.fill('#session_email', os.environ["COVID_ID"])
    page.fill('#session_password', os.environ["COVID_PASSWORD"])
    page.click('input[name="commit"]')
    page.wait_for_load_state("networkidle", timeout=60000)


def extract_ref_id(card: ElementHandle) -> str | None:
    m = REF_ID_PATTERN.search(card.inner_text())
    return m.group(1) if m else None


def extract_title(card: ElementHandle) -> str:
    el = card.query_selector(TITLE_SELECTOR)
    return el.inner_text().strip() if el else ""


def vote(card: ElementHandle, value: str) -> bool:
    buttons = card.query_selector_all(VOTE_BUTTON_SELECTOR)
    for b in buttons:
        if b.inner_text().strip() == value:
            b.click(force=True)
            return True
    return False


def process_one(page: Page, decisions: dict) -> tuple[str, bool]:
    """Returns (status, should_continue). status is one of:
    'voted', 'no_decision', 'empty_queue', 'extract_failed'."""
    page.goto(SCREENING_URL, timeout=60000)
    page.wait_for_load_state("networkidle", timeout=60000)
    page.wait_for_selector(CARD_SELECTOR, timeout=8000)

    card = page.query_selector(CARD_SELECTOR)
    if not card:
        return "empty_queue", False

    ref_id = extract_ref_id(card)
    title = extract_title(card)

    if not ref_id:
        logger.warning(f"Could not extract Ref ID from top study (title: {title!r}). Skipping vote.")
        return "extract_failed", True

    record = decisions.get(ref_id)
    if record is None:
        logger.warning(
            f"PMID {ref_id} ({title!r}) has no pre-computed decision on file. "
            f"Stopping run without voting -- resolve this manually (decide if it's "
            f"in scope, or vote it directly in Covidence) before restarting the script."
        )
        return "no_decision", False

    covidence_vote = DECISION_TO_VOTE.get(record["decision"], "Maybe")
    ok = vote(card, covidence_vote)
    if not ok:
        logger.error(f"Vote button '{covidence_vote}' not found for PMID {ref_id} ({title!r}).")
        return "extract_failed", True

    logger.info(f"PMID {ref_id}: {record['decision']} ({title!r})")
    return "voted", True


def run(decisions_path: str, limit: int, headless: bool) -> None:
    decisions = load_decisions(decisions_path)
    logger.info(f"Loaded {len(decisions)} pre-computed decisions from {decisions_path}")

    processed = 0
    no_decision_count = 0

    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=headless)
        page: Page = browser.new_page()
        try:
            login(page)
            while processed < limit:
                status, should_continue = process_one(page, decisions)
                if status == "voted":
                    processed += 1
                elif status == "no_decision":
                    no_decision_count += 1
                elif status == "empty_queue":
                    logger.info("No more studies in the screening queue. Done.")
                    break
                elif status == "extract_failed":
                    time.sleep(2)
                if not should_continue:
                    break
                logger.info(f"Processed so far: {processed}")
        finally:
            browser.close()

    logger.info(f"Finished. Processed {processed} studies this run.")
    if no_decision_count:
        logger.warning(
            "Run stopped early because a study had no pre-computed decision on file. "
            "It was NOT voted on. Check covidence_apply.log for its PMID, resolve it "
            "manually, then rerun the script to continue from the next study."
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply pre-computed screening decisions to Covidence")
    parser.add_argument("--decisions", default="search-results-2026-10/screening_decisions.csv",
                        help="CSV with columns: pmid, decision, justification")
    parser.add_argument("--limit", type=int, default=10000, help="Max studies to process this run")
    parser.add_argument("--headless", action="store_true", help="Run without a visible browser window")
    args = parser.parse_args()

    if "COVID_ID" not in os.environ or "COVID_PASSWORD" not in os.environ:
        print("Missing COVID_ID / COVID_PASSWORD. Create a .env file — see .env.example.", file=sys.stderr)
        sys.exit(1)

    run(args.decisions, args.limit, args.headless)
