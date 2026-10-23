# Exporting as Code (/exporting-your-scene/web/exporting-as-code)

> Export your scene as Vanilla JS, React, Next.js, Three.js or react-three-fiber code.



## Code Export Options [#code-export-options]

Spline allows you to export the code of your scene as:

* **Vanilla JS**
  * 📄 Runtime Docs: [https://www.npmjs.com/package/@splinetool/runtime](https://www.npmjs.com/package/@splinetool/runtime)
* **Three.js**
  * 📄 Loader Docs: [https://www.npmjs.com/package/@splinetool/loader](https://www.npmjs.com/package/@splinetool/loader)
* **React**
  * 📄 React Docs: [https://github.com/splinetool/react-spline](https://github.com/splinetool/react-spline)
* **Next.js**
  * 📄 Next.js Docs: [https://github.com/splinetool/react-spline#nextjs](https://github.com/splinetool/react-spline#nextjs)
* **react-three-fiber**
  * 📄 r3f Docs: [https://github.com/splinetool/r3f-spline](https://github.com/splinetool/r3f-spline)

<Callout>
  Animations and events are only enabled when exporting to Vanilla js and React.
</Callout>

## How to Export [#how-to-export]

1. Once you’re happy with your scene, press the `Export` button on the toolbar.
2. Select &#x2A;**“Code”*** on the left sidebar and choose from any of the code types available on the top dropdown, then wait for the URL to be generated.
3. A toast notification will appear to let you know when your URL is ready.
4. You can copy the code, open it as a CodeSandbox project, or download the local files to host it yourself.
5. Multiple properties can be adjusted under [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).

<Video src="https://cdn.spline.design/_assets/docs/6f459b15-d645-4d35-a967-db58cf3e322c.mp4" />

<Callout>
  You can download the code exports and host them on your own server.
</Callout>

## About the Web Content Export (Vanilla JS) [#about-the-web-content-export-vanilla-js]

1. Following the steps above you can export as Web Content by choosing &#x2A;**Vanilla JS*** as the code type under the dropdown.
2. You will find a button at the bottom of the panel to download the content as a `.zip` file.
3. If you want to play the experience, you need to run a [*localserver*](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server). Open your OS terminal or console from the uncompressed folder path and run: `python -m SimpleHTTPServer`

*The files saved from the "Web Content" option are the same used for the "Public URL". This is the way to add the files directly to your web project.*

The file structure might look something like the following:

<Image src="https://cdn.spline.design/_assets/docs/a686e8d3-4ffb-4486-ac5e-72b04646007b.png" alt="image" maxWidth="400" />

<Callout>
  Note: Inside the index.html there is a Canvas element, which is where your scene renders. Spline draws on **WebGPU** by default and falls back to **WebGL** automatically on browsers without WebGPU support — you don't need to configure anything. The export panel's **Renderer** setting lets you change that per scene; see [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).
</Callout>

## Drafts [#drafts]

You can use drafts to version your exports. Each Draft is a snapshot of your scene.

The Draft labeled `Production` is the one to which the main URL is pointing to. If there are additional changes on the scene or export settings, click `Generate Draft` or `Promote to Production` for the code to reflect the latest changes.

There is one production code, and many drafts can be created as needed under the Drafts tab. Any of the Drafts can be promoted to Production.

<Image src="https://cdn.spline.design/_assets/docs/af50ab32-3e6d-4285-b776-92369c3ab526.png" alt="image" maxWidth="600" />

## Handling events outside of Spline [#handling-events-outside-of-spline]

Learn more about Code API for Web: [**Code API for Web**](https://docs.spline.design/exporting-your-scene/web/code-api-for-web.md)

You can handle events outside of Spline and use them to manipulate your spline objects.

Here are 2 examples:

1. [Example 1](https://t.co/LNY3rPisfx)
2. [Example 2](https://t.co/hxPGueXqL2)

<Video src="https://cdn.spline.design/_assets/docs/d343d430-dbae-43de-8f42-91f4cef10bd0.mp4" />

### 👉 Related docs [#-related-docs]

[Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md), [How to optimize your scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md)
