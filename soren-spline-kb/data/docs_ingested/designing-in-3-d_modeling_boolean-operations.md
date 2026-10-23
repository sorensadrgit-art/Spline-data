# Boolean Operations (/designing-in-3-d/modeling/boolean-operations)



<Embed src="https://www.youtube.com/embed/Ib-OD9gfBFI" title="YouTube video player" />

There are 3 different Boolean Operations that you can apply to a set of selected 3D objects:

* **Union** - Combines the selected objects into a single one.

* **Subtract** - Removes the overlapping parts from the base object. The base object is always the bottom layer and the top layer is subtracted from it.

* **Intersect** - Creates an object from the parts where the selected objects overlap.

<Image src="https://cdn.spline.design/_assets/docs/f66096f9-72ad-476f-ab03-387afbd27a25.png" alt="image" maxWidth="500" />

You can also play with nested booleans, which means that you can have boolean objects inside other boolean objects.

Once a boolean object is created you can change the type of operation at any time.

<Image src="https://cdn.spline.design/_assets/docs/482d6cfc-b3b6-4b60-98e2-93351dcd0c06.png" alt="image" maxWidth="500" />

Finally, you can use the Merge Geometries function to merge a set of selected objects into a single geometry but with the structure of all the objects retained.

#### Booleans Performance [#booleans-performance]

Boolean operations can end up becoming very expensive in terms of performance. Here are some suggestions of what to do to mitigate performance issues related to booleans.

1. Reduce the sides of the objects involved in boolean operations. (Instead of using a Sphere with sides of 64, try reducing them. Usually, there won’t be a very noticeable difference)
2. Baking the boolean object using the “Apply & Edit” option. (You can save a copy of your editable boolean object and hide it, so it doesn’t load in the scene)
3. Instead of animating the Size property, animate the Scale instead, it is more performance efficient.
