# Section Eight: 3-D Editor

HVE's 3-D Editor is a separate editing session in which the user builds and edits environment geometry (surfaces, boxes, cones, text, lights) with Open Inventor manipulators, assigns object types, overlays and friction factors, and groups objects into a library.

!!! note "HVE Studio"
    HVE Studio has no separate 3-D Editor and no Launch 3-D Editor command. All 3-D work happens in the **Viewport** panel (**View › Viewport**), the same view used for every editor mode and for playback. What the 3-D Editor did is divided as follows:

    - **Navigating and viewing** — the Viewport's views, mouse and keyboard controls, rendering modes and overlays ([Chapter 19](19-using-3d-editor.md)).
    - **Environment geometry** — imported, not built: **Environment › Environment… › Terrain › Scene Geometry** reads DXF, `.h3d`, `.iv`, OBJ and glTF sites, and an HVE `.hve` case brings its own site with it. Roads and friction zones are drawn over it with the **Surface Generator** ([Chapter 20](20-object-tools.md)).
    - **Object attributes** — each surface's type and friction are set for the surface selected in the Viewport or the **Outliner** (the **Selected Surface** section of **Environment › Environment… › Terrain**) and in the Surface node of the **Shader Editor**; HVE's overlays are the layers of the **Outliner** (**View › Outliner**) ([Chapter 19](19-using-3d-editor.md)).
    - **Manipulators** — one gizmo with keyboard operators (G move, R rotate) for positioning vehicles and scene positions in the Event editor ([Chapter 21](21-manipulators.md)).

## General Procedure

To edit a scene in HVE Studio, perform the following steps:

1. Select the **Environment (F4)** editor tab.
2. Open **Environment › Environment…**. In the **Terrain** section, under **Scene Geometry**, enter or browse for a geometry file and press **Import**. (A `.hve` case opened with **File › Open Case...** already carries its site.)
3. Click a surface in the Viewport, or pick it in the **Outliner**, and set its **Surface Type** and **Friction Multiplier**.
4. Use the **Outliner** to show, hide and re-layer surfaces, and the **Shader Editor** to change how they look.
5. Save the case (**File › Save Case**). The case carries the site's geometry inside it, as an HVE case does; unticking **File › Embed the environment in the case** makes it name the geometry file instead.

## Overview of Section Eight

This section describes the HVE Studio equivalents of HVE's 3-D Editor:

- [Chapter 19](19-using-3d-editor.md) describes the Viewport: views, navigation, selection, surface attributes, layers, materials, rendering and overlays.
- [Chapter 20](20-object-tools.md) describes HVE's Object Tools and what HVE Studio offers in their place (imported geometry, the Surface Generator, signals and lights).
- [Chapter 21](21-manipulators.md) describes the HVE Studio gizmo and the G/R keyboard operators that replace HVE's manipulators.
- Chapter 22 (reserved for future use)
- [Chapter 23](23-tutorial.md) provides a short tutorial: importing a site, setting surface properties, using layers and positioning a vehicle.
- Chapter 24 (reserved for future use)
- Chapter 25 (reserved for future use)

## Related Reference Pages

- [3-D Editor Menu](../../01-user-interface/3dEditor.md) (HVE)
- [Object Attributes Dialog Box](../../01-user-interface/ObjAttrDlg.md) (HVE)
- [Overlays Dialog Box](../../01-user-interface/OverLayDlg.md) (HVE)
- Object editor dialogs (HVE): [Surface](../../08-environment/SurfEdDlg.md), [Cone](../../08-environment/ConeEdtDlg.md), [Box](../../08-environment/BoxEdDlg.md), [Cylinder](../../08-environment/CylinEdDlg.md), [Sphere](../../08-environment/SpereEdtDlg.md), [Text](../../01-user-interface/TextEdDlg.md), [Light](../../01-user-interface/LightEdDlg.md)

---
*Converted and updated from the legacy HVE User's Manual (Seventh Edition, Jan 2006), Section Eight; adapted for HVE Studio.*

<!-- NAV -->

---

Next: [Chapter 19 — Using the 3-D Viewport](19-using-3d-editor.md) →

<!-- /NAV -->
