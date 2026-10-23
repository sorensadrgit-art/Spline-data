# Task Runbook 06: Implementing Variable Logic and Conditional Actions

## Workflow Overview
Store state, count user clicks, manage score/toggle states using Spline Variables and Conditional Actions.

## Primary Editor Mode
3D Spatial Editor & Hana

## Prerequisites
- Scene requiring dynamic state storage (e.g., toggle button, counter).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `variable_tools` / `logic_tools`

## Exact UI Path
1. Left/Right Sidebar -> **Variables** panel -> Click **+**.
2. Define Variable:
   - **Name**: e.g., `isMuted` or `clickCount`.
   - **Type**: Boolean, Number, or String.
   - **Initial Value**: `false` or `0`.
3. Select Interactive Object -> **Events** panel -> Add **Mouse Down**.
4. Action 1 -> **Set Variable**: Set `clickCount` = `clickCount + 1`.
5. Action 2 -> **Conditional Action**:
   - `IF clickCount >= 5 THEN Transition to State_Active ELSE Transition to State_Base`.

## Expected Outcomes
- Scene responds dynamically based on variable thresholds and evaluation logic.

## Failure Recovery & Common Pitfalls
- **Problem**: Variable value fails to update.
- **Fix**: Ensure variable scope is global and event execution order places `Set Variable` before `Conditional Action`.

## Source References
- [Variables Docs](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables)
