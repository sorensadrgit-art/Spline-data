# Task Runbook 01: Creating Glass & Physical Translucent Materials in 3D

## Workflow Overview
Create realistic refractive glass or liquid glass materials on 3D mesh geometry in Spline's 3D Spatial Editor.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- A 3D mesh object (e.g., Sphere, Cube, Custom Mesh) selected in the viewport.
- Renderer setting supporting physical materials.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `material_tools` (e.g. `add_material_layer`, `update_material_layer`)

## Exact UI Path
1. Right Sidebar -> **Material** panel.
2. Click **+** to add a new Material Layer.
3. Open layer type dropdown -> Select **Glass** or **Physical**.
4. Configure Glass properties:
   - **Color / Opacity**: Set alpha / tint color.
   - **Blur**: Adjust internal blur strength (e.g., 10-30).
   - **Refm / Index of Refraction (IOR)**: Standard glass = ~1.45 to 1.52.
   - **Thickness**: Set internal volume thickness.
   - **Specular / Roughness**: Lower roughness (0.05-0.1) for clear glass.

## Expected Outcomes
- The selected object exhibits real-time refraction, glossy highlights, and semi-transparency in the viewport.

## Failure Recovery & Common Pitfalls
- **Problem**: Glass appears solid dark or invisible.
- **Fix**: Ensure background or HDR environment lighting is enabled in **Scene** -> **Environment** so glass has light/reflections to refract.

## Source References
- [Glass Material Layer Docs](https://docs.spline.design/materials-shading/basics/glass-layer)
- Academy Tutorial: *Create Liquid Glass Materials in 3D*
