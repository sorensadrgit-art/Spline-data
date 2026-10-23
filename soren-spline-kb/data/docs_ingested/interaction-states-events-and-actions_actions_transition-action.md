# Transition Action (/interaction-states-events-and-actions/actions/transition-action)



Transitions are used to make an object transition between multiple states and they are a core function of adding interactivity and animation to your scenes. A transition is an action of an event.

<Video src="https://cdn.spline.design/_assets/docs/8d5547c7-0ada-436a-b971-1be4bb304c26.mp4" />

### Creating a new Transition Action [#creating-a-new-transition-action]

To add a new transition you first need to create multiple states of your object and add an event that will trigger the transition action.

1. Select the object to which you want to apply a transition to.
2. Create at least one new state where you’ll transition to.
3. Add an event to the object.
4. Open the Event and add a transition action.

<Callout type="idea">
  Create transitions between multiple states for more complex sequential animations.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/8343c323-4f78-48af-a8a9-74d482c32ecc.mp4" />

***

### Customizing a Transition Action [#customizing-a-transition-action]

After your states and events are created, open the ‘Edit Event’ panel to customize your transitions.

Here are the different customizable sections of a transition action:

#### Target [#target]

The target is the object where you want the transition to happen.

#### Transitions [#transitions]

In the transitions section, you can define what states the transition will go through.

As well as defining the duration and transition properties for each individual transition.

#### Sequence [#sequence]

The sequence properties will affect the whole sequence defined in the Transitions section.

* **Delay** - how many seconds the sequence should wait before it’s played.
* **Loop Settings** - Count - for specific loop amount, Infinite - for looping forever.
* **Cycle** - If the sequence should return to its original starting point.

<Image src="https://cdn.spline.design/_assets/docs/d55f3ddc-cb97-478d-b666-d4c2c6c52b72.png" alt="image" maxWidth="300" />

#### Transition Properties [#transition-properties]

When pressing the transition curve between states, you can open the properties of each individual transition.

* **Transition Curve** - Linear, Ease, Ease In, Ease Out, Ease In Out, Bezier, Spring.
* **Duration** - Transition duration in seconds from ‘State A’ to ‘State B’.
* **Delay** - how many seconds the animation should wait before it’s played.
* **Loop Settings** - Count - for specific loop amount, Infinite - for looping forever.
* **Cycle** - If the transition should return to its original starting point.

<Image src="https://cdn.spline.design/_assets/docs/b6ae72ae-9069-4dc8-8dcf-08a987b25bda.png" alt="image" maxWidth="300" />

<Embed src="https://my.spline.design/spheressequentialcopy-1633f2db27cb608f0f8717391a2620d1/" title="Spline Embed" height="384" />

> *Sequential Transitions in action! ☝️ Drag to Orbit*
