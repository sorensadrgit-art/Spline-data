# Cloner Motion (/designing-in-3-d/animation/cloner-motion)



The Cloner enables you to duplicate and arrange objects via certain patterns or based on the shape of another object.

It’s also possible to randomize them and easily create a generative movement as seen in the video above.

<Video src="https://cdn.spline.design/_assets/docs/67c7a07e-fc2e-4245-a103-90e4e3cefcce.mp4" />

## Enable Cloner Modifier [#enable-cloner-modifier]

1. Select the object you want to clone
2. Find the Modifiers Panel on the properties sidebar
3. Press the "+" button and choose Cloner

All `Cloner` and `Randomness` parameters can be animated via state change to achieve procedural motion

<Image src="https://cdn.spline.design/_assets/docs/cloner-modifier.png" alt="image" />

***

## Cloning Types [#cloning-types]

The following types are available in Cloner: Radial, Linear, Grid, and Object. Each type allows the generation of a different pattern. Each type can be randomized by turning on the Randomness.

### Radial [#radial]

Radial type is a perfect start to create clones along a circle.

<Image src="https://cdn.spline.design/_assets/docs/c7644ceb-6f22-4ed1-9fcb-b82a4a1cc836.png" alt="image" />

* **Base** → Ability to show or hide the original cloned object.
* **Count** → Amount of clones to be created.
* **Radius** → Size of the radius.
* **Start/End** → Allows to define a circular sector, it’s set to a full circle by default.
* **Alignment** → Aligns the clones to the radius if active.
* **Axis** → set the orientation of the Radial Clones based on X/Y/Z
* **Transform** (Position, Scale, Rotation) → Modify the transform values of the clones (the base object will keep the original transform).

### Linear [#linear]

Linear type is a simple clone in one direction based on the base object’s direction.

<Image src="https://cdn.spline.design/_assets/docs/119cf8a1-455f-4e69-ae7c-06cd78019d86.png" alt="image" />

* **Base** → Ability to show or hide the original cloned object.
* **Count** → Amount of clones to be created.
* **Transform** (Position, Scale, Rotation) → Modify the transform values of the clones (the base object will keep its original values).

### Grid [#grid]

Grid type is able to clone objects along a 2D or 3D grid.

<Image src="https://cdn.spline.design/_assets/docs/f264f502-42fd-4727-bc09-22f67e5887bd.png" alt="image" />

* **Base** → Ability to show or hide the original cloned object.
* **Count** → Amount of clones to be created along each axis of the grid (X, Y, Z).
* **Transform** (Position, Scale, Rotation) → Modify the transform values of the clones (the base object will keep its original values).
* **Size** → Spacing between the clones can be defined for each axis (X, Y, Z).
* **Use center** → Base object can be aligned to the center of the grid or it can be the initial object in the clone sequence.

### Object [#object]

Object type can create more advanced results where clones can be aligned along the surface of another object.

<Image src="https://cdn.spline.design/_assets/docs/5c9ee758-1eb0-4c67-bf1c-93f62bc43a61.png" alt="image" />

* **Base** → Ability to show or hide the original cloned object.
* **To object** → Select the reference object based on which the clones will be created.
* **Count** → For Random, the spread type it’s defining the number of clones to be created. For the Polygon center, Edge, and Vertex spread types, the number of clones can be defined via percentages from 0 to 100.
* **Spread** → &#x2A;*Defines the distribution of the clones on the “*To object*”. The following types are available:**
  * **Random** → Randomly places the clones on the surface of the “*To object*”.
    * **Seed** → Set an arbitrary number to generate various random patterns.
  * **Polygon center** → Places the clones on the polygons of the “*To object*”.
  * **Edge** → Places the clones on the center of the “*To object*” edges.
  * **Vertex** → Places the clones on the vertices of the “*To object*”.
* **Align** → Set to “Normal” will be aligned to the “*To object*” normals. By setting it to “*Axis*” it will be based on the selected world axis.
  * **Axis** → Preferred axis for both “Normal” and “Axis” Align types (X, X-, Y, Y-, Z, Z-)
* **Transform** (Position, Scale, Rotation) → Modify the transform values of the clones (the base object will keep its original values).

***

## Randomness [#randomness]

<Image src="https://cdn.spline.design/_assets/docs/56956a11-9e0a-42f6-a66b-bca4a2917925.png" alt="image" />

If Cloner is turned on, `Randomness` can be applied below the Cloner to modify the cloner with random parameters. Randomness works with all Cloner types (Radial, Linear, Grid, Object).

The following parameters can be adjusted in Randomness:

* **Strength** → How strong the Randomness should be applied. If set to 0, randomness won’t be visible.
* **Noise** → Noise can be set to Perlin or Simplex. Perlin noise has higher contrast for more drastic effects.
* **Transform** → X, Y, and Z values can be randomized for Position, Rotation, and Scale. Try to play around with these values to achieve diverse results.
* **Seed** → Set an arbitrary number to generate various random patterns.
* **Movement** → Applies movement for the noise of the randomness which creates motion for the cloned objects.
* **Scale** → Adjust the value to amplify the size of the applied noise.

<Callout>
  Pro tip: To achieve procedural motion animate these values with state-based animations.
</Callout>

> [How state-based animation works](https://docs.spline.design/interaction-states-events-and-actions/concepts/how-state-based-animation-works.md)
