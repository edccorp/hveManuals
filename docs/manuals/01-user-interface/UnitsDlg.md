# Units Dialog Box

Allows the user to specify the current system of units. HVE maintains two basic sets of units: program units and user units.

Program units are always pounds, inches and seconds (and derivatives of these basic quantities). These units are used for all the internal workings and the user never sees them. Instead, the user sees the user units, which may be defined according to the user's needs through the use of the proper conversion factors. These conversion factors convert all the user's entries into program units so HVE can operate on them, and also convert all the program's results back into user units.

The dialog contains a *Current Units* group with three choices:

## U.S

Sets US units as the current system of units.

## S.I

Sets SI (metric) units as the current system of units.

## Custom

Sets a user-defined system of units, built from custom conversion factors defined in HVE's unit resources. This allows mixing of unit choices (for example, US units with velocities in mph).

Pressing **OK** applies the selected unit system throughout HVE: key results displays, variable output reports, the Position/Velocity dialog and the Distance Tool are all immediately converted to the new units.

> Note: The *Set Custom Units* button described in earlier versions of this help topic is no longer present in the dialog.

---
*Source topic: UnitsDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Text Editor Dialog Box](TextEdDlg.md)  |  [Index](README.md)

<!-- /NAV -->
