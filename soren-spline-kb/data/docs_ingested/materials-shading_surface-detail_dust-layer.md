# Dust Layer (/materials-shading/surface-detail/dust-layer)

> Settle dust, snow or grime onto the upward-facing surfaces of an object.



The **Dust Layer** adds a colour to the surfaces of an object that face upwards,
the way dust, snow or ash settles in the real world. Steep and downward-facing
surfaces stay clear.

It's the fastest way to make an object look weathered or a scene look cold, without
painting a texture or adding geometry.

***

## Adding the layer [#adding-the-layer]

Select an object, then in the **Material*&#x2A; section of the inspector click &#x2A;*+** and
choose **Dust**.

***

## Controls [#controls]

| Control         | What it does                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Color**       | The colour of the settled dust — white for snow, grey for dust, dark for grime                                                     |
| **Coverage**    | How far down the sides the effect reaches. Low values leave only the flattest faces covered; high values creep down steeper slopes |
| **Softness**    | How sharply the covered area gives way to the bare surface. Low is a crisp snow line, high is a gradual fade                       |
| **Noise**       | Breaks up the edge so it isn't a perfectly even band                                                                               |
| **Noise Scale** | The size of that variation — small for fine grain, large for patchy drifts                                                         |

***

## Tips [#tips]

* **Snow:** white, high coverage, low softness, a little noise for a natural edge.
* **Dust on a shelf or machine:** light grey, low coverage, high softness.
* **Grime in crevices:** try the [Cavity Layer](https://docs.spline.design/materials-shading/surface-detail/cavity-layer.md)
  instead — it targets recesses rather than upward faces, and the two stack well.
* The effect follows the object's **orientation in the scene**, so rotating the
  object moves the dust to whatever now faces up.
