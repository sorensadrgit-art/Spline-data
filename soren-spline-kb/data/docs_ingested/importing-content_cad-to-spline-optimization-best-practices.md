# CAD to Spline: Optimization Best Practices (/importing-content/cad-to-spline-optimization-best-practices)

> Prepare CAD models from SolidWorks, Fusion 360 and similar tools for use in Spline.



This guide outlines best practices for converting CAD models from tools such as **SolidWorks, Fusion 360, Solid Edge, Rhino**, and others into optimized 3D assets suitable for **real-time, web-based experiences**. These guidelines help ensure efficient performance for product showcases, interactive demos, configurators, and more.

For general tips on optimizing scenes in Spline, check out the [**How to optimize your scene**](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md) guide.

### 🧱 1. Prepare and Simplify Your CAD Model [#-1-prepare-and-simplify-your-cad-model]

#### Clean Up Geometry [#clean-up-geometry]

In your CAD software:

* **Remove unnecessary details** that won't be visible in the final 3D scene (e.g., internal parts, small screws, fine fillets).
* **Hide or delete hidden components** to avoid exporting redundant geometry.
* **Consolidate geometry** where possible:
  * Merge similar or repeated parts into a single object.
  * Standardize materials and colors — identical objects should use the same material definition.

***

### 📤 2. Export from CAD as Mesh [#-2-export-from-cad-as-mesh]

#### General Export Strategy [#general-export-strategy]

1. **Convert NURBS/solids to mesh:**
   * Most CAD programs offer a way to convert solids into mesh geometry (polygonal).
   * Look for settings like *Mesh Refinement*, *Deviation*, or *Chord Tolerance*.
2. **Adjust tessellation settings:**
   * Use fewer polygons when the visual fidelity doesn't suffer.
   * Tune parameters like:
     * **Distance Deviation / Chord Height:** Higher values → lower polygon count.
     * **Angle Deviation / Normal Tolerance:** Controls detail in curved surfaces.
3. **Choose the Right Export Format**
   * Recommended formats: `.GLB`, `.STL`, `.OBJ`, or `.FBX`.
   * Ensure correct **units** (e.g., mm vs. cm) and **normal orientation** during export.
   * **Geometry merging options**:
     * If your model uses a single material, merging all parts into one mesh can improve performance.
     * For complex models or when maintaining object-level control is important, export as **separate objects**— Spline allows merging later.

***

### 🛠️ 🤖 3. Optimize for Spline [#️--3-optimize-for-spline]

#### Mesh Optimization [#mesh-optimization]

* Ensure **clean topology**:
  * Avoid n-gons, intersecting geometry, and non-manifold edges.
  * Merge elements that use the same material.
* Keep object count and polygon count low:
  * **Target:** 50k–150k polygons max.
  * Fewer objects generally means better real-time performance.

#### Other Tips [#other-tips]

* Use **descriptive object names** (`base_plate`, `screw_cap`) to aid scene organization.
* Limit the number of **materials and textures** — reuse materials wherever possible.

***

### 🧪 4. Import into Spline [#-4-import-into-spline]

1. Drag and drop your exported `.obj`, `.glb`, `.stl`, or `.fbx` file into the Spline canvas.
2. Add up to two **directional lights** for efficient real-time shadows.
3. For complex models:
   * Use **20 materials or fewer**.
   * Compress large image textures and avoid using too many.
4. Leverage Spline’s interactive tools to add animation, hover effects, or interactivity.
5. Use the **Performance Panel** and Play Settings on Export to:
   * Enable mesh and texture compression.
   * Adjust scene settings for real-time performance.

🔗 [Read more in the optimization guide](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md)
