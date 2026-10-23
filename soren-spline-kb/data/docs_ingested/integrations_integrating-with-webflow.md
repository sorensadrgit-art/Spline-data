# Integrating with Webflow (/integrations/integrating-with-webflow)



<Callout>
  If you have ideas, feature requests, or bug reports in regards to Webflow integration please send your feedback to us at [help@spline.design](mailto:help@spline.design).
</Callout>

Add interactive 3D content to your websites without the need to write code with the Webflow Integration called Spline Embed.

You can control many of the interactions of your Spline scene directly within Webflow. This allows the use of Webflow Events (e.g.: click, hover, mouse position, scroll) to manipulate the position, rotation, and scale of the available Spline objects.

To learn more about how to use it follow the steps and tips in this doc.

<Video src="https://cdn.spline.design/_assets/docs/b831f709-2b09-40bc-b51e-4c125ac54e76.mp4" />

## Exporting from Spline [#exporting-from-spline]

1. Open a Spline Scene.
2. Click on “**Export**” in the top toolbar.
3. Select “**Spline Viewer**”
4. Copy the scene link at the top. It should look like this: `https://prod.spline.design/HqdfCmOueigtautT/scene.splinecode `→ feel free to grab this scene to test embedding Webflow.

## Adding Spline Scene in Webflow [#adding-spline-scene-in-webflow]

Inside the Webflow editor, follow these steps to add a Spline Scene:

1. Click the “+” icon on the left toolbar
2. Under “Elements” search for the “Media” section
3. Click on “Spline Scene”
4. There is a default Spline Scene included in the “URL” input field. Paste your own Spline URL (see previous step [Exporting from Spline](#exporting-from-spline)).
5. Click on “Show All Settings” to get access to all the Webflow settings.

To learn more about how to style and size the Spline Scene on your website, check the following docs from Webflow:

* [Style Panel Overview in Webflow](https://university.webflow.com/lesson/style-panel-overview)
* [Element Settings Panel in Webflow](https://webflow.com/glossary/element-settings-panel)

<Image src="https://cdn.spline.design/_assets/docs/1045ce55-0945-42c9-84a0-f69ef4b877a6.png" alt="image" maxWidth="300" />

<Image src="https://cdn.spline.design/_assets/docs/bd73b283-cca5-45c3-87a4-e7818bc18065.png" alt="image" maxWidth="300" />

## Controlling the Spline scene from Webflow [#controlling-the-spline-scene-from-webflow]

<Video src="https://cdn.spline.design/_assets/docs/bdf9c4e1-1a29-41a3-af96-51a22b76721f.mp4" />

1. Select “⚡️ – Interactions” in the right sidebar top corner.
2. Create a new trigger (Element trigger or Page trigger), for this exercise select “**Mouse move in viewport*&#x2A;” with the “&#x2A;*+**” icon next to “**Page trigger**”.
3. Select the trigger.
4. Add an animation (”+” icon next to Mouse Animations).
5. Open the animation with the “⚙️ – cogwheel icon”.
6. At Mouse X Action click on the “+” icon and select “Spline” at the “Integrations” section → This unlocks access to Spline objects.
7. At 0% select the “Spline” object.
8. At the bottom of the sidebar next to “object” select from the dropdown the object you would like to manipulate → “Geometry” in the case of the example in the video.
9. Set the “Geometry” initial position, scale, and rotation, you need to define a value in order to take effect (default values will be ignored from the animation)
10. Now select the Spline object at 100% and there you should be defined by how much should be the object’s position, rotation, and scale be transformed.
11. Now preview the experience with the “👁️ – preview icon” in the top toolbar.
12. Done! Moving the mouse over the webpage should animate the Spline object.

<Image src="https://cdn.spline.design/_assets/docs/4ba0e411-7f5b-474e-b6e7-420165bbcf73.png" alt="image" maxWidth="300" />

## Previewing Spline scene in Webflow [#previewing-spline-scene-in-webflow]

In Webflow following options are available to preview your Spline Scene interactions

* **Option 1** → Click on the “👁️ – Toggle Preview” icon in the top toolbar
* **Option 2** → Publish the site in Webflow and load the page to see the Spline scene in action.

## Update Spline scene in Webflow [#update-spline-scene-in-webflow]

#### 1. In Spline [#1-in-spline]

1. Make an update in the Scene (e.g.: change the color of an object),
2. Click on Export
3. Select the Spline Viewer tab
4. Click on Update → Wait until the updates get pushed

#### 2. In Webflow [#2-in-webflow]

<Callout>
  In the case of an already published Webflow project, just reload the website that contains the Spline Embed and your most recent Spline update will be visible.
</Callout>

To see the update in the Webflow Editor follow these steps:

1. Select the Spline Scene.
2. In the right sidebar select “Element Settings”
3. At the “Spline Scene Settings” section click on “Reload Spline Scene”
4. Done, the updates are live!

## Best practices [#best-practices]

* **Scene optimization** → Learn to optimize your scene to make sure your scene loads quickly and runs efficiently on all sorts of devices. [How to optimize your scene](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md)
* **Various screen sizes** → To match your scene with responsive behaviours use the Screen Resize Event and match it with the breakpoints from your Webflow environment. [Screen Resize Event](https://docs.spline.design/interaction-states-events-and-actions/events/screen-resize-event.md)
