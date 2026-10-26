# CG To Back

**CG To Back (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE Studio has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, where six fields right after **CG Height** give the distance from the CG to each face that the engines receive: **CG to Front**, **CG to Rear**, **CG to Right**, **CG to Left**, **CG to Top** and **CG to Bottom**. All values are in the units set in Preferences.

## x Coord
Vehicle-fixed distance from the CG to the back of the vehicle. In HVE Studio this is the **CG to Rear** field under **Geometry**, and it is editable. It is **CG to Axle 2**, plus any spacing to the rearmost axle, plus **Rear Overhang** (measured from the rearmost axle): typing it sets **Rear Overhang** (never below zero) and keeps **Overall Length** in step. When the wheels carry their own X positions (the **Wheel Positions** table), CG to Rear is grayed, showing the wheels' value, along with the overhangs and the wheelbase.

### Rear Overhang
Distance from the rearmost axle to the back of the vehicle, stored as an **input** under **Geometry**; typing **CG to Rear** sets it.

### Overall Length
Shown under **Geometry**; the length the solver uses is **CG to Front** plus **CG to Rear**. Typing or dragging **Overall Length** moves each overhang by half the change. An overhang cannot go below zero: a shortfall one overhang cannot take goes to the other, so the shortest length is the axle span, with no overhang at either end, and the panel says so.

## Stiffness...
The rear face's A, B and Kv stiffness is edited in **Vehicle › Editors › Crush Stiffness...** (Vehicle editor, F3), the **Rear** column's **2-D** rows. Its 3-D node stiffness is the same column's **3-D** rows (DyMESH's Back zone). See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE Studio"
    - A separate CG To Back dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

!!! tip "New in HVE Studio"
    When a 3-D geometry file is loaded and the mesh does not reach the declared front and rear extents, Size & Weight warns, directly under the **Wheel Positions** table (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced). The warning is shown only when it applies.

<!-- NAV -->

---

← Previous: [CG To Front](CGsToAll.md)  |  [Index](README.md)  |  Next: [CG To Top](CGsToAll2.md) →

<!-- /NAV -->
