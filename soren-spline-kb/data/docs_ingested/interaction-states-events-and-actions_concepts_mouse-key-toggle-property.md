# Mouse & Key Toggle Property (/interaction-states-events-and-actions/concepts/mouse-key-toggle-property)

> Reverse an animation on the second click or key press, without building a second state.



This property allows you to easily reverse the animation of an event so each time you use a mouse or key event it’s going to switch from one state to another. This is useful to create interactions like toggle buttons.

### How to use the Toggle property in Mouse and Key events: [#how-to-use-the-toggle-property-in-mouse-and-key-events]

1. Select the object and add new states to it using the States panel. You can change the position or how it looks accordingly.
2. On the Events panels, add one of the following events that support toggle mode for the transition action: Mouse Down, Mouse Up, Key Down, Key Up, Collision, or Trigger Area.
3. Add a transition action to the Mouse Down event, and change the target object if needed.
4. Change the mode to “Toggle” - This will enable you to do the reverse when the object is clicked.
5. Add the transition steps to the action that you want to toggle between.
6. That’s it - Enter Play Mode to test.

<Embed src="https://my.spline.design/switchtutorial-70a23dd070513899912c011c202b0368/" title="Spline Embed" height="384" />

<Callout>
  *Test it! Press the switch above 👆*
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/85f41b24-1c21-4db5-aa39-6d30660429a0.mp4" />

> *Click the link to learn how to create this 3D Switch design: [Watch YouTube Tutorial](https://youtu.be/lJIDSiDlhvw?si=_3R5qCeGji_XrCoi)*
