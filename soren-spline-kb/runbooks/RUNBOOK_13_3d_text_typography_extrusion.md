# Task Runbook 13: Creating Dynamic 3D Text with Custom Typography & Extrusion

## Workflow Overview
Convert custom fonts and typography into fully extruded 3D geometric meshes with bevels.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Text layer in scene.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `text_tools` / `modeling_tools`

## Exact UI Path
1. Top Toolbar -> **+ Add Text** (`T`).
2. Right Sidebar -> **Text** Panel:
   - Font Family (Select Google Fonts or Upload `.ttf`/`.woff2`).
   - Size, Alignment, Line Height.
3. Right Sidebar -> **3D Text / Geometry**:
   - **Extrusion**: Depth thickness (e.g. 20px).
   - **Bevel**: Radius and curve segments.
   - **Curve Quality**: Smoothness resolution.

## Expected Outcomes
- Clean, extruded 3D text geometry ready for custom materials and lighting.

## Failure Recovery & Common Pitfalls
- **Problem**: Text letters overlap or exhibit self-intersecting geometry artifacts.
- **Fix**: Lower Bevel radius or increase letter spacing (tracking).

## Source References
- [Working with Text Docs](https://docs.spline.design/designing-in-3-d/objects/working-with-text)
