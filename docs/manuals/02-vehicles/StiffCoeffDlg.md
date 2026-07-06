# Stiffness Coefficient Dialog

**Stiffness Coefficients Dialog Box**

The vehicle's structural properties are defined by its stiffness coefficients. The user may choose to edit these coefficients for the front, back, sides, top or bottom of the vehicle using this dialog; the dialog title shows which surface is being edited (Front, Right Side, Rear, Left Side, Top or Bottom). Each value may be set either with its slider or by typing directly into the edit field.

**Note:** This dialog is used when HVE is running in 2-D mode. In 3-D mode, the Stiffness buttons in the Vehicle Dimensions dialogs open the Vehicle Exterior Stiffness dialog instead, which additionally supports 3-D (constant/linear/quadratic/cubic) stiffness definitions, saturation crush and maximum crush.

## Stiffness Coefficient A
Assigns the force per unit of damage width required to initiate permanent crush.

## Stiffness Coefficient B
Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush.

## Stiffness Coefficient Kv
Assigns the linear spring rate (force vs. deflection constant) per unit of damage width required to produce permanent crush. This value differs from the B constant in that it assumes the force vs. deflection graph goes through zero.

---
*Source topic: StiffCoeffDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Sprung Mass Dialog](SprungMassDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Drag Dialog](VehDragDlg.md) →

<!-- /NAV -->
