# Spline Mirror for visionOS (/exporting-your-scene/apple-platform/spline-mirror-for-vision-os)



<Callout>
  Exporting for Apple Platforms like visionOS and iOS is currently in **BETA** and under development.
</Callout>

Spline Mirror for visionOS allows you to experience your 3D content made in Spline spatially on the Apple Vision Pro — a complementary step to your workflow of exporting 3D designs for Apple Platforms like visionOS and iOS.

<Image src="https://cdn.spline.design/_assets/docs/aa98ee93-5e64-4362-a604-e44b3f505ad2.png" alt="image" />

## Spatial Design with Spline [#spatial-design-with-spline]

During the design process, you can experience your 3D content on the device to validate your 3D models, materials, animations, and interactions.

Once your scene is ready, you can integrate it into your Xcode projects with a Swift code snippet or with App Generation.

Learn more about [Native 3D Embeds for iOS](https://docs.spline.design/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os.md) and [iOS App Generation](https://docs.spline.design/exporting-your-scene/apple-platform/i-os-app-generation.md).

## Download Spline Mirror for visionOS [#download-spline-mirror-for-visionos]

Download the latest version of Spline Mirror for visionOS from the Apple App Store.

[→ ](https://apps.apple.com/us/app/spline-mirror/id6477194143)[Download on the App Store](https://apps.apple.com/us/app/spline-mirror/id6477194143)

### Required Specifications [#required-specifications]

Spline is using the latest technologies to render 3D content on Apple devices.

| Device     | Minimum Required OS   | Minimum Required Chip |
| ---------- | --------------------- | --------------------- |
| Vision Pro | visionOS 1.0 or later | M2                    |

## Getting started with Spline Mirror for visionOS [#getting-started-with-spline-mirror-for-visionos]

### 1. Log in or Sign up to Spline [#1-log-in-or-sign-up-to-spline]

To get started, you need to log in to your Spline account. If it’s your first time trying Spline, you can sign up from the Vision Pro, but you’ll need to access the Spline Editor to edit or create new scenes.

<Image src="https://cdn.spline.design/_assets/docs/f8fd98b8-a92e-418e-a2a6-50abeb38daa7.png" alt="image" />

### 2. Browse scenes from the Spline Library [#2-browse-scenes-from-the-spline-library]

If you haven’t exported any scenes for Apple Platforms, you can always open and experience examples from the Spline Library or visit the `Library` tab.

<Image src="https://cdn.spline.design/_assets/docs/c53d6a39-0ea5-42d2-8fe4-a32dd09f6042.png" alt="image" />

<Image src="https://cdn.spline.design/_assets/docs/8189db27-b2c8-41b5-9ee3-f7e50d789a68.png" alt="image" />

### 3. How to export for Apple Platforms and visionOS [#3-how-to-export-for-apple-platforms-and-visionos]

If it’s your first time using Spline Mirror for visionOS or exporting for Apple Platforms, you won’t see any scenes on the `Recents` tab. You’ll need to use the Spline Editor on a desktop to create and export your scenes.

<Callout>
  Embeds support for Volumes and Immersion mode is coming soon. You can use Spline Mirror to see how it works now.
</Callout>

To export your scene for Spline Mirror for visionOS from the Spline Editor, follow the steps below.

1. From the top toolbar, press the `Export` button to open the export panel;
2. Under Apple Platforms, select the `visionOS` option.
3. Select a View Mode. (Window, Volume, or Immersive)
4. Choose to show or hide the logo.
5. Press the `Update` button at the bottom.

<Image src="https://cdn.spline.design/_assets/docs/50e3b2ad-57ad-474a-a73f-f19f691fc2e7.png" alt="image" maxWidth="600" />

### 4. Browse your exported scenes [#4-browse-your-exported-scenes]

After exporting your scene from the Spline Editor for Apple Platforms and visionOS, the `Recents` tab is where you can find them.

<Image src="https://ucarecdn.com/e07c1356-80c7-4bd0-98fb-f487b90bd15c/" alt="Note: Currently, only scenes from ‘My Files’ are visible on your" />

*Note: Currently, only scenes from ‘My Files’ are visible on your Recents tab.*

### 5. Open and experience a 3D Scene [#5-open-and-experience-a-3d-scene]

To experience a scene from your `Recents` tab or from the `Library` tab, you can simply press it.

When opening a scene on the Apple Vision Pro, you can experience it in 3 different spatial content types: `Windows`, `Volumes`, and `Spaces`.

<Image src="https://ucarecdn.com/51e892f6-8d41-457a-8264-2e79d87533b8/" alt="A visual representation of" />

*A visual representation of Windows, Volumes, and Spaces, in that order.*

A visual representation of `Windows`, `Volumes`, and `Spaces`, in that order.

By default, your scene will open as a `Window`, but from the toolbar below, you can open your scene as a `Volume` or in immersive mode as a `Space`.

<Image src="https://cdn.spline.design/_assets/docs/46aafed6-3049-4c43-994e-bc61d359587c.png" alt="image" />

#### Windows [#windows]

`Windows` can display content on a flat surface and use 2D and 3D content.

You can use Spline Apple embeds on `Windows` the way you use them for your normal apps in iOS/iPadOS.

The Spline scenes in a `Window` can be complemented with native UI using SwiftUI.

<Image src="https://cdn.spline.design/_assets/docs/a7245fc8-1ff2-482a-9152-0f52a9b76a17.png" alt="image" />

#### Volumes [#volumes]

`Volumes` are 3D containers that can be rendered in your space alongside `Windows`.

They exist within a bounding box whose size can be customized to fit your needs. You can deploy multiple `Volumes` within a `Space`, which can coexist with `Windows` or even be anchored to them.

<Image src="https://cdn.spline.design/_assets/docs/972517e9-3df8-46fd-a0fa-e8ff7c12211b.png" alt="image" />

#### Spaces [#spaces]

For an immersive experience, apps can occupy the full `Space`, where the app's content expands around you.

Within a `Space`, applications can leverage `Windows`, `Volumes`, and even unbounded 3D content to create truly unique 3D experiences.

<Image src="https://cdn.spline.design/_assets/docs/4fd5b3e6-0f15-4616-98d8-516e7d5f375f.png" alt="image" />

<Callout>
  For more information about the differences between all the spatial content types and other relevant design guidelines, refer to Apple’s documentation on [Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos).
</Callout>

## Feature Support Roadmap [#feature-support-roadmap]

Here is a list of each feature's current status. This list will be updated weekly until everything is fully supported.

| **Feature**         | **Status** | **Notes**                                                                                                                                            |
| ------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Shapes              | ✅          | Subdivs are baked.                                                                                                                                   |
| Materials           | ✅          | Cavity Layer, Dust Layer, and Reflection Layer are not supported yet. Only Fresnel, Color, Matcap, Texture, Depth are supported in visionOS Volumes. |
| Events & States     | ✅          | AI Assistant Events are not supported yet.                                                                                                           |
| Physics             | ✅          |                                                                                                                                                      |
| Game Controls       | ✅          |                                                                                                                                                      |
| Variables           | ✅          |                                                                                                                                                      |
| Post-Processing     | ✅          | Ambient Shadows are not supported yet.                                                                                                               |
| Particles           | ✅          |                                                                                                                                                      |
| Animated Models     | ✅          |                                                                                                                                                      |
| Multi Scenes        | ✅          |                                                                                                                                                      |
| Shape Blend         | ✅          |                                                                                                                                                      |
| Align to Path       | ✅          |                                                                                                                                                      |
| Decals              | 🚧         |                                                                                                                                                      |
| Hair                | 🚧         |                                                                                                                                                      |
| Timeline Animations | 🚧         |                                                                                                                                                      |

***

## Integrate your production-ready 3D content into your Xcode Projects [#integrate-your-production-ready-3d-content-into-your-xcode-projects]

Export your 3D content for Apple Platforms like iOS and visionOS by using native embeds with a Swift code snippet.

[Native 3D Embeds for iOS](https://docs.spline.design/exporting-your-scene/apple-platform/native-3d-embeds-for-i-os.md)

Export your 3D content for Apple Platforms like iOS and visionOS by generating a pre-built Xcode project directly from Spline.

[iOS App Generation](https://docs.spline.design/exporting-your-scene/apple-platform/i-os-app-generation.md)
