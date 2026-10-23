# Exporting as Spline Viewer (/exporting-your-scene/web/exporting-as-spline-viewer)



The Spline Viewer is a more flexible way of embedding your Spline scenes into your websites.

`<spline-viewer>` is a native HTML web component and can be used with most web builders, frameworks, or browsers.

### Demos [#demos]

For interactive demos, check out

* [viewer.spline.design](http://viewer.spline.design)
* [viewer3d.framer.website](http://viewer3d.framer.website)

## Differences between a Public URL and the Viewer [#differences-between-a-public-url-and-the-viewer]

Public URLs can be embedded using an iFrame while the Viewer is a native HTML component that enables more flexibility.

Spline Viewer is able to capture the interactions that happen outside the canvas, allowing the 3D content to better connect with the web page where it is embedded (e.g.: create interactions based on the mouse position on the full web page or based on the web page’s scroll state).

### Global vs Local events [#global-vs-local-events]

* Global events are those that happen in the entire browser window.
* Local events only happen inside the canvas (or iFrame).

| **Feature**                      | **Public URL** | **Viewer** |
| -------------------------------- | -------------- | ---------- |
| **Works without an iFrame\***    | No             | Yes        |
| **Look At Event - Global/Local** | Only Local     | Both       |
| **Follow Event - Global/Local**  | Only Local     | Both       |
| **Scroll Event - Global/Local**  | Only Local     | Both       |

<Callout>
  Note: an iFrame is an HTML element that is commonly used to embed content on web pages. The iFrame only captures what happens within (Local).
</Callout>

## How to Export and Embed with Spline Viewer [#how-to-export-and-embed-with-spline-viewer]

1. Once you’ve set up your scene, press the `Export` button on the toolbar to open the Export panel.
2. Select &#x2A;**“Viewer”*** from the options on the left.
3. A toast notification will appear to let you know when your URL is ready.
4. You can now copy the Embed (Code snippet) and paste it into your web builder.
5. Multiple properties can be adjusted under [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).

<Video src="https://cdn.spline.design/_assets/docs/03f5d18e-7776-4080-9452-aca603aef953.mp4" />

<Callout>
  *👉 Check out the demo at: [https://viewer-embed.framer.website/](https://viewer-embed.framer.website/)*
</Callout>

## Viewer Options [#viewer-options]

### Logo [#logo]

If set to Yes a Spline logo will appear on your embed. If set to No the Spline logo will be removed from all your embeds.

### Hint [#hint]

Hint is an image that appears if no interaction with the scene is detected, to let users know it is possible to interact with the 3D content.

<Video src="https://cdn.spline.design/_assets/docs/7d2c3722-08bc-4197-a3be-a2a901503f50.mp4" />

### Loading [#loading]

Loading lets you decide if you want a spinner loader to appear while your scene is loading.

### Lazy-loading [#lazy-loading]

By default, the Spline Viewer uses a process called lazy loading, which loads the canvas content only when the canvas is visible on the screen.

You disable lazy-loading by using `loading="eager”`

### Mouse Events [#mouse-events]

**Global** (Full Window)

The global option means the mouse events will work on the full window of your web page.

**Local** (Canvas Container)

The local option means the mouse events will only work inside the container of the \<spline-viewer> HTML component.

<Video src="https://cdn.spline.design/_assets/docs/009899d4-4a95-45cd-828d-50e0d6b6e1be.mp4" />

<Callout>
  *👉 Check out the demo at: [https://viewer-scroll-event.framer.website/](https://viewer-scroll-event.framer.website/)*
</Callout>

## Integrations [#integrations]

Since `<spline-viewer>` is a native HTML component it is possible to integrate it with any framework, website builder, or browser!

Here are some known options:

* Framer

* Webflow

* Squarespace

* Typedream

* React

* JS

* Svelte

* \+ more…

## Main differences in Events [#main-differences-in-events]

All the events behave in the Viewer embeds as they would work normally with other embeds, but there are a few additional features you can take advantage of with the Scroll Event, Follow Event, and Look at Event. See more details below.

### Scroll Event [#scroll-event]

The **Scroll** event has a Type called **Scroll** which only works with the Viewer export.

This type lets you transition between states (set up in the actions section) based on the scroll of your web page.

👉 Check out the demo at: [https://viewer-scroll-event.framer.website/](https://viewer-scroll-event.framer.website/)

#### Start From - Enter View [#start-from---enter-view]

Objects with scroll events will start animating once the viewer component comes into view on your web page.

**Start At**

* **Top** → Animations will start once the top of the component gets into view.
* **Middle** → Animations will start once the middle of the component gets into view.
* **Bottom** → Animations will start once the bottom of the component gets into view.

**Offset**

For each Start At option, you can still add an offset to that option so it starts later.

**End After**

Defines at what scroll amount from the set Start At location (measured in pixels) should the Transition Action reach its final state.

<Image src="https://cdn.spline.design/_assets/docs/baff25cd-a97c-42c4-8ddc-64fa79bfd7c4.png" alt="image" maxWidth="300" />

#### Start From - Page [#start-from---page]

Objects with scroll events will start animating at the defined Start At the position of your web page, which means the height from the top of the webpage measured in pixels.

**Start At**

The position on your web page where the scroll events should start animating.

**End After**

Defines at what scroll amount (measured in pixels from the top of the web page) should the Transition Action reach its final state.

<Image src="https://cdn.spline.design/_assets/docs/5da91f3a-ebd2-486e-b7a5-549498751d1b.png" alt="image" maxWidth="300" />

### Follow Event [#follow-event]

With the Follow event, you can now control if the event works either:

* **Global** (mouse/touch events will work on the full window of the web page).
* **Local** (mouse/touch events will only work inside the container of the \<spline-viewer> HTML component).

<Video src="https://cdn.spline.design/_assets/docs/852480ab-6554-4025-9c39-1573d5a3b66f.mp4" />

<Callout>
  *👉 Check out the demo at: [https://viewer-follow-event.framer.website/](https://viewer-follow-event.framer.website/)*
</Callout>

### Look At Event [#look-at-event]

With the Look At event, you can now control if the event works either:

* **Global** (mouse/touch events will work on the full window of the web page).
* **Local** (mouse/touch events will only work inside the container of the \<spline-viewer> HTML component).

<Video src="https://cdn.spline.design/_assets/docs/b3156062-3505-4fff-ac22-4ce08dea7569.mp4" />

<Callout>
  *👉 Check out the demo at: [https://viewer-lookat-event.framer.website/](https://viewer-lookat-event.framer.website/)*
</Callout>

### 👉 Related docs [#-related-docs]

[Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md), [How to optimize your scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md)
