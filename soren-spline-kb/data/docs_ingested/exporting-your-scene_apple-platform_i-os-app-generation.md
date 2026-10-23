# iOS App Generation (/exporting-your-scene/apple-platform/i-os-app-generation)



App Generation allows you to generate a pre-built Xcode project directly from Spline ready to publish in the App Store using our Metal-based renderer.

Our Metal-based renderer enables you to bring all of the interactivity from your 3D designs made in Spline to Apple devices. It also takes full advantage of all the native performance from your Apple devices like the iPhone, iPad, or Mac.

<Embed src="https://www.youtube.com/embed/7l8LPgz47Zk" title="YouTube video player" />

<Callout>
  **iOS App Generation** is a paid feature. You’ll need an active **Pro** or **Max** subscription.
</Callout>

## Requirements [#requirements]

Follow the steps below to get set up for using App Generation.

### 1. Sign up for an Apple ID or join the Apple Developer Program [#1-sign-up-for-an-apple-id-or-join-the-apple-developer-program]

* To get started testing your app on your devices you’ll need a free [Apple ID](https://appleid.apple.com/).
* In order to publish your app on the App Store, you need to register with the [Apple Developer Program](https://developer.apple.com/).

For more information about the differences between an Apple ID and Apple Developer Program membership, refer to Apple’s documentation on [Choosing a Membership](https://developer.apple.com/support/compare-memberships/).

#### Team IDs [#team-ids]

To build your apps within Xcode, you might need a Team ID.

Learn how to find your Team ID on Apple’s documentation: [Locate your Team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

### 2. Download and Install Xcode [#2-download-and-install-xcode]

<Callout>
  Current Xcode version supported from &#x2A;*15.2.**
</Callout>

To build your app with the Xcode project generated from Spline you’ll need Xcode. Xcode is only available for macOS.

* Download the latest version of Xcode from the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835).
* Download the latest or beta versions of Xcode from the [Apple Developer website](https://developer.apple.com/xcode/).

## Getting Started [#getting-started]

Follow the steps below to use native 3D embeds on your Swift projects with Spline iOS Runtime.

### Platform Support [#platform-support]

Spline is using the latest technologies to render 3D content on Apple devices.

| Device      | Minimum Required OS                                       | Minimum Required Chip |
| ----------- | --------------------------------------------------------- | --------------------- |
| iPhone      | iOS 16.0 and up                                           | A13 and up            |
| iPad        | iPadOS 16.0 and up                                        | A13 and up            |
| Mac         | macOS 13.0 and up (via Mac Catalyst or Designed for iPad) | Apple Silicon         |
| Vision Pro  | VisionOS 1.0                                              | M2                    |
| Apple TV    | Not supported                                             | -                     |
| Apple Watch | Not supported                                             | -                     |

### Language and Libraries Support [#language-and-libraries-support]

The Spline iOS Runtime uses SwiftUI and Swift.

### 1. Generate an Xcode Project from Spline [#1-generate-an-xcode-project-from-spline]

1. From the top toolbar, press the `Export` button to open the export panel;
2. Under Apple Platforms, select the `App` option;
3. Fill in all the required settings to build your Xcode project. Refer below for more information;
4. Press the Generate button.

<Image src="https://cdn.spline.design/_assets/docs/4d443c6c-e56a-456c-b128-75f111924fcc.png" alt="image" maxWidth="600" />

#### 1.1 Settings Overview [#11-settings-overview]

Refer to the below for more information on all the different settings related to App Generation.

| Setting           | Purpose                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| App Icon          | Upload a 1024x1024 image to use as your app icon.                                                                                    |
| App Name          | The name of your app or project.                                                                                                     |
| Bundle identifier | The ID of your organization or team. Best practice is to use your domain reversed. `com.mycompany`                                   |
| Version           | The version of your app.                                                                                                             |
| Team ID           | The ID of your Xcode team or organization. Refer to [Team IDs section](#team-ids) to learn more.                                     |
| Mode              | The way your Spline scenes will be embedded. - Cloud will load the scene via URL. - Local will download and use a .splineswift file. |
| Xcode version     | The Xcode version needed to open the generated project.                                                                              |
| Logo              | Enable or disable the Spline logo.                                                                                                   |
| Orientation       | Define the orientation that your app will use. When in Auto-Rotation you’ll be able to select which orientations your app can use.   |
| Status Bar        | Define if your app has the status bar visible or hidden.                                                                             |

### 2. Build and run the app with Xcode [#2-build-and-run-the-app-with-xcode]

Building the app and running it is done through Xcode and can be achieved with a few simple steps.

1. On Xcode, go to File > Open and select the unzipped folder with your project;
2. Select your build device – you can use your physical device (iPhone, iPad, Mac) or a simulator;
3. Press ▶️ to build your project.

For more information on how to build an app with Xcode, refer to Apple’s documentation on [Building and Running an App](https://developer.apple.com/documentation/xcode/building-and-running-an-app).

If you don't add a Team ID from Spline, on Xcode, you might need to go into `Signing & Capabilities`, under `Signing`, you can add your team manually.

### 3. Publishing and distributing your app [#3-publishing-and-distributing-your-app]

For more information on publishing to the App Store, refer to Apple’s documentation on [Distributing your app for beta testing and releases](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).

## Possible Warnings [#possible-warnings]

When building your app, even if the app builds properly, there are a few errors that might be displayed on the embed. Refer below to see the warnings and their explanation.

`"Spline scene file is in an unknown format."`

The exported file is too old, the runtime is too old, or the file might have become corrupted.

`"Spline scene file URL could not be reached."`

It’s displayed when the runtime fails to download a `.splineswift` file from the web. It can be because of an invalid URL, or just a non-functioning network connection.

## Feature Support Roadmap [#feature-support-roadmap]

Here is a list of each feature's current status. This list will be updated weekly until everything is fully supported.

| **Feature**         | **Status** | **Notes**                                                             |
| ------------------- | ---------- | --------------------------------------------------------------------- |
| Shapes              | ✅          | Subdivs are baked.                                                    |
| Materials           | ✅          | Cavity Layer, Dust Layer, and Reflection Layer are not supported yet. |
| Events & States     | ✅          | AI Assistant Events are not supported yet.                            |
| Physics             | ✅          |                                                                       |
| Game Controls       | ✅          |                                                                       |
| Variables           | ✅          |                                                                       |
| Post-Processing     | ✅          | Ambient Shadows are not supported yet.                                |
| Particles           | ✅          |                                                                       |
| Animated Models     | ✅          |                                                                       |
| Multi Scenes        | ✅          |                                                                       |
| Shape Blend         | ✅          |                                                                       |
| Timeline Animations | ✅          |                                                                       |
| Align to Path       | ✅          |                                                                       |
| Decals              | 🚧         |                                                                       |
| Hair                | 🚧         |                                                                       |

***

## Export Native Embeds for iOS [#export-native-embeds-for-ios]

Another way to export your 3D content for Apple Platforms like iOS, is by using native embeds with a Swift code snippet.

Learn more about [Native 3D Embeds for iOS](https://docs.spline.design/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os.md).
