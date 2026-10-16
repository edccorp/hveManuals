# Spindle Axis Dialog

HVE edits the spindle (steer) axis geometry of one wheel in the Spindle Axis dialog, opened from the Suspension Data dialog and available only for steerable axles. HVE 2027 has no separate dialog: the same properties are in the **Steering System** dialog (**Vehicle › Steering System...** in the Vehicle Editor, or **Steering...** under Vehicle Properties). See [Steering System Dialog](SteerSysDlg.md).

The alignment values are rows of the dialog's main table, one column per axle (both wheels of the axle share them); the steering stops and steer-axis friction are in the **Steer-Axis Mechanics (per wheel)** table below it, one column per wheel (**A1-R**, **A1-L**, ...). Every field of an axle is greyed unless the axle's **Steerable Axle** box is checked. Lengths and torques are shown in the units set in Preferences.

## Alignment (main table, per axle)

**Caster Angle (deg)**
The fore-aft angle of the spindle axis. This angle is largely responsible for the self-aligning properties of a steerable axle. Editing it sets both wheels of the axle; if a vehicle read from an HVE file has different left and right values, a note under the table gives both.

**Kingpin Inclination (deg)**
The sideways angle of the spindle axis. This angle, along with the caster angle, is responsible for the self-aligning properties of the steerable axle. Editing it sets both wheels; a note reports a left/right difference, as for caster.

**Kingpin Offset** (HVE: Steering Offset)
The distance from the center of the tire contact patch to the point where the steering axis intersects the ground at equilibrium conditions. This distance produces a steering torque (positive or negative, depending on the sign of the scrub radius) due to longitudinal tire force (either braking or driving).

**Camber Angle (deg)**
The static camber angle of the axle's wheels.

**Toe-In**
Not in HVE 2027's Steering System dialog. HVE's per-wheel toe-in, a length, is kept with the vehicle (read from an HVE case or a vehicle database) but has no control in HVE 2027: no engine reads it, in HVE or here.

## Steer-Axis Mechanics (per wheel)

**Stub Axle Length**
The length of the stub axle (spindle) from the steering axis to the wheel plane.

**Kingpin Friction** (HVE: Steer Axis Friction Torque)
Constant (Coulomb) friction torque about the steer axis, opposing the steer rate. Rotation of the wheel about the steering axis is resisted by this torque, which must be overcome before the wheel steers. 0 is a free axis with nothing damping it.

**Stop Angle Right (deg)**, **Stop Angle Left (deg)**
How far the wheel can turn right, and left, of straight ahead. Both are entered as positive numbers; HVE 2027 applies the sign for the left stop.

**Stop Stiffness**
The mechanical stiffness of the steering stops (N·m/deg in SI, ft·lb/deg in US units). Additional steering beyond the stop angle is resisted by a torque that attempts to return the wheel towards zero steer. 0 means no stops at all.

**Stop Damping**
Greyed: SIMON does not use a steering stop damping term.

These steer-axis values matter only when the wheel's steer angle is free: SIMON's steer degree of freedom, set per axle by **Steer DOF (SIMON)** in the Steering System dialog or for the whole event in the event's SIMON options. A prescribed steer angle cannot be resisted. When no axle has its own Steer DOF set, a note in the dialog says so.

!!! warning "Not in HVE 2027"
    - **Stop Energy Ratio**. HVE 2027 carries no restitution for the steering stops.
    - The **Steering: Right (+) / Left (−)** radio buttons (both stops are shown at once).
    - Separate left and right caster and kingpin inclination entry: each is entered once per axle (left/right values read from an HVE file are kept and reported).

<!-- NAV -->

---

← Previous: [Roll Steer Properties](RollSteerNewDlg.md)  |  [Index](README.md)  |  Next: [Springs and Shocks Dialog](SprindShocksDlg.md) →

<!-- /NAV -->
