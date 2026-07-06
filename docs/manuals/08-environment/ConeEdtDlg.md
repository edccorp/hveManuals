# Cone Editor Dialog

The Cone Object Tool allows the user to create and edit 3-D cones. Cones are useful for creating highway delineator cones and simple trees. The Cone Editor dialog box displays information about the current cone object.

The dialog is divided into a position/orientation group on the left and a shape group on the right. Position labels display the units for the current unit system (e.g. ft, deg); the labels are refreshed from the language/units resources whenever the dialog is activated, so changing the unit options updates the displayed units. Values typed into the dialog are applied to the selected cone when the Apply button is pressed (pressing Enter is equivalent to Apply).

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

Combo box selecting whether the coordinate and angle values are displayed and entered in the Global (world) reference frame or the cone's Local reference frame. Options: *Global*, *Local*. Default: *Global*.

## Radius

Allows editing of the cone's base (bottom) radius.

## Length

Allows editing of the cone's length (the height of the cone from base to apex).

## Bind to

Radio buttons selecting what the coordinate fields are bound to when picking and editing:

- **Object** — the cone as a whole (default).
- **Face** — an individual face of the cone.
- **Vertex** — an individual vertex.

## Apply

Applies the values in the dialog to the selected cone and registers the change with the undo/redo system, so the edit can be undone or redone. Pressing Enter (OK) also applies; pressing Esc (Cancel) is ignored — the dialog remains open.

---
*Source topic: ConeEdtDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Box Editor Dialog](BoxEdDlg.md)  |  [Index](README.md)  |  Next: [Contact Surfaces Dialog](ContSurfDlg.md) →

<!-- /NAV -->
