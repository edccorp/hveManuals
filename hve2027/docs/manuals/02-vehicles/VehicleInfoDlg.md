# Getting Information about the Vehicle

**Vehicle Information Dialog**

New vehicles are added to the case in the Vehicle Editor (**Vehicle (F3)** tab): the **Vehicles** panel lists every vehicle in the case, and its **Add...**, **Replace...**, **Dup** and **Del** buttons add a vehicle from a database or from HVE's generic vehicles, replace the selected vehicle's data with a database record, copy it, or remove it. The identification and configuration of the selected vehicle are viewed and edited in the Vehicle Information dialog, opened with **Vehicle › Vehicle Information...** in the Vehicle Editor. The **Information** section at the top of the Vehicles panel carries the same identification and configuration fields, so most of these values can be edited in either place.

![Vehicles panel](images/hvn-vehicles-panel.png)

![Vehicle Information dialog](images/hvn-vehicle-info.png)

The **Vehicle** list at the top of the dialog selects which vehicle the dialog edits, and the note beside it says whether that vehicle is in the active event. While the active event's results are on screen the vehicles they were solved with are locked; reset the run to edit them.

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

## Vehicle Search

Shown only when a vehicle database is loaded. Type any part of the make, model or year (for example *honda accord* or *1998 or 1999*) and the matching database records are listed with their type, make, model, year, body style and source database. Click a match to load it into the vehicle. **Clear** empties the search.

## Database Lookup

When a vehicle database is loaded, **Make**, **Model**, **Year**, **Body Style** and **Source Database** are lists filled from the loaded databases; each selection filters the choices available in the lists below it, as in HVE.

When no database is loaded, the same five fields are plain text fields so the vehicle can be identified by hand.

## Configuration

### Number of Axles
Allowable selections are None, One, Two, Three or Four. For a Fixed Barrier the list is disabled and the number of axles is None.

### Driver Location
Allowable selections are None, Left, Center or Right. Disabled for a Fixed Barrier.

### Engine Location
Allowable selections are None, Front, Mid or Rear.

### Drive Axle(s)
Allowable selections depend on the number of axles: None; Axle 1; Axle 2; Axle 3; Axle 1 & 2; Axle 2 & 3; or Axle 1,2 & 3.

Engine Location and Drive Axle(s) are disabled for a vehicle without a powertrain: a Fixed Barrier, Trailer, Dolly or Movable Barrier, a vehicle with no axles, or a vehicle whose Driver Location is None. Setting the number of axles to None, or the driver location to None, also resets the engine location and drive axle to None.

### Vehicle Color
The body color used to draw the vehicle. Click the swatch for a color picker, or type the red, green and blue values.

## 3D Geometry

### 3D File
The 3-D geometry file used to draw the vehicle (OBJ, Inventor/VRML or HVE `.h3d`: `.obj`, `.iv`, `.wrl`, `.h3d`). **Browse...** picks the file; **Load 3D File** loads it, and **Clear** removes it so the vehicle is drawn with a generic body. A status line reports whether the load succeeded. Scaling, moving and rotating the model is done in the Vehicle Mesh dialog (**Vehicle › Vehicle Mesh...**).

## Tools

### Wizard...
Starts the Vehicle Wizard for building a custom vehicle. The button is enabled for Passenger Car, Pickup, Multi-Purpose, Van, Truck, Trailer and Dolly types having 1 to 3 axles; it is disabled for barriers, Other and Motorcycle, and while the vehicle is locked by results on screen.

### Vehicle Properties
Expands a list of buttons that open the vehicle's property dialogs: **Inertia / Mass...** (see [Vehicle Inertia Dialog](VehInerDlg.md)), **Aerodynamic Drag...** (see [Vehicle Drag Dialog](VehDragDlg.md)), **Tires...**, **Brakes...**, **Suspension...**, **Steering...** and **Connections...**. The same list appears in the Vehicles panel under **Vehicle Properties**.

### Save As...
Displays the [Save Vehicle As dialog](VehSaveAs.md), used to write the vehicle to a vehicle database.

### Delete
Removes the vehicle record from its source database file after a confirmation prompt. Enabled only when the vehicle was loaded from a writable user database (a database whose name contains *user*). The vehicle entry is permanently removed from the database file; the vehicle in the case is not deleted (use **Del** in the Vehicles panel for that).

!!! note "HVE 2027"
    The dialog shows all of HVE's Vehicle Information fields, grouped into Identity, Database Lookup, Configuration, 3D Geometry and Tools sections, and adds a free-text **Vehicle Search** across the loaded databases. The type list says *Multi-Purpose* where HVE's says *Sport-Utility*.

!!! tip "New in HVE 2027"
    - Vehicle types **Other** and **Motorcycle**, and a fourth axle. A Motorcycle always has two axles; in the Vehicles panel a **Seed Generic Motorcycle** button fills class-typical data, and a note explains that a single-track vehicle is modelled by a narrow-track approximation.
    - The 3-D geometry file is chosen here as well as in the Vehicle Mesh dialog.
    - Vehicle Properties buttons that open the vehicle's other property dialogs from one place.

<!-- NAV -->

---

← Previous: [Vehicle Drag Dialog](VehDragDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Inertia Dialog](VehInerDlg.md) →

<!-- /NAV -->
