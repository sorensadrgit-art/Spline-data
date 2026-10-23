# Working with Fog (/cameras/working-with-fog)



Adding fog to your scene is a great way to create depth.

To start make sure there are no objects selected by pressing anywhere on the viewport.

Then go to the Fog panel on the right sidebar and enable it.

<Video src="https://cdn.spline.design/_assets/docs/54857cd4-90f2-4e3f-8ca4-f573ad658345.mp4" />

Using the same color as the background is the best way to achieve the effect of actual fog.

There's also the option to change the color for more creative freedom.

<Video src="https://cdn.spline.design/_assets/docs/b3181d66-3c25-454d-a45d-6f9653583c41.mp4" />

The **Near** and **Far** values are used to change the depth of the Fog. The closer both are to each other the thicker the Fog transition is.

<Video src="https://cdn.spline.design/_assets/docs/7eece2e7-228e-4298-85f3-49a9089403c4.mp4" />

## Fog types [#fog-types]

The panel's type switch picks how the fog is computed:

* **Linear** (the default) fades objects purely by their distance from the camera, between **Near** and **Far**. The fog looks the same from every camera angle.
* **Height** is a realistic ground fog: a fog layer that is densest at its base and thins out with altitude. Because the fog is accumulated along each view ray, a camera looking down from above sees an almost clear scene, while a camera at ground level looks through the whole layer — the way real fog behaves.
* **Both** stacks the two: a Linear distance haze on top of the Height ground layer, sharing one fog color. Use it when distant content should always melt away (even seen from above) while the ground still holds a realistic fog layer.

Height fog is controlled with three values, all in world units:

* **Distance** — roughly how far you can see through the fog at its base before objects fade out. Smaller values make a thicker fog.
* **Thickness** — how tall the fog layer is. Small values hug the fog to the ground; large values build a taller layer that takes longer to rise out of.
* **Base** — the world height (Y) of the layer's floor, where the fog is densest.
