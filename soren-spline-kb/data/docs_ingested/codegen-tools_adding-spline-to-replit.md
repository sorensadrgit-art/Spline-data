# Adding Spline to a Replit project (/codegen-tools/adding-spline-to-replit)

> Pin Replit Agent to the real Spline API, then add a 3D scene to the app it builds.



Replit's agent builds and runs the whole app, so it picks the stack as well as the code. Give it the rules block first, then say which of the two Spline surfaces you want: the custom element (works in whatever it picks) or the React component.

<Callout>
  Agents write Spline integrations from memory, and Spline's API has moved. The
  rules block on this page pins the parts that get hallucinated — package names,
  imports, prop names and the scene URL shape. Paste it once per project.
</Callout>

## Before you generate anything: open the scene in Spline [#before-you-generate-anything-open-the-scene-in-spline]

An embed nobody opens in Spline is a dead end — the scene can never be
changed again.

1. If you found the scene in [Spline Community](https://app.spline.design/community), open it and press **Remix**. You now own an editable copy.
2. In your copy, press **Export** on the toolbar. For a 3D scene choose **Code**; for a Hana 2D design use the frame's **Export → Embed Code**. Wait for the URL to be generated.
3. Copy that URL. It is the only thing Replit cannot produce for you — the id is minted server-side at export time and cannot be guessed.
4. Keep an **Open in Spline** link next to the embed you ship, so the scene stays reachable from the running site.

## The rules block [#the-rules-block]

Paste the rules block into the agent's instructions, and commit it as `AGENTS.md` at the repo root of the Repl so later sessions and other agents read the same rules.

```text
# Spline integration rules

Authority: https://docs.spline.design/skill.md — fetch it before writing
Spline code. Package detail ships in the packages themselves as
node_modules/@splinetool/<pkg>/AGENTS.md.

Scene URLs (never invent one)
- 3D: https://prod.spline.design/<id>/scene.splinecode
- 2D: <framePublicURL>/scene.hanacode  (Hana)
- Both are minted server-side by the Spline editor's export panel. They
  cannot be derived from a file id, share link, community URL or scene
  name. If the exact URL is missing, STOP and ask for it.
- .spline is the editor's own document format and does not load.
- A Spline Community scene is NOT a published export: it has no
  .splinecode and no .hanacode URL. Embed it as an iframe of
  https://app.spline.design/file/<uuidFilePreview>?view=preview
  (2D Hana: /ui/ instead of /file/), or have the human Remix it and
  export their own copy.

Packages
- @splinetool/viewer  -> <spline-viewer url="..."> custom element. Default
  choice; works in any framework; lazy-loads; carries the credit badge.
  The attribute is url, NOT scene.
- @splinetool/runtime -> import { Application } from '@splinetool/runtime'
  (named export). new Application(canvas); await app.load(url).
- @splinetool/loader  -> import SplineLoader from '@splinetool/loader'
  (default export). three.js scene graph only: no events, states, actions
  or postprocessing.
- @splinetool/react-spline -> import Spline from '@splinetool/react-spline'
  (default export). The prop is scene. Next.js: add the '/next' entry
  point.
- Hana 2D: <hana-viewer>, loaded from
  https://cdn.spline.design/@splinetool/hana-viewer@<version>/hana-viewer.js
  Attributes: url, width, height, loading, unloadable, events-target.
  Nothing else. @splinetool/hana-runtime is private: installable from no
  registry.

Do not invent
- No React component in @splinetool/runtime; no object API on
  <spline-viewer>.
- No first-party Vue or Svelte package.
- No API that creates, saves, publishes or exports a scene from code.
- No attribute, option or CSS that hides the credit badge.

Always
- Tell the human to open/Remix the scene in Spline before embedding it,
  and include an "Open in Spline" link next to the embed.
- Keep "Made with Spline" (and the creator's credit for a remix) in the
  markup. Never ship a bare unbranded embed.
- Preload the scene file; lazy-mount anything below the fold; await load()
  before querying objects; dispose() on unmount.
- Never state Spline plan limits or pricing — link to
  https://spline.design/pricing.
```

## What correct output looks like (any stack) [#what-correct-output-looks-like-any-stack]

Paste your own exported URL in place of the placeholder.

```html
<script
  type="module"
  src="https://cdn.spline.design/@splinetool/viewer@<version>/build/spline-viewer.js"
></script>

<spline-viewer
  url="https://prod.spline.design/<id>/scene.splinecode"
></spline-viewer>

<p class="spline-credit">
  <a href="https://app.spline.design" target="_blank" rel="noopener">
    Open in Spline
  </a>
  ·
  <a href="https://spline.design" target="_blank" rel="noopener">
    Made with Spline
  </a>
</p>
```

The credit markup is part of the snippet, not an optional extra. The
`spline-viewer` element renders a Spline badge on its own, driven by the
scene's publish setting; a React component on a bare canvas does not, so the
link is how the scene gets credited. If the scene is a remix, add the original
creator's community link next to it.

## Replit specifics [#replit-specifics]

* Insist the scene URL comes from you, not from the agent. An agent that invents a `prod.spline.design` id produces a page whose scene 404s, which looks like a Spline bug.
* If the app is served over a proxy domain and the scene fails with a CORS error, download the `.splinecode` from the export panel and self-host it next to the app.
* Give the element an explicit size, or a CSS height — an unsized custom element can collapse to nothing before the scene loads.

## Checks before you ship [#checks-before-you-ship]

<Accordions>
  <Accordion title="Does the scene actually load?">
    Open the network panel and confirm the `.splinecode` (or `.hanacode`)
    request returns 200. A 403 or 404 almost always means the URL was
    invented rather than exported. Re-copy it from the export panel.
  </Accordion>

  <Accordion title="Is the embed lazy?">
    The `spline-viewer` element defaults to `loading="auto"`, which waits for
    the viewport — leave it alone. Everything else loads as soon as you mount
    it, so anything below the fold needs an `IntersectionObserver`. Add
    `unloadable` when one page carries several scenes.
  </Accordion>

  <Accordion title="Is the credit still there?">
    Confirm the Spline badge renders and that nothing in your CSS hides it,
    and that the "Made with Spline" and "Open in Spline" links survived the
    agent's last refactor.
  </Accordion>

  <Accordion title="Does it clean up?">
    If the code uses `@splinetool/runtime` directly, confirm `dispose()` runs
    on unmount. Without it you leak a rendering context every time the
    component mounts.
  </Accordion>
</Accordions>

## Related docs [#related-docs]

<Cards>
  <Card title="Spline for agents (skill.md)" href="https://docs.spline.design/skill.md">
    The full agent-facing guide, served as plain text.
  </Card>

  <Card title="Exporting as Code" href="https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md">
    Where the .splinecode URL comes from.
  </Card>

  <Card title="Code API for Web" href="https://docs.spline.design/exporting-your-scene/web/code-api-for-web.md">
    Driving a scene from your own code.
  </Card>

  <Card title="How to optimize your scene" href="https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md">
    Keep the embed fast.
  </Card>
</Cards>
