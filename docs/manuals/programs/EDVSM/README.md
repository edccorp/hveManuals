# EDVSM — Engineering Dynamics Corporation Vehicle Simulation Model

**Vehicle Simulator** — User's Manual, Version 3

Fifth Edition (January 2006) — *converted to Markdown and updated against the current HVE source code (`Physics/Source/Edvsm/`, `Physics/Include/`, `HVEINV-64/`)*

## How to Use This Manual

This manual is the user's manual for the EDVSM simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual. The HVE User's Manual provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor. For specific model definitions, the user is referred to the HVE User's Manual.

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. Please call — we're glad to help!

When you call, you should have the following information available:

- Your User ID number
- Your System Hardware Profile report (available from EDC)
- HVE Version Information (available from the HVE Help System)
- EDVSM Version Information (available from the EDVSM Program Data report)

## Contents

1. [Chapter 1 — EDVSM Program Description](01-program-description.md)
   - Overview, Model Inputs, Model Outputs, Validation, Basic Procedure
2. [Chapter 2 — EDVSM Program Input](02-program-input.md)
   - Objects Overview; Vehicles (Sprung Mass, Unsprung Mass, Tires, Suspension, Exterior, Steering, Brake and Drivetrain data); Environment (Visual and Physical Data); Event (Position/Velocity, Driver Controls, Wheels, Simulation Controls, Calculation Options, Executing an Event)
3. [Chapter 3 — EDVSM Program Output](03-program-output.md)
   - Alpha-Numeric Reports (Messages, Accident History, Driver Controls, Environment Data, Vehicle Data, Program Data); Graphic Reports; Variable Output Table; Trajectory Simulations; Damage Profile Simulations
4. [Chapter 4 — Calculation Method](04-calculation-method.md)
   - Basic Vehicle Model; Steering System (Stop Torque, Friction Torque, Tire-Ground Torque, Rotational Inertia)
5. [Chapter 5 — EDVSM Tutorial](05-tutorial.md)
   - Curb-tripped rollover validation event and tire blow-out parameter study; viewing and printing all output reports
6. [Chapter 6 — Messages](06-messages.md)
   - Complete EDVSM message catalog, verified against the current message resources
7. [Chapter 7 — References](07-references.md)
8. [Chapter 8 — Index](08-index.md)

See also: [EDVSM Calculation Options reference](../../10-calculation-options/CalcOptEDVSM.md) (code-verified description of the Tire Model Method, GetSurfaceInfo Method, Steer Degree of Freedom, and Vehicle Body vs. Environment Contact options).

## Notes on this Edition

This Markdown edition preserves the substance of the Fifth Edition (January 2006) printed manual and updates it where the current source code differs. Notable updates:

- **Calculation Options:** the Tire Model Method options *Radial Spring* and *Sidewall Impact* are disabled in the current dialog and rejected by the physics (only *Normal* is available); the Steer Degree of Freedom *Append* option is likewise disabled and rejected (Off and Normal remain); *Vehicle Body vs. Environment Contact* (rollover model) is off by default.
- **Messages:** one message was added after the Fifth Edition (a second Integration Error concerning the Velocity Convergence Criterion and Maximum Bisections), and the GetSurfaceInfo() Error text was shortened. See [Chapter 6](06-messages.md).
- Figures from the printed manual are indicated by italic placeholders.

<!-- NAV -->

---

Next: [Chapter 1 — EDVSM Program Description](01-program-description.md) →

<!-- /NAV -->
