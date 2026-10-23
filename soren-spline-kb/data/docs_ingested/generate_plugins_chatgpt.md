# ChatGPT and Codex (/generate/plugins/chatgpt)

> Add the Spline plugin to ChatGPT or Codex and build 3D scenes and designs in a Spline editor that opens right in the chat.



The **Spline plugin** lets ChatGPT and Codex build in Spline for you. Ask for a 3D scene, a website or an app screen, and it gets built in a real, editable Spline file. In ChatGPT, the Spline editor opens in a panel beside the chat, so you can watch it come together and keep editing it yourself.

<Card title="Add Spline to ChatGPT" href="https://chatgpt.com/plugins/spline">
  The Spline plugin in ChatGPT's plugin directory. The same plugin works in Codex.
</Card>

The plugin connects ChatGPT to Spline's [hosted MCP server](https://docs.spline.design/generate/spline-mcp-server.md#hosted-server) and includes the [Spline Agent Skill](https://docs.spline.design/generate/spline-agent-skill.md), so ChatGPT knows when to reach for Spline and how to use it well. There's nothing to install, and no API key: you sign in with your Spline account.

***

## Add the plugin [#add-the-plugin]

### ChatGPT [#chatgpt]

1. Open the [Spline plugin in ChatGPT's plugin directory](https://chatgpt.com/plugins/spline) and add it.
2. Ask for something to build. The first time, ChatGPT asks you to **Connect** Spline: sign in with your Spline account and allow access.

To connect the server by hand instead of adding the plugin, open &#x2A;*[Plugins](https://chatgpt.com/plugins)** in ChatGPT, choose **Add → Add MCP Server**, enter the URL `https://mcp.spline.design/mcp`, and sign in.

### Codex [#codex]

Add the same [Spline plugin](https://chatgpt.com/plugins/spline) in Codex. To add only the server from the Codex CLI:

```bash
codex mcp add spline --url https://mcp.spline.design/mcp
```

Then sign in:

```bash
codex mcp login spline
```

***

## The Spline panel [#the-spline-panel]

When ChatGPT creates or opens a file, the Spline editor opens in a panel next to the conversation. It's the real editor, signed in as you:

* **Watch it build.** The scene or design updates live as ChatGPT works on it.
* **Edit it yourself.** Move things on the canvas, change materials, tweak the layout. ChatGPT re-reads the file before its next change, so it builds on your edits rather than undoing them.
* **Switch files.** Open another of your files in the panel and ChatGPT works on that one from your next message.
* **Come back to it.** The file is saved to your Spline account like any other. Reopen the panel from the conversation, or open the file in the Spline app.

The panel also works in the ChatGPT desktop app. In the Codex app the file opens in the same panel when it can show one; in the Codex CLI you get a link to the file in the Spline web editor instead.

***

## What to ask for [#what-to-ask-for]

Start with something like:

* *"Create an interactive 3D music player."*
* *"Build a 3D cooking game."*
* *"Make a 3D chair configurator."*
* *"Design a landing page for a coffee brand, with a hero, three features and a signup form."*

Then keep going in the same conversation: follow-up requests edit the same file instead of starting a new one.

* *"Make the background warmer and add a soft shadow under the chair."*
* *"Publish it and give me the link."*

ChatGPT can build and edit **3D scenes** (objects, materials, lighting, cameras, animation and interactions) and **Hana designs** (websites, app screens and UI). It can generate 3D models and images with Spline AI, check its work with screenshots, and publish a scene to its public URL when you ask. The full list is in the [tool reference](https://docs.spline.design/generate/spline-mcp-server.md#tool-reference).

***

## Usage limits [#usage-limits]

Each Spline action ChatGPT takes counts toward a daily allowance set by your Spline plan, the same as with any AI tool connected to Spline. Ask ChatGPT how many Spline calls you have left today. See [Usage limits](https://docs.spline.design/generate/spline-mcp-server.md#usage-limits) for the details.

## Privacy [#privacy]

Sign-in uses OAuth: ChatGPT never sees your Spline password. The files ChatGPT creates are saved in your Spline account like any other. To disconnect, remove Spline from &#x2A;*[Plugins](https://chatgpt.com/plugins)** in ChatGPT. More in [Privacy & security](https://docs.spline.design/generate/spline-mcp-server.md#privacy--security).

***

## Troubleshooting [#troubleshooting]

<Accordions>
  <Accordion title="ChatGPT doesn't use Spline">
    Mention Spline in your request ("in Spline, make…"), and check that the Spline plugin is turned on in ChatGPT.
  </Accordion>

  <Accordion title="ChatGPT says Spline isn't connected or my sign-in expired">
    Connect again when ChatGPT asks, or reconnect Spline from &#x2A;*[Plugins](https://chatgpt.com/plugins)** in ChatGPT, then retry.
  </Accordion>

  <Accordion title="The panel is blank or the editor didn't finish loading">
    The editor for your conversation is starting up. Ask ChatGPT to try again in a moment; it keeps working in the same file rather than creating a new one.
  </Accordion>

  <Accordion title="ChatGPT says I reached my limit">
    You've used your plan's daily allowance, or made too many calls in a minute. The message says when it resets; upgrading your Spline plan raises the daily allowance from the next call.
  </Accordion>
</Accordions>
