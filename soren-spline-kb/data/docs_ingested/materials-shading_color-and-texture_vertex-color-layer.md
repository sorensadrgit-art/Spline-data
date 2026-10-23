# Vertex Color Layer (/materials-shading/color-and-texture/vertex-color-layer)

> Show the colours already baked into an imported model's mesh.



The **Vertex Color Layer** displays colour data stored in the mesh itself, rather
than colour you set in Spline.

Many models carry a colour per vertex — sculpts painted in ZBrush or Blender,
photogrammetry scans, point-cloud captures, or exports from CAD and generative
tools. Without this layer that data is ignored and the object renders in a single
flat colour.

***

## Adding the layer [#adding-the-layer]

Select the imported object, then in the **Material*&#x2A; section of the inspector click
&#x2A;*+** and choose **Vertex Color**.

There is nothing to configure — the layer shows what the mesh already contains.

***

## When it does nothing [#when-it-does-nothing]

If the object doesn't change, its mesh has no vertex colour data. That's common:

* **Primitives created in Spline** have no vertex colours — use a
  [Color Layer](https://docs.spline.design/materials-shading/color-and-texture/color-layer.md) or
  [Gradient Layer](https://docs.spline.design/materials-shading/color-and-texture/gradient-layer.md) instead.
* **Some formats and exports drop it.** If your model looked coloured in the tool
  you made it in, check that vertex colours were enabled on export.
* **Textured models** usually carry their colour in an image rather than in the
  mesh — use an [Image Layer](https://docs.spline.design/materials-shading/color-and-texture/image-layer.md) for those.

See [How to Import Content](https://docs.spline.design/importing-content/how-to-import-content.md) for supported
formats.

***

## Tips [#tips]

* **Stack it.** Add a [Lighting Layer](https://docs.spline.design/materials-shading/shading-and-reflection/lighting-layer.md) above it so
  the baked colours still respond to your scene's lights instead of looking flat.
* **Scans:** vertex colours are how most photogrammetry and point-cloud captures
  carry their appearance, so this is usually the first layer to add to one.
* The layer costs almost nothing to render — it's reading data the mesh already
  carries.
