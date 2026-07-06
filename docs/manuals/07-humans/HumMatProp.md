# Human Material Properties Dialog Box

This dialog is used to view and edit the human material assigned to the current contact ellipsoid (see the [Human Contact Ellipsoids Dialog Box](Human1.md)). Material properties may be edited directly, and material files may be opened and saved for later application. Each numeric property is edited either with its slider or by typing into the adjacent edit field.

This dialog box contains the following items:

## Human Material Graph
The area at the top of the dialog displays a plot of the material's force-deflection curve, computed from the current property values (constant, linear, quadratic and cubic stiffness terms, limited by the maximum force/deflection and unloading slope). Press Apply to redraw the graph after editing values.

## Material Name
User-editable material name.

## Constant (lb)
Force required to initiate deflection.

## Linear Stiffness (lb/in)
Linear material deformation coefficient.

## Quadratic Stiffness (lb/in²)
Quadratic material deformation coefficient.

## Cubic Stiffness (lb/in³)
Cubic material deformation coefficient.

## Damping Constant (lb-sec/in)
Material velocity-dependent deformation constant.

## Friction Constant
Inter-segment friction coefficient (dimensionless).

## Maximum Force (lb)
Force at which the 3rd order force-deflection relationship is abandoned.

## Maximum Deflection (in)
Deflection at which the 3rd order force-deflection relationship is abandoned.

## Unloading Slope (lb/in)
Linear unloading slope, applied beginning at maximum deflection.

## Max Deff / Time Step (in)
Maximum allowed change in deflection (penetration) per integration time step. This limits how far the contact deflection may advance in a single simulation time step.

## Print
Prints the current graph.

## Apply
Redraws the graph using the current values.

## New
Resets all properties to the built-in "Default Human Material" values (Constant 0.0 lb, Linear Stiffness 982.8 lb/in, Quadratic Stiffness -18.0 lb/in², Cubic Stiffness -3.4 lb/in³, Damping Constant 0.55 lb-sec/in, Friction 0.5, Maximum Force 1580.0 lb, Maximum Deflection 2.5 in, Unloading Slope 740.0 lb/in, Max Deff/Time Step 4.0 in) and redraws the graph.

## Open
Opens an existing human material file (HVE Material Files, *.matl) and loads its values into the dialog.

## Save As
Saves the current settings in a human material file (*.matl).

---
*Source topic: HumMatProp.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Human Joint Properties Dialog Box](HumJntPropDlg.md)  |  [Index](README.md)  |  Next: [Selected Humans & Vehicles Dialog Box](SelHumVehDlg.md) →

<!-- /NAV -->
