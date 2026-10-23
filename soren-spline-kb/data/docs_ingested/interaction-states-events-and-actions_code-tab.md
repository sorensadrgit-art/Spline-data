# Code Tab (/interaction-states-events-and-actions/code-tab)

> Write code inside a Spline file — the Code tab holds an HTML document layered over the 3D canvas, with a spline API for driving the scene.



The **Code tab** is where a Spline file's own code lives. A file can carry one
**HTML document** — markup, CSS and JavaScript — that the editor renders in a
sandboxed iframe layered exactly over the 3D canvas. Anything you build there
sits on top of the live scene, and an injected `spline` API lets it read and
drive that scene.

It covers two jobs:

* **Web UI over the scene** — HUDs, dashboards, panels, forms and controls.
* **Behavior and motion code** — animation loops, interaction logic, game
  loops. A document can be *headless*: one `<script>` and nothing visible.

The document is part of the file. It saves with it, it's undoable, it syncs to
collaborators, and it ships with your exports.

<Callout type="info">
  This is different from the [Code API for Web](https://docs.spline.design/exporting-your-scene/web/code-api-for-web.md),
  which drives an **already-published** scene from your own site. The Code tab
  lives *inside* the Spline file and travels with it.
</Callout>

***

## Where to find it [#where-to-find-it]

The Code tab is one of three **Preview | Edit | Code** tabs at the top of the
editor, which switch what the stage shows:

| Tab         | What it shows                                                             |
| ----------- | ------------------------------------------------------------------------- |
| **Preview** | The scene running with your HTML composited over it — what a visitor sees |
| **Edit**    | The bare 3D scene, nothing executing, full editing                        |
| **Code**    | The HTML document's source, over the scene                                |

Open **Code** to write or edit the document. A **Console** strip captures your
`console.*` output and any errors, so `console.log` is the way to debug.

***

## The document [#the-document]

One complete HTML document per file. Your CSS and JavaScript go inline, in the
document itself.

**External libraries work.** `<script src="…">` and remote stylesheets load
normally, so reach for a chart or animation library when it genuinely helps.
Prefer inline code for small things: every remote script is one more thing that
can fail to load at export time.

**Don't rebuild the scene in HTML.** The 3D content is behind you and stays
Spline's job — no WebGL canvases of your own.

### Two layout rules [#two-layout-rules]

1. **Keep the page background transparent.** Don't set a background on `html`
   or `body` — the 3D scene shows through everywhere you don't paint. Style
   your own panels and cards instead.
2. **Pointer events pass through the background.** Clicks on `html`/`body`
   reach the 3D viewport, so orbiting and scene interactions keep working
   between your UI elements. Events on your own elements stay yours — keep
   interactive HTML compact so the scene behind it stays reachable.

Position UI with `fixed` or `absolute` CSS against the full viewport — the
frame covers the canvas exactly.

***

## Talking to the scene [#talking-to-the-scene]

A `spline` object is injected into the document before your scripts run. It is
the seam between your code and the file's 3D content, and it works in both
directions:

* **Read the scene** — variables, the objects in the file and their current
  transforms, and a mesh's live geometry.
* **Drive the scene** — move, hide and restyle objects, change geometry
  parameters, and write variables.
* **Create at runtime** — copy a template object, clone an existing one, or
  build new primitives, text and lights from code.
* **React to what happens** — listen for variable changes and for the events
  you authored on objects, or trigger those events yourself.
* **Go beyond the layer system** — supply custom three.js materials for looks
  Spline's material layers can't express.

<Callout>
  Everything your code changes is **transient**: it's runtime state, never saved
  to the file and never added to undo history, and it resets on reload. That's
  what you want for interactive controls — but if something should permanently
  change the file, edit it in the scene instead.
</Callout>

***

## Edit mode vs Play mode [#edit-mode-vs-play-mode]

* Reads, object updates and variable writes work **while editing**, so you can
  build against the scene in place.
* Events you authored on objects only fire in **Play mode** — the interaction
  system is off while editing, and trying to trigger one warns in the console
  instead.

***

## What ships with exports [#what-ships-with-exports]

The HTML travels with the scene automatically:

| Export                                                                                | HTML content                          |
| ------------------------------------------------------------------------------------- | ------------------------------------- |
| [Public URL](https://docs.spline.design/exporting-your-scene/web/exporting-as-public-ur-ls.md)                     | ✅                                     |
| [`<spline-viewer>` embed](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer.md)       | ✅                                     |
| [Code export](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md) running the Spline runtime | ✅                                     |
| three.js / react-three-fiber code export                                              | ❌ — these don't use the Spline engine |

Exports always run in play mode, so the full event system is live there.

<Callout type="warn">
  Custom three.js materials work in the editor and in web exports, but are **not
  supported in `<spline-viewer>` embeds**. If you use them, fall back to a
  layered material so the scene still reads everywhere.
</Callout>

***

## Let the agent write it [#let-the-agent-write-it]

You don't have to write the document by hand. The
[AI Agent](https://docs.spline.design/spline-ai/ai-agent.md) can write and edit the document for you —
describe the UI or behavior you want and it produces the markup and the
`spline` calls, leaving source you can edit in the Code tab.
