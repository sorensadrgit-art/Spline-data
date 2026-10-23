# Particles (/designing-in-3-d/animation/particles)



Particles are graphical elements that are used to create various visual effects like fire, smoke, rain, snow, and other dynamic effects.

They mimic the physical properties of real-world particles. This includes their movement, interaction with forces like gravity or noise, and collisions with other objects.

<Embed src="https://www.youtube.com/embed/7l8LPgz47Zk" title="YouTube video player" />

Examples of particle-based effects include:

* **Fire and Smoke:** Simulating the movement and behavior of fire and smoke particles.
* **Explosions:** Creating explosive effects by simulating the motion and interaction of debris particles.
* **Water and Fluids:** Simulating the flow and behavior of water droplets or other fluids.
* **Magic:** Generating magical effects like sparks, glows, and magical trails.
* **Weather**: Simulate weather conditions like rain and snow.

<Embed src="https://www.youtube.com/embed/q1K5nji8KHM" title="YouTube video player" />

***

## Creating a new Particle Emitter [#creating-a-new-particle-emitter]

Particles are emitted from a source called an emitter. The emitter is defined by a shape like a plane, sphere, or even a custom object and it’s also where you control the emission duration which can be infinite, loop, or one time.

To create a new particle emitter follow these steps.

1. Press the + icon on the toolbar;
2. Select the Particle Emitter;
3. A new particle emitter will be created in world origin.

<Video src="https://cdn.spline.design/_assets/docs/dd16fe87-309f-4a69-8fce-d5f94b80fe4b.mp4" />

***

## Customizing the Particle Emitter [#customizing-the-particle-emitter]

When selecting a particle emitter, you can customize a variety of properties like how the particles look and behave. From the Particle Emitter panel, you can change properties related to how the particles are emitted.

* **Shape (Plane, Box, Sphere, Torus, Cone, or Custom Shape)** - The shape of the particle emitter.
* **Size** - Size of the emitter object.
* **Autoplay** - Decide if the emitter emits automatically or not.
* **Emit Time (Infinite, Loop, or One Time)** - How long the emitter emits particles.
  * On **Loop** and **One Time**:
    * **Delay** - Time before before the emitter starts emitting.
    * **Duration** - Duration of the emission.

<Image src="https://cdn.spline.design/_assets/docs/6e3e8433-5b03-4ad8-84e1-5f54aa71d8e3.png" alt="image" maxWidth="300" />

***

## Customizing Particle Properties [#customizing-particle-properties]

Particles can have various attributes, such as color, size, speed, birth rate, and lifetime. These attributes can be manipulated to control the appearance and behavior of the particles over time.

### Particle Attributes [#particle-attributes]

Control the look of the emitted particles.

* **Color A & B** - The colors of the particles.
* **Coloring → Blend or Random**
  * On **Blend** - the particles will change color from A to B during their lifetime.
  * On **Random** - the particles will start with a random color between colors A and B.
* **Size** - The size of the particles.
* **Rotation** - Rotation of the particles.
* **Birth Rate** - The number of particles generated at the start.
* **Lifetime** - The time the particles stay visible.
* **Alpha Fade** - How the color alpha of the particles changes during lifetime.
* **Size Fade** - How the particle size changes during lifetime.
* **Speed** - How fast the particles move.
* **Orientation → Axis or Surface**
  * On **Axis** - emits particles on world axis.
  * On **Surface** - emits particles from the emitter shape surface.
* **Direction** - Overwrite the direction of the particles.
* **Image** - Upload an image to be used in the particles.

<Image src="https://cdn.spline.design/_assets/docs/7ac1e933-506a-4eed-ab2d-f75639a7981c.png" alt="image" maxWidth="300" />

### Particle Forces [#particle-forces]

Control the forces affecting the emitted particles.

* **Gravity** - Adds gravity to particles. Positive values make the particles go up and negative values make the particles go down.
* **Collision** - Choose a particle collider or force that will affect the selected particle emitter.

<Image src="https://cdn.spline.design/_assets/docs/ec2d40c3-7e00-46b8-9216-b278676e1bde.png" alt="image" maxWidth="300" />

### Particle Noise [#particle-noise]

Affects the way particles move with different types of noise.

* **Type (Curl, Simplex, or Fbm)** - Choose the type of noise.
* **Scale** - Adjusts the size of the noise patterns, influencing the overall visual of the noise.
* **Variation** - Alters the diversity or randomness within the noise, allowing for different levels of complexity and irregularity.
* **Seed** - Provides a way to reproduce specific patterns by maintaining a consistent starting point.

<Image src="https://cdn.spline.design/_assets/docs/797c9a4c-9027-4ce7-b227-aa2b85f77b51.png" alt="image" maxWidth="300" />

### Particle Randomness [#particle-randomness]

Adds randomness to how the particles behave or are displayed.

* **Scale** - Adds randomness to the scale of the particles.
* **Rotation** - Adds randomness to the rotation of the particles.
* **Mass** - Adds randomness to the mass of the particles.

<Image src="https://cdn.spline.design/_assets/docs/6ee9b3e7-25bf-4c29-8080-52da2fb614d8.png" alt="image" maxWidth="300" />

***

## Particle Presets [#particle-presets]

With particle presets you can save your particle properties to reuse later in multiple different emitters.

To save a preset:

1. Select a particle emitter;
2. Press the assets icon on the particles panel;
3. Press the + button on the particle presets floating panel.

This is helpful when you need to quickly copy the settings from a previous emitter or use those settings as a starting point.

<Image src="https://cdn.spline.design/_assets/docs/d0b35a1c-546a-4777-88c2-30e82bcefdaf.png" alt="image" maxWidth="300" />

***

## Particle Control Action [#particle-control-action]

With the event system, you can control when an emitter should be emitting or not. To do so, you can use the Particle Control Action that can be triggered by most events.

* **Emitter** - Select Particle Emitter to control.
* **Emission (Start, Stop, Start/Stop, Pause, Pause/Resume, or Reset)** - Decide how to control the emission of the particles.
* **Delay** - Time before the event action is triggered.

<Image src="https://cdn.spline.design/_assets/docs/9462aa2d-2f31-425a-881c-b21f401a79ce.png" alt="image" maxWidth="300" />

***

## Particle Forces [#particle-forces-1]

Forces are custom areas that interact with particles and change how they behave.

### Creating a new Particle Force [#creating-a-new-particle-force]

To create a new particle force, follow these steps:

1. Press the + icon on the toolbar;
2. Select the Particle Force;
3. A new particle force will be created in world origin.

### Customizing the Particle Force [#customizing-the-particle-force]

When selecting a particle force, you can customize how the particle force will change the behavior of particles.

* **Force Type (Collider, Attractor, or Vortex)**
  * On **Collider** - the particles will collide with the force area.
  * On **Attractor** - the particles will be attracted to the force area.
  * On **Vortex** - the particles inside the force area will rotate around the area center.
* **Shape (Box or Sphere)** - The shape of the force area.
* **Size** - How big the area is.
* **Helper** - Show or hide the viewport helper of the force area.

<Image src="https://cdn.spline.design/_assets/docs/0d7e71cc-2989-4f7d-8e8d-c365b09c975e.png" alt="image" maxWidth="300" />

> Remember that to have a force interact with particles, it should be assigned from the particle emitter side. Refer to [Particle Forces panel section](https://docs.spline.design/designing-in-3-d/animation/particles.md#particle-forces) above.
