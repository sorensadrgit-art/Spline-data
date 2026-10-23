# Components (/designing-in-3-d/scenes/components)



Components are objects that can be reused multiple times throughout your scene and whenever there are changes made to the main component all instances will update accordingly.

Components will help you stay organized and consistent by allowing you to create a design system you can reuse across your scene.

<Embed src="https://www.youtube.com/embed/__ThJTCvMUs" title="YouTube video player" />

#### 🍀 Main Component [#main-component]

The main object that all instances will refer back to and where you can make changes to update all instances.

#### ☘️ Instances [#️instances]

For objects whose properties are connected to the main component, any changes made on the main component will be reflected on the instances unless there have been overrides made to some properties.

***

## Creating a Component [#creating-a-component]

There are two ways to create a new component:

1. By right-clicking and selecting “Create Component” from the object context menu
2. With the shortcut **⇧⌘K**

<Video src="https://cdn.spline.design/_assets/docs/9dbdbbb4-06f9-450d-9219-b78838006698.mp4" />

## Creating Instances [#creating-instances]

There are multiple ways to create an instance of the main component:

1. Duplicate the main component with **⌘D**
2. Copy and paste the main component with **⌘C*&#x2A; and **⌘V**
3. **⌘ + Drag** the main component to a different location

<Video src="https://cdn.spline.design/_assets/docs/53958604-cd2c-43a7-95c0-59612aded9ff.mp4" />

## Detaching Instances [#detaching-instances]

Detaching an Instance turns it into a normal object, meaning that it will no longer refer back to the main component and any changes on the main component will not be reflected on that object anymore.

There are two ways to detach an instance from the main component:

1. By right-clicking and selecting “Detach Instance” from the object context menu
2. From the Instance Panel, by pressing the detach icon

<Video src="https://cdn.spline.design/_assets/docs/a8936687-f5dc-49a3-9b5b-8fad708cef66.mp4" />

## Instance Overrides [#instance-overrides]

In an instance, it is possible to override object properties like Transform, Geometry Resize, Material, Events, etc.

<Video src="https://cdn.spline.design/_assets/docs/b6080417-e2b7-4c5b-9599-87a276ce8f47.mp4" />

### Reset Instance Overrides [#reset-instance-overrides]

From the Instance Panel, it is possible to Reset Overrides made to the Instance root or child objects of that Instance.

#### From the Instance root: [#from-the-instance-root]

* **Reset Object Overrides** → Resets overrides made on the Instance root (currently only physics properties)
* **Reset All Overrides** → Resets all overrides made on the root and all child objects of that Instance, making it look exactly like the main component again.
* **Push Changes to Main** → Pushes all the overrides made on the Instance to the Main Component.

#### From child objects of an Instance: [#from-child-objects-of-an-instance]

* **Reset Object Overrides** → Resets all overrides made only on the selected object. If that object has child objects or is a group, the child objects will not be reset.
* **Reset All Overrides** → Resets all the overrides made on the selected object and its child objects, making it look exactly like on the main component again.
* Reset individual properties like **Transform**, **Geometry**, **Material**, etc.

<Video src="https://cdn.spline.design/_assets/docs/4b1acfad-f4f4-4fa3-9dc6-7cfab398c8fc.mp4" />

## Component Swapping [#component-swapping]

From the Instance Panel, the instance dropdown allows you to swap between different components present in your scene.

<Video src="https://cdn.spline.design/_assets/docs/185b14b6-da3c-46cc-a792-7d2c4652952d.mp4" />

## Component Variations [#component-variations]

A great way to add versatility to your main component is by creating object variations that can be toggled visible/hidden based on what you want to show on your instances.

You can do this by creating different elements on your main component and hiding all the extra variations.

<Video src="https://cdn.spline.design/_assets/docs/7afeefd2-9130-4f3e-803d-f6766b1865eb.mp4" />

In your instances, you can now toggle visible/hidden variations to create different versions from your main component. While still keeping the connection to any changes made to the object variations made on the main component.

<Video src="https://cdn.spline.design/_assets/docs/db450205-3414-4580-8f23-add00ccd4a37.mp4" />
