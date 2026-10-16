# CG To Back

**CG To Back (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE 2027 has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Dimensions / Inertias › Overall**, and the distance from the CG to each face that the engines receive is shown, read-only, in the **Exterior Extents** table just below it. All values are in the units set in Preferences.

## x Coord
Vehicle-fixed distance from the CG to the back of the vehicle. In HVE 2027 this is the **X** row, *behind* column, of **Exterior Extents**. It is derived as **CG to Axle 2**, plus any spacing to the rearmost axle, plus **Rear Overhang (from the rearmost axle)**; edit those values under **Overall** to change it.

### Rear Overhang
Distance from the rearmost axle to the back of the vehicle, an **input** under **Overall**.

### Overall Length
Shown under **Overall** and, as derived by the solver, in the *Overall* column of **Exterior Extents**. Typing or dragging **Overall Length** moves each overhang by half the change. An overhang cannot go below zero: a shortfall one overhang cannot take goes to the other, so the shortest length is the axle span, with no overhang at either end, and the panel says so.

## Stiffness...
The rear face's A, B and Kv stiffness is edited in **Vehicle › Crush Stiffness...** (Vehicle editor, F3), section **Rear**, or in the **CG to Rear...** dialog of the **Crush & Geometry** window (**Event › Crush Profile...**, EDCRASH, EDSMAC and EDSMAC4 events). Its 3-D node stiffness is the **Rear** zone under **3-D Node Stiffness** in Crush Stiffness. See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE 2027"
    - A separate CG To Back dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE 2027 has no such preference. HVE 2027 shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

!!! tip "New in HVE 2027"
    When a 3-D geometry file is loaded, the Exterior Extents section also lists the loaded mesh's own extents for comparison, and warns when the mesh does not reach the declared front and rear extents (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced).

<!-- NAV -->

---

← Previous: [CG To Front](CGsToAll.md)  |  [Index](README.md)  |  Next: [CG To Top](CGsToAll2.md) →

<!-- /NAV -->
