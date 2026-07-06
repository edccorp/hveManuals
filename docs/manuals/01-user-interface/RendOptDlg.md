# Render Dialog Box

Sets various options that affect the visual appearance of all 3-D objects displayed by HVE.

## Humans and Vehicles — Show As

Separate *Show As* options are provided for humans and for vehicles:

- **Human — Actual** — HVE displays humans using the object's 3-D geometry file.
- **Human — Simple** — HVE displays humans as ellipsoids.
- **Vehicle — Actual** — HVE displays vehicles using the object's 3-D geometry file.
- **Vehicle — Simple** — HVE displays vehicles as simplified boxy-shaped objects.

> Note: The Human *Show As* options (Actual/Simple) are currently disabled (grayed out) in the dialog.

## Render Method (Shading)

HVE provides the following render methods:

- **Phong** — Phong shading is required for realistic images. Only if Phong shading is selected are special lighting and shading calculations performed. Because of these calculations, Phong shading also has the longest rendering time.
- **Flat** — Displays each object according to its user-defined color(s). However, no lighting or shading calculations are performed, so objects appear less realistic compared to Phong shading; objects are rendered more quickly.
- **Wireframe** — Shows only the edges of each object; no surfaces are displayed. The resulting display is fast but realism is lost. Wireframe mode is often useful as a construction technique during model building in the 3-D Editor.
- **Hidden** — Like Wireframe, except it includes depth calculations; objects hidden behind other objects are not displayed. Like Wireframe, hidden line mode is often useful as a construction technique during model building in the 3-D Editor.

## Complexity

The Complexity option specifies whether objects are drawn relative to object space or screen space:

- **Object** — All the object's polygons are rendered, regardless of the distance from the camera.
- **Screen** — HVE uses the object size and distance from the camera to decide whether to render all the object's polygons or just render its pixels at some average color.

> Note: The Complexity options are currently disabled (grayed out) in the dialog.

## Show Only Faces

When checked, surfaces are rendered with backface culling, i.e., polygons are drawn as one-sided faces. Polygons whose normals face away from the camera disappear, making it easy to identify surfaces whose normals point the wrong way — such surfaces will not work correctly with the physics models. This option is available only when the *Phong* or *Flat* render method is selected.

## Light Sources On

Turns user-created light sources (created with the Light Tool in the 3-D Editor) on or off in the rendered scene.

> Note: The Light Sources On check box is currently disabled (grayed out) in the dialog.

## Render Quality

A user-definable range (1 to 10) which defines how finely objects are subdivided (tessellated). The default value is 5. If a value less than 5 is entered, objects like cones and spheres appear more blocky and surfaces may have unrendered areas. Selecting a value greater than 5 results in smoother cones and spheres; the appearance of surfaces may or may not improve (depending on how they were created). There is a trade-off between speed and image quality.

## Texture Quality

A user-definable range that controls the resolution at which surface textures are rendered. Higher values produce sharper textures at the cost of rendering speed and texture memory; lower values render faster but textures appear blurrier.

> Note: The Texture Quality slider and edit field are currently disabled (grayed out) in the dialog.

## Anti-Aliasing Level

A user-definable range (1 to 10) which defines how smoothly objects are rendered. The default value is 1. If a value greater than 1 is selected, objects are re-rendered up to 10 times (depending on the selected value), resulting in a significant improvement in image quality. However, rendering time is increased significantly.

---
*Source topic: RendOptDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Report Window Dialog Box](PrevWnd.md)  |  [Index](README.md)  |  Next: [Select Object Dialog Box](SelObjDlg.md) →

<!-- /NAV -->
