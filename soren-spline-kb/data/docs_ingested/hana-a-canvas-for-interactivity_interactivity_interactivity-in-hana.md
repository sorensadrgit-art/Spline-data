# Interactivity in Hana (/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana)

> States, events and actions in Hana — how to make a design respond to clicks, hovers, keys and the pointer, and animate between states.



Interactivity in Hana is built from three things, and no code:

* **States** — alternative versions of an object. A button's hover look, a
  panel's open position, a card's lifted shadow.
* **Events** — what triggers a change. A click, a hover, a key, the moment the
  scene loads.
* **Actions** — what happens when an event fires. Usually a **transition** to a
  state, but also opening a link, showing an object, or playing a video.

Author them on the object itself, and Hana animates between the states for you —
you never keyframe a property.

***

## The workflow [#the-workflow]

1. Select an object and open the **States** panel. It always has a **Base State**:
   the object as designed.
2. Add a state and give it a name (`Hover`, `Open`, `Active`). With that state
   selected, change the object — move it, restyle it, resize it. Those changes
   belong to that state; the Base State is untouched.
3. Open the **Events** panel and add an event.
4. Give the event a **Transition** action pointing at the state you made.
5. Press **Play** to try it.

States can be renamed, duplicated and deleted as the design evolves, so it's
normal to build a hover state by duplicating one you already like.

***

## Events [#events]

| Event                                     | Fires when                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------ |
| **Start**                                 | The scene loads — for entrance animations and anything that should already be moving |
| **Mouse Down**                            | The pointer is pressed                                                               |
| **Mouse Up**                              | The pointer is released                                                              |
| **Mouse Press**                           | A press-and-release, the usual "click" — reverts on release                          |
| **Mouse Hover**                           | The pointer enters the object, and reverses when it leaves                           |
| **Key Down** / **Key Up** / **Key Press** | A keyboard key is pressed, released, or both                                         |
| **Look At**                               | Turns the object toward the pointer                                                  |
| **Follow**                                | Makes the object follow the pointer                                                  |

Mouse events work with touch on mobile devices too.

### Object or canvas [#object-or-canvas]

A mouse event can listen on **the object itself** or on **the whole canvas** —
the difference between a button reacting to its own click and a scene reacting to
a click anywhere.

### Passthrough [#passthrough]

The icon next to the **Events** label toggles **passthrough**, which decides what
happens when objects overlap:

* **On** — the event triggers on every object under the pointer, so a click on a
  stacked button activates both.
* **Off** — only the topmost object responds.

Useful for layered and nested interactions where a parent frame and its children
both carry events.

### Look At and Follow [#look-at-and-follow]

These two are continuous rather than one-shot, and have their own controls: a
**damping** factor for how loosely the object trails the pointer, a **distance
limit** so it stops at a boundary, whether it **resets when the pointer leaves**
and how fast it returns, and which **axis** it's allowed to move or turn on.
They're what you use for cursor-tracking eyes, parallax elements and magnetic
buttons.

***

## Actions [#actions]

| Action         | What it does                                                           |
| -------------- | ---------------------------------------------------------------------- |
| **Transition** | Animates the object to one or more states — the action you'll use most |
| **Show**       | Shows or hides an object, with an option to toggle                     |
| **Link**       | Opens a URL, in a new tab or the same one                              |
| **Video**      | Controls a video — play, pause, volume, looping                        |
| **Animation**  | Plays an animation clip from an imported 3D model                      |

One event can carry several actions, so a single click can transition a panel,
hide a button and open a link.

***

## Transitions [#transitions]

A transition is where the motion is shaped:

* **Duration** — how long the change takes.
* **Easing** — the curve. Alongside the familiar linear and ease in / out /
  in-out, Hana has **spring** physics (mass, stiffness, damping and initial
  velocity) for motion that settles naturally, and **custom bezier** curves when
  you want an exact shape.
* **Delay** — wait before starting, which is how you stagger several objects into
  a sequence.
* **Repeat** and **direction** — run a transition a number of times, or bounce it
  back and forth for a looping pulse.

A transition can hold **several states in sequence**, so one event can walk an
object through a multi-step move without extra events.

### Run mode [#run-mode]

| Mode       | Behavior                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| **Once**   | Plays through and stays there                                                                                      |
| **Repeat** | Loops                                                                                                              |
| **Toggle** | Alternates between the state and where it came from on each trigger — how a switch, accordion or menu button works |

***

## What can be animated [#what-can-be-animated]

| Animates                                  | Doesn't animate                   |
| ----------------------------------------- | --------------------------------- |
| Position, rotation, size                  | Padding, gap and layout direction |
| Fill and stroke — color and opacity       |                                   |
| Effects                                   |                                   |
| Custom shape edits, including booleans    |                                   |
| Vector and vector-network point positions |                                   |
| 3D projections                            |                                   |

Two caveats worth knowing before you build:

* **Vector transitions need matching point counts.** A vector can only tween to
  a state with the same number of points.
* **Layout properties are excluded.** A state can't change a frame's padding, gap
  or direction. If you want something to visibly grow or shrink, animate its
  width, height or scale instead — see
  [Auto Layout & Constraints](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints.md).

***

## Where to go next [#where-to-go-next]

[Effects in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/effects-in-hana.md),
[3D Shapes in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/3d-shapes-in-hana.md),
[Exporting in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/exporting-in-hana.md),
[AI Agent in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/ai-in-hana.md)
