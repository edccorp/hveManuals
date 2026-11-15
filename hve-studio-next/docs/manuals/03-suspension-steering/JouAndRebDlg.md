# Jounce and Rebound Stops Dialog

The jounce and rebound stop properties are displayed and edited in the **Jounce / Rebound** dialog. Open it in the Vehicle Editor as the **Jounce / Rebound** tab of **Vehicle › Editors › Suspension Data...**. The Suspension Data window's tabs are Springs & Dampers, Jounce / Rebound, Camber vs Deflection, Roll Steer and Anti-Pitch.

The **Vehicle** list at the top selects the vehicle.

Where HVE edits one wheel at a time and switches between the jounce and the rebound stop with two radio buttons, HVE Studio shows a table with one column per wheel (**A1 Left**, **A1 Right**, **A2 Left**, ...) and both stops at once, jounce rows above rebound rows. Values are shown in the units set in Preferences and take effect as they are typed.

## Suspension Group

A button per group above each wheel, numbered **S1**, **S2**, ... up to the number of wheels (a drop-down when there are more than four). Every wheel is in a group; a wheel alone in its group edits alone. Wheels in the same group share their values: an edit in one column is copied to the others in the group, and moving a wheel into a group that already has a member copies that member's values to it. By default both wheels of an axle are in the same group: axle 1 starts in group S1, the rear axles with single tires in the next group, and the axles with **Dual Tires** in a group of their own, so a car is S1, S2 and a truck with a single tag axle ahead of its duals is S1, S2, S3. The groups are set again when a wheel's **Dual Tires** or the number of axles changes; a group you choose stays until then. The groups are saved with the case, and **Undo** reverses a group change. This replaces HVE's *Copy To Other Side*.


**Layout...**, beside the group row's name, sets the usual arrangements in one step: **Same both sides** (each axle's left and right wheels in a group of their own), **Same on every wheel** (one group), and **Each wheel its own** (every wheel in a group of its own, so an edit changes only that wheel). The arrangement the wheels are in now is checked; none is when the groups are a mix of them. A new group takes the values of its first wheel, A1 Left first. Under **Copy once** it does what HVE's *Copy to Other Side* and *Copy to Other Axles* do: pick a wheel under **From**, then **To the other side**, **To the other axles** (the same side of every other axle) or **To every wheel**. The copy changes no group, and a wheel copied to takes its group mates with it. Pointing at a column outlines it and tints the wheels in its group, the ones an edit there will change; they stay marked while the field is being edited.

## Jounce (Compression)

**Linear Rate**
Linear constant (force per unit of wheel travel) of the jounce stop.

**Cubic Rate**
Cubic constant (force per unit of wheel travel cubed) of the jounce stop.

**Max Deflection**
Suspension travel distance from equilibrium to the jounce stop.

**Energy Ratio (Jounce)**
Ratio of conserved to total energy (restitution) of the jounce stop. The slider runs from 0 to 2.

## Rebound (Extension)

**Linear Rate**, **Cubic Rate**, **Max Deflection**, **Energy Ratio (Rebound)**
The same four properties for the rebound (extension travel limit) stop.

!!! note "HVE Studio"
    **Enter both travels as positive distances.** HVE shows the jounce deflection as a negative number; HVE Studio uses the size of the number for each stop and applies the sign itself, so a negative jounce travel read from an HVE file works the same. A travel of **0 disables that stop** (it is placed out of reach) rather than putting the stop at the ride position.

!!! warning "Not in HVE Studio"
    The Jounce/Rebound radio buttons (both stops are always shown) and HVE's 0-to-1 range on the energy ratio (the slider allows up to 2).

<!-- NAV -->

---

← Previous: [Camber vs Jounce/Rebound Dialog](CamberDlg.md)  |  [Index](README.md)  |  Next: [Roll Steer Dialog](RollSteerDlg.md) →

<!-- /NAV -->
