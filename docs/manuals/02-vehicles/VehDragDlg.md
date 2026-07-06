# Vehicle Drag Dialog

**Vehicle Drag (Aerodynamic Drag) Dialog Box**

The vehicle drag associated with aerodynamic pressure. The Aerodynamic Drag dialog allows the user to view or edit these properties for each of the vehicle's aerodynamic surfaces. Each surface stores its own complete set of coefficients and center-of-pressure data.

## Surface
Selects the surface whose data is displayed. Available surface options are:

- Front
- Right
- Back
- Left
- Top
- Bottom
- FrontDevice
- BackDevice

## Device Installed
Switch that activates the selected surface. When unchecked, most of the fields for that surface are disabled (the coefficient fields and the Center of Pressure X and Y fields); the Projected Surface Area edit and the Center of Pressure Z label remain enabled. The surface produces no aerodynamic force.

## Drag Coefficient
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the direction of the vehicle's total velocity vector. The force associated with this pressure is proportional to the velocity squared.

## Lift Coefficient
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the direction normal (vertical) to the vehicle's total velocity vector.

## Side Coefficient
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the lateral direction, normal to the vehicle's total velocity vector.

## Projected Surface Area
Assigns the projected area parallel to the selected surface.

## Center of Pressure X
Vehicle-fixed X coordinate where the effective force from aerodynamic pressure is applied.

## Center of Pressure Y
Vehicle-fixed Y coordinate where the effective force from aerodynamic pressure is applied.

## Center of Pressure Z
Vehicle-fixed Z coordinate where the effective force from aerodynamic pressure is applied.

**Note:** The center-of-pressure coordinates are displayed relative to the sprung-mass CG or the total-mass CG, according to the current Vehicle Dimensions Basis selected in the user options.

---
*Source topic: VehDragDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Stiffness Coefficient Dialog](StiffCoeffDlg.md)  |  [Index](README.md)  |  Next: [Getting Information about the Vehicle](VehicleInfoDlg.md) →

<!-- /NAV -->
