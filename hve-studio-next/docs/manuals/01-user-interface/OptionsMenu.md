# Options Menu

HVE Studio has **no Options menu**. HVE's Options menu mixes display switches, tools and settings dialogs; in HVE Studio they are spread over the **View** and **Tools** menus, the Event Editor's **Event** and **Output** menus, and the docked panels. The table lists every item of HVE's Options menu, in HVE's order, and where its function is in HVE Studio.

| HVE Options item | HVE Studio |
|---|---|
| Create DB | Not in HVE Studio. Vehicle databases are read as they are; **Save Vehicle As** writes a vehicle into a database file (see [Saving Vehicles](../02-vehicles/VehSaveAs.md)). |
| Show Key Results | **View › Key Results** or **Output › Key Results...** (Event and Playback editors) — see [Key Results Dialog Box](KeyResDlg.md). |
| Show Axes | **View › Scene Display › Axes**: the case's X, Y and Z at the origin and each vehicle's own axes at its CG, turning and tilting with it (red X forward, green Y right, blue Z down, as SAE and HVE; on by default). |
| Show Contacts | **View › Scene Display › Occupant Equipment** draws the active vehicle's contact surfaces, airbags and belts; **View › Scene Display › Occupant Equipment Through Bodywork** draws them over the body. |
| Show Belt Anchors | **View › Scene Display › Occupant Equipment** (as above). |
| Show Velocity Vectors | **View › Scene Display › Vectors › Velocity**. The same table in the Scene Display window has **Acceleration**, **Collision force**, **Collision moments**, **Tire Fx', Fy'**, **Tire Fz'** and **Tire Fz' (nodes)**, with **Collision load at the CG**, **Collision load at impact (line of action)** and **Draw Vectors Through Bodywork** below it. HVE's *Long Velocity Vectors* preference has no equivalent. |
| Show Skidmarks | **View › Scene Display › Skidmarks**: the contact-patch path drawn only where the tire was marking, faded by how hard. Skidmarks are drawn at the width of the tire that laid them. |
| Show Tracks | **View › Scene Display › Tire Contact Patch Paths**: where each tire touched the ground, one path per wheel. |
| Show CGs | Not available as a switch. |
| Show CG Paths | **View › Scene Display › CG Path**. **Path thickness (m)** in the same panel sets how thick CG and accelerometer paths are drawn (0 draws a hairline). |
| Show Accelerometers / Show Accelerometer Paths | **View › Scene Display › Accelerometer Path**: one path per installed accelerometer. |
| Show Position Sequences | Not in HVE Studio. |
| Show Targets | **View › Scene Display › Scene Ghosts**: **None**, **Outline**, **Translucent vehicle** or **Both**. Scene positions (HVE's targets) are drawn as an outline, a translucent copy of the vehicle, or both. |
| Show Connections | Not available as a switch. |
| Distance Tool | Not in HVE Studio. |
| Show Path | Not in HVE Studio. |
| Autoposition | Per event and per vehicle: **Auto Position (settle onto terrain)** under the vehicle in the **Vehicle Initial Conditions** section of the **Event Information** panel. It is always on for the planar methods. |
| Grid | A datum grid is drawn when no site is loaded; it has no settings. See [Set Grid Dialog Box](SetGridDlg.md). |
| Units | **Tools › Preferences... › Units** — see [Units Dialog Box](UnitsDlg.md). |
| Shadows | **View › Scene Display › Light & Shadow** (**Shadow cascades**): the sun's shadow is drawn in 1 to 4 nested layers, sharp over the vehicles and coarser out to the whole site. HVE's shadow radius, quality, precision and intensity are not offered. |
| Render (Ctrl+R) | **View › Scene Display › Rendering** — see [Render Dialog Box](RendOptDlg.md). (In HVE Studio **Ctrl+R** is **Output › Run Simulation...**, in the Event Editor: it opens the Event Designer's **Run** stage and runs the event.) |
| Playback | **Output › Playback Options...** (Event Editor) |
| Simulation Controls (Ctrl+Y) | The **Run** stage of the **Event Designer** (**Event › Event Designer...**), *Simulation Controls* section: duration, time steps, termination velocities and the integrator convergence controls the event's method uses. |
| Calculation Options (Ctrl+J) | **Method Options...** in the **Calculation Method** section of the **Event Information** panel opens the options window for the event's method (EDCRASH, EDSMAC/EDSMAC4, EDGEN, EDHIS, SIMON, EDVSM, GATB, ...). See the Calculation Options chapter. |
| DyMESH | **Event › DyMESH Options...** |
| Get Surface Info | The **Road Surface Search** section of the **Event Information** panel. |
| Preferences (Ctrl+F) | **Tools › Preferences...** — see [User Preferences Dialog Box](PrefDlg.md). |

!!! tip "New in HVE Studio"
    The Scene Display panel (**View › Scene Display**) also has **North Arrow**, **Humans Through Bodywork**, **Vehicle Extents** (a translucent box at the vehicle's declared extents), **See-Through Body**, and a DyMESH overlay table: rows **DyMESH Body** and **DyMESH Wheel**, each with a **Mesh** and a **Nodes** box. **DyMESH Body** draws the body DyMESH collides as a wireframe deformed by the run, crushed edges in red; **Nodes** draws its vertices; **DyMESH Wheel**'s **Nodes** also labels each wheel's contact model and tire law. The View menu itself has **Show Guidance Text** (the long explanatory notes in the dialogs, off by default; messages about a problem with the open case are always shown), **Panels Outside the Main Window**, **Outliner**, **Shader Editor** and **Dope Sheet**.

<!-- NAV -->

---

← Previous: [Object Attributes Dialog Box](ObjAttrDlg.md)  |  [Index](README.md)  |  Next: [Overlays Dialog Box](OverLayDlg.md) →

<!-- /NAV -->
