# Variable Control Action (/interaction-states-events-and-actions/actions/variable-control-action)



Variable Control Action allows you to control the interaction of dynamic variables in the scene.

<Callout>
  Learn more about [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md) to fully understand how to use Variable Control Action.
</Callout>

## How to use Variable Control Action [#how-to-use-variable-control-action]

When an Event is performed, a dynamic variable can be controlled with the following interaction types: `Play`, `Pause`, `Stop` , `Restart`, or `Toggle - Ping Pong` along with a delay value.

Here is a simple how-to example of interacting with the dynamic variable via a mouse click.

<Video src="https://cdn.spline.design/_assets/docs/86e552f7-30ff-404f-a428-2ba994a97182.mp4" />

*Video demonstrating how to use Variable Control Action with Dynamic Counter Variable.*

1. In a new scene, create a cube and a dynamic variable of type `Counter` from the Variable panel.
2. Set the Interval value to “0.001” to make the counter grow faster.
3. Select the cube and assign the counter variable to the X position of the cube.
4. Add an event in the right sidebar in the events section by clicking the “+” icon.

   <Image src="https://cdn.spline.design/_assets/docs/3113706f-18b5-463b-91e0-57da66c6a0d5.png" alt="image" maxWidth="300" />
5. Change the event type in the top dropdown to “Mouse Down”.
6. Add an action “Variable Control” and expand it by clicking on the “>” icon.
7. Click on the dropdown in the Variable Control Action and select the variable to be controlled –  the `Counter` for this example.
8. Enter Play mode and click on the cube to see it moving along the X axis over time.

<Image src="https://cdn.spline.design/_assets/docs/43958c6f-b33a-420b-a391-ff0c62c42e58.png" alt="image" maxWidth="300" />

***

## Events supporting Variable Control Action [#events-supporting-variable-control-action]

The following Events have access to Variable Control Action.

* [Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)
* [Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)
* [Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)
* [Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event.md)
* [Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)
* [Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)
* [Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)
* [Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)
* [Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event.md)
* [Drag and Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event.md)
* [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md)
* [Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event.md)
* [State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event.md)
* [Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)
* [Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event.md)
* [Screen Resize Event](https://docs.spline.design/interaction-states-events-and-actions/events/screen-resize-event.md)

***

## Variable Control Action properties [#variable-control-action-properties]

### Select Dynamic Variable [#select-dynamic-variable]

Select the dynamic variable to be updated via the Variable Control Action. The dropdown list will access any dynamic variables that are available in the current file.

### Interaction [#interaction]

Set the type of interaction that should occur when an event is performed.

**Play** → Plays the dynamic variable.

**Pause** → Pauses the dynamic variable.

**Play/Pause** → On event trigger, plays or pauses the dynamic variable based on the current state.

**Stop** → Stops the running dynamic variable.

**Restart** → Restarts the dynamic variable.

**Toggle - Ping Pong** → Reverses the dynamic variable.

### Delay [#delay]

Adds a delay to the interaction of the Variable Control Action to take place.

<Image src="https://cdn.spline.design/_assets/docs/20dd50c4-d8e4-4ad9-93d9-1f1bbb7008c0.png" alt="image" maxWidth="300" />

<Callout>
  Restart and Toggle interactions are only available for Counter Dynamic Variable.
</Callout>

***

## Using Variable Control with Conditional Action [#using-variable-control-with-conditional-action]

[Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md) allows you to create more sophisticated Variable Control Actions. Read the doc to learn more about it.
