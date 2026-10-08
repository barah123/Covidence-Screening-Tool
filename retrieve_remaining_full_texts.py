"""
Categorizes the 123 records still needing full text (full-text/retrieval_status_2026-10-08.csv,
statuses still_needs_retrieval / still_needs_retrieval_no_doi) by retrieval route:

  - DOI records: queried against Unpaywall (free OA-location lookup).
  - No-DOI records: first resolved to a DOI via a Crossref bibliographic
    title search, then the same Unpaywall check.

Any record with a direct OA PDF URL is downloaded (and validated as a real
PDF, not an HTML landing page) into full-text/open-access-2026-10-08/.
Everything else is categorized for manual follow-up (GWU institutional
access or ILL) and written to a report CSV -- nothing is downloaded without
a confirmed working PDF link.

Usage:
    python3 retrieve_remaining_full_texts.py
"""
import csv
import os
import re
import time
import urllib.parse
import urllib.request
import json

EMAIL = "you@example.com"  # Unpaywall requires a contact email -- any address works, set your own
STATUS_CSV = "full-text/retrieval_status_2026-10-08.csv"
OUT_DIR = "full-text/open-access-2026-10-08"
REPORT_CSV = "full-text/remaining_retrieval_categorized_2026-10-08.csv"

os.makedirs(OUT_DIR, exist_ok=True)


def http_get_json(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": f"systematic-review-script ({EMAIL})"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def norm_doi(doi):
    return doi.strip().lower().rstrip(".")


def unpaywall_lookup(doi):
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={EMAIL}"
    try:
        data = http_get_json(url)
    except Exception as e:
        return {"error": str(e)}
    best = data.get("best_oa_location") or {}
    return {
        "is_oa": data.get("is_oa", False),
        "pdf_url": best.get("url_for_pdf") or "",
        "landing_url": best.get("url") or "",
        "host_type": best.get("host_type") or "",
    }


def crossref_find_doi(title):
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({
        "query.bibliographic": title, "rows": 1
    })
    try:
        data = http_get_json(url)
    except Exception:
        return None
    items = data.get("message", {}).get("items", [])
    if not items:
        return None
    item = items[0]
    cr_title = (item.get("title") or [""])[0]
    # Require a reasonably close title match before trusting the DOI.
    def norm(t):
        return re.sub(r"[^a-z0-9 ]", "", t.lower())
    if norm(title)[:60] not in norm(cr_title) and norm(cr_title)[:60] not in norm(title):
        return None
    return item.get("DOI")


def download_pdf(url, dest_path):
    req = urllib.request.Request(url, headers={"User-Agent": f"systematic-review-script ({EMAIL})"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
    except Exception as e:
        return False, str(e)
    if not content.startswith(b"%PDF"):
        return False, "downloaded content is not a PDF (likely an HTML landing page)"
    with open(dest_path, "wb") as f:
        f.write(content)
    return True, None


def safe_doi_filename(doi):
    return re.sub(r"[^A-Za-z0-9._-]", "_", doi)


def main():
    rows = []
    with open(STATUS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["status"] in ("still_needs_retrieval", "still_needs_retrieval_no_doi"):
                rows.append(row)

    print(f"Processing {len(rows)} records...")
    results = []
    downloaded = 0

    for i, row in enumerate(rows, 1):
        title = row["title"]
        doi = norm_doi(row["doi"]) if row["doi"] else ""
        resolved_via_crossref = False

        if not doi:
            found = crossref_find_doi(title)
            time.sleep(0.3)
            if found:
                doi = norm_doi(found)
                resolved_via_crossref = True

        category = ""
        pdf_url = ""
        notes = ""

        if not doi:
            category = "no_doi_found_needs_manual_lookup"
        else:
            uw = unpaywall_lookup(doi)
            time.sleep(0.2)
            if "error" in uw:
                category = "unpaywall_lookup_failed"
                notes = uw["error"]
            elif uw["pdf_url"]:
                dest = os.path.join(OUT_DIR, f"{safe_doi_filename(doi)}.pdf")
                ok, err = download_pdf(uw["pdf_url"], dest)
                if ok:
                    category = "downloaded_open_access"
                    pdf_url = uw["pdf_url"]
                    downloaded += 1
                else:
                    category = "open_access_pdf_link_failed"
                    pdf_url = uw["pdf_url"]
                    notes = err
            elif uw["is_oa"] and uw["landing_url"]:
                category = "open_access_landing_page_only"
                pdf_url = uw["landing_url"]
                notes = "OA flagged but no direct PDF link -- needs a manual visit"
            else:
                category = "closed_needs_institutional_access_or_ill"

        results.append({
            "title": title,
            "doi": doi,
            "doi_resolved_via_crossref": resolved_via_crossref,
            "category": category,
            "pdf_or_landing_url": pdf_url,
            "notes": notes,
        })
        if i % 20 == 0:
            print(f"  {i}/{len(rows)} processed, {downloaded} downloaded so far")

    with open(REPORT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["title", "doi", "doi_resolved_via_crossref", "category", "pdf_or_landing_url", "notes"])
        w.writeheader()
        w.writerows(results)

    from collections import Counter
    tally = Counter(r["category"] for r in results)
    print(f"\nDone. {downloaded} PDFs downloaded to {OUT_DIR}/")
    print(f"Report written to {REPORT_CSV}")
    print("\nCategory breakdown:")
    for cat, count in tally.most_common():
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
