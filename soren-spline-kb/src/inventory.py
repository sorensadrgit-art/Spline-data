import os
import sys
import json
import hashlib
import zipfile
from datetime import datetime

SOURCE_DIR = "/app"
OUTPUT_FILE = "/app/soren-spline-kb/data/inventory.json"
EXTRACTED_SOURCE_INDEX = "/app/soren-spline-kb/data/Spline_Source_Index_2026-10-22.json"

EXCLUDED_PATTERNS = [
    "Finalize-SorenGatewayJwt.ps1",
    ".git",
    "soren-spline-kb"
]

def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    return sha256.hexdigest()

def inventory_sources():
    print("Starting source inventory...")
    files_by_hash = {}
    inventory = []
    excluded = []

    for root, dirs, files in os.walk(SOURCE_DIR):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDED_PATTERNS and not d.startswith('.')]

        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, SOURCE_DIR)

            # Check exclusion
            if any(pattern in rel_path for pattern in EXCLUDED_PATTERNS):
                excluded.append({
                    "file_path": rel_path,
                    "reason": "Excluded (secret, script, or system directory)"
                })
                continue

            # Compute SHA-256
            file_hash = hash_file(full_path)
            file_size = os.path.getsize(full_path)

            is_duplicate = file_hash in files_by_hash
            canonical_path = files_by_hash.get(file_hash, rel_path)

            if not is_duplicate:
                files_by_hash[file_hash] = rel_path

            item = {
                "file_name": file,
                "relative_path": rel_path,
                "absolute_path": full_path,
                "size_bytes": file_size,
                "sha256": file_hash,
                "is_duplicate": is_duplicate,
                "canonical_path": canonical_path,
                "inventory_timestamp": datetime.utcnow().isoformat() + "Z"
            }
            inventory.append(item)

    # Extract unique source-index JSON from archive if present
    extracted_source_index_info = None
    archive_path = os.path.join(SOURCE_DIR, "Spline_Knowledge_Base_Complete_2026-10-22.zip")
    if os.path.exists(archive_path):
        with zipfile.ZipFile(archive_path, 'r') as z:
            for zip_info in z.infolist():
                if zip_info.filename == "Spline_Source_Index_2026-10-22.json":
                    z.extract(zip_info, path="/app/soren-spline-kb/data")
                    extracted_data = z.read(zip_info.filename)
                    extracted_hash = hashlib.sha256(extracted_data).hexdigest()
                    extracted_source_index_info = {
                        "archive": "Spline_Knowledge_Base_Complete_2026-10-22.zip",
                        "extracted_file": "Spline_Source_Index_2026-10-22.json",
                        "output_path": EXTRACTED_SOURCE_INDEX,
                        "sha256": extracted_hash,
                        "size_bytes": len(extracted_data)
                    }

    result = {
        "inventory_metadata": {
            "source_dir": SOURCE_DIR,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "total_files_scanned": len(inventory) + len(excluded),
            "included_files_count": len(inventory),
            "unique_files_count": len(files_by_hash),
            "duplicate_files_count": sum(1 for item in inventory if item["is_duplicate"]),
            "excluded_files_count": len(excluded)
        },
        "inventory": inventory,
        "excluded": excluded,
        "extracted_archive_sources": extracted_source_index_info
    }

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    print(f"Inventory saved to {OUTPUT_FILE}")
    return result

if __name__ == '__main__':
    inventory_sources()
