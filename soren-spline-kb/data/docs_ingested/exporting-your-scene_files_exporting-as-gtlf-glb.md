# Exporting as GTLF/GLB (/exporting-your-scene/files/exporting-as-gtlf-glb)



GLTF and GLB are open-source file formats for 3D scenes and models, used in games, web apps, AR, VR, and more.

<Image src="https://cdn.spline.design/_assets/docs/4bf5d7a5-9da1-4396-9dd3-1cd4f7c46e42.png" alt="image" />

1. Once you're happy with your scene, press the Export button on the toolbar.
2. Scroll down to select "3D Formats" under *Files* section from the export sidebar.
3. Choose either “GLTF” or “GLB” from the *Format* dropdown.
4. Choose “Default Color (Grey)” or “Color & Texture” from *Material* dropdown and click Export.

#### Material types [#material-types]

Following material types can be selected for export:

* **Default Color (Grey)** → Exports only the scene geometry with default grey color material.
* **Color & Texture** → Exports the scene geometry with material layers (Color layer), including textures. (⚡ Paid feature, included in **Pro** and **Max** subscriptions.)

<Callout>
  Some material layers are not fully supported by the GLTF & GLB format. Texture support is limited to only primitive geometries with UV projection mode. No texture support for geometries with “Smooth & Edit”.
</Callout>

#### ✅ Supported features [#supported-features]

* Geometry
* Color Layer
* Textures (Only Basic Support)
* Timeline Animations (Position, Rotation, and Scale only — baked into glTF animation tracks)

#### ❌ Not supported features [#not-supported-features]

* All Material Layers
* Post-Processing
* Animation of materials, shape size, cloners, opacity, camera lens parameters, and light color/intensity
* Physics
* Environment, Lighting, and Fog
* States, Events, and Interactivity
* Assets, Components, and Variables
