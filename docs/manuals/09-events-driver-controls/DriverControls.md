# Driver Controls

This dialog box is used to assign Steering, Braking, Throttle, Gear selection, HVE Driver (path/speed follower), Wheel Data and Lights data for the selected vehicle.

This dialog box allows the user to enter parameters which describe how the driver attempted to control the vehicle. It is a tabbed property sheet; the pages that appear depend on the capabilities of the current event's calculation method and on the selected vehicle:

- **Steer** — steer table (this topic, below)
- **Brake** — see [Driver Controls Brake](DriverControls3.md)
- **Throttle** — see [Driver Controls Throttle](DriverControls4.md)
- **Gear** — see [Driver Controls Gear](DriverControls5.md)
- **HVE Driver** (path follower) — see [Driver Controls Path Follower](DriverControls7.md)
- **Wheel Data** — see [Driver Controls Wheel Data](DriverControls2.md)
- **Lights** — light systems activation (only shown when the calculation method supports light systems and the vehicle has lights defined). Select a light from the Light Name List, check *Is Active*, and choose the activation method: *Use Driver Controls* or *User-Entered* start/end time table. For turn signals, the *On/Off Cycle Time (sec)* and *Min Steer Angle (deg)* may also be entered.

Two table-editing buttons appear at the bottom of the sheet for the Steer, Brake and Throttle table pages:

- **Copy Cell** — copies the value in column 1 of the current row to all remaining columns of the row.
- **Copy Row** — inserts a duplicate of the current table row.

## Steer

Applies steer angles that attempt to steer the vehicle.

This page enables the user to enter data for the following items.

## Table

Selects the type of steer table (the available choices depend on the calculation method):

- **At Steering Wheel** — This method allows the user to enter a table of steering wheel angle versus time. The entered value is divided by the axle's steering gear ratio to determine the nominal steer angle at the tire.
- **At Axle** — This method allows the user to enter a table of steer angle at each tire of a steerable axle versus time. The entered value is applied directly to the tire, and is unaffected by any roll steer or toe-in. The table contains a pair of columns (right/left) for each steerable axle.

## Data Grid

A table of steering angle versus time. Rows may be added, duplicated and edited directly in the grid.

## Use Ackermann Steering

When checked, the simulation applies Ackermann geometry to the steer angles, so that the inside and outside tires of a steerable axle are steered through slightly different angles.

---
*Source topic: DriverControls.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Contacts Dialog Box](ContactsDlg.md)  |  [Index](README.md)  |  Next: [Driver Controls Path Follower Method](DriverControls1.md) →

<!-- /NAV -->
