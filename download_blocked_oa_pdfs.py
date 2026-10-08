"""
Downloads the confirmed-open-access PDFs that retrieve_remaining_full_texts.py's
raw urllib fetch got bot-blocked on (HTTP 403/429 from publisher WAFs like
Akamai) -- category "open_access_pdf_link_failed" in
full-text/remaining_retrieval_categorized_2026-10-08.csv, excluding the one
record whose fetch genuinely wasn't a PDF.

Uses a real Playwright Chromium browser instead of raw urllib: the request
goes out with a genuine browser TLS/HTTP fingerprint, which simple WAF bot
checks on an otherwise-public PDF link typically let through.

Usage:
    python3 download_blocked_oa_pdfs.py
"""
import csv
import os
import re
import time

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

REPORT_CSV = "full-text/remaining_retrieval_categorized_2026-10-08.csv"
OUT_DIR = "full-text/open-access-2026-10-08"
RESULT_CSV = "full-text/blocked_oa_download_results_2026-10-08.csv"

os.makedirs(OUT_DIR, exist_ok=True)


def safe_doi_filename(doi):
    return re.sub(r"[^A-Za-z0-9._-]", "_", doi)


def load_targets():
    targets = []
    with open(REPORT_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["category"] == "open_access_pdf_link_failed" and "not a PDF" not in row["notes"]:
                targets.append(row)
    return targets


def main():
    targets = load_targets()
    print(f"Loaded {len(targets)} blocked-but-confirmed-OA records to retry via browser")

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        for i, row in enumerate(targets, 1):
            doi = row["doi"]
            url = row["pdf_or_landing_url"]
            dest = os.path.join(OUT_DIR, f"{safe_doi_filename(doi)}.pdf")
            status = "failed"
            note = ""
            try:
                with page.expect_download(timeout=20000) as dl_info:
                    try:
                        page.goto(url, timeout=30000, wait_until="load")
                    except Exception:
                        pass  # goto() itself raises once the download starts; the download is what matters
                download = dl_info.value
                download.save_as(dest)
                with open(dest, "rb") as f:
                    if f.read(4) == b"%PDF":
                        status = "downloaded"
                    else:
                        status = "failed"
                        note = "downloaded file is not a PDF"
                        os.remove(dest)
            except PlaywrightTimeoutError:
                # No download event fired -- either a real page loaded (likely a
                # 403/block page) or something else went wrong with the direct goto.
                try:
                    resp = page.goto(url, timeout=30000, wait_until="load")
                    body = resp.body()
                    content_type = resp.headers.get("content-type", "")
                    if body.startswith(b"%PDF"):
                        with open(dest, "wb") as f:
                            f.write(body)
                        status = "downloaded"
                    else:
                        note = f"not a PDF (content-type={content_type}, status={resp.status})"
                except Exception as e:
                    note = str(e)[:200]
            except Exception as e:
                note = str(e)[:200]

            print(f"[{i}/{len(targets)}] {status}: {doi}" + (f" -- {note}" if note else ""))
            results.append({"doi": doi, "title": row["title"], "url": url, "status": status, "note": note})
            time.sleep(0.5)

        browser.close()

    with open(RESULT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["doi", "title", "url", "status", "note"])
        w.writeheader()
        w.writerows(results)

    downloaded = sum(1 for r in results if r["status"] == "downloaded")
    print(f"\nDone. {downloaded}/{len(targets)} downloaded.")
    print(f"Results written to {RESULT_CSV}")


if __name__ == "__main__":
    main()
