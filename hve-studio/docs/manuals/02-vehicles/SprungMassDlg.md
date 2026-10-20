# Sprung Mass Dialog

**Sprung Mass Parameter Groups**

In HVE, clicking the CG of the vehicle in the Vehicle Editor displays the Sprung Mass dialog, a column of buttons that open the sprung-mass parameter groups. HVE Studio has no Sprung Mass dialog and does not open dialogs by clicking the CG. The same parameter groups are reached from the **Vehicle** menu of the Vehicle Editor (**Vehicle (F3)**), from the **Components** buttons in the Vehicles panel, and from the panel's own sections:

| HVE button | Where it is in HVE Studio |
|---|---|
| Inertias... | **Edit...** in the Vehicles panel's **Inertia** section opens the **Inertia / Mass** dialog — see [Vehicle Inertia Dialog](VehInerDlg.md). The section itself shows the total weight and inertias on one line. |
| Move CG... | **Vehicle › Editors › Vehicle Mesh...** (or **Vehicle Mesh...** in the Vehicles panel's **3D Geometry** section), File & Placement tab, row **Move CG** — see [Moving CG](MoveCGDlg.md). |
| Color... | **Color** in the Identity section of the Vehicles panel. |
| Geometry File... | **Mesh File** in the Vehicles panel's **3D Geometry** section, or on the File & Placement tab of **Vehicle › Editors › Vehicle Mesh...**. |
| Refresh Geometry File | **Load 3D File** on the Vehicle Mesh window's File & Placement tab reloads the file from disk. |
| Transform Geometry... | **Vehicle › Editors › Vehicle Mesh...**, File & Placement tab, section **Move, Rotate and Scale the Model** (Translate, Rotate and per-axis Scale). |
| Contact Surfaces... | **Vehicle › Editors › Contact Surfaces...** |
| Belt Restraints... | **Vehicle › Editors › Belt Restraint...** |
| Airbag Restraints... | **Vehicle › Editors › Airbags...** |
| Connections... | **Connections...** in the Vehicles panel's Components section. |
| Aerodynamic Drag... | **Vehicle › Editors › Aerodynamic Drag...** (or **Aerodynamic Drag...** in the Vehicles panel's Components section) — see [Vehicle Drag Dialog](VehDragDlg.md). |
| Body Torsion... | **Vehicle › Editors › Body Torsion...** — see [Body Torsion Dialog](BodyTorDlg.md). |
| Handling... | **Event › Handling Parameters...**, available in the Event Editor when the event's method is EDSMAC or EDSMAC4. |
| Report Color... | Not in HVE Studio. |
| Lights... | **Vehicle › Editors › Vehicle Lights...** |

!!! note "HVE Studio"
    The **Handling Properties** values (total understeer, roll gradient, roll couple distribution and front weight distribution) are **editable** in HVE Studio, where HVE shows them as a read-only summary. No engine reads the values entered there.

!!! warning "Not in HVE Studio"
    **Report Color**: HVE Studio has no separate per-vehicle color for reports.

<!-- NAV -->

---

← Previous: [Payload Dialog Box](PayLoadDlg.md)  |  [Index](README.md)  |  Next: [Stiffness Coefficient Dialog](StiffCoeffDlg.md) →

<!-- /NAV -->
