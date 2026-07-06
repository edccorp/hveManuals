# Sphere Editor Dialog

The Sphere Object Tool allows the user to create and edit 3-D spheres. Spheres are useful for creating spherical or ellipsoidal shaped objects. The Sphere Editor dialog displays information about the current sphere object.

The dialog is divided into a position/orientation group on the left and a shape group on the right. Position labels display the units for the current unit system (e.g. ft, deg). Values typed into the dialog are applied to the selected sphere when the Apply button is pressed (pressing Enter is equivalent to Apply).

## Coordinates X

Displays and allows editing of the selected object's local or global X coordinate.

## Coordinates Y

Displays and allows editing of the selected object's local or global Y coordinate.

## Coordinates Z

Displays and allows editing of the selected object's local or global Z coordinate.

## Roll

Displays and allows editing of the selected object's local or global Roll orientation (degrees). Because a sphere is rotationally symmetric, orientation changes have no visible effect on the sphere's geometry itself, but they are stored with the object.

## Pitch

Displays and allows editing of the selected object's local or global Pitch orientation (degrees).

## Yaw

Displays and allows editing of the selected object's local or global Yaw orientation (degrees).

## Global/Local

Combo box selecting whether the coordinate and angle values are displayed and entered in the Global (world) reference frame or the sphere's Local reference frame. Options: *Global*, *Local*. Default: *Global*.

## Radius

Allows editing of the sphere's radius.

## Bind to

Radio buttons selecting what the coordinate fields are bound to when picking and editing:

- **Object** — the sphere as a whole (default).
- **Face** — an individual face of the sphere.
- **Vertex** — an individual vertex.

## Apply

Applies the values in the dialog to the selected sphere and registers the change with the undo/redo system, so the edit can be undone or redone. Pressing Enter (OK) also applies; pressing Esc (Cancel) is ignored — the dialog remains open.

---
*Source topic: SpereEdtDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [New Ellipsoid Dialog](NewEllpDlg.md)  |  [Index](README.md)  |  Next: [Surface Editor Dialog](SurfEdDlg.md) →

<!-- /NAV -->
