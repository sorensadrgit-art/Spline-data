# Set Variable Action (/interaction-states-events-and-actions/actions/set-variable-action)



Set Variable Action can update the value of a variable defined by an expression. The expression can reference another variable or variable helpers.

<Callout>
  Learn more about [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md) to fully understand how to use Set Variable Action.
</Callout>

## How to use Set Variable Action [#how-to-use-set-variable-action]

When an Event is performed, a variable can be set to a new value in the Set Variable Action by an expression – it can be either updated to another variable or a custom calculation. Following Events have access to Set Variable Action.

Learn how to use Set Variable Action through how-to steps in the [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md) doc.

## Events supporting Set Variable Action [#events-supporting-set-variable-action]

When an Event is performed, a variable can be set to a new value in the Set Variable Action by an expression – it can be either updated to another variable or a custom calculation. Following Events have access to Set Variable Action

[Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md)

[Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)

[Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)

[Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)

[Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)

[Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)

[Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)

[Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)

[Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event.md)

[Drag and Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event.md)

[Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event.md)

[State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event.md)

[Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)

[Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event.md)

## Set Variable Action properties [#set-variable-action-properties]

### Select Variable [#select-variable]

Select the variable to be updated via the Set Variable Action. The dropdown list will access any variables that are available on the current file.

### Add Expression [#add-expression]

Create an expression to which the selected variable should be updated.

The following variable types can be used:

| **Variable type**              | **Defined by**                                                                                                                                               | **Usage**                                                                                                                                                             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **🤹 Variables**               | Number, String, Boolean, Timers, Counter or Random                                                                                                           | Variables can store values that are reusable. For detailed explanation read the [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md) doc. |
| **ℹ️ Object Property**         | Object’s position, rotation, or scale (X, Y, Z), or it’s width, height and depth as a number, e.g.: `100`                                                    | Capture object property changes, and save them as variables to create advanced interactions.                                                                          |
| **🖱️ Mouse Position (2D)**    | The position of the mouse on the screen is defined by X and Y as numbers.                                                                                    | Animate or manipulate objects based on the mouse position                                                                                                             |
| **💥 Mouse Hit Position (3D)** | The position of the mouse hitting an object in 3D space, as Position X, Y, or Z of the hit location, or the Position X, Y, and Z of the object that was hit. | Create interactions based on specific hit positions, e.g.: visualize hit in 3D space.                                                                                 |

The following math operations can be used in formulas:

| **Symbol** | **Operator**                        |
| ---------- | ----------------------------------- |
| `+`        | Add                                 |
| `-`        | Subtract                            |
| `*`        | Multiply                            |
| `/`        | Divide                              |
| `Random`   | Random value                        |
| `(` `)`    | Group calculations with parenthesis |

Some example formulas to spark ideas

* Variable A + Variable B
* Variable A \* 10 / 2
* (Variable A + Variable B) \* 10

***

## Using Set Variable Action with Conditional Action [#using-set-variable-action-with-conditional-action]

[Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md) allows you to create more sophisticated Set Variable Actions. Read the doc to learn more about it.
