# Spline MCP Server (/generate/spline-mcp-server)

> Control Spline 3D and Hana from ChatGPT, Claude, Cursor, Codex, and other AI tools using MCP.



The **Spline MCP Server** connects AI tools like **ChatGPT**, **Claude**, **Cursor**, **Codex**, and **Antigravity** directly to Spline. Using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), any MCP-compatible client can build and edit **Spline 3D scenes** and **Hana designs** for you — creating files, generating 3D models and images, writing layouts, and running edits — and what it builds is an editable Spline file, not code you have to maintain.

Using ChatGPT or Codex? Add the Spline plugin: [Spline in ChatGPT and Codex](https://docs.spline.design/generate/plugins/chatgpt.md) has everything you need. For every other tool, there are two ways to connect:

<Cards>
  <Card title="Hosted server" href="#hosted-server">
    Sign in with your Spline account and the agent works in Spline's cloud editor. Nothing to install — the quickest way to start in ChatGPT, Claude, Cursor and Codex.
  </Card>

  <Card title="Desktop app" href="#desktop-app">
    The server built into the Spline desktop app. The agent edits the files you have open, running locally on your machine.
  </Card>
</Cards>

<Callout>
  **Agent without MCP support?** It can still read these docs: [`llms.txt`](https://docs.spline.design/llms.txt) indexes every page, [`llms-full.txt`](https://docs.spline.design/llms-full.txt) has them all in one file, and adding `.md` to any page's URL returns it as Markdown, like `docs.spline.design/generate/spline-mcp-server.md` for this page.
</Callout>

***

## Hosted server [#hosted-server]

The hosted server lives at `https://mcp.spline.design/mcp`. Your AI tool connects to it over the internet and signs in with your Spline account; every call then runs in a Spline editor in the cloud, one per conversation. Nothing has to be open on your machine — the agent keeps building even with no Spline tab in sight.

```
You    ──►  AI tool          ──►  mcp.spline.design   ──►  a Spline editor in the cloud
prompt      (ChatGPT, Claude,     (sign in once)            (Spline 3D or Hana)
             Cursor, Codex, …)
```

### Connect your AI tool [#connect-your-ai-tool]

The address is the same in every client: `https://mcp.spline.design/mcp`. Pick yours:

<Tabs items="['ChatGPT', 'Codex', 'Claude Code', 'Cursor', 'Claude', 'VS Code', 'Other']">
  <Tab value="ChatGPT">
    Add the [Spline plugin from ChatGPT's plugin directory](https://chatgpt.com/plugins/spline). The Spline editor opens in a panel beside the chat. Setup, the panel and example prompts: [Spline in ChatGPT and Codex](https://docs.spline.design/generate/plugins/chatgpt.md).
  </Tab>

  <Tab value="Codex">
    Add the same [Spline plugin](https://chatgpt.com/plugins/spline) in Codex, or add only the server with `codex mcp add spline --url https://mcp.spline.design/mcp` and sign in with `codex mcp login spline`. More in [Spline in ChatGPT and Codex](https://docs.spline.design/generate/plugins/chatgpt.md#codex).
  </Tab>

  <Tab value="Claude Code">
    ```bash
    claude mcp add --transport http --scope user spline https://mcp.spline.design/mcp
    ```

    `--scope user` makes Spline available in every project; leave it out to add it to the current project only. Then run `/mcp` in Claude Code, select **spline** and choose **Authenticate** to sign in.
  </Tab>

  <Tab value="Cursor">
    Add the server to `~/.cursor/mcp.json` (every project) or `.cursor/mcp.json` (one project):

    ```json
    {
      "mcpServers": {
        "spline": {
          "url": "https://mcp.spline.design/mcp"
        }
      }
    }
    ```

    Then open **Cursor Settings → MCP**, find **spline** and sign in from there.
  </Tab>

  <Tab value="Claude">
    In Claude on desktop or the web, open **Settings → Connectors**, select **Add custom connector**, name it `Spline` and paste `https://mcp.spline.design/mcp` as the URL. Select **Connect** to sign in.
  </Tab>

  <Tab value="VS Code">
    Add the server to `.vscode/mcp.json` in your project:

    ```json
    {
      "servers": {
        "spline": {
          "type": "http",
          "url": "https://mcp.spline.design/mcp"
        }
      }
    }
    ```

    VS Code asks you to sign in the first time the server starts.
  </Tab>

  <Tab value="Other">
    Any MCP client that supports remote (streamable HTTP) servers with OAuth sign-in can use the hosted server. Add a remote server with the URL `https://mcp.spline.design/mcp`; if your client asks for a transport, choose streamable HTTP.
  </Tab>
</Tabs>

<Callout type="idea">
  Want the agent to reach for Spline on its own, and get the authoring right the first time? Add the [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill.md#install) next to the server. It's optional: the tools work without it.
</Callout>

### Sign in [#sign-in]

When you sign in, your AI tool opens a browser window where you log in to Spline and approve access. Some tools only do this the first time the agent calls a Spline tool. After that the agent works in your Spline account: the files it creates are saved there like any other, and it can open files you already have.

To disconnect, remove the server from your AI tool.

### Using it [#using-it]

Just ask for what you want — no file needs to be open first.

* *"Create a 3D scene with a rotating glass sphere on a pedestal and a soft studio light."*
* *"Design a clean pricing page with three tiers and a call-to-action."*

When the agent creates or opens a file, it gives you a **link to it in the Spline web editor** (in ChatGPT, the file opens in the Spline panel instead). Open it in your browser to watch the design come together live, and to keep editing it yourself — on the canvas or by asking the agent for changes. Follow-up requests in the same conversation keep working on the same file.

To bring the result into your codebase, the agent can export a Hana frame's current HTML + CSS — including edits you made by hand — and adapt it into your project. For a 3D scene, ask the agent to publish it: it updates the scene's public URL, Viewer embed or code export and hands you the live link to embed. More in [Working with your codebase](#working-with-your-codebase).

### What the agent can do [#what-the-agent-can-do]

The hosted server offers the same tools as the [desktop app](#desktop-app), except those that read files from your computer:

**In Spline 3D**

* Create and open 3D files, and build or edit scenes.
* Generate 3D models and images with Spline AI.
* Inspect the scene and objects, set the camera view, and capture screenshots to check its work.
* Write the code layer over the canvas — HUDs, interfaces and game logic.
* Publish the scene to its public URL, the Spline Viewer embed or a code export, and give you the link. The agent only publishes when you ask it to.

**In Hana**

* Create and open Hana files, and design or rebuild frames (web pages, app screens, UI).
* Add, move, duplicate, resize, recolor and update objects.
* Generate and edit images, review a frame, and export it to HTML + CSS.

To use your own images in Hana, add them to the file in the editor, or use the [desktop app](#desktop-app), whose agent can upload files from your machine. Every tool is listed by name in the [tool reference](#tool-reference).

### Usage limits [#usage-limits]

Each tool call the agent makes counts toward a **daily allowance set by your Spline plan**, with a short per-minute cap on every plan to stop runaway loops. Reading guides and checking your profile don't count, and a call that fails on Spline's side is given back. Ask the agent how many Spline calls you have left today: it can check your plan and today's count. When you hit a limit, the agent is told which one and when it resets — the daily allowance at midnight UTC, the per-minute cap within a minute — and where to upgrade. Upgrades apply on the next call.

### Privacy & security [#privacy--security]

* Sign-in uses **OAuth**: your AI tool never sees your Spline password, only a token that lets it call Spline's tools on your behalf. Removing the server from your tool stops it calling them.
* The agent's calls and their results travel between your AI tool and Spline's servers, and run in a Spline editor in the cloud. The files it works on are stored in your Spline account like any other.

### Troubleshooting [#troubleshooting]

<Accordions>
  <Accordion title="The Spline tools don't appear in my AI client">
    Check that the `spline` server is enabled in your tool's settings, then restart the tool or reload its window — most tools only load MCP servers at startup.
  </Accordion>

  <Accordion title="The agent says Spline isn't connected or signed in">
    Open your tool's MCP settings and sign in to the Spline server again — the browser window to approve access opens from there.
  </Accordion>

  <Accordion title="A call says the editor didn't finish loading or couldn't start">
    The cloud editor for your conversation is starting up. Ask the agent to retry in a moment; it should keep working in the same file rather than creating a new one.
  </Accordion>

  <Accordion title="A call says I reached my limit">
    You've used your plan's daily allowance, or made too many calls in a minute. The message says when it resets; upgrading your plan raises the daily allowance from the next call.
  </Accordion>
</Accordions>

***

## Desktop app [#desktop-app]

The desktop server connects your AI coding tool to the live editor tabs in the **Spline desktop app**, running entirely on your machine.

<Card title="Download the Spline desktop app" icon="download" href="https://spline.design/download">
  Required to use the desktop server. Available for macOS and Windows.
</Card>

<Callout type="warn">
  The desktop server ships **built into the Spline desktop app** and doesn't work from the browser. There's no separate package to install: downloading and opening the desktop app is all the setup it needs. To work without the app, use the [hosted server](#hosted-server).
</Callout>

### How it works [#how-it-works]

The desktop server bridges your AI coding tool and the live editor tabs in the Spline desktop app:

```
You    ──►  AI coding tool   ──►  Spline MCP Server      ──►  your open editor tab
prompt      (Claude, Cursor,      (bundled with the app)      (Spline 3D or Hana)
             Codex, …)
```

* You describe what you want to your AI tool (for example, &#x2A;"add a floating island scene"*).
* Your AI tool works out which Spline tools to call, and sends them as structured requests — a tool name plus arguments, not your prompt text.
* The Spline app routes each call to the right editor tab, creating a file for you if none of that kind is open.
* The tab runs the call against your live document and returns the result, and your AI tool keeps calling until the task is done.

Because the calls run inside the editor tab, your AI tool can reach the scene, the objects, materials, cameras, and Spline's AI generation features.

**One server, two surfaces.** The same connection drives both products. Requests are routed automatically by kind:

* **3D requests** (scenes, meshes, cameras, lighting) go to your Spline 3D tab.
* **2D / Hana requests** (websites, app screens, UI, layouts) go to your Hana tab.

<Callout>
  Everything runs **locally on your machine** over `127.0.0.1`. The desktop server never exposes your work to the internet — the only place your requests and results travel is between the Spline app and the AI client you connected.
</Callout>

### Requirements [#requirements]

* The [**Spline desktop app**](https://spline.design/download) (macOS or Windows) — **required**, since the desktop server is bundled inside it and can't run from the browser.
* An **MCP-compatible AI coding tool**:
  * **Claude Code**, **Claude Desktop**, **Cursor**, **VS Code**, **Antigravity** and **ChatGPT** — configured automatically.
  * **Windsurf** and other MCP-compatible clients — a quick one-time setup, see [Connecting other clients](#connecting-other-clients).

### Setup [#setup]

#### Automatic setup [#automatic-setup]

When you install and open the Spline desktop app, it registers the MCP server
with every supported client it finds installed. No config editing required.

| Client         | Where Spline writes the server                                    |
| -------------- | ----------------------------------------------------------------- |
| Claude Code    | `~/.claude.json`                                                  |
| Claude Desktop | `claude_desktop_config.json` (including the Windows MSIX install) |
| Cursor         | Cursor's MCP config                                               |
| VS Code        | VS Code and VS Code Insiders                                      |
| Antigravity    | Antigravity's MCP config (current and legacy paths)               |
| ChatGPT        | The `codex` CLI bundled in the ChatGPT desktop app (TOML config)  |

1. [**Download the Spline desktop app**](https://spline.design/download) (macOS or Windows) and open it at least once. &#x2A;This step is required — the desktop server lives inside the app.*
2. Restart your AI client so it picks up the new server. Most clients only load MCP servers at startup.
3. That's it — Spline's tools are now available to the agent.

You can manage this per client in Spline's **MCP settings**, which lists every
supported client with its own toggle plus a global switch, and shows the exact
setup steps for whichever one you expand.

To confirm the connection, the tools will appear in your client namespaced under `Spline` (for example, `mcp__Spline__3d_run_code` or `mcp__Spline__2d_write_html`).

#### Connecting other clients [#connecting-other-clients]

For an MCP-compatible tool Spline doesn't auto-configure — **Windsurf**, for
example — copy the generated server entry into that tool's MCP config. Spline's
MCP settings has an **Other agents** panel that gives you exactly this entry to
paste, with the paths already resolved for your install.

<Video src="https://cdn.spline.design/docs/videos/1786615154449-mcp-other-agents.mp4" />

You'll find the entry the app created under the `Spline` key in:

* **Claude Code** — `~/.claude.json`
* **Claude Desktop** —
  * macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  * Windows: `%APPDATA%\Claude\claude_desktop_config.json`

It looks like this (the exact paths are specific to your machine and install):

```jsonc
{
  "mcpServers": {
    "Spline": {
      "type": "stdio",
      "command": "/path/to/Spline.app/.../MacOS/Spline",
      "args": ["/path/to/spline-mcp.cjs"],
      "env": {
        "ELECTRON_RUN_AS_NODE": "1"
      }
    }
  }
}
```

Copy that `Spline` entry into the MCP configuration of the tool you want to use, then restart it. Most tools accept this same `command`/`args`/`env` shape; check your tool's MCP docs if its config format differs.

<Callout type="idea">
  Because the app keeps its own entries healthy across updates and moves, the simplest way to stay current is to let Spline manage the clients it supports and copy the entry from one of those whenever a path changes.
</Callout>

### Using it [#using-it-1]

1. Open the **Spline desktop app** and keep it running.
2. In your AI client, just ask for what you want. You don't have to open a file first — if no matching file is open, the agent creates a new one and opens it in a tab.

**Example prompts**

* *"Create a 3D scene with a rotating glass sphere on a pedestal and a soft studio light."*
* *"In Hana, design a clean pricing page with three tiers and a call-to-action."*
* *"Generate a 3D model of a low-poly tree and add it to my scene."*
* *"Take the dashboard screen from `src/app/dashboard/page.tsx` and rebuild it in Hana so I can redesign it."*
* *"I refined the layout in Hana — export it and update the matching component in my repo."*

The agent picks the right surface automatically: design requests go to Hana, 3D requests go to Spline 3D. If you have both open, calls are routed to the most recently focused tab of the matching kind.

<Callout type="idea">
  Want the agent to *choose* Spline on its own — and get the authoring contract
  right first time? Install the [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill.md).
  It's optional, and the MCP server works without it.
</Callout>

As the agent works, the frame or scene it's editing lights up so you can follow along in real time. You can connect several sessions at once — they all route to the same running editor.

#### What the agent can do [#what-the-agent-can-do-1]

Once connected, the agent can, among other things:

**In Spline 3D**

* Create new 3D files and build or edit scenes.
* Generate 3D models and images with Spline AI.
* Inspect the scene and objects, run scene edits, set the camera view, and capture screenshots.
* Write the code layer over the canvas — HUDs, interfaces and game logic. See the **Preview / Edit / Code** tabs and [AI Agent](https://docs.spline.design/spline-ai/ai-agent.md).
* Publish the scene to its public URL, the Spline Viewer embed or a code export when you ask, and give you the live link.

**In Hana**

* Create new Hana files and design or rebuild frames (web pages, app screens, UI).
* Add, move, duplicate, resize, recolor, and update objects.
* Generate and edit images, upload images and other assets from your machine, work with 3D shapes, apply effects, and export designs.

Every tool is listed by name in the [tool reference](#tool-reference).

### MCP settings [#mcp-settings]

Open **Settings → MCP** in the Spline app. Every supported client gets its own
row with a toggle, so you can connect Claude Code but leave Cursor alone.
Expand a row to see the setup steps for that specific client.

<Video src="https://cdn.spline.design/docs/videos/1786615154449-mcp-settings.mp4" />

Turning a client **off** removes Spline's entry from that client's config and
stops it being re-added; turning it back **on** re-registers it. Agents only
load their MCP servers at startup, so Spline reminds you to restart the one you
just switched on.

<Video src="https://cdn.spline.design/docs/videos/1786615154449-mcp-toggle-agent.mp4" />

If you delete the `Spline` entry from a config by hand, Spline treats that as a
deliberate opt-out and won't put it back.

#### Connection status [#connection-status]

Each row shows whether that client is currently talking to Spline:

| What you see      | What it means                                                                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connected**     | The client has a live session with Spline right now                                                                                         |
| **Starts on use** | Registered and working, but this client only launches the connection when you actually use it — expect this for **VS Code** and **ChatGPT** |
| No label          | Registered and idle                                                                                                                         |

**"Starts on use" is not a problem.** VS Code and ChatGPT don't start the
connection when they open, so send a message in the client and it connects.

There's also an MCP status indicator in the app's sidebar — click it to jump
straight to these settings.

### Privacy & security [#privacy--security-1]

* The server binds to &#x2A;*`127.0.0.1`** only — it is never reachable from the network.
* Connections are gated by an **origin allowlist**, so arbitrary web pages can't reach it. There are no tokens to manage.
* Your scenes and prompts stay between the Spline app and the AI client you connected. (Spline AI generation features used by the agent run in the cloud, the same as when you use them in the editor.)

### Troubleshooting [#troubleshooting-1]

<Accordions>
  <Accordion title="The Spline tools don't appear in my AI client">
    Make sure the **Spline desktop app is installed and has been opened at least once**, then fully restart your AI client so it reloads its MCP servers. Confirm a `Spline` entry exists in your client's config (see [Connecting other clients](#connecting-other-clients) for the file locations).
  </Accordion>

  <Accordion title="A tool call fails or times out">
    Keep the Spline desktop app running while you work. Forwarded calls time out after about 60 seconds, so very long operations may need to be retried. Only one editor connection is active at a time — the most recent connection wins.
  </Accordion>

  <Accordion title="A client shows &#x22;Starts on use&#x22; instead of Connected">
    That's expected for **VS Code** and **ChatGPT** — they only open the connection when you actually use them, rather than at startup. Send a message in that client and it will connect.
  </Accordion>

  <Accordion title="My client reports a failed-to-start server after I uninstalled Spline">
    Deleting the app can leave its config entry behind. Turn that client **off** in **Settings → MCP** *before* uninstalling, or remove the `mcpServers.Spline` entry from its config by hand. Reinstalling Spline fixes the entry automatically.
  </Accordion>
</Accordions>

***

## Working with your codebase [#working-with-your-codebase]

Because your AI coding tool is already working inside your repository, Spline can sit right in your design-to-code loop instead of being a separate silo. This works the same with the hosted server and the desktop app.

### Spline 3D [#spline-3d]

* **Put a scene in your app.** Ask the agent to publish the scene and it hands back the public URL, the Spline Viewer embed, or a code export for React, Next.js, Vanilla JS, three.js or react-three-fiber, then wires it into your project. Publishing again updates the same link, so your app picks up scene changes without a code change.
* **Bring UI and logic into the scene.** Every scene has a code layer: a full HTML, CSS and JS document over the canvas, for HUDs, forms, interfaces and game logic. The agent can write it from code in your repo, edit it in place, and read it back out to keep your source in step.
* **Build from your project's content.** Point the agent at what's already in your repo — brand colors, copy, a product list — and it builds or updates the scene to match.

### Hana [#hana]

* **Bring a screen into Hana.** Point the agent at a page or component in your repo, and it rebuilds that screen as a live Hana frame — it translates the markup into Hana's supported HTML + CSS (flexbox) subset. From there you can redesign it visually on the canvas.
* **Build screens in Hana, in code.** You can also have the agent author a frame directly from HTML + CSS, so a screen you describe in code shows up as an editable Hana design.
* **Push your canvas edits back to code.** After you tweak the design in Hana, the agent exports the frame's *current* state back to HTML + CSS and translates those changes into your framework — Next.js, Vue, plain HTML, and so on. Every exported element keeps a stable reference back to its Hana object, so the agent can map a visual change to the right place in your source.

<Callout>
  The Hana round-trip works within Hana's supported HTML + CSS subset. Complex or framework-specific markup may need the agent to reconcile the exported HTML against your existing components rather than replacing them wholesale.
</Callout>

***

## Tool reference [#tool-reference]

Every tool the agent can call, by name, with the server that offers it. Your AI client shows the same names, so this is the list to check against when a tool seems missing. Names and tools change as Spline adds features.

{/* mcp-tools:start — generated by `npm run docs-tools --workspace=@splinetool/mcp-remote`, do not edit */}

**Files and account**

| Tool                 | What it does                                                        | Hosted | Desktop |
| -------------------- | ------------------------------------------------------------------- | :----: | :-----: |
| `spline_canvas`      | Show your Spline files (in ChatGPT, in the Spline panel).           |    ✓   |         |
| `spline_create_file` | Create a 3D or Hana file in your account and get a link to it.      |    ✓   |         |
| `spline_open_file`   | Open one of your files for the agent to work on.                    |    ✓   |         |
| `spline_profile`     | Your account, plan, and today's tool calls against the daily limit. |    ✓   |         |

**Spline 3D**

| Tool                   | What it does                                                                                     | Hosted | Desktop |
| ---------------------- | ------------------------------------------------------------------------------------------------ | :----: | :-----: |
| `3d_analyze_scene`     | Run the performance analysis behind the Performance panel.                                       |    ✓   |    ✓    |
| `3d_create_file`       | Create and open a 3D file in the desktop app.                                                    |        |    ✓    |
| `3d_edit_html_content` | Make targeted edits to the code layer.                                                           |    ✓   |    ✓    |
| `3d_generate_3d_model` | Start generating a 3D model with Spline AI.                                                      |    ✓   |    ✓    |
| `3d_generate_image`    | Start generating an image with Spline AI.                                                        |    ✓   |    ✓    |
| `3d_get_generation`    | Check on a generation and get the image or model.                                                |    ✓   |    ✓    |
| `3d_get_html_content`  | Read the code layer.                                                                             |    ✓   |    ✓    |
| `3d_get_objects`       | Read the full detail of specific objects.                                                        |    ✓   |    ✓    |
| `3d_get_scene`         | Read a compact summary of every object in the scene.                                             |    ✓   |    ✓    |
| `3d_get_scene_mcp`     | Read the scene and a free spot to build in: the usual first call.                                |    ✓   |    ✓    |
| `3d_list_versions`     | List the file's saved versions, to find one to go back to.                                       |    ✓   |    ✓    |
| `3d_load_skill`        | Load one of Spline's 3D authoring guides.                                                        |    ✓   |    ✓    |
| `3d_publish_export`    | Publish the scene to its public URL, Viewer embed or code export. Only when you ask.             |    ✓   |    ✓    |
| `3d_restore_version`   | Roll the file back to a saved version, keeping the current state in the history. Paid plans.     |    ✓   |    ✓    |
| `3d_run_code`          | Build, edit or animate anything in the scene: objects, materials, lights, cameras, interactions. |    ✓   |    ✓    |
| `3d_set_html_content`  | Set the code layer over the canvas: HTML, CSS and JS for HUDs, interfaces and game logic.        |    ✓   |    ✓    |
| `3d_set_view`          | Aim the agent's own screenshot camera.                                                           |    ✓   |    ✓    |
| `3d_take_screenshot`   | Capture an image from the agent's camera, without moving your view.                              |    ✓   |    ✓    |

**Hana**

| Tool                   | What it does                                                                                 | Hosted | Desktop |
| ---------------------- | -------------------------------------------------------------------------------------------- | :----: | :-----: |
| `2d_add_objects`       | Add objects inside a frame.                                                                  |    ✓   |    ✓    |
| `2d_create_file`       | Create and open a Hana file in the desktop app.                                              |        |    ✓    |
| `2d_delete_objects`    | Delete objects.                                                                              |    ✓   |    ✓    |
| `2d_duplicate_objects` | Duplicate objects, with an offset.                                                           |    ✓   |    ✓    |
| `2d_edit_image`        | Edit an image with AI: remove its background or describe a change.                           |    ✓   |    ✓    |
| `2d_export_html`       | Export a frame's current design, hand edits included, as HTML and CSS.                       |    ✓   |    ✓    |
| `2d_find_space`        | Find free space on the canvas for a new frame.                                               |    ✓   |    ✓    |
| `2d_generate_images`   | Start generating images with AI, ready for the frame that uses them.                         |    ✓   |    ✓    |
| `2d_get_canvas_state`  | Read the current selection and a free spot on the canvas.                                    |    ✓   |    ✓    |
| `2d_get_object`        | Read the full properties of one object.                                                      |    ✓   |    ✓    |
| `2d_get_scene`         | Read an overview of the scene tree.                                                          |    ✓   |    ✓    |
| `2d_list_versions`     | List the file's saved versions, to find one to go back to.                                   |    ✓   |    ✓    |
| `2d_load_skill`        | Load one of Spline's Hana authoring guides.                                                  |    ✓   |    ✓    |
| `2d_move_objects`      | Reparent objects or change their stacking order.                                             |    ✓   |    ✓    |
| `2d_recolor`           | Swap colors across a design by value, to retheme it.                                         |    ✓   |    ✓    |
| `2d_reserve_frames`    | Place empty frames for the screens about to be designed.                                     |    ✓   |    ✓    |
| `2d_resize_frame`      | Resize a frame to the page size being designed.                                              |    ✓   |    ✓    |
| `2d_restore_version`   | Roll the file back to a saved version, keeping the current state in the history. Paid plans. |    ✓   |    ✓    |
| `2d_review_frame`      | Screenshot a frame with a map of its objects, to check the design.                           |    ✓   |    ✓    |
| `2d_update_objects`    | Change properties on one or more objects.                                                    |    ✓   |    ✓    |
| `2d_update_scene`      | Change scene settings, like the canvas background.                                           |    ✓   |    ✓    |
| `2d_upload_assets`     | Upload images from your computer into the file.                                              |        |    ✓    |
| `2d_write_html`        | Design or rebuild a frame from HTML and CSS.                                                 |    ✓   |    ✓    |

{/* mcp-tools:end */}
