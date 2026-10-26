# Section Four: Vehicle Editor

*Adapted for HVE Studio from the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Section Four "Vehicle Editor".*

The purpose of the Vehicle Editor is to provide physically correct 3-D
vehicle models for use in dynamic reconstructions and simulations. The HVE
Vehicle Model is a general purpose physical/mathematical model of a vehicle
developed by EDC. Its generality of scope allows the same model to be used
by any 2-D or 3-D reconstruction or simulation calculation method, and
provides the capacity for human occupant and pedestrian simulation as well.
The model applies to any type of vehicle having left-side and right-side
wheels, including passenger cars, pickups, vans, sport-utility vehicles,
trucks, trailers, dollies and barriers.

!!! note "HVE Studio"
    HVE Studio uses HVE's vehicle model, so the parameters described in
    Chapter 11 are HVE's. The editor around them is new: the Vehicle Editor
    is the **Vehicle (F3)** tab, the vehicles of the case are managed in its
    **Vehicles** panel, and the vehicle data dialogs are on the **Vehicle**
    menu.

## General Procedure

To use the Vehicle Editor, perform the following steps:

1. Select the **Vehicle (F3)** tab (or press F3).
2. Add one or more vehicles with **Add…** in the Vehicles panel, from a
   vehicle database or HVE Studio's built-in generic vehicles. Vehicles also
   arrive with an HVE case file (`.hve`) or an HVE Studio case opened with
   **File › Open Case...**.
3. If desired, modify the properties of the selected vehicle(s) to suit the
   needs of the current case (sprung mass, exterior, suspensions, brakes,
   tires, wheels, drivetrain, steering system and brake system).

## Overview of Section Four

- **[Chapter 10 — Creating & Editing Vehicles](10-creating-editing-vehicles.md)**
  describes the process of creating and editing vehicles: the Vehicles
  panel and the viewport, adding new vehicles from a vehicle database,
  saving a vehicle to a database, selecting and editing vehicles, and Edit
  Mode.
- **Chapter 11 — Vehicle Model Definition** provides a detailed overview of
  the HVE Vehicle Model parameters. It is split here by major heading:
  - **[Part A — Sprung Mass](11a-sprung-mass.md)**: Inertial Properties,
    Move CG, Color, Geometry File, Contact Surfaces, Belt Restraints,
    Airbag Restraints, Inter-vehicle Connections, Aerodynamic Drag and Body
    Torsion.
  - **[Part B — Exterior](11b-exterior.md)**: Vehicle Exterior Dimensions
    and Exterior Stiffness Coefficients (A, B, Kv).
  - **[Part C — Suspension](11c-suspension.md)**: Suspension Type, Roll
    Couple Distribution, Inter-tandem Load Transfer, Springs and Shocks,
    Axle Inertia, Jounce/Rebound, Spindle Axis (Alignment and Steering
    Stops), Camber & Half-track Tables, Anti-Pitch and Roll Steer.
  - **[Part D — Brakes, Tires and Wheels](11d-brakes-tires-wheels.md)**:
    Brake Assembly Parameters (and Brake Designer access), Tire Properties
    (Physical Data, Friction Data, Fy vs Slip Angle, Fy vs Inclination
    Angle, Slip vs Rolloff Tables), Wheel Location and Wheel Image.
  - **[Part E — Drivetrain, Steering and Brake System](11e-drivetrain-steering-brake-system.md)**:
    Drivetrain (Engine, Transmission, Differential), Steering System
    Parameters, Brake System Parameters and the HVE Brake Designer
    overview.
- **[Chapter 12 — Vehicle Designer](12-vehicle-designer.md)** (new in HVE Studio)
  describes **Vehicle › Vehicle Designer...**, a parametric sedan body with
  dimension and shape controls, wheel positions and a four-view preview. It is a
  design tool; it does not change the case or any simulation.

## Related Dialog References

HVE's field-by-field dialog documentation is maintained separately and
cross-linked from the chapters above:

- [Vehicles (sprung mass, dimensions, stiffness)](../../02-vehicles/README.md)
- [Suspension and Steering](../../03-suspension-steering/README.md)
- [Brakes and Powertrain (incl. Brake Designer dialogs)](../../04-brakes-powertrain/README.md)
- [Tires and Wheels](../../05-tires-wheels/README.md)

<!-- NAV -->

---

Next: [Chapter 10 — Creating & Editing Vehicles](10-creating-editing-vehicles.md) →

<!-- /NAV -->
