# Reflection Layer (/materials-shading/shading-and-reflection/reflection-layer)

> Reflect the surrounding scene in a surface — a polished floor, a mirror, wet ground.



The **Reflection Layer** makes a surface reflect the rest of your scene. Use it for
polished floors, wet ground, glossy tabletops and mirrors.

Unlike the [Glass Layer](https://docs.spline.design/materials-shading/shading-and-reflection/glass-layer.md), which is about seeing
*through* a surface, this is about seeing the scene bounced *off* it.

<Callout>
  Reflections render on the **WebGPU** graphics pipeline. On a browser without WebGPU
  support, which falls back to WebGL, the layer will not appear — so set your scene's
  **Renderer** accordingly before publishing.
  See [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).
</Callout>

***

## Adding the layer [#adding-the-layer]

Select an object, then in the **Material*&#x2A; section of the inspector click &#x2A;*+** and
choose **Reflection**.

***

## Choosing a Surface mode [#choosing-a-surface-mode]

The **Surface** control is the first decision, because it changes what the
reflection can show:

| Mode       | Use it for                                | What it can show                                                  |
| ---------- | ----------------------------------------- | ----------------------------------------------------------------- |
| **Shape**  | Any geometry — curved, irregular, sloped  | Whatever is visible on screen                                     |
| **Mirror** | Flat surfaces: floors, walls, still water | A true reflection, including things the camera can't see directly |

**Shape** works on anything and is the right default. It reflects what's currently on
screen, so an object's hidden underside, or something just off the edge of the frame,
won't appear in the reflection.

**Mirror** is a genuine reflection rendered from the mirrored viewpoint, so it *can*
show an object's underside in a floor, or scenery outside the frame. It's meant for
flat surfaces.

<Callout type="warn">
  **One Mirror surface per scene.** If several objects use Mirror, the largest one gets
  the true reflection and the rest fall back to Shape. Plan for a single hero
  reflective surface — a floor or a water plane — rather than several.
</Callout>

***

## Controls [#controls]

| Control        | What it does                                                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Blur**       | Softens the reflection. Raise it for brushed metal, polished concrete or a rough wet surface; keep it at zero for a clean mirror |
| **Thickness**  | How thick the reflecting surface reads as being                                                                                  |
| **Steps**      | How far the reflection searches through the scene. Higher catches more distant detail at more cost                               |
| **Steps Size** | How finely it searches. Smaller is more accurate, larger is cheaper and can skip thin objects                                    |
| **Tracing**    | The search method — **Linear** or **Hi-Z**. Hi-Z generally holds up better over long distances                                   |

**Blur**, **Thickness**, **Steps**, **Step Size** and **Tracing** apply to the
**Shape** mode. A Mirror surface renders a true reflection and doesn't need them.

***

## Tips [#tips]

* **Blur does the heavy lifting.** Perfectly sharp reflections read as artificial in
  most scenes; a little blur is usually more convincing and cheaper.
* **If a reflection has gaps or streaks**, raise **Steps** or reduce **Step Size** —
  that's the search missing geometry.
* **Reflections cost performance.** On a scene that's slowing down, reduce Steps
  first. See
  [How to optimize your scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md).
* **Wet ground:** a dark base colour, moderate blur and a low roughness surface gets
  you most of the way there.
