# SOREN Spline Knowledge Base v1 - Gap Analysis & Recommendations

## 1. Overview
During the ingestion, indexing, and synthesis process of SOREN Spline Knowledge Base v1, several coverage gaps, video transcript limitations, and API boundaries were identified.

---

## 2. Identified Coverage Gaps & Artifact Differences

### GAP-01: Absence of Full Academy Video Transcripts
- **Description**: The video catalog (`Spline_Academy_Video_Catalog_2026-10-22.csv`) provides high-level metadata (title, level, duration, URLs, category) but does **not** contain full word-for-word spoken video transcripts.
- **Impact**: Deep conversational speech search inside video content is unavailable.
- **Mitigation / Status**: Video entries are strictly flagged `has_full_transcript: false`. Editorial summaries are indexed under clear disclaimer labels to prevent hallucination.
- **Recommendation**: Integrate YouTube automated transcript extraction APIs in v2 ingestion pipelines if required.

### GAP-02: Conditional Panel UI Context Variability
- **Description**: Certain context-sensitive panels in Spline (e.g., Vector Mesh Edit mode, Component Master override panels, Gaussian Splatting parameters) appear dynamically based on object selection.
- **Impact**: Static UI element listings may require active context hints during runbook execution.
- **Mitigation**: All 20 priority runbooks specify exact prerequisite selection states before outlining UI navigation paths.

### GAP-03: Real-Time API Endpoint Authorization Boundaries
- **Description**: While Spline supports live HTTP GET triggers in-engine, full OAuth / POST body payloads are limited in native client UI without custom JS wrapper code.
- **Mitigation**: Runbook 17 details standard REST GET binding procedures and specifies CORS header requirements for external servers.

---

## 3. Maintenance & Incremental Reindexing Recommendations
1. **Automated `llms.txt` Sync**: Run `python3 soren-spline-kb/src/doc_ingester.py` on a weekly cron schedule. Content SHA-256 comparison will ensure only changed markdown pages trigger reindexing.
2. **Spline Release Monitoring**: Track major release notes for Spline Hana / v2 updates to update UI element shortcuts and location strings.
