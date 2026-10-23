# Task Runbook 04: Setting Up 3D Scroll-Driven Animations

## Workflow Overview
Bind 3D object motion, camera transitions, or state interpolations directly to web page scroll events.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Scene with multi-state camera or target objects.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `event_tools` / `camera_tools`

## Exact UI Path
1. Right Sidebar -> **Events** panel.
2. Click **+** -> Select **Scroll** event.
3. Set **Trigger**: Select `Page Scroll` or `Element Scroll`.
4. Define Start/End boundaries (e.g., 0% to 100% viewport scroll).
5. Set Action -> **Transition** or **State Interpolation**.
6. Select Target Object or Camera and target State.

## Expected Outcomes
- As page scrolls, 3D camera smoothly moves through keyframes across the webpage section.

## Failure Recovery & Common Pitfalls
- **Problem**: Animation jumps erratically during scroll.
- **Fix**: Enable smooth damping / inertia in export viewer settings or web wrapper script.

## Source References
- [Scroll Event Docs](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event)
- Academy Tutorial: *Create a 3D Scroll Animation & Integrate into Framer*
