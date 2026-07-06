# Duo Servo Brake Dialog Box

This Brake Designer dialog is used to edit the physical parameters of a duo-servo drum brake, in which the primary shoe drives the secondary shoe through a link, producing a self-energizing (servo) action. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions. (The previous manual titled this topic "Due Servo Brake"; the correct name is Duo Servo.)

## Wheel Cylinder

**Piston Diameter (in)**
Diameter of the wheel cylinder piston.

**Wheel Cyl. Dist (in)**
Distance from the brake center to the wheel cylinder actuation point.

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

The following parameters are entered separately for the primary (Pri) and secondary (Sec) shoes. Parameters that apply to only one shoe of a duo-servo brake are disabled for the other shoe.

**Lining Arc Length (in)**
Length of the lining material along the arc of contact with the drum.

**Lining Alph 1 (deg)** (labeled *Lining Alph 1* in the dialog — a UI typo for *Lining Alpha 1*)
Angle locating the leading edge of the lining relative to the shoe actuation axis. (Entered for the secondary shoe only.)

**Lining Beta (deg)**
Angle locating the lining relative to the shoe abutment. (Entered for the primary shoe only.)

**Lining Thickness (in)**
Thickness of the lining material.

**Abutment Dist (in)**
Distance from the brake center to the primary shoe abutment (the link between the shoes). (Entered for the primary shoe only.)

**Abutment Width/2 (in)**
Half-width of the shoe abutment. (Entered for the primary shoe only.)

**Abutment Angle (deg)**
Angle of the abutment contact surface. (Entered for the primary shoe only.)

**Abutment Friction**
Coefficient of friction at the abutment contact. (Entered for the primary shoe only.)

**Shoe Pin Radius (in)**
Radial distance from the center of the brake to the anchor pin for the pinned (secondary) shoe. (Entered for the secondary shoe only.)

**Shoe Block Length (in)**
Length of the shoe abutment block. (Entered for the secondary shoe only.)

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
*Source topic: DueServoBrkDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Dual Wedge Brake Dialog Box](DualWedgeBrkDlg.md)  |  [Index](README.md)  |  Next: [Duplex Brake Dialog Box](DuplexBrkDlg.md) →

<!-- /NAV -->
