# Disk Brake Dialog Box

This Brake Designer dialog is used to edit the physical parameters of a hydraulic disc (caliper) brake. The dialog includes a schematic preview drawing of the brake, updated to reflect the current dimensions.

## Caliper

**Number of Pistons**
Drop-down list selecting the number of caliper pistons (1, 2 or 3).

**Piston Diameter (in)**
Diameter of each caliper piston.

**Push-out Pressure (psi)**
Pressure required to overcome the caliper seal/return force and begin developing brake torque.

## Rotor

**Outside Diameter (in)**
Outside diameter of the rotor.

**Inside Diameter (in)**
Inside diameter of the rotor swept (friction) surface.

**Rotor Thickness (in)**
Thickness of the rotor (used for calculating the thermal mass of the rotor).

## Lining (Inner and Outer columns)

The following parameters are entered separately for the inner and outer pads.

**Pad Thickness (in)**
Thickness of the pad lining material.

**Incl. Angle (deg)**
Included angle of the pad (the arc of the rotor surface covered by the pad).

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the pads after mechanical losses.

## Buttons and Results

**Friction ...**
Opens the Lining Friction Properties dialog, used to edit the pad friction coefficient as a function of lining temperature.

**Material ...**
Opens the Brake Designer Material Properties dialog, used to edit the rotor and pad material thermal properties.

**Apply**
Recomputes the results below from the current physical parameters.

**Brake Factor** *(read-only)*
Calculated ratio of total rotor drag force to actuation force for the brake.

**Actuation Factor** *(read-only)*
Calculated actuation force per unit of system pressure.

**Brake Torque Ratio (in-lb/psi)** *(read-only)*
Calculated wheel brake torque per unit of system pressure. On pressing OK, this value replaces the Brake Torque Ratio in the Brake Assembly dialog.

## Removed options

The following entries from the previous manual are no longer present in this dialog:

- **Number of Rotors** — removed; the model uses a single rotor per wheel.
- **Middle Pad Thickness** — removed; pad thickness is now entered per inner/outer pad.
- **Preview** button — removed; the schematic preview drawing is now always displayed in the dialog.

---
*Source topic: DiskBreakDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Differential Data Dialog Box](DiffDataDlg.md)  |  [Index](README.md)  |  Next: [Drive Train Dialog Box](DriveTraDlg.md) →

<!-- /NAV -->
