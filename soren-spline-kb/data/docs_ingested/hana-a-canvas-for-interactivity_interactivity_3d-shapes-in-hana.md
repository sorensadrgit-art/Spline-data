# 3D Shapes in Hana (/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana)



The 3D Shape effect lets you lift any 2D shape into 3D space with a single step, giving flat vector shapes depth, volume, and lighting instantly. Your original 2D shape remains fully editable, and any changes you make update the 3D form in real time.
It introduces a groundbreaking step in the design workflow — making 3D creation as fast and intuitive as working with 2D shapes.

This effect lives in the **Effects** panel and works with any shape layer, making it easy to add 3D shapes to your designs.

<Embed src="https://www.youtube.com/embed/Jsdl0fsn764" title="YouTube video player" />

***

## Adding the 3D Shape Effect [#adding-the-3d-shape-effect]

1. Select any shape on the canvas.
2. On the **Inspector** panel on the right, scroll to **Effects**.
3. Press &#x2A;*+** to add an effect and change it to **3D Shape**.
4. The effect appears in your Effects list, where it can be enabled/disabled or reordered.

<Image src="https://docs.spline.design/media/3d-shape-effect.png" alt="3D Shape effect added in the Effects tab" />

***

## 3D Shape Settings [#3d-shape-settings]

After enabling the 3D Shape effect, you’ll see properties you can adjust:

### Geometry [#geometry]

The Geometry controls define the underlying 3D shape created by the 3D Shape effect. These settings determine the object’s extrusion, smoothness, beveling, and how the final mesh is constructed.

* **Geometry** – Selects the base mesh type (e.g., *Custom*). This defines how the shape is generated. It can be Custom, which uses your 2D vector shapes, or you can pick set 3D objects like a Sphere or a Torus.

* **Scale** – Adjusts the overall size of the extruded 3D geometry.

* **Depth** – Controls how far the original 2D shape extrudes into 3D space.

* **Center** – Determines whether the extrusion expands outward from the center.
  * *Yes* - keeps the shape centered
  * *No* - extrudes in one direction

* **Bevel Size** – Sets the thickness of the beveled edge. Higher values create softer, rounder edges.

* **Bevel Type** – Controls the bevel profile (e.g., *Round*, *Flat*, etc.).

* **Bevel Sides** – Sets the number of segments used to smooth the bevel. More sides produce smoother curves but can also have performance impact.

* **Smooth Angle** – Determines how shading transitions across angled surfaces. Higher values reduce visible hard edges.

* **Subdivision** – Increases mesh resolution for smoother results. Higher values improve quality at the cost of performance.

### Transform [#transform]

Transform controls modify the rotation and perspective of the 3D Shape.

* **Rotation (X, Y, Z)** – Rotates the extruded object around each axis.

* **Perspective** – Adds perspective skew, enhancing the sense of depth or camera tilt.

### Material [#material]

These settings define how the surface reacts to lighting, reflection, transparency, and refraction.

* **Roughness** – Controls surface glossiness.
  * Lower values = shiny
  * Higher values = matte

* **Metalness** – Adds metallic reflectivity, making the material behave like metal.

* **Reflectivity** – Adjusts how strongly the object reflects the environment and light sources.

* **Glass** – Introduces transparency and subtle refraction effects for glass-like materials.

* **Aberration** – Adds chromatic aberration, creating color fringing along edges.

* **Thickness** – Sets the internal thickness of transparent materials, affecting refraction intensity.

* **Refraction** – Controls how much light bends through glass-like surfaces.

* **Blur** – Softens reflections for frosted or diffused surfaces.

### Fresnel [#fresnel]

The Fresnel effect adds a highlight around the edges of the object based on its viewing angle.
When turned on, additional Fresnel parameters become available (intensity, scale, color, etc).

### Environment Map [#environment-map]

Environment Maps provide image-based lighting and reflections using an HDRI texture.

* **Image** – Selects the HDRI environment used for lighting and reflections. You can upload your own or pick one from the presets.

* **Rotation (X, Y, Z)** – Rotates the environment image to control how reflections and lighting appear on the object.

### Light [#light]

Light controls define how the object responds to directional and ambient lighting.

* **Intensity** – Sets the brightness of the main light source.

* **Color** – Defines the color of the main light.

* **Shadow Color** – Determines shadow tint.
  * *Auto* - generates a color automatically
  * *Custom* - allows manual selection

* **Ambient Intensity** – Controls the amount of ambient light in the scene.

* **Ambient Color** – Sets the color of the ambient light.

* **Height** – Moves the light source up or down in the scene.

* **Direction** – Rotates the light direction, affecting where highlights and shadows fall.

### Tonemapping [#tonemapping]

Enables or disables **Tonemapping** for the selected object or effect.\
Tonemapping adjusts how exposure, brightness, and contrast are rendered, and can help achieve more balanced or stylized visuals.

***

## Interactivity [#interactivity]

All 3D Shape parameters are fully interactive and can be controlled through Hana's events and actions system. This means properties like Depth, Bevel Size, Smoothness, Rotation, Material settings, and more can respond to user input in real time.

With interactivity enabled, you can:

* Animate 3D Shapes with state transitions
* Adjust 3D Shape properties on hover (e.g., increase depth or bevel for a pressed-in effect)
* Trigger changes on click (e.g., animate rotation or material highlights)

This opens the door to creating dynamic 3D interactions — using the same editable 2D shapes as your starting point.

<Video src="https://docs.spline.design/media/3d-magical-shapes.webm" />

***

## Performance Notes [#performance-notes]

3D Shape is optimized for real-time rendering.\
However, using many high-detail shapes with large bevels or high smoothness may increase GPU load, especially on mobile and lower end devices.

***

## Summary [#summary]

The **3D Shape** effect brings easy, intuitive depth to your designs in Hana.\
Whether you're building UIs, interactive experiences, or stylized graphics, 3D Shape gives you accessible control over dimensional appearance without requiring complex modeling.
