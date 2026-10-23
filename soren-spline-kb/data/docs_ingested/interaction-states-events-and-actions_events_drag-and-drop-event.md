# Drag and Drop Event (/interaction-states-events-and-actions/events/drag-and-drop-event)



Drag and Drop Event allows you to create interactive experiences where objects can be dragged and dropped with customizable parameters.

<Embed src="https://www.youtube.com/embed/YZyxoDXoOyc" title="YouTube video player" />

***

## Adding a Drag and Drop Event [#adding-a-drag-and-drop-event]

<Callout>
  By customizing parameters and behaviors, you can create dynamic drag and drop interactions in your scenes.
</Callout>

<Image src="https://cdn.spline.design/_assets/docs/f06b6a8e-76ff-47d5-a552-b254eb6b070d.png" alt="image" />

Here's how to use the Drag and Drop Event:

1. Select the object(s) that you want to make draggable.
2. On the Events panel, add a new event and select `Drag and Drop` from the dropdown menu.
3. Open the `Drag and Drop` event and customize the settings to your liking.

<Embed src="https://my.spline.design/UQe8GKoXSTQP4rG1rCZ9i5Rx/" title="Spline Embed" height="384" />

<Callout>
  *Use your mouse/touchscreen to interact! 👆 You can drag and drop the purple cubes. Tip: You can snap them on the grey shapes.*
</Callout>

### Settings for Drag [#settings-for-drag]

**Cursor**

* Hand / Move / Default → Affects cursor appearance while hovering over draggable objects.

**Render**

* Normal: the draggable object will be covered with other objects.
* On Top of All: Renders the dragged objects on top of all other objects.

**Damping**

* Sets the damping value for the dragged objects. Values range from 1 to 80, where higher values provide more delay.

**Plane**

* Aligned with Camera: The drag plane is aligned with the camera's orientation.
* Adaptive to Camera: The drag plane adapts to the camera's orientation as it moves.
* Axis or Plane: The drag plane is aligned with the selected axis or plane.

**Plane Mode**

* Keep Initial Plane Position: The drag plane retains its initial position.
* Use Current Object Position: The drag plane uses the current position of the dragged object.

**Relative To**

* World: The drag is relative to the world coordinates.
* Parent: The drag is relative to the parent object's coordinates.
* Object: The drag is relative to the object's own coordinates.

**Objects to Drag**

* Add objects to the list that you want to make draggable.

**Drag Limits**

* Define the minimum and maximum values for the X, Y, and Z axes to limit the dragging range. Values can be arbitrary, ranging from negative to positive.

<Image src="https://cdn.spline.design/_assets/docs/546fb4e8-231c-409d-a47e-e49b28ecf538.png" alt="image" maxWidth="300" />

### Settings for Drop [#settings-for-drop]

Drop allows objects to snap to specific positions after being dropped. Drop is an optional feature. Turn it on to take effect. Customize the following properties:

**Snap to**

* Object Position: Snaps the dropped object to the position of another object.
* Surface: Snaps the dropped object to the surface it is dropped on.

**Snap Speed**

* Sets the speed at which the object snaps to the target position. Values range from 0 to 40, with higher values indicating faster snapping.

**Auto-Orient**

* Yes: The dropped object automatically orients itself to match the target object or surface.
* No: The dropped object maintains its original orientation.

**Fallback**

* Stay in Dropped Position: The dropped object remains in the position it was dropped.
* Return to Original Position: The dropped object returns to its original position.
* Return to Last Snapped Position: The dropped object returns to the last snapped position.

**Drop On**

* Any Object: The dropped object can be dropped on any object in the scene.
* List of Objects: Define a list of specific objects that the dropped object can be dropped on.

<Image src="https://cdn.spline.design/_assets/docs/6df344fe-d7bd-49f6-94dc-d3578aab5fe9.png" alt="image" maxWidth="300" />

### Behavior on Drag and Drop [#behavior-on-drag-and-drop]

Add actions such as transitions, sounds, or creating objects that will occur when the drag and drop event is triggered.

The following actions can be added for Drag and Drop events:

* [Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action.md) → e.g.: change the state of an object if it is Dragged or Dropped.
* [Sound Action](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action.md) → e.g.: add a sound effect when dragging or dropping the object.
* [Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action.md) → e.g.: spawn additional objects in the scene when the object is Dragged or Dropped.

<Image src="https://cdn.spline.design/_assets/docs/4e88ea41-35f8-4e57-9996-603880fdb535.png" alt="image" maxWidth="300" />
