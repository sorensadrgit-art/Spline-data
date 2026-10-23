# Sections in Hana (/hana-a-canvas-for-interactivity/basics/sections-in-hana)

> Group related frames and objects on the canvas into labelled containers.



**Sections** are containers for organising your canvas. Use them to group related
frames — a set of screens for one flow, all the states of a component, everything
still in progress — so a large file stays readable.

A section is a labelled box you draw around your work. Move the section and its
contents move with it.

***

## Creating a section [#creating-a-section]

The Section tool sits in the toolbar, in the same dropdown as **Frame**:

1. Click the frame icon in the toolbar and choose **Section** — or just press <kbd>S</kbd>.
2. Drag on the canvas to draw it.

New sections are named **Section 1**, **Section 2** and so on. Double-click the
label above the section to rename it.

***

## Working with sections [#working-with-sections]

* **Drag objects in and out.** Dropping a frame or object inside a section makes it
  a child; dragging it out removes it.
* **Move and resize as one.** Moving a section moves everything inside it. Deleting
  a section deletes its contents too.
* **They don't clip.** Unlike frames, a section never hides content that extends
  past its edges — it's there to group things, not to crop them.
* **Find them in the layers tree.** Sections appear alongside your frames with a
  dotted-square icon.

### Appearance [#appearance]

Select a section and the inspector shows **Transform**, **Shape**, **Fill**,
**Stroke** and **Export**. Change the fill to colour-code areas of a large canvas —
the label pill above the section picks up the fill colour, so the grouping stays
readable at a distance.

***

## What sections don't do [#what-sections-dont-do]

Sections are deliberately simpler than frames. A section is **not**:

* **A presentable screen.** Sections have no play button and can't be presented in
  Play mode — [frames](https://docs.spline.design/hana-a-canvas-for-interactivity/basics/pages-in-hana.md) are what you
  present.
* **A component.** You can't turn a section into a component.
* **An auto-layout container.** Auto-layout applies to frames, not sections.
* **A prompt target.** [AI prompts](https://docs.spline.design/hana-a-canvas-for-interactivity/ai-in-hana.md) work
  on a frame, so point them at the frames inside a section rather than the section
  itself.

Sections do **export** exactly like frames, so grouping your work doesn't change
what you can get out of it. See
[Exporting in Hana](https://docs.spline.design/hana-a-canvas-for-interactivity/assets-and-export/exporting-in-hana.md).

<Callout>
  If you want a container that crops its contents, presents in Play mode, or uses
  auto-layout, use a **Frame** instead.
</Callout>
