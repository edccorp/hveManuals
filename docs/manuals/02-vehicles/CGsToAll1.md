# CG To Back

**CG To Back Dialog Box**

The vehicle's exterior dimensions are defined by its overall length and overall width. The user may choose to edit these dimensions using the Vehicle Dimensions dialogs; the CG to Back dialog box is one among them. The distance is displayed relative to the sprung-mass CG or the total-mass CG, according to the current Vehicle Dimensions Basis selected in the user options.

## x Coord
Vehicle-fixed distance from the CG to the back of the vehicle.

## Rear Overhang
Distance from the rear axle to the back of the vehicle. This value is read-only; it is calculated and displayed by the dialog based on the entered CG-to-back distance and the rear axle location.

## Overall Length
This value is read-only; it is calculated and displayed by the dialog from the entered CG-to-back distance and the CG-to-front distance.

## Stiffness...
Displays the stiffness dialog for the back surface. In 3-D mode this is the Vehicle Exterior Stiffness dialog; otherwise it is the [Stiffness Coefficients Dialog Box](StiffCoeffDlg.md) (A, B and Kv). This button is disabled for Fixed Barrier and Movable Barrier vehicle types.

## Apply
Applies the entered dimension to the vehicle without closing the dialog. OK applies the value and closes the dialog; Cancel reverts the vehicle to its original dimensions and stiffness.

---
*Source topic: CGsToAll1.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [CG To Front](CGsToAll.md)  |  [Index](README.md)  |  Next: [CG To Top](CGsToAll2.md) →

<!-- /NAV -->
