# Frame as Fill 3D Meshes (/hana-a-canvas-for-interactivity/interactivity/frame-as-fill-3d-meshes)



The **Frame as Fill** option lets you use an existing frame as the visual content for any shape. Instead of applying a flat color, gradient, image, or video directly, you can reference a frame and display its live content on another shape.

This is especially powerful when combined with the **3D Shape** effect, allowing you to project UI, images, video, or animated content onto 3D meshes.

<Video src="https://cdn.spline.design/docs/videos/1770041389065-frame-as-fill.mp4" />

### Using a Frame as Fill [#using-a-frame-as-fill]

You can apply a frame as fill from the **Fill** panel:

1. Select a shape on the canvas.
2. Go to the **Fill** panel in the right sidebar.
3. In the fill type options, choose **Frame**.
4. Pick which frame you want to use as the source.
5. The selected frame’s content will appear inside your shape.

The shape now acts as a viewport for that frame, showing whatever is inside it.

### Working with 3D Shape Effect [#working-with-3d-shape-effect]

When you combine **Frame as Fill** with the **3D Shape** effect:

* Apply the **3D Shape** effect to your shape.
* Set the shape’s **Fill** type to **Frame** and select a frame that contains your UI, image, or video.
* The frame content will be mapped onto the 3D surface, making it appear as if the mesh has that interface or media applied to it.

This is useful for:

* Displaying app or website UIs on 3D devices or panels.
* Showing videos or motion content on 3D screens.
* Presenting dynamic frames (like carousels or interactive layouts) on 3D cards or surfaces.

### Live Content & Updates [#live-content--updates]

Because the fill references a frame:

* Any changes you make inside the source frame (text, images, animations, states) will automatically update in realtime everywhere that frame is used as a fill.
* You can reuse the same frame as fill across multiple shapes to keep different views in sync.

### Tips & Best Practices [#tips--best-practices]

* Use dedicated frames for content you plan to reuse as fills (for example, *App Screen*, *Video Frame*, or *Dashboard UI*).
* Keep source frames organized and named clearly so they’re easy to find in the **Frame** fill selector.
* For complex 3D layouts, start by designing your UI inside a regular frame, then apply it as fill to your 3D shapes for better control and iteration.
