# Game Controls Event (/interaction-states-events-and-actions/events/game-controls-event)



With a Game Controls event, you can create interactive experiences, where you control a character (that’s what we call the controlled object), by walking or flying around your scenes.

Navigate your scene and control your character with key inputs, joysticks and buttons on mobile, gravity, and collision detection.

There are many different options to customize it to the type of experience you decide to build.

***

## Test the gameplay 🎮👇 [#test-the-gameplay-]

Before moving on with the documentation, why not give the game controls a quick test below?

Use `W S A D` keys to move the character, `SPACE` to jump, and `↑↓←→` keys to move the camera.

<Embed src="https://my.spline.design/pigislandtutorialcopy-421e2ff873658c086c6846c5d9b79317/" title="Spline Embed" height="384" />

<Callout>
  *Click the embed to focus. Open the experience in a new tab [HERE](https://my.spline.design/pigislandtutorialcopy-421e2ff873658c086c6846c5d9b79317/).*
</Callout>

***

## Game Controls Video Tutorial [#game-controls-video-tutorial]

If you prefer to follow along with a video, we’ve made this tutorial where we go through all the details of a Game Controls event.

<Embed src="https://www.youtube.com/embed/yvehPjQhS5U" title="YouTube video player" />

***

## Adding a Game Controls Event [#adding-a-game-controls-event]

Here's how to add a Game Controls event to an object in your scene:

1. Select the object that you want to control.
2. On the Events panel, add a new event and select `Game Controls` from the dropdown menu.
3. Open the Game Controls event and tweak the settings to your liking.

<Video src="https://cdn.spline.design/_assets/docs/a7427866-2f8b-4151-8400-0609a95decd2.mp4" />

## Adjusting Character Orientation [#adjusting-character-orientation]

If your character is composed of grouped objects and you notice it is moving backwards, you’ll need to make sure it is facing towards the -Z direction.

<Image src="https://cdn.spline.design/_assets/docs/dbb612f0-3d77-4417-87c0-7286c25efd6f.png" alt="image" maxWidth="300" />

To fix this you’ll need to select all the objects inside your main group and rotate them to face the -Z direction.

This usually means rotating all the objects inside your character group by 180º degrees.

<Video src="https://cdn.spline.design/_assets/docs/8ebb478f-c5cd-4b02-b557-99aec482b096.mp4" />

*Adjusting the orientation of a character so it faces the -Z direction.*

***

## Understanding the Game Controls Settings [#understanding-the-game-controls-settings]

Let's now dive deep into all the settings that can be found inside the Game Controls event, so you can adjust them to properly match the experience you’re building.

### Movement [#movement]

In Movement, you can define how your character will be moving around your scene.

<Video src="https://cdn.spline.design/_assets/docs/43ca1af9-3c8a-4a85-8280-b254ae4bcc39.mp4" />

*Walk or Fly are the two movement modes of a Game Controls event.*

**Movement Mode**

* **Walk** - is used for experiences where you move on surfaces.
* **Fly** - is used for experiences where you fly around your scene.

**Auto-Orientation**

When turned on, the character rotates automatically based on the direction you’re moving in.

**Speed**

Control the speed of position and rotation.

**Delay**

Control the acceleration at the Start and deceleration at the End of position and rotation.

<Image src="https://cdn.spline.design/_assets/docs/ea8ccef7-a1d3-4e7a-8dbe-94fdde605897.png" alt="image" maxWidth="300" />

***

## Controls [#controls]

To create unique game mechanics controls can be adjusted.

Desktop Controls is where we can define what keys are going to be used to control our character and what each of them does.

<Video src="https://cdn.spline.design/_assets/docs/e73684fc-386e-4def-bec1-7ab4deae8e5b.mp4" />

*Remapping a key and changing its action.*

**Rotate By**

Define how you can rotate the camera. Either by using the Mouse, the Arrow keys, or both.

**Keyboard Keys**

Once you select a key, you can either press another key to assign it or change the action of that key on the dropdown below.

If you’ve made too many changes, the reset button (on the top right) will let you reset to the default keys.

Here’s a list of all the behaviors and their default keys:

| Default Key | Behavior          |
| ----------- | ----------------- |
| W           | Move Forward (-Z) |
| S           | Move Back (+Z)    |
| A           | Move Left (-X)    |
| D           | Move Right (+X)   |
| ↑           | Rotate Up (+X)    |
| ↓           | Rotate Down (-X)  |
| ←           | Rotate Left (+Y)  |
| →           | Rotate Right (-Y) |
|             |                   |
| Space       | Jump              |
| Ctrl        | None by default   |
| Shift       | Run               |
| None        | Move Up (+Y)      |
| None        | Move Down (-Y)    |

### Multiple Game Controls Events [#multiple-game-controls-events]

If you have multiple Game Controls events in your scene, only one of them will be the one where you can define the desktop and mobile controls.

So on every new Game Controls event, you create, you’ll see this warning, letting you know that the event you’re editing is not the main Game Controls event.

But you can always press the button below to make it the main one and edit the controls from there.

<Image src="https://cdn.spline.design/_assets/docs/7608ce10-a07c-4e24-801b-76f6b4916b5e.png" alt="image" maxWidth="300" />

***

## Touch Controls [#touch-controls]

Touch Controls lets you define the controls of your experience on touch-based devices like phones and tablets.

<Video src="https://cdn.spline.design/_assets/docs/cde48552-c64a-4ffd-bdf6-46424fb1c097.mp4" />

*How touch controls look on a touch-based device.*

**Rotate By**

Define how you can rotate the camera. Either by dragging on the screen or by using a joystick.

**Joysticks and Buttons Position**

Choose where to position the joysticks and buttons for **Move**, **Rotate** (only visible if Rotate By is set to Joystick), and **Jump**.

The representation you see is how they will be positioned on the device’s screen.

**Offset** - The space the control has from the screen edge.

**Button Size** - The size of each control.

**Visibility** - Defines if the selected control is always visible or becomes visible when interacted with.

<Image src="https://cdn.spline.design/_assets/docs/118f7168-3365-4fc4-b3ba-a33817a8c6ed.png" alt="image" maxWidth="300" />

***

## Collision [#collision]

With collision, we can define how our character will collide with everything in our scene.

Make changes to the collider on your character and tweak settings like Gravity, Jump Power, and the Reset Position.

<Video src="https://cdn.spline.design/_assets/docs/9b99ac20-46ee-4c0c-9410-0fad1af8bf7f.mp4" />

*Resizing a capsule collider and testing it in Play Mode.*

**Collider**

Define the boundaries of your character by choosing a collider like a Capsule or a Sphere, and match it perfectly by changing its size, position and rotation.

**Jump**

Define how high your character will jump.

**Reset Y Position**

Define the value on the Y axis where if the character reaches it, the scene will reset.

This is useful for scenes with platforms which the character can fall from.

<Image src="https://cdn.spline.design/_assets/docs/53aeb91a-30ef-458c-8d41-c641f788b653.png" alt="image" maxWidth="300" />

**To control the Gravity of your scene**

Unselect all objects and find the scene settings on the right sidebar.

On Simulation, you’ll find the Gravity property.

This affects how your character jumps and falls. As you make the value closer to 0, the character will float more.

<Image src="https://cdn.spline.design/_assets/docs/cf650be8-0d97-4afb-9ee9-e97857404dd0.png" alt="image" maxWidth="300" />

***

## Click To Move - Navigation Mesh [#click-to-move---navigation-mesh]

A navigation mesh is like a map that helps characters or objects move around in a 3D environment. It's made up of connected polygons that represent walkable areas. These polygons are like puzzle pieces that fit together, creating a navigation mesh to show where characters can go without getting stuck.

When instructed to move, Characters use the navigation mesh to find the best path, avoid obstacles and move smoothly in the 3D environment.

With this feature turned on, you can now press around your scene to tell your character where to move to.

<Video src="https://cdn.spline.design/_assets/docs/93eb2298-16b4-4c4c-ad27-87f3eadf8519.mp4" />

Click To Move is a component of the Game Controls event and you can toggle it ON from the event settings.

**Grid Size** → How big the polygons that make up the navigation mesh are. This allows you to fine-tune your navigation mesh.

**Offset** → Adds spacing along edges or walls so the character doesn’t walk up to them.

**Helper** → Visibility of the wireframe of your navigation mesh.

**Radius** → Radius of the click circle.

**Color** → Color of the click circle.

<Image src="https://cdn.spline.design/_assets/docs/1a1c6240-32f5-4f6f-85ab-12b51b207728.png" alt="image" maxWidth="300" />

#### Zones [#zones]

**All** → Will use all objects from the scene to generate the navigation mesh.

**Custom** → Gives you control over what objects to use when generating the navigation mesh.

<Image src="https://cdn.spline.design/_assets/docs/278e5cd2-9aa2-416e-a86a-332c44f0ad65.png" alt="image" maxWidth="300" />

***

## Camera Follow [#camera-follow]

If you need a camera to be following your character, this is where you can define which one will be used for it.

<Callout>
  So you stay organized, better collaborate with others and avoid accidental changes, we recommend that you create a new camera for this purpose and use your Personal Camera to move around in the editor.
</Callout>

To create a new camera, you can do so from the “+” icon on the toolbar and selecting Camera, or from the Camera Panel and then pressing “Add new camera” from the dropdown.

Make sure to position the camera in the position you want the experience to be viewed by everyone in the final result.

<Video src="https://cdn.spline.design/_assets/docs/b8454db6-ac2b-4700-9b42-5cd34a676c8d.mp4" />

*Difference between a static Camera and a Camera following the character.*

**Camera**

Select the camera that is going to be following your character.

**Orient To**

**Normal** - When moving the character the camera will follow it by moving forward, backwards, or pan to the sides.

**Angle** - When moving the character the camera will follow it by moving but also rotate at an angle behind the character.

**Up/Down & Left/Right**

With the directions Up, Down, Left, and Right, you can decide how the user can control the camera.

You can either allow the user to move it in those directions, disable it, or define limits by using angle values.

<Image src="https://cdn.spline.design/_assets/docs/a7ae6d1a-9b9f-45d6-aaf8-d78aa3e6f4b6.png" alt="image" maxWidth="300" />

**Matching Cameras**

Remember that the camera used to follow the character should also be the camera defined as the Play Camera in the export settings.

If they’re not, you’ll see this warning, where pressing the button will match the two.

<Image src="https://cdn.spline.design/_assets/docs/0db5ff98-db6e-4ed3-b712-a2d470f3b37c.png" alt="image" maxWidth="300" />

If the cameras are all correctly set up, you’ll see this in the export panel, letting you know that the camera is being controlled by a Game Controls event.

Meaning that the camera defined as the Play Camera is currently used to follow a character.

<Image src="https://cdn.spline.design/_assets/docs/965a74f2-2f6d-41b0-b40c-387389e00a5a.png" alt="image" maxWidth="300" />

***

## Behaviors [#behaviors]

With Behaviors, it is possible to add actions to the character when on Idle, when moving, and when jumping, that way creating more interactive reactions to it.

#### Adding Behaviors [#adding-behaviors]

To add behaviors to your character do the following:

1. Open the Game Controls event of your character(s), scroll down to the Behavior section, and open the behavior to which you want to add an action to. The current behaviors are the following:

   * **Idle -** Actions for when the character is in a resting state.
   * **On Move -** Actions for when the character is moving.
   * **On Jump -** Actions for when the character is jumping.
   * **On Run** - Actions for when the character is running

   <Image src="https://cdn.spline.design/_assets/docs/7e5800f7-6638-4218-b2fb-cc4d2bf76af9.png" alt="image" maxWidth="300" />
2. Following actions are supported:

* [Transition Action](https://docs.spline.design/interaction-states-events-and-actions/actions/transition-action.md)
* [Animation Action](https://docs.spline.design/interaction-states-events-and-actions/actions/animation-action.md)
* [Sound Action](https://docs.spline.design/interaction-states-events-and-actions/actions/sound-action.md)
* [Video Action](https://docs.spline.design/interaction-states-events-and-actions/actions/video-action.md)
* [Create Object Action](https://docs.spline.design/interaction-states-events-and-actions/actions/create-object-action.md)

<Image src="https://cdn.spline.design/_assets/docs/ef6d973a-be6e-4cc2-9daa-1645cf9a5548.png" alt="image" maxWidth="300" />

3. Create an action on the behavior that you want to adjust and select the object and the state target. Similar to other events, Behaviors can trigger transitions that target objects and trigger a state change with transitions, delay, cycle, and loop properties. Sound actions can play, pause, and stop sounds from Spline’s Original Sounds Library or your own custom sounds.

<Image src="https://cdn.spline.design/_assets/docs/c3c1261e-2c44-4437-b714-d49aa9c37eba.png" alt="image" maxWidth="300" />

<Callout>
  We recommend adding the behavior states in new groups of your character to have better control over them.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/e2dbc29e-6827-4ead-b324-a9a2e2e7975f.mp4" />

*Adding Behaviors to the character.*
