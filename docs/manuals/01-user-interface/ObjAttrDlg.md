# Object Attributes Dialog Box

Every object created using the 3-D Editor has the following attributes:

## Object Name

The Object Name is simply the name of the object tool used to create the object (e.g., *surface, box, cylinder*, etc.). If the selected object is a group composed of several individual objects, the Object Name is *Group*. If the grouped object was selected from the Highway Furnishings Library, the Object Name is the object's filename. This field is read-only.

## Type

Every object created by the 3-D Editor has an Object Type attribute. The available types are:

- **Human** — The default object type attribute for humans.
- **Vehicle** — The default object type for vehicles.
- **Road** — The default object type for environments. Road objects have physical properties (surface elevation, normal and friction factor) used by the current reconstruction or simulation model.
- **Friction Zone** — An optional object type. Friction Zone objects have physical properties (surface elevation, normal and friction factor) used by the current reconstruction or simulation model.
- **Curb** — An optional object type identifying the object as a curb for calculation models that include curb impacts.
- **Water** — An optional object type identifying the surface as water. Selecting Water enables the Water Depth controls (see below).
- **Other** — An optional object type for purely visual objects.

## Overlay

Every object created using the 3-D Editor belongs to a named overlay. Examples of named overlays are *Accident Debris* and *Measured Skids*.

HVE maintains a list of current overlay names. This list is available in the [Overlays Dialog Box](OverLayDlg.md), displayed by choosing Overlays from the View menu. The user may display or remove one or more overlays using the Overlays dialog.

Overlays serve several very useful purposes. Some examples are:

- Overlays may be used to show an accident scene as it appeared before and after the accident by creating overlays named Accident Debris and Skidmarks. Turning off these overlays shows the scene as it appeared before the accident; turning them on shows the scene after the accident.
- An overlay may be used to compare simulated and measured skidmarks.
- A scanned image (bitmap) overlay may be used to compare a 3-D model of the accident site with a photograph to confirm the model's accuracy.

## Material Name

A user-editable name identifying the material assigned to the object (e.g., asphalt, gravel). The name is stored with the object and shown in surface information output.

## Friction Factor

Objects created using the 3-D Editor have friction properties. This friction factor is a user-editable object attribute used by the current calculation model to determine the frictional properties of the surface.

Use this option to create regions with different frictional properties from the base surface. Examples include gravel shoulders, oil slicks and other regions.

## Water Depth (in)

Available when the object Type is *Water*. Two options are provided:

- **Static** (first radio button, with depth field) — The water has the user-entered constant depth over the surface.
- **Dynamic** — The water depth is determined dynamically from the water surface elevation and the underlying terrain.

## Material Edit...

Displays the Material Editor dialog box, used to edit the visual material (color, texture) of the object.

## Apply

Applies the current attribute settings to the selected object.

## Group / UnGroup / Load / Save

A row of picture buttons at the bottom of the dialog:

- **Group** — Combines the currently selected objects into a single group object.
- **UnGroup** — Breaks the selected group back into its individual objects.
- **Load** — Loads a previously saved object (e.g., from the Highway Furnishings Library) into the scene.
- **Save** — Saves the selected object or group to a file so it can be re-used in other environments.

---
*Source topic: ObjAttrDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Light Editor Dialog Box](LightEdDlg.md)  |  [Index](README.md)  |  Next: [Options Menu](OptionsMenu.md) →

<!-- /NAV -->
