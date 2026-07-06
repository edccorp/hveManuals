# Accelerometers Dialog

The Accelerometers dialog (title: *Accelerometer Data: [vehicle name]*) allows the user to assign the vehicle-fixed x, y, z coordinates for up to five accelerometers. The simulation model can then return the velocity and acceleration at each selected location. Accelerometers are assigned in event mode using this dialog.

Coordinates are entered in the vehicle-fixed coordinate system. If the vehicle dimensions basis is set to Total (rather than Sprung) in the Options, the displayed coordinates are adjusted accordingly.

## Location No.

A drop-down list used to select the accelerometer device being edited (1 through 5). All remaining fields apply to the currently selected device.

## Device In Use

A checkbox indicating whether the selected accelerometer is in use. Default: not in use. When unchecked, the coordinate fields below are disabled.

## Coordinates (in) - x

Vehicle-fixed x coordinate of the accelerometer. Default: 0. Typical range ±300 in; allowed range ±500 in.

## y

Vehicle-fixed y coordinate of the accelerometer. Default: 0. Typical range ±102 in; allowed range ±500 in.

## z

Vehicle-fixed z coordinate of the accelerometer. Default: 0. Typical range ±300 in; allowed range ±500 in. This field is read-only if the event's calculation method does not compute 3-dimensional position and velocity (per the physics program's options).

---
*Source topic: AcclMtrsDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Safety Systems](README.md)  |  [Index](README.md)  |  Next: [Air Bag Restraints Dialog Box](AirBagDlg.md) →

<!-- /NAV -->
