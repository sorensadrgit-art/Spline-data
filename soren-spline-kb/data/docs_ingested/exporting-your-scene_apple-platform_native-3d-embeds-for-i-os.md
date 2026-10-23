# Native 3D Embeds for iOS (/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os)



With our Metal-based renderer, you can now embed native 3D content in your SwiftUI projects.

This native renderer enables you to bring all of the interactivity from your 3D designs made in Spline to Apple devices. It also takes full advantage of all the native performance in your Apple devices like the iPhone, iPad, or Mac.

<Embed src="https://www.youtube.com/embed/7l8LPgz47Zk" title="YouTube video player" />

## Requirements [#requirements]

Follow the steps below to get set up to use the Spline iOS Runtime.

### 1. Sign up for an Apple ID or join the Apple Developer Program [#1-sign-up-for-an-apple-id-or-join-the-apple-developer-program]

* To get started testing your app on your devices, you’ll need a free [Apple ID](https://appleid.apple.com/).
* To publish your app on the App Store, you need to register with the [Apple Developer Program](https://developer.apple.com/).

For more information about the differences between an Apple ID and Apple Developer Program membership, refer to Apple’s documentation on [Choosing a Membership](https://developer.apple.com/support/compare-memberships/).

**Team IDs**

In order for you to build your apps within Xcode, you might need a Team ID.

Learn how to find your Team ID on Apple’s documentation: [Locate your Team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

### 2. Download and Install Xcode [#2-download-and-install-xcode]

<Callout>
  The minimum Xcode version supported is **16.3**
</Callout>

To use Spline native embeds, you’ll need to integrate the Spline iOS Runtime into an Xcode project. This means you must install Xcode if you want to build an iOS application. Xcode is only available for macOS.

* Download the latest version of Xcode from the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835).
* Download the latest or beta versions of Xcode from the [Apple Developer website](https://developer.apple.com/xcode/).

## Getting Started [#getting-started]

Follow the steps below to get started using native 3D embeds on your Swift projects with Spline iOS Runtime.

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

### 1. Adding the Spline iOS Runtime package to Xcode [#1-adding-the-spline-ios-runtime-package-to-xcode]

To add via Swift Package Manager, in Xcode, select **File** > **Add Package Dependency**.

In the package finder, select the search input and search using the full repository URL: [https://github.com/splinetool/spline-ios](https://github.com/splinetool/spline-ios)

<Image src="https://cdn.spline.design/_assets/docs/8525f622-c205-465f-84ef-855f680d6922.png" alt="image" />

For more information, refer to Apple’s documentation on [Adding package dependencies to your app](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app)

### 2. Importing the Spline iOS Runtime [#2-importing-the-spline-ios-runtime]

To import the Spline iOS Runtime, make sure to always add the following code to the top of the file where Spline Runtime is used.

```swift
import SplineRuntime
```

### 3. Using the Spline iOS Runtime [#3-using-the-spline-ios-runtime]

#### 3.1 Exporting from Spline [#31-exporting-from-spline]

1. From the top toolbar, press the `Export` button to open the export panel;
2. Under Mobile Platform select `Apple`, and then the `Embed` option.

Make sure to come back to the export panel and press the `Update` button to see all the updates made to the scene in your app.

To load your Spline scene locally, you can use the `Download` button below the code snippet.

To export for Apple Platforms, you’ll need an active **Pro** or **Max** subscription.

<Image src="https://cdn.spline.design/_assets/docs/5b10360c-4495-4eac-a19a-2e63e2c492db.png" alt="image" maxWidth="600" />

#### 3.2 Integrating with your Xcode Project [#32-integrating-with-your-xcode-project]

#### From the Cloud [#from-the-cloud]

1. Copy the code snippet and paste it into your `ContentView` Swift file;

```swift
import SplineRuntime
import SwiftUI

struct ContentView: View {
	var body: some View {
		// // fetching from local
		// let url = Bundle.main.url(forResource: "scene", withExtension: "splineswift")!

		// fetching from cloud
		let url = URL(string: "https://build.spline.design/nDkzGcy787CUJYaEI-gy/scene.splineswift")!

		SplineView(sceneFileURL: url).ignoresSafeArea(.all)
	}
}
```

* If not using local files, you can either keep the `fetching from local` code commented or remove it completely.
* Use `.ignoresSafeArea(.all)` if you want to show your experience on full-screen without the title bars.
* When working with multiple cloud embeds, you can use the same code snippet and change the URL after the `string`.

#### Locally [#locally]

1. Use the Download button below the code snippet to get a local copy of your Spline Scene as a `.splineswift` file;
2. Import the `.splineswift` file into your Xcode project’s root folder;
3. Copy the code snippet and paste it into the `ContentView`;
4. Comment out the `fetching from cloud` code and uncomment the fetching from local code.

```swift
import SplineRuntime
import SwiftUI

struct ContentView: View {
	var body: some View {
		// fetching from local
		let url = Bundle.main.url(forResource: "scene", withExtension: "splineswift")!

		// fetching from cloud
		// let url = URL(string: "https://build.spline.design/nDkzGcy787CUJYaEI-gy/scene.splineswift")!

		SplineView(sceneFileURL: url).ignoresSafeArea(.all)
	}
}
```

* When working with multiple local files, you can change the file name after `forResource`. If the file name is `scene.splineswift` the code should look like: `forResource: "scene"`

#### 4. Publishing and distributing your app [#4-publishing-and-distributing-your-app]

For more information on publishing to the App Store, refer to Apple’s documentation on [Distributing your app for beta testing and releases](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).

## Download Xcode Demo [#download-xcode-demo]

See how it works by downloading an Xcode demo project using cloud iOS embeds.

[File](https://ucarecdn.com/c9244d1b-5d79-410c-9920-d469b8dbb18e/)

**Get Started with the following steps:**

1. On Xcode, go to File > Open and select the unzipped folder with your project;
2. Select your build device – you can use your physical device (iPhone, iPad, Mac) or a simulator;
3. Press ▶️ to build your project.

**Before Building**

1. You might need to go into `Signing & Capabilities`, and under `Signing` **add your team manually**.
2. Optionally, make sure to change the `Bundle Identifier` to a unique one.

**3D Scenes:**

* Avatar 1: [https://app.spline.design/file/a2770bba-eb91-4dce-9cec-44857322d7ad](https://app.spline.design/file/a2770bba-eb91-4dce-9cec-44857322d7ad)
* Avatar 2: [https://app.spline.design/file/5f77c44e-411e-4420-93ac-438fe058c4ae](https://app.spline.design/file/5f77c44e-411e-4420-93ac-438fe058c4ae)
* Avatar 3:[https://app.spline.design/file/30f38922-2b3f-488e-bc78-14dd25fd2ba1](https://app.spline.design/file/30f38922-2b3f-488e-bc78-14dd25fd2ba1)

<Video src="https://cdn.spline.design/_assets/docs/731f0d67-ee48-48aa-b518-f5e5b82a18de.mp4" />

## Possible Warnings [#possible-warnings]

When building your app, even if the app builds properly, there are a few errors that might be displayed on the embed. Refer below to see the warnings and their explanation.

<Callout>
  *"Spline scene file is in an unknown format."*
</Callout>

The exported file is too old, the runtime is too old, or the file might have become corrupted.

<Callout>
  *"Spline scene file URL could not be reached."*
</Callout>

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

## Generate an App [#generate-an-app]

Another way to export your 3D content for Apple Platforms like iOS is by generating a pre-built Xcode project directly from Spline.

Learn more about [iOS App Generation](https://docs.spline.design/exporting-your-scene/apple-platform/i-os-app-generation.md).
