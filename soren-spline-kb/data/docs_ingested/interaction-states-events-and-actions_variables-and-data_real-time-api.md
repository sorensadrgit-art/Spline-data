# Real-time API (/interaction-states-events-and-actions/variables-and-data/real-time-api)



The Real-time API feature in Spline allows you to integrate external services, retrieve or send data, and automate responses based on events. This enables dynamic and interactive experiences within your Spline projects.

<Embed src="https://www.youtube.com/embed/ga6R8qDqLHo" title="YouTube video player" />

***

## Creating a New API item [#creating-a-new-api-item]

<Image src="https://cdn.spline.design/_assets/docs/16bb6e8b-1716-4a7d-8dc0-eb05887e47b8.png" alt="image" />

1. Navigate to the **Variables & Data Panel** on the right sidebar of Spline editor (accessible when nothing is selected in editor).
2. Click on the **APIs** tab.
3. Click on **New API** to create a new API item.

## Configuring an API [#configuring-an-api]

Select the way you would like to communicate with the API, from the following options

* **GET**: Retrieve data.
* **POST**: Send data.
* **DELETE**: Remove data.
* **PUT**: Update data.
* **HEAD**: Retrieve headers only.
* **OPTIONS**: Describe allowed methods.
* **PATCH**: Apply partial modifications.

<Image src="https://cdn.spline.design/_assets/docs/caf63f02-8e33-42ff-b998-e9ae5a145d47.png" alt="image" maxWidth="500" />

**API URL:** add in the URL of your API

**Request on Start:** Choose whether the API request should automatically start when the scene loads (Yes or No).

**Headers:** Add necessary headers by entering the Key and Value. Use the “+” icon to add multiple headers.

<Image src="https://cdn.spline.design/_assets/docs/ef5deedf-c406-4e7f-bd08-12532b224614.png" alt="image" maxWidth="600" />

***

## Response handling [#response-handling]

**Preview**: The API response can be previewed directly within the Response tab.

**Refresh**: Click the refresh button to retrieve the latest response from the API.

***

## Using an API response in Spline [#using-an-api-response-in-spline]

#### API Updated Event [#api-updated-event]

This event triggers when the API receives a response. Learn more about:

[API Updated Event](https://docs.spline.design/interaction-states-events-and-actions/events/api-updated-event.md)

#### API Request Action [#api-request-action]

You can trigger an API request based on specific events, such as the start of the scene, a mouse click, or any other custom event. Learn more about:

[API Request Action](https://docs.spline.design/interaction-states-events-and-actions/actions/api-request-action.md)

#### Using Variables with APIs [#using-variables-with-apis]

When using APIs, the data retrieved can be stored in variables, which can then be used to dynamically update properties within your Spline project. Here’s how you can leverage variables:

* **Set Variables from API Response:** You can map the response data to specific variables (e.g., Numbers, Strings, Booleans). For example, if your API returns a temperature value, you can store this value in a **Number** variable.
* **Update Object Properties**: Variables can be attached to object properties such as position, scale, or color. For instance, if you receive a new position from the API, you can update the object’s position dynamically.
* **Trigger Actions Based on Variables**: Use the **Variable Change Event** to trigger actions when the API updates the variables. For example, if an API updates a String variable with new text, you can automatically update a text label in your scene.

***

## Practical Use Cases [#practical-use-cases]

<Callout>
  APIs provide endless possibilities for integrating external services into your Spline projects, enabling you to create highly customized and dynamic experiences. Depending on the provider you choose to integrate with, the functionality can vary widely. Here are some examples:
</Callout>

* **Dynamic Weather Display**:
  * Use a weather API to retrieve real-time weather data.
  * Store the temperature in a Number variable and display it on a text object.
  * Use Variable Change Events to trigger visual changes, such as modifying the transforms of objects in your scene to reflect changes in weather conditions.
* **Live Scoreboard**:
  * Integrate a sports API to fetch live scores.
  * Update the score in real-time using variables and display it on the scoreboard.
  * Trigger animations when a new score is received.
* **General API Integrations**:
  * Connect with services like **Airtable** to manage and display dynamic data in your scene.
  * Use **OpenAI** to generate text dynamically, providing real-time updates based on AI-generated responses.
  * Integrate with any other REST API to fetch or send data, allowing for virtually limitless possibilities in terms of what your Spline project can achieve.

***

## Best Practices [#best-practices]

* **Testing**: Test your API configuration thoroughly to ensure it works as expected.
* **Optimization**: Minimize the number of API calls by using the Request on Start option only when necessary.
* **Warning**: Never share sensitive information, such as API keys or authorization tokens, publicly. Ensure that these details are securely stored and used only within a protected environment.
