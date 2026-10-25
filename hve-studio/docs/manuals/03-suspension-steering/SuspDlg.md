# Suspension Data Dialog

The suspension parameters of the vehicle are displayed and edited using the **Suspension Data** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Suspension Data...**, or with **Suspension...** under **Components** in the Vehicles panel. The **Vehicle** list at the top selects the vehicle.

Where HVE edits one wheel at a time (the dialog title names the axle and side) and reaches the springs, inertia, stops and geometry through further dialogs, HVE Studio shows **every axle at once**: the dialog is a table with one column per axle (**Axle 1**, **Axle 2**, ...) and one row per parameter. The values are per axle; both wheels of an axle share them. Values are shown in the units set in Preferences and take effect as they are typed. While results are on screen the vehicle is locked; reset the run to edit it.

This dialog contains the following items:

## Suspension Group

Four small buttons per axle: **-**, **S1**, **S2** and **S3**. Axles in the same group (S1, S2 or S3) share their values: an edit in one column is copied to every other axle in the group, and moving an axle into a group that already has a member copies that member's values to it. **-** leaves the axle independent. By default axle 1 starts in group A, the rear axles with single tires in the next group, and the axles with **Dual Tires** in a group of their own, so a car is A, B and a truck with a single tag axle ahead of its duals is A, B, C. The groups are set again when you switch vehicles or change a wheel's **Dual Tires**; a group you choose stays until then. This replaces HVE's *Copy to Other Side* and *Copy to Other Axle(s)* check boxes.

## Type & Distribution

### Suspension Type
The HVE Vehicle Model includes the following suspension types:

- **Independent** — The right and left wheels move independently from each other.
- **Solid Axle** — The right and left wheels are rigidly connected.
- **4-Spring Tandem** — A set of two solid axle suspensions sharing an articulated spring support, such that the force on the rear of the leading spring is transferred to the front of the trailing spring.
- **Walking Beam Tandem** — A set of two solid axle suspensions connected by a rigid link.

All four types are offered for every axle.

### Roll Couple Dist
The fraction (0 to 1) of the total sprung mass roll couple (lateral load transfer) reacted at the axle. HVE's *Lateral Load Transfer Coef*.

### Int. Tandem Load Xfr
The inter-tandem load transfer for a tandem axle set. Used only with the tandem suspension types.

## Spring & Damper

HVE's Springs and Shocks dialog; see [Springs and Shocks Dialog](SprindShocksDlg.md).

### Spring Rate
Spring rate (force per unit of wheel travel) at the wheel due to the spring. HVE's *Wheel Rate*.

### Damp Rate
Velocity-dependent suspension force due to shock absorbers. HVE's *Damping at Wheel*.

### Static Deflection, Natural Freq (Hz)
Read-only rows: the spring's static deflection and the ride natural frequency, estimated from the vehicle's mass shared equally over its wheels. They are a check on the entered spring rate, not inputs.

### Aux Roll Stiffness
Roll stiffness (torque per unit of sprung mass roll) added by an anti-sway bar.

### Coulomb Friction
Friction force required to initiate suspension travel.

### Friction Null Band
Minimum suspension velocity required for full Coulomb friction force.

## Solid Axle

### Roll Ctr Below CG
Vertical distance from the sprung mass CG down to the suspension roll center (solid axles). 0 lets HVE Studio estimate it.

### Lat. Spring Space
Lateral distance between the left and right springs of a solid axle. 0 lets HVE Studio estimate it from the track width.

### Tandem Axle Spacing
For a tandem set, how far the tandem axle sits behind the axle ahead of it. It is the same value as the **Axle Spacing** rows (for example **A2 to A3**) in the Vehicles panel under **Size & Weight › Axle Spacing**; 0 uses a default spacing.

### Beam Mass, 0=default / Beam Inertia, 0=default
The axle beam's weight and inertia (HVE's Axle Inertia dialog); see [Inertia Dialog Box](../02-vehicles/InertiasDlg.md).

## Where HVE's other suspension buttons are

| HVE button | HVE Studio |
|---|---|
| Springs and Shocks... | The **Spring & Damper** and **Solid Axle** rows of this dialog. |
| Inertia... | **Beam Mass** and **Beam Inertia** rows of this dialog. |
| Jounce/Rebound... | the **Jounce / Rebound** tab of **Vehicle › Editors › Suspension Data...** — see [Jounce and Rebound Stops Dialog](JouAndRebDlg.md). |
| Spindle Axis... | **Vehicle › Editors › Steering System...** — see [Spindle Axis Dialog](SpndleAxisDlg.md). |
| Camber... | the **Camber vs Deflection** tab of **Vehicle › Editors › Suspension Data...** — see [Camber Dialog](CamberDlg.md). |
| Anti-Pitch... | the **Anti-Pitch** tab of **Vehicle › Editors › Suspension Data...** — see [Anti-Pitch Dialog](AntiPitchDlg.md). |
| Roll Steer... | the **Roll Steer** tab of **Vehicle › Editors › Suspension Data...** — see [Roll Steer Dialog](RollSteerDlg.md). |

!!! warning "Not in HVE Studio"
    - **HVE's enable rules**: HVE Studio does not gray Inter-Tandem Load Transfer for non-tandem types, the Roll Center Height and Lateral Spring Spacing for an independent suspension, the axle inertia for an independent suspension, Anti-Pitch for a solid axle, or Spindle Axis for a non-steerable axle. It offers the tandem types on every axle, where HVE offers them only where a tandem set is possible.
    - **Automatic balancing of the lateral load transfer coefficients** across axles: each axle's Roll Couple Dist is entered independently.
    - **Per-wheel (left/right) suspension data**: the values are per axle.
    - The **Copy to Other Side** and **Copy to Other Axle(s)** check boxes (use Suspension Group instead).

!!! tip "New in HVE Studio"
    All axles in one table, Suspension Groups, the Tandem Axle Spacing row, and the read-only static deflection and natural frequency check.

<!-- NAV -->

---

← Previous: [Steering System Dialog](SteerSysDlg.md)  |  [Index](README.md)  |  Next: [Wheel Location Dialog](WheelLocDlg.md) →

<!-- /NAV -->
