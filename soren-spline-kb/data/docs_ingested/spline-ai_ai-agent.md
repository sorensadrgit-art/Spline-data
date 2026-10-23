# AI Agent (/spline-ai/ai-agent)

> Build and edit 3D scenes by describing what you want. The agent works the editor the same way you do — with real, undoable edits.



The **AI Agent** builds and edits 3D scenes for you. Describe what you want and it
does the work through the editor itself — creating objects, setting up materials
and lighting, animating, wiring interactivity — using the same commands you'd
use by hand.

That last part matters: every edit the agent makes is a **normal editor edit**.
It lands in your undo history, it syncs to anyone collaborating in the file, and
you can take over at any point.

<Callout type="tip">
  Designing in Hana instead? It has its own assistant — see
  [AI Agent in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/ai-in-hana.md).
</Callout>

<Callout>
  The agent runs on your workspace's monthly **AI credits**, included with every
  paid plan. See [AI credits](https://docs.spline.design/account/pricing.md#ai-credits).
</Callout>

***

## Where to find it [#where-to-find-it]

Open the **Agent** tab at the top of the left sidebar — the first of the three
tabs, next to **Objects** and **Assets**. It's the tab the editor opens on, so
it's usually already there.

Type what you want in the prompt box at the bottom of the panel and press Enter.

### The panel, top to bottom [#the-panel-top-to-bottom]

| Where                | What it is                                                                                                              |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Sidebar tab row      | **Agent**, plus **New chat** and **Chat history** buttons on the right                                                  |
| Middle of the panel  | The conversation                                                                                                        |
| Above the prompt box | Queued prompts, your selection chips, and any attachments                                                               |
| The prompt box       | Type here. `/` opens the command menu                                                                                   |
| Bottom row           | **+** to attach, the **model** and **effort** pickers, and **Send** — which becomes **Stop** while the agent is working |

***

## Writing a good prompt [#writing-a-good-prompt]

The agent reads your scene before it acts, so you can talk about what's already
there rather than describing everything from scratch.

* **Say what you want, not how to build it.** "A cabin on a rocky island at
  sunset" gets further than a list of primitives and coordinates.
* **Select first, then refer to the selection.** Whatever you have selected when
  you hit send becomes the meaning of "this", "it" and "these", and it scopes an
  edit that doesn't name a target. The objects you selected appear as chips above
  the prompt so you can see exactly what the agent will act on.
* **Iterate.** "Make the roof steeper", "add fog", "warmer light" — follow-ups
  are usually faster and more predictable than one enormous prompt.
* **Ask it to fix what you can see.** It looks at the result, so "the door is
  floating, put it on the ground" works.

### Attaching images and files [#attaching-images-and-files]

The &#x2A;*+** button at the bottom-left of the prompt box attaches an **image**,
**media** or a **document** — useful for reference art, a style you want matched,
or a model to work from. Attachments appear above the prompt box before you send;
click one to view it full size, or use the ✕ to remove it.

### Selection chips [#selection-chips]

Select objects in the viewport or the **Objects** tab before you send, and they
appear as chips just above the prompt box. The chips name the first object and
count the rest (`+3 more`) — hover either part for the full list.

They stay on the message after it's sent, so scrolling back through a conversation
still shows what "make these blue" was pointing at, even if those objects were
later renamed or deleted.

***

## What the agent can do [#what-the-agent-can-do]

Beyond building and editing the scene, you can ask it to:

* **Check and fix its own work** — "the door is floating, put it on the ground"
  works, because it can see the result.
* **Generate images** — textures, reference art, or image content for the scene.
* **Generate 3D models** — from text or an image, inserted straight into the
  scene. See [AI 3D Generation](https://docs.spline.design/generate/ai-3d-generation.md).
* **Speed up a slow scene** — ask it to optimise, or send it a fix from the
  Performance panel. See
  [How to optimize your scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md).
* **Write code over the canvas** — HUDs, interfaces and game logic that drive the
  3D scene, in the **Preview / Edit / Code** tabs at the top of the editor.

### Slash commands [#slash-commands]

Type `/` in the prompt box to pin a request to one job instead of leaving the
choice to the agent:

| Command  | What it does                                    |
| -------- | ----------------------------------------------- |
| `/image` | Generate an AI image from the text that follows |
| `/3d`    | Generate a 3D model from the text that follows  |

***

## Models and effort [#models-and-effort]

Both pickers sit on the bottom row of the panel, to the right of the &#x2A;*+** button.

The first sets which model handles your request. Tiers run
from **Fast** — quickest, least detail — up to **Ultra Max** and **Astra**, the
highest quality and the most expensive. Each option shows what it's good for, so
you can pick against the job rather than memorising the list.

The second, **effort**, sets how much the model thinks before acting, from
**Minimal** through **Max**. Higher effort helps with scenes that have a lot of
moving parts — interactivity, physics, precise layout — and mostly just costs time
on simple ones. Not every model offers every level; the control shows the ones
available for what you've picked.

Higher is not automatically better. For small edits, a quicker tier at moderate
effort usually gets you there sooner and spends fewer credits.

***

## Working while the agent works [#working-while-the-agent-works]

**You don't have to wait.** Press Enter while the agent is working and your prompt
joins a queue. Queued prompts appear as a numbered stack just above the prompt box,
under a **QUEUED** header — the numbers are the order they'll run in.

* **Pause**, in that header, holds the queue so you can see how the first change
  lands before committing to the rest. **Clear**, next to it, empties it.
* **✕** on any row drops just that prompt.
* **Stop** — the button that replaces Send while the agent works — interrupts the
  current run *and* clears the queue. Stopping means stopping, not carrying on
  with whatever was lined up behind it.
* If something fails, the queue stays put and visible instead of running on.

Each queued prompt keeps the text, attachments and selection you had when you
typed it, and stays with its conversation even if you move to another file.

### The viewport follows along [#the-viewport-follows-along]

Your camera moves to keep the work in frame while the agent builds, and settles on
a view of what it made when it finishes.

**Orbiting, panning or zooming stops that.** If you take the camera, you keep it.

***

## Conversations [#conversations]

Chats are saved to your account and kept per file. The two buttons at the
right-hand end of the sidebar's tab row manage them:

* **New chat** starts a fresh conversation in the current file.
* **Chat history** lists your previous conversations in this file — click one to
  switch to it, or use the ✕ on a row to delete it.

Reopening a file drops you back into the conversation you were last in. To copy a
reply out, hover the message and use the copy button.

***

## Credits [#credits]

The agent spends your workspace's monthly **AI credits**. A banner appears above
the prompt box once you've used more than 90% of your monthly allowance, showing
the percentage used; clicking it opens the upgrade options.

See [AI credits](https://docs.spline.design/account/pricing.md#ai-credits) for what each plan includes and how
to add more.

***

## Limitations [#limitations]

* The agent works on **one file at a time**, and on one change at a time — which
  is why extra prompts queue rather than running together.
* It is much better at **intent** than at exact numeric layout. If something needs
  to sit at a precise coordinate, it's usually quicker to place it yourself.
* Complex requests can apply only partly. When that happens the step is marked
  with an amber warning and the agent corrects the rest on its next attempt —
  that's normal, not a failure.
* It won't change a scene while you're in **Play mode**, and it won't repoint a
  camera you've deliberately framed yourself.
