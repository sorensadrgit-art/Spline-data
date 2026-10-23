# Hair Systems (/designing-in-3-d/animation/hair-systems)

> Add simulated hair, fur, grass or fibres that move with gravity and wind.



A **Hair System** grows thousands of simulated strands from a surface. Use it for
character hair, animal fur, grass, moss, carpet or any fibrous surface. The strands
are simulated, so they hang under gravity, sway with wind, and settle when the
object stops moving.

<Callout>
  Hair renders on the **WebGPU** graphics pipeline. On a browser without WebGPU
  support, which falls back to WebGL, hair will not appear — so set your scene's
  **Renderer** accordingly before publishing.
  See [Play Settings](https://docs.spline.design/exporting-your-scene/play-settings.md).
</Callout>

***

## Adding hair [#adding-hair]

From the toolbar's **Create** menu, choose **Hair**.

The new Hair System arrives with a built-in scalp so you can see the strands
immediately. To grow hair from your own geometry instead, select the Hair System
and set **Object** in the inspector to the object you want it to grow from.

***

## The inspector [#the-inspector]

Select a Hair System and the inspector groups its controls:

| Group            | What it controls                                              |
| ---------------- | ------------------------------------------------------------- |
| **Simulation**   | Play, pause and reset the strand simulation in the editor     |
| **Object**       | The surface the strands grow from                             |
| **Hair Shape**   | Length, curl, clumping and how the strands are distributed    |
| **Physics**      | Gravity, stiffness, wind and damping                          |
| **Colors**       | Root, mid and tip colours, or inheriting the surface's colour |
| **Noise Colors** | An optional colour variation mixed across the strands         |

### Simulation [#simulation]

Hair is simulated, so it needs to run to settle into place. Use the **Play** and
**Pause** buttons in the Simulation group to watch it in the editor, and **Reset**
to drop it back to its starting pose.

You don't need to press play for the published scene — **Play mode and published
scenes always simulate**. The buttons are for previewing while you work.

### Where the strands grow [#where-the-strands-grow]

The **Object** control decides the surface. You can either:

* Use one of the **built-in scalp shapes**, which the Hair System renders itself —
  useful for a quick head of hair, or as a stand-in while you block out a scene.
* **Point it at an object in your scene**, and the strands seed from that object's
  surface. This is how you get fur on a creature or grass across a terrain.

### Hair Shape [#hair-shape]

Controls the strands themselves: how **long** they are, how much they **kink** or
curl and how often, how strongly they **clump** together and how big those clumps
are, how far the tips **separate**, and how widely the roots **spread** across the
surface.

Clumping is what separates convincing hair from a uniform fuzz — real hair gathers
into strands that share a direction.

### Physics [#physics]

**Gravity** pulls the strands down; **stiffness** resists it, holding a shape rather
than hanging limp. **Wind** pushes the strands sideways, and **damping** controls how
quickly motion dies away — low damping keeps hair swinging after the object stops.

### Colour [#colour]

By default you set a **root**, **mid** and **tip** colour and the strands blend
between them, which is how most hair and fur reads: darker at the root, lighter at
the tips.

Alternatively, have the hair **take its colour from the base object's surface**, so
strands growing out of a patterned or textured object pick up that pattern. You can
then brighten or darken the root and tip relative to the sampled colour.

**Noise Colors** mixes additional colours across the hair to break up a flat result —
useful for grass, where uniform green looks synthetic.

***

## Tips [#tips]

* **Fewer, better strands.** Long, heavily kinked, densely clumped hair costs more
  to simulate and draw. If a scene slows down, reduce length and strand density
  before anything else.
* **Let it settle.** Judge a look with the simulation running, not paused — gravity
  and stiffness change the silhouette substantially.
* **Grass is hair.** Short strands, high stiffness, low gravity and a noise colour
  mix over a ground object gives you a grass field without modelling anything.
* **Shadows are optional.** Hair can cast and receive shadows from your scene
  lights; turning casting off is an easy performance win on dense hair.
