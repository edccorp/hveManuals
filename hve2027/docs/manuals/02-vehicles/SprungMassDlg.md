# Sprung Mass Dialog

**Sprung Mass Parameter Groups**

In HVE, clicking the CG of the vehicle in the Vehicle Editor displays the Sprung Mass dialog, a column of buttons that open the sprung-mass parameter groups. HVE 2027 has no Sprung Mass dialog and does not open dialogs by clicking the CG. The same parameter groups are reached from the **Vehicle** menu of the Vehicle Editor (**Vehicle (F3)**), from the **Vehicle Properties** buttons in the Vehicles panel and the [Vehicle Information dialog](VehicleInfoDlg.md), and from the panel's own sections:

| HVE button | Where it is in HVE 2027 |
|---|---|
| Inertias... | **Inertia / Mass...** under Vehicle Properties — see [Vehicle Inertia Dialog](VehInerDlg.md). Weight and inertias are also in the Vehicles panel under **Dimensions / Inertias**. |
| Move CG... | **Vehicle › Vehicle Mesh...** (or the Vehicles panel's **3D Geometry** section), row **Move CG** — see [Moving CG](MoveCGDlg.md). |
| Color... | **Vehicle Color** in Vehicle Information, or **Color** in the Information section of the Vehicles panel. |
| Geometry File... | **3D File** in Vehicle Information, or **Mesh File** in the Vehicle Mesh editor (the **3D Geometry** section of the Vehicles panel, or **Vehicle › Vehicle Mesh...**). |
| Refresh Geometry File | **Load 3D File** in the same places reloads the file from disk. |
| Transform Geometry... | **Vehicle › Vehicle Mesh...**, section **Move, Rotate and Scale the Model** (Translate, Rotate and per-axis Scale). |
| Contact Surfaces... | **Vehicle › Contact Surfaces...** |
| Belt Restraints... | **Vehicle › Belt Restraint...** |
| Airbag Restraints... | **Vehicle › Airbags...** |
| Connections... | **Connections...** under Vehicle Properties. |
| Aerodynamic Drag... | **Vehicle › Aero Dynamic Drag...** (or **Aerodynamic Drag...** under Vehicle Properties) — see [Vehicle Drag Dialog](VehDragDlg.md). |
| Body Torsion... | **Vehicle › Body Torsion...** — see [Body Torsion Dialog](BodyTorDlg.md). |
| Handling... | **Event › Handling Parameters...**, available in the Event Editor when the event's method is EDSMAC or EDSMAC4. |
| Report Color... | Not in HVE 2027. |
| Lights... | **Vehicle › Vehicle Lights...** |

!!! note "HVE 2027"
    The **Handling Properties** values (total understeer, roll gradient, roll couple distribution and front weight distribution) are **editable** in HVE 2027, where HVE shows them as a read-only summary. No engine reads the values entered there.

!!! warning "Not in HVE 2027"
    **Report Color**: HVE 2027 has no separate per-vehicle color for reports.

<!-- NAV -->

---

← Previous: [Payload Dialog Box](PayLoadDlg.md)  |  [Index](README.md)  |  Next: [Stiffness Coefficient Dialog](StiffCoeffDlg.md) →

<!-- /NAV -->
