# Airbag Restraint System Dialog Box

The Airbag Restraint System dialog is used in event mode to place an installed airbag in use for a specific occupant and to control when it deploys. The airbag itself (deploy location, bag geometry, gas properties, etc.) must first be installed on the vehicle using the vehicle editor's Air Bag dialog; a location's controls are enabled only if an airbag is installed there.

## Airbag Restraints For

A drop-down list used to select the occupant (and seat location) receiving the airbag. Each occupied position is listed by the human's name followed by an abbreviated seat position label — (F/R), (F/C), (F/L), (B/R), (B/C), (B/L), (R/R), (R/C), (R/L) — for the nine possible occupant locations (Front/Back/Rear rows, Right/Center/Left positions). Unoccupied positions are not listed. A position can only be selected if the human at that position has an Initial Position human kit placed in the event; otherwise an error message is displayed and the previous selection is restored.

## Device In Use

A checkbox that determines whether the airbag restraint installed at the selected location is in use for this event. Default: not in use. This checkbox is enabled only if an airbag is installed at the selected location on the vehicle. When unchecked, the remaining controls in the dialog are disabled.

## Airbag Contacts

A multiple-selection list containing the contact ellipsoids of the human at the selected location (all ellipsoids of all body segments). Select the ellipsoid(s) that may contact the airbag; only the selected ellipsoids will develop contact forces with the airbag. (Note: earlier versions of this help described this field as the vehicle contact surface supporting the airbag; that surface is now assigned as the Backside Contact Surface in the vehicle editor's Air Bag dialog.)

## AutoStart

A checkbox that determines how airbag deployment is triggered. When checked, deployment is started automatically by the simulation and the two fill-time fields below are disabled. When unchecked, the user specifies the deployment timing using Airbag Begin Fill Time and Airbag Fill Duration.

## Airbag Begin Fill Time (sec)

The simulation time at which the airbag begins to fill. Default: 0.0010 sec. Allowed range 0.0010-40.0 sec. Only editable when AutoStart is unchecked.

## Airbag Fill Duration (sec)

The length of time over which the airbag fills. Default: 0.05 sec. Typical range 0.0001-0.20 sec; allowed range 0-40 sec. Only editable when AutoStart is unchecked.

---
*Source topic: AirBagSysDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Air Bag Restraints Dialog Box](AirBagDlg.md)  |  [Index](README.md)  |  Next: [Belt Restraint System Dialog Box](BeltResSysDlg.md) →

<!-- /NAV -->
