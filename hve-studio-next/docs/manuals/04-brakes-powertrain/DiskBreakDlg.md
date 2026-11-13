# Disk Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE Studio has a single **Brake Designer** for all of them, a table with one column per wheel: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...** and choose **Disc** in a wheel's **Brake Design** list. This page describes the parts of the Brake Designer every type shares, then the disc brake's own fields. The **Vehicle** list at the top selects the vehicle. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

![Brake Designer dialog, showing the Generic design](images/hvn-brake-designer.png)

## The table

One column per wheel (**A1 Left**, **A1 Right**, ... on every axle of the vehicle); each wheel keeps its own design. The **Brake Group** row sets each wheel's group (**B1**, **B2**, ..., and **Layout...**), the same groups as the [Brake Assembly](BrkAsmblyDlg.md)'s: an edit to a wheel is made to every wheel of its group.

### Brake Design
The brake type: **Generic**, **Disc**, **Duo-Servo**, **Duplex**, **Single Piston**, **Dual Piston**, **S-Cam**, **Single Wedge**, **Dual Wedge** or **Air Disc** (HVE's full names in the open list). The rows below follow the designs: a row appears when some wheel's design uses it, and a wheel whose design does not shows `--` there. A **Generic** wheel has only a **Pushout Pressure** and a **Torque Ratio**, which are the Brake Assembly's own values.

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

A collapsible section under the table for the wheel the **Wheel:** buttons pick (every type but Generic), HVE's **Friction ...** dialog:

- **Friction vs. Temperature (µ)**: a table of lining temperature (°C) against friction coefficient, with a plot of the curve. **x** deletes a row; **Add Row** adds one (up to six).
- **Friction Multiplier vs. Sliding Speed**: a table of sliding speed (in the units set in Preferences) against a friction multiplier, edited the same way.

## Results

The rows at the bottom of the table, recomputed continuously from the current parameters, with the lining at 20 °C:

**Brake Factor** *(read-only)*
Calculated ratio of total rotor or drum drag force to actuation force for the brake.

**Actuation Factor** *(read-only)*
Calculated actuation force per unit of system pressure (shown in m²).

**Torque Ratio** *(read-only)*
Calculated wheel brake torque per unit of system pressure, in N·m/kPa (SI) or in·lb/psi (US).

## Apply / Apply all wheels

The **Brake Assembly** row reads **applied** when the wheel's [Brake Assembly](BrkAsmblyDlg.md) has its design's brake type and torque ratio. After an edit it shows **Apply**, which writes the designed Torque Ratio and Pushout Pressure into the Brake Assembly of the wheel and every wheel of its brake group, and sets the drum-or-disc Temperature Model to match the design (Generic leaves it as it was). **Apply all wheels**, under the table, applies every wheel not yet applied. Choosing a design in the **Brake Design** row, or in Brake Assembly's **Brake Type**, applies it at once.

**Design...** in Brake Assembly opens this window with that wheel picked, on any axle of the vehicle.

!!! note "HVE Studio"
    A wheel whose design is not **Generic** has its brake torque recomputed at every step of a simulation from this design: the brake factor at the simulated lining temperature and sliding speed, the actuation factor, and for S-cam, wedge and air disc brakes the stroke factor (see [Chapter 29](../hve-users/10-brake-designer/29-brake-designer.md)). A **Generic** wheel runs on the Brake Assembly's **Torque Ratio** and **Pushout**.

!!! note "Removed in HVE Studio 2026-10-21"
    The **Drum data slots** / **Disc data slots** section, the old S-Cam Brake and Disc Brake tables' values for the selected wheel, is gone. Nothing read those values; the engine's brake data comes from the design above. A case saved before then loads normally and the old values are dropped.

!!! warning "Not in HVE Studio"
    - The schematic preview drawing of the brake.
    - A separate **Friction ...** dialog (it is a collapsible section here).
    - A separate **Material ...** dialog: it is the **Material** and **Thicknesses** rows of the table here (see [Brake Designer Material Properties](BrkMatPropDlg.md)).

<!-- NAV -->

---

← Previous: [Differential Data Dialog Box](DiffDataDlg.md)  |  [Index](README.md)  |  Next: [Drive Train Dialog Box](DriveTraDlg.md) →

<!-- /NAV -->
