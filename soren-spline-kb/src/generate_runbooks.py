import os

RUNBOOKS_DIR = "/app/soren-spline-kb/runbooks"
os.makedirs(RUNBOOKS_DIR, exist_ok=True)

runbooks_data = [
    {
        "filename": "RUNBOOK_01_create_3d_glass_material.md",
        "content": """# Task Runbook 01: Creating Glass & Physical Translucent Materials in 3D

## Workflow Overview
Create realistic refractive glass or liquid glass materials on 3D mesh geometry in Spline's 3D Spatial Editor.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- A 3D mesh object (e.g., Sphere, Cube, Custom Mesh) selected in the viewport.
- Renderer setting supporting physical materials.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `material_tools` (e.g. `add_material_layer`, `update_material_layer`)

## Exact UI Path
1. Right Sidebar -> **Material** panel.
2. Click **+** to add a new Material Layer.
3. Open layer type dropdown -> Select **Glass** or **Physical**.
4. Configure Glass properties:
   - **Color / Opacity**: Set alpha / tint color.
   - **Blur**: Adjust internal blur strength (e.g., 10-30).
   - **Refm / Index of Refraction (IOR)**: Standard glass = ~1.45 to 1.52.
   - **Thickness**: Set internal volume thickness.
   - **Specular / Roughness**: Lower roughness (0.05-0.1) for clear glass.

## Expected Outcomes
- The selected object exhibits real-time refraction, glossy highlights, and semi-transparency in the viewport.

## Failure Recovery & Common Pitfalls
- **Problem**: Glass appears solid dark or invisible.
- **Fix**: Ensure background or HDR environment lighting is enabled in **Scene** -> **Environment** so glass has light/reflections to refract.

## Source References
- [Glass Material Layer Docs](https://docs.spline.design/materials-shading/basics/glass-layer)
- Academy Tutorial: *Create Liquid Glass Materials in 3D*
"""
    },
    {
        "filename": "RUNBOOK_02_interactive_hover_states.md",
        "content": """# Task Runbook 02: Building Interactive Hover and Click States

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
"""
    },
    {
        "filename": "RUNBOOK_03_hana_interactive_card_2d.md",
        "content": """# Task Runbook 03: Designing a 2D Interactive UI Card in Hana

## Workflow Overview
Utilize Hana canvas layout tools, glass effect, and progressive blur to craft modern 2D UI components.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Hana Mode active (Toggle Hana mode from Top Toolbar).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools`

## Exact UI Path
1. Switch to **Hana** mode in top bar.
2. Press `F` or select Frame tool -> Draw a frame container on canvas.
3. Right Sidebar -> **Layout**: Set Auto Layout (Flex / Fill / Hug), Padding (e.g. 24px), Gap (12px).
4. Add child layers: Text layers, Image layers, Shapes.
5. Right Sidebar -> **Effects**: Add **Progressive Blur** or **3D Shape Effect**.
6. Apply **Corners**: Set corner radius to 16px.

## Expected Outcomes
- Responsive 2D card element with clean auto-layout and visual depth ready for 3D/2D embedding.

## Failure Recovery & Common Pitfalls
- **Problem**: Elements overlap unexpectedly in frame.
- **Fix**: Ensure Auto Layout direction (Horizontal / Vertical) and distribution (Packed / Space Between) are configured correctly.

## Source References
- [Hana Basics Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana)
- Academy Tutorial: *Get Started with Interactive 2D in Hana*
"""
    },
    {
        "filename": "RUNBOOK_04_3d_scroll_driven_animation.md",
        "content": """# Task Runbook 04: Setting Up 3D Scroll-Driven Animations

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
"""
    },
    {
        "filename": "RUNBOOK_05_physics_rigid_bodies_collision.md",
        "content": """# Task Runbook 05: Enabling Physics Rigid Bodies and Collisions

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
"""
    },
    {
        "filename": "RUNBOOK_06_variable_logic_conditional_actions.md",
        "content": """# Task Runbook 06: Implementing Variable Logic and Conditional Actions

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
"""
    },
    {
        "filename": "RUNBOOK_07_lighting_shadows_hdri.md",
        "content": """# Task Runbook 07: Configuring Lighting, Soft Shadows, and HDRI Environment

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
"""
    },
    {
        "filename": "RUNBOOK_08_particle_emitter_effects.md",
        "content": """# Task Runbook 08: Creating Particle Emitter Systems and Visual Effects

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
"""
    },
    {
        "filename": "RUNBOOK_09_export_web_embed_spline_viewer.md",
        "content": """# Task Runbook 09: Exporting and Embedding Interactive Web Scenes (<spline-viewer>)

## Workflow Overview
Publish a live 3D scene and embed it seamlessly into web applications using official Spline web component tags.

## Primary Editor Mode
Dashboard & Export Panel

## Prerequisites
- Completed scene ready for production release.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `export_tools`

## Exact UI Path
1. Top Bar -> Click **Export** button.
2. Select **Web Content** -> **Public URL / Embed**.
3. Configure Export Options:
   - **Orbit Controls**: Enable/disable pan, zoom, rotate.
   - **Background**: Transparent or Solid Color.
   - **Page Scroll Interactivity**: Enable if using scroll-driven events.
4. Click **Update Public URL / Generate Code**.
5. Copy embed snippet: `<script type="module" src="https://unpkg.com/@splinetool/viewer/build/spline-viewer.js"></script><spline-viewer url="https://prod.spline.design/.../scene.splinecode"></spline-viewer>`.

## Expected Outcomes
- Performant, fully interactive 3D web canvas embedded in standard HTML/React/Webflow page.

## Failure Recovery & Common Pitfalls
- **Problem**: Scene shows dark gray background instead of transparent canvas.
- **Fix**: In Export Panel, set Background to `Transparent` before copying embed link.

## Source References
- [Export as Spline Viewer Docs](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer)
"""
    },
    {
        "filename": "RUNBOOK_10_code_api_react_three_fiber.md",
        "content": """# Task Runbook 10: Integrating Spline Code API with React & Three.js

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
"""
    },
    {
        "filename": "RUNBOOK_11_camera_transition_multi_scene.md",
        "content": """# Task Runbook 11: Setting Up Multi-Camera Transitions and Scene Cameras

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
"""
    },
    {
        "filename": "RUNBOOK_12_hana_path_animation.md",
        "content": """# Task Runbook 12: Animating Along a Path in Hana & 3D

## Workflow Overview
Guide shapes, text, or 3D objects along vector path curves smoothly.

## Primary Editor Mode
Hana / 2D Design & 3D Spatial Editor

## Prerequisites
- A Vector Path line drawn in canvas/viewport.
- Target object to attach to path.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `path_tools` / `animation_tools`

## Exact UI Path
1. Draw path using Vector Tool (`V`).
2. Select target object and vector path -> Right Click -> **Attach to Path** or check **Animate Along Path**.
3. Right Sidebar -> **Path Controls**:
   - **Progress**: 0% to 100%.
   - **Orient to Path**: Toggle align rotation to curve normal.
4. Add Event -> **Start** or **Hover** -> Action: **Transition Progress 0% -> 100%**.

## Expected Outcomes
- Object smoothly travels along the curved vector line trajectory.

## Failure Recovery & Common Pitfalls
- **Problem**: Object flips direction upside down along sharp curve corners.
- **Fix**: Adjust vector curve handles to avoid inflection points or disable Orient to Path.

## Source References
- Academy Tutorial: *How to Animate Along a Path with Hana and Spline*
"""
    },
    {
        "filename": "RUNBOOK_13_3d_text_typography_extrusion.md",
        "content": """# Task Runbook 13: Creating Dynamic 3D Text with Custom Typography & Extrusion

## Workflow Overview
Convert custom fonts and typography into fully extruded 3D geometric meshes with bevels.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Text layer in scene.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `text_tools` / `modeling_tools`

## Exact UI Path
1. Top Toolbar -> **+ Add Text** (`T`).
2. Right Sidebar -> **Text** Panel:
   - Font Family (Select Google Fonts or Upload `.ttf`/`.woff2`).
   - Size, Alignment, Line Height.
3. Right Sidebar -> **3D Text / Geometry**:
   - **Extrusion**: Depth thickness (e.g. 20px).
   - **Bevel**: Radius and curve segments.
   - **Curve Quality**: Smoothness resolution.

## Expected Outcomes
- Clean, extruded 3D text geometry ready for custom materials and lighting.

## Failure Recovery & Common Pitfalls
- **Problem**: Text letters overlap or exhibit self-intersecting geometry artifacts.
- **Fix**: Lower Bevel radius or increase letter spacing (tracking).

## Source References
- [Working with Text Docs](https://docs.spline.design/designing-in-3-d/objects/working-with-text)
"""
    },
    {
        "filename": "RUNBOOK_14_hana_liquid_glass_interactive_switch.md",
        "content": """# Task Runbook 14: Creating an Interactive UI Switch with Liquid Glass in Hana

## Workflow Overview
Combine Hana 2D states, liquid glass blur, and mouse follow interaction for a UI toggle switch.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Active Hana Mode canvas.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools` / `material_tools`

## Exact UI Path
1. Create background container frame and rounded pill handle.
2. Apply **Glass** material layer to pill handle with internal blur (20px).
3. Right Sidebar -> **States**:
   - **Base State**: Switch position LEFT (Off).
   - **State 2**: Switch position RIGHT (On) + Color glow change.
4. Right Sidebar -> **Events**:
   - Add **Mouse Down** -> Action: **Toggle State**.

## Expected Outcomes
- Tactile, liquid-glass visual toggle switch with smooth state transitions on click.

## Failure Recovery & Common Pitfalls
- **Problem**: Glass blur looks flat.
- **Fix**: Ensure background frame has rich underlying colors or gradients to diffuse blur.

## Source References
- Academy Tutorial: *Design Interactions with Liquid Glass & 3D Transforms in Hana*
"""
    },
    {
        "filename": "RUNBOOK_15_importing_3d_gltf_usdz_optimization.md",
        "content": """# Task Runbook 15: Importing 3D Models (glTF/USDZ/FBX) and Polygon Optimization

## Workflow Overview
Import external 3D CAD/DCC models into Spline and optimize polygon count for web performance.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- `.gltf`, `.glb`, `.fbx`, or `.usdz` 3D model file.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `asset_import_tools` / `mesh_tools`

## Exact UI Path
1. Drag and drop file onto Spline viewport OR Top Menu -> **File** -> **Import**.
2. Select imported parent model -> Right Sidebar -> **Geometry** panel.
3. Check Polycount in viewport stats.
4. If polycount is high (>100k triangles) -> Right Sidebar -> **Simplify / Decimate Mesh**.
5. Adjust reduction percentage (e.g. 50%) and verify topology preserve normals.

## Expected Outcomes
- Clean imported 3D model with optimized polygon count for smooth 60fps web rendering.

## Failure Recovery & Common Pitfalls
- **Problem**: Materials import pitch black or missing textures.
- **Fix**: Re-link missing texture images in Material panel or convert materials to Standard/Physical.

## Source References
- [Importing Assets Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/importing-assets-to-hana)
"""
    },
    {
        "filename": "RUNBOOK_16_ai_3d_generation_and_texture_mapping.md",
        "content": """# Task Runbook 16: Using AI 3D Generation & AI Texture Synthesis

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
"""
    },
    {
        "filename": "RUNBOOK_17_realtime_api_data_visualization.md",
        "content": """# Task Runbook 17: Connecting 3D Visuals to Real-Time REST APIs and Data

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
"""
    },
    {
        "filename": "RUNBOOK_18_hana_responsive_constraints_autolayout.md",
        "content": """# Task Runbook 18: Implementing Responsive Auto Layout Constraints in Hana

## Workflow Overview
Construct responsive UI components that adapt dynamically to different screen dimensions and aspect ratios.

## Primary Editor Mode
Hana / 2D Design

## Prerequisites
- Multi-element UI canvas in Hana mode.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `hana_2d_tools`

## Exact UI Path
1. Select outer Frame -> Right Sidebar -> **Layout** -> Enable **Auto Layout**.
2. Direction: Horizontal (`Row`) or Vertical (`Column`).
3. Alignment: Top/Center/Bottom, Left/Center/Right.
4. Child Sizing: Set widths/heights to `Fixed`, `Hug Contents`, or `Fill Container`.
5. Constraints: Set Pin to Top/Bottom/Left/Right/Center.

## Expected Outcomes
- UI layout resizes fluidly without breaking spacing, alignment, or content boundaries.

## Failure Recovery & Common Pitfalls
- **Problem**: Text truncates unexpectedly on small viewports.
- **Fix**: Set text sizing constraint to `Fill Container` with Auto Height enabled.

## Source References
- [Auto Layout & Constraints Docs](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints)
"""
    },
    {
        "filename": "RUNBOOK_19_audio_sound_effects_spatial_trigger.md",
        "content": """# Task Runbook 19: Adding Spatial Audio and Interactive Sound Triggers

## Workflow Overview
Trigger ambient sound effects or 3D positional audio when users interact with scene elements.

## Primary Editor Mode
3D Spatial Editor

## Prerequisites
- Sound file (`.mp3` or `.wav`).

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `audio_tools` / `event_tools`

## Exact UI Path
1. Right Sidebar -> **Events** -> Add Event (e.g. **Mouse Down** or **Trigger Area / Proximity**).
2. Action -> **Play Sound**.
3. Sound Asset -> Upload audio file or select from library.
4. Sound Settings:
   - Volume (0.0 to 1.0).
   - Loop (Toggle On/Off).
   - Spatial Audio (Toggle On -> Distance attenuation curve).

## Expected Outcomes
- Audio playback triggers instantly upon user interaction or proximity entry.

## Failure Recovery & Common Pitfalls
- **Problem**: Audio fails to play automatically on page load.
- **Fix**: Modern web browsers block unmuted autoplay without user gesture; attach audio trigger to user click/hover event instead.

## Source References
- [Sound Action Docs](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action)
"""
    },
    {
        "filename": "RUNBOOK_20_version_history_collaboration.md",
        "content": """# Task Runbook 20: Managing Version History, Branching, and Multi-User Collaboration

## Workflow Overview
Manage version snapshots, restore previous project states, and collaborate live with team members.

## Primary Editor Mode
Dashboard & Top Navigation Menu

## Prerequisites
- Active project in Spline workspace.

## Native Spline MCP Tool Families & Execution Authority
- Execution Authority: `spline_mcp` / Agent Skill
- Tool Family: `workspace_tools` / `version_tools`

## Exact UI Path
1. Top Menu -> Click Project Title -> Select **Version History**.
2. Right Panel shows chronological snapshot commits.
3. To save explicit version: Click **Save Version Snapshot** -> Enter Name & Notes.
4. To restore: Click snapshot context menu -> Select **Restore this version** or **Duplicate as new file**.
5. Live Collaboration: Click **Share** button at top right -> Add team email addresses with Edit/View permissions.

## Expected Outcomes
- Safe project state tracking, instant rollback safety net, and concurrent real-time multi-user editing.

## Failure Recovery & Common Pitfalls
- **Problem**: Accidentally overwrote scene changes.
- **Fix**: Open Version History, locate auto-save snapshot prior to edit, and click Restore.

## Source References
- [Version History Docs](https://docs.spline.design/designing-in-3-d/scenes/version-history)
"""
    }
]

for rb in runbooks_data:
    path = os.path.join(RUNBOOKS_DIR, rb["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(rb["content"].strip() + "\n")

print(f"Generated {len(runbooks_data)} priority runbooks in {RUNBOOKS_DIR}.")
