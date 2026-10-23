# Events & Interactivity (/interaction-states-events-and-actions/concepts/events-interactivity)



<Callout>
  Events enable you to change an [object state](https://docs.spline.design/interaction-states-events-and-actions/concepts/how-state-based-animation-works.md) based on your input to the Viewport; this is similar to how CSS or JS events work (if you are familiar with these terms).
</Callout>

Events are how you can trigger actions like transitions to have animation and interactivity.

#### Spline Events [#spline-events]

To learn more about each specific event, see its page:

* [Start Event](https://docs.spline.design/interaction-states-events-and-actions/events/start-event.md)
* [Mouse Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-up-event.md)
* [Mouse Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-down-event.md)
* [Mouse Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-press-event.md)
* [Mouse Hover Event](https://docs.spline.design/interaction-states-events-and-actions/events/mouse-hover-event.md)
* [Key Up Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-up-event.md)
* [Key Down Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-down-event.md)
* [Key Press Event](https://docs.spline.design/interaction-states-events-and-actions/events/key-press-event.md)
* [Scroll Event](https://docs.spline.design/interaction-states-events-and-actions/events/scroll-event.md)
* [Look At Event](https://docs.spline.design/interaction-states-events-and-actions/events/look-at-event.md)
* [Follow Event](https://docs.spline.design/interaction-states-events-and-actions/events/follow-event.md)
* [Game Controls Event](https://docs.spline.design/interaction-states-events-and-actions/events/game-controls-event.md)
* [Distance Event](https://docs.spline.design/interaction-states-events-and-actions/events/distance-event.md)
* [State Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/state-change-event.md)
* [Variable Change Event](https://docs.spline.design/interaction-states-events-and-actions/events/variable-change-event.md)
* [Collision Event](https://docs.spline.design/interaction-states-events-and-actions/events/collision-event.md)
* [Drag and Drop Event](https://docs.spline.design/interaction-states-events-and-actions/events/drag-and-drop-event.md)
* [Trigger Area Event](https://docs.spline.design/interaction-states-events-and-actions/events/trigger-area-event.md)
* [Screen Resize Event](https://docs.spline.design/interaction-states-events-and-actions/events/screen-resize-event.md)
* [API Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event.md)
* [Webhook Called Event](https://docs.spline.design/interaction-states-events-and-actions/events/webhook-called-event.md)
* [AI Assistant Listener Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-listener-event.md)
* [AI Assistant Trigger Event](https://docs.spline.design/interaction-states-events-and-actions/events/ai-assistant-trigger-event.md)

***

## Creating your first Event & Action [#creating-your-first-event--action]

1. Select the object you want to add a new event to.
2. Go to the Events panel on the right sidebar and click the `+` icon.
3. Open the Event created and if necessary, use the top dropdown to switch to a different event type.
4. Create a new action by choosing one of the options available in the empty state.
5. From the Target dropdown, choose the object you want to target for the event.
6. In the Transitions section, you can build your sequence of transitions between different states.

You can now play around with the rest of the settings and preview your animation by entering Play Mode.

<Video src="https://cdn.spline.design/_assets/docs/e8389604-8924-456b-bef3-161ec8cb3a63.mp4" />

*Example: Creating a "Start" Event cycling and looping with a "Spring" transition curve.*

Here is a live example of the above.

<Embed src="https://my.spline.design/HMMfOZl8imhZ7slGwLPdAKn9/" title="Spline Embed" height="384" />

> *Click & Drag 👆 – A "Start" Event cycling and looping with a "Spring" transition curve.*
