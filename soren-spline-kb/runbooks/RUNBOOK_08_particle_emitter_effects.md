# Task Runbook 08: Creating Particle Emitter Systems and Visual Effects

## Workflow Overview
Generate dynamic visual particle effects such as sparklers, floating dust, rain, smoke, or ambient magic fields.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Active 3D scene.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `particle_tools`

## Exact UI Path
1. Top Toolbar -> **+ Add Object** -> Select **Particle System**.
2. Right Sidebar -> **Particles** Panel:
   - **Emitter Type**: Point, Box, Sphere, Mesh.
   - **Rate / Count**: Set particles per second.
   - **Life / Speed**: Particle lifespan duration and velocity.
   - **Size & Fade**: Start size, end size, opacity decay curve.
   - **Shape / Material**: Assign custom mesh or sprite texture to individual particles.

## Expected Outcomes
- Continuous or event-triggered particle streams flowing from emitter bounds.

## Failure Recovery & Common Pitfalls
- **Problem**: High particle count causes frame rate drops.
- **Fix**: Lower particle count / emission rate and shorten particle lifetime.

## Source References
- [Particle Emitter Docs](https://docs.spline.design/designing-in-3-d/particles/particle-emitter)
