# Task Runbook 09: Exporting and Embedding Interactive Web Scenes (<spline-viewer>)

## Workflow Overview
Publish a live 3D scene and embed it seamlessly into web applications using official Spline web component tags.

## Primary Editor Mode
Dashboard & Export Panel

## Prerequisites
- Completed scene ready for production release.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `export_tools`

## Exact UI Path
1. Top Bar -> Click **Export** button.
2. Select **Web Content** -> **Public URL / Embed**.
3. Configure Export Options:
   - **Orbit Controls**: Enable/disable pan, zoom, rotate.
   - **Background**: Transparent or Solid Color.
   - **Page Scroll Interactivity**: Enable if using scroll-driven events.
4. Click **Update Public URL / Generate Code**.
5. Copy embed snippet: `<script type="module" src="https://unpkg.com/@splinetool/viewer/build/spline-viewer.js"></script><spline-viewer url="https://prod.spline.design/.../scene.splinecode"></spline-viewer>`.

## Expected Outcomes
- Performant, fully interactive 3D web canvas embedded in standard HTML/React/Webflow page.

## Failure Recovery & Common Pitfalls
- **Problem**: Scene shows dark gray background instead of transparent canvas.
- **Fix**: In Export Panel, set Background to `Transparent` before copying embed link.

## Source References
- [Export as Spline Viewer Docs](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer)
