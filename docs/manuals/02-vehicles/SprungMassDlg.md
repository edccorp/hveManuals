# Sprung Mass Dialog

**Sprung Mass Dialog Box**

Clicking on the CG of the vehicle in the Vehicle Editor allows the user to edit the sprung mass parameter groups. Each button opens the dialog for the corresponding parameter group.

This dialog contains the following items:

## Inertias...
Displays the [Vehicle Inertia Dialog Box](VehInerDlg.md).

## Move CG...
Displays the [Move CG Dialog Box](MoveCGDlg.md).

## Color...
The color of the vehicle is obvious from looking at it. The color may be edited using the Color dialog.

## Geometry File...
The current vehicle may be visualized using a simplified vehicle shape or an actual 3-D geometry file created by digitizing the vehicle. If a 3-D geometry file is available for the current vehicle, it may be selected and displayed. (In HVE-2D this button is labeled **Exterior Geometry...**.)

## Refresh Geometry File
Reloads the current 3-D geometry file from disk, picking up any changes made to the file outside of HVE.

## Transform Geometry...
Displays the Transform Geometry dialog, used to translate, rotate or scale the vehicle's 3-D geometry. This button is available only when the vehicle uses a complex (file-based) geometry.

## Contact Surfaces...
Displays the [Contact Surfaces Dialog Box](../08-environment/ContSurfDlg.md). (Not available in HVE-2D.)

## Belt Restraints...
Displays the Belt Restraints Dialog Box. (Not available in HVE-2D.)

## Airbag Restraints...
Displays the [Airbag Restraints Dialog Box](../06-safety-systems/AirBagDlg.md). (Not available in HVE-2D.)

## Connections...
Displays the [Inter-Vehicle Connections Dialog Box](../09-events-driver-controls/IntrVehConnsDlg.md).

## Aerodynamic Drag...
Displays the [Aerodynamic Drag Dialog Box](VehDragDlg.md). (Not available in HVE-2D.)

## Body Torsion...
Displays the [Body Torsion Dialog Box](BodyTorDlg.md). (Not available in HVE-2D.)

## Handling...
Displays the Handling Properties dialog, a read-only summary of the vehicle's calculated handling parameters: total understeer gradient, steering wheel sensitivity, roll gradient, roll couple distribution, weight distribution, and static front/rear tire weights.

## Report Color...
Edits the color used to represent this vehicle in reports.

## Lights...
Displays the Lights dialog, used to configure the vehicle's lamps for visualization.

---
*Source topic: SprungMassDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Payload Dialog Box](PayLoadDlg.md)  |  [Index](README.md)  |  Next: [Stiffness Coefficient Dialog](StiffCoeffDlg.md) →

<!-- /NAV -->
