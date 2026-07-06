# Driver Controls Throttle

Applies longitudinal tire forces that attempt to accelerate the vehicle.

This page enables the user to enter data for the following items.

## Table

Selects the type of throttle table (the available choices depend on the calculation method):

- **Wide-open Throttle** — This method allows the user to enter a table of percent of wide-open throttle versus time. The vehicle's drivetrain model converts the throttle setting to engine torque, and thus to tractive force at each drive wheel. This option engages the vehicle's engine and drivetrain data.
- **Tractive Effort** — This method allows the user to enter a table of tractive effort (total force accelerating the vehicle) versus time. The resulting table determines how much accelerating force is applied at each drive wheel. The table contains a pair of columns (right/left) for each drive axle.
- **Available Friction** — This method allows the user to enter a table of available friction force (percentage of the total available frictional force accelerating the vehicle) versus time. The calculations are performed by the simulation model, which multiplies the entered value by the currently available tire friction and vertical tire load. The table contains a pair of columns (right/left) for each drive axle.

## Data Grid

A table of the selected throttle quantity versus time. Rows may be added, duplicated and edited directly in the grid. The *Copy Cell* and *Copy Row* buttons at the bottom of the Driver Controls dialog may be used to fill all columns of a row from column 1 and to duplicate rows.

## Use Clutch/Torque Converter

When checked, the drivetrain model includes the clutch (manual transmission) or torque converter (automatic transmission) when computing the drive torque delivered to the wheels.

---
*Source topic: DriverControls4.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Brake](DriverControls3.md)  |  [Index](README.md)  |  Next: [Driver Controls Gear](DriverControls5.md) →

<!-- /NAV -->
