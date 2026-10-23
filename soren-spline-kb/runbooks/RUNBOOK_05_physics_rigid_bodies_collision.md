# Task Runbook 05: Enabling Physics Rigid Bodies and Collisions

## Workflow Overview
Simulate gravity, bouncing, collisions, and physical object interactions in real time.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- 3D mesh geometry (Dynamic objects and Ground/Static objects).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `physics_tools`

## Exact UI Path
1. Select Ground object -> Right Sidebar -> **Physics** panel.
2. Toggle Physics **On** -> Set Body Type to **Static** (Mass = 0).
3. Select Falling/Dynamic object -> **Physics** panel.
4. Toggle Physics **On** -> Set Body Type to **Dynamic**.
5. Configure Physics attributes:
   - **Mass**: Object weight (kg).
   - **Friction**: Surface resistance (0.0 to 1.0).
   - **Bounciness / Restitution**: Bounce factor (0.0 to 1.0).
   - **Collider Shape**: Box, Sphere, Hull, or Mesh.

## Expected Outcomes
- Dynamic objects fall under scene gravity and collide realistically with static ground geometries.

## Failure Recovery & Common Pitfalls
- **Problem**: Objects fall through ground plane.
- **Fix**: Ensure ground object has Static body type enabled and collider shape fits geometry bounds.

## Source References
- [Physics Feature Docs](https://docs.spline.design/designing-in-3-d/physics/physics-overview)
