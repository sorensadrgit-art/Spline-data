# Code API for Kotlin (/exporting-your-scene/android/code-api-for-kotlin)



The **Code API** allows you to seamlessly integrate interactive 3D experiences into your projects, offering greater control and customization. It enables you to trigger actions, modify object properties, and create dynamic, responsive 3D environments directly from your existing code and user interface.

<Embed src="https://www.youtube.com/embed/2dFCRFg3d3o" title="YouTube video player" />

<Callout>
  **Important**: The Code API allows your native interface to control properties in the Spline scene, and vice versa. However, it's important to note that this is different from the Real-time APIs feature. For information about APIs used for server communication and integrating your scenes with other apps, please refer to the specific API documentation: [Real-time API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api.md)
</Callout>

## Key capabilities [#key-capabilities]

* **Event Listeners**: React to real-time events within your 3D scenes.
* **Adjust Properties**: Dynamically update position, scale, rotation, and more.
* **Trigger Transitions**: Create transitions and animations based on events.
* **Adjust variables:** Retrieve and update variables in a Spline scene.

## Usage [#usage]

### Getting started [#getting-started]

First, make sure you're familiar with [Native 3D Embeds for Android](https://docs.spline.design/exporting-your-scene/android/native-3d-embeds-for-android.md) and you can already embed 3D content in your Android projects.

```kotlin
@Composable
fun SplineScene() {
    AndroidView(
        factory = { ctx ->
            val view = SplineView(context = ctx)
            view.loadResource(R.raw.scene)
            view
        },
        modifier = Modifier
            .fillMaxWidth()
            .fillMaxHeight()
    )
}
```

To access the API, use the `loadResource` or `loadUrl` callback which is invoked once the scene has finished loading:

```kotlin
@Composable
fun SplineScene() {
    AndroidView(
        factory = { ctx ->
            val view = SplineView(context = ctx)
            view.loadResource(R.raw.scene) {
                // Scene is loaded, you can now use the API
                val obj = view.findObjectByName("Cube")
                Log.d("Spline", "Found object: ${obj?.name}")
            }
            view
        },
        modifier = Modifier
            .fillMaxWidth()
            .fillMaxHeight()
    )
}
```

<Callout>
  **Info:** The `SplineView` loads its content asynchronously, so API calls may return `null` or do nothing if the scene hasn't finished loading. Always use the `onComplete` callback to ensure the scene is ready before accessing the API.
</Callout>

### Read and modify Spline objects [#read-and-modify-spline-objects]

You can query any Spline object in the scene via `findObjectByName()` or `findObjectById()` functions. Then, you can read or write any of its properties.

*(You can get the ID of the object from the right-click context panel on the object in the Spline Editor).*

```kotlin
view.loadResource(R.raw.scene) {
    val cube = view.findObjectByName("Cube")

    // Read properties
    val currentPosition = cube?.position
    Log.d("Spline", "Position: ${currentPosition?.x}, ${currentPosition?.y}, ${currentPosition?.z}")

    // Modify properties
    cube?.position = Vector3(currentPosition!!.x + 100f, currentPosition.y, currentPosition.z)
    cube?.rotation = Vector3(0f, 45f, 0f)
    cube?.scale = Vector3(2f, 2f, 2f)
    cube?.visible = false
}
```

The function returns `null` if an object with the specified name was not found.

### Listen to events [#listen-to-events]

You can listen to any Spline Event you set in the Events panel of the editor by attaching a listener to the view. You can find a list of all of the Spline Event listeners in the *API* section.

```kotlin
view.loadResource(R.raw.scene) {
    view.addEventListener(SplineEventName.mouseDown) { event ->
        Log.d("Spline", "Mouse down on: ${event.target.name}")

        if (event.target.name == "Cube") {
            // Handle cube click
            event.target.visible = false
        }
    }

    view.addEventListener(SplineEventName.mouseUp) { event ->
        Log.d("Spline", "Mouse up on: ${event.target.name}")
    }
}
```

### Trigger Spline events from outside [#trigger-spline-events-from-outside]

You can trigger any animation Event you set in the Events panel in the Spline Editor. You can use the `emitEvent()` function, passing the event type and the name or ID of your object.

*(You can get the ID of the object from the right-click context panel on the object).*

```kotlin
view.loadResource(R.raw.scene) {
    // Trigger event by object name
    view.emitEvent(SplineEventName.mouseDown, "Cube")

    // Or trigger event in reverse
    view.emitEventReverse(SplineEventName.mouseDown, "Cube")
}
```

Or you can query the spline object first, and then trigger the event:

```kotlin
view.loadResource(R.raw.scene) {
    val cube = view.findObjectByName("Cube")
    cube?.emitEvent(SplineEventName.keyUp)

    // Or in reverse
    cube?.emitEventReverse(SplineEventName.keyUp)
}
```

You can find a list of all of the Spline Events you can pass to the `emitEvent()` function in the Spline Events section.

### Handling multiple views [#handling-multiple-views]

If you have several `SplineView`'s in your Android view hierarchy, each view is independent and has its own API. Simply keep a reference to each view to control them separately.

```kotlin
@Composable
fun MultipleSplineScenes() {
    var cubesView: SplineView? = null
    var spheresView: SplineView? = null

    Column {
        AndroidView(
            factory = { ctx ->
                val view = SplineView(context = ctx)
                cubesView = view
                view.loadResource(R.raw.cubes)
                view
            },
            modifier = Modifier.weight(1f).fillMaxWidth()
        )

        AndroidView(
            factory = { ctx ->
                val view = SplineView(context = ctx)
                spheresView = view
                view.loadResource(R.raw.spheres)
                view
            },
            modifier = Modifier.weight(1f).fillMaxWidth()
        )

        Button(onClick = {
            cubesView?.emitEvent(SplineEventName.keyUp, "Cube1")
        }) {
            Text("Go Cube")
        }

        Button(onClick = {
            spheresView?.emitEvent(SplineEventName.keyUp, "Sphere1")
        }) {
            Text("Go Sphere")
        }
    }
}
```

### Updating scene variables [#updating-scene-variables]

If you set up variables in your Spline scene from the editor, you can change them from code after the scene is loaded.

<Callout>
  **Note:** If in the Spline Editor you have multiple variables with the same name, only the first one will be updated, so make sure to give unique names to the variables you want to update.
</Callout>

```kotlin
view.loadResource(R.raw.scene) {
    // Check if variable exists
    if (view.hasVariable("opacity")) {
        // Set variables by type
        view.setNumberVariable("opacity", 0.5f)
        view.setBooleanVariable("isActive", true)
        view.setStringVariable("label", "Hello World")

        // Get variable values
        val opacity = view.getNumberVariable("opacity")
        val isActive = view.getBooleanVariable("isActive")
        val label = view.getStringVariable("label")
    }
}
```

### Playback control [#playback-control]

You can pause and resume the scene rendering and animations:

```kotlin
view.loadResource(R.raw.scene) {
    // Pause after 5 seconds
    Handler(Looper.getMainLooper()).postDelayed({
        view.stop()
    }, 5000)

    // Resume after 10 seconds
    Handler(Looper.getMainLooper()).postDelayed({
        view.play()
    }, 10000)
}
```

### Customizing the scene [#customizing-the-scene]

You can customize certain scene properties like zoom level and background color:

```kotlin
view.loadResource(R.raw.scene) {
    // Set camera zoom (1.0 is default, > 1 zooms in, < 1 zooms out)
    view.setZoom(2.0f)

    // Set background color (RGBA values from 0.0 to 1.0)
    val color = Color.valueOf(0.0f, 1.0f, 0.0f, 1.0f) // Green background
    view.setBackgroundColor(color)
}
```

## API [#api]

### SplineView Methods [#splineview-methods]

You can call all these different methods on the `SplineView` instance.

| Name                                 | Description                                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| loadResource(id, onComplete)         | Load a Spline scene from a raw resource file. The callback is invoked when loading is complete.                                                 |
| loadUrl(url, onComplete)             | Load a Spline scene from a URL. The callback is invoked when loading is complete.                                                               |
| addEventListener(event, callback)    | Add an event listener for Spline events.                                                                                                        |
| removeEventListener(event, callback) | Remove a previously added event listener.                                                                                                       |
| emitEvent(event, nameOrUuid)         | Triggers a Spline event associated to an object with the provided name or UUID. Starts from the first state to the last state.                  |
| emitEventReverse(event, nameOrUuid)  | Triggers a Spline event associated to an object with the provided name or UUID in reverse order. Starts from the last state to the first state. |
| findObjectById(uuid)                 | Searches through the scene's children and returns the object with that UUID.                                                                    |
| findObjectByName(name)               | Searches through the scene's children and returns the first object with that name.                                                              |
| setZoom(zoom)                        | Sets the camera zoom, expects a number value > 0 where 1 is base zoom.                                                                          |
| setNumberVariable(name, value)       | Updates value for passed number variable by name.                                                                                               |
| getNumberVariable(name)              | Get current value for a specific number variable from its name.                                                                                 |
| setBooleanVariable(name, value)      | Updates value for passed boolean variable by name.                                                                                              |
| getBooleanVariable(name)             | Get current value for a specific boolean variable from its name.                                                                                |
| setStringVariable(name, value)       | Updates value for passed string variable by name.                                                                                               |
| getStringVariable(name)              | Get current value for a specific string variable from its name.                                                                                 |
| hasVariable(name)                    | Check if a variable with the given name exists in the scene.                                                                                    |
| stop()                               | Stop/Pause all rendering, controls and events.                                                                                                  |
| play()                               | Play/Resume rendering, controls and events.                                                                                                     |
| setBackgroundColor(color)            | Manually sets the scene/canvas background color with a Color value.                                                                             |

### SplineObject Properties and Methods [#splineobject-properties-and-methods]

After retrieving a Spline Object with `findObjectById()` or `findObjectByName()`, there are a variety of properties and methods you can use.

| Name                    | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| uuid                    | Gets object UUID.                                           |
| name                    | Gets / Sets object name.                                    |
| visible                 | Gets / Sets object visibility.                              |
| position                | Gets / Sets object position as Vector3.                     |
| rotation                | Gets / Sets object rotation as Vector3.                     |
| scale                   | Gets / Sets object scale as Vector3.                        |
| intensity               | Only for light objects. Gets / Sets the light intensity.    |
| emitEvent(event)        | Force trigger an event defined in Spline Editor.            |
| emitEventReverse(event) | Force trigger an event defined in Spline Editor in reverse. |

### Spline Events [#spline-events]

These are all the Spline event types that you can pass to the `addEventListener()`, `emitEvent()` and `emitEventReverse()` functions.

| **Name**                       | **Description**                               |
| ------------------------------ | --------------------------------------------- |
| **SplineEventName.mouseUp**    | Refers to the Spline `Mouse Up` event type    |
| **SplineEventName.mouseDown**  | Refers to the Spline `Mouse Down` event type  |
| **SplineEventName.mousePress** | Refers to the Spline `Mouse Press` event type |
| **SplineEventName.mouseHover** | Refers to the Spline `Mouse Hover` event type |
| **SplineEventName.keyUp**      | Refers to the Spline `Key Up` event type      |
| **SplineEventName.keyDown**    | Refers to the Spline `Key Down` event type    |
| **SplineEventName.keyPress**   | Refers to the Spline `Key Press` event type   |
| **SplineEventName.start**      | Refers to the Spline `Start` event type       |
| **SplineEventName.lookAt**     | Refers to the Spline `Look At` event type     |
| **SplineEventName.follow**     | Refers to the Spline `Follow` event type      |
