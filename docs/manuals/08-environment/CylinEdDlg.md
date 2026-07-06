# Cylinder Editor Dialog

The Cylinder Object Tool allows the user to create and edit 3-D cylinders. Cylinders are useful for creating telephone poles, signposts and numerous other objects. The Cylinder Editor dialog displays information about the current cylinder object.

The dialog is divided into a position/orientation group on the left and a shape group on the right. Position labels display the units for the current unit system (e.g. ft, deg); the labels are refreshed from the language/units resources whenever the dialog is activated, so changing the unit options updates the displayed units. Values typed into the dialog are applied to the selected cylinder when the Apply button is pressed (pressing Enter is equivalent to Apply).

## Coordinates X

Displays and allows editing of the selected object's local or global X coordinate.

## Coordinates Y

Displays and allows editing of the selected object's local or global Y coordinate.

## Coordinates Z

Displays and allows editing of the selected object's local or global Z coordinate.

## Roll

Displays and allows editing of the selected object's local or global Roll orientation (degrees).

## Pitch

Displays and allows editing of the selected object's local or global Pitch orientation (degrees).

## Yaw

Displays and allows editing of the selected object's local or global Yaw orientation (degrees).

## Global/Local

Combo box selecting whether the coordinate and angle values are displayed and entered in the Global (world) reference frame or the cylinder's Local reference frame. Options: *Global*, *Local*. Default: *Global*.

## Radius

Allows the user to edit the cylinder's radius.

## Length

Allows the user to edit the cylinder's length (the height of the cylinder along its axis).

## Bind to

Radio buttons selecting what the coordinate fields are bound to when picking and editing:

- **Object** — the cylinder as a whole (default).
- **Face** — an individual face of the cylinder.
- **Vertex** — an individual vertex.

## Apply

Applies the values in the dialog to the selected cylinder and registers the change with the undo/redo system, so the edit can be undone or redone. Pressing Enter (OK) also applies; pressing Esc (Cancel) is ignored — the dialog remains open.

---
*Source topic: CylinEdDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Contact Surfaces Dialog](ContSurfDlg.md)  |  [Index](README.md)  |  Next: [Environment Material Properties Dialog](EnvrMatPropDlg.md) →

<!-- /NAV -->
