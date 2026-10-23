# Screen Resize Event (/interaction-states-events-and-actions/events/screen-resize-event)



A Screen Resize Event will trigger actions based on the size of the canvas. Define multiple sizes by adding breakpoints. This is useful when needing to rearrange your scene to better fit different types of screen sizes like desktop vs. mobile.

<Video src="https://cdn.spline.design/_assets/docs/8545c0f1-22eb-4b1d-8925-a854256a0043.mp4" />

***

### Settings for Screen Resize Event [#settings-for-screen-resize-event]

#### Type [#type]

On type, you can define if the breakpoints on the event will be horizontal or vertical.

#### Breakpoints [#breakpoints]

Breakpoints are defined by pixel values and an operator (`> more than`, `< less than`, and `<> between`).

<Callout>
  Eg. On the UI to the right, on the Mobile preset, the actions will be triggered once the canvas becomes less than 480 pixels horizontally.
</Callout>

* There are 3 presets available (Mobile, Table, Desktop) or you can set your Custom values.
* To add a new breakpoint, use the “Add New Breakpoint” button at the bottom.
* To delete a breakpoint, look for the delete icon that appears on hover.
* To add a new action, use the + icon on the respective breakpoint you want to add an action to.

<Image src="https://cdn.spline.design/_assets/docs/9f95d698-ec6b-4852-a04b-abafdb61a371.png" alt="image" maxWidth="300" />

#### Actions [#actions]

Here are the different actions you can trigger with the Screen Resize Event:

* [Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action.md)
* [Animation Action](https://docs.spline.design/interaction-states-events-and-actions/actions/animation-action.md)
* [Sound Action](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action.md)
* [Particle Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/particles-control-action.md)
* [Video Action](https://docs.spline.design/interaction-states-events-and-actions/actions/video-action.md)
* [Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action.md)
* [Destroy Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/destroy-object-action.md)
* [Switch Camera Action](https://docs.spline.design/interaction-states-events-and-actions/actions/switch-camera-action.md)
* [Scene Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/scene-transition-action.md)
* [Reset Scene Action](https://docs.spline.design/interaction-states-events-and-actions/actions/reset-scene-action.md)
* [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md)
* [Variable Control Action](https://docs.spline.design/interaction-states-events-and-actions/actions/variable-control-action.md)
* [Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md)
* [Clear Local Storage Action](https://docs.spline.design/interaction-states-events-and-actions/actions/clear-local-storage-action.md)
* [API Request Action](https://docs.spline.design/interaction-states-events-and-actions/actions/api-request-action.md)
