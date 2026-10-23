# Physics (/designing-in-3-d/animation/physics)



On Spline you can create different types of physics simulations, each object can be adjusted to react to gravity and collision forces.

This video contains outdated UI elements. For the latest information and updated UI, please refer to the details below.

<Embed src="https://www.youtube.com/embed/NdBpmhGvvW0" title="YouTube video player" />

## How to add physics to your 3D objects [#how-to-add-physics-to-your-3d-objects]

1. Go to the Right Sidebar, Locate the “Simulation” panel and enable the Physics property.
   * **Gravity** - Change the value to vary the effect of gravity in the scene. Positive values invert gravity.

<Image src="https://cdn.spline.design/_assets/docs/0cfea9bc-63f7-41db-821d-9eb29890856a.png" alt="image" maxWidth="300" />

2. Select the object(s) and go to the Physics section. The following parameters can be adjusted:
   * **Enabled** - Enable or disable physics, or based on visibility.
   * **Children** - By default, all groups behave as single objects. If you want the child objects to behave as single objects, change this parameter to **Separate**, then select all of the child objects and set the parameters.
   * **Body Type** - By default, all objects are set to **Positioned**, which means that they will not react to gravity forces unless you change the Body Type to **Dynamic**.
   * **Collider** - Controls the collision type, setting it to **Precise** will make the collision slower.

<Image src="https://cdn.spline.design/_assets/docs/193a22a4-b012-4dad-a45d-be40f8f3a2d7.png" alt="image" maxWidth="300" />

3. After setting an object as Dynamic, these new parameters can be adjusted:
   * **Weight** - Controls the weight of the object, which means that heavier objects will fall faster.
   * **Gravity Scale** - Controls the gravity force of a particular object.
   * **Friction** - Controls the amount of friction on the surface, the less friction you set, the more the object will move on the surface.
   * **Damping** - Increasing this value will make the object fall slower.
   * **Bounce** - Increasing this value will make the object bounce more when it hits a surface.
   * **Translation** - Constrains the positional movement based on an axis.
   * **Rotation** - Constrains the angular movement based on an axis.

<Image src="https://cdn.spline.design/_assets/docs/0dbf4dd2-d63e-46e0-9243-29135a4759cd.png" alt="image" maxWidth="300" />

***

<Embed src="https://my.spline.design/kidsplaygroundphysicscopy-f089de2f278f611a77214558f93a65bf/" title="Embedded content" height="384" />

> *Try it! ☝️ Use WASD keys to move the ball*
