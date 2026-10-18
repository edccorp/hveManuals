# Jounce and Rebound Stops Dialog

The jounce and rebound stop properties are displayed and edited in the **Jounce / Rebound** dialog. Open it in the Vehicle Editor as the **Jounce / Rebound** tab of **Vehicle › Editors › Suspension Data...**. The Suspension Data window's tabs are Springs & Dampers, Jounce / Rebound, Camber vs Deflection, Roll Steer and Anti-Pitch.

The **Vehicle** list at the top selects the vehicle.

Where HVE edits one wheel at a time and switches between the jounce and the rebound stop with two radio buttons, HVE 2027 shows a table with one column per wheel (**A1 Right**, **A1 Left**, **A2 Right**, ...) and both stops at once, jounce rows above rebound rows. Values are shown in the units set in Preferences and take effect as they are typed.

## Link Group

Four small buttons per wheel: **-**, **A**, **B** and **C**. Wheels in the same group share their values: an edit in one column is copied to the others in the group, and moving a wheel into a group that already has a member copies that member's values to it. By default both wheels of axle 1 are in group A and all other wheels in group B. This replaces HVE's *Copy To Other Side*.

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

!!! note "HVE 2027"
    **Enter both travels as positive distances.** HVE shows the jounce deflection as a negative number; HVE 2027 uses the size of the number for each stop and applies the sign itself, so a negative jounce travel read from an HVE file works the same. A travel of **0 disables that stop** (it is placed out of reach) rather than putting the stop at the ride position.

!!! warning "Not in HVE 2027"
    The Jounce/Rebound radio buttons (both stops are always shown) and HVE's 0-to-1 range on the energy ratio (the slider allows up to 2).

<!-- NAV -->

---

← Previous: [Camber vs Jounce/Rebound Dialog](CamberDlg.md)  |  [Index](README.md)  |  Next: [Roll Steer Dialog](RollSteerDlg.md) →

<!-- /NAV -->
