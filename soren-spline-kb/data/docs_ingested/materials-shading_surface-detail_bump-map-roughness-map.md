# Bump Map & Roughness Map (/materials-shading/surface-detail/bump-map-roughness-map)



Bump Map and Roughness Map create the illusion of depth and detail, making the material look more realistic without changing the object’s geometry. This way you can add details to your object without increasing polygons and affecting the performance of your scene.

## How to use a Bump Map [#how-to-use-a-bump-map]

A bump map is an image from which its luminance date (lighter/darker areas) are used to simulate concavity on the surface of your shapes. Spline will automatically capture the luminance from any image layer (color or black-and-white) and use it as the map.

1. Add an image layer with your bump map.
2. On the lighting layer, select either Phong or Physical.
3. Click on the lighting layer to assign a Bump Map to it.
4. Select the image you want to use as a Bump Map from the dropdown on the lightning layer's Bump map section.
5. Use the intensity parameter to control the appearance of the bump map.

<Video src="https://cdn.spline.design/_assets/docs/74b6d67d-3281-4e71-a4f5-7f01b4429d4d.mp4" />

## How to use a Roughness Map [#how-to-use-a-roughness-map]

A roughness map helps control how shiny or rough a surface appears in a 3D object. It uses the luminance (light/dark areas) of an image to guide how light interacts with the surface, making lighter areas look smooth and reflective and darker areas look rough and less reflective. Spline will automatically capture the luminance from any image layer (color or black-and-white) and use it as the map.

1. Add an image layer with your Roughness Map.
2. On the lighting layer, select Physical.
3. Click on the lighting layer to assign a Roughness Map to it
4. Select the image you want to use as a Roughness Map from the dropdown on the lightning layer's Rough Map section.
5. Use the Roughness, Metalness, and Reflectivity parameters to control the appearance of the Roughness Map.

<Video src="https://cdn.spline.design/_assets/docs/9d88a17c-a910-47bd-8803-4bfbfaa2bf15.mp4" />
