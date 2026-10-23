# Task Runbook 16: Using AI 3D Generation & AI Texture Synthesis

## Workflow Overview
Generate 3D meshes and custom material textures from natural language prompts using Spline AI.

## Primary Editor Mode
3D Spatial Editor & AI Prompt Bar

## Prerequisites
- Active internet connection with AI tool access.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `ai_tools`

## Exact UI Path
1. Top Bar -> Click **AI** button or press `Cmd/Ctrl + K` -> Select **Generate 3D**.
2. Type prompt: e.g. *"A futuristic sleek mechanical drone"*.
3. Review candidate variations -> Select **Apply to Canvas**.
4. To generate AI Texture: Select object -> Material Panel -> Click **AI Style / Texture Generator** -> Enter style prompt.

## Expected Outcomes
- Complete 3D mesh object and custom seamless material texture generated in seconds.

## Failure Recovery & Common Pitfalls
- **Problem**: AI mesh output is too complex or dirty topology.
- **Fix**: Apply Remesh / Simplify operation or smooth normals in geometry panel.

## Source References
- [AI 3D Generation Docs](https://docs.spline.design/generate/ai-3d-generation)
