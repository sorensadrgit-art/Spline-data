# Effects in Hana (/hana-a-canvas-for-interactivity/interactivity/effects-in-hana)



The **Effects Panel** in Hana adds visual enhancements like shadows, blurs and glass to shapes, text, and frames. These effects bring depth and polish to your designs.

When selecting any **shape**, **text**, or **frame**, the **Effects Panel** appears in the right-side properties panel, just below the **Fill** and **Stroke** panels. From here, you can apply and adjust multiple visual effects.

You can apply and stack multiple effects, adjusting them to fit your design needs:

### Drop Shadow [#drop-shadow]

Creates a shadow behind an object, adding depth.

* **Properties:** Offset (X, Y), Blur, Spread, Color & Opacity

***

### Inner Shadow [#inner-shadow]

Applies a shadow inside the edges of an object, creating a subtle “pressed-in” or embossed effect.

* **Properties:** Offset (X, Y), Blur, Spread, Color & Opacity

***

### Layer Blur [#layer-blur]

Blurs the entire object and its contents for a soft, out-of-focus effect.

* **Use:** Great for background elements or creating depth.

***

### Background Blur [#background-blur]

Blurs the content behind the object, perfect for a frosted-glass effect.

* **Tip:** Lower the **Fill Opacity** to reveal the background blur effect.

***

### Progressive Blur [#progressive-blur]

Both **Layer Blur** and **Background Blur** can use progressive blur. Progressive blur creates a directional blur between two points, each with its own adjustable blur value. Use the blur control line to define the direction and customize how the blur transitions across the object with Start and End values.

***

### Liquid Glass [#liquid-glass]

The **Liquid Glass** effect simulates the natural distortion, refraction, and depth of real glass surfaces. Inspired by Apple’s new **Liquid Glass** design language, it allows you to create fluid, glass-like visuals that feel dynamic and lifelike.

**Tip:** Complement the Liquid Glass effect with inner and drop shadows to help emphasize depth and light interaction.

* **Offset (X / Y):** Adjusts the position of the distortion map along the X or Y axis, controlling where the effect is applied relative to the main shape.

* **Distortion:** Controls the intensity of the warping effect, increasing or decreasing how much the content appears distorted through the glass.

* **Depth:** Defines the perceived thickness of the glass, affecting how strongly it bends light and distorts background content.

* **Blur:** Adds softness to the refracted content, simulating the blurriness of frosted or imperfect glass.

* **Aberration:** Introduces chromatic aberration (color fringing) along the glass edges or across the surface, with an option to focus this effect on the **Edge** or fill the entire **Fill** area.

* **Profile:** Shapes the distortion profile for more organic or structured refraction patterns.

* **Magnification:** Controls how much the glass "zooms in" on the background content, enhancing or reducing the lens-like effect.

***

### Noise Glass [#noise-glass]

The Noise Glass effect distorts a surface as if viewed through textured or uneven glass, creating refractive ripples and visual warping. It can be used to simulate frosted glass, water surfaces, or heat haze.

* **Noise Type** – Sets the type (**Simplex**, **Fbm**, **Voronoi**, **Sine**) of the noise pattern used for distortion.

* **Blur** – Softens the distortion to create a frosted or diffused effect.

* **Type** – **Uniform** applies the distortion evenly, while **Progressive** fades it gradually across the surface.\
  When **Progressive** is selected, additional parameters become available:

  * **Amplitude Start / End** – Define the starting and ending amplitude (strength) of the noise across the progression.
  * **Pos Start / End (X, Y)** – Set the start and end positions for the noise effect in normalized coordinates.
  * **Falloff** – Determines how the noise transitions between start and end; options include **Linear** or **Radial**.

* **Amplitude** – Controls the intensity of the distortion; negative values invert the displacement direction.

* **Scale** – Changes the size and density of the distortion pattern.

* **Stretch (X, Y)** – Stretches the distortion’s shape along specific axes.

* **Offset (X, Y)** – Moves the distortion pattern across the surface.

* **Movement** – Animates the distortion for flowing or shifting effects.

* **Seed** – Randomizes the distortion pattern while allowing consistent results when fixed.

***

### Layer Noise [#layer-noise]

The Layer Noise effect adds procedural variation to a surface, introducing organic texture or displacement. It’s useful for breaking up uniform areas, creating natural imperfections, or adding dynamic motion.

* **Noise Type** – Selects the noise algorithm (**Simplex**, **Fbm**, **Voronoi**, **Sine**), each with a different look and feel.

* **Blur** – Softens the noise edges for smoother results.

* **Type** – **Uniform** applies the noise evenly, while **Progressive** applies it gradually across the surface. \
  When **Progressive** is selected, additional parameters become available:

  * **Amplitude Start / End** – Define the starting and ending amplitude (strength) of the noise across the progression.
  * **Pos Start / End (X, Y)** – Set the start and end positions for the noise effect in normalized coordinates.
  * **Falloff** – Determines how the noise transitions between start and end; options include **Linear** or **Radial**.

* **Amplitude** – Controls the strength or displacement amount of the noise.

* **Scale** – Adjusts the size and frequency of the noise pattern.

* **Stretch (X, Y)** – Stretches or compresses the noise along the horizontal or vertical axis.

* **Offset (X, Y)** – Moves the noise pattern without changing its scale or stretch.

* **Movement** – Animates the noise pattern over time.

* **Seed** – Randomizes the noise pattern; the same seed will always produce the same result.

***

### 3D Projection [#3d-projection]

The 3D Projection effect wraps 2D layers onto a three-dimensional shape, adding depth, curvature, and realistic lighting. Use it to simulate volumetric projections, creating a more immersive scene.

* **Type** – Selects the base 3D shape to wrap the 2D layers onto. (**Sphere** or **Cylinder**)

* **Radius** – Adjusts the radius of the 3D shape.

* **Height*&#x2A; &#x2A;(For **Cylinder** only)* – Controls the vertical length of the cylinder.

* **Rotation (X, Y, Z)** – Changes the position of the wrapped layers in the 3D projection.

* **Perspective** – Controls the amount of depth distortion; higher values increase the perspective effect.

* **Wrap Area (X, Y)** – Defines the surface that is wrapped horizontally and vertically.

* **Resolution** – Sets the rendering quality of the wrapped layers.

* **Side** – Chooses whether the effect applies to the **front**, **back**, or **both** sides of the 3D shape.

* **Light** – Toggles lighting on or off.

  * **Light Intensity / Color / Shadow Color** – Controls the brightness, hue, and shadow color of the light source.
  * **Ambient Intensity / Color** – Adjusts the overall fill light and its color across the surface.
  * **Specular** – Sets the strength of reflective highlights.
  * **Light Height / Direction** – Positions the light source, affecting how highlights and shadows are cast.
