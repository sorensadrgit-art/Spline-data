# Variables (/interaction-states-events-and-actions/variables-and-data/variables)



<Embed src="https://www.youtube.com/embed/Id_SZVCUVMM" title="YouTube video player" />

*Tutorial: How to use variables to create interactive 3d content in Spline*

Variables allow you to create reusable values/parameters. They can be applied to many object properties (like Position, Scale, Rotation, etc.) and can be combined with events and actions. This enables you to create highly customized interactions that understand logic.

Some high-level concepts for variables are:

* Create variables such as **Numbers**, **Strings**, and **Booleans**
* Use Dynamic variables: **Time**, **Counter**, **Random**
* Attach variables to object properties and text fields.
* Trigger events from variables
* Capture object and mouse property changes

By leveraging variables, along with [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md) and [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md), you can craft truly interactive and dynamic experiences. We encourage you to explore, experiment, and push the boundaries of creativity with variables in Spline.

***

## Variables [#variables]

Variables are data containers with values that can change. The following variable types are available:

<Image src="https://cdn.spline.design/_assets/docs/06c71a80-ee47-48f4-a152-baa5e7425036.png" alt="image" maxWidth="500" />

### 🔢 Number [#number]

* Easily manage numerical data to control and animate objects.
* Can be a decimal or a round number, e.g.: `9` or `67,123`
* Usage: alter or adjust any property on your object that uses a number (e.g.: position, rotation, scale, material layer opacity, etc.)

### 🔤 String [#string]

* Can be any text value, e.g.: `some text`
* Incorporate text-based variables for labels, messaging or updating the status of your experience.

### 🔘 Boolean [#boolean]

* Toggle between `true` and `false` states for interactive behavior.
* With the help of booleans, you can build sophisticated logic into your experience, especially if you combine it with [Conditional Action](https://docs.spline.design/interaction-states-events-and-actions/actions/conditional-action.md) and [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md).

***

## Dynamic variables [#dynamic-variables]

Dynamic variables are changing over time based on specific conditions. These unlock the creation of interactive experiences driven by variables. The following dynamic variable types are available: **Time**, **Counter**, &#x2A;*Random.**

<Image src="https://cdn.spline.design/_assets/docs/9cf4a1da-aa96-4e4f-8f47-c3cf55534e87.png" alt="image" maxWidth="500" />

### 🕓 Time [#time]

* Harness the flow of time to create dynamic animations and transitions
* It’s defined by a string that can be applied as the content of a Text object.
* It has following types: **Clock**, **Timer**, **Stopwatch**
* All types have unique property options, listed below

<Image src="https://cdn.spline.design/_assets/docs/379a67f1-0790-4996-9e75-8c6bdc3fe13e.png" alt="image" maxWidth="300" />

🕓 **Clock** → Updating time, based on local time or on a specific time zone.

| Property  | Explanation                                                           | Options                                            |
| --------- | --------------------------------------------------------------------- | -------------------------------------------------- |
| Format    | Change the appearance of the time based on common formatting options. | `HH:mm:ss` `mm:ss` `Seconds` `Seconds (3-decimal)` |
| 12/24h    | Option to use 24 hours based time.                                    | `12h` `12h AM/PM` `24h`                            |
| Time Zone | Show the local time zone or a specific time zone.                     | `None`, from `UTC -12` to `UTC+14`                 |

⏲️ **Timer** → Calculating from a pre-defined time backwards, e.g.: from 30 seconds to 0 seconds

| Property  | Explanation                                                                        | Options                                                                                                              |
| --------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Format    | Change the appearance of the time based on common formatting options.              | `HH:mm:ss` `mm:ss` `Seconds` `Seconds (3-decimal)`                                                                   |
| Value     | At what time should the timer/stopwatch start                                      | `H` – hour, `M` – minute, `S` – second                                                                               |
| End Value | If set to `YES` it can be defined when should the timer end                        | `H` – hour, `M` – minute, `S` – second                                                                               |
| On End    | Can be decided if the timer should restart, or end after it reached the end value. | `Restart` – restarts the timer after reaches the end value, `Stop` – stops the timer after it reaches the end value. |

⏱️ **Stopwatch** → Calculating from a pre-defined time forward, e.g.: from 0 seconds to 30 seconds.

| Property  | Explanation                                                                            | Options                                                                                                                      |
| --------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Format    | Change the appearance of the time based on common formatting options.                  | `HH:mm:ss` `mm:ss` `Seconds` `Seconds (3-decimal)`                                                                           |
| Value     | At what time should the stopwatch start                                                | `H` – hour, `M` – minute, `S` – second                                                                                       |
| End Value | If set to `YES` it can be defined when should the timer end                            | `H` – hour, `M` – minute, `S` – second                                                                                       |
| On End    | Can be decided if the stopwatch should restart, or end after it reached the end value. | `Restart` – restarts the stopwatch after reaches the end value, `Stop` – stops the stopwatch after it reaches the end value. |

### 🔢 Counter [#counter]

The Counter will start counting in seconds with a set interval defined in seconds. It can be great to use it for iterating through dynamic sequences or loops, e.g.: driving an animation with the counter.

| Property  | Explanation                                                                        | Options                                                                                                              |
| --------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Format    | Change the appearance of the time based on common formatting options.              | `HH:mm:ss` `mm:ss` `Seconds` `Seconds (3-decimal)`                                                                   |
| Value     | At what time should the counter start                                              | `H` – hour, `M` – minute, `S` – second                                                                               |
| Interval  |                                                                                    |                                                                                                                      |
| Step      |                                                                                    |                                                                                                                      |
| End Value | If set to `YES` it can be defined when should the timer end                        | `H` – hour, `M` – minute, `S` – second                                                                               |
| On End    | Can be decided if the timer should restart, or end after it reached the end value. | `Restart` – restarts the timer after reaches the end value, `Stop` – stops the timer after it reaches the end value. |

### 🔀 Random [#random]

Random will generate a random value within a set range. With random values create randomness and unpredictability in your project, e.g., mini-game logic and procedural visuals.

| Property      | Explanation                                                                                            | Options                               |
| ------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| Default value | A default value can be defined for the variable.                                                       | `number`                              |
| Static        | Random can be static, or non-static                                                                    | `Yes`, `No`                           |
| Interval      | If Static is set to No, a new random number will be generated with the set interval defined in seconds | `S` – interval defined in seconds     |
| Minimum       | The range in which the random numbers should be picked, defining it’s minimum value.                   | `number`                              |
| Maximum       | The range in which the random numbers should be picked, defines it’s maximum value.                    | `number`                              |
| Decimals      | Defining the formatting of the random numbers.                                                         | `0 (Integer)`, `0.0`, `0.00`, `0.000` |

***

## Local Storage [#local-storage]

Enabling local storage on your variables will allow you to store persistent data on your exported scenes using variables.

<Callout>
  **Variables Local Storage** is a paid feature; you’ll need an active **Pro** or **Max** subscription to use it.
</Callout>

Try it on the demo: [→ Bar Chart - Persistent](https://my.spline.design/barchartpersistent-52a67ab58b5afe48ee6f62ca8a40d842/)

### Enabling Local Storage [#enabling-local-storage]

1. Open the variables panel, from the right sidebar.
2. Find the variable you want to make persistent with local storage.
3. Press the local storage icon that shows up on hover.

<Image src="https://cdn.spline.design/_assets/docs/2e114ad3-2273-4a21-9cf9-6c7e3dce1e74.png" alt="image" maxWidth="500" />

To reset the persistent data of your variables back to their default values using an event trigger you can use the [Clear Local Storage Action](https://docs.spline.design/interaction-states-events-and-actions/actions/clear-local-storage-action.md).

***

## Events supporting variables [#events-supporting-variables]

Following Events have access to the [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md). This means when any of these events are performed, a variable can be set to a new value via an expression – either another variable or a custom calculation.

* [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md)
* [Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)
* [Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)
* [Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)
* [Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)
* [Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)
* [Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)
* [Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)
* [Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event.md)
* [Drag and Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event.md)
* [Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event.md)
* [State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event.md)
* [Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)
* [Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event.md)

Some high-level concepts for using variables with events and actions:

* [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md) - A special event that is triggered when a variable’s value changes. Pro tip: use these with the dynamic variables (e.g.: counter) to animate an object’s property.
* [Set Variable Action](https://docs.spline.design/interaction-states-events-and-actions/actions/set-variable-action.md) - An action that allows you to modify variables and object properties. It can be either another referenced variable or can be a custom calculation.

***

## How to use variables [#how-to-use-variables]

Here is a simple guide to creating variables, assigning them to a cube, and updating it via an event.

### Create variables [#create-variables]

1. Open the variable table from the right sidebar, it’s visible when no objects are selected.
2. Select a variable type, for this exercise select “Number”.
3. Change the number to a specific value in the right column, e.g.: `100`.
4. Double-click the name of the variable “Number”, to change its name, name it something like `Initial Position`.
5. Right-click the variable and select “duplicate” to duplicate it.
6. Name the duplicate something like `New Position` and adjust it’s value to `200`.
7. Done, the variables are ready to be used!

### Assign a variable to an object [#assign-a-variable-to-an-object]

1. Create a cube (select it in the top toolbar and click on the viewport).
2. Select the cube.
3. Hover any of it’s properties (e.g.: Position X).
4. Click on the little dot in the upper right corner.
5. Select the variable to be assigned, `Initial Position` in this case.
6. Done, the object is driven by a variable!

### Update variables with events and actions [#update-variables-with-events-and-actions]

Variables can be updated with all sorts of events and actions. Here is a simple example of updating the variable via a mouse click.

1. Select the cube.
2. Add an event in the right sidebar at the events section.
3. Open the event “Start” by clicking on it.
4. Change the event type in the top dropdown to “Mouse Down”.
5. Add an action “Set Variable”.
6. Expand the action by clicking on the “>” icon.
7. Select the variable you would like to change, it should be `Initial Position` in this exercise.
8. In the “To” section there is an “Add expression” field, here is the place where you can define what should be the selected variable updated to when the event is performed. Click in the field and select the initially created `New Position` variable.
9. Enter Play mode and click on the cube.
10. Congrats! You have created your first variable update via a Mouse Down Event.

***

## Best practices and troubleshooting [#best-practices-and-troubleshooting]

* **Keep It Simple**: Start with a few variables and build complexity as you gain confidence.
* **Test and Iterate**: Experiment with different variable values to find the perfect balance for your spline project.
* **Variable Not Updating?**: Ensure that the Variable Change events and Set Variable actions are correctly configured and referencing the right variable. Also, check the formula being used.
* **Unexpected Behavior**: Double-check your logic to identify any discrepancies in your variable usage.
