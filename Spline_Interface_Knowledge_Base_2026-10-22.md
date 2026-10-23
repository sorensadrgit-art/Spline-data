# Spline Interface Knowledge Base

**Official-source research snapshot:** 22 October 2026  
**Primary scope:** Spline V2 3D Editor, Hana (2D), tools and panels, state-based interaction, Timeline, Code Tab, exports, shortcuts, and official Academy media.  
**Canonical sources:** <https://docs.spline.design/> · <https://academy.spline.design/> · <https://spline.design/tutorials> · <https://blog.spline.design/spline-v2>

> **Evidence standard.** This is a curated, source-linked reference, not a live DOM inventory. Firecrawl returned 210 documentation crawl entries (including auxiliary/alternate paths), 110 Academy crawl entries and 108 unique tutorial cards from the Academy listing. A page's inclusion in the URL index does **not** establish that each live submenu was independently inspected. Structured AI extraction was checked against the source documentation; unsupported shortcuts or click paths have not been adopted. The Spline app's live editor could not be exercised because the inspection browser lacked WebGL. Some Academy pages expose only a login shell to the crawler.
>
> **Video copyright/transcript status.** The source crawler did not obtain full caption transcripts. Entire third-party transcripts are not reproduced here. Every lesson includes its original watch links and an **editorial technical study outline** (not a claimed transcript). Only verified chapters/timestamps are listed. You can open a video's YouTube **Show transcript** control to read any captions the publisher makes available; availability varies.
>
> **Version note.** The August 20, 2026 V2 redesign added the three **Preview | Edit | Code** tabs, AI Agent, WebGPU-first rendering and new MCP/desktop workflows. Older educational videos may show the previous layout. Consult the V2 UI tour and current docs before memorizing screen coordinates.

## Contents

1. [Overall architecture](#1-overall-architecture)
2. [3D Editor — detailed UI map](#2-3d-editor--detailed-ui-map)
3. [Hana 2D Editor — detailed UI map](#3-hana-2d-editor--detailed-ui-map)
4. [Key tools and click paths](#4-key-tools-and-click-paths)
5. [Features, animation, interactivity and exports](#5-features-animation-interactivity-and-exports)
6. [Official video library](#6-official-video-library)
7. [Keyboard shortcuts — complete documented table](#7-keyboard-shortcuts--complete-documented-table)
8. [Documentation source directory](#8-documentation-source-directory)
9. [Structured extraction schema and QA](#9-structured-extraction-schema-and-qa)

---

## 1. Overall architecture

### Spline 3D Editor vs. Hana

| Dimension | Spline 3D Editor | Hana 2D Editor |
|---|---|---|
| Best for | 3D objects, spatial scenes, interactive web content, modeling, materials, cameras, physics | Canvas-first 2D UI, responsive frames, motion graphics, vector networks, 2.5D/3D treatments |
| Canvas | 3D viewport with orbit/pan/zoom | Infinite 2D canvas with frames, pages, sections and layers |
| Main left navigation | **Agent / Objects / Assets** | **Agent / Layers**, plus Pages list |
| Right inspector | Scene settings if nothing is selected; object settings otherwise | **Transform, Shape, Layout, States, Events, Fill, Stroke, Effects, Export** depending on selected element |
| Runtime mode | Three stage tabs: **Preview | Edit | Code** | **Play** control in left-side toolbar |
| Motion systems | Object states and events, Timeline/Graph Editor, physics/cloners/particles | States, events and actions; transition timing/springs; vector and effect animation |
| Code | In-file HTML/CSS/JS overlay with `spline` bridge; externally published Code APIs | Interactive native canvas export; Hana does not share the 3D Code stage tabs |
| Publishing | 3D viewer/public URL/code/self-hosted, images/videos, 3D files and selected native routes | Individual parent-frame public URL, iframe or `<hana-viewer>`, image/video; sections can be exported but are not Play screens |

Source: [Understanding Spline's UI](https://docs.spline.design/basics/understanding-splines-ui), [What is Hana?](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/what-is-hana), [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab).

### 1.1 Dashboard versus Editor

1. Open <https://app.spline.design/> or the Windows/macOS desktop application. Sign into your account where required.
2. On the **Dashboard**, use **Home**, **My files**, **Templates**, **Community**, or **Academy** from the sidebar. The workspace name switches the active workspace; project folders group files.
3. The file view supplies **My files / Shared with me**, filters, sorting, grid/list controls, folder creation and **+ Create**. Create the desired file type before entering an editor.
4. **Desktop application:** has its own file tab bar; its home icon returns to files, and **+** opens a new tab. **Browser:** each file ordinarily opens in a normal browser tab/window. The desktop app can host both 3D and Hana documents.
5. **3D file** opens the Spline editor; a **Hana – 2D Design** file opens Hana. These are distinct editors, not merely two editing modes in one 3D file.

### 1.2 Preview, Edit and Code — do not conflate them

| Stage | How to open | What happens | Important distinction |
|---|---|---|---|
| **Edit** | 3D editor > top **Edit** tab | Manipulate the bare 3D scene | Authored object events do not execute as Play interactions |
| **Preview (Play)** | Top **Preview** tab | Runs scene interaction and HTML overlay as visitors see it | Restart and full-screen chips appear by the tabs |
| **Code** | Top **Code** tab | Edit one HTML document carrying inline CSS/JS | Document is saved as part of Spline file and travels with supported runtime exports |
| **Hana Play** | Hana left toolbar > **Play** | Runs Hana state/action interactions | Hana has a different editor UI; do not look for the 3D Code tab here |

**Technical Code distinction:** Spline's in-file Code Tab uses a sandboxed iframe over the scene and an injected `spline` API; the [Code API for Web](https://docs.spline.design/exporting-your-scene/web/code-api-for-web) drives a separately published scene from a host application. JS changes to objects made at runtime are **transient** and reset when the scene reloads; scene edits made through the editor persist. Keep page background transparent if the 3D viewport should remain visible. HTML's unused background can pass pointer events through to the 3D viewport; custom interactive overlays capture their own pointer events. Custom three.js materials are not supported in `<spline-viewer>` embeds even though they can work in the editor and other web exports.

Sources: [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab), [Spline V2 announcement](https://blog.spline.design/spline-v2).

---

## 2. 3D Editor — detailed UI map

### 2.1 Spatial layout

```text
┌────────────────────────────── 3D EDITOR ─────────────────────────────────────────────┐
│ Left sidebar                  Stage / viewport                           Right panel│
│ ┌─────────────────────┐   Preview | Edit | Code                 ┌─────────────────┐│
│ │ Agent | Objects |   │   ┌──────────────────────────────────┐  │ Scene settings  ││
│ │ Assets              │   │                                  │  │    OR          ││
│ │ Scenes              │   │       Editable 3D viewport       │  │ Object settings ││
│ │ Searchable Outliner │   │                                  │  │ Transform       ││
│ │ Nested groups       │   │                                  │  │ Shape/Material  ││
│ │                     │   │                                  │  │ States/Events   ││
│ │                     │   └──────────────────────────────────┘  │ Modifiers etc.  ││
│ └─────────────────────┘   Add (+) • Transform • Timeline           └─────────────────┘│
│                     Zoom • Performance • Share • Export                            │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

This is a conceptual placement diagram, not a pixel-perfect screenshot. [Official annotated screenshot](https://docs.spline.design/basics/understanding-splines-ui).

### 2.2 Left sidebar: Agent / Objects / Assets

**Agent** (editor default): type prompts for the Spline AI assistant to edit **real scene elements**, not an image of the scene. The panel has New chat and Chat history, a prompt field, selection chips/attachments, model and effort selectors, and Send/Stop. `/image` generates image content; `/3d` generates a 3D model. Selecting an object before prompting scopes phrases like “this”. Prompts submitted while it is working queue in order; **Pause**, **Clear**, per-row remove and **Stop** manage that queue. Edits normally land in undo history. Agent usage may consume AI credits. [AI Agent docs](https://docs.spline.design/spline-ai/ai-agent).

**Objects**: opens the scene tree (**Outliner**) and a **Scenes** selector above it. Use the tree to select individual objects, nest groups, locate an object and reason about parent/child selection. Multi-scene files keep distinct environments/object sets. The selection changes the inspector at right. [Multi-Scenes](https://docs.spline.design/designing-in-3-d/scenes/multi-scenes).

**Assets**: the asset browser and workspace/team libraries for reusable materials, images or other saved design assets. Prefer reusable assets for duplicated materials. A linked component is different from a duplicate object. [Team Libraries](https://docs.spline.design/sharing-collaboration-and-workspaces/team-libraries), [Material Library](https://docs.spline.design/materials-shading/basics/material-library).

### 2.3 Top stage tabs and scene controls

- **Preview** plays interactions, physics and in-file code. Use the Preview restart/fullscreen chips for testing.
- **Edit** edits scene geometry, object properties, camera view, timeline and assets.
- **Code** contains the single in-file HTML document plus **Console** for logs and runtime errors.
- **Zoom / performance** inspect and adjust the viewport / runtime footprint as exposed by the current workspace.
- **Share** handles file collaboration; **Export** opens output routes and Play Settings.

### 2.4 Tool dock and object creation

The **+** entry opens the full list of available objects. The arrow icon is **Transform**, used for selecting, moving, scaling and rotating. Quick documented creation shortcuts include **R Rectangle**, **O Ellipse**, **K Triangle**, **J Polygon** (these are 3D-editor shortcuts, not Hana shortcuts). The viewport also hosts a Pen tool for editable vectors and **+ > Path** for true 3D paths. Spline supports 2D shapes in a 3D world; they have width/height and can be moved through XYZ space, while extrusion gives them physical depth.

**Mouse/trackpad camera controls on Windows:** Alt+drag = orbit, Space+drag = pan, Ctrl+wheel = zoom; on a trackpad, pinch/2-finger drag/Alt+tap-drag. On macOS replace Alt with Option and Ctrl with Cmd where documented. Press **S** to focus selection, **Shift+S** to orient to object, **M** to switch perspective/orthographic, **L** to switch local/world transform axes.

### 2.5 Right-hand Property Panels: conditional layout

When nothing is selected, the inspector describes **the scene**: background color, environment/sky/HDRi, lighting, simulation, fog, effects/post-processing, ambient shadows, color. Select an object and the inspector changes to its object-type controls such as **Transform**, **Shape**, **Material**, **Modifiers**, **Shadows**, **Physics**, **States**, **Events** and object-specific parameters. **Not every section appears for every type**. Scene settings should not be misattributed to an object, and vice versa.

#### Shape / mesh editing

1. Select a supported geometry in the viewport or Outliner.
2. In the right **Shape** panel choose **Smooth & Edit** to enter editable subdivision geometry.
3. Work with **Extrude**, **Inset**, **Edge Loops**, **Loop Cuts**, **Slide**, vertex/edge/face modifications and **Fill Holes**.
4. Under modeling settings: **Extrude & Inset Mode** (individual/group), **Extrude Direction**, **Selection Side** (front/both), **Selection Mode** (and paint radius), and **Hole Filling** (**Flat, Curved, Ngon**).
5. For boolean geometry, use the dedicated Boolean tools. Their computation can be costly; avoid high-sided input meshes and consider an applied result after preserving an editable source.

[3D Modeling Tools](https://docs.spline.design/designing-in-3-d/modeling/3d-modeling-tools) · [Boolean Operations](https://docs.spline.design/designing-in-3-d/modeling/boolean-operations) · [3D Sculpting](https://docs.spline.design/designing-in-3-d/modeling/3d-sculpting).

#### Pen — draw vectors in 3D

1. Select **Pen** on the toolbar; click to place vector points in the 3D scene; press/drag to form Bézier curves.
2. Double-press an existing vector shape to edit it; **Esc** exits. Hold **Alt/Option** while dragging curve handles to break a continuous curve. The docs also describe a Bend tool with Ctrl/Cmd modifier.
3. In **Shape**, add **Extrusion** for depth; optionally add **Rounded Corners** and extrusion **Bevels**.
4. Style through Material and Lighting. Unlike a Path object, a Pen shape is fundamentally vector geometry that may be extruded.

[Pen Tool](https://docs.spline.design/designing-in-3-d/objects/pen-tool).

#### Path — tubes, wires, rails and motion tracks

1. Click **+** in the toolbar → **Path**; click points in 3D space; a red plane during placement indicates surface snapping.
2. With the path selected, the **Path** panel exposes **Size, Corner, Subdivision, Edit Path**. Select a point to edit its **Position/Corner**.
3. Choose a path **Shape** profile: **Rectangle, Circle, Polygon, Star, Custom**. Set **Depth, Offset, Angle, Twist, Start Scale, End Scale, Caps**.
4. To make an object follow: select it → **Modifiers** → **+** → **Align to Path** → choose source path; animate **Slide**. Controls include **Object, Orientation, Offset, Slide**.
5. **Important:** A directly aligned object's rotation is controlled by its path and can snap back. To add independent local rotation/animation, align a **parent group**, then animate the child inside the group.
6. For hidden motion guide paths, turn off materials and shadow casting/receiving. To convert a Vector Shape to a Path, select that vector and use **Convert to Path**.

[3D Paths](https://docs.spline.design/designing-in-3-d/objects/3d-paths).

### 2.6 Timeline and motion

The **Timeline toggle** in the editor toolbar opens the bottom Timeline panel. Select an object → **Animate** → add a property track (or a preset) → move the playhead and change the property to produce keyframes. Use **Graph Editor** to tune interpolation curves. Create multiple timelines via the timeline selector **+**. To run a timeline in Preview/export, use an event (for example **Start**) linked to the **Timeline Animation** action. Available property families include Transform, Size, Material, Material Opacity, Cloner, Align to Path and Path Extrusion. Export a chosen timeline as a video through Export's timeline settings. [Timeline Animation](https://docs.spline.design/designing-in-3-d/animation/timeline-animation).

---

## 3. Hana 2D Editor — detailed UI map

### 3.1 Start a Hana file

1. Go to Spline **Home** or **My Files**.
2. Click **+ Create** → **Hana – 2D Design**.
3. Select the **Layers** view in the left sidebar; manage **Pages** above its layer tree. Open **Agent** as needed. Draw frames or shapes using the left vertical toolbar.

[Designing in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana).

### 3.2 Editor anatomy

```text
┌────────────────────────────────────── HANA ──────────────────────────────────┐
│ Left sidebar      Left toolbar       Canvas                 Right inspector │
│ Agent | Layers    Select             Frames, sections       Transform       │
│ Pages             Frame / Section    Vector art             Shape           │
│ Layer tree        Shapes             UI, image/video        Layout          │
│                  3D Shapes           Live interactions       States / Events │
│                  Text                                        Fill / Stroke   │
│                  Vector / Pencil                             Effects        │
│                  Comments, Play                               Export         │
│                  Zoom / Share / Export above inspector                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

The Hana document is *not* a Spline 3D scene with a flat camera. Pages, frames and sections have different responsibilities:

| Container | Function | Constraints / caveats |
|---|---|---|
| **Page** | One of multiple distinct canvases in a Hana file | Pages show separate canvas contents; add, rename, duplicate, delete, reorder from Pages list |
| **Frame** | Screen/artboard with nested objects and optional auto layout | Parent frame is a unit of Play and publishing; nested child frames cannot independently export as embed |
| **Section** | Labeled grouping box enclosing frames/objects | Create from **Frame dropdown > Section**, or press **S** in **Hana**; moving moves children, never clips; cannot Play as screen, cannot be component or auto-layout container. Can export. |
| **Layer** | An object in the active page tree | Nest, reorder, select; can be masked and animated |

[Pages](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/pages-in-hana) · [Sections](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/sections-in-hana).

### 3.3 Left toolbar: every described class of tool

- **Selection:** select/manipulate existing elements on canvas.
- **Frame / Section:** draw artboards or labeled groupings. **Section** is a dropdown entry under Frame.
- **Shapes:** **Rectangle, Ellipse, Star, Polygon**.
- **3D Shapes / 3D Shape effect:** introduce dimensional appearance and controllable depth/bevel/material effects to a 2D-first design. The toolbar and inspector's effect/settings should not be conflated.
- **Text:** author typography; style through the right **Text** inspector and Fill/Stroke.
- **Vector Tool:** draw precise points and vector networks; unlike conventional simple paths, network junctions may connect multiple edges.
- **Pencil Tool:** freehand drawing; resulting points remain vector-editable.
- **Comments:** add feedback while collaborating.
- **Play:** preview interactive behavior; appears toward toolbar bottom.

Source: [Understanding Spline's UI](https://docs.spline.design/basics/understanding-splines-ui), [Designing in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana), [3D Shapes in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana).

### 3.4 Right-hand inspector: transforms and responsive layout

- **Transform / Shape:** position, width, height, rotation, corner radius, and shape attributes. **3D Transform** can rotate/position apparent 2D elements in 3D space. **Flatten 3D** treats nested children as one plane; **Backface** controls whether rotated reverse sides show.
- **Layout:** select a **Frame** → **Layout** to enable Auto Layout. Set **Direction** (**Horizontal, Vertical, Horizontal Wrap**, including Masonry option), **Align**, **Gap** (including negative), and **Padding**. Set children to **Fixed, Fill, Hug** sizing. For a free-positioned overlay element, choose absolute positioning in Transform.
- **Constraints:** left, right, left-and-right, center or scale per horizontal axis; top, bottom, top-and-bottom, center or scale vertically. Responsive reflow differs from uniformly scaling an artboard.
- **Fill:** colors, gradients, images, video or a referenced **Frame**. A Frame Fill displays live content of a separate frame; combine with a 3D Shape effect to show a functioning UI on a mesh.
- **Stroke:** outline thickness, color, opacity, style/corners, gradient and image stroke variants where supported.
- **Boolean modifiers:** **Union, Subtract, Intersect** combine vector shapes. **Align to Path** modifier uses a vector curve as the follower path.
- **Vector Masking:** choose a vector shape and target content → right-click → **Use as Mask**. Alternatively mark the mask in the layer outliner; layer order determines masked targets. Masks can be state-animated.

**Non-animatable layout properties:** Hana's States do not interpolate **padding, gap or layout direction**. Animate geometric width/height/scale instead. Vector morphing across states requires the **same number of points**. [Auto Layout and Constraints](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints), [Interactivity in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana).

### 3.5 Hana effects reference

Select shape/text/frame → right-side **Effects** panel. Effects can stack, but do not assume combinations are free on mobile GPUs.

| Effect | What it changes | Key settings |
|---|---|---|
| **Drop Shadow** | Outside depth/shadow | X/Y offset, blur, spread, color, opacity |
| **Inner Shadow** | Inside/pressed depth | X/Y offset, blur, spread, color, opacity |
| **Layer Blur** | Blurs object and own contents | Blur amount; supports progressive blur |
| **Background Blur** | Blurs what is behind an object | Blur amount; lower fill opacity for glassy results |
| **Progressive Blur** | Directional gradient of blur | Control line, blur start/end, direction |
| **Liquid Glass** | Refractive/distorting translucent optics | Offset X/Y, Distortion, Depth, Blur, Aberration (Edge/Fill), Profile, Magnification |
| **Noise Glass** | Noise-distorted refractive background | Simplex/Fbm/Voronoi/Sine; Uniform/Progressive, amplitude, falloff, scale, stretch, offset, movement, seed |
| **Layer Noise** | Procedural noisy displacement/textures | Noise algorithm, blur, uniform/progressive falloff, amplitude/scale/stretch, movement |
| **3D Shape** | Adds volumetric/dimensional form to 2D/vector shapes | Depth, Bevel Size, Smoothness, rotation, material/lighting, Tonemapping where applicable |

[Effects in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/effects-in-hana), [3D Shapes in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana).

### 3.6 Hana interaction system

1. Select an object → **States**. **Base State** is always present. Create a new state (e.g. `Hover`, `Open`, `Active`); edit position, size, fill or effects while that state is active.
2. On the same object → **Events** → add trigger (Start, Mouse Down/Up/Press/Hover, Key Down/Up/Press, Look At, Follow).
3. In the event, add one or more **Actions**: Transition, Show, Link, Video, or Animation (imported 3D clips). Point Transition to the state(s) you authored.
4. Set **Duration**, **Delay**, easing (including springs with mass/stiffness/damping/velocity, or custom Bézier), Repeat/Direction; select run mode **Once / Repeat / Toggle**. Several states may run sequentially.
5. Test in **Play**, including mouse, keyboard and touch behavior. Passthrough in the Events header determines whether overlapping objects all receive pointer events or only the topmost does.
6. **Look At** and **Follow** are continuous behaviors with damping, movement axis, distance limits and reset-on-leave settings — useful for parallax, magnetic buttons and cursor-tracking eyes.

**Hana actions are not equal to every 3D action.** The documented Hana set is smaller: Transition, Show, Link, Video, Animation. [Interactivity in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana).

### 3.7 Hana Agent and asset operations

The left **Agent** can create multiple frames in one request, change selected objects, generate imagery, and wire interaction States/Events with normal editable results. Its prompt panel supports attachment (including images/video and glTF), model and effort choice, history and new chats. Unlike the 3D Agent's queued prompts, Hana can start a **parallel chat** when prompted while working. Image context-menu actions include **Remove Background** and **Upscale Image**. File imports include SVG (editable vector geometry), PNG/JPEG imagery, and MP4 video. [AI Agent in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/ai-in-hana), [Importing Assets](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/importing-assets-to-hana).

### 3.8 Hana Export and responsive embed

1. Select an **outer/parent Frame** (not a nested child). Use frame border **⋯ > Export Embed**, or upper-right **Export**, or right inspector's **Export > +**.
2. Choose **Public URL**, **Iframe Embed**, or native **Hana Embed** (`<hana-viewer>`).
3. Set **Frame Size**: **Contain** (letterbox as necessary), **Cover** (may crop), **Actual** (natural pixels), or **Responsive** (children/constraints reflow; may clip at extremes). Toggle page scroll and branding where permitted.
4. For transparent background, create a frame fill then **hide it or set opacity to 0%**. Without any fill, published background can default to black.
5. To update a published scene/setting change, press **Export** again to refresh its URL.
6. Images support scale ratio and background/logo options. Videos support Duration, FPS **15/24/30/48/60**, resolution scales **1×–4× / 480p–4K**. For interactive motion to appear in exported video, have at least one **Start event** trigger a **Transition** action on an object.

[Exporting in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/exporting-in-hana).

---

## 4. Key tools and click paths

This machine-readable table is also supplied in the companion **`Spline_UI_Elements_2026-10-22.json`**. Records represent source-described controls and access paths. A missing shortcut means **not documented**, not necessarily that no shortcut exists. **Context matters:** `S` in the 3D editor focuses an object, but `S` in Hana creates a Section; do not transfer shortcuts across editors without checking.

| Mode | Location / UI element | Exact access path or gesture | Function / options | Shortcut |
|---|---|---|---|---|
| Dashboard | **Desktop tab bar → Home** | Click home icon at far left of tab bar | Return to dashboard/files — options: New tab (+), open file tabs | — |
| Dashboard | **Left sidebar → Home** | Dashboard > Home | Workspace home | — |
| Dashboard | **Left sidebar → My files** | Dashboard > My files | Files owned by the workspace | — |
| Dashboard | **Left sidebar → Templates** | Dashboard > Templates | Starter scenes and files | — |
| Dashboard | **Left sidebar → Community** | Dashboard > Community | Browse community work | — |
| Dashboard | **Left sidebar → Academy** | Dashboard > Academy | Tutorials and learning | — |
| Dashboard | **Workspace header → Workspace selector** | Click workspace name | Switch workspaces | — |
| Dashboard | **File view → Shared with me** | Dashboard > file view > Shared with me | Find shared files | — |
| Dashboard | **File view → + Create** | Dashboard > + Create | Create a new Spline 3D or Hana file — options: Hana – 2D Design, 3D scene | — |
| Dashboard | **Project list → Projects +** | Dashboard > Projects > + | Create shared project/folder | — |
| 3D Edit | **Left sidebar tab → Agent** | 3D editor > left sidebar > Agent | AI assistant, edits scene through native actions | — |
| 3D Edit | **Left sidebar tab → Objects** | 3D editor > left sidebar > Objects | Scenes list, object outliner, nesting, search | — |
| 3D Edit | **Left sidebar tab → Assets** | 3D editor > left sidebar > Assets | Asset browser and team libraries | — |
| 3D Edit | **Objects sidebar → Scenes** | Objects tab > Scenes list | Switch scenes within the file | — |
| 3D Edit | **Objects sidebar → Outliner** | Objects tab > scene tree | Select, nest, search, group objects | — |
| 3D Preview | **Top stage tabs → Preview** | Top of 3D editor > Preview | Run the scene as a visitor sees it, HTML overlay and interactions | — |
| 3D Edit | **Top stage tabs → Edit** | Top of 3D editor > Edit | Editable 3D viewport with no play interactions | — |
| 3D Code | **Top stage tabs → Code** | Top of 3D editor > Code | Edit the per-file HTML/CSS/JS document | — |
| 3D Preview | **Near stage tabs → Restart** | Preview > restart chip | Restart running scene | — |
| 3D Preview | **Near stage tabs → Full-screen** | Preview > full-screen chip | Play full screen | — |
| 3D Edit | **Tool dock → + Add** | 3D Edit > tool dock > + | Open complete list of addable objects — options: Primitives, lights, camera, text, path | — |
| 3D Edit | **Tool dock → Transform** | 3D Edit > tool dock > arrow | Move, rotate, scale selected objects | — |
| 3D Edit | **Tool dock → Rectangle** | Press R or use add tools | Create 2D rectangle in 3D world | R |
| 3D Edit | **Tool dock → Ellipse** | Press O or use add tools | Create ellipse | O |
| 3D Edit | **Tool dock → Triangle** | Press K or use add tools | Create triangle | K |
| 3D Edit | **Tool dock → Polygon** | Press J or use add tools | Create polygon | J |
| 3D Edit | **Tool dock → Pen** | Select Pen on toolbar | Draw vector points and Bezier curves — options: Straight point, curve, extrusion, rounded corners, bevel | — |
| 3D Edit | **Tool dock → Path** | Click + > Path | Draw editable 3D path — options: Edit Path, Size, Corner, Subdivision, path profile | — |
| 3D Edit | **Viewport → Orbit** | Alt + drag or Alt + trackpad tap-drag | Orbit working camera | Alt + drag (Win) |
| 3D Edit | **Viewport → Pan** | Space + drag | Pan viewport | Space + drag |
| 3D Edit | **Viewport → Zoom** | Ctrl + wheel / trackpad pinch | Zoom viewport | Ctrl + wheel (Win) |
| 3D Edit | **Right panel → Scene Properties** | Click empty viewport | Change scene-wide appearance and rendering — options: Background, lights, simulation, effects, fog, sky, ambient shadows, color | — |
| 3D Edit | **Right panel → Object Properties** | Select object in viewport/outliner | Inspect and modify selected object — options: Transform, Shape, Material, modifiers, shadows, states, events | — |
| 3D Edit | **Right panel > Shape → Smooth & Edit** | Select object > Shape > Smooth & Edit | Convert primitive geometry to editable subdivision mesh — options: Extrude, Inset, Edge Loop, Loop Cut, Slide, Fill Hole | — |
| 3D Edit | **Modeling settings → Extrude & Inset Mode** | Edit mesh > modeling settings > Extrude & Inset Mode | Grouped vs individual face operation | — |
| 3D Edit | **Modeling settings → Extrude Direction** | Edit mesh > modeling settings > Extrude Direction | Controls extrusion direction | — |
| 3D Edit | **Modeling settings → Selection Side** | Edit mesh > modeling settings > Selection Side | Front vs both sides | — |
| 3D Edit | **Modeling settings → Selection Mode** | Edit mesh > modeling settings > Selection Mode | Mesh selection and paint radius | — |
| 3D Edit | **Modeling settings → Hole Filling** | Edit mesh > modeling settings > Hole Filling | Flat, Curved or Ngon | — |
| 3D Edit | **Right panel > Modifiers → Cloner** | Select object > Modifiers > + > Cloner | Procedurally repeat an object — options: Radial, Linear, Grid, Object, Randomness | — |
| 3D Edit | **Right panel > Modifiers → Align to Path** | Select follower > Modifiers > + > Align to Path | Align and animate object along a 3D path — options: Object, Orientation, Offset, Slide | — |
| 3D Edit | **Timeline panel → Timeline toggle** | 3D Edit > toolbar > timeline toggle | Open timeline at bottom — options: Animate, clip tracks, keyframes, Graph Editor | — |
| 3D Edit | **Timeline panel → Animate** | Select object > timeline > Animate | Choose property track for keyframe animation — options: Position, Rotation, Scale, Size, Material, opacity, Cloner, paths | — |
| 3D Edit | **Timeline panel → Graph Editor** | Open timeline > Graph Editor | Edit timing/easing curves | — |
| 3D Edit | **Viewport upper controls → Performance** | Editor > performance/Export panel | Inspect size and optimization opportunities — options: Polygons, materials, clones, lights, compression | — |
| 3D Edit | **Viewport upper controls → Share** | Top-right > Share | Invite collaborators and share scene | — |
| 3D Edit | **Viewport upper controls → Export** | Top-right > Export | Choose output types and Play Settings — options: Public URL, Viewer, Code, images, video, 3D files | — |
| 3D Code | **Code editor → Console** | Code tab > Console strip | Inspect console logs and JS errors | — |
| 3D Code | **Code editor → Injected spline API** | Code > script > global spline object | Read/update objects, variables, events, runtime entities — options: Runtime clone, geometry, custom materials | — |
| 3D Edit | **Agent sidebar → Agent prompt** | Agent tab > prompt box | Edit objects and scenes with AI — options: /3d, /image, attachments, model, effort, chat history, queue | — |
| 3D Edit | **Agent sidebar → Slash commands** | Agent prompt > type / | Generate image or 3D model with explicit command — options: /image, /3d | — |
| 3D Edit | **Agent sidebar → Queue** | Submit prompt while agent running | Queue prompts without stopping active job — options: Pause, Clear, remove queued prompt, Stop | — |
| Hana | **Dashboard → Hana – 2D Design** | Home or My Files > + Create > Hana – 2D Design | Create a Hana file | — |
| Hana | **Left sidebar tabs → Agent** | Hana > left sidebar > Agent | AI-generated frames, styles, effects, interactivity — options: Model, effort, attach image/video/glTF, chat history | — |
| Hana | **Left sidebar tabs → Layers** | Hana > left sidebar > Layers | Browse and nest current page layer tree | — |
| Hana | **Left sidebar > Pages → Pages** | Hana > left > Pages | Manage per-file canvases — options: + New, Rename, Duplicate, Delete, Reorder | — |
| Hana | **Left toolbar → Selection** | Hana canvas > left toolbar > selection | Select objects | — |
| Hana | **Left toolbar → Frame** | Left toolbar > Frame | Create exportable screen/artboard — options: Frame, Section | — |
| Hana | **Left toolbar → Section** | Left toolbar > Frame dropdown > Section | Group multiple frames and content without clipping | S (Hana) |
| Hana | **Left toolbar → Shape: Rectangle** | Left toolbar > Shapes > Rectangle | Draw a rectangle for UI/graphics | — |
| Hana | **Left toolbar → Shape: Ellipse** | Left toolbar > Shapes > Ellipse | Draw a ellipse for UI/graphics | — |
| Hana | **Left toolbar → Shape: Star** | Left toolbar > Shapes > Star | Draw a star for UI/graphics | — |
| Hana | **Left toolbar → Shape: Polygon** | Left toolbar > Shapes > Polygon | Draw a polygon for UI/graphics | — |
| Hana | **Left toolbar → 3D Shapes** | Left toolbar > 3D shapes | Place 3D-shaped elements on 2D canvas | — |
| Hana | **Left toolbar → Text** | Left toolbar > Text | Draw editable text; type and format via Text panel | — |
| Hana | **Left toolbar → Vector Tool** | Left toolbar > vector tools | Draw vector points and connected vector networks | — |
| Hana | **Left toolbar → Pencil Tool** | Left toolbar > pencil/vector tools | Freehand sketch then edit vector points | — |
| Hana | **Left toolbar → Comments** | Left toolbar > Comments | Place design feedback | — |
| Hana | **Left toolbar bottom → Play** | Hana > left toolbar > Play | Run interactive frame | — |
| Hana | **Right properties panel → Transform** | Hana > select relevant object > right inspector > Transform | Position, rotation, size and optional 3D transform — options: Position, Rotation, Width, Height, 3D Transform, Flatten 3D, Backface | — |
| Hana | **Right properties panel → Shape** | Hana > select relevant object > right inspector > Shape | Geometry and corner attributes — options: Corner radius, geometry controls | — |
| Hana | **Right properties panel → Layout** | Hana > select relevant object > right inspector > Layout | Responsive auto layout on frames — options: Direction, Wrap, Align, Gap, Padding, Fixed, Fill, Hug | — |
| Hana | **Right properties panel → Constraints** | Hana > select relevant object > right inspector > Constraints | Pin/scale elements as parent frame resizes — options: Left, Right, Center, Scale, Top, Bottom | — |
| Hana | **Right properties panel → States** | Hana > select relevant object > right inspector > States | Create alternate versions of a selected object — options: Base State, Hover, Open, Active | — |
| Hana | **Right properties panel → Events** | Hana > select relevant object > right inspector > Events | Triggers and actions for transitions — options: Start, Mouse, Key, Look At, Follow, Transition | — |
| Hana | **Right properties panel → Fill** | Hana > select relevant object > right inspector > Fill | Surface treatments — options: Color, Gradient, Image, Video, Frame | — |
| Hana | **Right properties panel → Stroke** | Hana > select relevant object > right inspector > Stroke | Borders and outlines — options: Thickness, Color, Corner styles, Gradient | — |
| Hana | **Right properties panel → Effects** | Hana > select relevant object > right inspector > Effects | Visual effects including glass, blur, shadows and noise — options: Drop Shadow, Inner Shadow, Background Blur, Layer Blur, Liquid Glass, Noise Glass | — |
| Hana | **Right properties panel → Export** | Hana > select relevant object > right inspector > Export | Publish parent frame or export image/video — options: Public URL, iframe, hana-viewer, Video | — |
| Hana | **Object context menu → Use as Mask** | Select mask and targets > right-click > Use as Mask | Group objects with vector mask — options: Also mask button in layers tree | — |
| Hana | **Right panel > Modifiers → Align to Path** | Select follower > Modifiers > Align to Path | Make elements follow vector paths | — |
| Hana | **Right panel > Fill → Frame as Fill** | Select shape > Fill > Frame > source frame | Display a live frame as texture/content of another shape — options: Can combine with 3D Shape effect | — |
| Hana | **Right panel > Effects → Liquid Glass** | Select shape/text/frame > Effects > Liquid Glass | Refractive glass with controllable distortion and perceived depth — options: Offset X/Y, Distortion, Depth, Blur, Aberration, Profile, Magnification | — |
| Hana | **Right panel > Effects → Noise Glass** | Select object > Effects > Noise Glass | Noise-based refractive distortion — options: Simplex, Fbm, Voronoi, Sine, Progressive, Amplitude, Movement | — |
| Hana | **Right panel > Export → Export Embed** | Select parent frame > frame three-dot > Export Embed | Generate public link or embed — options: Iframe Embed, Hana Embed | — |
| Hana | **Object context menu → Remove Background** | Right-click an image > Remove Background | AI removes image background | — |
| Hana | **Object context menu → Upscale Image** | Right-click an image > Upscale Image | AI increases image resolution | — |

[Structured UI records with per-item source URLs: companion JSON file](Spline_UI_Elements_2026-10-22.json).

---

## 5. Features, animation, interactivity and exports

### 5.1 3D modeling and procedural construction

| Feature | Access / high-level process | Relevant official doc |
|---|---|---|
| Parametric shapes | Add object > adjust Shape parameters (sides, geometry, depth and related fields vary) | [Parametric Objects](https://docs.spline.design/designing-in-3-d/objects/working-with-parametric-objects) |
| Editable subdivisions | Select object > Shape > Smooth & Edit | [3D Modeling](https://docs.spline.design/designing-in-3-d/modeling/3d-modeling-tools) |
| 2D→3D extrusion | Select 2D shape > Shape > Extrusion | [Extrude 2D Objects](https://docs.spline.design/designing-in-3-d/objects/extruding-2d-objects-in-3-d) |
| Pen / Vector | Pen toolbar > vector points and curves | [Pen Tool](https://docs.spline.design/designing-in-3-d/objects/pen-tool) |
| 3D Path | + > Path; modifier Align to Path for follower | [3D Paths](https://docs.spline.design/designing-in-3-d/objects/3d-paths) |
| Booleans | Combine/subtract geometry, preserve editable source before applying | [Booleans](https://docs.spline.design/designing-in-3-d/modeling/boolean-operations) |
| Sculpting | Sculpt tools with brush controls and symmetry | [Sculpting](https://docs.spline.design/designing-in-3-d/modeling/3d-sculpting) |
| Shape Blend | Use shape blend primitives/mesh sources to create smooth connected forms | [Shape Blend](https://docs.spline.design/designing-in-3-d/modeling/shape-blend) |
| Cloner | Selected object > Modifiers > + > Cloner, choose Radial/Linear/Grid/Object | [Cloner Motion](https://docs.spline.design/designing-in-3-d/animation/cloner-motion) |
| Components | Right-click object > Create Component; instances reuse main geometry with per-instance overrides | [Components](https://docs.spline.design/designing-in-3-d/scenes/components) |
| Gaussian splats | Use documented scene/import workflows; check format and platform limits | [3D Gaussian Splatting](https://docs.spline.design/designing-in-3-d/scenes/3d-gaussian-splatting) |
| Hair systems | Grow strands from meshes, with strand dynamics, wind, lighting | [Hair Systems](https://docs.spline.design/designing-in-3-d/animation/hair-systems) |
| Physics | Add applicable simulation/collision properties to moving scene objects | [Physics](https://docs.spline.design/designing-in-3-d/animation/physics) |
| Particles | Configure emitter and particle parameters; control with events | [Particles](https://docs.spline.design/designing-in-3-d/animation/particles) |

### 5.2 Cloner options

- **Radial:** Base (show original), Count, Radius, Start/End angle, Alignment, Axis (X/Y/Z), Transform offsets.
- **Linear:** Base, Count, Transform offsets.
- **Grid:** Base, Count per axis, Size/spacing, Use center, Transform offsets.
- **Object:** Reference object, Count/distribution/Spread, vertex/edge/polygon/random-related options, Seed where applicable.
- Cloner/Randomness parameters can be animated through state changes, but repeated high-poly objects still require performance review. [Cloner Motion](https://docs.spline.design/designing-in-3-d/animation/cloner-motion).

### 5.3 Materials, shading, lights and camera

**Material layer families:** the official documentation includes **Color, Vertex Color, Gradient, Image, Video, Pattern, Noise, Rainbow, Lighting, Toon, Matcap, Fresnel, Glass, Reflection, Depth Layer/3D Gradient, Normal, Bump/Roughness, Displace, Cavity, Dust, Outline**. It also documents **Material Library, PBR Materials, Material Layers, Layer Masking**. See the complete linked directory in §8.

**Advanced V2:** PBR/metalness/roughness and HDR workflows; reflection layer with screen-space reflection under WebGPU and a planar Mirror option; Physical Sky and HDRi Sky, procedural/height fog, Dust and Vertex Color. Materials are layered: order and opacity influence final appearance. A glass surface without useful environmental light will look different from one with HDRi and polished reflections.

**Lighting:** directional/point/spot lights, environment and HDRi, softness/penumbra, ambient shadows. **Cameras:** add scene camera, camera parameters, Depth of Field, post-processing, fog and Play camera selection. Viewport orbit is not the same as animating an authored camera.

Performance rule: use effects for material difference, not by default everywhere. Reflections, many lights, high polygon counts and layered effects have real export/runtime cost. [PBR](https://docs.spline.design/materials-shading/basics/pbr-materials), [Environment](https://docs.spline.design/lighting/environment-and-hdri), [V2](https://blog.spline.design/spline-v2).

### 5.4 Animation systems — decision table

| Goal | Native method | Trigger / caveat |
|---|---|---|
| Hover-scale button | New **State** plus **Mouse Hover → Transition** | Best for finite property transitions |
| Animated product spin on load | **Start Event** + Transition or Timeline Animation | For long choreography choose Timeline |
| Precisely timed motion choreography | **Timeline + keyframes + Graph Editor** | In Preview, trigger timeline with event/action |
| Object follows path | **Align to Path** modifier, animate Slide | Group follower if independent rotation needed |
| Procedural repetition | **Cloner** + randomness / state transitions | Efficient compared with arbitrary copies, but budget total clones |
| Motion responding to physics | **Physics**, collisions and event linkage | Validate collisions and device performance |
| Particle burst | **Particles** + particles control action | Validate event run and export path |
| HUD/game logic | **Code Tab** with injected `spline` | Runtime object edits transient; state/edit events have Play dependency |

### 5.5 3D events — canonical source-page index

Each item below has its own official page under **Interaction, States, Events, and Actions → Events**. Names correspond to available documentation, not a promise every event appears on every object type.

- **[Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event)** — Triggers as the scene begins
- **[Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event)** — Pointer release
- **[Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event)** — Pointer down
- **[Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event)** — Press/release interaction
- **[Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event)** — Hover enter/leave
- **[Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event)** — Keyboard key release
- **[Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event)** — Keyboard key down
- **[Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event)** — Key press
- **[Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event)** — Scrolling input
- **[Look At Event](https://docs.spline.design/interaction-states-events-and-actions/events/look-at-event)** — Orient an object toward target/pointer
- **[Follow Event](https://docs.spline.design/interaction-states-events-and-actions/events/follow-event)** — Make an object follow a pointer/target
- **[Game Controls Event](https://docs.spline.design/interaction-states-events-and-actions/events/game-controls-event)** — Keyboard/joystick style movement controls
- **[Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event)** — Proximity check
- **[State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event)** — A state changes
- **[Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event)** — A variable changes
- **[Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event)** — Collision condition met
- **[Drag And Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event)** — Drag and drop gesture
- **[Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event)** — Enter or exit trigger area
- **[Screen Resize Event](https://docs.spline.design/interaction-states-events-and-actions/events/screen-resize-event)** — Viewport resize
- **[Api Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event)** — API-fed data changes
- **[Webhook Called Event](https://docs.spline.design/interaction-states-events-and-actions/events/webhook-called-event)** — Webhook invoked
- **[Ai Assistant Listener Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-listener-event)** — AI assistant listening-related trigger
- **[Ai Assistant Trigger Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-trigger-event)** — AI assistant trigger

### 5.6 3D actions — canonical source-page index

- **[Animation Action](https://docs.spline.design/interaction-states-events-and-actions/actions/animation-action)** — Trigger an imported object animation
- **[Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action)** — Animate between object states
- **[Sound Action](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action)** — Play/control sound
- **[Video Action](https://docs.spline.design/interaction-states-events-and-actions/actions/video-action)** — Control video
- **[Open Link Action](https://docs.spline.design/interaction-states-events-and-actions/actions/open-link-action)** — Open a link
- **[Reset Scene Action](https://docs.spline.design/interaction-states-events-and-actions/actions/reset-scene-action)** — Reset current scene
- **[Switch Camera Action](https://docs.spline.design/interaction-states-events-and-actions/actions/switch-camera-action)** — Switch active camera
- **[Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action)** — Create/instantiate object
- **[Destroy Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/destroy-object-action)** — Remove an object at runtime
- **[Scene Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/scene-transition-action)** — Move between scenes
- **[Particles Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/particles-control-action)** — Control emitter/particles
- **[Variable Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/variable-control-action)** — Operate on variables
- **[Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action)** — Branch based on a condition
- **[Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action)** — Set value of variable
- **[Clear Local Storage Action](https://docs.spline.design/interaction-states-events-and-actions/actions/clear-local-storage-action)** — Clear saved client-local data
- **[Api Request Action](https://docs.spline.design/interaction-states-events-and-actions/actions/api-request-action)** — Request remote API data

### 5.7 States, variables, API and logic

- **State-based animation:** define alternate object property states, then wire Event → Action (often Transition), with easing and trigger modes.
- **Variables** act as shared values driving parameters and logic, including change events and actions. **Conditional Action**, **Variable Control**, **Set Variable**, **API Request**, **Webhook** and related features add data-driven workflows.
- **Real-time APIs** and **Webhooks** enable external data flow. Treat API credentials and personal secrets as sensitive; don't put privileged service keys into public scene JS or exported HTML.
- **Input** systems support user-controlled interactions; **Game Controls** may be used for more navigable experiences.
- **AI Text/Voice** documentation covers external service integrations, subject to current availability and credentials.
- **Code Tab** can read scene objects, variables and runtime geometry, create/clone objects and listen for interactions. Runtime changes are not persistent scene edits; do not mistake live state for saved authoring changes.

Primary references: [States](https://docs.spline.design/interaction-states-events-and-actions/concepts/how-state-based-animation-works), [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables), [Real-time API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api), [Webhooks](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/webhooks), [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab).

### 5.8 Play Settings, export formats and code caveats

**3D export entry:** top-right **Export**. In web runtime exports, open **Play Settings**. Available categories documented by Spline include:

| Output | Example options | Considerations |
|---|---|---|
| Web URL | Public URL, viewer, runtime code, self-hosted project | HTML from Code Tab goes with supported Spline-runtime exports |
| Code API for Web | Web app controls published scene via Spline API | Distinct from **in-file Code Tab** |
| Web integrations | Framer, Figma, Webflow, Shopify, Wix, Notion and more | Host embed behavior and resize strategy matter |
| Raster/video | Image, video, image sequence | Export dimensions, duration, FPS, camera and scene chosen |
| 3D files | glTF/GLB, USDZ, STL | Do not assume all runtime events/materials/HTML survive static 3D export |
| Native/mobile | iOS/SwiftUI, visionOS, Android/Kotlin/APK/AAB where documented | Use platform-specific integration/export docs; verify current plan |

**Play Settings — scene/view**: Main Scene, Camera, BG Color/visibility, Page Scroll, Cursor; Orbit/Pan/Zoom enablement; Soft Orbit; touch orbit/pan gesture count and pinch zoom; hover camera behavior (sensitivity/damping/reset); Orbit/Pan limits, Zoom limits and Animated Turntable speed/direction; hit behavior **Stop At Object** vs **Passthrough object**.

**Play Settings — performance**: Geometry Quality **Performance / Default / Quality**, Image Quality, Preload, Renderer **Auto / WebGPU / WebGL**. **Auto** uses WebGPU where available with WebGL fallback; WebGPU-only lacks fallback and may block visitors. New scenes are WebGPU-first; exported scenes from earlier settings may retain Auto behavior. Branding visibility is subject to the account plan.

**Optimization diagnostics**: Performance Panel, accessible through export-related controls, reports estimated export size/load score and counts of objects, clones, booleans, polygons, materials, audio, lights, post-processing and textures. Red/yellow/gray optimization opportunities indicate urgency. Lower geometry sides, reuse components/material assets, avoid high subdivision, simplify overlapping occluded geometry and expensive multi-layer materials, and inspect loading on a mobile target.

**Compatibility caveats:** HTML overlay works with public URLs, `<spline-viewer>` runtime and Spline runtime code export. **Three.js/React Three Fiber code export** does not carry that Spline HTML document. Custom three.js materials in the Code Tab do **not** work inside `<spline-viewer>` embeds. [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab), [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings), [Optimize](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene).

### 5.9 AI Agent, Spline MCP and desktop integration

Spline V2's agentic workflow supports direct scene-authoring changes as normal editor operations. **Spline MCP** connects compatible agent clients to Spline's native tools; the desktop application is the preferred integration route described in Spline's V2 notes, and the live compatibility/setup instructions should be verified for each client. Agent changes are undoable and collaborative; when an object target is ambiguous, select it first. For enterprise or complex changes, ask the agent for one bounded edit at a time, use snapshots/duplicate files where appropriate, validate interactive outcomes in Preview, and run Performance before export.

Official: [Spline MCP Server](https://docs.spline.design/generate/spline-mcp-server), [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill), [ChatGPT and Codex](https://docs.spline.design/generate/plugins/chatgpt), [V2 desktop announcement](https://blog.spline.design/spline-v2).

---

## 6. Official video library

### 6.1 Provenance and transcript interpretation

**Indexed:** 108 unique official Spline Academy lesson cards, with title, topic category, lesson URL, official YouTube ID, Academy rounded duration (minutes), and Academy level. Academy durations are **rounded**, not exact video runtime; the linked YouTube page may show a more precise duration. Additional V2 introduction, V2 editor tour, MCP and Hana introduction videos appear separately as update references. All video URLs below were obtained from YouTube IDs exposed by the Academy's official thumbnail links or directly from Spline's own docs/official YouTube listings.

**Transcripts:** no complete caption body was retrieved, so no entry claims to contain a transcript. The **Study focus** is an independently written outline using the tutorial title plus relevant official product documentation; it is not a verbatim, timestamped recounting of the video. **Chapters** are only present when directly observed in scraped official YouTube metadata/descriptions.

### 6.2 Start here — current UI video references

| Video | Approximate duration | Source |
|---|---|---|
| [Spline V2 Update Full Tour: New Layout, Faster Creation, Agent Workflow](https://www.youtube.com/watch?v=ZIWjpVarofw) | 9 min | Official Spline video about redesigned UI (2026) |
| [Introducing Spline V2 — AI Agents, WebGPU and MCP](https://www.youtube.com/watch?v=i8g1dnPOrCc) | Not verified | Official V2 release video (Aug 20, 2026) |
| [Spline MCP: Build 3D Web Experiences with AI](https://www.youtube.com/watch?v=tO4BrbNTqKA) | ~6 min | Official MCP tutorial |
| [Introducing Hana — A New Canvas for Interactivity](https://www.youtube.com/watch?v=ZsYijIY7qBA) | Not verified | Official introduction linked by Hana documentation |
| [Get Started with 3D in Spline](https://www.youtube.com/watch?v=Kxz8fzU2OUE) | ~26 min | Academy introduction (older UI; compare V2) |
| [Get Started with Interactive 2D in Hana](https://www.youtube.com/watch?v=DD8z1voLghU) | ~17 min | Academy introduction |

### 6.3 Curated learning track (50 videos)

Recommended order is editorial, designed for learning V2, not a claim of an official Spline playlist. Use the individual video cards below for levels and durations.

1. **[Get Started with 3D in Spline](https://www.youtube.com/watch?v=Kxz8fzU2OUE)** — 3D Fundamentals / Project; ~26 min; Beginner.
2. **[Get Started with Interactive 2D in Hana](https://www.youtube.com/watch?v=DD8z1voLghU)** — Hana / 2D; ~17 min; Beginner.
3. **[Create 3D Icons from Scratch](https://www.youtube.com/watch?v=yfNvUjxcG7M)** — Modeling / Simulation; ~15 min; Beginner.
4. **[Build 3D Icons with Vectors](https://www.youtube.com/watch?v=CQM4hxQX9f4)** — Modeling / Simulation; ~10 min; Beginner.
5. **[Modify 3D Shapes using Boolean Operations](https://www.youtube.com/watch?v=Ib-OD9gfBFI)** — Modeling / Simulation; ~5 min; Beginner.
6. **[How to Create 3D Paths in Spline](https://www.youtube.com/watch?v=5pU7tGajw2E)** — Modeling / Simulation; ~36 min; Beginner.
7. **[How to Sculpt a 3D Gummy Bear with Shape Blend](https://www.youtube.com/watch?v=UKZ5dezNOeg)** — Modeling / Simulation; ~8 min; Beginner.
8. **[Explore 3D Shape Blending in Spline](https://www.youtube.com/watch?v=JIcnI0kUnFM)** — Modeling / Simulation; ~25 min; Beginner.
9. **[How to Create a Spinning 3D Icon](https://www.youtube.com/watch?v=bzbL6eNEfek)** — 3D Fundamentals / Project; ~15 min; Beginner.
10. **[Master Lighting for 3D Scenes](https://www.youtube.com/watch?v=RinPy7h_fhY)** — Materials / Rendering; ~13 min; Beginner.
11. **[Set Up Photo Studio Lighting for 3D Scenes](https://www.youtube.com/watch?v=PoScgWfatPI)** — Materials / Rendering; ~5 min; Beginner.
12. **[Improve Realism by Adding Soft Shadows](https://www.youtube.com/watch?v=z5q_CcaS0I4)** — Materials / Rendering; ~2 min; Beginner.
13. **[Create Vibrant Glossy Materials using Matcaps](https://www.youtube.com/watch?v=DhwA82tJK4M)** — Materials / Rendering; ~7 min; Beginner.
14. **[Create Liquid Glass Materials in 3D](https://www.youtube.com/watch?v=gnhUypBNMc0)** — Materials / Rendering; ~11 min; Beginner.
15. **[Add Depth of Field Lens Blur for Photorealistic 3D Scenes](https://www.youtube.com/watch?v=xoujiGBf5Ow)** — Materials / Rendering; ~6 min; Beginner.
16. **[How to Animate 3D Motion Using Timelines](https://www.youtube.com/watch?v=diBHRtoM2J4)** — Motion / Animation; ~12 min; Advanced.
17. **[Craft Seamless 3D Loop Animations](https://www.youtube.com/watch?v=pUamUyt7EDU)** — Motion / Animation; ~10 min; Beginner.
18. **[Animate Organic 3D Blobs with States](https://www.youtube.com/watch?v=KclCVV4bnow)** — Motion / Animation; ~5 min; Beginner.
19. **[Animate Clones for 3D Motion Graphics](https://www.youtube.com/watch?v=uhIDqxCG5Cc)** — Motion / Animation; ~24 min; Intermediate.
20. **[How to Build Reusable 3D Components](https://www.youtube.com/watch?v=eWuFrHiyyu0)** — 3D Fundamentals / Project; ~6 min; Intermediate.
21. **[Use Variables to Create Interactive 3D Content](https://www.youtube.com/watch?v=Id_SZVCUVMM)** — Interactivity / Logic; ~24 min; Advanced.
22. **[Add Mouse-Based Interactions to 3D Objects](https://www.youtube.com/watch?v=rdZrrXFLxuw)** — Interactivity / Logic; ~13 min; Beginner.
23. **[How to Create 3D Button Interactions](https://www.youtube.com/watch?v=B8o5O7PyKjY)** — Interactivity / Logic; ~10 min; Beginner.
24. **[Trigger Interactions with Proximity Using the Distance Event](https://www.youtube.com/watch?v=9U0l2_eKVMQ)** — Interactivity / Logic; ~5 min; Beginner.
25. **[How to Build Drag & Drop Interactions in 3D](https://www.youtube.com/watch?v=gDXVdJdLJfE)** — Interactivity / Logic; ~10 min; Beginner.
26. **[Add Look At Animations to 3D Objects](https://www.youtube.com/watch?v=L4fD9X_uhtc)** — Motion / Animation; ~10 min; Beginner.
27. **[Build an Interactive Keyboard with Hana](https://www.youtube.com/watch?v=2hLXgB3JV_U)** — Hana / 2D; ~9 min; Beginner.
28. **[Design Smooth Interactive Icons in Hana](https://www.youtube.com/watch?v=pzZjGKa2WRA)** — Hana / 2D; ~6 min; Beginner.
29. **[Design Interactions with Liquid Glass & 3D Transforms in Hana](https://www.youtube.com/watch?v=IZM1H1xBQdk)** — Hana / 2D; ~16 min; Beginner.
30. **[Design Interactive Effects with Progressive Blur and Smoothing Gradients](https://www.youtube.com/watch?v=hr5wqdVX4co)** — Hana / 2D; ~9 min; Beginner.
31. **[Design and Animate with Vector Masks](https://www.youtube.com/watch?v=3DHhZPcPfqs)** — Hana / 2D; ~6 min; Beginner.
32. **[Create Interactive Designs That React to Your Mouse with Hana](https://www.youtube.com/watch?v=TgZdS8RK0bM)** — Hana / 2D; ~6 min; Beginner.
33. **[How to Animate Along a Path with Hana and Spline](https://www.youtube.com/watch?v=u-fEUpXoyCU)** — Hana / 2D; ~6 min; Beginner.
34. **[How to Use AI Image Generation in Hana](https://www.youtube.com/watch?v=hYZ3OF30Awo)** — Hana / 2D; ~7 min; Beginner.
35. **[Apply Image & Video Textures to 3D Objects](https://www.youtube.com/watch?v=MVnWnB0g5YA)** — Materials / Rendering; ~9 min; Beginner.
36. **[Create Dynamic Particle Effects in 3D](https://www.youtube.com/watch?v=lRhLWE_cXkc)** — Modeling / Simulation; ~20 min; Intermediate.
37. **[How to Design Interactive Leaf Particles in 3D](https://www.youtube.com/watch?v=n1QPSxD454k)** — Interactivity / Logic; ~9 min; Intermediate.
38. **[Add Physics Simulation to 3D Scenes](https://www.youtube.com/watch?v=NdBpmhGvvW0)** — Modeling / Simulation; ~9 min; Intermediate.
39. **[Create a Drivable 3D Car with Physics and Game Controls](https://www.youtube.com/watch?v=J5yi_scY2GE)** — Interactivity / Logic; ~4 min; Intermediate.
40. **[Camera orbit with transitions in 3D - SplineLive](https://www.youtube.com/watch?v=mGYZmmZk5ro)** — 3D Fundamentals / Project; ~13 min; Beginner.
41. **[How to Build 3D Multi-scenes and Import Animations](https://www.youtube.com/watch?v=lpYK67LQItI)** — Motion / Animation; ~18 min; Intermediate.
42. **[Turn Your Spline Designs into Interactive Web Experiences](https://www.youtube.com/watch?v=4iyMkuga-C0)** — Export / Integration; ~10 min; Beginner.
43. **[Create a 3D Scroll Animation & Integrate into Framer](https://www.youtube.com/watch?v=j5sEe5NQtUU)** — Export / Integration; ~12 min; Beginner.
44. **[Designing a 3D website with Spline and Framer](https://www.youtube.com/watch?v=8bqkvfRuFYk)** — Export / Integration; ~13 min; Beginner.
45. **[How to Add Interactive Designs Made in Spline into Figma](https://www.youtube.com/watch?v=Woi5g8UHpC8)** — Export / Integration; ~6 min; Beginner.
46. **[Export Interactive Experiences Natively for iOS and visionOS](https://www.youtube.com/watch?v=44OPMq7FdD0)** — Export / Integration; ~15 min; Intermediate.
47. **[How to Export Native 3D for Android](https://www.youtube.com/watch?v=Sot5W1iATGM)** — Export / Integration; ~11 min; Intermediate.
48. **[How to Create 3D Data Visualizations in Spline Using Variables and Real-Time APIs](https://www.youtube.com/watch?v=Kue1OjJ8KOE)** — Interactivity / Logic; ~14 min; Advanced.
49. **[How to Set Up Real-Time APIs and Webhooks for Your 3D Scenes](https://www.youtube.com/watch?v=b9o8-zYx3Qw)** — Interactivity / Logic; ~15 min; Advanced.
50. **[Build an AI Voice Assistant in 3D](https://www.youtube.com/watch?v=TPzHbYRRHzo)** — Interactivity / Logic; ~13 min; Advanced.

### 6.4 Complete official Academy catalog — individual lesson records

Every entry has a verified Academy card, source links, rounded duration/level, a technical study focus, and the actual transcript status. The study focus is **not a transcript**, because individual YouTube captions were not retrieved.

#### 001. Turn Your Spline Designs into Interactive Web Experiences

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=4iyMkuga-C0) · [Academy lesson](https://academy.spline.design/tutorials/turn-your-spline-designs-into-interactive-web-experiences).  
**Study focus (editorial, not observed transcript):** Review the current export routes, including Public URL, viewer, code exports and third-party integration.  
**Verified chapters/timestamps:** 0:33 Sharing via URL · 1:24 Embedding with Spline Viewer · 3:11 Vanilla JavaScript export · 4:27 Advanced JS interactions · 4:52 Three.js · 5:27 React/Next.js · 6:10 React Three Fiber · 6:37 Self-hosted · 7:28 No-code integrations.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 002. Creating Refractive 3D Text in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=B6PBtUxK0qE) · [Academy lesson](https://academy.spline.design/tutorials/creating-refractive-3d-text-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Verified chapters/timestamps:** 0:29 Add text · 0:56 3D shape effect · 2:31 Duplicate text.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 003. Build a Tilt-Controlled 3D Portal Experience in SwiftUI

**Category:** Export / Integration · **Level:** Advanced · **Academy duration:** ~14 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=-LQUQsFJjDk) · [Academy lesson](https://academy.spline.design/tutorials/build-a-tilt-controlled-3d-portal-experience-in-swiftui).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 004. How to Design a Realistic 3D Diamond in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=mN2oNMdsN7g) · [Academy lesson](https://academy.spline.design/tutorials/how-to-design-a-realistic-3d-diamond-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 005. Add Dimension to Hana Designs with the 3D Shape Effect

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~2 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=LUWbtpkP7lU) · [Academy lesson](https://academy.spline.design/tutorials/add-dimension-to-hana-designs-with-the-3d-shape-effect).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 006. Design Smooth Interactive Icons in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=pzZjGKa2WRA) · [Academy lesson](https://academy.spline.design/tutorials/design-smooth-interactive-icons-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor. Build simple primitives/vectors, materials and a small interaction, checking object count.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 007. How to Use AI Image Generation in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=hYZ3OF30Awo) · [Academy lesson](https://academy.spline.design/tutorials/how-to-use-ai-image-generation-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 008. How to Animate 3D Motion Using Timelines

**Category:** Motion / Animation · **Level:** Advanced · **Academy duration:** ~12 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=diBHRtoM2J4) · [Academy lesson](https://academy.spline.design/tutorials/how-to-animate-3d-motion-using-timelines).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Verified chapters/timestamps:** 0:22 Timeline UI and navigation · 2:51 Creating initial animations · 4:29 Keyframe/clip management · 6:01 Advanced property animation · 8:56 Graph Editor · 10:22 Triggering animations · 11:27 Exporting animations.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 009. Design and Animate with Vector Masks

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=3DHhZPcPfqs) · [Academy lesson](https://academy.spline.design/tutorials/design-and-animate-with-vector-masks).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 010. Explore 3D Projections and Noise Effects

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~8 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=dgXJvA2ZErw) · [Academy lesson](https://academy.spline.design/tutorials/explore-3d-projections-and-noise-effects).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 011. How to Build a Reactive 3D Orb with Motion and Interaction

**Category:** Motion / Animation · **Level:** Intermediate · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=ol3f-vwZhBI) · [Academy lesson](https://academy.spline.design/tutorials/how-to-build-a-reactive-3d-orb-with-motion-and-interaction).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 012. How to Use the Code API for SwiftUI

**Category:** Export / Integration · **Level:** Advanced · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=_1T4BkslzsU) · [Academy lesson](https://academy.spline.design/tutorials/how-to-use-the-code-api-for-swiftui).  
**Study focus (editorial, not observed transcript):** Review documented real-time API, webhook and variable behavior; secure secrets outside public client code.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 013. How to Create 3D Data Visualizations in Spline Using Variables and Real-Time APIs

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~14 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Kue1OjJ8KOE) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-3d-data-visualizations-in-spline-using-variables-and-real-time-apis).  
**Study focus (editorial, not observed transcript):** Review documented real-time API, webhook and variable behavior; secure secrets outside public client code. Study the variable graph, input/data changes and conditional actions.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 014. Design Interactions with Liquid Glass & 3D Transforms in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~16 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=IZM1H1xBQdk) · [Academy lesson](https://academy.spline.design/tutorials/design-interactions-with-liquid-glass-3d-transforms-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor. Compare glass/refraction controls with Lighting/PBR and scene performance constraints.  
**Verified chapters/timestamps:** 0:34 Build toggle · 2:28 Liquid Glass effect · 5:00 Interaction.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 015. Build an Interactive Keyboard with Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=2hLXgB3JV_U) · [Academy lesson](https://academy.spline.design/tutorials/build-an-interactive-keyboard-with-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 016. Create Liquid Glass Materials in 3D

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=gnhUypBNMc0) · [Academy lesson](https://academy.spline.design/tutorials/create-liquid-glass-materials-in-3d).  
**Study focus (editorial, not observed transcript):** Compare glass/refraction controls with Lighting/PBR and scene performance constraints. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 017. Create an Interactive Switch with Progressive Blur and Gradients

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~3 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=a-fKAlKbuP4) · [Academy lesson](https://academy.spline.design/tutorials/create-an-interactive-switch-with-progressive-blur-and-gradients).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 018. Design Interactive Effects with Progressive Blur and Smoothing Gradients

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=hr5wqdVX4co) · [Academy lesson](https://academy.spline.design/tutorials/design-interactive-effects-with-progressive-blur-and-smoothing-gradients).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 019. Create Interactive Designs That React to Your Mouse with Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=TgZdS8RK0bM) · [Academy lesson](https://academy.spline.design/tutorials/create-interactive-designs-that-react-to-your-mouse-with-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 020. How to Animate Along a Path with Hana and Spline

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=u-fEUpXoyCU) · [Academy lesson](https://academy.spline.design/tutorials/how-to-animate-along-a-path-with-hana-and-spline).  
**Study focus (editorial, not observed transcript):** Compare vector/path editing with 3D path profiles, object following and state-driven animation. Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 021. Create a 2D Follow Interaction

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=bKrapjgDBNo) · [Academy lesson](https://academy.spline.design/tutorials/create-a-2d-follow-interaction).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 022. Get Started with Interactive 2D in Hana

**Category:** Hana / 2D · **Level:** Beginner · **Academy duration:** ~17 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=DD8z1voLghU) · [Academy lesson](https://academy.spline.design/tutorials/get-started-with-interactive-2d-in-hana).  
**Study focus (editorial, not observed transcript):** Compare Hana frames, layers, vector tools, states/events and visual effect controls in the 2D editor.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 023. Create Animated 3D Blobs that React to Your Mouse

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=l32kDk5DU00) · [Academy lesson](https://academy.spline.design/tutorials/create-animated-3d-blobs-that-react-to-your-mouse).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 024. Build a 3D Voxel Character

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~12 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=0rZEe9obS_g) · [Academy lesson](https://academy.spline.design/tutorials/build-a-3d-voxel-character).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 025. Create a 3D Scroll Animation & Integrate into Framer

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~12 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=j5sEe5NQtUU) · [Academy lesson](https://academy.spline.design/tutorials/create-a-3d-scroll-animation-integrate-into-framer).  
**Study focus (editorial, not observed transcript):** Map scroll-driven interaction design and export integration; verify actual build steps in the linked lesson. Review web embed options, parent sizing, viewer settings and responsive behavior in the host.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 026. Trigger Interactions with Proximity Using the Distance Event

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=9U0l2_eKVMQ) · [Academy lesson](https://academy.spline.design/tutorials/trigger-interactions-with-proximity-using-the-distance-event).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 027. Add Mouse-Based Interactions to 3D Objects

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=rdZrrXFLxuw) · [Academy lesson](https://academy.spline.design/tutorials/add-mouse-based-interactions-to-3d-objects).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 028. Launch an Interactive 3D Storefront on Instant.so

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~3 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Thobux-qBQo) · [Academy lesson](https://academy.spline.design/tutorials/launch-an-interactive-3d-storefront-on-instantso).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 029. Get Started with 3D in Spline

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~26 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Kxz8fzU2OUE) · [Academy lesson](https://academy.spline.design/tutorials/get-started-with-3d-in-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Verified chapters/timestamps:** 0:19 Get Started · 0:27 Understanding the UI · 2:27 Version History · 3:05 Toolbar · 3:17 Spline Library · 4:13 Adjust frame size · 4:31 Comments · 4:41 Sharing.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 030. How to Embed 3D Scenes from Spline into Shopify

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=ZdE9NesjEiw) · [Academy lesson](https://academy.spline.design/tutorials/how-to-embed-3d-scenes-from-spline-into-shopify).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 031. Shape Interactive 3D Fluid Shapes That Follow the Cursor

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=5W0BSoS24Jk) · [Academy lesson](https://academy.spline.design/tutorials/shape-interactive-3d-fluid-shapes-that-follow-the-cursor).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 032. How to Sculpt a 3D Gummy Bear with Shape Blend

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~8 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=UKZ5dezNOeg) · [Academy lesson](https://academy.spline.design/tutorials/how-to-sculpt-a-3d-gummy-bear-with-shape-blend).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 033. Explore 3D Shape Blending in Spline

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~25 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=JIcnI0kUnFM) · [Academy lesson](https://academy.spline.design/tutorials/explore-3d-shape-blending-in-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 034. How to Build Reusable 3D Components

**Category:** 3D Fundamentals / Project · **Level:** Intermediate · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=eWuFrHiyyu0) · [Academy lesson](https://academy.spline.design/tutorials/how-to-build-reusable-3d-components).  
**Study focus (editorial, not observed transcript):** Use reusable main components, instances, overrides and detached instances. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 035. How to Set Up Real-Time APIs and Webhooks for Your 3D Scenes

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~15 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=b9o8-zYx3Qw) · [Academy lesson](https://academy.spline.design/tutorials/how-to-set-up-real-time-apis-and-webhooks-for-your-3d-scenes).  
**Study focus (editorial, not observed transcript):** Review the current export routes, including Public URL, viewer, code exports and third-party integration. Review documented real-time API, webhook and variable behavior; secure secrets outside public client code.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 036. Create 3D Icons from Scratch

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~15 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=yfNvUjxcG7M) · [Academy lesson](https://academy.spline.design/tutorials/create-3d-icons-from-scratch).  
**Study focus (editorial, not observed transcript):** Build simple primitives/vectors, materials and a small interaction, checking object count. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 037. How to Create a 3D Carousel Interaction

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~16 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=pR2AhQ22KwM) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-a-3d-carousel-interaction).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 038. Embed Interactive 3D Scenes into Wix Websites

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=ncoSN9mgWe8) · [Academy lesson](https://academy.spline.design/tutorials/embed-interactive-3d-scenes-into-wix-websites).  
**Study focus (editorial, not observed transcript):** Review the current export routes, including Public URL, viewer, code exports and third-party integration. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 039. Build an AI Voice Assistant in 3D

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=TPzHbYRRHzo) · [Academy lesson](https://academy.spline.design/tutorials/build-an-ai-voice-assistant-in-3d).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 040. Add Look At Animations to 3D Objects

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=L4fD9X_uhtc) · [Academy lesson](https://academy.spline.design/tutorials/add-look-at-animations-to-3d-objects).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 041. Captivating Skull Scene Atmosphere with Fog

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=i29GQQUxtl0) · [Academy lesson](https://academy.spline.design/tutorials/captivating-skull-scene-atmosphere-with-fog).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 042. Create Vibrant Glossy Materials using Matcaps

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=DhwA82tJK4M) · [Academy lesson](https://academy.spline.design/tutorials/create-vibrant-glossy-materials-using-matcaps).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 043. Master Lighting for 3D Scenes

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=RinPy7h_fhY) · [Academy lesson](https://academy.spline.design/tutorials/master-lighting-for-3d-scenes).  
**Study focus (editorial, not observed transcript):** Use lighting types, environment/HDRi, material response and shadow trade-offs. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 044. How to Create a Spinning 3D Icon

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~15 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=bzbL6eNEfek) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-a-spinning-3d-icon).  
**Study focus (editorial, not observed transcript):** Build simple primitives/vectors, materials and a small interaction, checking object count. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 045. How to Animate a 3D Walking Character

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=6g4XnfmD0tg) · [Academy lesson](https://academy.spline.design/tutorials/how-to-animate-a-3d-walking-character).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 046. Export Interactive Experiences Natively for iOS and visionOS

**Category:** Export / Integration · **Level:** Intermediate · **Academy duration:** ~15 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=44OPMq7FdD0) · [Academy lesson](https://academy.spline.design/tutorials/export-interactive-experiences-natively-for-ios-and-visionos).  
**Study focus (editorial, not observed transcript):** Review output destination, runtime support, image/video settings and play configuration.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 047. How to Export Native 3D for Android

**Category:** Export / Integration · **Level:** Intermediate · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Sot5W1iATGM) · [Academy lesson](https://academy.spline.design/tutorials/how-to-export-native-3d-for-android).  
**Study focus (editorial, not observed transcript):** Review output destination, runtime support, image/video settings and play configuration. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 048. How to Design Interactive Leaf Particles in 3D

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=n1QPSxD454k) · [Academy lesson](https://academy.spline.design/tutorials/how-to-design-interactive-leaf-particles-in-3d).  
**Study focus (editorial, not observed transcript):** Study emitter behavior, particle motion settings and event-driven control. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 049. How to Create 3D Button Interactions

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=B8o5O7PyKjY) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-3d-button-interactions).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 050. Create Playful 3D Abstract Illustrations in Spline

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~24 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=xc-ExwgYDQI) · [Academy lesson](https://academy.spline.design/tutorials/create-playful-3d-abstract-illustrations-in-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 051. Add More Easy Interactions with Drag & Drop

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=g3sMaFsFJQ0) · [Academy lesson](https://academy.spline.design/tutorials/add-more-easy-interactions-with-drag-drop).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 052. How to Easily Design a 3D Glass Cube

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~12 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=c32GIZUrlgs) · [Academy lesson](https://academy.spline.design/tutorials/how-to-easily-design-a-3d-glass-cube).  
**Study focus (editorial, not observed transcript):** Compare glass/refraction controls with Lighting/PBR and scene performance constraints. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 053. Apply Image & Video Textures to 3D Objects

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=MVnWnB0g5YA) · [Academy lesson](https://academy.spline.design/tutorials/apply-image-video-textures-to-3d-objects).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 054. How to Create 3D Layer Masks and Patterns with Spline

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=KhjpCA9ZQNo) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-3d-layer-masks-and-patterns-with-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 055. How to Add Interactive Designs Made in Spline into Figma

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Woi5g8UHpC8) · [Academy lesson](https://academy.spline.design/tutorials/how-to-add-interactive-designs-made-in-spline-into-figma).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 056. Create an Interactive 3D Character using Variables

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~17 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=eCxLYk2rNzg) · [Academy lesson](https://academy.spline.design/tutorials/create-an-interactive-3d-character-using-variables).  
**Study focus (editorial, not observed transcript):** Study the variable graph, input/data changes and conditional actions. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 057. How to Create an Iridescent Material Effect

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=i0YGxdn990Y) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-an-iridescent-material-effect).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 058. Create Flat 2D-Styles in 3D Scenes

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=rhuvJuptf-4) · [Academy lesson](https://academy.spline.design/tutorials/create-flat-2d-styles-in-3d-scenes).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 059. How to Create Interactive Magical Particles in Spline

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=q1K5nji8KHM) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-interactive-magical-particles-in-spline).  
**Study focus (editorial, not observed transcript):** Study emitter behavior, particle motion settings and event-driven control.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 060. Craft Seamless 3D Loop Animations

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=pUamUyt7EDU) · [Academy lesson](https://academy.spline.design/tutorials/craft-seamless-3d-loop-animations).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 061. Master Cameras to Create Dynamic Scenes

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~4 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=S4uHli4tNio) · [Academy lesson](https://academy.spline.design/tutorials/master-cameras-to-create-dynamic-scenes).  
**Study focus (editorial, not observed transcript):** Compare edit viewport movement, camera objects, and export/play camera controls.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 062. Create an Interactive Bee Character for the Web

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=hRy-Iqle6EU) · [Academy lesson](https://academy.spline.design/tutorials/create-an-interactive-bee-character-for-the-web).  
**Study focus (editorial, not observed transcript):** Review the current export routes, including Public URL, viewer, code exports and third-party integration.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 063. Animate Interactive 3D Boxes

**Category:** Motion / Animation · **Level:** Intermediate · **Academy duration:** ~4 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=RmC2xEtXobE) · [Academy lesson](https://academy.spline.design/tutorials/animate-interactive-3d-boxes).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 064. Bring an Interactive 3D Robot to Life

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=JPUSjRxQEKI) · [Academy lesson](https://academy.spline.design/tutorials/bring-an-interactive-3d-robot-to-life).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 065. Design Stylized 3D Text with Paths

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=QVRCZi0kyL0) · [Academy lesson](https://academy.spline.design/tutorials/design-stylized-3d-text-with-paths).  
**Study focus (editorial, not observed transcript):** Compare vector/path editing with 3D path profiles, object following and state-driven animation. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 066. How to Create Interactive Sand Particles in 3D

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=kS_EJGDYN-g) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-interactive-sand-particles-in-3d).  
**Study focus (editorial, not observed transcript):** Study emitter behavior, particle motion settings and event-driven control. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 067. Add Depth of Field Lens Blur for Photorealistic 3D Scenes

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=xoujiGBf5Ow) · [Academy lesson](https://academy.spline.design/tutorials/add-depth-of-field-lens-blur-for-photorealistic-3d-scenes).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 068. Create Dynamic Particle Effects in 3D

**Category:** Modeling / Simulation · **Level:** Intermediate · **Academy duration:** ~20 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=lRhLWE_cXkc) · [Academy lesson](https://academy.spline.design/tutorials/create-dynamic-particle-effects-in-3d).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 069. Use Variables to Create Interactive 3D Content

**Category:** Interactivity / Logic · **Level:** Advanced · **Academy duration:** ~24 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Id_SZVCUVMM) · [Academy lesson](https://academy.spline.design/tutorials/use-variables-to-create-interactive-3d-content).  
**Study focus (editorial, not observed transcript):** Study the variable graph, input/data changes and conditional actions. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 070. How to Build Drag & Drop Interactions in 3D

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=gDXVdJdLJfE) · [Academy lesson](https://academy.spline.design/tutorials/how-to-build-drag-drop-interactions-in-3d).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 071. How to Build 3D Multi-scenes and Import Animations

**Category:** Motion / Animation · **Level:** Intermediate · **Academy duration:** ~18 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=lpYK67LQItI) · [Academy lesson](https://academy.spline.design/tutorials/how-to-build-3d-multi-scenes-and-import-animations).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 072. Making sequential transitions in 3D - SplineLive

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~11 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=_3ETQW_C6s0) · [Academy lesson](https://academy.spline.design/tutorials/making-sequential-transitions-in-3d-splinelive).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 073. Create video textures in 3D - SplineLive

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=9LYRVdho8sE) · [Academy lesson](https://academy.spline.design/tutorials/create-video-textures-in-3d-splinelive).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 074. Camera orbit with transitions in 3D - SplineLive

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=mGYZmmZk5ro) · [Academy lesson](https://academy.spline.design/tutorials/camera-orbit-with-transitions-in-3d-splinelive).  
**Study focus (editorial, not observed transcript):** Compare edit viewport movement, camera objects, and export/play camera controls. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 075. How to Create 3D Paths in Spline

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~36 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=5pU7tGajw2E) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-3d-paths-in-spline).  
**Study focus (editorial, not observed transcript):** Study the + > Path flow, mesh profile settings, curve edits, and Align to Path modifier. Compare vector/path editing with 3D path profiles, object following and state-driven animation.  
**Verified chapters/timestamps:** 0:00 Create paths · 1:45 Round corners · 2:20 Path extrusion · 3:15 Depth and offset · 4:10 Angle/twist · 5:47 Custom vector shape · 8:33 Text shapes · 10:25 Gradient layers · 11:50 Animate parameters · 14:04 Infinite loops · 15:30 Cloner and path · 21:55 Animate objects along path · 28:58 Physics and path animation · 30:20 Convert 2D vectors to paths.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 076. How to Add a Follow Interaction to a 3D Object

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=TQe5Ae16rE8) · [Academy lesson](https://academy.spline.design/tutorials/how-to-add-a-follow-interaction-to-a-3d-object).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 077. How to Design and Use Components in 3D

**Category:** 3D Fundamentals / Project · **Level:** Intermediate · **Academy duration:** ~14 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=VSddFnDjPUA) · [Academy lesson](https://academy.spline.design/tutorials/how-to-design-and-use-components-in-3d).  
**Study focus (editorial, not observed transcript):** Use reusable main components, instances, overrides and detached instances. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 078. Animate Clones for 3D Motion Graphics

**Category:** Motion / Animation · **Level:** Intermediate · **Academy duration:** ~24 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=uhIDqxCG5Cc) · [Academy lesson](https://academy.spline.design/tutorials/animate-clones-for-3d-motion-graphics).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use Modifier > Cloner, distribution types and parameter animation.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 079. How to use logic in your 3D scenes with Spline

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=6XLvzJ9ngtg) · [Academy lesson](https://academy.spline.design/tutorials/how-to-use-logic-in-your-3d-scenes-with-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 080. Create a Drivable 3D Car with Physics and Game Controls

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~4 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=J5yi_scY2GE) · [Academy lesson](https://academy.spline.design/tutorials/create-a-drivable-3d-car-with-physics-and-game-controls).  
**Study focus (editorial, not observed transcript):** Understand physics objects, collision triggers and simulated motion. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 081. Add Physics Simulation to 3D Scenes

**Category:** Modeling / Simulation · **Level:** Intermediate · **Academy duration:** ~9 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=NdBpmhGvvW0) · [Academy lesson](https://academy.spline.design/tutorials/add-physics-simulation-to-3d-scenes).  
**Study focus (editorial, not observed transcript):** Understand physics objects, collision triggers and simulated motion. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 082. Animate Organic 3D Blobs with States

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=KclCVV4bnow) · [Academy lesson](https://academy.spline.design/tutorials/animate-organic-3d-blobs-with-states).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Define Base State and new states, then connect events to transition actions.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 083. Design a Glass Cube in 3D

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=IKkRtimo7Qc) · [Academy lesson](https://academy.spline.design/tutorials/design-a-glass-cube-in-3d).  
**Study focus (editorial, not observed transcript):** Compare glass/refraction controls with Lighting/PBR and scene performance constraints. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 084. How to create 3D blobs using Spline

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=td55wUvU66U) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-3d-blobs-using-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 085. Designing a 3D website with Spline and Framer

**Category:** Export / Integration · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=8bqkvfRuFYk) · [Academy lesson](https://academy.spline.design/tutorials/designing-a-3d-website-with-spline-and-framer).  
**Study focus (editorial, not observed transcript):** Review web embed options, parent sizing, viewer settings and responsive behavior in the host. Review the current export routes, including Public URL, viewer, code exports and third-party integration.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 086. Make a 3D Game Experience

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~17 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=yvehPjQhS5U) · [Academy lesson](https://academy.spline.design/tutorials/make-a-3d-game-experience).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 087. How to Enhance 3D Scenes with Bloom & Glow Effects

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~4 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=rMEU4LaVJKE) · [Academy lesson](https://academy.spline.design/tutorials/how-to-enhance-3d-scenes-with-bloom-glow-effects).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 088. Add Atmospheric Fog to 3D Scenes

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~3 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=C28JPxy4RDo) · [Academy lesson](https://academy.spline.design/tutorials/add-atmospheric-fog-to-3d-scenes).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 089. How to Create Stylized Toon Shading in 3D

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~4 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=5tq9R2zQxYg) · [Academy lesson](https://academy.spline.design/tutorials/how-to-create-stylized-toon-shading-in-3d).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 090. Add Stylized Outlines to 3D Objects

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~3 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Ol6h9dyijew) · [Academy lesson](https://academy.spline.design/tutorials/add-stylized-outlines-to-3d-objects).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 091. Build a Mini House Scene in 3D

**Category:** 3D Fundamentals / Project · **Level:** Intermediate · **Academy duration:** ~22 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=3uK_UTrl2ns) · [Academy lesson](https://academy.spline.design/tutorials/build-a-mini-house-scene-in-3d).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 092. Rotate & Animate 3D Objects

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=FhIVue3qOfE) · [Academy lesson](https://academy.spline.design/tutorials/rotate-animate-3d-objects).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 093. Set Up Photo Studio Lighting for 3D Scenes

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=PoScgWfatPI) · [Academy lesson](https://academy.spline.design/tutorials/set-up-photo-studio-lighting-for-3d-scenes).  
**Study focus (editorial, not observed transcript):** Use lighting types, environment/HDRi, material response and shadow trade-offs. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 094. Improve Realism by Adding Soft Shadows

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~2 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=z5q_CcaS0I4) · [Academy lesson](https://academy.spline.design/tutorials/improve-realism-by-adding-soft-shadows).  
**Study focus (editorial, not observed transcript):** Use the linked official lesson as a worked example; cross-check its controls against V2 documentation before following it.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 095. Refine & Style 3D Icons with Materials

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~8 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=7Jl27UWUqs0) · [Academy lesson](https://academy.spline.design/tutorials/refine-style-3d-icons-with-materials).  
**Study focus (editorial, not observed transcript):** Build simple primitives/vectors, materials and a small interaction, checking object count. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 096. Build 3D Icons with Vectors

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~10 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=CQM4hxQX9f4) · [Academy lesson](https://academy.spline.design/tutorials/build-3d-icons-with-vectors).  
**Study focus (editorial, not observed transcript):** Use vector geometry, point editing, masks and conversion to 3D where appropriate. Build simple primitives/vectors, materials and a small interaction, checking object count.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 097. Creating animation loops and blinking effects with Spline

**Category:** Motion / Animation · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=UbtGZ1pncpo) · [Academy lesson](https://academy.spline.design/tutorials/creating-animation-loops-and-blinking-effects-with-spline).  
**Study focus (editorial, not observed transcript):** Distinguish state-based transitions, timeline clips and animation export.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 098. Build a Dark Interactive Keyboard in 3D

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~15 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=1ZVdMR1qErw) · [Academy lesson](https://academy.spline.design/tutorials/build-a-dark-interactive-keyboard-in-3d).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 099. Build a 3D Light Switch with Interaction

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~12 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=lJIDSiDlhvw) · [Academy lesson](https://academy.spline.design/tutorials/build-a-3d-light-switch-with-interaction).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 100. How to Make a Frosted Glass 3D Icon

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~7 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=QuZH-t5zMbk) · [Academy lesson](https://academy.spline.design/tutorials/how-to-make-a-frosted-glass-3d-icon).  
**Study focus (editorial, not observed transcript):** Compare glass/refraction controls with Lighting/PBR and scene performance constraints. Build simple primitives/vectors, materials and a small interaction, checking object count.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 101. Modify 3D Shapes using Boolean Operations

**Category:** Modeling / Simulation · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=Ib-OD9gfBFI) · [Academy lesson](https://academy.spline.design/tutorials/modify-3d-shapes-using-boolean-operations).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 102. Making The Batman logo in 3D with Spline

**Category:** 3D Fundamentals / Project · **Level:** Beginner · **Academy duration:** ~5 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=HGMWURhKxc4) · [Academy lesson](https://academy.spline.design/tutorials/making-the-batman-logo-in-3d-with-spline).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 103. Timelapse: Model a Polaroid Go in 3D

**Category:** Modeling / Simulation · **Level:** Intermediate · **Academy duration:** ~18 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=g5CcAK67nEw) · [Academy lesson](https://academy.spline.design/tutorials/timelapse-model-a-polaroid-go-in-3d).  
**Study focus (editorial, not observed transcript):** Study parametric and editable geometry operations, then apply materials and lighting. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 104. Build a Realistic 3D Planet with Materials & Lighting

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=gAB5LCAatCE) · [Academy lesson](https://academy.spline.design/tutorials/build-a-realistic-3d-planet-with-materials-lighting).  
**Study focus (editorial, not observed transcript):** Use lighting types, environment/HDRi, material response and shadow trade-offs. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 105. Timelapse: Model Molang in 3D

**Category:** Modeling / Simulation · **Level:** Intermediate · **Academy duration:** ~14 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=JlrzLhEwMGI) · [Academy lesson](https://academy.spline.design/tutorials/timelapse-model-molang-in-3d).  
**Study focus (editorial, not observed transcript):** Study parametric and editable geometry operations, then apply materials and lighting. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 106. Designing a 3D toggle button micro-interaction with Spline

**Category:** Interactivity / Logic · **Level:** Beginner · **Academy duration:** ~13 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=zkw5GT9nYS8) · [Academy lesson](https://academy.spline.design/tutorials/designing-a-3d-toggle-button-micro-interaction-with-spline).  
**Study focus (editorial, not observed transcript):** Connect source events to transition or action targets, then validate in Preview. Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 107. Add a Smooth 3D Gradient Depth Effect

**Category:** Materials / Rendering · **Level:** Beginner · **Academy duration:** ~6 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=LY8HvCBvlJo) · [Academy lesson](https://academy.spline.design/tutorials/add-a-smooth-3d-gradient-depth-effect).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

#### 108. Design an Interactive 3D Keyboard

**Category:** Interactivity / Logic · **Level:** Intermediate · **Academy duration:** ~16 min (rounded).  
**Links:** [Watch official video](https://www.youtube.com/watch?v=cdru3Ibj8Eg) · [Academy lesson](https://academy.spline.design/tutorials/design-an-interactive-3d-keyboard).  
**Study focus (editorial, not observed transcript):** Use the current editor object/scene hierarchy, inspect modifiers and test in Preview.  
**Chapters/timestamps:** Not verified from the retrieved page.  
**Full transcript:** Not captured; not reproduced. See YouTube “Show transcript” where available.

## 7. Keyboard shortcuts — complete documented table

**Source of truth:** [Spline Keyboard Shortcuts](https://docs.spline.design/basics/keyboard-shortcuts) (3D editor, not Hana). Mac notation: **⌘ Command**, **⇧ Shift**, **⌃ Control**, **⌥ Option/Alt**. Some source cells contain `...` separators; these are not keyboard bindings and are excluded. One ambiguous Windows Zoom In cell and an unlisted Windows Ungroup binding are left flagged rather than guessed. **Hana Section shortcut `S`** is separately documented under [Sections in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/sections-in-hana).

| Action | macOS | Windows |
|---|---|---|
| Open / Import | `⌘ O` | `Ctrl + O` |
| Save File to Local | `⌘ ⇧ S` | `Ctrl + Shift + S` |
| Undo | `⌘ Z` | `Ctrl + Z` |
| Redo | `⌘ ⇧ Z` | `Ctrl + Shift + Z / Ctrl + Y` |
| Copy | `⌘ C` | `Ctrl + C` |
| Cut | `⌘ X` | `Ctrl + X` |
| Duplicate | `⌘ D` | `Ctrl + D` |
| Paste | `⌘ V` | `Ctrl + V` |
| Paste in Place | `⌘ ⇧ V` | `Ctrl + Shift + V` |
| Select All Objects | `⌘ A` | `Ctrl + A` |
| Unselect Objects | `ESC` | `ESC` |
| Rename | `⌃ R` | `Ctrl + R` |
| Toggle UI | `⌘ \\` | `Ctrl + \\` |
| Toggle Full Screen | `⌘ ⇧ F` | `Ctrl + Shift + F` |
| Zoom In | `⌘ +` | `Ctrl + (as displayed; ambiguous)` |
| Zoom Out | `⌘ -` | `Ctrl -` |
| Reset View / Camera | `⌥ R` | `Alt + R` |
| Group Selection | `⌘ G` | `Ctrl + G` |
| Ungroup Selection | `⌘ ⇧ G` | `Not listed by docs` |
| Delete Objects | `DELETE` | `DELETE` |
| Escape Creating Object | `ESC` | `ESC` |
| Rectangle | `R` | `R` |
| Ellipse | `O` | `O` |
| Triangle | `K` | `K` |
| Polygon | `J` | `J` |
| Switch to Local/World Space (TransformControls) | `L` | `L` |
| Focus Object | `S` | `S` |
| Orientated to Object | `⇧ S` | `Shift + S` |
| Zoom 100% | `⇧ 1` | `Shift + 1` |
| Perspective/Orthographic | `M` | `M` |
| Drag Copy | `⌘ + Drag` | `Ctrl + Drag` |
| Transform (Mirror) | `⌥` | `Alt` |
| Transform (Aspect Ratio) | `⇧` | `Shift` |
| Transform (Mirror & Aspect Ratio) | `⇧ ⌥` | `Shift + Alt` |
| Zoom (mouse) | `⌘ + Wheel` | `Ctrl + Wheel` |
| Pan (mouse) | `SPACE + Drag` | `SPACE + Drag` |
| Orbit (mouse) | `⌥ + Drag` | `Alt + Drag` |
| Zoom (trackpad) | `Pinch or ⌘ + 2 Finger Swipe` | `Pinch or Ctrl + Swipe` |
| Pan (trackpad) | `2 Finger drag` | `2 Finger drag` |
| Orbit (trackpad) | `⌥ + Tap & Drag` | `Alt + Tap & Drag` |
| Outliner: Select/deselect range with children | `⇧ Click` | `Shift + Click` |
| Outliner: Toggle multiple with children | `⌘ Click` | `Ctrl + Click` |
| Outliner: Single object without children | `⌥ ⌘ Click` | `Alt + Ctrl + Click` |
| Outliner: Multiple without children | `⌥ ⌘ ⇧ Click` | `Alt + Ctrl + Shift + Click` |
| Viewport: Toggle objects with children one-by-one | `⇧ Click` | `Shift + Click` |
| Viewport: Select multiple with children | `⇧ + Drag` | `Shift + Drag` |
| Viewport: Single without children | `⌥ ⌘ Click` | `Alt + Ctrl + Click` |
| Viewport: Multiple without children (drag) | `⌥ ⌘ Drag` | `Alt + Ctrl + Drag` |
| Viewport: Toggle without children one-by-one | `⌥ ⌘ ⇧ Click` | `Alt + Ctrl + Shift + Click` |
| Viewport: Multiple without children (drag) | `⌥ ⌘ ⇧ Drag` | `Alt + Ctrl + Shift + Drag` |

### Additional documented, context-specific shortcuts

- **Hana Section:** `S` (only when Hana is active), via Frame dropdown or shortcut. [Sections in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/sections-in-hana).
- **Spline 3D Pen curve modifier:** Ctrl/Cmd (Bend) and Alt/Option while dragging handle to break curve. [Pen Tool](https://docs.spline.design/designing-in-3-d/objects/pen-tool).
- **Create a 3D component:** Spline docs list `Shift+Cmd+K` on macOS. Windows equivalent is not explicitly provided on this page. [Components](https://docs.spline.design/designing-in-3-d/scenes/components).

---

## 8. Documentation source directory

The following are official documentation URLs recovered from the Firecrawl map/crawl; groups are organizational categories. This is a navigable directory rather than a copy of every source page. Number of canonical unique links in this directory is recorded below. Index entries are not proof that every site page or panel state was independently checked in a live editor. Published docs can change after this research snapshot.

**Indexed canonical source URLs in this directory: 193.**

### Basics and platform (9 pages)

- [What Is Spline](https://docs.spline.design/basics/what-is-spline)
- [How Is Spline Different](https://docs.spline.design/basics/how-is-spline-different)
- [Creating Your First Scene](https://docs.spline.design/basics/creating-your-first-scene)
- [Understanding Splines Ui](https://docs.spline.design/basics/understanding-splines-ui)
- [Watch Intro Tutorials](https://docs.spline.design/basics/watch-intro-tutorials)
- [Keyboard Shortcuts](https://docs.spline.design/basics/keyboard-shortcuts)
- [Change Theme On Spline](https://docs.spline.design/basics/change-theme-on-spline)
- [Download Spline For Desktop](https://docs.spline.design/basics/download-spline-for-desktop)
- [Faq](https://docs.spline.design/basics/faq)

### Objects, geometry and modeling (11 pages)

- [Working With 2D And 3D Objects](https://docs.spline.design/designing-in-3-d/objects/working-with-2d-and-3d-objects)
- [Working With Parametric Objects](https://docs.spline.design/designing-in-3-d/objects/working-with-parametric-objects)
- [Extruding 2D Objects In 3 D](https://docs.spline.design/designing-in-3-d/objects/extruding-2d-objects-in-3-d)
- [Working With Text](https://docs.spline.design/designing-in-3-d/objects/working-with-text)
- [Pen Tool](https://docs.spline.design/designing-in-3-d/objects/pen-tool)
- [3D Paths](https://docs.spline.design/designing-in-3-d/objects/3d-paths)
- [Moving The Object Pivot](https://docs.spline.design/designing-in-3-d/objects/moving-the-object-pivot)
- [3D Modeling Tools](https://docs.spline.design/designing-in-3-d/modeling/3d-modeling-tools)
- [3D Sculpting](https://docs.spline.design/designing-in-3-d/modeling/3d-sculpting)
- [Boolean Operations](https://docs.spline.design/designing-in-3-d/modeling/boolean-operations)
- [Shape Blend](https://docs.spline.design/designing-in-3-d/modeling/shape-blend)

### Animation, simulation, scenes (10 pages)

- [Timeline Animation](https://docs.spline.design/designing-in-3-d/animation/timeline-animation)
- [Cloner Motion](https://docs.spline.design/designing-in-3-d/animation/cloner-motion)
- [Physics](https://docs.spline.design/designing-in-3-d/animation/physics)
- [Particles](https://docs.spline.design/designing-in-3-d/animation/particles)
- [Hair Systems](https://docs.spline.design/designing-in-3-d/animation/hair-systems)
- [Components](https://docs.spline.design/designing-in-3-d/scenes/components)
- [3D Library](https://docs.spline.design/designing-in-3-d/scenes/3d-library)
- [Multi Scenes](https://docs.spline.design/designing-in-3-d/scenes/multi-scenes)
- [3D Gaussian Splatting](https://docs.spline.design/designing-in-3-d/scenes/3d-gaussian-splatting)
- [Version History](https://docs.spline.design/designing-in-3-d/scenes/version-history)

### Materials and shading (26 pages)

- [Material Library](https://docs.spline.design/materials-shading/basics/material-library)
- [Creating Material Layers](https://docs.spline.design/materials-shading/basics/creating-material-layers)
- [Pbr Materials](https://docs.spline.design/materials-shading/basics/pbr-materials)
- [Material Color And Image Assets](https://docs.spline.design/materials-shading/basics/material-color-and-image-assets)
- [Layer Masking](https://docs.spline.design/materials-shading/basics/layer-masking)
- [Color Layer](https://docs.spline.design/materials-shading/color-and-texture/color-layer)
- [Vertex Color Layer](https://docs.spline.design/materials-shading/color-and-texture/vertex-color-layer)
- [Gradient Layer](https://docs.spline.design/materials-shading/color-and-texture/gradient-layer)
- [Image Layer](https://docs.spline.design/materials-shading/color-and-texture/image-layer)
- [Video Layer](https://docs.spline.design/materials-shading/color-and-texture/video-layer)
- [Pattern Layer](https://docs.spline.design/materials-shading/color-and-texture/pattern-layer)
- [Noise Layer](https://docs.spline.design/materials-shading/color-and-texture/noise-layer)
- [Rainbow Layer](https://docs.spline.design/materials-shading/color-and-texture/rainbow-layer)
- [Lighting Layer](https://docs.spline.design/materials-shading/shading-and-reflection/lighting-layer)
- [Toon Layer](https://docs.spline.design/materials-shading/shading-and-reflection/toon-layer)
- [Matcap Layer](https://docs.spline.design/materials-shading/shading-and-reflection/matcap-layer)
- [Fresnel Layer](https://docs.spline.design/materials-shading/shading-and-reflection/fresnel-layer)
- [Glass Layer](https://docs.spline.design/materials-shading/shading-and-reflection/glass-layer)
- [Reflection Layer](https://docs.spline.design/materials-shading/shading-and-reflection/reflection-layer)
- [Depth Layer 3D Gradient](https://docs.spline.design/materials-shading/shading-and-reflection/depth-layer-3d-gradient)
- [Normal Layer](https://docs.spline.design/materials-shading/surface-detail/normal-layer)
- [Bump Map Roughness Map](https://docs.spline.design/materials-shading/surface-detail/bump-map-roughness-map)
- [Displace Layer](https://docs.spline.design/materials-shading/surface-detail/displace-layer)
- [Cavity Layer](https://docs.spline.design/materials-shading/surface-detail/cavity-layer)
- [Dust Layer](https://docs.spline.design/materials-shading/surface-detail/dust-layer)
- [Outline Layer](https://docs.spline.design/materials-shading/surface-detail/outline-layer)

### Lighting and cameras (11 pages)

- [Working With Lights](https://docs.spline.design/lighting/working-with-lights)
- [Environment And Hdri](https://docs.spline.design/lighting/environment-and-hdri)
- [Directional Light](https://docs.spline.design/lighting/directional-light)
- [Point Light](https://docs.spline.design/lighting/point-light)
- [Spot Light](https://docs.spline.design/lighting/spot-light)
- [Soft Shadows](https://docs.spline.design/lighting/soft-shadows)
- [Working With Cameras](https://docs.spline.design/cameras/working-with-cameras)
- [Camera Parameters](https://docs.spline.design/cameras/camera-parameters)
- [Depth Of Field Dof](https://docs.spline.design/cameras/depth-of-field-dof)
- [Effects Post Processing](https://docs.spline.design/cameras/effects-post-processing)
- [Working With Fog](https://docs.spline.design/cameras/working-with-fog)

### Agents and code (9 pages)

- [Ai Agent](https://docs.spline.design/spline-ai/ai-agent)
- [Ai Textures](https://docs.spline.design/spline-ai/ai-textures)
- [Ai Style Transfer](https://docs.spline.design/spline-ai/ai-style-transfer)
- [Spell Ai 3D Worlds](https://docs.spline.design/spline-ai/spell-ai-3d-worlds)
- [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab)
- [Ai 3D Generation](https://docs.spline.design/generate/ai-3d-generation)
- [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill)
- [Spline Mcp Server](https://docs.spline.design/generate/spline-mcp-server)
- [Chatgpt](https://docs.spline.design/generate/plugins/chatgpt)

### 3D interactions: concepts and data (10 pages)

- [How State Based Animation Works](https://docs.spline.design/interaction-states-events-and-actions/concepts/how-state-based-animation-works)
- [Events Interactivity](https://docs.spline.design/interaction-states-events-and-actions/concepts/events-interactivity)
- [Animatable Properties](https://docs.spline.design/interaction-states-events-and-actions/concepts/animatable-properties)
- [Mouse Key Toggle Property](https://docs.spline.design/interaction-states-events-and-actions/concepts/mouse-key-toggle-property)
- [Input](https://docs.spline.design/interaction-states-events-and-actions/concepts/input)
- [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables)
- [Real Time Api](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api)
- [Webhooks](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/webhooks)
- [Ai Text Open Ai Api](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/ai-text-open-ai-api)
- [Ai Voice Assistant Api](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/ai-voice-assistant-api)

### 3D events (23 pages)

- [Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event)
- [Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event)
- [Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event)
- [Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event)
- [Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event)
- [Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event)
- [Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event)
- [Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event)
- [Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event)
- [Look At Event](https://docs.spline.design/interaction-states-events-and-actions/events/look-at-event)
- [Follow Event](https://docs.spline.design/interaction-states-events-and-actions/events/follow-event)
- [Game Controls Event](https://docs.spline.design/interaction-states-events-and-actions/events/game-controls-event)
- [Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event)
- [State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event)
- [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event)
- [Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event)
- [Drag And Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event)
- [Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event)
- [Screen Resize Event](https://docs.spline.design/interaction-states-events-and-actions/events/screen-resize-event)
- [Api Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event)
- [Webhook Called Event](https://docs.spline.design/interaction-states-events-and-actions/events/webhook-called-event)
- [Ai Assistant Listener Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-listener-event)
- [Ai Assistant Trigger Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-trigger-event)

### 3D actions (16 pages)

- [Animation Action](https://docs.spline.design/interaction-states-events-and-actions/actions/animation-action)
- [Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action)
- [Sound Action](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action)
- [Video Action](https://docs.spline.design/interaction-states-events-and-actions/actions/video-action)
- [Open Link Action](https://docs.spline.design/interaction-states-events-and-actions/actions/open-link-action)
- [Reset Scene Action](https://docs.spline.design/interaction-states-events-and-actions/actions/reset-scene-action)
- [Switch Camera Action](https://docs.spline.design/interaction-states-events-and-actions/actions/switch-camera-action)
- [Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action)
- [Destroy Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/destroy-object-action)
- [Scene Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/scene-transition-action)
- [Particles Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/particles-control-action)
- [Variable Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/variable-control-action)
- [Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action)
- [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action)
- [Clear Local Storage Action](https://docs.spline.design/interaction-states-events-and-actions/actions/clear-local-storage-action)
- [Api Request Action](https://docs.spline.design/interaction-states-events-and-actions/actions/api-request-action)

### Import and export (26 pages)

- [Import Animated Objects](https://docs.spline.design/importing-content/import-animated-objects)
- [Morph Targets](https://docs.spline.design/importing-content/morph-targets)
- [How To Import Content](https://docs.spline.design/importing-content/how-to-import-content)
- [Cad To Spline Optimization Best Practices](https://docs.spline.design/importing-content/cad-to-spline-optimization-best-practices)
- [Play Mode](https://docs.spline.design/exporting-your-scene/play-mode)
- [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings)
- [How To Optimize Your Scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene)
- [Exporting As Public Urls](https://docs.spline.design/exporting-your-scene/web/exporting-as-public-ur-ls)
- [Exporting As Spline Viewer](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer)
- [Exporting As Code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code)
- [Exporting As Self Hosted Project](https://docs.spline.design/exporting-your-scene/web/exporting-as-self-hosted-project)
- [Code Api For Web](https://docs.spline.design/exporting-your-scene/web/code-api-for-web)
- [Native 3D Embeds For Ios](https://docs.spline.design/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os)
- [I Os App Generation](https://docs.spline.design/exporting-your-scene/apple-platform/i-os-app-generation)
- [Spline Mirror For Visionos](https://docs.spline.design/exporting-your-scene/apple-platform/spline-mirror-for-vision-os)
- [Code Api For Swift Ui](https://docs.spline.design/exporting-your-scene/apple-platform/code-api-for-swift-ui)
- [Native 3D Embeds For Android](https://docs.spline.design/exporting-your-scene/android/native-3d-embeds-for-android)
- [Android Package Apk](https://docs.spline.design/exporting-your-scene/android/android-package-apk)
- [Android App Bundles Aab](https://docs.spline.design/exporting-your-scene/android/android-app-bundles-aab)
- [Code Api For Kotlin](https://docs.spline.design/exporting-your-scene/android/code-api-for-kotlin)
- [Exporting As An Image](https://docs.spline.design/exporting-your-scene/files/exporting-as-an-image)
- [Exporting As Video](https://docs.spline.design/exporting-your-scene/files/exporting-as-video)
- [Exporting Image Sequences](https://docs.spline.design/exporting-your-scene/files/exporting-image-sequences)
- [Exporting As Gltf Glb](https://docs.spline.design/exporting-your-scene/files/exporting-as-gtlf-glb)
- [Exporting As Usdz](https://docs.spline.design/exporting-your-scene/files/exporting-as-usdz)
- [Exporting As Stl 3D Printing](https://docs.spline.design/exporting-your-scene/files/exporting-as-stl-3d-printing)

### Hana editor (12 pages)

- [What Is Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/what-is-hana)
- [Designing In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana)
- [Auto Layout And Constraints](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints)
- [Pages In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/pages-in-hana)
- [Sections In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/sections-in-hana)
- [Interactivity In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana)
- [Effects In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/effects-in-hana)
- [3D Shapes In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana)
- [Frame As Fill 3D Meshes](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/frame-as-fill-3d-meshes)
- [Ai In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/ai-in-hana)
- [Importing Assets To Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/importing-assets-to-hana)
- [Exporting In Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/exporting-in-hana)

### Integrations and code generation (19 pages)

- [Integrating With Framer](https://docs.spline.design/integrations/integrating-with-framer)
- [Integrating With Figma](https://docs.spline.design/integrations/integrating-with-figma)
- [Integrating With Webflow](https://docs.spline.design/integrations/integrating-with-webflow)
- [Integrating With Notion](https://docs.spline.design/integrations/integrating-with-notion)
- [Integrating With Shopify](https://docs.spline.design/integrations/integrating-with-shopify)
- [Integrating With Play](https://docs.spline.design/integrations/integrating-with-play)
- [Integrating With Wix](https://docs.spline.design/integrations/integrating-with-wix)
- [Integrating With Wix Studio](https://docs.spline.design/integrations/integrating-with-wix-studio)
- [Integrating With Typedream](https://docs.spline.design/integrations/integrating-with-typedream)
- [Integrating With Tome](https://docs.spline.design/integrations/integrating-with-tome)
- [Integrating With Toddle](https://docs.spline.design/integrations/integrating-with-toddle)
- [Integrating With Instant So](https://docs.spline.design/integrations/integrating-with-instant-so)
- [Adding Spline To V0](https://docs.spline.design/codegen-tools/adding-spline-to-v0)
- [Adding Spline To Lovable](https://docs.spline.design/codegen-tools/adding-spline-to-lovable)
- [Adding Spline To Bolt New](https://docs.spline.design/codegen-tools/adding-spline-to-bolt-new)
- [Adding Spline To Replit](https://docs.spline.design/codegen-tools/adding-spline-to-replit)
- [Adding Spline To Cursor](https://docs.spline.design/codegen-tools/adding-spline-to-cursor)
- [Adding Spline To Claude Code](https://docs.spline.design/codegen-tools/adding-spline-to-claude-code)
- [Adding Spline To Github Copilot](https://docs.spline.design/codegen-tools/adding-spline-to-github-copilot)

### Workspace and account (11 pages)

- [Files View](https://docs.spline.design/sharing-collaboration-and-workspaces/files-view)
- [Workspaces](https://docs.spline.design/sharing-collaboration-and-workspaces/workspaces)
- [File Sharing](https://docs.spline.design/sharing-collaboration-and-workspaces/file-sharing)
- [Real Time Collaboration In 3 D](https://docs.spline.design/sharing-collaboration-and-workspaces/real-time-collaboration-in-3-d)
- [Comments Feedback In 3 D](https://docs.spline.design/sharing-collaboration-and-workspaces/comments-feedback-in-3-d)
- [Team Libraries](https://docs.spline.design/sharing-collaboration-and-workspaces/team-libraries)
- [Community Platform](https://docs.spline.design/sharing-collaboration-and-workspaces/community-platform)
- [Pricing](https://docs.spline.design/account/pricing)
- [Subscriptions And Renewal](https://docs.spline.design/account/subscriptions-and-renewal)
- [Spline For Enterprise](https://docs.spline.design/account/spline-for-enterprise)
- [Content Training](https://docs.spline.design/account/content-training)

## 9. Structured extraction schema and QA

### 9.1 Stable machine-readable UI schema

A companion JSON file contains the same fields requested for the UI extractor, plus a `source_url` for provenance. Null shortcut = no verified shortcut stated by the page. The extraction is normalized and editorially checked against the docs, not a dump of hallucinated AI JSON fields. Sample:

```json
{
  "mode": "3D Edit",
  "location": "Right panel > Modifiers",
  "element_name": "Cloner",
  "how_to_access": "Select object > Modifiers > + > Cloner",
  "what_it_does": "Procedurally repeat an object",
  "related_tools_or_options": ["Radial", "Linear", "Grid", "Object", "Randomness"],
  "keyboard_shortcut": null,
  "notes": "",
  "source_url": "https://docs.spline.design/designing-in-3-d/animation/cloner-motion"
}
```

### 9.2 Validation procedure and actual limits

- Confirmed the docs crawl completed (210 entries) and the Academy crawl completed (110 entries) in Firecrawl; some entries are duplicates/alternate Markdown endpoints.
- Compared core interface descriptions with [Understanding Spline's UI](https://docs.spline.design/basics/understanding-splines-ui), [Modeling Tools](https://docs.spline.design/designing-in-3-d/modeling/3d-modeling-tools), [Pen Tool](https://docs.spline.design/designing-in-3-d/objects/pen-tool), [Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana), [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab), and [Shortcuts](https://docs.spline.design/basics/keyboard-shortcuts).
- Retrieved canonical video IDs, names, rounded durations and level from the Academy's index. This covers **108 unique catalog entries**, not all possible YouTube uploads by Spline.
- Firecrawl returned some video description text and chapter anchors, **but not the complete transcripts**, and other videos returned anti-bot/login shells. Therefore transcript fields remain unavailable, not falsely marked captured.
- Public app inspection attempted with Firecrawl Interact but returned a WebGL unsupported page; actual live editor panel activation was **not** exercised.
- This document may miss undocumented buttons, feature-flagged panels or differences under other account tiers; consult live Spline for exact version/plan-specific affordances.

### 9.3 Sources and historical transition

- [Current documentation home](https://docs.spline.design/)
- [Understanding Spline's UI (3D/Hana)](https://docs.spline.design/basics/understanding-splines-ui)
- [Spline V2 release, August 20, 2026](https://blog.spline.design/spline-v2)
- [Academy tutorials index](https://academy.spline.design/)
- [Official Spline YouTube channel](https://www.youtube.com/@splinetool)
- [Official Spline MCP documentation](https://docs.spline.design/generate/spline-mcp-server)

**Maintainer rule for future updates:** re-map docs and Academy; diff URL inventories; re-scrape any changed panel pages; validate new shortcuts against UI; never assume a 2025 video describes 2026 tool placement; record the date and evidence status of each updated field.
