# Scroll Event (/interaction-states-events-and-actions/events/scroll-event)



The Scroll Event requires the user to scroll in order to go through the transitions added inside.

<Video src="https://cdn.spline.design/_assets/docs/3266f025-b2f6-498e-8a86-1d43ee052632.mp4" />

There are two types available on the Scroll Event

* **Steps** → The amount of scroll needed to go from the beginning of a transition to the end.
* **Scroll →** lets you transition between states (set up in the actions section) based on the scroll of your web page.

Here are the different Actions you can trigger with the Scroll Event:

* [Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action.md)
* [Animation Action](https://docs.spline.design/interaction-states-events-and-actions/actions/animation-action.md)
* [Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action.md)
* [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md)
* [Variable Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/variable-control-action.md)
* [Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md)
* [Clear Local Storage Action](https://docs.spline.design/interaction-states-events-and-actions/actions/clear-local-storage-action.md)
* [API Request Action](https://docs.spline.design/interaction-states-events-and-actions/actions/api-request-action.md)

<Image src="https://cdn.spline.design/_assets/docs/886f2e69-927f-45e3-8b6f-945dc446820e.png" alt="image" maxWidth="300" />

***

### Type Scroll [#type-scroll]

The **Scroll** event has a Type called **Scroll*&#x2A; which only works with the &#x2A;**Viewer export***.

This type lets you transition between states (set up in the actions section) based on the scroll of your web page.

<Video src="https://cdn.spline.design/_assets/docs/31e175ef-6f7a-4e17-be12-26ff45d8b2ae.mp4" />

<Callout>
  *👉 Check out the demo at: [https://viewer-scroll-event.framer.website/](https://viewer-scroll-event.framer.website/)*
</Callout>

#### Start From - Enter View [#start-from---enter-view]

Objects with scroll events will start animating once the viewer component comes into view on your web page.

* **Start At**
  * **Top** → Animations will start once the top of the component gets into view.
  * **Middle** → Animations will start once the middle of the component gets into view.
  * **Bottom** → Animations will start once the bottom of the component gets into view.

* **Offset** - For each Start At option, you can still add an offset to that option so it starts later.

* **End After** - Defines at what scroll amount from the set Start At location (measured in pixels) should the Transition Action reach its final state.

<Image src="https://cdn.spline.design/_assets/docs/5bda9684-613c-4010-a41d-36e8783dc632.png" alt="image" maxWidth="300" />

#### Start From - Page [#start-from---page]

Objects with scroll events will start animating at the defined Start At the position of your web page, which means the height from the top of the webpage measured in pixels.

* **Start At** - The position on your web page where the scroll events should start animating.
* **End After** - Defines at what scroll amount (measured in pixels from the top of the web page) should the Transition Action reach its final state.

<Image src="https://cdn.spline.design/_assets/docs/b387d735-e5bd-4511-9ba4-769216514788.png" alt="image" maxWidth="300" />

***

<Embed src="https://my.spline.design/HRCtQcUt2dS48gy7AYUs8MCP/" title="Spline Embed" height="384" />

> *Scroll to interact! 👆 The Scroll Event uses scroll to go through the transitions added inside.*
