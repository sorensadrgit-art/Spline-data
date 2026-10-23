# Task Runbook 20: Managing Version History, Branching, and Multi-User Collaboration

## Workflow Overview
Manage version snapshots, restore previous project states, and collaborate live with team members.

## Primary Editor Mode
Dashboard & Top Navigation Menu

## Prerequisites
- Active project in Spline workspace.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `workspace_tools` / `version_tools`

## Exact UI Path
1. Top Menu -> Click Project Title -> Select **Version History**.
2. Right Panel shows chronological snapshot commits.
3. To save explicit version: Click **Save Version Snapshot** -> Enter Name & Notes.
4. To restore: Click snapshot context menu -> Select **Restore this version** or **Duplicate as new file**.
5. Live Collaboration: Click **Share** button at top right -> Add team email addresses with Edit/View permissions.

## Expected Outcomes
- Safe project state tracking, instant rollback safety net, and concurrent real-time multi-user editing.

## Failure Recovery & Common Pitfalls
- **Problem**: Accidentally overwrote scene changes.
- **Fix**: Open Version History, locate auto-save snapshot prior to edit, and click Restore.

## Source References
- [Version History Docs](https://docs.spline.design/designing-in-3-d/scenes/version-history)
