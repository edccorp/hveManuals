# Anti-Pitch Dialog

The anti-pitch properties of the wheels are displayed and edited in the **Anti-Pitch** dialog. Open it in the Vehicle Editor as the **Anti-Pitch** tab of **Vehicle › Editors › Suspension Data...**. Anti-pitch data are entered as a table of anti-pitch coefficient vs. suspension deflection. The **Vehicle** list at the top selects the vehicle.

HVE Studio shows one table with a column per wheel (**A1 Right**, **A1 Left**, **A2 Right**, ...), where HVE edits one wheel at a time.

!!! note "HVE Studio"
    An orange note at the top of the dialog says which engines use the table: **EDVSM** reads it, in each wheel's suspension force; SIMON only prints it on a report page; no other engine reads it. This is HVE's own behavior.

## Link Group

Four small buttons per wheel: **-**, **A**, **B** and **C**. Wheels in the same group share their values, as in the [Jounce and Rebound Stops Dialog](JouAndRebDlg.md).

## Data Table

**Num Points**
The number of rows in the wheel's table, 3 to 15.

**Pt *n* Deflect**
Suspension deflection of row *n* (jounce negative, rebound positive), in the units set in Preferences.

**Pt *n* Anti-Pitch**
The anti-pitch coefficient at that deflection: the suspension force per unit tire-force moment, in lb/ft-lb (imperial) or N/N·m (metric), as set in Preferences. HVE labels it *Anti-Pitch (lb/ft-lb)*.

!!! warning "Not in HVE Studio"
    - The **Anti-Pitch vs. Jounce/Rebound** graph, **Apply** and **Print**, and HVE's sorting and validation of the rows.
    - HVE's rule that makes the dialog available only for an Independent suspension: it is always available.

<!-- NAV -->

---

← Previous: [Suspension & Steering](README.md)  |  [Index](README.md)  |  Next: [Camber vs Jounce/Rebound Dialog](CamberDlg.md) →

<!-- /NAV -->
