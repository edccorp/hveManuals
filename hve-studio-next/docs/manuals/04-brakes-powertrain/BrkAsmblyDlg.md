# Brake Assembly Dialog Box

The Brake Assembly properties of the wheels are displayed and edited using the **Brake Assembly** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Assembly...**, or with **Brakes...** › **Brake Assembly...** under **Components** in the Vehicles panel. The **Vehicle** list at the top selects the vehicle.

![Brake Assembly dialog](images/hvn-brake-assembly.png)

Where HVE edits one wheel at a time, HVE Studio shows a table with one column per wheel (**A1 Left**, **A1 Right**, **A2 Left**, ...). Pressures and torque ratios are shown in the units set in Preferences. Values take effect as they are typed; while results are on screen the vehicle is locked.

This dialog contains the following parameters.

## Brake Group

A button per group above each wheel, numbered **B1**, **B2**, ... up to the number of wheels (a drop-down when there are more than four). Every wheel is in a group; a wheel alone in its group edits alone. One group per wheel serves the brakes as a whole: an edit in the Brake Designer is made to every wheel of the group as it is made, and its **Apply** writes that design into every wheel's assembly, the ABS System and ABS Designer edit the same row, and a wheel that joins a group takes the group's brake design with its assembly. Wheels in the same group share their values: an edit in one column is copied to every other wheel in the group, and moving a wheel into a group that already has a member copies that member's values to it. By default the wheels whose brakes are identical share a group, numbered in wheel order, and a dual-tire wheel never shares one with a single-tire one. The groups are saved with the case, and **Undo** reverses a group change. This replaces HVE's *Copy to Other Side* and *Copy to Other Axles*.

**Layout...**, beside the group row's name, sets the usual arrangements in one step: **Same both sides** (each axle's left and right wheels in a group of their own), **Same on every wheel** (one group), and **Each wheel its own** (every wheel in a group of its own, so an edit changes only that wheel). The arrangement the wheels are in now is checked; none is when the groups are a mix of them. A new group takes the values of its first wheel, A1 Left first. Under **Copy once** it does what HVE's *Copy to Other Side* and *Copy to Other Axles* do: pick a wheel under **From**, then **To the other side**, **To the other axles** (the same side of every other axle) or **To every wheel**. The copy changes no group, and a wheel copied to takes its group mates with it. Pointing at a column outlines it and tints the wheels in its group, the ones an edit there will change; they stay marked while the field is being edited.

## Brake Type & Design

### Brake Type
HVE's brake type for each wheel, listed with HVE's own labels: **Generic Brake**, **Disc Brake**, **Duo-Servo Brake**, **Duplex Brake**, **Single Piston, Leading/Trailing Shoe**, **Dual Piston, 2 Leading Shoes**, **S-Cam**, **Single Wedge**, **Dual Wedge** or **Air Disc Brake** (shortened in the table cell, for example *1-Piston*). It is the same setting as the **Brake Design** list of the [Brake Designer](DiskBreakDlg.md).

- **Generic**: the **Pushout** and **Torque Ratio** below are what the engine brakes with, as you enter them.
- **A design**: choosing it computes the Pushout and Torque Ratio from the wheel's design (as HVE does on the same change), and they are shown read-only. Edit the design with **Design...**.

### Design...
One button per wheel. It opens the **Brake Designer** on that wheel, in its design. It is grayed for a Generic wheel, which has nothing to design.

### Temperature Model
Shown, not edited: **Drum** or **Disc**, which brake temperature model the engines run. A design sets it; a Generic wheel keeps the case's. The engines take **one per axle, from the right wheel**, and a note says so when the right and left wheels of an axle differ (HVE warns about this too). The brake temperature model's inputs are the Brake Designer's **Material** and **Thicknesses** rows.

## Actuation

### Time Lag (s)
Time required before the driver's brake pedal inputs reach the wheel.

### Time Rise (s)
Time required for the brake system pressure at the wheel to begin causing the maximum brake torque as specified by the Brake Torque Ratio.

### Pushout
Brake system pressure required to begin causing brake torque (any system pressure below this point is simply taking out the slack in the system).

### Torque Ratio
Wheel brake torque per unit of system pressure at the wheel. The actual braking torque at the wheel is the product of the current wheel system pressure and the Brake Torque Ratio. **Apply to Wheel** in the Brake Designer writes the designed Torque Ratio and Pushout here.

## Options

### Proportioning
Check if the system pressure at the wheel is reduced by a proportioning value.

### P-Start
Proportioning starting pressure, the valve's knee: beginning at this level of system pressure, any additional master cylinder pressure is reduced. It sits with Proportioning and is grayed on a wheel where Proportioning is off, since no engine reads it there.

### Proportion Ratio
At master cylinder pressure above P-Start, additional pressure is reduced by this ratio (grayed where Proportioning is off): the wheel sees P-Start + (P − P-Start) × ratio. A ratio of 1.0 reduces nothing, and a note says so when Proportioning is on at 1.0 (HVE's own cases use 0.16 to 0.33). A ratio of **0** is valid: it caps the wheel pressure at P-Start.

### Antilock (ABS)
Check if the wheel has an anti-lock device. Checking it enables ABS Efficiency. EDSVS and EDVTS use it wheel by wheel. SIMON regulates **every** wheel once any wheel's box is checked, or once the vehicle's **ABS Installed** is (**Vehicle › Editors › Brakes › ABS / Brake Design... › ABS System...**); the dialog says so under the table. EDVDS has no ABS model.

### ABS Efficiency
The ability of the anti-lock system to achieve and hold the wheel at its peak frictional force, even if the driver braking input exceeds the available frictional force (0 to 1). A 100% effective anti-lock system maintains a longitudinal wheel force associated with the peak coefficient of friction. A 0% effective system maintains a longitudinal wheel force associated with the slide coefficient of friction. A 50% effective system would maintain a longitudinal force halfway between that associated with peak and slide friction.

The detailed per-wheel ABS data (HVE's **ABS Designer...** button) are in **Vehicle › Editors › Brakes › ABS / Brake Design... › ABS Designer...**.

!!! warning "Not in HVE Studio"
    - The rule that enables the antilock controls only when **ABS Installed** is checked: they are always enabled. ABS Installed is in **Vehicle › Editors › Brakes › ABS / Brake Design... › ABS System...** (see [Brake System Pressure vs Pedal Force](BrkSysVsPedFrcDlg.md)).

!!! tip "New in HVE Studio"
    All wheels in one table, Brake Groups, the Temperature Model row, and the note on a proportioning ratio of 1.0.

!!! note "Changed in HVE Studio 2026-10-09"
    The **S-Cam Brake** and **Disc Brake** tables are no longer opened from here: they were offered for every brake at once. Nothing read their values, and the section that kept them in the Brake Designer was removed on 2026-10-21. A wheel's brake is designed in the Brake Designer, whose design the engine uses.

<!-- NAV -->

---

← Previous: [Brakes & Powertrain](README.md)  |  [Index](README.md)  |  Next: [Brake Designer Material Properties Dialog Box](BrkMatPropDlg.md) →

<!-- /NAV -->
