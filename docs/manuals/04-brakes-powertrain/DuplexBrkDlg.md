# Duplex Brake Dialog Box

This Brake Designer dialog is used to edit the physical parameters of a duplex drum brake, in which each shoe is actuated by its own wheel cylinder and both shoes act as leading shoes. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions.

## Wheel Cylinder

**Piston Diameter (in)**
Diameter of the wheel cylinder pistons.

**Wheel Cyl. Dist (in)**
Distance from the brake center to the wheel cylinder actuation points.

**Push-out Pressure (psi)**
Pressure required to overcome force associated with return springs and begin developing brake torque.

## Shoe/Drum

**Drum Diameter (in)**
Inside diameter of the brake drum.

**Drum Lining Width (in)**
Width of the lining material.

**Drum Thickness (in)**
Thickness of the drum wall (used for calculating the thermal mass of the drum).

## Lining (Primary and Secondary columns)

The following parameters are entered separately for the primary (Pri) and secondary (Sec) shoes.

**Lining Arc Length (deg)**
Arc length of the lining material in contact with the drum.

**Lining Beta (deg)**
Angle locating the lining relative to the shoe abutment.

**Lining Thickness (in)**
Thickness of the lining material.

**Abutment Dist (in)**
Distance from the brake center to the shoe abutment. (The secondary shoe value follows the primary and is not directly editable.)

**Abutment Width (in)**
Width of the shoe abutment. (The secondary shoe value follows the primary and is not directly editable.)

**Abutment Angle (deg)**
Angle of the abutment contact surface. (The secondary shoe value follows the primary and is not directly editable.)

**Abutment Friction**
Coefficient of friction at the abutment contact. (The secondary shoe value follows the primary and is not directly editable.)

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical losses.

## Buttons and Results

**Friction ...**
Opens the Lining Friction Properties dialog, used to edit the lining friction coefficient as a function of lining temperature for the primary and secondary linings.

**Material ...**
Opens the Brake Designer Material Properties dialog, used to edit the drum and lining material thermal properties.

**Apply**
Recomputes the results below from the current physical parameters.

**Brake Factor** *(read-only)*
Calculated ratio of total drum drag force to actuation force for the brake.

**Actuation Factor** *(read-only)*
Calculated actuation force per unit of system pressure.

**Brake Torque Ratio (in-lb/psi)** *(read-only)*
Calculated wheel brake torque per unit of system pressure. On pressing OK, this value replaces the Brake Torque Ratio in the Brake Assembly dialog.

## Removed options

- **Preview** button — removed; the schematic preview drawing is now always displayed in the dialog.

---
*Source topic: DuplexBrkDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Duo Servo Brake Dialog Box](DueServoBrkDlg.md)  |  [Index](README.md)  |  Next: [Transmission Data Dialog Box](TransDataDlg.md) →

<!-- /NAV -->
