# Material Properties Dialog

This dialog box allows the user to review and edit the material physical parameters associated with the current vehicle contact surface (interaction between the selected source and target segments). The dialog also includes a graph of the force-deflection relationship for the current parameters. Each numeric parameter may be edited either by dragging its slider or by typing directly into the adjacent edit field.

Note: The old help described these parameters as properties of "the terrain at X,Y"; they are in fact the properties of the selected vehicle contact-surface material.

This dialog contains the following parameters:

## Material Properties Graph
Graph of force vs. deflection for the current material parameters. It is redrawn when Apply is clicked.

## Material Name
A user-editable name describing the material assigned to the current contact surface.

## Constant
The force required to initiate deflection (lb; range 0–5,000). Default is 0.

## Linear Stiffness
The first-order force-deflection coefficient (lb/in; range -1,200 to 5,000). Default is 982.8 lb/in.

## Quadratic Stiffness
The second-order force-deflection coefficient (lb/in²; range -2,500 to 2,500). Default is -18.0 lb/in².

## Cubic Stiffness
The third-order force-deflection coefficient (lb/in³; range -100 to 3,500). Default is -3.4 lb/in³.

## Damping Constant
The velocity-dependent force contribution (lb-sec/in; range 0.0–5.0). Default is 0.55 lb-sec/in.

## Friction Constant
Friction coefficient multiplier for the contact surface (dimensionless; range 0.0–2.0). Default is 0.5.

## Maximum Force
The maximum (saturation) force the material can develop (lb; range 0–1,000,000). Default is 1,580 lb.

## Maximum Deflection
The deflection at which maximum force is reached (in; range 0–50). Default is 2.5 in.

## Unloading Slope
The first-order unloading force-deflection coefficient, applied beginning at maximum deflection (lb/in; range 0–1,000,000). Default is 740 lb/in.

## Max Defl / Time Step
The maximum change in deflection (penetration) allowed during a single integration time step (in; range 0–30). Default is 4.0 in.

## Print
Prints the displayed graph.

## Apply
Validates the entered values, saves them to the current material and redraws the graph with the new values.

## New
Resets the dialog to the "Default Vehicle Material" using the default values listed above.

## Open...
Opens a material from an HVE Material file (\*.matl) in the vehicle materials directory.

## Save As...
Saves the current settings to an HVE Material file (\*.matl) for later reuse.

## OK / Cancel
OK validates and accepts the material for the current contact surface; Cancel discards the changes.

---
*Source topic: MatPropDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Lining Friction Properties Dialog](LinFriPropDlg.md)  |  [Index](README.md)  |  Next: [New Ellipsoid Dialog](NewEllpDlg.md) →

<!-- /NAV -->
