# Native 3D Embeds for Android (/exporting-your-scene/android/native-3d-embeds-for-android)



With our Vulkan-based renderer, you can embed native 3D content in your Android projects.

This native renderer enables you to bring all of the interactivity from your 3D designs made in Spline to Android devices and take full advantage of their native performance.

<Embed src="https://www.youtube.com/embed/mGpqmV-gJmA" title="YouTube video player" />

## Requirements [#requirements]

Follow the steps below to get set up to use the Spline Android Runtime.

### 1. Download and Install Android Studio [#1-download-and-install-android-studio]

<Callout>
  We recommend that you use the latest stable version of Android Studio.
</Callout>

To use Spline native embeds, you’ll need to integrate the Spline Android Runtime into a Kotlin or Java project. This means you must install Android Studio to build an Android application. Android Studio is available on Windows and Mac.

* Download the latest versions of Android Studio from the [Android Developer website](https://developer.android.com/studio).

## Getting Started [#getting-started]

Follow the steps below to get started using native 3D embeds on your Kotlin or Java projects with Spline Android Runtime.

### Platform Support [#platform-support]

<Callout>
  We recommend Android 10.0+
</Callout>

Spline is using the latest technologies to render 3D content on Android devices.

It runs on Phones, Tablets, Wear OS, Desktop, TV, and Automotive from &#x2A;*Android 7.0 and up, but we recommend using Android 10.0+. Vulkan support is required.**

### Language and Libraries Support [#language-and-libraries-support]

The Spline Android Runtime can be used with Kotlin and Java.

### Android Studio Simulator [#android-studio-simulator]

The performance on the Android Studio simulator is not representative of the performance of the 3D scene on the final app running on physical devices. Depending on your development hardware, the Android simulator sometimes uses only the CPU (lower) or GPU (faster) for rendering graphics. However, the 3D scenes on your device will always use the GPU.

### 1. Adding the Spline Android Runtime [#1-adding-the-spline-android-runtime]

Open your project's `build.gradle.kts` file, and add this line of code under dependencies.

Copy

```kotlin
implementation("design.spline:spline-runtime:+")
```

*Note: This will always run the latest version of the runtime.*

After making changes on your `build.gradle.kts` file, make sure to press the `Sync Now` button to apply the changes.

<Image src="https://cdn.spline.design/_assets/docs/4588d7f1-76e8-4d16-8c86-1ecb351d0030.png" alt="image" />

You can find Spline’s Android runtime hosted on Maven: [https://central.sonatype.com/artifact/design.spline/spline-runtime/overview](https://central.sonatype.com/artifact/design.spline/spline-runtime/overview)

For more information, refer to Android’s documentation on [Adding dependencies to your app](https://developer.android.com/build/dependencies#kts).

### 2. Importing the Spline Android Runtime [#2-importing-the-spline-android-runtime]

To import the Spline Android Runtime, make sure to always add the following code to the top of the file where the Spline Runtime is used.

```kotlin
import design.spline.runtime.SplineView
```

For cloud embeds, you’ll need to allow your app to have internet access. To do so, you can add these two lines of code to your `AndroidManifest.xml` file inside `your-app-name/manifests`.

```kotlin
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

<Image src="https://cdn.spline.design/_assets/docs/c3487fd9-c60c-4687-97d0-53d8ab5b8b3c.png" alt="image" />

### 3. Using the Spline Android Runtime [#3-using-the-spline-android-runtime]

#### 3.1 Exporting from Spline [#31-exporting-from-spline]

1. From the top toolbar, press the `Export` button to open the export panel;
2. Under Android Platform, select the `Embed` option.

Make sure to come back to the export panel and press the `Update` button to see all the updates made to the scene in your app.

To load your Spline scene locally, you can use the `Download the scene to local` button below the code snippet.

<Image src="https://cdn.spline.design/_assets/docs/cabbbf27-266c-4e9a-97dc-b092bec9c29f.png" alt="image" maxWidth="600" />

#### 3.2 Integrating with your Android Studio Project [#32-integrating-with-your-android-studio-project]

Since the embedded code snippet utilizes AndroidView, ensure you include the following line in the file where you are embedding your Spline scene.

```kotlin
import androidx.compose.ui.viewinterop.AndroidView
```

#### From the Cloud [#from-the-cloud]

1. Copy the code snippet and paste it on the `MainActivity.kt` file or wherever you’d like to embed the Spline scene.

```kotlin
import design.spline.runtime.SplineView

@Composable
fun MyView() {
    AndroidView(
        factory = { ctx ->
            SplineView(ctx).apply {
				// fetching from cloud
                loadUrl("https://build.spline.design/nDkzGcy787CUJYaEI-gy/scene.splinecontent")

				// fetching from local
				// loadResource(R.raw.scene)
            }
        }
    )
}
```

* If not using local files, you can either keep the `fetching from local` code commented or remove it completely.

#### Locally [#locally]

1. Use the Download button below the code snippet to get a local copy of your Spline Scene as a `.splinecontent` file;
2. Import the `.splinecontent` file into your Android Studio project’s `your-app-name/res/raw` folder;
3. Copy the code snippet and paste it on the `MainActivity.kt` file or wherever you’d like to embed the Spline scene.;
4. Comment out the `fetching from cloud` code and uncomment the `fetching from local` code.

```kotlin
import design.spline.runtime.SplineView

@Composable
fun MyView() {
    AndroidView(
        factory = { ctx ->
            SplineView(ctx).apply {
				// fetching from cloud
	      // loadUrl("https://build.spline.design/nDkzGcy787CUJYaEI-gy/scene.splinecontent")

				// fetching from local
				loadResource(R.raw.scene)
            }
        }
    )
}
```

* When working with multiple local files, you can change the file name in `R.raw.[file-name]`. If the file name is `demo.splinecontent` the code should look like: `R.raw.demo`
* For more information on adding resources to your project, refer to Android’s documentation on [App Resources](https://developer.android.com/guide/topics/resources/providing-resources).

#### 4. Publishing and distributing your app [#4-publishing-and-distributing-your-app]

For more information on publishing to the Google Play Store, refer to Android’s documentation on [Publishing your app](https://developer.android.com/studio/publish).

## Feature Support Roadmap [#feature-support-roadmap]

Here is a list of each feature's current status. This list will be updated weekly until everything is fully supported.

| **Feature**         | **Status** | **Notes**                                                                          |
| ------------------- | ---------- | ---------------------------------------------------------------------------------- |
| Shapes              | ✅          | Subdivs are baked.                                                                 |
| Materials           | ✅          | Cavity Layer, Dust Layer, Reflection Layer, and Video Layer are not supported yet. |
| Events & States     | ✅          | AI Assistant Events are not supported yet.                                         |
| Physics             | ✅          |                                                                                    |
| Game Controls       | ✅          |                                                                                    |
| Variables           | ✅          |                                                                                    |
| Post-Processing     | ✅          |                                                                                    |
| Particles           | ✅          |                                                                                    |
| Animated Models     | ✅          |                                                                                    |
| Multi Scenes        | ✅          |                                                                                    |
| Shape Blend         | ✅          |                                                                                    |
| Timeline Animations | ✅          |                                                                                    |
| Align to Path       | ✅          |                                                                                    |
| Decals              | 🚧         |                                                                                    |
| Hair                | 🚧         |                                                                                    |

***

## Generate an APK [#generate-an-apk]

Export your 3D content for Android devices by generating an Android Package file (APK) directly from Spline.

Learn more about [Android Package (APK)](https://docs.spline.design/exporting-your-scene/android/android-package-apk.md).

## Generate an App Bundle (AAB) [#generate-an-app-bundle-aab]

Export your 3D content for Android devices by generating a pre-built Android App Bundle file (AAB) directly from Spline.

Learn more about [Android App Bundles (AAB)](https://docs.spline.design/exporting-your-scene/android/android-app-bundles-aab.md).
