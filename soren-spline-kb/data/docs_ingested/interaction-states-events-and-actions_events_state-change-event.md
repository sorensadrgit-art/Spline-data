# State Change Event (/interaction-states-events-and-actions/events/state-change-event)



The State Change Event allows you to trigger actions based on the state of an object.

<Video src="https://cdn.spline.design/_assets/docs/52581247-8251-4a87-887e-ce3cf4e31dce.mp4" />

Here are the different properties of a State Change Event.

* **Object** - The object we want to check if the state has changed.
* **Changes to** - If the object gets to this state, the actions will be triggered.

In this example, if `Rectangle` changes to `State 1`, the actions under ‘Then’ will be triggered.

And if `Rectangle` changes back to any other state, the actions under ‘Else’ will be triggered.

<Image src="https://cdn.spline.design/_assets/docs/ea86a822-552f-45ab-a7cc-d9fa4f60c42a.png" alt="image" maxWidth="300" />

***

<Embed src="https://my.spline.design/BEb5KGCREZd6awNWYbibePAn/" title="Spline Embed" height="384" />

> *In this simple example, there is a State Change Event on the Pink Cube which triggers a transition on it when the Purple Cube arrives at State 1.*
