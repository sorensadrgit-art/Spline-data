# Code API for SwiftUI (/exporting-your-scene/apple-platform/code-api-for-swift-ui)



The **Code API** allows you to seamlessly integrate interactive 3D experiences into your projects, offering greater control and customization. It enables you to trigger actions, modify object properties, and create dynamic, responsive 3D environments directly from your existing code and user interface.

<Embed src="https://www.youtube.com/embed/2dFCRFg3d3o" title="YouTube video player" />

<Callout>
  **Important**: The Code API allows your native interface to control properties in the Spline scene, and vice versa. However, it’s important to note that this is different from Real-time data APIs feature. To learn more about real-time data APIs, go here [Real-time API](https://docs.spline.design/interaction-states-events-and-actions/variables-and-data/real-time-api.md)).
</Callout>

## Key capabilities [#key-capabilities]

* **Event Listeners**: React to real-time events within your 3D scenes.
* **Adjust Properties**: Dynamically update position, scale, rotation, and more.
* **Trigger Transitions**: Create transitions and animations based on events.
* **Adjust variables:** Retrieve and update variables in a Spline scene.

## Usage [#usage]

### Getting started [#getting-started]

First, make sure you’re familiar with [Native 3D Embeds for iOS](https://docs.spline.design/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os.md) and you can already embed 3D content in your SwiftUI projects.

```
struct ContentView: View {
    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url)
    }
}
```

Then, to access the API, create a **SplineController** object and pass it to **SplineView** initializer for the view you want to control.

```
struct ContentView: View {
		private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller)
    }
}
```

<Callout>
  **Info:** A controller object is only able to control a single view. Do NOT use the same controller for more views. See [**Handling multiple views**](https://docs.spline.design/exporting-your-scene/apple-platform/code-api-for-swift-ui.md#handling-multiple-views) section.
</Callout>

#### Read and modify Spline objects [#read-and-modify-spline-objects]

You can query any Spline object in the scene via `findObject(name:)` or `findObject(id:)` functions. Then, you can read or write any of its properties.

*(You can get the ID of the object from the right-click context panel on the object).*

```
struct ContentView: View {
    private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller)

        Button("Move") {
            let cube = controller.findObject(name: "Cube")
            cube?.position.y += 10
        }
    }
}
```

The function returns `nil` if an object with the specified name was not found.

Note that `SplineView` loads its content asynchronously, and so these and all other functions may return `nil` or may do nothing when the scene file still hasn’t finished loading. This is especially important when you want to access the API right at the start. For this, see the next example.

#### Listen to events [#listen-to-events]

You can listen to any Spline Event you set in the Events panel of the editor by attaching a listener to the controller. You can find a list of all of the Spline Event listeners in the *API* section.

To register event listeners when the view loads, make sure to use a `task()` or `onAppear()` modifier on the view that holds loaded content (`SplineContent`) and not the `SplineView` itself.

```
struct ContentView: View {
    private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller) { phase in
            phase.content?.task {
                controller.addEventListener(.mouseUp) { obj in
                    if obj.name == "Cube" {
                        print("Cube clicked")
                    }
                }
            }
        }
    }
}
```

#### Trigger Spline events from outside [#trigger-spline-events-from-outside]

You can trigger any animation Event you set in the Events panel in the Spline Editor. You can use the `emitEvent(_:)` function, passing the event type and the name or ID of your object.

*(You can get the ID of the object from the right-click context panel on the object).*

```
struct ContentView: View {
    private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller)

        Button("Jump") {
            controller.emitEvent(.keyUp, nameOrUUID: "Cube")
        }
    }
}
```

Or you can query the spline object first, and then trigger the event:

```
struct ContentView: View {
    private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller)

        Button("Jump") {
            let cube = controller.findObject(name: "Cube")
            cube?.emitEvent(.keyUp)
        }
    }
}
```

You can find a list of all of the Spline Events you can pass to the `emitEvent(:_)` function in the Spline Events section.

#### Handling multiple views [#handling-multiple-views]

If you have several `SplineView`'s in a SwiftUI view hierarchy, and multiple of them are using the Code API, each view must have its own `SplineController` object.

```
struct ContentView: View {
    private var cubes = SplineController()
    private var spheres = SplineController()

    var body: some View {
        let urlCubes = ...
        let urlSpheres = ...
        let urlCylinders = ...

        SplineView(sceneFileURL: urlCubes, controller: cubes)
        SplineView(sceneFileURL: urlSpheres, controller: spheres)
        SplineView(sceneFileURL: urlCylinders)

        Button("Go Cube") {
            cubes.emitEvent(.keyUp, nameOrUUID: "Cube1")
        }

        Button("Go Sphere") {
            spheres.emitEvent(.keyUp, nameOrUUID: "Sphere1")
        }
    }
}
```

#### Updating scene variables [#updating-scene-variables]

If you set up variables in your Spline scene from the editor, you can change them from code after the scene is loaded.

<Callout>
  **Note:** If in the Spline Editor you have multiple variables with the same name, only the first one will be updated, so make sure to give unique names to the variables you want to update. Also note that the values you pass to your variables will be cast into their original type (number, boolean, or string).
</Callout>

```
struct ContentView: View {
    private var controller = SplineController()

    var body: some View {
        let url = URL(string: "https://build.spline.design/4-2CGowqS9z7MGA62D-B/scene.splineswift")!

        SplineView(sceneFileURL: url, controller: controller) { phase in
            phase.content?.task {
                controller.setNumberVariable(name: "opacity", value: 25)
            }
        }
    }
}
```

## Download Xcode Demo [#download-xcode-demo]

See how it works by downloading an Xcode demo project using Spline's cloud iOS embeds and SwiftUI Code API.

[File](https://ucarecdn.com/9ef5c84f-c88b-40f7-852f-ea32668b2c04/)

<Video src="https://cdn.spline.design/_assets/docs/efccd7a1-0e44-4c26-8e19-2a6761d40398.mp4" />

**Trying out the demo:**

1. On Xcode, go to File > Open and select the unzipped folder with your project;
2. Select iPhone as the build device – you can use your physical device or a simulator;
3. Trigger the preview on Xcode or press ▶️ to build your project.

**Before Building**

1. You might need to go into `Signing & Capabilities`, and under `Signing`, **add your team manually**.
2. Optionally, make sure to change the `Bundle Identifier` to a unique one.

**3D Scene:**

* [https://app.spline.design/file/f68f548d-9f78-4eee-90ce-fc72dafca6de](https://app.spline.design/file/f68f548d-9f78-4eee-90ce-fc72dafca6de)

## API [#api]

#### Spline Controller Methods [#spline-controller-methods]

You can call all these different methods on the `SplineController` instance.

| Name                             | Description                                                                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| addEventListener(\_:callback:)   | Add an event listener for Spline events                                                                                                         |
| emitEvent(\_:nameOrUUID:)        | Triggers a Spline event associated to an object with the provided name or UUID. Starts from the first state to the last state.                  |
| emitEventReverse(\_:nameOrUUID:) | Triggers a Spline event associated to an object with the provided name or UUID in reverse order. Starts from the last state to the first state. |
| findObject(id:)                  | Searches through the scene's children and returns the object with that UUID.                                                                    |
| findObject(name:)                | Searches through the scene's children and returns the first object with that name.                                                              |
| setZoom(\_:)                     | Sets the camera zoom, expects a number value > 0 where 1 is base zoom.                                                                          |
| setNumberVariable(name:value:)   | Updates value for passed variable by name.                                                                                                      |
| setBoolVariable(name:value:)     | Updates value for passed variable by name.                                                                                                      |
| setStringVariable(name:value:)   | Updates value for passed variable by name.                                                                                                      |
| getNumberVariable(name:)         | Get current value for a specific variable from its name                                                                                         |
| getBoolVariable(name:)           | Get current value for a specific variable from its name                                                                                         |
| getStringVariable(name:)         | Get current value for a specific variable from its name                                                                                         |
| stop()                           | Stop/Pause all rendering controls and events.                                                                                                   |
| play()                           | Play/Resume rendering, controls and events.                                                                                                     |
| setBackgroundColor(\_:)          | Manually sets the scene/canvas background color with a SIMD color value.                                                                        |

#### Spline Objects Methods and Properties [#spline-objects-methods-and-properties]

After retrieving a Spline Object with `controller.findObject(id:)` or `controller.findObject(name:)`, there are a variety of properties and methods you can call on those.

| Name                  | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| name                  | Gets / Sets object name.                                    |
| uuid                  | Gets object uuid.                                           |
| position              | Gets / Sets object position.                                |
| rotation              | Gets / Sets object rotation.                                |
| scale                 | Gets / Sets object scale.                                   |
| visible               | Gets / Sets object vibility.                                |
| intensity             | Only for light objects. Used to change the light intensity. |
| emitEvent(\_:)        | Force trigger an event defined in Spline Editor.            |
| emitEventReverse(\_:) | Force trigger an event defined in Spline Editor.            |

#### Spline Events [#spline-events]

These are all the Spline event types that you can pass to the `addEventListener(:)`, `emitEvent(:)` and `emitEventReverse(_:)` functions.

| **Name**        | **Description**                               |
| --------------- | --------------------------------------------- |
| **.mouseUp**    | Refers to the Spline `Mouse Up` event type    |
| **.mouseDown**  | Refers to the Spline `Mouse Down` event type  |
| **.mousePress** | Refers to the Spline `Mouse Press` event type |
| **.mouseHover** | Refers to the Spline `Mouse Hover` event type |
| **.keyUp**      | Refers to the Spline `Key Up` event type      |
| **.keyDown**    | Refers to the Spline `Key Down` event type    |
| **.keyPress**   | Refers to the Spline `Key Press` event type   |
| **.start**      | Refers to the Spline `Start` event type       |
| **.lookAt**     | Refers to the Spline `Look At` event type     |
| **.follow**     | Refers to the Spline `Follow` event type      |
