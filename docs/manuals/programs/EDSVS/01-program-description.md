# Chapter 1 — EDSVS Program Description

## Overview

**EDSVS** (**E**ngineering **D**ynamics Corporation **S**ingle **V**ehicle **S**imulator) is a simulation analysis of a motor vehicle (4-wheeled automobile or truck having tandem axles and dual tires) to driver inputs (accelerating, braking and steering). It is based on a program called TBST developed at the University of Michigan Transportation Research Institute [14]. EDSVS determines how the vehicle responds to the inputs by generating the path, velocity, acceleration, tire force, and other data as a function of time.

Accident investigators can use EDSVS to determine how a driver may have lost vehicular control. By repeated adjustments of the throttle, braking and steering input tables, the user will converge on those driver inputs which match accident site evidence. EDSVS can also be used to study the handling effects due to changes in vehicle weight distribution, wheelbase, track width, CG height, tire friction, cornering stiffness, and other parameters.

An extremely useful feature of EDSVS is the ability to quickly and accurately review the results generated from different input scenarios. Termed *what if* analysis, changes can be made to an isolated variable or set of variables and the effects are displayed immediately. For example, the sensitivity of the trajectory to various front/rear tire combinations can be studied simply by changing the tire data; the sensitivity to CG location can be studied by moving its position. However, the major purpose of EDSVS can be realized by changing the driver input tables (throttle, braking and steering) until the resulting trajectory matches the actual trajectory produced by the vehicle during a particular maneuver. Thus, the user learns how a driver's inputs may have affected the outcome of an accident.

![Figure 1-1](images/p016-000.png)
*Figure 1-1: EDSVS Event.*

## Model Inputs

EDSVS inputs include one vehicle and an optional driving environment. Event set-up parameters include vehicle initial position and velocity, and various driver control options (steering, braking and throttle).

## Model Outputs

EDSVS output reports include Accident History, Messages, Program Data, Trajectory Simulations, Variable Output and Vehicle Data.

## Validation

The EDSVS simulation model was first validated by direct comparison with results using TBST. These in-house validations included a validation study in the original TBST research document.

The in-use accuracy of the program is dependent upon several factors. Because EDSVS is a 3-degree of freedom analysis, jounce and rebound suspension effects are ignored. Therefore, the program is well suited for the study of vehicle trajectories on low-friction surfaces, such as ice and/or snow. It also serves as an excellent first-order approximation for normally encountered road surfaces, such as dry asphalt and concrete. Good geometrical, inertial, and tire data are essential for accurate results.

> **HVE:** EDSVS has been extended and revalidated for use in the HVE environment to account for 3-D terrain. Vehicle roll and pitch angles are allowed and accounted for within the limits of the small angle assumption (normally 15 degrees). See reference 25 for further details regarding the validation of EDSVS.

## HVE-2D and HVE

EDSVS is compatible with both HVE-2D and HVE. While EDSVS has been extended and revalidated for use in the HVE environment to account for 3-D terrain (described above), EDSVS is essentially a 2-dimensional physics simulation program.

> **HVE:** If you are using EDSVS within the HVE environment, the Human, Vehicle, and Environment Editors will have additional features that are not available in HVE-2D. These features are described in great detail in the HVE User's Manual. While some dialogs do look different between HVE-2D and HVE, the required input for EDSVS is found in both. Where there are differences related to the use of EDSVS, these differences are noted in this manual.

## Basic Procedure

The procedure for using EDSVS is substantially the same as using any simulator in the HVE-2D environment:

1. Use the Vehicle Editor to add one or more vehicles to the case. Optionally, edit any of the default vehicle parameters.
2. Optionally, use the Environment Editor to create a visual and physical environment.
3. Use the Event Editor to set up and execute the EDSVS simulation model by performing the following steps:
   - Choose one vehicle from the list of vehicles created earlier.
   - Choose the EDSVS calculation model.
   - Position the vehicle in the environment, and assign an initial velocity.
   - Assign driver controls (Steering, Braking, Throttle).
4. Execute the simulation event.
5. Modify the initial conditions and driver inputs as required to achieve the desired match between the simulation and actual event.
6. Use the Playback Editor to view the various reports and trajectory simulations. If desired, produce a video output of the simulation.

---

[Contents](README.md) | [Next: Chapter 2 — EDSVS Program Input](02-program-input.md)

<!-- NAV -->

---

← Previous: [EDSVS — Single Vehicle Simulator](README.md)  |  [Index](README.md)  |  Next: [Chapter 2 — EDSVS Program Input](02-program-input.md) →

<!-- /NAV -->
