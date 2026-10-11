# EDVTS Calculation Options

EDVTS (Engineering Dynamics Corporation Vehicle Trailer Simulator) is a simulation analysis of the response of an articulated vehicle (either a passenger car pulling a standard trailer, or a commercial tractor-trailer vehicle) to driver inputs (accelerating, braking and steering). It is based on a program called TBSTT developed at the University of Michigan Transportation Research Institute. EDVTS determines how the vehicle responds to the inputs by generating the path, velocity, acceleration, tire force, and other data as a function of time.

Accident investigators can use EDVTS to determine how a driver may have lost vehicular control. By repeated adjustments of the throttle, braking and steering input tables, the user will converge on those driver inputs which match accident site evidence. EDVTS can also be used to study the handling effects due to changes in vehicle weight distribution, wheelbase, track width, CG height, tire friction, cornering stiffness, hitch or kingpin location and other parameters.

An extremely useful feature of EDVTS is the ability to quickly and accurately review the results generated from different input scenarios. Termed *what if* analysis, changes can be made to an isolated variable or set of variables and the effects are displayed immediately. For example, the sensitivity of the trajectory to various front/rear tire combinations can be studied simply by changing the tire data; the sensitivity to CG location can be studied by moving its position. However, the major purpose of EDVTS can be realized by changing the driver input tables (throttle, braking and steering) until the resulting trajectory matches the actual trajectory produced by the vehicle during a particular maneuver. Thus, the user learns how a driver's inputs may have affected the outcome of an accident.

## Opening the options

EDVTS has no calculation options window in HVE 2027 (as in current HVE, it reads
no calculation-option values from the event). **Method Options...** in Event
Information is greyed for an EDVTS event.

## Roll Couple Distribution

Roll Couple Distribution sets the fraction of the tow vehicle's total lateral load transfer (roll couple) that is reacted by the front axle; the remainder is reacted by the rear axle. It is expressed as a fraction (units %/100) in the range 0.00 to 1.00.

For EDVTS this value is **not** entered through a calculation options window. It is the tow vehicle's suspension setting: in the Vehicle editor open **Vehicle › Suspension Data** and edit the **Roll Couple Dist** row.

Within the physics model, this parameter is the front-axle lateral load transfer coefficient $\gamma_1$, with the rear axle taking $\gamma_2 = 1 - \gamma_1$ for the tow vehicle, which apportion the lateral weight shift used to compute the individual tire normal loads during cornering.

## Other settings EDVTS reads

- The simulation controls, including **Maximum Bisections** and **Velocity
  Convergence** — see [Simulation Controls](../09-events-driver-controls/SimuCtrlDlg.md).
- The road surface search — **Road Surface Search** in
  [Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search).
- The trailer's starting state is its **articulation** relative to the tow
  vehicle (Event Information); EDVTS derives the trailer's position from the
  hitch.

<!-- NAV -->

---

← Previous: [EDVSM Calculation Options](CalcOptEDVSM.md)  |  [Index](README.md)  |  Next: [Calculation Options for EDHIS](CalcOptionsEDHIS.md) →

<!-- /NAV -->
