# AI Assistant Listener Event (/interaction-states-events-and-actions/events/ai-assistant-listener-event)



The AI Assistant Listener event is used in conjunction with the [AI Voice Assistant API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/ai-voice-assistant-api.md) and it's an event that is constantly listening for changes in the audio spectrum of the AI Assistant.

***

## AI Assistant Listener Event Properties [#ai-assistant-listener-event-properties]

Since this event is designed to work with the AI Assistant’s audio spectrum, it is only compatible with **Set Variable** actions. You can use a **Set Variable** action to apply the audio spectrum to one of your variables or modify any other variables that depend on the audio spectrum.

You can then use those variables to manipulate properties of your objects like position, rotation, scale, etc.

### Frequency [#frequency]

In frequency, you can select different ways of using the voice audio waves.

**Average** - Uses an average value from all the frequencies.

**Range** - Uses the average of a range of frequencies.

**Single** - Uses a single frequency.

<Image src="https://cdn.spline.design/_assets/docs/7265a2dc-0bcd-4859-b277-6d9823c362de.png" alt="image" maxWidth="300" />

Learn more about related topics:

* [AI Voice Assistant API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/ai-voice-assistant-api.md)
* [Variables](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/variables.md)
