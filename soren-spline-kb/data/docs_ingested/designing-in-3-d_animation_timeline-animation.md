# Timeline Animation (/designing-in-3-d/animation/timeline-animation)



Spline’s timeline animation lets you bring your 3D designs to life with smooth, keyframe-based motion. You can animate properties like position, rotation, scale, and much more over time, making it easier to define the timing of your animations. Refine the flow of your keyframe transitions with the built-in graph editor.

<Embed src="https://www.youtube.com/embed/RoDQpvi8HbA" title="YouTube video player" />

## How to create a timeline animation [#how-to-create-a-timeline-animation]

To create a timeline animation, click the timeline toggle in the toolbar. This will open the timeline panel at the bottom of the screen, where you can start adding and adjusting keyframes.

<Video src="https://cdn.spline.design/_assets/docs/c9117ce9-5aeb-48b6-894a-7ba87960b6c1.mp4" />

## How to start animating objects [#how-to-start-animating-objects]

1. Select the object you want to animate in the viewport or outliner.
2. Click the Animate button in the timeline to add the property you want to animate. Or select a preset animation.
3. Once the object is on the timeline, edit it in the viewport or properties panel — new keyframes will be recorded automatically.

<Video src="https://cdn.spline.design/_assets/docs/d655b03f-b2d3-43dc-8d86-0a7ea36554af.mp4" />

## The Graph Editor [#the-graph-editor]

The Graph Editor allows you to fine-tune your animations by adjusting the speed and easing of keyframes. Instead of linear motion, you can edit the animation curves to create smoother, more natural, or dynamic transitions.

<Image src="https://cdn.spline.design/_assets/docs/a0623277-3e01-480f-8ecf-0bd8559f29dc.png" alt="image" />

## Create multiple timelines [#create-multiple-timelines]

You can create multiple timelines from the timelines panel by pressing the + button.

This is useful for organizing animations of different groups of objects into cleaner timelines or triggering different types of animations for the same objects.

<Image src="https://cdn.spline.design/_assets/docs/16b2a861-6a95-486c-a752-c473993a2a0d.png" alt="image" />

## How to play a timeline in Play Mode [#how-to-play-a-timeline-in-play-mode]

To play a timeline in Play Mode, you need to trigger it with an event.

The most common way is to use a **Start** event with a **Timeline Animation action**, which will play the timeline on the first load of your scene. You can also use any other event to trigger a timeline animation.

<Image src="https://cdn.spline.design/_assets/docs/2ee4e281-38e2-4326-9803-0ca675295881.png" alt="image" />

## Timeline Animation Action [#timeline-animation-action]

The Timeline Animation action lets you play a timeline through the events system, connecting animations to specific triggers.

<Image src="https://cdn.spline.design/_assets/docs/bb41638e-07d9-48cb-8ffe-05429e7d3b93.png" alt="image" maxWidth="300" />

## Exporting a timeline as video [#exporting-a-timeline-as-video]

To export the timeline as video, follow these steps:

* Click on "Export" in the top right corner of your Spline Scene
* Select the Timeline you would like to export in the "Timeline" dropdown
* Choose duration of your export (tip: match it with your timeline length)
* Select FPS and Resolution.

<Video src="https://cdn.spline.design/_assets/docs/7bd3f79a-ca67-4dae-bac5-984a9ce629db.mp4" />

## Animatable Properties [#animatable-properties]

* Transform
  * Position
  * Rotation
  * Scale
* Size
* Material
* Material Opacity
* Cloner
* Align to Path
* Path Extrusion
