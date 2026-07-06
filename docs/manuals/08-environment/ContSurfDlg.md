# Contact Surfaces Dialog

The current vehicle may include contact surfaces used for simulating interaction forces between the vehicle and its occupants or pedestrians.

Contact surfaces are planes defined by 3 corners (the fourth corner is automatically assigned by assuming a parallelogram). Contact surfaces are created using the Contact Surfaces dialog box.

This dialog is used for assigning contact surfaces to the current vehicle. A vehicle may have up to 25 contact surfaces.

This dialog contains the following parameters:

## Contact Surface
Select the contact surface from the combo box to edit its properties.

## Location
Radio buttons assigning the location attribute of the current surface:

- **Interior** — assigns the Interior attribute, used by the simulation model to identify surfaces on the vehicle's interior (occupant simulation).
- **Exterior** — assigns the Exterior attribute, used by the simulation model to identify surfaces on the vehicle's exterior (pedestrian simulation).

## Bind Material To
Radio buttons determining whether the material is associated with individual vertices, with polygonal areas, or with the whole group. The setting applies to the vehicle's contact-surface set as a whole:

- **Vertex** — the material is bound to each vertex.
- **Face** — the material is bound to each face (polygonal area).
- **Group** — the material is bound to the surface group.

These buttons are disabled until at least one contact surface exists.

## Corners (Counter-Clockwise)
Assigns the vehicle-fixed x, y, z coordinates (in inches) for the three corners — **First**, **Middle** and **Third** — of the contact surface. The fourth corner is assigned automatically by assuming a parallelogram. The corner coordinates are validated when the surface is saved; invalid (degenerate) coordinates are rejected.

## Material Name
Displays the name of the material assigned to the current contact surface (read-only in this dialog; edit it in the Material Properties dialog). Newly added surfaces are assigned the "Default Vehicle Material".

## Add
Adds a contact surface. A New Contact Surface dialog prompts for the surface name; the name must be non-empty and unique. The new surface is created with corner coordinates of 0,0,0 and the default vehicle material (linear stiffness 982.8 lb/in, friction 0.5, maximum force 1580 lb, maximum deflection 2.5 in, unloading slope 740 lb/in). No more than 25 surfaces may be added.

## Delete Surface
Deletes the current contact surface (after a confirmation prompt).

## Material...
Displays the [Material Properties Dialog Box](MatPropDlg.md) for the current contact surface.

## OK / Cancel
OK validates the corner coordinates and saves the contact surfaces to the vehicle; Cancel discards the changes.

---
*Source topic: ContSurfDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Cone Editor Dialog](ConeEdtDlg.md)  |  [Index](README.md)  |  Next: [Cylinder Editor Dialog](CylinEdDlg.md) →

<!-- /NAV -->
