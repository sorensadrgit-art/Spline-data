# Task Runbook 12: Animating Along a Path in Hana & 3D

## Workflow Overview
Guide shapes, text, or 3D objects along vector path curves smoothly.

## Primary Editor Mode
Hana / 2D Design & 3D Spatial Editor

## Prerequisites
- A Vector Path line drawn in canvas/viewport.
- Target object to attach to path.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `path_tools` / `animation_tools`

## Exact UI Path
1. Draw path using Vector Tool (`V`).
2. Select target object and vector path -> Right Click -> **Attach to Path** or check **Animate Along Path**.
3. Right Sidebar -> **Path Controls**:
   - **Progress**: 0% to 100%.
   - **Orient to Path**: Toggle align rotation to curve normal.
4. Add Event -> **Start** or **Hover** -> Action: **Transition Progress 0% -> 100%**.

## Expected Outcomes
- Object smoothly travels along the curved vector line trajectory.

## Failure Recovery & Common Pitfalls
- **Problem**: Object flips direction upside down along sharp curve corners.
- **Fix**: Adjust vector curve handles to avoid inflection points or disable Orient to Path.

## Source References
- Academy Tutorial: *How to Animate Along a Path with Hana and Spline*
