import os
import sys
import json
import glob
import sqlite3

DB_PATH = "/app/soren-spline-kb/data/spline_kb.db"
RUNBOOKS_DIR = "/app/soren-spline-kb/runbooks"

class SorenSplineKBRetriever:
    def __init__(self, db_path=DB_PATH, runbooks_dir=RUNBOOKS_DIR):
        self.db_path = db_path
        self.runbooks_dir = runbooks_dir

    def _get_conn(self):
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Database file not found at {self.db_path}. Please build the DB first.")
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def search_fts(self, query_text, limit=10):
        """
        Global full-text search across UI elements, doc pages, and academy videos.
        """
        conn = self._get_conn()
        cursor = conn.cursor()

        # Clean query string for FTS5 syntax safety
        safe_query = " OR ".join([f'"{term.replace('\"', '')}"' for term in query_text.split() if term])
        if not safe_query:
            return []

        cursor.execute("""
            SELECT entity_id, entity_type, title, content, mode, url, rank
            FROM kb_fts
            WHERE kb_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (safe_query, limit))

        rows = cursor.fetchall()
        results = []
        for r in rows:
            results.append({
                "entity_id": r["entity_id"],
                "entity_type": r["entity_type"],
                "title": r["title"],
                "snippet": r["content"][:300] + "..." if len(r["content"]) > 300 else r["content"],
                "mode": r["mode"],
                "url": r["url"]
            })
        conn.close()
        return results

    def lookup_ui_element(self, element_name=None, mode=None, shortcut=None):
        """
        Exact or partial lookup of UI elements by name, editor mode, or keyboard shortcut.
        """
        conn = self._get_conn()
        cursor = conn.cursor()

        query = "SELECT * FROM ui_elements WHERE 1=1"
        params = []

        if element_name:
            query += " AND element_name LIKE ?"
            params.append(f"%{element_name}%")
        if mode:
            query += " AND mode LIKE ?"
            params.append(f"%{mode}%")
        if shortcut:
            query += " AND (keyboard_shortcut LIKE ? OR keyboard_shortcut = ?)"
            params.append(f"%{shortcut}%")
            params.append(shortcut)

        cursor.execute(query, params)
        rows = cursor.fetchall()

        results = [dict(r) for r in rows]
        conn.close()
        return results

    def get_doc_page(self, url=None, title=None):
        """
        Retrieve documentation page by exact URL or title.
        """
        conn = self._get_conn()
        cursor = conn.cursor()

        if url:
            cursor.execute("SELECT * FROM doc_pages WHERE url = ?", (url,))
        elif title:
            cursor.execute("SELECT * FROM doc_pages WHERE title LIKE ?", (f"%{title}%",))
        else:
            return None

        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def search_runbooks(self, topic):
        """
        Search 3D & Hana task runbooks matching the query topic.
        """
        runbook_files = glob.glob(os.path.join(self.runbooks_dir, "*.md"))
        matches = []
        topic_lower = topic.lower()

        for path in runbook_files:
            filename = os.path.basename(path)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            if topic_lower in content.lower() or topic_lower in filename.lower():
                # Extract first line title
                first_line = content.split('\n')[0].replace('#', '').strip()
                matches.append({
                    "filename": filename,
                    "title": first_line,
                    "path": path,
                    "content": content
                })

        return matches

    def get_academy_videos(self, category=None, level=None):
        """
        Retrieve Academy video catalog metadata (strictly flagged as non-transcripts).
        """
        conn = self._get_conn()
        cursor = conn.cursor()

        query = "SELECT * FROM academy_catalog WHERE 1=1"
        params = []

        if category:
            query += " AND category LIKE ?"
            params.append(f"%{category}%")
        if level:
            query += " AND level LIKE ?"
            params.append(f"%{level}%")

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]

if __name__ == '__main__':
    kb = SorenSplineKBRetriever()
    print("Testing FTS Search for 'glass':")
    print(json.dumps(kb.search_fts("glass", limit=2), indent=2))

    print("\nTesting UI Lookup for 'Home':")
    print(json.dumps(kb.lookup_ui_element(element_name="Home"), indent=2))

    print("\nTesting Runbook Search for 'Physics':")
    rb_res = kb.search_runbooks("Physics")
    print(f"Found {len(rb_res)} runbook(s):", [r["filename"] for r in rb_res])
