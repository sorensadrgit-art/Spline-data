# Cavity Layer (/materials-shading/surface-detail/cavity-layer)

> Bring out an object's shape by shading its ridges and recesses.



The **Cavity Layer** shades an object according to the curvature of its surface:
raised edges get one treatment, recessed areas another. It's what makes carved
detail, panel gaps and sculpted forms legible instead of flattening out under even
lighting.

Useful on sculpted meshes, imported CAD parts and anything with fine surface detail
that isn't reading clearly.

***

## Adding the layer [#adding-the-layer]

Select an object, then in the **Material*&#x2A; section of the inspector click &#x2A;*+** and
choose **Cavity**.

***

## Controls [#controls]

| Control    | What it does                                                  |
| ---------- | ------------------------------------------------------------- |
| **Ridge**  | How strongly raised edges and convex areas are picked out     |
| **Valley** | How strongly recesses, creases and concave areas are darkened |

Both can be used on their own. Valley alone reads as accumulated grime or ambient
shadow in the recesses; Ridge alone catches the light on the edges, like wear on a
raised lip.

***

## Tips [#tips]

* **Start with Valley.** Darkening recesses does more for readability than
  brightening ridges, and it's closer to how real surfaces age.
* **Keep it subtle.** High values on both look like an outline filter rather than
  surface shading.
* **It reads shape, not lighting.** The effect stays consistent as you move lights
  around, which makes it a dependable way to keep detail visible in a dim scene.
* Pairs well with the [Dust Layer](https://docs.spline.design/materials-shading/surface-detail/dust-layer.md) — dust on the
  upward faces, grime in the recesses.
