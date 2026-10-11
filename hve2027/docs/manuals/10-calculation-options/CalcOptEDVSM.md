# EDVSM Calculation Options

EDVSM (Engineering Dynamics Corporation Vehicle Simulation Model) is a 3-D analysis of the response of a unit vehicle to a driver's inputs (steering, throttle, brakes, gear selection). EDVSM is based on the HVOSM model developed at Calspan. The original HVOSM model was developed in two versions: The Roadside Design version (RD2) was developed for studying vehicle interactions with the roadside environment, while the Vehicle Dynamics version (VD2) was developed for studying vehicle response to driver inputs. EDVSM was derived from the VD2 version of HVOSM, and includes several extensions and refinements provided by Engineering Dynamics Corporation.

EDVSM computes vehicle kinematics (position, velocity and acceleration vs time) from forces defined at the tire-road interface, as well as from aerodynamics. EDVSM is useful for predicting and visualizing a vehicle's response to driver's inputs, as well as for studying the effects of various design parameters on vehicle behavior.

The EDVSM vehicle model is *fully* three-dimensional. It includes six degrees of freedom for the sprung mass. It also includes degrees of freedom for both independent and solid axle suspension types. A wheel spin degree of freedom is also included for each wheel, and a steer degree of freedom exists for the steering system.

EDVSM includes detailed models of braking systems to allow the study of vehicle brake system characteristics on vehicle behavior during severe driving maneuvers, such as that which might occur during accident avoidance. EDVSM also has a detailed drivetrain model that includes an engine, transmission and differential. The drivetrain model may be used for detailed studies of a vehicle's response to throttle inputs and gear selection.

## Opening the options

In Event Information, with an EDVSM event active, press **Method Options...**
under Calculation Method. The **EDVSM Options** window has two groups.

## Vehicle Body vs. Environment Contact

**Vehicle body vs. environment contact** — default off (unchecked), HVE's own default.

When checked, EDVSM performs body-to-terrain contact calculations using the HVOSM hard-point model: when the vehicle's roll or pitch angle exceeds a threshold, the body is tested against the terrain and contact forces and moments (including friction) are applied to the sprung mass. This is what lets the body strike the ground, so this option must be checked for rollover simulations. It also holds a tire's deflection at its secondary (bottoming) deflection instead of ending the run.

When unchecked, no body contact is computed, the simulation is limited to maneuvers in which only the tires contact the terrain, and a wheel driven past 1.2 times its maximum deflection ends the run with an *excessive tire deflection* error.

## Steering Degree of Freedom

- **Off - prescribed steer table only** (default) — The steer degree of freedom is not integrated; the front wheel steer angles follow the driver's steer table directly.
- **On - steer is a degree of freedom** — HVE's *Normal*. The front wheel steer angle is computed dynamically from the moments acting about the steer axis (tire forces, gyroscopic moments, steering system stiffness and damping), so the simulated steering response includes steering system compliance effects.

!!! warning "Not in HVE 2027"
    - **Append** is not offered: EDVSM refuses it (steer model not supported),
      as it does in HVE.
    - **Tire Model Method** is not offered: EDVSM is always run with the
      **Normal** point-contact tire model. *Radial Spring* and *Sidewall Impact*
      are refused by the engine (tire model not supported), as in HVE.

## Other settings EDVSM reads

- The simulation controls — see [Simulation Controls](../09-events-driver-controls/SimuCtrlDlg.md).
  EDVSM uses its own integrator, so the Integrator Convergence group is not
  shown.
- The road surface search — **Road Surface Search** in
  [Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search).
  *By Elevation* is not offered (EDVSM does not support it).
- The path follower — see
  [Driver Controls Path Follower](../09-events-driver-controls/DriverControls7.md).

<!-- NAV -->

---

← Previous: [EDVDS Calculation Options](CalcOptEDVDS.md)  |  [Index](README.md)  |  Next: [EDVTS Calculation Options](CalcOptEDVTS.md) →

<!-- /NAV -->
