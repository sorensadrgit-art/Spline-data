# Task Runbook 18: Implementing Responsive Auto Layout Constraints in Hana

## Workflow Overview
Construct responsive UI components that adapt dynamically to different screen dimensions and aspect ratios.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Multi-element UI canvas in Hana mode.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools`

## Exact UI Path
1. Select outer Frame -> Right Sidebar -> **Layout** -> Enable **Auto Layout**.
2. Direction: Horizontal (`Row`) or Vertical (`Column`).
3. Alignment: Top/Center/Bottom, Left/Center/Right.
4. Child Sizing: Set widths/heights to `Fixed`, `Hug Contents`, or `Fill Container`.
5. Constraints: Set Pin to Top/Bottom/Left/Right/Center.

## Expected Outcomes
- UI layout resizes fluidly without breaking spacing, alignment, or content boundaries.

## Failure Recovery & Common Pitfalls
- **Problem**: Text truncates unexpectedly on small viewports.
- **Fix**: Set text sizing constraint to `Fill Container` with Auto Height enabled.

## Source References
- [Auto Layout & Constraints Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints)
