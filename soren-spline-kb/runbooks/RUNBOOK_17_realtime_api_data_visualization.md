# Task Runbook 17: Connecting 3D Visuals to Real-Time REST APIs and Data

## Workflow Overview
Drive 3D scale, rotation, color, or text content in real time using external HTTP REST APIs.

## Primary Editor Mode
3D Spatial Editor & Logic Panel

## Prerequisites
- Accessible JSON REST API endpoint.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `api_tools` / `variable_tools`

## Exact UI Path
1. Left Sidebar -> **Variables** -> Add Variable `apiTemp` (Number).
2. Right Sidebar -> **Events** -> Add **Start** event.
3. Action -> **Fetch API / HTTP Request**:
   - URL: `https://api.weather.com/...`
   - Method: `GET`
   - Response Mapping: Map `data.temp` -> Variable `apiTemp`.
4. Add **Variable Change** event for `apiTemp` -> Action: **Update Object Scale Y** or **Material Color Interpolation**.

## Expected Outcomes
- 3D scene elements dynamically reflect real-time live data feeds automatically.

## Failure Recovery & Common Pitfalls
- **Problem**: API call fails with CORS error in web preview.
- **Fix**: Ensure target API server allows cross-origin requests (`Access-Control-Allow-Origin: *`) or use proxy.

## Source References
- [Real-time API Docs](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api)
