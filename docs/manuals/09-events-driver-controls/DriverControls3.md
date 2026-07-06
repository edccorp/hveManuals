# Driver Controls Brake

Applies longitudinal tire forces that attempt to slow the vehicle.

This page enables the user to enter data for the following items.

## Table

Selects the type of brake table (the available choices depend on the calculation method):

- **Pedal Force** — This method allows the user to enter a table of brake pedal force versus time. The vehicle's brake system model converts the pedal force to a brake torque, and thus a longitudinal force, at each wheel. This is the only option that engages the vehicle's brake system (and Brake Designer) data.
- **Wheel Force** — This method allows the user to enter a table of brake force (attempted longitudinal force decelerating the vehicle) versus time at each wheel. The resulting table determines how much decelerating force is applied at each wheel. The table contains a pair of columns (right/left) for each axle.
- **Available Friction** — This method allows the user to enter a table of available frictional braking force (percentage of the total available frictional force braking the vehicle) versus time at each wheel. The calculations are performed by the simulation model, which multiplies the entered value by the currently available tire friction and vertical tire load. The table contains a pair of columns (right/left) for each axle.

## Data Grid

A table of the selected brake quantity versus time. Rows may be added, duplicated and edited directly in the grid. The *Copy Cell* and *Copy Row* buttons at the bottom of the Driver Controls dialog may be used to fill all columns of a row from column 1 and to duplicate rows.

---
*Source topic: DriverControls3.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Wheel Data](DriverControls2.md)  |  [Index](README.md)  |  Next: [Driver Controls Throttle](DriverControls4.md) →

<!-- /NAV -->
