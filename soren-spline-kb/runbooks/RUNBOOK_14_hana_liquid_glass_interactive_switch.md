# Task Runbook 14: Creating an Interactive UI Switch with Liquid Glass in Hana

## Workflow Overview
Combine Hana 2D states, liquid glass blur, and mouse follow interaction for a UI toggle switch.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Active Hana Mode canvas.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools` / `material_tools`

## Exact UI Path
1. Create background container frame and rounded pill handle.
2. Apply **Glass** material layer to pill handle with internal blur (20px).
3. Right Sidebar -> **States**:
   - **Base State**: Switch position LEFT (Off).
   - **State 2**: Switch position RIGHT (On) + Color glow change.
4. Right Sidebar -> **Events**:
   - Add **Mouse Down** -> Action: **Toggle State**.

## Expected Outcomes
- Tactile, liquid-glass visual toggle switch with smooth state transitions on click.

## Failure Recovery & Common Pitfalls
- **Problem**: Glass blur looks flat.
- **Fix**: Ensure background frame has rich underlying colors or gradients to diffuse blur.

## Source References
- Academy Tutorial: *Design Interactions with Liquid Glass & 3D Transforms in Hana*
