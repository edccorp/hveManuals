# SIMON — Simulation Model Non-Linear

**Engineering Dynamics Corporation**
**SIMON (SIMulation mOdel Non-linear), Version 2**

Updated Markdown edition, converted from the Fifth Edition printed manual (January 2006) and verified against the current HVE source code (SIMON physics engine in `Physics/Source/Simon/`, the DyMESH collision code in `Physics/Include/DYMESH.H` and `Physics/Source/LibHve/Dymesh.cpp`, and the HVE user-interface dialogs in `HVEINV-64/`). Passages that differ from the printed edition because the software has changed are marked with italic *(updated: ...)* notes. Figures from the printed manual are referenced by placeholder.

## How to Use This Manual

This manual is the user's manual for the SIMON simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual. The HVE User's Manual provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor. For specific model definitions, the user is referred to the HVE User's Manual.

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. When you call, you should have the following information available:

- Your User ID number
- Your System Hardware Profile report (available from EDC)
- HVE Version Information (available from the HVE Help System)
- SIMON Version Information (available from the SIMON Program Data report)

## Contents

1. **[Chapter 1 — SIMON Program Description](01-program-description.md)**
   Overview; General Features and Capabilities; Model Inputs; Model Outputs; Validation; Basic Procedure
2. **[Chapter 2 — SIMON Program Input](02-program-input.md)**
   Objects Overview; Humans; Vehicles (Sprung Mass, Unsprung Mass, Exterior, Steering/Brake/Drivetrain Data); Environment; Event (Set-up, Position/Velocity, Driver Controls, Vehicle Mesh, Payload, Wheels, Accelerometers); Event Calculation Options *(incl. Hydroplaning Model, Connection Model, Solid Axle Inertia, Accident History Basis, Include Free Space)*; DyMESH Options; Simulation Controls; Executing an Event
3. **[Chapter 3 — SIMON Program Output](03-program-output.md)**
   Overview; Alpha-Numeric Reports (Accident History, Damage Data, Driver Data, Environment Data, Event Data, Human Data, Messages, Program Data, Vehicle Data); Graphic Reports; Variable Output Table; Trajectory Simulations; Damage Profiles
4. **[Chapter 4 — Calculation Method](04-calculation-method.md)**
   Basis for Analysis; Equations of Motion (Sprung Mass, Unsprung Mass, Wheel Spin); Steering System; Payloads; Human Occupants; Driver Controls; Wheel Torque; Wheel Position; Wheel Orientation; Tire Contact Patch Velocity; Tire-Road Contact Patch; Tire Radial Deflection and Force; Tire Model; Suspension Force; Inter-Vehicle Connection Model; Dollys; Aerodynamics Model; Sprung Mass Impact Model (DyMESH); Software Implementation
5. **[Chapter 5 — SIMON Tutorial](05-tutorial.md)**
   ISO 3888 lane-change maneuver with and without ABS: creating the vehicle and environment, setting up and executing the events, and viewing/printing all output reports
6. **[Chapter 6 — Messages](06-messages.md)**
   Complete catalog of SIMON run-time messages (fatal, diagnostic and informative), verified against `Physics/Source/Simon/SIMON.rsc`
7. **[Chapter 7 — Technical References](07-technical-references.md)**
   Published references for the SIMON, DyMESH, tire, brake and driver models
8. **[Chapter 8 — Index](08-index.md)**
   Topic index adapted for this Markdown edition

## Notable Differences from the Fifth Edition (2006)

- **Calculation Options** have grown from three options (Tire Model Method, Steer DOF, Collision Acceleration Threshold) to include: three semi-empirical tire model versions, an AutoStart Steer DOF mode, a Hydroplaning Model (NASA / NASA-TTI / Gallaway), a Connection Model selector, a Connection Failure Start Time, a Solid Axle Inertia selector, an Accident History Basis (Impact Force / Acceleration) selector, and an Include Free Space damage-report option (see Chapter 2).
- **DyMESH Options** are now configured in a dedicated dialog: Use DyMESH, Include Environment, Force to x-y Plane, Tow Vehicle / Trailer Contact, DyMESH Version 3/4, vehicle and environment start times, contact search (Automatic / Set Box Size) and mesh smoothing model (see Chapter 2).
- **DyMESH wheel contact and damage**: wheels may carry collision meshes; collision forces beyond user-set thresholds displace and reorient wheels, and the displacement is now capped by the actual wheel-mesh contact motion each timestep (see Chapter 4, Sprung Mass Impact Model).
- **Message catalog** extended with collision/damage-related messages Msg24–Msg36 and a roll/pitch limit message (see Chapter 6).

<!-- NAV -->

---

Next: [Chapter 1 — SIMON Program Description](01-program-description.md) →

<!-- /NAV -->
