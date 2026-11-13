# Camber vs Jounce/Rebound Dialog

The camber properties of the wheels are displayed and edited in the **Camber vs Deflection** dialog. Open it in the Vehicle Editor as the **Camber vs Deflection** tab of **Vehicle › Editors › Suspension Data...**. The **Vehicle** list at the top selects the vehicle.

Where HVE opens either this table/graph dialog (independent suspension) or a single constant *Camber (deg)* dialog (solid and tandem axles), HVE Studio shows both: a grid with a column per wheel (**A1 Left**, **A1 Right**, **A2 Left**, ...) for the values each wheel has one of, and under it one wheel's camber table with its graphs, as HVE's dialog has them. Deflections and half-track changes are shown in the units set in Preferences; angles are in degrees.

## Suspension Group

A button per group above each wheel (**S1**, **S2**, ...; a drop-down where the column is too narrow for the buttons). Every wheel is in a group; wheels in the same group share their values, the camber table and half-track change included, as in the [Jounce and Rebound Stops Dialog](JouAndRebDlg.md).

**Layout...** sets the groups in one step and copies a wheel's values once, as in the [Jounce and Rebound Stops Dialog](JouAndRebDlg.md).

## Solid-Axle Const (deg)

The constant camber angle of a solid or tandem axle (HVE's small Camber dialog). Enabled only for wheels on an axle whose suspension type is not Independent. Pointing at the row's name says which value a run reads: a solid axle takes this constant and ignores its table, an independent axle reads its table and ignores this.

## Camber Table

Each wheel's table size (*3 points*, ...; *(not read)* on a solid axle). Click a wheel's cell to edit its table below.

## Camber vs deflection: the wheel's table

The wheel shown is picked with the **Wheel** buttons, or by clicking its cell in the **Camber Table** row. A line under them names the wheels of its suspension group, which every edit here also changes. The table has a row per point:

**Deflection**
Suspension deflection of the point (jounce negative, rebound positive). The rows are kept in order of deflection: a changed deflection moves its row when you finish typing.

**Camber (deg)**
Wheel camber angle at that deflection.

**Half-Track Change**
How far the wheel center moves sideways at that deflection. SIMON reads it for the wheel's lateral position and the suspension's jacking force. (It used to be read from an HVE file and passed to the engine with no way to see or change it.)

**x** removes a point (a table keeps at least 3); **Add Point** adds one a step past the last deflection, up to 15. Under the table, two graphs draw **camber** and **half-track change** against deflection, and follow every edit.

!!! warning "Not in HVE Studio"
    - **Apply** and **Print**.
    - HVE's other checks on Apply/OK (removing empty rows, rejecting duplicate deflections).

<!-- NAV -->

---

← Previous: [Anti-Pitch Dialog](AntiPitchDlg.md)  |  [Index](README.md)  |  Next: [Jounce and Rebound Stops Dialog](JouAndRebDlg.md) →

<!-- /NAV -->
