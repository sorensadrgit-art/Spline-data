# How is Spline different? (/basics/how-is-spline-different)

> How Spline compares to traditional 3D tools like Blender, Maya and Cinema 4D.



Like Blender, Cinema 4D, 3ds Max or Maya, Spline is a tool for creating 3D
content — but it is built around collaboration, the web, and interactive output
rather than around rendered frames. The differences that matter most:

* **It's web-based.** Spline runs in the browser on any platform, with nothing
  to install and no GPU requirements to check. Files live in the cloud, so there
  are no local project folders to manage or hand around.
* **It's multiplayer.** Several people can edit the same file at the same time
  and give feedback in place, the way they would in a 2D design tool.

  [Real-time Collaboration in 3D](https://docs.spline.design/sharing-collaboration-and-workspaces/real-time-collaboration-in-3-d.md)
* **It works in real time.** What you see in the editor is what ships. There is
  no render step and no waiting for frames.
* **The output is interactive, not a picture of your work.** You publish a live
  scene that responds to clicks, scroll, keys and collisions — embeddable on any
  site or app — instead of exporting a still or a video.

  [Events & Interactivity](https://docs.spline.design/interaction-states-events-and-actions/concepts/events-interactivity.md),
  [Exporting as Public URLs](https://docs.spline.design/exporting-your-scene/web/exporting-as-public-ur-ls.md)
* **Animation is state-based.** Instead of keying every property on a timeline,
  you define states and let Spline animate between them — though a timeline is
  there when you want one.

  [How state-based animation works](https://docs.spline.design/interaction-states-events-and-actions/concepts/how-state-based-animation-works.md)
* **It uses a 2D approach to 3D.** Materials are stacked layers, not shader
  graphs, and the interface borrows its conventions from graphic design tools.
  That makes it far quicker to learn if you've never opened a 3D application.

  [Creating Material Layers](https://docs.spline.design/materials-shading/basics/creating-material-layers.md)
* **Code is optional, and it lives in the file.** Most work needs none, but a
  file can carry its own HTML, CSS and JavaScript over the 3D canvas, with an
  injected `spline` API for driving the scene — no build step, no separate
  repo, and it ships with the scene when you publish.

  [Code Tab](https://docs.spline.design/interaction-states-events-and-actions/code-tab.md)
* **3D and 2D live in the same product.** Hana, Spline's 2D canvas, shares the
  same interactivity model, collaboration and publishing pipeline as the 3D
  editor — so an interface and the 3D content inside it are built in one tool.

  [What is Hana?](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/what-is-hana.md)
* **An AI agent can do the work with you.** Describe what you want and it builds
  it through the editor itself, leaving fully editable results behind.

  [AI Agent](https://docs.spline.design/spline-ai/ai-agent.md)

For a full tour of what the product includes, see
[What is Spline?](https://docs.spline.design/basics/what-is-spline.md).
