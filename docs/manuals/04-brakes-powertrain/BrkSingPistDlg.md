# Brake Designer Single Piston Dialog Box

This Brake Designer dialog (Single Piston, Leading/Trailing Shoe) is used to edit the physical parameters of a single-piston drum brake in which one wheel cylinder actuates a leading (primary) shoe and a trailing (secondary) shoe. Because some single-piston wheel cylinders use different piston areas on each end, the actuation force is calculated separately for the primary and secondary shoes. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions.

## Wheel Cylinder

**Area, Primary Piston (in^2)**
Cross-sectional area of the wheel cylinder piston acting on the primary (leading) shoe.

**Area, Secondary Piston (in^2)**
Cross-sectional area of the wheel cylinder piston acting on the secondary (trailing) shoe.

**Push-out Pressure (psi)**
Pressure required to overcome the force associated with the return springs and begin developing brake torque.

## Shoe/Drum

**Drum Diameter (in)**
Inside diameter of the brake drum.

**Drum Lining Width (in)**
Width of the lining material (and drum friction surface).

**Drum Thickness (in)**
Thickness of the drum wall (used for calculating the thermal mass of the drum).

## Lining (Primary and Secondary columns)

The following parameters are entered separately for the primary (Pri) and secondary (Sec) shoes.

**Lining Arc Length (in)**
Length of the lining material along the arc of contact with the drum.

**Lining Alph 1 (deg)** (labeled *Lining Alph 1* in the dialog — a UI typo for *Lining Alpha 1*)
Angle locating the leading edge of the lining relative to the shoe actuation axis.

**Lining Thickness (in)**
Thickness of the lining material.

**Shoe Pin Radius (in)**
Radial distance from the center of the brake to the anchor pin for pinned brake shoes. (The secondary shoe value follows the primary and is not directly editable.)

**Shoe lock Length (in)** (labeled *Shoe lock Length* in the dialog — a UI typo for *Shoe Block Length*)
Length of the shoe abutment block. (The secondary shoe value follows the primary and is not directly editable.)

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical (friction and linkage) losses.

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

---
*Source topic: BrkSingPistDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Brake Designer Material Properties Dialog Box](BrkMatPropDlg.md)  |  [Index](README.md)  |  Next: [Brake System Pressure vs Pedal Force Dialog Box](BrkSysVsPedFrcDlg.md) →

<!-- /NAV -->
