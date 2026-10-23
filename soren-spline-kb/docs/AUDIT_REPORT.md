# SOREN Spline Knowledge Base v1 - Audit Report

**Date of Audit**: October 23, 2026
**Target Knowledge Base Path**: `/app/soren-spline-kb`
**Original Read-Only Source Path**: `/app`

---

## 1. Executive Summary
The **SOREN Spline Knowledge Base v1** has been successfully constructed in a dedicated sibling directory (`soren-spline-kb`), keeping all original source files strictly intact and untouched. The knowledge base integrates local source files, live official documentation crawled via `llms.txt`, 20 priority task runbooks, and SQLite FTS5 full-text indexing with exact UI element lookups.

---

## 2. Source Inventory & Content Deduplication

| Source File Name | Relative Path | Size (Bytes) | SHA-256 Hash | Ingestion Status |
| :--- | :--- | :--- | :--- | :--- |
| `Spline_Academy_Video_Catalog_2026-10-22.csv` | `Spline_Academy_Video_Catalog_2026-10-22.csv` | 28,475 | `a7f63eebdc2eec5a2232cbfb427a3dec827a8c60c381c0ae773d4f34ba994ece` | Normalized into SQLite `academy_catalog` |
| `Spline_Interface_Knowledge_Base_2026-10-22.md` | `Spline_Interface_Knowledge_Base_2026-10-22.md` | 171,690 | `0e8ae49c05309afa6ffcd46817f9e0093543c9741cae38c3778ae41f66ae222a` | Canonical UI interface source |
| `Spline_Interface_Knowledge_Base_2026-10-22 (1).md` | `Spline_Interface_Knowledge_Base_2026-10-22 (1).md` | 171,690 | `0e8ae49c05309afa6ffcd46817f9e0093543c9741cae38c3778ae41f66ae222a` | **Identified as Duplicate**; mapped to canonical file |
| `Spline_Knowledge_Base_Complete_2026-10-22.zip` | `Spline_Knowledge_Base_Complete_2026-10-22.zip` | 48,634 | `3abd521725c3fc06b3f4c1189a7ac9f577ceb423e14c5f92f9b85cd76ea4893b` | Archive source |
| `Spline_UI_Elements_2026-10-22.json` | `Spline_UI_Elements_2026-10-22.json` | 40,642 | `0eb12dfdcea0ae214996cd4defea5ca3c792c6e3da0832d86980a34bcddbf22c` | Normalized into SQLite `ui_elements` |
| `Spline_Source_Index_2026-10-22.json` | `soren-spline-kb/data/Spline_Source_Index_2026-10-22.json` | 17,011 | `e9605f32fc92138ba7464d91792184497347056cda4648f5262967d8d71dff2e` | Extracted from ZIP archive |

### Excluded Artifacts & Security Audit
- **`Finalize-SorenGatewayJwt.ps1`**: Strictly **EXCLUDED**. PowerShell JWT gateway script containing potential authentication / secret patterns. Excluded from index and storage.

---

## 3. Live Documentation Ingestion Metrics
- **Source Index Endpoint**: `https://docs.spline.design/llms.txt` (`llms.txt` SHA-256: `66d84f884bfed8bcbd31a9dc9f5efdbb9b2be56a73c09bcae9fa7bc865e921d7`)
- **Total Markdown Doc Pages Crawled**: 191 pages
- **Successful Ingestions**: 191 pages (100% success rate)
- **Failed Ingestions**: 0 pages
- **Editor Modes Classifications**:
  - 3D Spatial Editor: 132 pages
  - Hana / 2D Design: 24 pages
  - Code / Integration: 21 pages
  - AI Tools / Generation: 8 pages
  - Dashboard / Files: 6 pages

---

## 4. Normalization & Provenance Audit
1. **Academy Catalog Transcript Audit**:
   - Total catalog entries: 29 video entries.
   - All entries verified with `has_full_transcript: false` / `is_transcript: false`.
   - Editorial video summaries explicitly labeled: *"Editorial summary / video metadata only; no video transcript reproduced."*
2. **SQLite FTS5 & Exact Indexing**:
   - `ui_elements`: 87 distinct elements with exact paths, shortcuts, and modes.
   - `doc_pages`: 191 indexed full-text pages with source URLs and SHA-256 hashes.
   - `academy_catalog`: 29 video items.
   - `kb_fts`: 307 full-text search documents indexed via FTS5 virtual table.
