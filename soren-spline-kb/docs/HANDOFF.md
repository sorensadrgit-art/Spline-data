# SOREN Spline Knowledge Base v1 - Implementation Handoff

## 1. Project Overview & Architecture
The **SOREN Spline Knowledge Base v1** provides structured, verified, and queryable retrieval interfaces across the entire official Spline ecosystem (3D Spatial Editor, Hana 2D Canvas, Code APIs, Integrations, and Academy tutorials).

### Directory Structure
```
soren-spline-kb/
├── data/
│   ├── inventory.json                  # Hash & deduplication record of original sources
│   ├── Spline_Source_Index_2026-10-22.json # Extracted source index
│   ├── docs_manifest.json              # Crawl manifest for llms.txt pages
│   ├── spline_kb.db                    # SQLite database with FTS5 virtual tables
│   └── eval_results.json               # Benchmark evaluation output
├── docs/
│   ├── AUDIT_REPORT.md                 # Complete source & ingestion audit report
│   ├── GAP_LIST.md                     # Gap list & mitigation details
│   └── HANDOFF.md                      # System integration handoff guide
├── runbooks/
│   ├── RUNBOOK_01_create_3d_glass_material.md
│   ├── ...
│   └── RUNBOOK_20_version_history_collaboration.md
├── src/
│   ├── inventory.py                    # Stage 1 source inventory & hashing
│   ├── doc_ingester.py                 # Live llms.txt crawling script
│   ├── db_builder.py                   # SQLite schema, normalization & FTS5 indexing
│   ├── generate_runbooks.py            # Runbook synthesis script
│   └── retriever.py                    # Read-only retrieval interface
└── tests/
    ├── test_kb.py                      # Automated schema & provenance test suite
    └── eval_suite.py                   # 20-question evaluation benchmark suite
```

---

## 2. Using the Retrieval Interface (`retriever.py`)

The knowledge base exposes a clean, read-only Python interface compatible with SOREN Universal:

```python
from soren_spline_kb.src.retriever import SorenSplineKBRetriever

retriever = SorenSplineKBRetriever()

# 1. Global Full-Text Search (FTS5)
results = retriever.search_fts("liquid glass materials", limit=5)

# 2. Exact UI Path & Shortcut Lookup
ui_item = retriever.lookup_ui_element(element_name="Home")

# 3. Task-Oriented Runbook Search
runbooks = retriever.search_runbooks("physics rigid bodies")

# 4. Doc Page Lookup
doc = retriever.get_doc_page(url="https://docs.spline.design/basics/what-is-spline")
```

---

## 3. Execution Authority & SOREN Agent Skill Rules
- **Execution Authority**: The official `spline_mcp` / Agent Skill remains the sole execution authority for altering or creating Spline scenes.
- **Read-Only Scope**: `soren-spline-kb` functions strictly as a READ-ONLY knowledge server to feed context, exact UI paths, and tool call parameters into execution agents without modifying live scenes.

---

## 4. Verification & Testing Summary
- **Unit Test Suite**: `python3 -m unittest soren-spline-kb/tests/test_kb.py` (Passed 100%)
- **Evaluation Benchmark**: `python3 soren-spline-kb/tests/eval_suite.py` (20/20 Queries Matched, 100% Success Rate)
