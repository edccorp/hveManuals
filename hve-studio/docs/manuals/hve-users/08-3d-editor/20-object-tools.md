# Chapter 20 — 3-D Editor Object Tools

## Overview

HVE's 3-D Editor creates environment objects with nine Object Tools — Surface, Cone, Box, Cylinder, Sphere, Text, Light, Signal and Edit — each with its own Object Editor dialog for size, position and orientation.

!!! warning "Not in HVE Studio"
    HVE Studio does not build environment geometry. There are no Surface, Cone, Box, Cylinder, Sphere or Text tools, no object editor dialogs, and no vertex editing. A site is **imported**:

    - from a geometry file — DXF, `.h3d`, `.iv`, OBJ or glTF — under **Environment › Environment… › Terrain › Scene Geometry** (enter or browse for the file, set the scale and axis options, tick **Use surfaces as terrain (physics)** if vehicles are to drive on it, and press **Import**); or
    - with an HVE case: **File › Open Case...** reads a `.hve` case, including the site built for it in HVE's 3-D Editor, with its object types, overlays and friction factors.

    Build or edit the site in HVE or in a modeling program and import the result. The tools that remain are described below.

The table maps each HVE tool to what HVE Studio offers:

| HVE tool | HVE Studio |
|---|---|
| Surface | Imported geometry; surface type and friction set per surface ([Chapter 19](19-using-3d-editor.md#object-attributes-tool)) |
| Cone, Cylinder, Sphere, Text | Not available |
| Box | Not available; see [Box Tool](#box-tool) |
| Light | The Environment panel's **Lights** section — point and spot site lights (below) |
| Signal | Not available; see [Signal Tool](#signal-tool) |
| Edit | Click to select in the Viewport ([Chapter 19](19-using-3d-editor.md#object-attributes-tool)); vehicles are moved with the gizmo ([Chapter 21](21-manipulators.md)) |

## Surface Tool

HVE's Surface tool creates drivable polygons (roads, medians, adjacent surfaces) vertex by vertex.

!!! warning "Not in HVE Studio"
    Surfaces come only from imported geometry. What HVE Studio does edit on an imported surface is its **Surface Type**, **Friction Multiplier** and other physical properties, its **layer**, whether it is **drawn** and whether it is **driven on**, and its display **material** — see [Chapter 19](19-using-3d-editor.md#object-attributes-tool). Reversing a surface's normals, moving vertices and changing object hierarchy are not available.

## Cone Tool

!!! warning "Not in HVE Studio"
    There is no Cone tool. Include delineators in the imported geometry.

## Box Tool

HVE's Box tool creates box-shaped objects such as buildings and curbs.

!!! warning "Not in HVE Studio"
    There is no Box tool and no Box Editor dialog. Include buildings, curbs and walls in the imported geometry (**Environment › Environment… › Terrain › Scene Geometry**: DXF, `.h3d`, `.iv`, OBJ or glTF), and draw drivable regions or friction zones over the site with the **Surface Generator** (Environment panel, *Surface Generator* section). See [Box Editor Dialog](../../08-environment/BoxEdDlg.md).

## Cylinder Tool

!!! warning "Not in HVE Studio"
    There is no Cylinder tool.

## Sphere Tool

!!! warning "Not in HVE Studio"
    There is no Sphere tool.

## Text Tool

!!! warning "Not in HVE Studio"
    There is no Text tool. Street names and other labels cannot be placed in the scene.

## Light Tool

HVE's Light tool adds point, directional and spot light sources (such as street lights) to the environment.

!!! note "HVE Studio"
    Site lights are made in the Environment Editor (F4), in the Environment panel's **Lights** section, not with a tool in the viewport. **Add Light** puts a light 8 m above the ground at the middle of the view; for each light you set its name, on/off, **On in daylight too**, type (**Point** or **Spot** — the sun is the only directional light), position (**X**, **Y**, **Height above the ground**), a spot's aim, tilt, cone and edge softness, and its color and intensity. They come on as the sky darkens, as vehicle lamps do, and light the 3-D view, the ray-traced render and the glTF export. While the Environment is selected, each is marked by a yellow star (gray when off) with a dotted line to the ground. No engine reads them. See [Environment Information › Lights](../../08-environment/EnvtInfoDlg.md#lights).

    **Vehicle › Editors › Vehicle Lights…** keeps each vehicle's own lamps, which move with it. Lamps modeled in a vehicle's mesh can be given an emissive material in the Shader Editor.

## Signal Tool

HVE's Signal tool creates traffic signal lights in the environment.

!!! warning "Not in HVE Studio"
    There is no Signal tool, and no traffic signal is drawn or recorded with the case. No engine models a traffic light.

## Edit Tool

HVE's Edit tool selects an object so that its attributes can be edited and a manipulator attached.

!!! note "HVE Studio"
    There is no separate Edit tool; clicking selects. In the Environment editor a click on a surface selects it for the Environment panel's Selected Surface section and the Shader Editor. In the Event editor a click on a vehicle selects it and shows its gizmo ([Chapter 21](21-manipulators.md)). In the Vehicle editor, **Tab** enters Edit Mode, in which a click picks a named part of the vehicle mesh. In the Environment editor, **Tab** enters Edit Mode, in which a click picks one face of the site ([Chapter 12](../05-environment-editor/12-creating-editing-environments.md#edit-mode-faces-of-the-site)).

---
*Converted and updated from the legacy HVE User's Manual (Seventh Edition, Jan 2006), Chapter 20; adapted for HVE Studio.*

<!-- NAV -->

---

← Previous: [Chapter 19 — Using the 3-D Viewport](19-using-3d-editor.md)  |  [Index](README.md)  |  Next: [Chapter 21 — Manipulators](21-manipulators.md) →

<!-- /NAV -->
