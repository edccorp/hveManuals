# 3-D Editor Menu

The purpose of HVE's 3-D Editor is to provide a tool to create and edit 3-D objects used to visualize humans, vehicles and environments. In addition to providing visual information, the surfaces are also physical surfaces, with physical properties, including surface normal and friction properties, that simulate a physical environment for human and vehicle dynamics models.

!!! warning "Not in HVE 2027"
    HVE 2027 has **no 3-D Editor** and no 3-D Edit menu: there are no object creation tools (surface, cone, box, sphere, cylinder, text, light or signal tools), no manipulators and no 3-D Editor viewer layouts. 3-D objects are **imported**, not built inside the program.

## Where the 3-D Editor's jobs are done in HVE 2027

| HVE 3-D Editor item | HVE 2027 |
|---|---|
| Creating environment surfaces (roads, shoulders, buildings, ...) | Import the site's geometry from a file — DXF, HVE `.h3d`, Inventor `.iv`, OBJ or glTF — in the Environment Editor (**Environment (F4)**), **Environment** panel, **Terrain** section (*Scene Geometry*). An HVE case opened with **File › Open Case...** brings its environment with it. |
| Box tool | **Environment › Scene Box Editor...** adds named boxes with a position (x forward, y right, z up), a size (L, W, H) and a rotation. The boxes are for display; they are not drivable surfaces. |
| Object Attributes (type, friction, material name) | Each surface of the imported site has a **Surface Type** (Road, Friction Zone, Curb, Water or Other), friction and other physical properties, set in the Environment panel's **Surface Materials** list or in the **Shader Editor**. See [Object Attributes Dialog Box](ObjAttrDlg.md). |
| Material Color, Material Texture | **View › Shader Editor** edits a surface's or a vehicle part's material. In the Vehicle Editor, **Vehicle › Edit Mode (materials per part)** (Tab) lets you click a part of the vehicle in the viewport and give it a material. |
| Manipulators | Objects are moved in the **Viewport** with a gizmo: select a vehicle and drag its handles, or press **G** to move and **R** to rotate it, **X**, **Y** or **Z** to lock the motion to an axis, and type a number for an exact distance or angle. |
| Light tool | Not available. The scene is lit by the sun and the ambient light (**View › Shader Editor**, *Sun & Sky*), and by each vehicle's own lights (**Vehicle › Vehicle Lights...**). |
| Text tool, Signal tool | Not available. Traffic signal timing is entered in the Environment panel's **Signals** section and the event's **Signals** dialog (EDGEN). |
| Viewer layouts (XZ, YZ, XY, Perspective, All) | The **Viewport** panel's **Top**, **Front**, **Side**, **Momentum** and **3D** views. |
| Overlays | **View › Outliner** — see [Overlays Dialog Box](OverLayDlg.md). |

<!-- NAV -->

---

← Previous: [User Interface](README.md)  |  [Index](README.md)  |  Next: [Camera Setup Dialog Box](CameraSetDlg.md) →

<!-- /NAV -->
