# Steering System Dialog

The steering system parameters for the current vehicle are displayed and edited using the **Steering System** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Steering System...**, or with **Steering...** under **Vehicle Properties** (in the Vehicles panel or the Vehicle Information dialog). The **Vehicle** list at the top selects the vehicle.

Where HVE shows one axle at a time (chosen with *Steering Data For*), HVE 2027 shows a table with one column per axle (**Axle 1**, **Axle 2**, ...). Below it, the **Steer-Axis Mechanics (per wheel)** table holds HVE's Spindle Axis data; see [Spindle Axis Dialog](SpndleAxisDlg.md). Values are shown in the units set in Preferences and take effect as they are typed.

The Steering System parameters are:

## Steerable Axle
Check box to allow or disallow steering at the axle. When unchecked, all of the axle's other fields (in both tables) are disabled.

## Gear & Preset

### Gear Ratio
Ratio of the steering wheel angle to the road wheel steer angle, −30 to 30. A positive ratio steers with the steering wheel; a **negative** ratio counter-steers (a steerable tag axle). A larger magnitude gives a smaller road-wheel angle. A steerable axle with a ratio of 0 is given 16:1; a non-steerable axle has no steering gear and is passed a ratio of 0, as HVE does.

### Steer Data Preset
**Ackermann**, **Parallel Steer** or **Custom**. Axle 1's setting decides whether SIMON uses Ackermann steering for the vehicle: with **Ackermann**, the inner and outer front wheels get slightly different angles from the steering geometry; otherwise both get the same angle. HVE sets *Use Ackermann Steering* in the event's Driver Controls instead.

### Steer DOF (SIMON)
Whether SIMON solves this axle's steer angle as a free degree of freedom: **Event default** (use the event's own SIMON steer setting), **Normal (free)**, **Append (free after table)** (follow the steer table, then free) or **Auto start (free at contact)** (free from the first contact).

### Has steering column
Uncheck for a castoring axle with no steering linkage. The free steer axis then has the wheels' own inertia only, instead of adding the column's inertia scaled by the square of the gear ratio.

## Geometry

### Caster Angle (deg), Kingpin Inclination (deg), Camber Angle (deg), Toe Angle (deg), Kingpin Offset
The axle's alignment; see [Spindle Axis Dialog](SpndleAxisDlg.md).

### Column Friction
Friction torque measured at the steering wheel.

### Column Inertia
Rotational inertia of the steering wheel and column.

### Friction Lag (rad/s)
Rotational velocity required to develop the full steering friction torque. HVE enters it in deg/sec.

### Front Track, Rear Track
Track widths stored with the steering data. They are not passed to the engines; the track widths the engines use are the **Track Width** values in the Vehicles panel (**Dimensions / Inertias › Overall**) and the wheel positions.

Column Friction, Column Inertia and Friction Lag are used only when an axle's steer angle is free (see Steer DOF); a note under the table says so when no axle sets its own Steer DOF.

!!! warning "Not in HVE 2027"
    - **Steering Column Stiffness**, **Steering Linkage Mass**, **Steering Linkage Stiffness** and **Steering Linkage Damping**. They are not read from an HVE vehicle or case, and cannot be edited; the engines receive fixed column and linkage stiffnesses.
    - **Steering Data For** (all axles are shown at once).

!!! tip "New in HVE 2027"
    Per-axle **Steer DOF (SIMON)**, **Has steering column**, the **Steer Data Preset**, negative (counter-steering) gear ratios, and the per-wheel steer-axis mechanics in the same dialog.

<!-- NAV -->

---

← Previous: [Springs and Shocks Dialog](SprindShocksDlg.md)  |  [Index](README.md)  |  Next: [Suspension Data Dialog](SuspDlg.md) →

<!-- /NAV -->
