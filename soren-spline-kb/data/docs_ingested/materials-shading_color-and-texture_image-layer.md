# Image Layer (/materials-shading/color-and-texture/image-layer)



The Image layer allows you to upload, or generate with AI, an image to texture your 3D objects.

## How to create an Image Layer [#how-to-create-an-image-layer]

To add an image layer, you’ll need to:

1. Select an object and add a new layer on the Material Panel.
2. Change the layer to &#x2A;*“Image”** by clicking on the dropdown on the newly created layer.
3. Open the **Image Layer** settings by clicking on the layer thumbnail.

<Image src="https://cdn.spline.design/_assets/docs/4422b0e6-c8bd-47be-8141-734be8efaed7.png" alt="image" />

## Image Layer Settings [#image-layer-settings]

You can either upload an image or generate a texture with AI to get started.

### Mode [#mode]

Some layers, including Image Layer, can be used as masks, which you can do by selecting Mask on the layer mode. Learn more here: [Layer Masking](https://docs.spline.design/materials-shading/basics/layer-masking.md).

### Settings [#settings]

#### Projection [#projection]

Determines how the texture fits onto the model's surface, like adjusting a sticker on a curved or flat area.

* **UV** - Maps textures based on the model's UV coordinates.
* **Planar** - Projects the texture onto the model from a single direction.
* **Spherical** - Wraps the texture around the model as if it were a globe, ideal for round objects.
* **Cylindrical** - Applies the texture around the model like a label on a can, perfect for cylinder-shaped objects.
* **Triplanar** - Projects the texture from three directions and blends them, great for complex surfaces without clear orientation.

<Image src="https://cdn.spline.design/_assets/docs/4b89527a-8c79-4505-b35b-36aa7b3e96df.png" alt="image" maxWidth="300" />

#### Wrapping [#wrapping]

Decides how textures behave at edges, whether they repeat, stretch, or cut off.

* **Clamp** - Extends the edges of the texture to the bounds of the surface, preventing tiling but possibly stretching the edge pixels.
* **Repeat** - Tiles the texture across the surface, repeating it both horizontally and vertically.
* **Mirror** - Similar to repeat, but each tile is mirrored, creating a symmetrical tiling effect.

**Sharpness** - Adjusts texture clarity, making it crisp or smooth or pixelated.

**Crop** - Use the texture only on a part of the object without it being stretched.

**Scale** - Changes the texture's size on the model.

**Offset** - Moves the texture's position on the surface of the model.

**Rotation** - Spins the texture around a point, altering its angle on the model.

## Image Assets [#image-assets]

You can save your images as assets to reuse on other image layers.

To save an image asset, you’ll need to:

1. Select the object using the image you want to save.
2. Open the Image Layer panel.
3. On the Image Assets panel, press the + button on the top left, and your image asset will be saved

<Video src="https://cdn.spline.design/_assets/docs/8d1892ed-7a33-4f8c-b64d-1dfbe1ed4017.mp4" />

## Bump and Roughness Maps [#bump-and-roughness-maps]

The image layers added to your material can be used as bump and roughness maps.

[Bump Map & Roughness Map](https://docs.spline.design/materials-shading/surface-detail/bump-map-roughness-map.md)
