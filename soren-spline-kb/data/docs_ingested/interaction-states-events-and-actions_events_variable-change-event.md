# Variable Change Event (/interaction-states-events-and-actions/events/variable-change-event)



The Variable Change Event allows you to trigger actions when a specific variable changes.

## Variable Change Event Properties [#variable-change-event-properties]

#### Select Variable [#select-variable]

On the first dropdown, select the variable that the event should check for changes.

Once the event detects a change in the variable value, it will trigger the Actions added to it.

The dropdown list will access any variables available on the current file.

<Image src="https://cdn.spline.design/_assets/docs/ed7dc797-822b-4e7e-b888-4e493679339b.png" alt="image" maxWidth="300" />

The following variable types can be used:

| Variable type              | Defined by                                                                                                                                                   | Usage                                                                                                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🤹 Variables               | Number, String, Boolean, Timers, Counter or Random                                                                                                           | Variables can store values that are reusable. For detailed explanation read the [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md) doc. |
| ℹ️ Object Property         | Object’s position, rotation, or scale (X, Y, Z), or it’s width, height and depth as a number, e.g.: `100`                                                    | Capture object property changes, and save them as variables to create advanced interactions.                                                                          |
| 🖱️ Mouse Position (2D)    | The position of the mouse on the screen is defined by X and Y as numbers.                                                                                    | Animate or manipulate objects based on the mouse position                                                                                                             |
| 💥 Mouse Hit Position (3D) | The position of the mouse hitting an object in 3D space, as Position X, Y, or Z of the hit location, or the Position X, Y, and Z of the object that was hit. | Create interactions based on specific hit positions, e.g.: visualize hit in 3D space.                                                                                 |
