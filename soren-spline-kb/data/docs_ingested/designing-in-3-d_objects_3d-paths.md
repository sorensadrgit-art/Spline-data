# 3D Paths (/designing-in-3-d/objects/3d-paths)



3D Paths are meshes generated with points and bezier curves.

They allow you to easily create objects like Tubes, Pipes, Ropes, Cables, Rails, Pathways, etc. As well as creating paths for other objects to follow.

<Embed src="https://www.youtube.com/embed/5pU7tGajw2E" title="YouTube video player" />

***

## Creating a 3D Path [#creating-a-3d-path]

1. Click on the “Plus” icon in the toolbar.
2. Select “Path”.
3. Start drawing your Path in the 3D space by adding new points.

<Callout type="idea">
  When seeing a red plane, it means you’ll be snapping points to another object’s surface.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/45723493-1ede-4dce-ad6d-8a25b109fdd8.mp4" />

## Editing a 3D Path [#editing-a-3d-path]

The Path Panel is composed of the following parameters:

* **Size** - Size of the path object.
* **Corner** - Add curve to all points of the path that don’t have a bezier curve already.
* **Subdivision** - Control subdivision of the path mesh.
* **Edit Path Button** - Enter Edit Path mode to make changes on the 3D Path.

<Image src="https://cdn.spline.design/_assets/docs/a47cdae1-697a-412f-b9c4-68012123e14a.png" alt="image" maxWidth="300" />

## Editing a 3D Path Point [#editing-a-3d-path-point]

When selecting a 3D Path Point, you’ll be able to control the following parameters:

* **Position** - Where the point is positioned in the 3D space.
* **Corner** - Add curve to a specific point.

<Image src="https://cdn.spline.design/_assets/docs/7bc80214-ed81-490c-99c5-a14c2f6932bf.png" alt="image" />

## Customizing a 3D Path [#customizing-a-3d-path]

#### Shape [#shape]

On the shape parameter you can choose the shape of your 3D Path.

<Image src="https://cdn.spline.design/_assets/docs/22bab081-49fb-49f7-a308-9d3987557bc7.png" alt="image" maxWidth="300" />

Here are the shape options available:

* Rectangle
* Circle
* Polygon
* Star
* Custom

With a custom shape, you can select any vector shape from your scene to use as a shape for a 3D Path.

<Video src="https://cdn.spline.design/_assets/docs/04425906-7b3e-48f5-b169-451275e29513.mp4" />

Here are all the rest of the 3D Path parameters:

* **Depth** - The length of the mesh along the path.
* **Offset** - Offset the start of the mesh along the path.
* **Angle** - Change the angle of the path shape.
* **Twist** - Twist the shape along the path.
* **Start Scale** - Scale of the shape at the start of the path.
* **End Scale** - Scale of the shape at the end of the path.
* **Caps** - Make the ends of the path either flat or round.

<Image src="https://cdn.spline.design/_assets/docs/69f2c40e-1b42-4081-906c-fb9f03932fc6.png" alt="image" maxWidth="300" />

## Animating a 3D Path [#animating-a-3d-path]

It’s possible to animate the parameters of a 3D Path by creating States and Transitions.

<Video src="https://cdn.spline.design/_assets/docs/e9e1bf09-1165-4e13-acc4-3a22cec4d6e7.mp4" />

## Align Objects to 3D Paths [#align-objects-to-3d-paths]

When selecting an object you want to align to a path:

1. Go to the Modifiers Panel
2. Press the "+" button and choose Align to Path
3. On Object, select the Path you want to align the object to

<Image src="https://cdn.spline.design/_assets/docs/align-to-path-modifier.png" alt="image" />

Here are the parameters for aligning an object to a path:

* **Object** - Select the path to align the object to.
* **Orientation** - Will the object be oriented along the path or to the world.
* **Offset** - Offset the start of the mesh along the path.
* **Slide** - The position of the object on the path.

<Callout type="idea">
  When using a 3D Path as an invisible path for other objects to follow, select the path, hide all Materials (from the Materials Panel), and hide Cast and Receive Shadows (from the Shadows Panel)
</Callout>

<Callout>
  When an object is aligned to a path, its orientation is controlled by the path. If you manually rotate or animate the aligned object, it may appear to work initially, but after a scene refresh, it will snap back to match the path’s orientation.
</Callout>

>

<Callout>
  Recommended approach: To animate or transform an object while it’s following a path, wrap it inside a group. Align the group to the path, and leave it untouched. Then, apply any rotation, animation, or transforms to the object inside the group. This keeps the path-follow behavior intact without interference.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/22c7dd7f-b67b-4b05-a223-ba1b7c56a23a.mp4" />

## Convert Vector Shapes into 3D Paths [#convert-vector-shapes-into-3d-paths]

When selecting a Vector Shape, there’s a Convert to Path button available.

<Image src="https://cdn.spline.design/_assets/docs/c2629a92-4218-415a-a451-5a67ed5d02ae.png" alt="image" maxWidth="300" />

This button will convert the Vector Shape selected into a 3D Path.

<Callout type="idea">
  A great use case is converting text into Vector Shapes and then converting them into 3D Paths.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/df75f479-90cf-47ee-82ff-cefe39100c07.mp4" />

***

<Embed src="https://my.spline.design/3dpathshandwrittencopy-5738fab2c72ab2937badc0013eff7d8e/" title="Embedded content" height="384" />

> *3D Paths in action! ☝️ Drag to Orbit*
