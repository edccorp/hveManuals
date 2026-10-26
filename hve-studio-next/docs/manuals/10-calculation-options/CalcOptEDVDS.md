# EDVDS Calculation Options

EDVDS (Engineering Dynamics Corporation Vehicle Dynamics Simulator) is a simulation of the dynamic response of a vehicle towing up to three trailers. It is based on a program called Phase 4 developed at the University of Michigan Transportation Research Institute. EDVDS simulates the vehicle's response to driver inputs (accelerating, braking and steering). EDVDS determines how the vehicle responds to these inputs by generating the vehicle path, velocity, acceleration, tire forces, and other data as a function of time.

EDVDS includes several extensions to the original Phase 4 program. These extensions, developed by Engineering Dynamics Corporation, include a full 3-D simulation capability, an updated suspension model with jounce and rebound stops, an updated semi-empirical tire model that supports a full 360-degree range of slip angles and a 2-step radial tire stiffness, and the ability of each tire to respond to an arbitrary 3-D terrain.

Vehicle design engineers can use EDVDS to assess how various changes to suspension and tire parameters affect vehicle handling behavior. After setting up a series of simulation experiments, such as step-steer or J-turn maneuvers, alternate ramp traversals or a timed series of brake application pressures, engineers can vary the vehicle design parameters of interest and quickly determine their effect.

Accident investigators can use EDVDS to determine how a driver may have lost vehicular control. By repeated adjustments of the throttle, braking and steering input tables, the researcher will converge on those driver inputs which match accident site evidence. Thus, the user learns how a driver's input may have affected the cause and/or outcome of an accident.

EDVDS employs full 3-D engineering models with up to 23 degrees of freedom for each vehicle. The program supports up to 4 axles per vehicle, solid axle suspension types with inter-tandem load transfer, and single and dual tires. Combination vehicles are connected using fixed and converter dollies with rigid or hinged drawbars. EDVDS also employs a comprehensive drivetrain model with engine performance parameters and multi-gear transmissions and differentials.

Tire vs terrain contact is modeled transparently to the user. At each simulation timestep, the EDVDS tire model queries the terrain's physical characteristics (elevation, slope and friction) beneath each tire. The EDVDS tire model then uses this information to determine current tire forces at each tire.

## Opening the options

EDVDS has no calculation options window in HVE Studio; **Method Options...** in
Event Information is grayed for an EDVDS event. HVE's one EDVDS option, the
tire model method, is fixed:

## Tire Model Method

HVE Studio always runs EDVDS with the **Semi-Empirical** tire model: the
EDC-extended semi-empirical model, which supports a full 360-degree range of
slip angles and a 2-step radial tire stiffness, and is fed from the vehicle's
tire friction and cornering tables.

!!! warning "Not in HVE Studio"
    - **Linear** cannot be selected. (Run with the linear tire model, EDVDS's own
      tutorial case stops early with an excessive tire deflection error.)
    - **Table Look-Up** cannot be selected. EDVDS refuses it at input (stop code
      −5504, tire model not supported), as it does in HVE.

## Other settings EDVDS reads

- The simulation controls, including **Maximum Bisections** and **Velocity
  Convergence** — see [Simulation Controls](../09-events-driver-controls/SimuCtrlDlg.md).
- The road surface search — **Road Surface Search** in
  [Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search).
  *By Elevation* is not offered (EDVDS does not support it).
- The path follower of the **tow unit** only — see
  [Driver Controls Path Follower](../09-events-driver-controls/DriverControls7.md).

!!! note "HVE Studio"
    HVE Studio's EDVDS applies HVE's tandem-axle load equalizer, but relaxes the
    correction over at least 5 ms where HVE applies it in full every step. The
    two are the same at integration timesteps of 5 ms and above; at finer
    timesteps HVE Studio's answer is smoother. This is a deliberate, documented
    difference.

<!-- NAV -->

---

← Previous: [EDSVS Calculation Options](CalcOptEDSVS.md)  |  [Index](README.md)  |  Next: [EDVSM Calculation Options](CalcOptEDVSM.md) →

<!-- /NAV -->
