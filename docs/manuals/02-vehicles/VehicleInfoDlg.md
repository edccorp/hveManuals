# Getting Information about the Vehicle

**Vehicle Information Dialog Box**

New vehicles are added to the current case using the Vehicle Editor, and the properties of the selected vehicle can be viewed and edited using the Vehicle Information dialog box. The Make, Model, Year, Body Style and Source Database lists are filled from the installed vehicle databases; each selection filters the choices available in the lists below it.

This dialog box contains the following items:

## Vehicle Name
A user-editable field allowing the user to assign a name to the current vehicle. If no name is entered, a default name is generated from the vehicle's year, make and model.

## Vehicle Type
Defines the basic vehicle type. Only types actually present in the installed vehicle databases are listed. The possible selections are:

- Passenger Car
- Pickup
- Sport-Utility
- Van
- Truck
- Trailer
- Dolly
- Fixed Barrier
- Movable Barrier

## Wizard...
Starts the Vehicle Wizard for building a custom vehicle. The button is enabled for Passenger Car, Pickup, Sport-Utility, Van, Truck, Trailer and Dolly types having 1 to 3 axles; it is disabled for Fixed and Movable Barriers.

## Make
Vehicle manufacturer, chosen from the manufacturers available in the database for the selected vehicle type.

## Model
Vehicle model, chosen from the models available for the selected make.

## Year
Model year, chosen from the years available for the selected model.

## Body Style
Vehicle body style (e.g., 2-Dr Hardtop, 4-Dr Sedan, etc.), chosen from the styles available for the selected year.

## Source Database
The vehicle database file that supplies the selected vehicle's data (e.g., the EDC database or the user database). Displays "Unknown" if the source cannot be determined.

## Number of Axles
Allowable selections are None, One, Two or Three. For a Fixed Barrier, the only selection is None.

## Driver Location
Allowable selections are None, Left, Center or Right.

## Engine Location
Allowable selections are None, Front, Mid or Rear.

## Drive Axle(s)
Allowable selections depend on the number of axles: None; Axle No. 1; Axle No. 2; Axle No. 3; Axle Nos. 1 and 2; Axle Nos. 2 and 3; or Axle Nos. 1, 2 and 3.

## Save As...
Allows the user to save the current vehicle to the user vehicle database, either overwriting an existing entry with the same keys or creating a new entry. It displays the [Save As New Vehicle dialog box](VehSaveAs.md).

## Delete
Removes the selected vehicle from its source database file after a confirmation prompt. Use with care; the vehicle entry is permanently removed from the database.

---
*Source topic: VehicleInfoDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Vehicle Drag Dialog](VehDragDlg.md)  |  [Index](README.md)  |  Next: [Vehicle Inertia Dialog](VehInerDlg.md) →

<!-- /NAV -->
