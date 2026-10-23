# Task Runbook 07: Configuring Lighting, Soft Shadows, and HDRI Environment

## Workflow Overview
Set up professional lighting rigs, directional key lights, drop shadows, and image-based HDRI environment maps.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Active 3D scene.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `lighting_tools` / `scene_environment`

## Exact UI Path
1. Top Toolbar -> **+ Add Light** -> Select **Directional Light** or **Point Light**.
2. Right Sidebar -> **Light** Panel:
   - **Color & Intensity**: Set exposure intensity.
   - **Shadows**: Toggle **Shadows ON**.
   - **Shadow Softness / Bias**: Fine-tune penumbra blur.
3. Click empty background -> Right Sidebar -> **Scene**:
   - **Environment**: Select **HDRI Preset** or upload custom `.hdr` file.
   - **Exposure & Rotation**: Tune ambient illumination intensity.

## Expected Outcomes
- Dynamic key lighting with realistic soft contact shadows and environmental reflection maps.

## Failure Recovery & Common Pitfalls
- **Problem**: Shadows appear pixelated or jagged.
- **Fix**: Increase Shadow Map Resolution in Scene Performance settings or adjust Shadow Map Bias.

## Source References
- [Lighting Docs](https://docs.spline.design/lighting/working-with-lights)
