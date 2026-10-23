# Task Runbook 15: Importing 3D Models (glTF/USDZ/FBX) and Polygon Optimization

## Workflow Overview
Import external 3D CAD/DCC models into Spline and optimize polygon count for web performance.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- `.gltf`, `.glb`, `.fbx`, or `.usdz` 3D model file.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `asset_import_tools` / `mesh_tools`

## Exact UI Path
1. Drag and drop file onto Spline viewport OR Top Menu -> **File** -> **Import**.
2. Select imported parent model -> Right Sidebar -> **Geometry** panel.
3. Check Polycount in viewport stats.
4. If polycount is high (>100k triangles) -> Right Sidebar -> **Simplify / Decimate Mesh**.
5. Adjust reduction percentage (e.g. 50%) and verify topology preserve normals.

## Expected Outcomes
- Clean imported 3D model with optimized polygon count for smooth 60fps web rendering.

## Failure Recovery & Common Pitfalls
- **Problem**: Materials import pitch black or missing textures.
- **Fix**: Re-link missing texture images in Material panel or convert materials to Standard/Physical.

## Source References
- [Importing Assets Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/importing-assets-to-hana)
