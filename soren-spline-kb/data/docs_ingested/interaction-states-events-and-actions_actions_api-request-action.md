# API Request Action (/interaction-states-events-and-actions/actions/api-request-action)



The API Request Action can be triggered based on specific events, such as the start of a scene, a mouse click, or any other custom event. It will send a request to the API to retrieve the latest data.

## Creating a new API Request Action [#creating-a-new-api-request-action]

1. Select the object that you want to add the event to.
2. On the Events panel, add an event that can trigger an API request like Start, Mouse Down / Up / Press, Key Down / Up / Press, etc.
3. Open the Event and add an API Request Action.
4. Expand the API Request Action and from the drop-down list select the API you would like to request the data from.

Eg. Mouse Down Event on an object to trigger a refresh on the Weather API data.

<Image src="https://cdn.spline.design/_assets/docs/04f61211-e1be-49e9-8b95-69e1c4846fdf.png" alt="image" maxWidth="300" />

After setting up an API Request you can set up an [API Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event.md), which will check for new API updates and trigger a set of actions once the API update is complete. For example, to update the variables where you’re storing the API data.

Relevant docs related to API Updated Event:

* [Real-time API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api.md)
* [OpenAI API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/ai-text-open-ai-api.md)
* [API Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event.md)
