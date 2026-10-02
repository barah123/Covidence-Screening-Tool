"""
Read-only diagnostic script. Logs into Covidence, opens the screening queue,
and prints out exactly what it finds on the first few study cards -- WITHOUT
clicking any vote button or changing anything.

Run this, then paste the full terminal output back so the real selectors in
apply_screening_decisions.py can be corrected based on what Covidence's page
actually contains (rather than guessing).

Usage:
    python3 debug_queue.py
"""
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

SIGN_IN_URL = "https://app.covidence.org"
SCREENING_URL = "https://app.covidence.org/reviews/818465/review_studies/screen?filter=vote_required_from"
CARD_SELECTOR = '[class*="StudyListItem-module__card"]'


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(SIGN_IN_URL, timeout=60000)
        page.fill('#session_email', os.environ["COVID_ID"])
        page.fill('#session_password', os.environ["COVID_PASSWORD"])
        page.click('input[name="commit"]')
        page.wait_for_load_state("networkidle", timeout=60000)

        page.goto(SCREENING_URL, timeout=60000)
        page.wait_for_load_state("networkidle", timeout=60000)
        page.wait_for_selector(CARD_SELECTOR, timeout=8000)

        cards = page.query_selector_all(CARD_SELECTOR)
        print(f"\n=== Found {len(cards)} card(s) matching CARD_SELECTOR on this page ===\n")

        for i, card in enumerate(cards[:3]):
            print(f"\n----- CARD {i} : full visible text -----")
            print(card.inner_text())
            print(f"\n----- CARD {i} : outer HTML (first 4000 chars) -----")
            html = card.evaluate("el => el.outerHTML")
            print(html[:4000])
            print(f"\n----- CARD {i} : end -----\n")

        print("\n=== Done. No votes were cast. Browser will stay open 15s for you to look too. ===")
        page.wait_for_timeout(15000)
        browser.close()


if __name__ == "__main__":
    if "COVID_ID" not in os.environ or "COVID_PASSWORD" not in os.environ:
        raise SystemExit("Missing COVID_ID / COVID_PASSWORD in .env")
    main()
