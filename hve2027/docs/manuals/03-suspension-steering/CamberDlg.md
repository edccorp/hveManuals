# Camber vs Jounce/Rebound Dialog

The camber properties of the wheels are displayed and edited in the **Camber vs Deflection** dialog. Open it in the Vehicle Editor with **Vehicle › Advanced Suspension...** and then **Camber vs Deflection...**. The **Vehicle** list at the top selects the vehicle.

Where HVE edits one wheel at a time, and opens either this table/graph dialog (independent suspension) or a single constant *Camber (deg)* dialog (solid and tandem axles), HVE 2027 shows one table with a column per wheel (**A1 Right**, **A1 Left**, **A2 Right**, ...) holding both. Deflections are shown in the units set in Preferences; angles are in degrees.

## Link Group

Four small buttons per wheel: **-**, **A**, **B** and **C**. Wheels in the same group share their values, as in the [Jounce and Rebound Stops Dialog](JouAndRebDlg.md).

## Solid-Axle Const (deg)

The constant camber angle of a solid or tandem axle (HVE's small Camber dialog). Enabled only for wheels on an axle whose suspension type is not Independent; for an independent axle the field is greyed, and its tooltip says that the axle's camber comes from the table.

## Data Table

**Num Points**
The number of rows in the wheel's camber table, 3 to 15.

**Pt *n* Deflect**
Suspension deflection of row *n* (jounce negative, rebound positive).

**Pt *n* Angle (deg)**
Wheel camber angle at that deflection.

A wheel with fewer points than the longest table shows *--* in the rows it does not use. Type into a cell, or Ctrl+click it, to enter a value.

An orange note under the table states which entry the solver reads: a solid axle reads the constant row and an independent axle reads the table. When every axle is solid the note says that the table is ignored.

!!! warning "Not in HVE 2027"
    - The **Camber vs. Jounce/Rebound** and **Half-track Change vs. Jounce/Rebound** graphs, and **Apply** and **Print**.
    - The **Half-track Change** column. A half-track table read from an HVE file is kept with the vehicle and passed to the engine, but it cannot be viewed or edited.
    - HVE's validation on Apply/OK (sorting the rows by deflection, removing empty rows, rejecting incomplete rows and duplicate deflections): enter the rows in order of deflection.

<!-- NAV -->

---

← Previous: [Anti-Pitch Dialog](AntiPitchDlg.md)  |  [Index](README.md)  |  Next: [Jounce and Rebound Stops Dialog](JouAndRebDlg.md) →

<!-- /NAV -->
