# CG To Left

**CG To Left (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE Studio has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, and the distance from the CG to each face that the engines receive is shown, read-only, in the **Exterior Extents** table under the section's collapsed **Details** node. All values are in the units set in Preferences.

## y Coord
Vehicle-fixed distance from the CG to the left side of the vehicle. In HVE Studio this is the **Y** row, *left* column, of **Exterior Extents**. The body is taken as symmetric about the CG. For a vehicle read from an HVE database or case it is the mean of HVE's own CG-to-left and CG-to-right distances; for a vehicle that carries none, it is half of **Overall Width**, which is entered under **Geometry**.

### Overall Width
An **input** under **Geometry**. The CG-to-left and CG-to-right distances are each half of it only when the vehicle carries no CG-to-side distances of its own; a vehicle read from an HVE database or case normally carries them, and editing Overall Width does not change its side extents.

## Stiffness...
The left face's A, B and Kv stiffness is edited in **Vehicle › Editors › Crush Stiffness...** (Vehicle editor, F3), section **Left**. Its 3-D node stiffness is the **Left** zone under **3-D Node Stiffness** in Crush Stiffness. See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE Studio"
    - A separate CG To Left dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.
    - Separate CG-to-left and CG-to-right distances cannot be entered: the left and right extents are always equal.

!!! tip "New in HVE Studio"
    When a 3-D geometry file is loaded, Exterior Extents warns when the mesh does not reach the declared front and rear extents (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced).

<!-- NAV -->

---

← Previous: [CG To Top](CGsToAll2.md)  |  [Index](README.md)  |  Next: [CG To Right](CGsToAll4.md) →

<!-- /NAV -->
