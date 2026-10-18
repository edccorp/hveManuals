# Getting Information about the Vehicle

**Vehicle Information Dialog**

!!! note "HVE 2027"
    HVE 2027 has no Vehicle Information dialog. HVE's Vehicle Information
    fields are edited in the Vehicle Editor's **Vehicles** panel, in its
    **Identity** and **Configuration** sections; the fields below are
    described as they appear there.

New vehicles are added to the case in the Vehicle Editor (**Vehicle (F3)** tab): the **Vehicles** panel lists every vehicle in the case, and its **Add...**, **Replace...**, **Dup** and **Del** buttons add a vehicle from a database or from HVE's generic vehicles, replace the selected vehicle's data with a database record, copy it, or remove it. Below the list the panel is the selected vehicle's editor: **Identity**, **Configuration**, **Size & Weight**, **Inertia**, **Components** and **3D Geometry** (see [Creating & Editing Vehicles](../hve-users/04-vehicle-editor/10-creating-editing-vehicles.md#vehicles-panel)).

![Vehicles panel](images/hvn-vehicles-panel.png)

While the active event's results are on screen the vehicles they were solved with are locked; reset the run to edit them.

## Identity

### Name
A user-editable name for the vehicle. A red note appears if another vehicle in the case already uses the same name.

### Type
Defines the basic vehicle type. The choices are:

- Passenger Car
- Pickup
- Multi-Purpose
- Van
- Truck
- Trailer
- Dolly
- Fixed Barrier
- Movable Barrier
- Other
- Motorcycle

When a vehicle database is loaded, changing the type re-runs the database lookup below.

## Database Lookup

When a vehicle database is loaded, **Make**, **Model**, **Year**, **Body Style** and **Source Database** are lists filled from the loaded databases; each selection filters the choices available in the lists below it, as in HVE.

When no database is loaded, Make, Model, Year and Body Style are plain text fields so the vehicle can be identified by hand, and the source database is shown read-only.

To search the databases by free text (for example *honda accord*), use the **Filter** of the vehicle database dialog opened by **Add...** or **Replace...**.

### Vehicle Color
The body color used to draw the vehicle. Click the swatch for a color picker, or type the red, green and blue values.

The line under the color gives the HVE version that wrote the vehicle's database record, when it is known.

## Configuration

### Number of Axles
Allowable selections are None, One, Two, Three or Four, as the vehicle type allows (a Motorcycle has two). For a Fixed Barrier the number of axles is None. The axle count is set only here; the Size & Weight section has no axle control.

### Driver Location
Allowable selections are None, Left, Center or Right. Disabled for a Fixed Barrier.

### Engine Location
Allowable selections are None, Front, Mid or Rear.

### Drive Axle(s)
Allowable selections depend on the number of axles: None; Axle 1; Axle 2; Axle 3; Axle 1 & 2; Axle 2 & 3; or Axle 1,2 & 3.

Engine Location and Drive Axle(s) are disabled for a vehicle without a powertrain: a Fixed Barrier, Trailer, Dolly or Movable Barrier, a vehicle with no axles, or a vehicle whose Driver Location is None. Setting the number of axles to None, or the driver location to None, also resets the engine location and drive axle to None. These rules are applied when you change one of these fields; an imported case keeps what it states.

## 3D Geometry

### 3D File
In HVE 2027 the 3-D geometry file is the **Mesh File** of the Vehicles panel's **3D Geometry** section (with **...** to browse and **Library...**), and everything else about the model is in the Vehicle Mesh window (**Vehicle › Editors › Vehicle Mesh...**, or **Vehicle Mesh...** in that section). See [Geometry File](../hve-users/04-vehicle-editor/11a-sprung-mass.md#geometry-file).

## Tools

### Wizard...
HVE's Vehicle Wizard is the Vehicles panel's **Size & Weight** section, applied as you type; there is no separate Wizard window.

### Vehicle Properties
The vehicle's property dialogs are buttons in the Vehicles panel's **Components** section (every vehicle data dialog, grouped as Chassis, Body, Equipment and Occupant Protection), and items of the **Vehicle** menu. The Inertia / Mass dialog (see [Vehicle Inertia Dialog](VehInerDlg.md)) is opened with **Edit...** in the panel's **Inertia** section.

### Save As...
Use **Vehicle › Save Vehicle As...** (see [Save Vehicle As dialog](VehSaveAs.md)) or **Vehicle › Save to My Vehicles...**.

### Delete
**Delete from database...**, in the Identity section, removes the vehicle's record from its database file after a confirmation prompt. It is shown only when the record is in one of your own, writable databases (for example *My Vehicles*). The record is permanently removed from the database file; the vehicle in the case is kept (use **Del** in the Vehicles panel to remove it from the case).

!!! note "HVE 2027"
    All of HVE's Vehicle Information fields are in the Vehicles panel, in its Identity and Configuration sections. The type list says *Multi-Purpose* where HVE's says *Sport-Utility*.

!!! tip "New in HVE 2027"
    - Vehicle types **Other** and **Motorcycle**, and a fourth axle. A Motorcycle always has two axles; under Vehicle Type a **Seed Generic Motorcycle** button fills class-typical data, and a note explains that a single-track vehicle is modelled by a narrow-track approximation.
    - The Components section opens every vehicle data dialog from one place.

<!-- NAV -->

---

← Previous: [Vehicle Drag Dialog](VehDragDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Inertia Dialog](VehInerDlg.md) →

<!-- /NAV -->
