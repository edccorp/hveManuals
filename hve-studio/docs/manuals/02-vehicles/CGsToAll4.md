# CG To Right

**CG To Right (Exterior Dimensions)**

HVE edits the vehicle's exterior dimensions in six Vehicle Dimensions dialogs, one per face (CG to Front, Back, Top, Left, Right and Bottom), each with a Stiffness button. HVE Studio has no per-face dialogs. The exterior dimensions are entered in the Vehicle Editor (**Vehicle (F3)**), in the **Vehicles** panel under **Size & Weight › Geometry**, where six fields right after **CG Height** give the distance from the CG to each face that the engines receive: **CG to Front**, **CG to Rear**, **CG to Right**, **CG to Left**, **CG to Top** and **CG to Bottom**. All values are in the units set in Preferences.

## y Coord
Vehicle-fixed distance from the CG to the right side of the vehicle. In HVE Studio this is the **CG to Right** field under **Geometry**, and it is editable: it is the vehicle's stored CG-to-right distance, which a vehicle read from an HVE database or case carries from HVE's own data. A vehicle that carries none shows half of **Overall Width** (entered under **Geometry**) until a value is typed. The engines take the body as symmetric about the CG: each side receives the mean of **CG to Left** and **CG to Right** (or the one that is set).

### Overall Width
An **input** under **Geometry**. The CG-to-left and CG-to-right distances are each half of it only when the vehicle carries no CG-to-side distances of its own; a vehicle read from an HVE database or case normally carries them, and editing Overall Width does not change its side extents.

## Stiffness...
The right face's A, B and Kv stiffness is edited in **Vehicle › Editors › Crush Stiffness...** (Vehicle editor, F3), the **Right** column's **2-D** rows. Its 3-D node stiffness is the same column's **3-D** rows (DyMESH's Right zone). See [Stiffness Coefficient Dialog](StiffCoeffDlg.md).

!!! warning "Not in HVE Studio"
    - A separate CG To Right dialog, and its Apply / OK / Cancel buttons. Edits in the Vehicles panel take effect as they are typed.
    - HVE displays the distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.
    - Unequal left and right extents in the engines. **CG to Left** and **CG to Right** are stored separately, but each side receives their mean.

!!! tip "New in HVE Studio"
    When a 3-D geometry file is loaded and the mesh does not reach the declared front and rear extents, Size & Weight warns, directly under the **Wheel Positions** table (EDSMAC4 refuses such a run, and DyMESH crush would be misplaced). The warning is shown only when it applies.

<!-- NAV -->

---

← Previous: [CG To Left](CGsToAll3.md)  |  [Index](README.md)  |  Next: [CG To Bottom](CGsToAll5.md) →

<!-- /NAV -->
