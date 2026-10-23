# Collision Event (/interaction-states-events-and-actions/events/collision-event)



With Collision Events and Physics, it is possible to trigger events when objects hit other objects. In combination with Game Controls, you can create more interactive experiences.

### How to add a Collision Event [#how-to-add-a-collision-event]

1. For Collision Events to work, it is needed to have Physics Enabled on the environment as well as on the objects. Go to Environment settings and enable Physics, then select the object(s) to enable physics on them as well.
2. Select the object(s) and create a new event under the Events Panel.
3. Open the Collision event to start adding and tweaking actions and parameters. The following parameters can be adjusted:
   * **With -** Select with what the collision event will be triggered: *Characters* (objects with Game Control events), and *Anything* (any object of the scene).
   * **Toggle -** Allows reversing the animation of an event so each time a collision happens, the event will trigger an action and reverse it.

<Image src="https://cdn.spline.design/_assets/docs/9d844e49-09c3-48a3-8dd8-1f9d52ec3134.png" alt="image" maxWidth="300" />

<Callout>
  To learn more about the Toggle option, go to [Mouse & Key Toggle Property](https://docs.spline.design/interaction-states-events-and-actions/concepts/mouse-key-toggle-property.md).
</Callout>

#### Actions [#actions]

Similar to other events, Collision events can trigger transitions that target objects and trigger a state change with transitions, delay, cycle, and loop properties. Sound actions can play, pause, and stop sounds from Spline’s Sounds Library or your own custom sounds.

<Callout>
  *A Starter, Professional or Team subscription is needed to access Spline’s Sounds Library.*
</Callout>

Here’s how to add Collision Events to your scene.

<Video src="https://cdn.spline.design/_assets/docs/e15b5ef1-84ed-4c7c-b357-5b6fdb8170fd.mp4" />

*Adding Collision Events.*
