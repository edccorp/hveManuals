# CG To Bottom

**CG To Bottom Dialog Box**

The vehicle's exterior dimensions are defined by its overall length, width and height. The user may choose to edit these dimensions using the Vehicle Dimensions dialogs; the CG to Bottom dialog box is one among them.

## z Coord
Vehicle-fixed distance from the CG to the bottom of the vehicle.

## Ground Clearance
This value is read-only; it is calculated by the dialog as the difference between the CG height (calculated from the wheel positions and tire radius) and the entered CG-to-bottom distance. For vehicles without axles (e.g., fixed barriers) the ground clearance is zero. An error message is displayed if the entered distance would produce a negative ground clearance.

## Stiffness...
Displays the stiffness dialog for the bottom surface. In 3-D mode this is the Vehicle Exterior Stiffness dialog; otherwise it is the [Stiffness Coefficients Dialog Box](StiffCoeffDlg.md) (A, B and Kv). This button is disabled for Fixed Barrier and Movable Barrier vehicle types.

## Apply
Applies the entered dimension to the vehicle without closing the dialog. OK applies the value and closes the dialog; Cancel reverts the vehicle to its original dimensions and stiffness.

---
*Source topic: CGsToAll5.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [CG To Right](CGsToAll4.md)  |  [Index](README.md)  |  Next: [Inertia Dialog Box](InertiasDlg.md) →

<!-- /NAV -->
