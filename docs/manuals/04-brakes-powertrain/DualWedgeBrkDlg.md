# Dual Wedge Brake Dialog Box

This Brake Designer dialog is used to edit the physical parameters of an air-actuated dual wedge drum brake, in which two air chambers drive wedges that spread the shoes against the drum. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions.

## Air Chamber

**Chamber**
Drop-down list selecting the air chamber size, by standard chamber type (Type 9, 12, 18, 20, 24, 30 or 36). Selecting a chamber type automatically sets the Chamber Area to the corresponding nominal effective area.

**Chamber Area (in^2)**
Effective diaphragm area of the air chamber. Set automatically from the selected chamber type; may also be edited directly. (The previous manual listed this as "Area, Primary Chamber".)

**Push-out Pressure (psi)**
Pressure required to overcome force associated with return springs and begin developing brake torque.

## Wedge

**Wedge Location (in)**
Location of the wedge actuation point relative to the brake center.

**Wedge Angle, Primary (deg)**
Included angle of the wedge actuating the primary shoe.

**Wedge Angle, Secondary (deg)**
Included angle of the wedge actuating the secondary shoe.

**Maximum Stroke (in)**
Maximum available stroke of the air chamber push rod.

**Stroke @ 2ndary Defl (in)**
Push rod stroke at which secondary (structural) deflection begins.

**2ndary Defl. Factor**
Factor describing the additional stroke consumed by secondary deflection after the secondary deflection stroke is reached.

**Expansion Coef (in/deg F)**
Thermal expansion coefficient of the drum; used to compute the additional stroke required as the drum heats and expands.

## Shoe/Drum

**Drum Diameter (in)**
Inside diameter of the brake drum.

**Drum Lining Width (in)**
Width of the lining material.

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

**Abutment Dist (in)**
Distance from the brake center to the shoe abutment. (The secondary shoe value follows the primary and is read-only.)

**Abutment Width (in)**
Width of the shoe abutment. (The secondary shoe value follows the primary and is read-only.)

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
*Source topic: DualWedgeBrkDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Dual Piston Brake Dialog Box](DualPistBrkDlg.md)  |  [Index](README.md)  |  Next: [Duo Servo Brake Dialog Box](DueServoBrkDlg.md) →

<!-- /NAV -->
