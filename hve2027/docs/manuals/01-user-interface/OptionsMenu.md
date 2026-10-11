# Options Menu

HVE 2027 has **no Options menu**. HVE's Options menu mixes display switches, tools and settings dialogs; in HVE 2027 they are spread over the **View** and **Tools** menus, the Event Editor's **Event** and **Output** menus, and the docked panels. The table lists every item of HVE's Options menu, in HVE's order, and where its function is in HVE 2027.

| HVE Options item | HVE 2027 |
|---|---|
| Create DB | Not in HVE 2027. Vehicle databases are read as they are; **Save Vehicle As** writes a vehicle into a database file (see [Saving Vehicles](../02-vehicles/VehSaveAs.md)). |
| Show Key Results | **View › Key Results** (or **Output › Key Results...** in the Event Editor) — see [Key Results Dialog Box](KeyResDlg.md). |
| Show Axes | Not available as a switch. |
| Show Contacts | **View › Scene Display › Occupant Equipment** draws the active vehicle's contact surfaces, airbags and belts; **View › Scene Display › Occupant Equipment Through Bodywork** draws them over the body. |
| Show Belt Anchors | **View › Scene Display › Occupant Equipment** (as above). |
| Show Velocity Vectors | **View › Scene Display › Vectors › Velocity Vectors**. The same submenu has **Collision Force (PDOF)**, **Tire Force Vectors** (optionally **...include vertical Fz'**) and **Draw Vectors Through Bodywork**. HVE's *Long Velocity Vectors* preference has no equivalent. |
| Show Skidmarks | **View › Scene Display › Skidmarks**: the contact-patch path drawn only where the tire was marking, faded by how hard. Skidmarks are drawn at the width of the tire that laid them. |
| Show Tracks | **View › Scene Display › Tire Contact Patch Paths**: where each tire touched the ground, one path per wheel. |
| Show CGs | Not available as a switch. |
| Show CG Paths | **View › Scene Display › CG Path**. **Path thickness (m)** in the same panel sets how thick CG and accelerometer paths are drawn (0 draws a hairline). |
| Show Accelerometers / Show Accelerometer Paths | **View › Scene Display › Accelerometer Path**: one path per installed accelerometer. |
| Show Position Sequences | Not in HVE 2027. |
| Show Targets | **View › Scene Display › Scene Ghosts**: **None**, **Outline**, **Translucent vehicle** or **Both**. Scene positions (HVE's targets) are drawn as an outline, a translucent copy of the vehicle, or both. |
| Show Connections | Not available as a switch. |
| Distance Tool | Not in HVE 2027. |
| Show Path | Not in HVE 2027. |
| Autoposition | Per event and per vehicle: **Auto Position (settle onto terrain)** under the vehicle in the **Vehicle Initial Conditions** section of the **Event Information** panel. It is always on for the planar methods. |
| Grid | A datum grid is drawn when no site is loaded; it has no settings. See [Set Grid Dialog Box](SetGridDlg.md). |
| Units | **Tools › Preferences... › Units** — see [Units Dialog Box](UnitsDlg.md). |
| Shadows | **View › Scene Display › Shadow Coverage**: **Vehicles (sharp)** fits the shadows to the vehicles, **Whole scene** to the site as well. HVE's shadow radius, quality, precision and intensity are not offered. |
| Render (Ctrl+R) | **View › Scene Display › Rendering** — see [Render Dialog Box](RendOptDlg.md). (In HVE 2027 **Ctrl+R** is **Output › Run Simulation...**, in the Event Editor.) |
| Playback | **Output › Playback Options...** (Event Editor) |
| Simulation Controls (Ctrl+Y) | The **Simulation** panel (**View › Simulation**), *Simulation Controls* section: duration, time steps, termination velocities and the integrator convergence controls the event's method uses. |
| Calculation Options (Ctrl+J) | **Method Options...** in the **Calculation Method** section of the **Event Information** panel opens the options window for the event's method (EDCRASH, EDSMAC/EDSMAC4, EDGEN, EDHIS, SIMON, EDVSM, GATB, ...). See the Calculation Options chapter. |
| DyMESH | **Event › DyMESH Options...** |
| Get Surface Info | The **Road Surface Search** section of the **Event Information** panel. |
| Preferences (Ctrl+F) | **Tools › Preferences...** — see [User Preferences Dialog Box](PrefDlg.md). |

!!! tip "New in HVE 2027"
    The Scene Display panel (**View › Scene Display**) also has **Axes** (the case's X, Y and Z at the origin, and, while it is on, each vehicle's own axes at its CG, turning and tilting with it; red X forward, green Y right, blue Z up; on by default), **North Arrow**, **Humans Through Bodywork**, **Vehicle Extents** (a translucent box at the vehicle's declared extents) and **DyMESH Wheel Mesh**. The View menu itself has **Show Guidance Text** (the long explanatory notes in the dialogs, off by default; messages about a problem with the open case are always shown), **Panels Outside the Main Window**, **Outliner**, **Shader Editor** and **Dope Sheet**.

<!-- NAV -->

---

← Previous: [Object Attributes Dialog Box](ObjAttrDlg.md)  |  [Index](README.md)  |  Next: [Overlays Dialog Box](OverLayDlg.md) →

<!-- /NAV -->
