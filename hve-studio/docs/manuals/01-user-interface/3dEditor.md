# 3-D Editor Menu

The purpose of HVE's 3-D Editor is to provide a tool to create and edit 3-D objects used to visualize humans, vehicles and environments. In addition to providing visual information, the surfaces are also physical surfaces, with physical properties, including surface normal and friction properties, that simulate a physical environment for human and vehicle dynamics models.

!!! warning "Not in HVE Studio"
    HVE Studio has **no 3-D Editor** and no 3-D Edit menu: there are no object creation tools (surface, cone, box, sphere, cylinder, text, light or signal tools), no manipulators and no 3-D Editor viewer layouts. 3-D objects are **imported**, not built inside the program. HVE's manipulators could move, rotate and scale a selected surface, box or cylinder; HVE Studio moves and turns the whole site or one of its surfaces (below), but does not scale a surface.

## Where the 3-D Editor's jobs are done in HVE Studio

| HVE 3-D Editor item | HVE Studio |
|---|---|
| Creating environment surfaces (roads, shoulders, buildings, ...) | Import the site's geometry from a file — DXF, HVE `.h3d`, Inventor `.iv`, OBJ or glTF — in the Environment Editor (**Environment (F4)**), **Environment** panel, **Terrain** section (*Scene Geometry*). An HVE case opened with **File › Open Case...** brings its environment with it. |
| Box tool | Not available. Model box-shaped objects (curbs, walls, buildings) in the site geometry and import it (**Environment › Environment... › Terrain › Scene Geometry**); draw a drivable region or friction zone with the **Surface Generator** (Environment panel). See [Box Editor Dialog](../08-environment/BoxEdDlg.md). |
| Object Attributes (type, friction, material name) | Each surface of the imported site has a **Surface Type** (Road, Friction Zone, Curb, Water or Other), friction and other physical properties, set for the surface selected in the viewport or **View › Outliner** (the Environment panel's **Selected Surface** section) in the **Shader Editor**. See [Object Attributes Dialog Box](ObjAttrDlg.md). |
| Material Color, Material Texture | **View › Shader Editor** edits a surface's or a vehicle part's material. In the Vehicle Editor, **Vehicle › Edit Mode (materials per part)** (Tab) lets you click a part of the vehicle in the viewport and give it a material; its **Faces** switch picks single faces and **Make Part** turns them into a part of their own. |
| Manipulators | In the Event Editor the **Viewport** gizmo moves a vehicle (and its scene positions): select it and drag its handles, or press **G** to move and **R** to rotate it, **X**, **Y** or **Z** to lock the motion to an axis, and type a number for an exact distance or angle. In the Environment Editor **G**, **R** and **S** move, turn and scale the **site** -- or, with a surface selected, **that surface**, and with several selected, all of them together about their common centre -- the same way; the Environment panel's **Site Placement** fields (*Scene Geometry*) and the selected surface's **Placement** fields (*Selected Surface*) hold the same numbers. The solver drives on the moved ground. On a site taken from an HVE case the road moves only with the whole site, because the case keeps it twice (the polygons the solver drives on and the picture drawn over them); its scenery moves on its own. In the Vehicle Editor **G**, **R** and **S** move, rotate and scale the vehicle's **mesh** (its picture and its collision mesh): **X**, **Y** or **Z** lock an axis (with **R**, X and Y roll and pitch by moving the mouse up or down), a typed number is exact (metres, degrees or a factor), **Enter** or a click keeps it and **Esc** or a right click puts it back; they edit the same Translate, Rotate and Scale rows as **Vehicle › Editors › Vehicle Mesh...**. A site's scale and up axis are set when it is imported, and a point cloud is placed by its offsets in the Environment panel. |
| Light tool | Not available. The scene is lit by the sun and the ambient light (**View › Shader Editor**, *Sun & Sky*), and by each vehicle's own lights (**Vehicle › Editors › Vehicle Lights...**). |
| Text tool, Signal tool | Not available. HVE Studio has no traffic signal objects and no signal timing. |
| Viewer layouts (XZ, YZ, XY, Perspective, All) | The **Viewport** panel shows one 3-D view. Click a face of the view cube in its top-right corner for a top, front, back, left, right or bottom view in orthographic projection, or use the number keys. |
| Overlays | **View › Outliner** — see [Overlays Dialog Box](OverLayDlg.md). |

<!-- NAV -->

---

← Previous: [User Interface](README.md)  |  [Index](README.md)  |  Next: [Camera Setup Dialog Box](CameraSetDlg.md) →

<!-- /NAV -->
