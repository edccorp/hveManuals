# Accident History

The Accident History output report is a table of positions and velocities describing the motion of each object during the event. The report is displayed in a scrollable Common Reports window (see the Common Reports Dialog Box topic); it contains no editable controls.

The exact contents of the report depend on the physics program that produced the event:

## Path-based Programs (e.g. EDGEN)

The report is a table of positions and velocities for each user-entered path position. Rows are labeled *Initial:*, *Posn. n* and *Final:* (or *Rest:*), and include:

- **Time** — time at which the object reached the position
- **X, Y, Z** — earth-fixed coordinates of the position
- **Roll, Pitch, Yaw** — orientation angles at the position
- **V-tot** — total velocity
- **Sideslip** — sideslip angle
- **u-vel, v-vel, w-vel** — body-fixed linear velocity components
- **Roll vel, Pitch vel, Yaw vel** — angular velocity components

## Collision Simulation Programs (e.g. EDSMAC4, SIMON)

The report is a table of positions and velocities at key phases of the collision sequence. Rows are labeled *Start of Simulation*, *At Impact*, *At Separation* and *At Final/Rest*, and include time, position (X, Y, PSI), total velocity, body-fixed velocity components, yaw velocity and Delta-V.

For these programs, the times reported for the impact and separation phases are determined according to the **Accident History Basis** calculation option (*Force* or *Acceleration*), selected in the event's Calculation Options dialog.

---
*Source topic: AcciHistDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Reports & Output](README.md)  |  [Index](README.md)  |  Next: [Collision Pulse In-Use Factors Dialog Box](ColPulFact.md) →

<!-- /NAV -->
