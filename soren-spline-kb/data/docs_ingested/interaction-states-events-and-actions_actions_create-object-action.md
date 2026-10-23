# Create Object Action (/interaction-states-events-and-actions/actions/create-object-action)



The Create Object action allows the creation of new objects within a scene. Spawning objects is possible via a variety of events, which unlocks plenty of use cases for playful effects and interactions.

<Image src="https://ucarecdn.com/d12f036f-0034-4c9a-b47e-bc2f7cd4dd13/" alt="Create Object in action with Mouse Down and Follow events" />

*Create Object in action with Mouse Down and Follow events*

## Creating a new Create Object Action [#creating-a-new-create-object-action]

1. Select an object and create an event on the right-side panel for it. (e.g.: Follow, Start, Mouse down)
2. Open the event and find the “Actions” panel.
3. Add “Create Object” to your actions.
4. Select the object to be created and customize the behavior to your liking.

<Embed src="https://my.spline.design/gikOzZnGrPC1fSkbc2Sr1PNv/" title="Spline Embed" height="384" />

<Callout>
  *👆 Drag your mouse or finger around to experience object creation via follow event.*
</Callout>

Object creation can be used with the following events:

[Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)

[Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)

[Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)

[Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event.md)

[Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)

[Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)

[Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)

[Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)

[Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event.md)

[Drag and Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event.md)

[Follow Event](https://docs.spline.design/interaction-states-events-and-actions/events/follow-event.md)

[Game Controls Event](https://docs.spline.design/interaction-states-events-and-actions/events/game-controls-event.md)

[Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)

## Customizing a Create Object Action [#customizing-a-create-object-action]

**Object →** Select the target object to be created.

**Origin →** Specifies the location of creation, either in the `world position` or `relative to another object`.

**Base →** Determines the visibility of the reference object in play mode.

**Position →** Sets the specific position of the created object based on the x, y, and z values.

**Delay** → Specifies the delay in seconds before the object is created.

**Frequency** → Sets the frequency at which the object is created, ranging from 0.01 to 60 times per second.

**Rotation** → Specifies the rotation of the created object based on the x, y, and z values.

**Dynamic** → Determines whether physics is applied to the created object.

<Image src="https://cdn.spline.design/_assets/docs/b0ac6f7a-3fcc-4c8a-98ee-f783e93ff925.png" alt="image" maxWidth="300" />

**Velocity →** Sets the initial velocity of the created object along the x, y, and z axes.

**Destroy** → Determines when the created object should be destroyed.

* **No:** The object will not be destroyed automatically.
* **After Lifetime:** The object will be destroyed after a specified lifetime in seconds.
* **After Collision:** The object will be destroyed upon collision with another object.
* **After Amount is Reached:** The object will be destroyed after a specific number of instances have been created.
  * **Amount:** Specifies the desired number of instances to be created before the object is destroyed.
