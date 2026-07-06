# Saving Vehicles

**Save As New Vehicle Dialog Box**

New vehicles may be added to the user vehicle database (user.db), thus extending the vehicle library. When OK is chosen, the vehicle is written to the user database using the keys entered below. If a vehicle with the same Type/Make/Model/Year/Body Style keys already exists, the user is asked whether to overwrite it. After saving, the vehicle database is rebuilt and the saved vehicle becomes the current vehicle.

This dialog box contains the following items:

## Vehicle Type
The basic type of the vehicle being saved (Passenger Car, Pickup, etc.). This field is read-only; the type is inherited from the current vehicle.

## Make
Specify the vehicle manufacturer.

## Model
Specify the vehicle model.

## Year
Specify the model year.

## Body Style
Specify the vehicle body style (e.g., 2-Dr Hardtop, 4-Dr Sedan, etc.).

## Security Key
Specify the security key for the vehicle. This key may be used to restrict access to proprietary vehicle data.

## Version Information
Specify version information for the vehicle. This text is stored with the vehicle's database entry so revisions of the same vehicle can be identified.

## Geometry File Name
The current vehicle may be visualized using a simplified vehicle shape or an actual 3-D geometry file created by digitizing the vehicle. If a 3-D geometry file is available for the current vehicle, its file name may be entered here and is stored with the saved vehicle.

---
*Source topic: VehSaveAs.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Vehicle Inertia Dialog](VehInerDlg.md)  |  [Index](README.md)

<!-- /NAV -->
