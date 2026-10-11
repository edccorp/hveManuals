# Chapter 10 — Creating & Editing Vehicles

*Adapted for HVE 2027 from the HVE User's Manual (Version 5, Seventh
Edition, Jan 2006), Chapter 10.*

The Vehicle Editor is used for creating and editing the vehicles of the
current case. This chapter describes how to use it, beginning with its
components.

> **NOTE:** Refer to the next chapter, [Vehicle Model Definition](11a-sprung-mass.md),
> for a detailed description of each Vehicle Model parameter.

## Vehicle Editor Components

To use the Vehicle Editor, select the **Vehicle (F3)** tab under the menu
bar, or press **F3**. HVE 2027 opens in the Vehicle editor. Its components
are:

- **Vehicles panel** — Docked at the left. Used for adding vehicles to the
  case, selecting the current vehicle and editing its basic attributes,
  dimensions and weights. It takes the place of HVE's Vehicle Editor dialog.
- **Viewport** — Displays the current vehicle.
- **Vehicle menu** — Present on the menu bar only in the Vehicle editor. It
  opens the Vehicle Information dialog and every vehicle data dialog (see
  [Selecting and Editing Vehicles](#selecting-and-editing-vehicles)).

![Figure 10-1](../images/hvn-04-vehicle-editor.png)
*Figure 10-1: HVE 2027 Vehicle Editor — the Vehicles panel, the Vehicle menu and the viewport.*

### Vehicles Panel

The Vehicles panel is the heart of the Vehicle Editor. Its toolbar and list
manage all the vehicles in the case:

- **Add…** — Adds a vehicle to the case from a vehicle database or from
  HVE 2027's built-in generic vehicles (see Adding New Vehicles, below).
- **Replace…** — Replaces the current vehicle's data with a database record,
  keeping its place in the case and in its events.
- **Dup** — Adds a copy of the current vehicle with every setting, named
  "*name* (copy)". The copy is not added to any event.
- **Del** — Removes the current vehicle from the case.
- **Vehicle list** — The names of all the vehicles in the case, each with
  its color swatch. Click a name to make it the current vehicle. Drag a name
  to reorder the list.

Below the list, the panel shows the current vehicle in collapsible sections:

- **Information** — Name, Vehicle Type, Make, Model, Year, Body Style, Source
  DB, Number of Axles, Driver Location, Engine Location, Drive Axle(s),
  Color, and **Save As…**.
- **Dimensions / Inertias** — HVE's Vehicle Wizard, applied as you type:
  the axle count, total weight and its front/rear distribution and axle
  weights, the overall dimensions, CG height, wheelbase, overhangs, CG to
  axle distances, axle spacings and track widths, with the resulting axle
  layout. Below it are **Exterior Extents** (the derived CG-to-front, back,
  side, top and bottom distances the solver receives), **Wheel Positions
  (from CG)** (per-wheel x, y, z overrides), **Dimensions From CG** (CG to
  axle and CG height on the total and sprung bases, and trailer connection
  geometry) and **Inertia** (weight and roll, pitch and yaw inertia on the
  total and sprung bases, and the XZ product).
- **Vehicle Properties** — Buttons for Inertia / Mass, Aerodynamic Drag,
  Tires, Brakes, Suspension, Steering and Connections.
- **3D Geometry** — The vehicle's 3-D model file, with Browse, Load 3D File
  and Clear.

![Figure 10-2](../images/hvn-04-vehicles-panel.png)
*Figure 10-2: The Vehicles panel, with its Information, Dimensions / Inertias, Vehicle Properties and 3D Geometry sections.*

> **NOTE:** Deleting a vehicle deletes it only from the current case, NOT
> from the database! Events that used it are updated.

!!! note "HVE 2027"
    - A case always holds at least one vehicle, so **Del** is disabled when
      only one is left. HVE's rule that a vehicle used in an event cannot be
      deleted does not apply: HVE 2027 removes it from those events.
    - While the results of a simulation are on screen, the data of the
      vehicles that run used is read-only, and Add, Replace, Dup, Del and
      reordering are disabled as they would change it. Reset the run to edit.
    - Edit › Undo (Ctrl+Z) undoes vehicle edits.
    - Many vehicle dialogs carry explanatory notes — which simulation reads a
      field, what convention a number is in. They are shown with **View ›
      Show Guidance Text** (off by default). Notes that say a field reaches
      no simulation, or that HVE 2027 differs from HVE, are always shown.

### Viewport

The viewport displays the current vehicle. The view controls are described
in the user-interface section of this manual (Top / Front / Side / Momentum /
3D views; the hints along the top of the viewport list the keys).

!!! warning "Not in HVE 2027"
    HVE's Vehicle Viewer offers pickable components — the CG sphere, the
    wheels, the exterior spheres, the brake master cylinder, the steering
    wheel and the engine — each opening that component's dialogs. HVE 2027
    has no pickable components: every vehicle dialog is opened from the
    **Vehicle** menu or from the Vehicles panel (see
    [Selecting and Editing Vehicles](#selecting-and-editing-vehicles) for the
    map). Clicking a part of the vehicle in **Edit Mode** selects it for a
    display material (see [Edit Mode](#edit-mode-materials-per-part)).

> **NOTE:** Although every vehicle's properties are defined using the Vehicle
> Editor, vehicles are not positioned using the Vehicle Editor. The position
> of a vehicle in an event is an event-related issue, and is performed using
> the Event Editor. Think of it this way: At this point, we don't care if the
> Buick crashes, rolls over or simply slows to a stop. All we care about is
> that the Buick weighs 2970 pounds and has other properties of our choosing.

## Adding New Vehicles

To add a new vehicle, press **Add…** in the Vehicles panel. The Add Vehicle
dialog is displayed (Figure 10-3). It lists every vehicle in the vehicle
databases (`.db` files) HVE 2027 has found, and contains:

- **Database folders** — The folders searched for `.db` files, each database
  with its vehicle count. The databases installed with HVE 2027 are found
  without any setup. To use other databases, type or **Browse…** to a folder
  and press **Add**; the folder is remembered for later sessions. **Remove**
  removes a folder you added.
- **Built in (no database needed)** — HVE 2027's generic vehicles, grouped by
  type and class, with their own **Add** button. These are available even
  when no database is installed.
- **Filter** — Shows only the vehicles whose make, model, year or name
  contains the text typed. **Clear** clears it; **Generics** shows HVE's
  generic vehicles (Generic.db: one per class of car, sport-utility, pickup,
  truck, van and trailer).
- **Vehicle table** — Name, Make, Model, Year, Body and Type. Click a column
  heading to sort by it; click again to reverse; Shift-click a second heading
  to add a tie-break. The line under the table summarizes the selected
  vehicle (mass, weight, axles, yaw inertia, CG location).
- **Add Vehicle** / **Cancel**.

![Figure 10-3](../images/hvn-04-vehicle-database.png)
*Figure 10-3: The vehicle database dialog. Opened with Add… it is titled Add Vehicle; opened with Replace… (shown) it is titled Load Vehicle from Database and replaces the current vehicle's data.*

Select a vehicle and press **Add Vehicle**. The vehicle is added to the case,
becomes the current vehicle, and is also added to the active event.

> **NOTE:** EDC's databases are licensed. The databases HVE 2027 can read are
> the ones present on your computer.

> **NOTE:** The same vehicle Make, Model, Year and Body Style may be
> contained in more than one database.

After adding the vehicle, set the remaining attributes in the Information
section of the Vehicles panel or in the Vehicle Information dialog (Vehicle ›
Vehicle Information):

- **Name** — A user-editable name for the vehicle. The Vehicle Information
  dialog warns if another vehicle in the case already uses the name.
- **Type** — Passenger Car, Pickup, Multi-Purpose, Van, Truck, Trailer,
  Dolly, Fixed Barrier, Movable Barrier, Other or Motorcycle.
- **Make, Model, Year, Body Style, Source Database** — With a database
  loaded these are HVE's drill-down: each list is filtered by the selection
  above it, and choosing a different leaf replaces the vehicle's data with
  that database record. Without a database they are plain text.
- **Number of Axles** — None, One, Two, Three or Four in the Vehicle
  Information dialog. For a Fixed Barrier the only selection is None.
- **Driver Location** — None, Left, Center or Right.
- **Engine Location** — None, Front, Mid or Rear.
- **Drive Axle(s)** — Axle 1, Axle 2, Axle 3, Axle 1 & 2, Axle 2 & 3 or
  Axle 1,2 & 3, as the number of axles allows. Engine Location and Drive
  Axle(s) are disabled for a Trailer, Dolly or barrier.

!!! tip "New in HVE 2027"
    - The Vehicle Information dialog has a **Vehicle Search** box: type, for
      example, "honda accord" or "1998 or 1999" to list matching database
      records, and click one to load it.
    - **Motorcycle** is a vehicle type. Choosing it seeds a generic machine
      and rider; **Seed Generic Motorcycle** in the Vehicles panel re-seeds
      it. A motorcycle is a narrow-track approximation (see the motorcycle
      chapter of this manual set).

The **Wizard…** button in the Vehicle Information dialog opens HVE's Vehicle
Wizard as a separate window. It is enabled for Passenger Car, Pickup,
Multi-Purpose, Van, Truck, Trailer and Dolly types having 1 to 3 axles. The
same wizard is drawn, live, in the Vehicles panel's Dimensions / Inertias
section.

![Figure 10-4](../images/hvn-04-vehicle-information.png)
*Figure 10-4: Vehicle Information dialog (Vehicle › Vehicle Information).*

### Vehicle Database

The vehicle *Type, Make, Model, Year* and *Body Style* are keys used to
select a vehicle from the Vehicle Database. These keys provide the basic
vehicle definition, while the *Number of Axles, Driver Location, Engine
Location* and *Drive Axle(s)* provide the exact configuration.

The Vehicle Editor creates a copy of the selected vehicle for use in the
current case. The properties of this vehicle may be edited. Changes made to
the current vehicle do not affect the Vehicle Database.

### Save-As New Vehicle

To add the current vehicle to a database, choose **Vehicle › Save Vehicle
As**, or **Save As…** in the Vehicles panel or the Vehicle Information
dialog. The Save Vehicle As dialog (Figure 10-5) contains:

- **Identification** — Name, Type, Make, Model, Year and Body Style for the
  new record.
- **File & Version** — Geometry File, Version Info and Security Key.
- **Database** — **Database File**: the `.db` file to write. It defaults to
  `user.db` in a folder HVE 2027 may write to, never to an installed
  database.
- **Save to Database** — Writes the record.
- **Apply to Vehicle** — Copies the identification back onto the vehicle in
  the case, without writing a database.

![Figure 10-5](../images/hvn-04-save-vehicle-as.png)
*Figure 10-5: Save Vehicle As dialog.*

!!! warning "Not in HVE 2027"
    **Save to Database writes the database record the vehicle was loaded
    from, not the edited vehicle.** It copies that record and replaces only
    its identification (name, type, make, model, year, body style), its
    configuration (number of axles, driver location, engine location, drive
    axles) and its color. Edits to inertias, dimensions, suspension, tires,
    brakes and every other property are not written. The Geometry File,
    Version Info and Security Key fields are not written either. Save to
    Database is available only when the vehicle's Make, Model, Year and Body
    Style match a loaded database record. To keep an edited vehicle, save the
    case (File › Save Case).

A vehicle in a writable user database can be removed from it with
**Delete** in the Vehicle Information dialog.

## Adding Vehicles from Previous Cases

!!! warning "Not in HVE 2027"
    HVE 2027 has no Previous Vehicle Selection dialog (HVE's Mode › Vehicle ›
    Add › Previous). To reuse a vehicle from another case, open that case
    with File › Open Case... (an HVE `.hve` case or an HVE 2027 case); to vary a
    vehicle within a case, use **Dup**.

## Selecting and Editing Vehicles

The last vehicle added becomes the current vehicle. To select and edit any
vehicle:

1. Click its name in the Vehicles panel's list. The selected vehicle becomes
   the current vehicle and is displayed in the viewport. Every vehicle dialog
   also has a vehicle selector at its top.
2. If desired, edit its basic attributes in the Information section, or in
   the Vehicle Information dialog (Vehicle › Vehicle Information).
3. If desired, edit the vehicle's properties with the dialogs listed below.

The vehicle data that HVE reaches by clicking the vehicle's components is
reached in HVE 2027 as follows:

| HVE component and data | HVE 2027 |
|---|---|
| CG: Inertias | Vehicles panel › Vehicle Properties › **Inertia / Mass…**; also the panel's Dimensions / Inertias section |
| CG: Move CG | **Vehicle › Vehicle Mesh** (Move CG); for EDSMAC/EDSMAC4 events also **Event › Move CG** |
| CG: Color | Vehicles panel Information › **Color**; Vehicle Information › **Vehicle Color** |
| CG: Geometry File | Vehicles panel › **3D Geometry**; **Vehicle › Vehicle Mesh** |
| CG: Contact Surfaces | **Vehicle › Contact Surfaces** |
| CG: Belt / Airbag Restraints | **Vehicle › Belt Restraint**, **Vehicle › Airbags** (one bag per seat) |
| CG: Connections | Vehicles panel › Vehicle Properties › **Connections…** |
| CG: Aerodynamic Drag | **Vehicle › Aero Dynamic Drag** |
| CG: Body Torsion | **Vehicle › Body Torsion** |
| CG: Lights | **Vehicle › Vehicle Lights** |
| Wheel: Suspension | **Vehicle › Suspension Data**, **Vehicle › Advanced Suspension** |
| Wheel: Tire | **Vehicle › Tire Data (Detailed)**, **Vehicle › Tire Tables** |
| Wheel: Brake | **Vehicle › Brake Assembly**, **Vehicle › Brake Designer** |
| Wheel: Location | Vehicles panel › Dimensions / Inertias › **Wheel Positions (from CG)** |
| Exterior: dimensions | Vehicles panel › Dimensions / Inertias |
| Exterior: stiffness | **Vehicle › Crush Stiffness**; also **Event › Crush Profile** (Crush & Geometry), for EDCRASH, EDSMAC and EDSMAC4 events |
| Brake master cylinder | **Vehicle › Brake System Pressure**, **Vehicle › ABS / Brake Design** |
| Steering wheel | **Vehicle › Steering System** |
| Engine | **Vehicle › Drivetrain** |

The Vehicle menu also offers **Brake Material Props**, **Accelerometers**,
**Advanced Mesh Options** (the same Vehicle Mesh dialog) and **Edit Mode**.
Each of these data categories is described in the following chapter,
[Vehicle Model Definition](11a-sprung-mass.md).

### Edit Mode (materials per part)

!!! tip "New in HVE 2027"
    **Vehicle › Edit Mode (materials per part)**, or **Tab** in the Vehicle
    editor, switches the vehicle on screen into Edit Mode. Click a part of
    the vehicle — the body, the glass, a lamp lens — to select it; a panel
    in the corner of the viewport names the part and offers a **Material**
    list, **+ New** (a new material for that part alone) and **Edit in Shader
    Editor**. Press Tab again to leave. Parts come from the material names in
    the 3-D model file; a model that names no parts (OBJ, glTF, the generic
    body) has only the whole-vehicle material. Materials are display only
    and change no result.

<!-- NAV -->

---

← Previous: [Section Four: Vehicle Editor](README.md)  |  [Index](README.md)  |  Next: [Chapter 11 — Vehicle Model Definition (Part A: Sprung Mass)](11a-sprung-mass.md) →

<!-- /NAV -->
