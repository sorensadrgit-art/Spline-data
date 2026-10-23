# Webhooks (/interaction-states-events-and-actions/variables-and-data/webhooks)



Webhooks in Spline allow you to create real-time, event-driven interactions by listening for and responding to external events. By using webhooks, your Spline project can automatically trigger actions, update variables, and react to data sent from external sources, enabling dynamic and interactive experiences.

<Embed src="https://www.youtube.com/embed/ga6R8qDqLHo" title="YouTube video player" />

***

## Creating a New Webhook [#creating-a-new-webhook]

1. Navigate to the **Variables & Data Panel** on the right sidebar of Spline editor (accessible when nothing is selected in editor).
2. Select the **Webhooks** tab.
3. Click on the **New Webhook** button to create a new Webhook item.
4. Rename the Webhook, Change the default name ("New Webhook") to something more descriptive to better organize your webhooks.

***

## Configuring Webhooks [#configuring-webhooks]

* **Webhook URL**: A default webhook URL will be automatically generated. Copy this URL to integrate with external services that support Webhooks. This URL will listen for incoming data
* **Configure Parameters**: Predefine the variables your webhook will receive by clicking on the “+” icon. The supported types include Strings, Numbers, and Booleans.
* **The example code snippet** will automatically adjust based on the variables you set. You can edit the snippet to use any value you want. The snippet is just an example using Curl, but you can also use any automation tool, such as Zapier, to call the webhook.

<Image src="https://cdn.spline.design/_assets/docs/ec2b883d-f2e4-4242-b0fe-b7af961fa3f9.png" alt="image" maxWidth="600" />

***

## Using Webhooks in Spline [#using-webhooks-in-spline]

Webhooks are powerful tools that can trigger actions and update variables in real-time based on external events. Here’s how to utilize them effectively:

#### Webhook Called Event [#webhook-called-event]

This event is triggered whenever your webhook receives data from an external source.

* **Select Webhook**: Assign the specific webhook you want to monitor for incoming data.
* **Actions**: Define the actions to execute when the webhook is called. Actions could include updating variables, triggering animations, or initiating other API calls.

[Webhook Called Event](https://docs.spline.design/interaction-states-events-and-actions/events/webhook-called-event.md)

#### Using Variables with Webhooks [#using-variables-with-webhooks]

Webhook data can be mapped to variables, allowing you to dynamically update and control elements within your Spline project based on real-time data.

* **Set Variables from Webhook Data**: Map incoming webhook data to Spline variables (e.g., Numbers, Strings, Booleans). For example, if your webhook sends a temperature reading, store this value in a **Number** variable to display it in your project.
* **Update Object Properties:** Attach variables to object properties so that changes in webhook data are immediately reflected in your scene. For instance, update a text field with the latest information from the webhook or change an object’s color based on the data received.
* **Trigger Actions Based on Variables**: Use **Variable Change Events** to trigger specific actions when a webhook updates a variable. For example, when a Boolean variable (e.g., "Alert Status") is set to `true`, you could trigger an animation, alert, or change the state of an object in your scene.

***

## Practical Use Cases [#practical-use-cases]

<Callout>
  Webhooks offer endless possibilities for integrating real-time data and external events into your Spline projects. Here are some examples of how webhooks can be used:
</Callout>

* **Real-time Notifications**:
  * Use webhooks to receive real-time notifications from services like Slack, Zapier, or other custom systems.
  * Display these notifications directly within your Spline project or trigger animations based on the incoming data.
* **IoT Integration**:
  * Connect your Spline project to IoT devices via webhooks.
  * For example, update the state of objects in your scene based on data from a smart home device, such as a temperature sensor or motion detector.
* **Custom Alerts and Responses**:
  * Set up webhooks to listen for specific external events, such as changes in a database or new messages from an API, and trigger responses in your project.
  * For instance, if a webhook detects that a certain threshold has been met (like a stock price or environmental sensor reading), you can trigger a visual or audio alert in your Spline scene.

***

## Best Practices [#best-practices]

* **Test Your Webhook**: Ensure that your webhook is correctly configured and responding as expected before deploying it in a live environment. Testing helps you verify that the data is being received and processed correctly.
* **Security**: Always use secure, encrypted connections (HTTPS) for your webhook URLs. Avoid exposing sensitive information, such as authorization tokens, publicly, and ensure they are securely stored and transmitted.
* **Debugging**: Use logging and debugging tools to monitor incoming webhook data. This can help you troubleshoot issues and ensure that your actions and variable updates are functioning as intended.
