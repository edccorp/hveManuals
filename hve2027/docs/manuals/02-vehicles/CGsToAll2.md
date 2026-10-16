# CG To Top

**CG To Top (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE 2027 has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, and the distance from the CG to each face that the engines receive is shown, read-only, in the **Exterior Extents** table under the section's collapsed **Details** node. All values are in the units set in Preferences.

## z Coord
Vehicle-fixed distance from the CG to the top of the vehicle. In HVE 2027 this is the **Z** row, *above* column, of **Exterior Extents**. It is derived as **Overall Height** minus **CG Height**; edit those two values under **Geometry** to change it.

### Overall Height
An **input** under **Geometry**; the CG-to-top distance is derived from it.

## Stiffness...
There is no A/B/Kv stiffness for this face in HVE 2027. Its 3-D node stiffness (used by DyMESH) is the **Top** zone under **3-D Node Stiffness** in **Vehicle › Crush Stiffness...** (Vehicle editor, F3). See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE 2027"
    - A separate CG To Top dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE 2027 has no such preference. HVE 2027 shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

!!! tip "New in HVE 2027"
    When a 3-D geometry file is loaded, Exterior Extents warns when the mesh does not reach the declared front and rear extents (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced).

<!-- NAV -->

---

← Previous: [CG To Back](CGsToAll1.md)  |  [Index](README.md)  |  Next: [CG To Left](CGsToAll3.md) →

<!-- /NAV -->
