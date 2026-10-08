"""
Uploads locally-held full-text PDFs into Covidence for records that are
currently sitting in Full Text Review with no full text attached, matched
by DOI against full-text/retrieval_status_2026-10-08.csv's
"have_locally_needs_upload" rows.

For each record: search Covidence by title, open the (hopefully unique)
match, open the "Upload full text" dialog, attach the local PDF, confirm.

Usage:
    python3 upload_full_texts.py --limit 1       # test on one record first
    python3 upload_full_texts.py                 # run all
"""
import argparse
import csv
import logging
import os
import sys
import time
import urllib.parse

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page

load_dotenv()

SIGN_IN_URL = "https://app.covidence.org"
STATUS_CSV = "full-text/retrieval_status_2026-10-08.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("upload_full_texts.log", mode="a")],
)
logger = logging.getLogger("upload_full_texts")


def load_targets(status_csv: str):
    rows = []
    with open(status_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["status"] == "have_locally_needs_upload":
                path = row["local_pdf_path"].split("; ")[0]  # first file if duplicates
                rows.append({"doi": row["doi"], "title": row["title"], "pdf_path": os.path.abspath(path)})
    return rows


def login(page: Page) -> None:
    page.goto(SIGN_IN_URL, timeout=60000)
    page.fill('#session_email', os.environ["COVID_ID"])
    page.fill('#session_password', os.environ["COVID_PASSWORD"])
    page.click('input[name="commit"]')
    page.wait_for_load_state("networkidle", timeout=60000)


def norm_title(t: str) -> str:
    return " ".join(t.strip().lower().split())


def search_and_open(page: Page, title: str) -> str:
    """Searches by title, returns 'opened' / 'no_results' / 'ambiguous'.

    When the search has exactly one match, Covidence skips the results-list
    page entirely and navigates straight to that study's own page (URL
    becomes .../review_studies/select?...&id=NNNN). A 0- or 2+-match search
    lands on the .../review_studies/search?... results list instead, where
    each result is a plain <a href="/reviews/818465/review_studies/{id}">
    (no "select?" in the href -- that only appears after you click through).
    On a multi-result page we still look for an exact title match among the
    (often loosely/fuzzily matched) results rather than assuming the first.
    """
    # Covidence hard-limits search queries to 150 characters (longer queries
    # silently return zero results with an on-page warning). Truncate at a
    # word boundary; the exact-title check below still matches against the
    # full title, so a shortened query just needs to surface the right
    # record among the results, not uniquely identify it by itself.
    query = title if len(title) <= 150 else title[:150].rsplit(" ", 1)[0]
    url = ("https://app.covidence.org/reviews/818465/review_studies/search"
           f"?search%5Bterm%5D={urllib.parse.quote(query)}")
    page.goto(url, timeout=60000)
    page.wait_for_load_state("networkidle", timeout=60000)

    if "/review_studies/select" in page.url:
        return "opened"

    links = page.locator('main a[href*="/review_studies/"]')
    count = links.count()
    if count == 0:
        return "no_results"

    target = norm_title(title)
    match_index = None
    for i in range(count):
        link_text = norm_title(links.nth(i).inner_text())
        if target in link_text:
            if match_index is not None:
                return "ambiguous"  # more than one exact-title match
            match_index = i
    if match_index is None:
        return "ambiguous"

    links.nth(match_index).click()
    page.wait_for_load_state("networkidle", timeout=60000)
    return "opened"


def dismiss_libkey_modal(page: Page) -> None:
    modal_close = page.locator('text="Access your library\'s full texts"')
    if modal_close.count() > 0:
        page.keyboard.press("Escape")
        time.sleep(0.5)


def upload_pdf(page: Page, pdf_path: str) -> bool:
    upload_btn = page.get_by_text("Upload full text", exact=True)
    if upload_btn.count() == 0:
        return False
    upload_btn.first.click()
    page.wait_for_selector('text="Upload full text"', timeout=10000)

    file_input = page.locator('input[type="file"]')
    file_input.set_input_files(pdf_path)

    # Wait for the upload to register (filename/thumbnail appears) before closing.
    page.wait_for_timeout(2500)

    done_btn = page.get_by_role("button", name="Done", exact=True)
    if done_btn.count() > 0:
        done_btn.first.click()
    else:
        page.keyboard.press("Escape")
    page.wait_for_timeout(1000)
    return True


def run(limit: int, headless: bool, status_csv: str) -> None:
    targets = load_targets(status_csv)
    logger.info(f"Loaded {len(targets)} records to upload")

    processed = 0
    results = {"uploaded": [], "no_results": [], "ambiguous": [], "upload_failed": []}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        try:
            login(page)
            for t in targets:
                if processed >= limit:
                    break
                if not os.path.exists(t["pdf_path"]):
                    logger.error(f"Local PDF missing on disk: {t['pdf_path']}")
                    results["upload_failed"].append(t)
                    continue

                processed += 1
                status = search_and_open(page, t["title"])
                if status != "opened":
                    logger.warning(f"{status.upper()}: {t['title'][:80]!r} (DOI {t['doi']})")
                    results[status].append(t)
                    continue

                dismiss_libkey_modal(page)
                ok = upload_pdf(page, t["pdf_path"])
                if ok:
                    logger.info(f"UPLOADED: {t['title'][:80]!r} (DOI {t['doi']})")
                    results["uploaded"].append(t)
                else:
                    logger.error(f"UPLOAD BUTTON NOT FOUND: {t['title'][:80]!r} (DOI {t['doi']})")
                    results["upload_failed"].append(t)
        finally:
            browser.close()

    logger.info(f"Finished. Processed {processed} record(s).")
    for k, v in results.items():
        logger.info(f"  {k}: {len(v)}")
    if results["no_results"] or results["ambiguous"] or results["upload_failed"]:
        logger.warning("Records needing manual attention:")
        for k in ("no_results", "ambiguous", "upload_failed"):
            for t in results[k]:
                logger.warning(f"  [{k}] {t['title'][:80]!r} (DOI {t['doi']})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1000)
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--csv", default=STATUS_CSV,
                         help="Status CSV to read 'have_locally_needs_upload' rows from "
                              f"(default: {STATUS_CSV})")
    args = parser.parse_args()

    if "COVID_ID" not in os.environ or "COVID_PASSWORD" not in os.environ:
        print("Missing COVID_ID / COVID_PASSWORD. Create a .env file.", file=sys.stderr)
        sys.exit(1)

    run(args.limit, args.headless, args.csv)
