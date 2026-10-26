# CG To Top

**CG To Top (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE Studio has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, where six fields below **Overall Height** give the distance from the CG to each face that the engines receive: **CG to Front**, **CG to Rear**, **CG to Right**, **CG to Left**, **CG to Top** and **CG to Bottom**. All values are in the units set in Preferences.

## z Coord
Vehicle-fixed distance from the CG to the top of the vehicle. In HVE Studio this is the **CG to Top** field under **Geometry**, and it is editable. It is **Overall Height** minus **CG Height**: typing it sets **Overall Height** (CG Height plus the value typed).

### Overall Height
An **input** under **Geometry**; **CG to Top** is it less CG Height, and typing **CG to Top** sets it.

## Stiffness...
There is no A/B/Kv stiffness for this face in HVE Studio. Its 3-D node stiffness (used by DyMESH) is the **Top** column's **3-D** rows in **Vehicle › Editors › Crush Stiffness...** (Vehicle editor, F3); its **2-D** rows show "--". See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE Studio"
    - A separate CG To Top dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

!!! tip "New in HVE Studio"
    When a 3-D geometry file is loaded and the mesh does not reach the declared front and rear extents, Size & Weight warns, directly under the **Wheel Positions** table (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced). The warning is shown only when it applies.

<!-- NAV -->

---

← Previous: [CG To Back](CGsToAll1.md)  |  [Index](README.md)  |  Next: [CG To Left](CGsToAll3.md) →

<!-- /NAV -->
