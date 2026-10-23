# Code API for Web (/exporting-your-scene/web/code-api-for-web)



The **Code API** allows you to seamlessly integrate interactive 3D experiences into your projects, offering greater control and customization. It enables you to trigger actions, modify object properties, and create dynamic, responsive 3D environments directly from your existing code and user interface.

<Callout>
  **Important**: The Code API is a set of tools for developers to add custom interactivity between Spline scenes and their custom code. This is different from the Real-time API feature, which is a feature that allows the creation of API connections with your Spline scenes, all made within the Spline editor.
</Callout>

>

<Callout>
  Learn more: [Real-time API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api.md)
</Callout>

#### Key capabilities: [#key-capabilities]

<Callout>
  This is a high-level overview of the key capabilities with CodeAPI, for more specific capabilities go to relevant library documentation below.
</Callout>

* **Adjust variables:** Retrive and update variables in a Spline scene.
* **Adjust Properties**: Dynamically update position, scale, rotation, and more.
* **Trigger Transitions**: Create transitions and animations based on events.
* **Event Listeners**: React to real-time events within your 3D scenes.

## ✅ Supported platforms [#supported-platforms]

CodeAPI is based on the Spline Runtime and is available in Vanilla.js, React, and Next.js. For more details, read below. Learn more about the supported export formats here: [Exporting as Code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md).

### Vanilla.js Code API [#vanillajs-code-api]

Our vanilla.js runtime library is the core of any runtime-based library (our React and Next.js libraries use it internally).

Open this [CodeSandbox example](https://y5w4vn.csb.app/) to get you started. Learn more about the Code API capabilities between Vanilla.js and Spline here:

[https://www.npmjs.com/package/@splinetool/runtime](https://www.npmjs.com/package/@splinetool/runtime)

### React Code API [#react-code-api]

React serves as a wrapper for the Vanilla.js Spline Runtime, allowing you to leverage the full functionality of the Code API within your React projects. Anything possible in Vanilla.js runtime library above is also possible in the React library.

Learn more about the Code API capabilities between React and Spline here:

[https://github.com/splinetool/react-spline#nextjs](https://github.com/splinetool/react-spline#nextjs)

### Next.js [#nextjs]

Our Next.js library is almost the same as the React one with a few additional Next.js specific features. Everything that you can do with React library is also achievable with the Next.js one.

Learn more about the Code API capabilities between Next.js and Spline here:

[https://github.com/splinetool/react-spline#nextjs](https://github.com/splinetool/react-spline#nextjs)
