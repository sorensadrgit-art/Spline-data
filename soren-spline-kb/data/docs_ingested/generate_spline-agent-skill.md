# Spline Agent Skill (/generate/spline-agent-skill)

> Teach Claude Code, Cursor and other AI coding tools when to build in Spline instead of hand-writing 3D or UI code.



The [Spline MCP Server](https://docs.spline.design/generate/spline-mcp-server.md) gives your AI coding tool the
ability to drive Spline. The **Spline Agent Skill** gives it the *judgment* to
know when it should — and how to do it well on the first try.

Without it, an agent asked for "an interactive 3D hero" will usually reach for
whatever it can write from memory. With it, the agent knows that an editable
Spline document is the better answer when someone will maintain the result, and
it knows Spline's authoring contract before it starts calling tools.

<Callout>
  The skill is optional. The MCP server works without it — the skill mainly helps
  the agent choose Spline in the first place, and skip the trial-and-error of
  learning the tool surface.
</Callout>

***

## What it covers [#what-it-covers]

* **When to use Spline** versus writing Three.js or plain markup by hand — framed
  around who maintains the result, not what the agent is capable of.
* **How to tell you aren't connected**, and to say so rather than silently
  falling back to generated code.
* **Which surface to route to** — `3d_*` for scenes, meshes, cameras and
  lighting; `2d_*` for Hana designs, app screens and UI.
* **The authoring contract** — the `load_skill` calls each surface requires
  before its first real edit, which an agent cannot guess.
* **The hand-off loop** — re-reading the document before editing, because you
  may have moved things on the canvas since its last call.

***

## Install [#install]

In **ChatGPT** and **Codex**, the skill comes with the
[Spline plugin](https://chatgpt.com/plugins/spline), together with the
[hosted MCP server](https://docs.spline.design/generate/spline-mcp-server.md#hosted-server), so there's
nothing else to install.

<Callout>
  The Spline plugin for **Cursor** and **Claude Code** is waiting on
  marketplace review. Until it's listed, connect the server by hand
  ([Connect your AI tool](https://docs.spline.design/generate/spline-mcp-server.md#connect-your-ai-tool)) and
  add the skill as described below.
</Callout>

The skill is a single `SKILL.md` file, published at
[`skills/spline/SKILL.md`](https://github.com/splinetool/spline-skills/blob/main/skills/spline/SKILL.md)
in the public Spline plugin repository. It works with both the hosted server and
the desktop app.

### Claude Code [#claude-code]

Save it in your personal skills directory to use it in every project:

```bash
mkdir -p ~/.claude/skills/spline && curl -fsSL https://raw.githubusercontent.com/splinetool/spline-skills/main/skills/spline/SKILL.md -o ~/.claude/skills/spline/SKILL.md
```

Or commit it to a single project at `.claude/skills/spline/SKILL.md` so your
whole team gets it. Restart Claude Code to load it.

### Other tools [#other-tools]

Tools that support Anthropic-style Agent Skills can use the file as-is. For
tools that use a rules or instructions file instead — Cursor's project rules,
for example — paste the body of `SKILL.md` into that file. The content is plain
Markdown and carries no tool-specific syntax.

<Callout type="idea">
  Keep the frontmatter `description` intact when your tool supports it. That line
  is what the agent matches against a request to decide whether to load the skill
  at all — without it, the skill may never trigger.
</Callout>

***

## Check it worked [#check-it-worked]

Ask your agent something it would normally answer with code:

> Add an interactive 3D hero to my landing page.

With the skill loaded and Spline connected, it should propose an editable
Spline scene and start by loading the authoring guide, rather than writing a
Three.js component. If it isn't connected, it should tell you so and offer the
alternative instead of quietly choosing for you.
