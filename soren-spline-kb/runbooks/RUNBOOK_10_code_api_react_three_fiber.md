# Task Runbook 10: Integrating Spline Code API with React & Three.js

## Workflow Overview
Control Spline scene objects, trigger animations, and listen to events programmatic in React via `@splinetool/react-spline`.

## Primary Editor Mode
Code / Export Integration

## Prerequisites
- Node.js project with React installed (`npm i @splinetool/react-spline @splinetool/runtime`).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `export_tools` / `code_api`

## Exact UI Path
1. Export Panel -> Select **Code** -> Select **React**.
2. Import Spline in React component:
   ```jsx
   import Spline from '@splinetool/react-spline';

   export default function App() {
     function onLoad(splineApp) {
       const obj = splineApp.findObjectByName('Cube');
       console.log('Found object:', obj);
     }
     return <Spline scene="https://prod.spline.design/XXXXX/scene.splinecode" onLoad={onLoad} />;
   }
   ```

## Expected Outcomes
- Full programmatic control over 3D scene objects via React state and event handlers.

## Failure Recovery & Common Pitfalls
- **Problem**: `findObjectByName` returns `null`.
- **Fix**: Verify exact object layer name in Spline Outliner (case-sensitive).

## Source References
- [React Spline Integration Docs](https://docs.spline.design/exporting-your-scene/web/exporting-as-code)
