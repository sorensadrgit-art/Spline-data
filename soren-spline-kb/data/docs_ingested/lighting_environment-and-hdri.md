# Environment & HDRi (/lighting/environment-and-hdri)

> Light a scene with an HDRi image or a physical sky — image-based lighting, reflections, and the background your scene sits in.



Lights aren't the only way to illuminate a scene. The **Sky** gives your scene
an *environment*: a surrounding image that lights every surface from all
directions at once and shows up in reflections. It's what makes materials —
especially metals and glossy surfaces — read as if they're somewhere real.

You'll find it in the scene's page settings, in the **Sky** panel, with a toggle
to turn it on. There are two modes:

| Mode         | What it is                                                                                           |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| **HDRi**     | An equirectangular environment image — a studio, an interior, a landscape — wrapped around the scene |
| **Physical** | A simulated sky and atmosphere, with a sun position and weather                                      |

***

## HDRi [#hdri]

Pick an **Image** from the built-in presets — neutral and colored studios,
interiors, landscapes, gradients — or upload your own. Alongside regular image
files, `.hdr` and `.exr` files are accepted, which is what you'll get from an
HDRi library.

| Control             | What it does                                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Image**           | The environment image, from the presets or your own upload                                                              |
| **Rotation**        | Spins the environment around the scene, from 0° to 360° — use it to move highlights and reflections where you want them |
| **Blur**            | Softens the environment. Sharp environments give crisp reflections; blurred ones give smooth, diffuse light             |
| **Show BG**         | Whether the image is drawn *behind* the scene, or only used to light it                                                 |
| **Affect Lighting** | How much the environment drives the scene's lighting — see below                                                        |
| **Light Intensity** | Multiplier on that lighting                                                                                             |

<Callout type="idea">
  Turning **Show BG** off is the classic product-render setup: the environment
  still lights the scene and appears in reflections, but your flat background
  color shows behind the objects instead of a photographic skybox.
</Callout>

Presets you pick are stored in the file, so a scene stays self-contained when
you share it or hand it off.

***

## Physical [#physical]

Instead of an image, the Physical mode simulates a sky. Set the **Time** of day
to place the sun, choose a **Weather** preset from clear through to storm, and
the atmosphere and light color follow.

| Control                                  | What it does                                              |
| ---------------------------------------- | --------------------------------------------------------- |
| **Time**                                 | Time of day, which drives the sun's position              |
| **Weather**                              | Cloud-cover preset, from clear to overcast and storm      |
| **Clouds**                               | Turns the cloud layers on and off                         |
| **Wind** and **Animate Wind**            | How fast clouds drift, and whether they move in real time |
| **Weather Seed**                         | Regenerates the cloud pattern                             |
| **Exposure**                             | Overall brightness of the sky                             |
| **Affect Lighting**, **Light Intensity** | Same as HDRi — how strongly the sky lights the scene      |

***

## How environment lighting works [#how-environment-lighting-works]

With **Affect Lighting** on, the environment becomes a light source: the scene
gets a dome of light taking its color from the environment, plus a directional
light following the sun. While that's on, the scene's own **Ambient** light
steps aside — the environment dome replaces it — and comes back when you turn it
off.

The setting has three positions:

* **Off** — the environment is only a backdrop and reflections; your own lights
  do the lighting.
* **Low** — full sky-driven light, but environment reflections are limited to
  the surfaces where they're most visible, like metals and glossy materials. A
  performance dial for heavy scenes.
* **Full** — every physical material samples the environment.

<Callout>
  The Physical sky renders on the **WebGPU** pipeline. Check your scene's
  **Renderer** setting before publishing — see
  [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).
</Callout>

***

## Getting the most out of it [#getting-the-most-out-of-it]

* **Environments and PBR materials go together.** Roughness, metalness and
  reflections have nothing to reflect without an environment, which is why a
  metal object can look flat and grey in an unlit scene. See
  [PBR Materials](https://docs.spline.design/materials-shading/basics/pbr-materials.md).
* **Rotate before you add lights.** Often an environment rotation gets you the
  highlight you were about to add a light for.
* **Blur for mood, sharp for product.** A blurred environment reads as soft
  studio light; a sharp one puts recognizable detail in your reflections.
* **Combine with your own lights.** The environment handles ambient light and
  reflections; a [Directional Light](https://docs.spline.design/lighting/directional-light.md) or
  [Spot Light](https://docs.spline.design/lighting/spot-light.md) still gives you control over shadows and
  accents.

[Working with Lights](https://docs.spline.design/lighting/working-with-lights.md),
[Reflection Layer](https://docs.spline.design/materials-shading/shading-and-reflection/reflection-layer.md),
[Working with Fog](https://docs.spline.design/cameras/working-with-fog.md)
