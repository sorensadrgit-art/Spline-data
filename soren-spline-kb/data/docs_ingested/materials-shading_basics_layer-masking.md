# Layer Masking (/materials-shading/basics/layer-masking)



Layer masking allows selective control of the visibility or transparency of specific areas within a material. It involves using greyscale to determine which parts of the masked layer are visible or hidden. Closer to white will be more visible and closer to black will be more hidden.

This technique is helpful for texturing, compositing, and creating complex visual effects to texture your 3D objects.

<Video src="https://cdn.spline.design/_assets/docs/1f1b8a0b-d721-4d08-863b-86e560c06eda.mp4" />

The following layers support Mask Mode:

* [Image Layer](https://docs.spline.design/materials-shading/color-and-texture/image-layer.md)
* [Noise Layer](https://docs.spline.design/materials-shading/color-and-texture/noise-layer.md)
* [Pattern Layer](https://docs.spline.design/materials-shading/color-and-texture/pattern-layer.md)
* [Metcap Layer](https://docs.spline.design/materials-shading/shading-and-reflection/matcap-layer.md)
* [Video Layer](https://docs.spline.design/materials-shading/color-and-texture/video-layer.md)
* [Depth Layer / 3D Gradient](https://docs.spline.design/materials-shading/shading-and-reflection/depth-layer-3d-gradient.md)
* [Gradient Layer](https://docs.spline.design/materials-shading/color-and-texture/gradient-layer.md)
* [Fresnel Layer](https://docs.spline.design/materials-shading/shading-and-reflection/fresnel-layer.md)
* [Rainbow Layer](https://docs.spline.design/materials-shading/color-and-texture/rainbow-layer.md)

## How to create a Layer Mask [#how-to-create-a-layer-mask]

To create a layer mask, you’ll need to:

1. Select a layer that supports Mask Mode or add a new one on the Material Panel.
2. Open the layer settings by clicking the layer thumbnail and select Mask Mode.
3. Add the layer you want to mask right below the Mask layer.

<Callout>
  Remember to use greyscale on your mask. White where you want your masked layer to be visible and black where you want it to be hidden.
</Callout>

<Video src="https://cdn.spline.design/_assets/docs/136d4ece-c02c-4936-9ff0-a0df67cc2f9e.mp4" />

When a layer is in Mask Mode, it becomes purple and has an arrow pointing to the layer below (the layer that is masked).

The Mask will only mask one layer, which is right below it.

<Image src="https://cdn.spline.design/_assets/docs/54d7aec5-c826-47e8-b283-22c9098568e3.png" alt="image" maxWidth="400" />
