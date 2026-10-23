# Adding Spline to a Cursor project (/codegen-tools/adding-spline-to-cursor)

> Pin Cursor to the real Spline API, then add a 3D scene to your codebase.



Cursor edits your real repository, so the rules belong in the repository — that way every future session, and every other agent that opens the project, starts from the same API surface instead of from memory.

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
3. Copy that URL. It is the only thing Cursor cannot produce for you — the id is minted server-side at export time and cannot be guessed.
4. Keep an **Open in Spline** link next to the embed you ship, so the scene stays reachable from the running site.

## The rules block [#the-rules-block]

Commit the rules block as `AGENTS.md` at the repo root. If your setup also uses a Cursor-specific rules file, put the same content there.

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

## What correct output looks like (React) [#what-correct-output-looks-like-react]

Paste your own exported URL in place of the placeholder.

```jsx
import Spline from '@splinetool/react-spline';

export default function Hero() {
	return (
		<div className="spline-embed">
			<Spline scene="https://prod.spline.design/<id>/scene.splinecode" />
			<p className="spline-credit">
				<a href="https://app.spline.design" target="_blank" rel="noopener">
					Open in Spline
				</a>{' '}
				·{' '}
				<a href="https://spline.design" target="_blank" rel="noopener">
					Made with Spline
				</a>
			</p>
		</div>
	);
}
```

The credit markup is part of the snippet, not an optional extra. The
`spline-viewer` element renders a Spline badge on its own, driven by the
scene's publish setting; a React component on a bare canvas does not, so the
link is how the scene gets credited. If the scene is a remix, add the original
creator's community link next to it.

## Cursor specifics [#cursor-specifics]

* Cursor can read the packages you have installed. Point it at `node_modules/@splinetool/runtime/AGENTS.md` — and the same file in `@splinetool/loader` and `@splinetool/viewer` — for the full method-by-method surface. Those files ship inside the published tarballs, so they match the version you actually installed.
* When you paste a scene URL into a chat, paste the whole thing. A truncated id is indistinguishable from a hallucinated one.
* For imperative control, ask for `@splinetool/runtime` and check the import is `import { Application }` — a named import. A default import of the runtime is a hallucination.

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
