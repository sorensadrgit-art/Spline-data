# AI Agent in Hana (/hana-a-canvas-for-interactivity/ai-in-hana)

> Describe a screen and Hana designs it — layouts, styling, interactivity and images, all editable afterwards.



Hana's **AI Agent** designs for you. Describe a screen and it builds it on the
canvas: layout, type, colour, effects, states and interactions. Ask for changes
and it edits what's already there.

Everything it makes is **ordinary Hana content** — real frames, text, shapes and
vectors you can select, restyle and rearrange by hand. Nothing is locked or
flattened.

<Callout type="tip">
  Looking for the 3D editor instead? It has its own assistant — see
  [AI Agent](https://docs.spline.design/spline-ai/ai-agent.md).
</Callout>

<Callout>
  The agent runs on your workspace's monthly **AI credits**, included with every
  paid plan. See [AI credits](https://docs.spline.design/account/pricing.md#ai-credits).
</Callout>

***

## Where to find it [#where-to-find-it]

Open the AI panel from the left of the Hana editor and type into the prompt box
at the bottom.

The prompt tells you what it expects:

| When                         | Placeholder                                         |
| ---------------------------- | --------------------------------------------------- |
| Empty canvas                 | *Describe your design…*                             |
| After it has built something | *Describe changes… (e.g. "Make the button red")*    |
| While it's working           | *Describe another change… (starts a parallel chat)* |

Along the bottom of the panel: the **paperclip** attaches a reference, and the
**model** and **effort** pickers sit beside it. Above the prompt box you'll find
your selection chips, any attachments, and a credits banner once you pass 90% of
your monthly allowance.

At the top right of the panel, **Chat history** lists your previous conversations
in this file, and **New chat** starts a fresh one.

***

## Writing a good prompt [#writing-a-good-prompt]

* **Describe the screen, not the shapes.** "A settings screen with a profile row,
  three toggles and a sign-out button" gets much further than a list of rectangles.
* **Name the platform if it matters.** Say "iOS app screen" or "marketing landing
  page" and the layout conventions follow.
* **Select first, then say "this".** Whatever you have selected becomes the target
  of an unqualified change; the chips above the prompt box show exactly what the
  agent will act on.
* **Iterate in small steps.** "Tighten the spacing", "make the header sticky",
  "use a warmer palette" land more predictably than one long brief.

### Attaching references [#attaching-references]

The **paperclip** attaches an **image or video** — a screenshot to match, a brand
reference, a photo to build around. You can also **drag files straight onto the
panel**; it shows *Drop images or videos to attach* while you drag.

You can attach a **3D model** the same way. Drop a glTF file onto the panel and the
agent can place it in the design — see
[3D Shapes in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana.md).

***

## What the agent can do [#what-the-agent-can-do]

* **Build and edit frames** — layout, type, colour, strokes, fills and spacing.
* **Add effects** — the blurs, shadows, noise and glass treatments covered in
  [Effects in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/effects-in-hana.md).
* **Wire interactivity** — states, events and actions, so a prototype responds to
  clicks and hovers. See
  [Interactivity in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana.md).
* **Generate images** — ask for imagery and it creates and places it, rather than
  you generating separately and importing.
* **Fix what you point out** — "the button is overlapping the title" or "this text
  is too small" works, and it corrects the frame in place.

***

## Asking for several screens at once [#asking-for-several-screens-at-once]

The agent can design **more than one frame in a single request**. Ask for
"three landing pages", "a mobile and a desktop version" or "5 variations" and it
creates a frame for each and builds them **at the same time**, not one after
another.

You'll see an empty frame appear for each screen as soon as it starts, so you can
watch them fill in parallel. Each finished frame then gets its own review pass to
catch overlaps and visual mistakes.

<Callout type="warn">
  **A long description is still one screen.** Listing lots of sections, widgets or
  features — "a dashboard with a sidebar, a chart, a stats row and a settings
  panel" — describes *one* design made of those parts, not four frames. You get
  several frames only when you ask for several **screens**, **designs** or
  **variants**.
</Callout>

Asking for a variant of something that already exists — "a dark mode of this", "a
mobile version" — matches the size of the frame you're referring to. See
[Pages in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/pages-in-hana.md).

***

## Running several prompts at once [#running-several-prompts-at-once]

Send another prompt while the agent is working and it **starts a separate chat*&#x2A;
rather than waiting — the prompt box tells you so, reading &#x2A;"Describe another
change… (starts a parallel chat)"*.

That makes it practical to explore two directions side by side. Each chat keeps its
own history, and **Chat history** lets you switch between them.

***

## Editing images on the canvas [#editing-images-on-the-canvas]

Two image operations live on the object itself rather than in the panel. Select an
image and right-click:

* **Remove Background** — cuts the subject out, turning the image into a reusable
  asset for stickers, product shots or layered compositions.
* **Upscale Image** — raises resolution and sharpness, for high-density screens or
  print.

***

## Limitations [#limitations]

* **It's better at intent than at exact numbers.** For a precise pixel value, set it
  yourself in the inspector.
* **Judge the result, then refine.** The first pass gets you a structure worth
  editing, not usually a finished screen.
