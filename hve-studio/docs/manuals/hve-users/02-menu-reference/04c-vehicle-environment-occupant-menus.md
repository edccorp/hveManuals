# Chapter 4C: Vehicle, Environment and Human Menus

*HVE User's Manual — Section Two: Menu Reference, HVE Studio edition. A new
chapter. In HVE these dialogs were reached from each editor's own dialog and
viewer (clicking a vehicle's engine, for example, opened the Drivetrain dialog).
In HVE Studio each editor has a menu that lists them.*

Each of these menus appears only in its own editor: **Vehicle** in the Vehicle
editor (F3), **Environment** in the Environment editor (F4), **Human** in the
Human editor (F2). The dialogs edit the vehicle, environment or human selected in
that editor. Vehicle data is locked while a solved run that used the vehicle is
on screen; press **Reset** in the Event editor to edit it.

---

## VEHICLE MENU

![The Vehicle menu](../images/hvn-02-vehicle-menu.png)
*The Vehicle menu (Vehicle editor).*

The Vehicle editor's **Vehicles** panel lists the case's vehicles, with **Add...**
(choose a vehicle from the loaded databases or one of HVE's generic vehicles),
**Replace...** (replace the selected vehicle's data with a database record),
**Dup** (copy the selected vehicle) and **Del**, and below the list the selected
vehicle's editor: **Identity**, **Configuration**, **Size & Weight**,
**Inertia** (with **Edit...** for the Inertia / Mass dialog), **Components**
(a button for each dialog below) and **3D Geometry** (see
[Chapter 10](../04-vehicle-editor/10-creating-editing-vehicles.md#vehicles-panel)).
The Vehicle menu opens the Vehicle Designer first, then the detailed dialogs
for that vehicle under **Editors**: every one of them is also hosted in a
designer stage, so the submenu is for a reader who wants one dialog alone.

| Item | Opens | Dialog reference |
|---|---|---|
| **Vehicle Designer...** | The staged Vehicle Designer for the selected vehicle, which also opens on switching to the Vehicle editor: vehicle, size & weight, mass & inertia, stiffness, geometry, tires, brakes, suspension, engine, transmission, steering, connections (with body torsion), exterior, occupant protection, test track and summary (see [Chapter 12](../04-vehicle-editor/12-vehicle-designer.md)) | — |
| **Save Vehicle As...** | Save Vehicle As: identification, geometry file, and **Save to Database** — HVE's Options › Create DB and the vehicle Save As | [Vehicle Save As](../../02-vehicles/VehSaveAs.md) |
| **Save to My Vehicles...** | Save to My Vehicles: keeps the vehicle, as edited in the case, in one of your own vehicle databases (`MyVehicles.hvedb` or one you name), where **Add...** lists it; new in HVE Studio | [My Vehicles](../04-vehicle-editor/10-creating-editing-vehicles.md#save-to-my-vehicles) |
| **Edit Mode (materials per part)** (Tab) | Switches the viewport to selecting parts of the vehicle body, to assign materials per part (as Blender's Edit Mode); new in HVE Studio | — |
| **Editors ›** **Vehicles Panel** | The Vehicles panel the Vehicle Designer replaced as the Vehicle editor's panel | — |
| **Editors ›** **Suspension Data...** | Suspension Data | [Suspension](../../03-suspension-steering/SuspDlg.md) |
| **Editors ›** **Steering System...** | Steering System | [Steering System](../../03-suspension-steering/SteerSysDlg.md) |
| **Editors ›** **Tires...** | Tire Properties: the per-wheel grid, and below it the **Load & Speed Tables** panel (friction, cornering, camber and Fy roll-off tables of the selected wheel) | [Tire Information](../../05-tires-wheels/TireInfoDlg.md), [Tire Friction Data](../../05-tires-wheels/TireFrictDataDlg.md) |
| **Editors ›** **Drivetrain...** | Drivetrain | [Drivetrain](../../04-brakes-powertrain/DriveTraDlg.md) |
| **Editors ›** **Brakes ›** **Brake Assembly...** | Brake Assembly | [Brake Assembly](../../04-brakes-powertrain/BrkAsmblyDlg.md) |
| **Editors ›** **Brakes ›** **Brake Designer...** | Brake Designer | [Brake Designer](../10-brake-designer/29-brake-designer.md) |
| **Editors ›** **Brakes ›** **Brake System Pressure...** | Brake System Pressure | [Brake System vs Pedal Force](../../04-brakes-powertrain/BrkSysVsPedFrcDlg.md) |
| **Editors ›** **Brakes ›** **ABS / Brake Design...** | A hub opening ABS System and ABS Designer | [ABS](../10-brake-designer/31-abs.md) |
| **Editors ›** **Aerodynamic Drag...** | Aerodynamic Drag | [Vehicle Drag](../../02-vehicles/VehDragDlg.md) |
| **Editors ›** **Body Torsion...** | Body Torsion | [Body Torsion](../../02-vehicles/BodyTorDlg.md) |
| **Editors ›** **Crush Stiffness...** | Crush Stiffness: one table with a column per face, A, B and Kv (2-D) and the 3-D node stiffness, with a graph of the selected column and **From crash tests...** (CRASH3 A and B from staged barrier tests) | [Stiffness Coefficient Dialog](../../02-vehicles/StiffCoeffDlg.md) |
| **Editors ›** **Vehicle Mesh...** | Vehicle Mesh, in four tabs: **File & Placement**, **Collision**, **Display** and **Wheel Images** (see [Chapter 4, Part B](04b-setup-menu.md#vehicle-mesh)) | — |
| **Editors ›** **Vehicle Lights...** | Vehicle Lights: each light's type, intensity, direction, spot parameters, position and color | — |
| **Editors ›** **Accelerometers...** | Accelerometers | [Accelerometers](../../06-safety-systems/AcclMtrsDlg.md) |
| **Editors ›** **Contact Surfaces...** | Contact Surfaces: the vehicle's interior surfaces for occupant simulations | [Contact Surfaces](../../08-environment/ContSurfDlg.md) |
| **Editors ›** **Airbags...** | Airbags | [Airbag System](../../06-safety-systems/AirBagSysDlg.md) |
| **Editors ›** **Belt Restraint...** | Belt Restraint System | [Belt Restraint System](../../06-safety-systems/BeltResSysDlg.md) |

!!! note "HVE Studio"
    - There is no **Vehicle Information** dialog: the Vehicles panel is the
      vehicle's editor ([Vehicle Information](../../02-vehicles/VehicleInfoDlg.md)
      says where each of its fields is). To search the databases, use the
      **Filter** of the dialog opened by **Add...** or **Replace...**.
    - There is no **Brake Material Props** dialog: HVE's lining and rotor
      friction library was read by no engine (see
      [Brake Material Properties](../../04-brakes-powertrain/BrkMatPropDlg.md)).
      A brake design's lining friction is in the Brake Designer.

!!! note "HVE Studio"
    The Accelerometers, Vehicle Mesh, Airbags and Belt Restraint
    dialogs are also on the Event menu. While Contact Surfaces, Airbags
    or Belt Restraint is open, that equipment is drawn in the
    viewport; View › Scene Display › Occupant Equipment draws it at any time.

---

## ENVIRONMENT MENU

![The Environment menu](../images/hvn-02-environment-menu.png)
*The Environment menu (Environment editor).*

| Item | Opens |
|---|---|
| **Environment Designer...** | The staged Environment Designer beside the 3-D view: Site, Geometry, Surfaces, Weather, Sky & Lights, Site Check and Summary (see [Chapter 14](../05-environment-editor/14-environment-designer.md)) | — |
| **Environment...** | The **Environment** panel (it opens by itself when you enter the Environment editor): **Location**, **Terrain** (the site geometry — DXF, `.h3d`, `.iv`, OBJ or glTF — a survey point cloud, and the surface materials), **Sky**, **Lights** (the site's own point and spot lights, display only), **Physical** (ambient conditions and wind, atmosphere and gravity, standing water) and **Surface Generator** (roads, friction zones, water and other surfaces drawn over the site) |
| **Aerial Image...** | Aerial Image Options: an image file laid over the site, with its world bounds (upper-left and lower-right corners) |
| **Save Environment As...** | Writes this case's environment to a file of its own (`.hveenv.json`): location, sky and lights, physical data, the site geometry with its surface types, materials, layers and placements, and the point cloud reference. The site is embedded, so the file opens on a machine without the geometry file it was read from. New in HVE Studio |
| **Load Environment...** | Replaces this case's environment with one saved by **Save Environment As...**, and reads its site. Disabled while results are on screen, because every event drives on the site. New in HVE Studio |
| **Edit Mode (materials per face)** (Tab) | Switches the viewport to selecting single faces of the site, to give them materials of their own or move them (as Blender's Edit Mode); new in HVE Studio. See [Edit Mode: faces of the site](../05-environment-editor/12-creating-editing-environments.md#edit-mode-faces-of-the-site) |

![The Environment panel](../images/hvn-01-environment.png)
*The Environment panel.*

!!! warning "Not in HVE Studio"
    HVE's 3-D Editor built environment objects from boxes, cylinders, cones,
    spheres and surfaces. HVE Studio has none of those editors: site geometry is
    imported in the Environment panel's Terrain section, or comes with the
    imported HVE case, and roads and friction zones are drawn with its Surface
    Generator.

See the dialog reference: [Environment](../../08-environment/README.md),
[Environment Information](../../08-environment/EnvtInfoDlg.md).

---

## HUMAN MENU

![The Human menu](../images/hvn-02-occupant-menu.png)
*The Human menu (Human editor); the picture predates its rename from Occupant.*

| Item | Opens |
|---|---|
| **Human Information...** | The **Humans** panel, if it has been closed (it opens by itself when you enter the Human editor) |

The Humans panel holds what HVE's Human Editor and Human Information dialog
held: **Add Human** and **Remove**, the human list, **Identity**
(Location), **Anthropometry** (subject type, age group, weight and height
percentiles, and **Regenerate GEBOD Body**), and buttons for **Injury
Tolerances...**, **Body Segments...**, **Joint Properties...** and **Body
Pose...**. A seat's airbag belongs to the vehicle (Vehicle › Editors › Airbags...). Which vehicle an occupant rides in, and
where, is set in the event (Event Information › Humans in Event).

See the dialog reference: [Humans](../../07-humans/README.md),
[Human Information](../../07-humans/HumanInfoDlg.md).

<!-- NAV -->

---

← Previous: [Chapter 4: Event Menu (Part B)](04b-setup-menu.md)  |  [Index](README.md)  |  Next: [Chapter 4D: Output Menu](04d-output-menu.md) →

<!-- /NAV -->
