import os
import sys
import re
import json
import hashlib
import urllib.request
import urllib.error
from datetime import datetime, timezone

LLMS_TXT_URL = "https://docs.spline.design/llms.txt"
DOCS_DIR = "/app/soren-spline-kb/data/docs_ingested"
MANIFEST_FILE = "/app/soren-spline-kb/data/docs_manifest.json"

def classify_editor_mode(url, title, content):
    lower_text = f"{url} {title} {content[:500]}".lower()
    if "hana" in lower_text or "/hana" in lower_text:
        return "Hana / 2D Design"
    elif "dashboard" in lower_text:
        return "Dashboard / Files"
    elif "api" in lower_text or "code-export" in lower_text or "react" in lower_text or "three" in lower_text:
        return "Code / Integration"
    elif "ai" in lower_text:
        return "AI Tools / Generation"
    else:
        return "3D Spatial Editor"

def fetch_url(url, timeout=15):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SorenSplineKB/1.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code} for {url}")
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def ingester():
    print(f"Fetching llms.txt from {LLMS_TXT_URL}...")
    llms_txt_content = fetch_url(LLMS_TXT_URL)
    if not llms_txt_content:
        print("Failed to fetch llms.txt")
        sys.exit(1)

    os.makedirs(DOCS_DIR, exist_ok=True)

    # Save llms.txt
    llms_hash = hashlib.sha256(llms_txt_content.encode('utf-8')).hexdigest()
    with open(os.path.join(DOCS_DIR, "llms.txt"), 'w', encoding='utf-8') as f:
        f.write(llms_txt_content)

    # Extract Markdown links: [Title](URL)
    pattern = r'\[([^\]]+)\]\((https?://docs\.spline\.design/[^\)]+)\)'
    matches = re.findall(pattern, llms_txt_content)

    # Deduplicate URLs
    unique_links = {}
    for title, url in matches:
        if url not in unique_links:
            unique_links[url] = title

    print(f"Found {len(unique_links)} unique doc endpoints in llms.txt.")

    manifest_entries = []
    success_count = 0
    fail_count = 0

    for i, (url, title) in enumerate(unique_links.items(), 1):
        # Format filename from URL path
        path_part = url.replace("https://docs.spline.design/", "")
        filename = path_part.replace("/", "_")
        if not filename.endswith(".md"):
            filename += ".md"

        filepath = os.path.join(DOCS_DIR, filename)

        print(f"[{i}/{len(unique_links)}] Fetching {url}...")
        content = fetch_url(url)

        retrieval_timestamp = datetime.now(timezone.utc).isoformat()

        if content:
            content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            editor_mode = classify_editor_mode(url, title, content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            entry = {
                "title": title,
                "url": url,
                "local_file": filename,
                "size_bytes": len(content.encode('utf-8')),
                "sha256": content_hash,
                "retrieved_at": retrieval_timestamp,
                "editor_mode": editor_mode,
                "version_applicability": "Spline 3D / Hana v2+",
                "provenance": "Official Spline Docs via llms.txt",
                "verification_status": "Verified Official Source",
                "fetch_status": "SUCCESS"
            }
            success_count += 1
        else:
            entry = {
                "title": title,
                "url": url,
                "local_file": filename,
                "retrieved_at": retrieval_timestamp,
                "fetch_status": "FAILED"
            }
            fail_count += 1

        manifest_entries.append(entry)

    manifest = {
        "metadata": {
            "source_llms_txt": LLMS_TXT_URL,
            "llms_txt_sha256": llms_hash,
            "total_endpoints": len(unique_links),
            "successfully_ingested": success_count,
            "failed_ingestion": fail_count,
            "ingested_at": datetime.now(timezone.utc).isoformat()
        },
        "documents": manifest_entries
    }

    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f"Documentation Ingestion complete! Successfully fetched: {success_count}, Failed: {fail_count}")
    print(f"Manifest saved to {MANIFEST_FILE}")

if __name__ == '__main__':
    ingester()
