# Task Runbook 11: Setting Up Multi-Camera Transitions and Scene Cameras

## Workflow Overview
Define distinct camera perspectives and smoothly transition between camera angles during user interaction.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Scene with multiple key points of interest.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `camera_tools`

## Exact UI Path
1. Top Toolbar -> **+ Add Camera** -> Position camera in 3D viewport.
2. Select Camera -> Right Sidebar -> **Camera** Panel (Field of View, Near/Far Clipping).
3. Right Sidebar -> **States** -> Create **State 2** for Camera (move target position/rotation).
4. Select Trigger Button -> **Events** -> Add **Mouse Down** -> Action: **Transition**.
5. Target: Select `Camera Object` -> State: `State 2`.

## Expected Outcomes
- Cinematic smooth camera transit when user clicks or triggers transition.

## Failure Recovery & Common Pitfalls
- **Problem**: Transition clips through scene geometry.
- **Fix**: Adjust easing curve or add intermediate waypoint camera states.

## Source References
- [Camera Docs](https://docs.spline.design/designing-in-3-d/cameras/working-with-cameras)
