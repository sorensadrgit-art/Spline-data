# PBR Materials (/materials-shading/basics/pbr-materials)

> Physically based materials in Spline — roughness, metalness and texture maps, and how to bring a PBR material set in from another tool.



**PBR** — physically based rendering — is the shading model most 3D tools share.
Instead of describing a surface with ad-hoc highlight settings, you describe what
it's *made of*: how rough it is, whether it's metal, and which texture maps carry
that detail per-pixel. The renderer works out how light should behave.

In Spline this lives in the [Lighting Layer](https://docs.spline.design/materials-shading/shading-and-reflection/lighting-layer.md)
of a material. Set that layer's mode to **Physical** and you're working with a
PBR surface.

<Callout type="idea">
  PBR materials need something to reflect. A metal in a scene with no environment
  has nothing to pick up and reads as flat grey — pair these materials with an
  [environment or HDRi](https://docs.spline.design/lighting/environment-and-hdri.md).
</Callout>

***

## The two dials that matter most [#the-two-dials-that-matter-most]

| Control       | What it does                                                                                                                                               |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Roughness** | How scattered reflections are. Low is a mirror or polished metal; high is chalk, rubber or unfinished wood                                                 |
| **Metalness** | Whether the surface behaves like metal. Metals take their color from what they reflect; non-metals keep their own color and reflect the environment on top |

Most real-world looks come from these two alone. **Reflectivity** tunes how
strongly a non-metal surface reflects — or use **IOR** (index of refraction) with
**Specular** for the physically-stated version of the same thing, which is what
glass, water and gemstone values are usually quoted as.

***

## Texture maps [#texture-maps]

Any of the dials above can be driven per-pixel by an image instead of a single
value. That's what a downloaded or authored material set gives you:

| Map              | What it carries                                                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Rough Map**    | Per-pixel roughness — worn patches, polished edges, smudges                                                                          |
| **Metal Map**    | Which parts of the surface are metal                                                                                                 |
| **Normal Map**   | Surface detail as direction data, for dents and grain that catch light without extra geometry. **Normal Scale** adjusts the strength |
| **Bump Map**     | The simpler height-based alternative to a normal map                                                                                 |
| **AO Map**       | Baked ambient occlusion — contact shadows in crevices. **AO Intensity** dials it back                                                |
| **Emissive Map** | Which parts glow, with **Emissive** for the color and **Emissive Power** for the strength. Push it past 1 and it blooms              |

### Packed textures [#packed-textures]

Material sets often pack three maps into one image — occlusion in red, roughness
in green, metalness in blue. Each map has a **Channel** selector (Luminance, Red,
Green, Blue, Alpha) so you can point all three at the same image and read a
different channel for each, with no need to split it into separate files first.

***

## Beyond the basics [#beyond-the-basics]

Some surfaces need more than roughness and metalness, and the Physical mode has
dedicated lobes for them:

* **Clearcoat** and **Coat Rough** — a thin glossy layer over the base, like car
  paint, lacquered wood or a screen behind glass.
* **Sheen** and **Sheen Rough** — the soft rim of light on fabric: velvet,
  satin, brushed cloth.
* **Iridescence** — color that shifts with viewing angle, like a soap bubble,
  beetle shell or oil slick.

Each stays inactive until you touch it, so a material only carries what it
actually uses.

<Callout>
  PBR texture maps and the extended lobes above render on the **WebGPU** pipeline.
  Set your scene's **Renderer** accordingly before publishing — see
  [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).
</Callout>

***

## Bringing materials in from other tools [#bringing-materials-in-from-other-tools]

If you import a **glTF or GLB** whose materials are already metallic-roughness —
what Blender, Substance, Houdini and most asset libraries export — Spline
recognizes it and wires the maps up for you, packed channels included. You land
on a Physical lighting layer with the base color, roughness, metalness, normal
and occlusion already connected.

[How to Import Content](https://docs.spline.design/importing-content/how-to-import-content.md),
[CAD to Spline: optimization best practices](https://docs.spline.design/importing-content/cad-to-spline-optimization-best-practices.md)

***

## Where to go next [#where-to-go-next]

[Creating Material Layers](https://docs.spline.design/materials-shading/basics/creating-material-layers.md),
[Lighting Layer](https://docs.spline.design/materials-shading/shading-and-reflection/lighting-layer.md),
[Bump Map & Roughness Map](https://docs.spline.design/materials-shading/surface-detail/bump-map-roughness-map.md),
[Reflection Layer](https://docs.spline.design/materials-shading/shading-and-reflection/reflection-layer.md),
[Environment & HDRi](https://docs.spline.design/lighting/environment-and-hdri.md),
[AI Textures](https://docs.spline.design/spline-ai/ai-textures.md)
