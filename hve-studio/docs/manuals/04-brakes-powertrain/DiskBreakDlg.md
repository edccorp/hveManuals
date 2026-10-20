# Disk Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE Studio has a single **Brake Designer** dialog for all of them: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...** and choose **Disc** in its **Brake Design** list. This page describes the parts of the Brake Designer every type shares, then the disc brake's own fields. The **Vehicle** list at the top selects the vehicle. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

![Brake Designer dialog, showing the Generic design](images/hvn-brake-designer.png)

## Wheel

### Axle, Side
Select the wheel whose brake design is shown (any axle of the vehicle). Each wheel keeps its own design.

### Brake Design
The brake type: **Generic (torque ratio)**, **Disc**, **Duo-Servo Drum**, **Duplex Drum**, **Single-Piston Drum**, **Dual-Piston Drum**, **S-Cam (Air Drum)**, **Single-Wedge (Air)**, **Dual-Wedge (Air)** or **Air Disc**. The **Design Parameters** below change with the type. **Generic** shows only a **Torque Ratio** and a **Pushout Pressure**, entered directly.

## Disc design parameters

**Number of Pistons**
Drop-down list selecting the number of caliper pistons (1 to 4).

**Piston Diameter**
Diameter of each caliper piston.

**Rotor Outer Diameter**
Outside diameter of the rotor.

**Rotor Inner Diameter**
Inside diameter of the rotor swept (friction) surface.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the pads after mechanical losses.

**Pushout Pressure**
Pressure required to overcome the caliper seal/return force and begin developing brake torque.

## Lining Friction Properties

A collapsible section (every type but Generic), HVE's **Friction ...** dialog:

- **Friction vs. Temperature (µ)**: a table of lining temperature (°C) against friction coefficient, with a plot of the curve. **x** deletes a row; **Add Row** adds one (up to six).
- **Friction Multiplier vs. Sliding Speed**: a table of sliding speed (in the units set in Preferences) against a friction multiplier, edited the same way.

## Results

Recomputed continuously from the current parameters (there is no Apply button), with the lining at 20 °C:

**Brake Factor** *(read-only)*
Calculated ratio of total rotor or drum drag force to actuation force for the brake.

**Actuation Factor** *(read-only)*
Calculated actuation force per unit of system pressure (shown in m²).

**Torque Ratio** *(read-only)*
Calculated wheel brake torque per unit of system pressure, in N·m/kPa (SI) or in·lb/psi (US).

## Apply to Wheel / Apply to All Wheels

**Apply to Wheel** writes the designed Torque Ratio and Pushout Pressure into the selected wheel's [Brake Assembly](BrkAsmblyDlg.md) data and sets its drum-or-disc Temperature Model to match the design (Generic leaves it as it was). **Apply to All Wheels** copies this design to every wheel and applies it to each. Choosing a design in Brake Assembly's **Brake Type** applies it the same way; edits made here afterwards reach the engines when you press Apply.

**Design...** in Brake Assembly opens this window on that wheel, on any axle of the vehicle.

## Drum data slots / Disc data slots

A collapsed section with the drum (S-cam) or disc hardware table for the selected wheel — whichever matches its type. It is recorded with the case and read by nothing, as the note in it says: the engine's brake-data block is filled from the design above it. It is kept so that a case can record the hardware. Until 2026-10-09 these were two all-wheel tables opened from Brake Assembly.

!!! note "HVE Studio"
    The engines compute brake torque from the Brake Assembly's **Torque Ratio** and **Pushout**; the design parameters themselves are not passed to them. The Brake Designer is the calculator that produces those two numbers.

!!! warning "Not in HVE Studio"
    - The schematic preview drawing of the brake.
    - A separate **Friction ...** dialog (it is a collapsible section here).
    - **Rotor Thickness**, the pad thicknesses and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.

<!-- NAV -->

---

← Previous: [Differential Data Dialog Box](DiffDataDlg.md)  |  [Index](README.md)  |  Next: [Drive Train Dialog Box](DriveTraDlg.md) →

<!-- /NAV -->
