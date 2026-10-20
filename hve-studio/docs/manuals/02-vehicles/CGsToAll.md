# CG To Front

**CG To Front (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE Studio has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, and the distance from the CG to each face that the engines receive is shown, read-only, in the **Exterior Extents** table under the section's collapsed **Details** node. All values are in the units set in Preferences.

![Vehicles panel, Size & Weight](images/hvn-vehicles-panel.png)

## x Coord
Vehicle-fixed distance from the CG to the front of the vehicle. In HVE Studio this is the **X** row, *ahead* column, of **Exterior Extents**. It is derived as **CG to Axle 1** plus **Front Overhang**; edit those two values under **Geometry** to change it.

### Front Overhang
Distance from the front axle to the front of the vehicle. In HVE Studio it is an **input** (under **Geometry**), and the CG-to-front distance is derived from it.

### Overall Length
Shown under **Geometry** and, as derived by the solver, in the *Overall* column of **Exterior Extents**. If the entered Overall Length disagrees with the length the axle distances and overhangs describe, an orange note says so; the solver uses the derived figure. Typing or dragging **Overall Length** moves each overhang by half the change. An overhang cannot go below zero: a shortfall one overhang cannot take goes to the other, so the shortest length is the axle span, with no overhang at either end, and the panel says so.

## Stiffness...
The front face's A, B and Kv stiffness is edited in **Vehicle › Editors › Crush Stiffness...** (Vehicle editor, F3), section **Front**, or in the **CG to Front...** dialog of the **Crush & Geometry** window (**Event › Crush Profile...**, EDCRASH, EDSMAC and EDSMAC4 events). Its 3-D node stiffness is the **Front** zone under **3-D Node Stiffness** in Crush Stiffness. See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE Studio"
    - A separate CG To Front dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

!!! tip "New in HVE Studio"
    When a 3-D geometry file is loaded, Exterior Extents warns when the mesh does not reach the declared front and rear extents (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced).

<!-- NAV -->

---

← Previous: [B Stiffness Coefficient Dialog](BStiffDlg.md)  |  [Index](README.md)  |  Next: [CG To Back](CGsToAll1.md) →

<!-- /NAV -->
