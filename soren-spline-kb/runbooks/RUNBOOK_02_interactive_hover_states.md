# Task Runbook 02: Building Interactive Hover and Click States

## Workflow Overview
Configure real-time interactive states and transitions triggered by user mouse events in 3D or 2D scenes.

## Primary Editor Mode
3D Spatial Editor & Hana / 2D Design

## Prerequisites
- Target 3D object or Hana frame/layer.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `state_tools` and `event_tools`

## Exact UI Path
1. Right Sidebar -> **States** panel.
2. Click **+** to create a base state (**Base State** is created automatically, add **State 2** / **Hover State**).
3. Select **State 2** and modify target properties (e.g. Scale to 1.1x, Position offset, Material Color change).
4. Right Sidebar -> **Events** panel.
5. Click **+** -> Select **Mouse Hover** or **Mouse Down**.
6. Set Action -> **Transition**.
7. Target -> Select current object; State -> Transition to **State 2**.
8. Set Duration (e.g. 0.3s) and Easing (e.g. Ease Out / Elastic).

## Expected Outcomes
- Hovering or clicking the object smoothly transitions between base state and target state.

## Failure Recovery & Common Pitfalls
- **Problem**: Hover interaction triggers repeatedly in a loop.
- **Fix**: Check hit area geometry or parent bounding box to ensure state change doesn't move object outside mouse boundary.

## Source References
- [States and Events Docs](https://docs.spline.design/interaction-states-events-and-actions/basics/states-and-events)
