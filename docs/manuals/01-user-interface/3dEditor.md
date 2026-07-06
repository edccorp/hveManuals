# 3-D Editor Menu

The purpose of the 3-D Editor is to provide the user a tool to create and edit 3-D objects used to visualize humans, vehicles and environments. In addition to providing visual information, the surfaces are also physical surfaces, with physical properties, including surface normal and friction properties, that simulate a physical environment for human and vehicle dynamics models.

The 3-D Edit menu contains the following items:

## Launch 3-D Editor (Ctrl+L)

Launches the 3-D Editor.

## Material Color

Used to set the material color of the selected object. The Material Color dialog box is displayed; set the color using that dialog.

## Material Texture

Displays the Texture Editor dialog box.

## Manipulators

Choose a manipulator for the selected object. Choosing Manipulators from the menu displays a cascade menu listing the various manipulators available for manipulating (positioning and orienting) objects using the 3-D Editor. The following manipulators are available:

- **Direct** — No manipulator is used. Instead, the user clicks directly on the object and moves it.
- **Jack** — Scales the selected object in all directions; no translation or rotation.
- **Trackball** — Used for 3-dimensional rotation of the selected object; no translation.
- **Centerball** — Translates the object center to new X,Y,Z coordinates and rotates the object about the new center.
- **Handle Box** — Provides 3-dimensional translation and scaling of the selected object.
- **Transform Box** — Scales the object in all directions; translates and rotates the object in the selected direction.
- **Tab Box** — Translates the object in the selected plane.

## Object Tools (Toolbar)

The 3-D Editor is used for creating and editing the objects used by HVE. These objects are broadly categorized as human, vehicle or environment objects. The user creates and edits these objects using the 3-D Editor's selection of creation and editing tools.

An object, such as a surface or sphere, is always created by first selecting an object tool from the toolbar. The following object tools are available:

- **Surface Tool** — Used for creating surfaces, such as roads, shoulders and adjacent highway environment.
- **Cone Tool** — Used for creating cone-shaped objects, such as traffic cones.
- **Box Tool** — Used for creating box-shaped objects, including buildings, sidewalks and bridges.
- **Sphere Tool** — Used for creating spherical and ellipsoidal shaped objects, such as commercial building signs.
- **Cylinder Tool** — Used for creating cylindrical-shaped objects, such as signs, sidewalk corners and tanks.
- **Text Tool** — Used for labeling objects such as signs, buildings and vehicles.
- **Light Tool** — Used for creating light sources in the environment.
- **Signal Tool** — Used for creating traffic signal lights in the environment.
- **Edit Tool** — Used for editing existing objects.

## Object Attributes

Every object created using the 3-D Editor has attributes (name, type, overlay, material, friction factor, and related properties). Choosing this option displays the Object Attributes dialog box. For more information, see [Object Attributes Dialog Box](ObjAttrDlg.md).

## Viewer

Displays the 3-D Editor Viewer Options dialog. Use the *Show Viewer(s)* drop-down to select which viewer layout is displayed while editing: the XZ (side), YZ (front), or XY (plan) orthographic viewer, the Perspective viewer, or All (all four viewers at once).

## Close 3-D Editor

Closes the 3-D Editor and returns to the Environment Editor. Changes made to the current object are automatically applied to that object.

---
*Source topic: 3dEditor.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [User Interface](README.md)  |  [Index](README.md)  |  Next: [Camera Setup Dialog Box](CameraSetDlg.md) →

<!-- /NAV -->
