# EDVSM Calculation Options

EDVSM (Engineering Dynamics Corporation Vehicle Simulation Model) is a 3-D analysis of the response of a unit vehicle to a driver's inputs (steering, throttle, brakes, gear selection). EDVSM is based on the HVOSM model developed at Calspan. The original HVOSM model was developed in two versions: The Roadside Design version (RD2) was developed for studying vehicle interactions with the roadside environment, while the Vehicle Dynamics version (VD2) was developed for studying vehicle response to driver inputs. EDVSM was derived from the VD2 version of HVOSM, and includes several extensions and refinements provided by Engineering Dynamics Corporation.

EDVSM computes vehicle kinematics (position, velocity and acceleration vs time) from forces defined at the tire-road interface, as well as from aerodynamics. EDVSM is useful for predicting and visualizing a vehicle's response to driver's inputs, as well as for studying the effects of various design parameters on vehicle behavior.

The EDVSM vehicle model is *fully* three-dimensional. It includes six degrees of freedom for the sprung mass. It also includes degrees of freedom for both independent and solid axle suspension types. A wheel spin degree of freedom is also included for each wheel, and a steer degree of freedom exists for the steering system.

EDVSM includes detailed models of braking systems to allow the study of vehicle brake system characteristics on vehicle behavior during severe driving maneuvers, such as that which might occur during accident avoidance. EDVSM also has a detailed drivetrain model that includes an engine, transmission and differential. The drivetrain model may be used for detailed studies of a vehicle's response to throttle inputs and gear selection.

EDVSM has the following user-selectable calculation options:

## Tire Model Method

This radio group selects the method used to model the tire-terrain interaction. The selection is stored in `calcOptions.calcInt[0]`. The choices are:

- **Normal** (0, the default) — Tire forces are computed at the tire-road contact patch using the standard EDVSM point-contact tire model.
- **Radial Spring** (1) — *Not currently available.* Intended for modeling tire traversal of sharp-edged terrain irregularities using radial springs distributed around the tire circumference. This choice is greyed out in the dialog, and the physics engine rejects any value other than Normal (`ERROR_TIRE_MODEL_NOT_SUPPORTED`).
- **Sidewall Impact** (2) — *Not currently available.* Intended for modeling forces produced by contact between the tire sidewall and a curb-like obstacle. This choice is greyed out in the dialog and rejected by the physics engine.

## Steer DOF

This radio group controls the steering system's steer degree of freedom. The selection is stored in `calcOptions.calcInt[2]` and mapped to the HVOSM-heritage curb/steer option flag `indcrb`. The choices are:

- **Off** (0, the default; `indcrb = NO_CURB`) — The steer degree of freedom is not integrated; the front wheel steer angles follow the driver's steer input tables directly.
- **Normal** (1; `indcrb = NO_CURB_W_STEER`) — The steer degree of freedom is active. The front wheel steer angle is computed dynamically from the moments acting about the steer axis (tire forces, gyroscopic moments, steering system stiffness and damping), so the simulated steering response includes steering system compliance effects.
- **Append** (2) — *Not currently available.* This choice is greyed out in the dialog, and the physics engine rejects it (`ERROR_STEER_MODEL_NOT_SUPPORTED`).

## Vehicle Body vs Environment Contact

This checkbox is stored in `calcOptions.calcBoolean[0]` and assigned to the physics engine's `AllowRollover` flag. The default is off (unchecked).

When checked, EDVSM performs body-to-terrain contact calculations using the HVOSM hardpoint model extended by EDC to use the vehicle's 3-D body mesh: when the vehicle's roll or pitch angle exceeds a threshold (5 degrees), each body mesh vertex is tested against the terrain, and contact forces and moments (including friction) are applied to the sprung mass. Vertex deformations are accumulated, allowing a damage profile to be computed and visualized; Damage Profiles output is available in Playback mode only when this option is checked. Enabling this option also removes the wheel camber inclination limit that otherwise prevents rollover, so this option must be checked for rollover simulations.

When unchecked, body-terrain contact forces are not computed, and the simulation is limited to maneuvers in which only the tires contact the terrain.

## Removed Options

Earlier versions of this help topic listed the terrain surface-search choices **From First Polygon**, **From Previous Polygon** and **By Elevation** as EDVSM calculation options. These are no longer part of the EDVSM Calculation Options dialog. The surface-search method is now selected in the separate Get Surface Information Options dialog (Options menu). Note that EDVSM does not support the By Elevation method; choosing it for an EDVSM event produces an error message when the event is executed.

---
*Source topic: CalcOptEDVSM.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [EDVDS Calculation Options](CalcOptEDVDS.md)  |  [Index](README.md)  |  Next: [EDVTS Calculation Options](CalcOptEDVTS.md) →

<!-- /NAV -->
