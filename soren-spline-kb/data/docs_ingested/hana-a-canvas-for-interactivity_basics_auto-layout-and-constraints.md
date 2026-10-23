# Auto Layout & Constraints (/hana-a-canvas-for-interactivity/basics/auto-layout-and-constraints)

> Build responsive designs in Hana — frames that arrange their own children, and elements that adapt when a frame resizes.



Designs rarely stay one size. Hana has two systems for handling that, and they
solve different problems:

| System          | What it does                                                                        | Reach for it when                                                                     |
| --------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Auto Layout** | A frame arranges its children in a row or column, spacing and resizing them for you | Buttons, lists, nav bars, cards, stacked sections — anything whose content can change |
| **Constraints** | An element holds a relationship to its parent frame's edges as that frame resizes   | Backgrounds, pinned headers, corner badges, anything placed freely                    |

They work together: constraints handle elements positioned freely, auto layout
handles the ones flowing inside a container.

***

## Auto Layout [#auto-layout]

Select a frame and turn on the **Layout** panel in the properties sidebar. Its
children stop being individually positioned and start flowing in order.

<Callout type="idea">
  You don't need a frame first. Turn Layout on with a plain selection and Hana
  wraps it in a frame for you; turn it on with a group selected and the group
  becomes a frame.
</Callout>

### Direction and wrapping [#direction-and-wrapping]

**Direction** sets the flow: **horizontal** or **vertical**. Turn on **wrap** and
items that don't fit continue onto a new line or column instead of overflowing —
which is what you want for tag lists, image grids and card collections. Wrap mode
also offers a **masonry** option, staggering items into a Pinterest-style
arrangement rather than aligning them in strict rows.

### Align [#align]

**Align** decides where children sit inside the container, as a nine-position
grid — top-left through to bottom-right. In a horizontal layout the vertical half
of that choice controls whether items ride the top, the middle or the baseline of
the row; in a vertical layout the horizontal half does the same for columns.

### Gap and padding [#gap-and-padding]

**Gap** is the space *between* items, set separately for the main direction and
for rows when wrapping. It accepts **negative values** — useful for deliberately
overlapping avatars or stacked cards.

**Padding** is the space between the container's edges and its content, adjustable
independently on each side.

***

## Sizing children: Fixed, Fill and Hug [#sizing-children-fixed-fill-and-hug]

This is the part that makes auto layout click. Every child of an auto-layout
frame chooses how it sizes on each axis:

| Sizing    | Behavior                                           | Typical use                                                           |
| --------- | -------------------------------------------------- | --------------------------------------------------------------------- |
| **Fixed** | Stays exactly the size you set                     | An icon, an avatar, a fixed-width sidebar                             |
| **Fill**  | Grows to take the available space in the container | A text field next to a fixed button; the flexible middle of a nav bar |
| **Hug**   | Shrinks to fit its own content                     | A button that stays snug around its label                             |

A button is usually **Hug** on both axes; the container it lives in is often
**Fill** horizontally. Two elements that both **Fill** share the space between
them.

<Callout type="idea">
  The classic pattern: a row set to Fill the frame, with a **Hug** button on the
  right and a **Fill** text element on the left. Change the label, resize the
  frame — the row keeps working without you touching a coordinate.
</Callout>

### Taking a child out of the flow [#taking-a-child-out-of-the-flow]

Sometimes one element inside an auto-layout frame shouldn't participate — a badge
pinned to a corner, a decorative shape behind the content. Switch that child to
**absolute** positioning from the **Transform** panel and it leaves the flow: you
position it freely, and it follows its **constraints** instead.

***

## Constraints [#constraints]

An element that isn't flowing in an auto layout needs to know what to do when its
parent frame changes size. That's what the **Constraints** panel is for — a
visual picker plus a dropdown per axis.

| Horizontal         | Vertical           | What it does                                              |
| ------------------ | ------------------ | --------------------------------------------------------- |
| **Left**           | **Top**            | Keeps a fixed distance from that edge                     |
| **Right**          | **Bottom**         | Keeps a fixed distance from the opposite edge             |
| **Left and Right** | **Top and Bottom** | Holds both edges, so the element stretches with the frame |
| **Center**         | **Center**         | Stays centered as the frame grows                         |
| **Scale**          | **Scale**          | Keeps its position and size proportional to the frame     |

Set each axis independently — a header is typically **Left and Right** plus
**Top**, so it spans the width and stays at the top. A full-bleed background is
**Left and Right** with **Top and Bottom**. A floating action button is **Right**
and **Bottom**.

***

## Things worth knowing [#things-worth-knowing]

* **Layout properties don't animate.** Padding, gap and direction can't change
  between states — a state that needs to visibly resize should change width,
  height or scale instead. See
  [Interactivity in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/interactivity/interactivity-in-hana.md).
* **Nest layouts freely.** A vertical page frame holding horizontal row frames is
  the normal way to build a screen, and each level manages its own spacing.
* **Frames are also your export unit**, so the frame you build a layout in is
  usually the frame you publish. See
  [Exporting in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/exporting-in-hana.md).

[Designing in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/designing-in-hana.md),
[Sections in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/sections-in-hana.md),
[Pages in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/pages-in-hana.md)
