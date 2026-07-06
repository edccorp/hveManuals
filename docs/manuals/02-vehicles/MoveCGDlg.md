# Moving CG

**Move CG Dialog**

The default CG (center of gravity) location of the vehicle is determined from raw data (e.g., measured or table values). The user may choose to edit the CG location using the Move CG dialog. The entered offsets are displayed relative to the sprung-mass CG or the total-mass CG, according to the current Vehicle Dimensions Basis selected in the user options.

This dialog box contains the following items:

## Change Dx
Moves the CG in the +x or -x direction, relative to the vehicle-fixed coordinate system (+x is forward in the SAE coordinate system).

## Change Dy
Moves the CG in the +y or -y direction, relative to the vehicle-fixed coordinate system (+y is to the right in the SAE coordinate system). In HVE-2D this field is read-only.

## Change Dz
Moves the CG in the +z or -z direction, relative to the vehicle-fixed coordinate system (+z is down in the SAE coordinate system).

## CG Height
Approximate CG height, calculated from the vehicle wheel positions and the tire radius. Tire deflection is ignored. This field is read-only.

## Apply
Applies the entered CG movement to the vehicle without closing the dialog, so the effect can be inspected. OK applies the movement and closes the dialog.

---
*Source topic: MoveCGDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Inertia Dialog Box](InertiasDlg.md)  |  [Index](README.md)  |  Next: [Payload Dialog Box](PayLoadDlg.md) →

<!-- /NAV -->
