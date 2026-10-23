import os
import sys
import json
import csv
import sqlite3
import hashlib
from datetime import datetime, timezone

DB_PATH = "/app/soren-spline-kb/data/spline_kb.db"
UI_JSON_PATH = "/app/Spline_UI_Elements_2026-10-22.json"
ACADEMY_CSV_PATH = "/app/Spline_Academy_Video_Catalog_2026-10-22.csv"
DOCS_MANIFEST_PATH = "/app/soren-spline-kb/data/docs_manifest.json"
DOCS_DIR = "/app/soren-spline-kb/data/docs_ingested"

def get_connection(db_path=DB_PATH):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_schema(conn):
    cursor = conn.cursor()

    # Metadata / Tracking table for incremental reindexing
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indexed_sources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_type TEXT NOT NULL,
        source_identifier TEXT UNIQUE NOT NULL,
        content_hash TEXT NOT NULL,
        last_indexed_at TEXT NOT NULL
    );
    """)

    # Normalized UI Elements Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ui_elements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        element_name TEXT NOT NULL,
        mode TEXT NOT NULL,
        location TEXT,
        how_to_access TEXT,
        what_it_does TEXT,
        related_tools TEXT,
        keyboard_shortcut TEXT,
        notes TEXT,
        source_url TEXT,
        content_hash TEXT NOT NULL,
        last_updated TEXT NOT NULL
    );
    """)

    # Exact UI Lookup Index
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_ui_name ON ui_elements(element_name);
    """)
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_ui_mode ON ui_elements(mode);
    """)
    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_ui_shortcut ON ui_elements(keyboard_shortcut);
    """)

    # Normalized Documentation Pages Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doc_pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        url TEXT UNIQUE NOT NULL,
        editor_mode TEXT,
        version_applicability TEXT,
        provenance TEXT,
        verification_status TEXT,
        content TEXT,
        content_hash TEXT NOT NULL,
        retrieved_at TEXT NOT NULL
    );
    """)

    # Normalized Academy Catalog Table (Strictly NOT transcripts)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS academy_catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT,
        level TEXT,
        duration_approx_minutes INTEGER,
        youtube_url TEXT,
        academy_url TEXT,
        youtube_id TEXT,
        has_full_transcript BOOLEAN DEFAULT 0,
        is_transcript BOOLEAN DEFAULT 0,
        transcript_note TEXT,
        content_hash TEXT NOT NULL,
        last_updated TEXT NOT NULL
    );
    """)

    # SQLite FTS5 Virtual Table for Global Full-Text Search
    cursor.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS kb_fts USING fts5(
        entity_id,
        entity_type,
        title,
        content,
        mode,
        url,
        tokenize='porter ascii'
    );
    """)

    conn.commit()

def build_database(db_path=DB_PATH):
    print(f"Building SQLite KB Database at {db_path}...")
    conn = get_connection(db_path)
    cursor = conn.cursor()

    init_schema(conn)

    # 1. Populate UI Elements
    if os.path.exists(UI_JSON_PATH):
        with open(UI_JSON_PATH, 'r', encoding='utf-8') as f:
            ui_data = json.load(f)

        ui_json_str = json.dumps(ui_data, sort_keys=True)
        ui_hash = hashlib.sha256(ui_json_str.encode('utf-8')).hexdigest()

        # Check incremental index
        cursor.execute("SELECT content_hash FROM indexed_sources WHERE source_identifier = ?", ("ui_elements",))
        row = cursor.fetchone()
        if not row or row[0] != ui_hash:
            print("Indexing UI Elements...")
            cursor.execute("DELETE FROM ui_elements;")
            cursor.execute("DELETE FROM kb_fts WHERE entity_type = 'ui_element';")

            for elem in ui_data.get('elements', []):
                related = json.dumps(elem.get('related_tools_or_options', [])) if isinstance(elem.get('related_tools_or_options'), list) else str(elem.get('related_tools_or_options', ''))
                cursor.execute("""
                INSERT INTO ui_elements (element_name, mode, location, how_to_access, what_it_does, related_tools, keyboard_shortcut, notes, source_url, content_hash, last_updated)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    elem.get('element_name', ''),
                    elem.get('mode', ''),
                    elem.get('location', ''),
                    elem.get('how_to_access', ''),
                    elem.get('what_it_does', ''),
                    related,
                    elem.get('keyboard_shortcut'),
                    elem.get('notes', ''),
                    elem.get('source_url', ''),
                    ui_hash,
                    datetime.now(timezone.utc).isoformat()
                ))
                ui_id = cursor.lastrowid

                # Index in FTS
                fts_text = f"{elem.get('element_name', '')} {elem.get('location', '')} {elem.get('how_to_access', '')} {elem.get('what_it_does', '')} {elem.get('notes', '')} shortcut: {elem.get('keyboard_shortcut', '')}"
                cursor.execute("""
                INSERT INTO kb_fts (entity_id, entity_type, title, content, mode, url)
                VALUES (?, 'ui_element', ?, ?, ?, ?)
                """, (
                    str(ui_id),
                    elem.get('element_name', ''),
                    fts_text,
                    elem.get('mode', ''),
                    elem.get('source_url', '')
                ))

            cursor.execute("""
            INSERT OR REPLACE INTO indexed_sources (source_type, source_identifier, content_hash, last_indexed_at)
            VALUES ('json', 'ui_elements', ?, ?)
            """, (ui_hash, datetime.now(timezone.utc).isoformat()))
        else:
            print("UI Elements already up to date.")

    # 2. Populate Doc Pages
    if os.path.exists(DOCS_MANIFEST_PATH):
        with open(DOCS_MANIFEST_PATH, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        docs_count = 0
        for doc in manifest.get('documents', []):
            if doc.get('fetch_status') != 'SUCCESS':
                continue

            doc_file = os.path.join(DOCS_DIR, doc['local_file'])
            if os.path.exists(doc_file):
                with open(doc_file, 'r', encoding='utf-8') as df:
                    content = df.read()

                url = doc['url']
                doc_hash = doc['sha256']

                cursor.execute("SELECT content_hash FROM indexed_sources WHERE source_identifier = ?", (url,))
                row = cursor.fetchone()
                if not row or row[0] != doc_hash:
                    cursor.execute("DELETE FROM doc_pages WHERE url = ?;", (url,))
                    cursor.execute("DELETE FROM kb_fts WHERE entity_type = 'doc_page' AND url = ?;", (url,))

                    cursor.execute("""
                    INSERT INTO doc_pages (title, url, editor_mode, version_applicability, provenance, verification_status, content, content_hash, retrieved_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        doc.get('title', ''),
                        url,
                        doc.get('editor_mode', ''),
                        doc.get('version_applicability', ''),
                        doc.get('provenance', ''),
                        doc.get('verification_status', ''),
                        content,
                        doc_hash,
                        doc.get('retrieved_at', datetime.now(timezone.utc).isoformat())
                    ))
                    doc_id = cursor.lastrowid

                    # Index in FTS
                    cursor.execute("""
                    INSERT INTO kb_fts (entity_id, entity_type, title, content, mode, url)
                    VALUES (?, 'doc_page', ?, ?, ?, ?)
                    """, (
                        str(doc_id),
                        doc.get('title', ''),
                        content,
                        doc.get('editor_mode', ''),
                        url
                    ))

                    cursor.execute("""
                    INSERT OR REPLACE INTO indexed_sources (source_type, source_identifier, content_hash, last_indexed_at)
                    VALUES ('doc', ?, ?, ?)
                    """, (url, doc_hash, datetime.now(timezone.utc).isoformat()))
                    docs_count += 1
        print(f"Indexed/updated {docs_count} doc pages.")

    # 3. Populate Academy Video Catalog
    if os.path.exists(ACADEMY_CSV_PATH):
        with open(ACADEMY_CSV_PATH, 'rb') as f:
            csv_raw = f.read()
        csv_hash = hashlib.sha256(csv_raw).hexdigest()

        cursor.execute("SELECT content_hash FROM indexed_sources WHERE source_identifier = ?", ("academy_catalog",))
        row = cursor.fetchone()
        if not row or row[0] != csv_hash:
            print("Indexing Academy Catalog...")
            cursor.execute("DELETE FROM academy_catalog;")
            cursor.execute("DELETE FROM kb_fts WHERE entity_type = 'academy_video';")

            with open(ACADEMY_CSV_PATH, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row_data in reader:
                    title = row_data.get('title', '')
                    category = row_data.get('category', '')
                    level = row_data.get('level', '')
                    dur = int(row_data.get('duration_approx_minutes', 0)) if row_data.get('duration_approx_minutes', '').isdigit() else 0
                    yt_url = row_data.get('youtube_url', '')
                    acad_url = row_data.get('academy_url', '')
                    yt_id = row_data.get('youtube_id', '')

                    # Strictly set transcript flags to FALSE
                    cursor.execute("""
                    INSERT INTO academy_catalog (title, category, level, duration_approx_minutes, youtube_url, academy_url, youtube_id, has_full_transcript, is_transcript, transcript_note, content_hash, last_updated)
                    VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?, ?, ?)
                    """, (
                        title, category, level, dur, yt_url, acad_url, yt_id,
                        "Editorial summary / video metadata only; no video transcript reproduced.",
                        csv_hash, datetime.now(timezone.utc).isoformat()
                    ))
                    acad_id = cursor.lastrowid

                    # Index in FTS
                    fts_text = f"Tutorial Video: {title}. Category: {category}. Level: {level}. Duration: {dur} mins. Summary video catalog entry."
                    cursor.execute("""
                    INSERT INTO kb_fts (entity_id, entity_type, title, content, mode, url)
                    VALUES (?, 'academy_video', ?, ?, ?, ?)
                    """, (
                        str(acad_id),
                        title,
                        fts_text,
                        category,
                        acad_url
                    ))

            cursor.execute("""
            INSERT OR REPLACE INTO indexed_sources (source_type, source_identifier, content_hash, last_indexed_at)
            VALUES ('csv', 'academy_catalog', ?, ?)
            """, (csv_hash, datetime.now(timezone.utc).isoformat()))
        else:
            print("Academy Catalog already up to date.")

    conn.commit()
    conn.close()
    print("Database build complete!")

if __name__ == '__main__':
    build_database()
