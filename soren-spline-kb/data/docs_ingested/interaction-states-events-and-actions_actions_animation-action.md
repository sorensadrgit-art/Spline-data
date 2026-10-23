# Animation Action (/interaction-states-events-and-actions/actions/animation-action)



With the Events system, you can trigger animations from imported objects. In order to use an animation action, you’ll need to have imported an animated object first. Learn more about how to import animation: [Import Animated Objects](https://docs.spline.design/importing-content/import-animated-objects.md).

## Creating a new Animation Action [#creating-a-new-animation-action]

You can trigger an animation by doing the following:

1. Select the object to which you want to add an animation action to.
2. On the Events panel, add an event that should trigger the animation action.
3. Open the Event and add an animation action.

<Video src="https://cdn.spline.design/_assets/docs/a9d43005-bba9-4512-bf1b-089293482518.mp4" />

\
Animation action is currently compatible within the following events:

To simply play your animation on start: [Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)

To play animation with mouse, touchscreen or keyboard interactions:

[Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)

[Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)

[Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event.md)

[Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)

[Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)

[Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)

[Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)

To make more dynamic game controls with the following options: On Idle, On Move, On Jump, On Run.

[Game Controls Event](https://docs.spline.design/interaction-states-events-and-actions/events/game-controls-event.md)

To trigger animations based on conditions:

[Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md)

To play animations upon collision, e.g.: an object explodes when collides:

[Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)

## Edit an Animation Action [#edit-an-animation-action]

* **Interaction** → what the action does to the animation:
  * **Play** → plays the selected animation (the default, with the options below)
  * **Pause** → holds the animation where it is. A later Play action on the same animation resumes it from there.
  * **Stop** → holds the animation on its first frame.
* **Object** → select a reference object that should be considered for the action
* **Animation** → select the animation to be played related to the object.
* **Start / End** → allows to trim your animation based on the available keyframes
* **Delay** → allows to play the animation with a delay, defined in seconds
* **Loop**
  * **Infinite** → will play the animation forever
  * **Count** → will play it for a set amount
  * **None** → will only play it once
* **Cycle** → if set to Ping Pong animation will be played forward and backwards in a loop.

## Pause or stop an animation [#pause-or-stop-an-animation]

Set the action's **Interaction** to **Pause** or **Stop** to control animations started by other actions, the same way a Timeline Animation action can pause or stop a timeline.

* **Object** → the animated object to pause or stop. Leave it on **All Objects** to affect every animation currently playing in the scene.
* **Animation** → with an object selected, the animation to pause or stop, or **All Animations** for every animation of that object.
* **Delay** → waits the given number of seconds before pausing or stopping.

A paused animation keeps its pose. Triggering a Play action for the same animation resumes it from where it was paused instead of restarting it; a stopped animation restarts from its first frame.

<Embed src="https://my.spline.design/floatingstonescenesfix-bd6918be45e8faffacb3431eb74ad9b9/" title="Spline Embed" height="384" />

> *Try out animation action with Game Controls in this example experience.*
