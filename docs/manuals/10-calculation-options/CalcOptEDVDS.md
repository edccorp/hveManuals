# EDVDS Calculation Options

EDVDS (Engineering Dynamics Corporation Vehicle Dynamics Simulator) is a simulation of the dynamic response of a vehicle towing up to three trailers. It is based on a program called Phase 4 developed at the University of Michigan Transportation Research Institute. EDVDS simulates the vehicle's response to driver inputs (accelerating, braking and steering). EDVDS determines how the vehicle responds to these inputs by generating the vehicle path, velocity, acceleration, tire forces, and other data as a function of time.

EDVDS includes several extensions to the original Phase 4 program. These extensions, developed by Engineering Dynamics Corporation, include a full 3-D simulation capability, an updated suspension model with jounce and rebound stops, an updated semi-empirical tire model that supports a full 360-degree range of slip angles and a 2-step radial tire stiffness, and the ability of each tire to respond to an arbitrary 3-D terrain.

Vehicle design engineers can use EDVDS to assess how various changes to suspension and tire parameters affect vehicle handling behavior. After setting up a series of simulation experiments, such as step-steer or J-turn maneuvers, alternate ramp traversals or a timed series of brake application pressures, engineers can vary the vehicle design parameters of interest and quickly determine their effect.

Accident investigators can use EDVDS to determine how a driver may have lost vehicular control. By repeated adjustments of the throttle, braking and steering input tables, the researcher will converge on those driver inputs which match accident site evidence. Thus, the user learns how a driver's input may have affected the cause and/or outcome of an accident.

EDVDS employs full 3-D engineering models with up to 23 degrees of freedom for each vehicle. The program supports up to 4 axles per vehicle, solid axle suspension types with inter-tandem load transfer, and single and dual tires. Combination vehicles are connected using fixed and converter dollies with rigid or hinged drawbars. EDVDS also employs a comprehensive drivetrain model with engine performance parameters and multi-gear transmissions and differentials.

Tire vs terrain contact is modeled transparently to the user. At each simulation timestep, the EDVDS tire model uses HVE's *GetSurfaceInfo()* function to query the terrain's physical characteristics (elevation, slope and friction) beneath each tire. The EDVDS tire model then uses this information to determine current tire forces at each tire.

EDVDS has the following user-selectable calculation option:

## Tire Model Method

This radio group selects the method used to compute tire forces. The selection is stored in `calcOptions.calcInt[0]` and assigned to the physics engine's `TireModelMethod` variable. The choices are:

- **Linear** (`LINEAR_TIRE` = 0, the default) — Tire shear forces are computed using the linear tire model, in which lateral and longitudinal forces are derived from the tire's cornering stiffness and longitudinal stiffness.
- **Semi-Empirical** (`TIRE_MODEL` = 1) — Tire shear forces are computed using the EDC-extended semi-empirical tire model. This model supports a full 360-degree range of slip angles and a 2-step radial tire stiffness, and is generally preferred for severe maneuvers involving large slip angles.
- **Table Look-Up** (`TIRE_TABLE_LOOKUP` = 2) — *Not currently available.* This choice is greyed out in the dialog, and the physics engine rejects it (`ERROR_TIRE_MODEL_NOT_SUPPORTED`) if it is ever selected.

## Removed Options

Earlier versions of this help topic listed the terrain surface-search choices **From First Polygon**, **From Previous Polygon** and **By Elevation** as EDVDS calculation options. These are no longer part of the EDVDS Calculation Options dialog. The surface-search method is now selected in the separate Get Surface Information Options dialog (Options menu). Note that EDVDS does not support the By Elevation method; choosing it for an EDVDS event produces an error message when the event is executed.

---
*Source topic: CalcOptEDVDS.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [EDSVS Calculation Options](CalcOptEDSVS.md)  |  [Index](README.md)  |  Next: [EDVSM Calculation Options](CalcOptEDVSM.md) →

<!-- /NAV -->
