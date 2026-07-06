# CG To Right

**CG To Right Side Dialog Box**

The vehicle's exterior dimensions are defined by its overall length and overall width. The user may choose to edit these dimensions using the Vehicle Dimensions dialogs; the CG to Right dialog box is one among them.

## y Coord
Vehicle-fixed distance from the CG to the right side of the vehicle.

## Overall Width
This value is read-only; it is calculated and displayed by the dialog from the entered CG-to-right distance and the CG-to-left distance.

## Copy to Other Side
When checked, the entered distance (and stiffness) is also applied to the left side of the vehicle, keeping the vehicle symmetric. In HVE-2D this option is always checked and cannot be changed.

## Stiffness...
Displays the stiffness dialog for the right surface. In 3-D mode this is the Vehicle Exterior Stiffness dialog; otherwise it is the [Stiffness Coefficients Dialog Box](StiffCoeffDlg.md) (A, B and Kv). This button is disabled for Fixed Barrier and Movable Barrier vehicle types.

## Apply
Applies the entered dimension to the vehicle without closing the dialog. OK applies the value and closes the dialog; Cancel reverts the vehicle to its original dimensions and stiffness.

---
*Source topic: CGsToAll4.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [CG To Left](CGsToAll3.md)  |  [Index](README.md)  |  Next: [CG To Bottom](CGsToAll5.md) →

<!-- /NAV -->
