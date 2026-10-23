# Task Runbook 03: Designing a 2D Interactive UI Card in Hana

## Workflow Overview
Utilize Hana canvas layout tools, glass effect, and progressive blur to craft modern 2D UI components.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Hana Mode active (Toggle Hana mode from Top Toolbar).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools`

## Exact UI Path
1. Switch to **Hana** mode in top bar.
2. Press `F` or select Frame tool -> Draw a frame container on canvas.
3. Right Sidebar -> **Layout**: Set Auto Layout (Flex / Fill / Hug), Padding (e.g. 24px), Gap (12px).
4. Add child layers: Text layers, Image layers, Shapes.
5. Right Sidebar -> **Effects**: Add **Progressive Blur** or **3D Shape Effect**.
6. Apply **Corners**: Set corner radius to 16px.

## Expected Outcomes
- Responsive 2D card element with clean auto-layout and visual depth ready for 3D/2D embedding.

## Failure Recovery & Common Pitfalls
- **Problem**: Elements overlap unexpectedly in frame.
- **Fix**: Ensure Auto Layout direction (Horizontal / Vertical) and distribution (Packed / Space Between) are configured correctly.

## Source References
- [Hana Basics Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana)
- Academy Tutorial: *Get Started with Interactive 2D in Hana*
