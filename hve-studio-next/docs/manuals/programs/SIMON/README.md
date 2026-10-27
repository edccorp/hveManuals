# SIMON — Simulation Model Non-Linear

**Engineering Dynamics Corporation**
**SIMON (SIMulation mOdel Non-linear), Version 2**

Updated Markdown edition, converted from the Fifth Edition printed manual (January 2006) and brought up to date with the current version of HVE, covering the SIMON physics engine, the DyMESH collision model and the HVE user-interface dialogs. Passages that differ from the printed edition because the software has changed are marked with italic *(updated: ...)* notes. Figures from the printed manual are referenced by placeholder.

## SIMON in HVE Studio

HVE Studio compiles HVE's own SIMON source, so the vehicle dynamics, tire, suspension, brake, driver and DyMESH collision models described in this manual are HVE's. What is different is the program around them: the user interface is new, and a small number of deliberate changes and extensions are marked where they apply.

**Selecting SIMON.** In the Event editor (**Event (F5)** tab), open **Event › Event Information...** (the *Event Information* panel). Under **Calculation Method**, choose **SIMON** in the **Method** list. The **Method Options...** button below it opens the *SIMON Options* dialog (HVE's SIMON Calculation Options). Run the event with **Run** on the playback bar under the viewport, or **Output › Run Simulation...**. See [Chapter 2](02-program-input.md#event).

**What is the same.** The equations of motion, the tire model versions, the HVE Brake Designer and ABS model, the HVE Driver Model, tire blow-out, wheel damage, the inter-vehicle connection model, aerodynamics, hydroplaning, the TCS/YSC stability systems, DyMESH, and the engine's own report pages and messages. On EDC's own SIMON cases, opened directly from their `.hve` files, HVE Studio reproduces HVE's saved trajectories closely: the tutorial and the UV-1, UV-2, UV-4, AV-1 and AV-2 validation runs end within 0.05 m of HVE's saved positions. (The curb-tripped rollover, UV-3, is a chaotic event and differs by about 0.9 m.)

**What differs** (each is marked in the chapter where it applies):

- **Up to four axles per vehicle** (HVE: three), for a tag axle — [Chapter 2, Vehicles](02-program-input.md#vehicles).
- **Steer degree of freedom per axle**, so a castoring axle can steer itself while the front follows the driver — [Chapter 2, Steering System Data](02-program-input.md#steering-system-data).
- **A differential model**: HVE records Open / Limited Slip / Locked but solves every differential as open; HVE Studio biases torque for Limited Slip and Locked — [Chapter 2, Drivetrain Data](02-program-input.md#drivetrain-data).
- **The path follower stops per vehicle at an impact** (HVE stops every vehicle's driver model at the first collision anywhere), and it can optionally keep following through an impact — [Chapter 2, Driver Controls](02-program-input.md#driver-controls).
- **Antilock can be switched per event** without editing the vehicle — [Chapter 2, Vehicle Wheels](02-program-input.md#vehicle-wheels).
- **Options HVE lists but SIMON refuses** (ABS Algorithms 3, 5 and 6, DyMESH's "search all vertices") are offered and marked -- the Blythe-Day hydroplaning model is not offered at all, and an imported case stating it is told -- rather than silently replaced — [Chapter 2, Event Calculation Options](02-program-input.md#event-calculation-options).
- **Options that reach no engine** (integration method, several DyMESH restoration options, *Include Free Space*) are marked or absent — [Chapter 2](02-program-input.md#dymesh-options).
- **Lean command** for a single-track vehicle (motorcycle), read while it rides the single-track model — [Chapter 2, Driver Controls](02-program-input.md#driver-controls).
- **Output** is reached from the **Output** menu and the viewport instead of the Playback Editor's report windows — [Chapter 3](03-program-output.md).

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
   Complete catalog of SIMON run-time messages (fatal, diagnostic and informative)
7. **[Chapter 7 — Technical References](07-technical-references.md)**
   Published references for the SIMON, DyMESH, tire, brake and driver models
8. **[Chapter 8 — Index](08-index.md)**
   Topic index adapted for this Markdown edition
9. **[Electronic Stability Systems (TCS and YSC)](09-electronic-stability-systems.md)**
   Supplementary reference for the Traction Control and Yaw Stability Control models: sensor models, control laws, user parameters, outputs, and limitations

## Notable Differences from the Fifth Edition (2006)

- **Calculation Options** have grown from three options (Tire Model Method, Steer DOF, Collision Acceleration Threshold) to include: three semi-empirical tire model versions, an AutoStart Steer DOF mode, a Hydroplaning Model (NASA / NASA-TTI / Gallaway), a Connection Model selector, a Connection Failure Start Time, a Solid Axle Inertia selector, an Accident History Basis (Impact Force / Acceleration) selector, and an Include Free Space damage-report option (see Chapter 2).
- **DyMESH Options** are now configured in a dedicated dialog: Use DyMESH, Include Environment, Force to x-y Plane, Tow Vehicle / Trailer Contact, DyMESH Version 3/4, vehicle and environment start times, contact search (Automatic / Set Box Size) and mesh smoothing model (see Chapter 2).
- **DyMESH wheel contact and damage**: wheels may carry collision meshes; collision forces beyond user-set thresholds displace and reorient wheels, and the displacement is now capped by the actual wheel-mesh contact motion each timestep (see Chapter 4, Sprung Mass Impact Model).
- **Message catalog** extended with collision/damage-related messages and a roll/pitch limit message (see Chapter 6).

<!-- NAV -->

---

Next: [Chapter 1 — SIMON Program Description](01-program-description.md) →

<!-- /NAV -->
