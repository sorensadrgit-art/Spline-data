import os
import sys
import json
import sqlite3
import unittest

sys.path.insert(0, "/app/soren-spline-kb/src")
from retriever import SorenSplineKBRetriever

DB_PATH = "/app/soren-spline-kb/data/spline_kb.db"
INVENTORY_PATH = "/app/soren-spline-kb/data/inventory.json"
DOCS_MANIFEST_PATH = "/app/soren-spline-kb/data/docs_manifest.json"

class TestSplineKnowledgeBase(unittest.TestCase):

    def setUp(self):
        self.retriever = SorenSplineKBRetriever(db_path=DB_PATH)

    def test_database_exists_and_populated(self):
        self.assertTrue(os.path.exists(DB_PATH), "Database file missing")
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute("SELECT COUNT(*) FROM ui_elements;")
        ui_count = c.fetchone()[0]
        self.assertGreater(ui_count, 0, "UI Elements table is empty")

        c.execute("SELECT COUNT(*) FROM doc_pages;")
        doc_count = c.fetchone()[0]
        self.assertGreater(doc_count, 0, "Doc pages table is empty")

        c.execute("SELECT COUNT(*) FROM academy_catalog;")
        academy_count = c.fetchone()[0]
        self.assertGreater(academy_count, 0, "Academy catalog table is empty")

        c.execute("SELECT COUNT(*) FROM kb_fts;")
        fts_count = c.fetchone()[0]
        self.assertGreater(fts_count, 0, "FTS index is empty")
        conn.close()

    def test_inventory_deduplication_and_exclusion(self):
        self.assertTrue(os.path.exists(INVENTORY_PATH), "Inventory JSON missing")
        with open(INVENTORY_PATH, 'r', encoding='utf-8') as f:
            inv = json.load(f)

        # Confirm duplicate detected
        dup_count = inv["inventory_metadata"]["duplicate_files_count"]
        self.assertGreaterEqual(dup_count, 1, "Expected duplicate file not detected in inventory")

        # Confirm script/secret excluded
        excluded_files = [item["file_path"] for item in inv["excluded"]]
        self.assertIn("Finalize-SorenGatewayJwt.ps1", excluded_files, "JWT script was not excluded")

    def test_academy_transcripts_flagged_false(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT has_full_transcript, is_transcript FROM academy_catalog;")
        rows = c.fetchall()
        for has_trans, is_trans in rows:
            self.assertEqual(has_trans, 0, "has_full_transcript must be FALSE (0)")
            self.assertEqual(is_trans, 0, "is_transcript must be FALSE (0)")
        conn.close()

    def test_fts_retrieval(self):
        results = self.retriever.search_fts("glass", limit=5)
        self.assertGreater(len(results), 0, "FTS search for 'glass' returned no results")

    def test_ui_element_lookup(self):
        results = self.retriever.lookup_ui_element(element_name="Home")
        self.assertGreater(len(results), 0, "UI element lookup for 'Home' failed")
        self.assertEqual(results[0]["element_name"], "Home")

    def test_runbook_retrieval(self):
        results = self.retriever.search_runbooks("physics")
        self.assertGreater(len(results), 0, "Runbook search for 'physics' returned no results")

if __name__ == '__main__':
    unittest.main()
