# Dual Piston Brake Dialog Box

The brake factor for a dual piston drum brake (Dual Piston, 2 Leading Shoes) is calculated by assuming the primary and secondary shoes are each a pinned leading shoe. Like a single piston brake, some dual piston drum brakes use a different piston area for the primary and secondary shoes. Therefore, the actuation force is calculated separately for the primary and secondary shoes. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions.

This dialog box contains the following attributes:

## Wheel Cylinder

**Area, Primary Piston (in^2)**
Cross-sectional area of the wheel cylinder piston acting on the primary shoe.

**Area, Secondary Piston (in^2)**
Cross-sectional area of the wheel cylinder piston acting on the secondary shoe.

**Push-out Pressure (psi)**
Pressure required to overcome force associated with return springs and begin developing brake torque.

## Shoe/Drum

**Drum Diameter (in)**
Inside diameter of the brake drum.

**Drum Lining Width (in)**
Width of lining material.

**Drum Thickness (in)**
Thickness of the drum wall (used for calculating the thermal mass of the drum).

## Lining (Primary and Secondary columns)

The following parameters are entered separately for the primary (Pri) and secondary (Sec) shoes.

**Lining Arc Length (in)**
Length of the lining material along the arc of contact with the drum.

**Lining Alph 1 (deg)** (labeled *Lining Alph 1* in the dialog — a UI typo for *Lining Alpha 1*)
Angle locating the leading edge of the lining relative to the shoe actuation axis.

**Lining Thickness (in)**
Thickness of lining material.

**Shoe Pin Radius (in)**
Radial distance from the center of the brake to the anchor pin for pinned brake shoes. (The secondary shoe value follows the primary and is not directly editable.)

**Shoe Block Length (in)**
Length of the shoe abutment block. (The secondary shoe value follows the primary and is not directly editable.)

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
*Source topic: DualPistBrkDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Drive Train Dialog Box](DriveTraDlg.md)  |  [Index](README.md)  |  Next: [Dual Wedge Brake Dialog Box](DualWedgeBrkDlg.md) →

<!-- /NAV -->
