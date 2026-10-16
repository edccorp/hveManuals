# EDVDS — Vehicle Dynamics Simulator

**EDVDS** — Engineering Dynamics Corporation Vehicle Dynamics Simulator, Version 2

*User's Manual, Fourth Edition (January 2006), converted to Markdown and updated to match the current HVE software.*

> *(updated: this edition describes the current EDVDS program. Notable updates: the **Table Look-Up** tire model is not supported by the physics program; the **By Elevation** surface search is unsupported; and the message catalog has grown from 7 to 12 messages. See the individual chapters for details.)*

## EDVDS in HVE 2027

HVE 2027 compiles HVE's own EDVDS source, so the model described in this manual — the equations of motion, the tire, suspension, brake and connection models, and the messages — is the model HVE 2027 runs. On EDC's own tutorial case (`EdvdsTutorialEDC.hve`), HVE 2027's run follows the trajectory HVE saved in that file to within about 2 cm. What differs is the user interface, and a short list of physics and set-up details:

- **Selecting EDVDS.** In the **Event (F5)** editor, choose **EDVDS** in **Event Information › Calculation Method**. The vehicles are listed in **Vehicles in Event** as slots V1, V2, …; the slot order is the order of the vehicle train (tow vehicle first).
- **Up to four vehicles.** HVE 2027 accepts at most four vehicles in an EDVDS event (tractor, semitrailer, dolly, semitrailer). HVE's six-object triple cannot be set up.
- **Tire model.** HVE 2027 always runs the **Semi-Empirical** tire model. There is no Tire Model Method option; Table Look-Up is refused by the engine itself.
- **Tandem equalizer.** The 4-spring tandem suspension's load-equalizer is a documented HVE 2027 change; see [Chapter 4](04-calculation-method.md#tandem-axles).
- **Payload.** **Event › Payload** is not available for EDVDS events in this version; a payload stored in an imported HVE case is used.
- **Connections.** Edited in the Vehicle editor (**Vehicles** panel › **Components** › **Connections…**). Mating connections must be at the same height above ground; HVE 2027 checks this before running and names the vehicles.
- **Output.** A solved event plays back in the Event editor's own viewport (the **Playback** editor, F6, plays several events in sequence), and **Output › HVE Reports** shows the report pages EDVDS itself builds.

See also [Differences from HVE](../../getting-started/05-differences-from-hve.md).

## How to Use This Manual

This manual is the user's manual for the EDVDS simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual. The HVE User's Manual provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor. For specific model definitions, the user is referred to the HVE Operations Manual.

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. Please call — we're glad to help!

!!! note "HVE 2027"
    EDC supports HVE and its physics programs. HVE 2027 is a separate program built from HVE's physics source; EDC does not support it, and the version and hardware-profile items below refer to HVE.

When you call, you should have the following information available:

- Your User ID number (available from the HVE Help System)
- Your System Hardware Profile Report (available from EDC)
- HVE Version Information (available from the HVE Help System)
- EDVDS Version Information (available from the EDVDS Program Data report)

## Contents

- [Chapter 1 — EDVDS Program Description](01-program-description.md)
  - Overview, Model Inputs, Model Outputs, Validation, Basic Procedure
- [Chapter 2 — EDVDS Program Input](02-program-input.md)
  - Objects Overview; Vehicles (sprung mass, unsprung mass, tires, suspensions, steering, brakes, drivetrain); Environment; Event set-up; Simulation Controls; Calculation Options
- [Chapter 3 — EDVDS Program Output](03-program-output.md)
  - Alpha-numeric Reports (Messages, Accident History, Driver Controls, Environment Data, Program Data, Vehicle Data); Graphic Reports; Variable Output; Trajectory Simulations
- [Chapter 4 — Calculation Method](04-calculation-method.md)
  - Basis for Analysis; Equations of Motion; External Forces (tire, connection and suspension forces); Brake System; Steering System; Dollys; Assumptions
- [Chapter 5 — EDVDS Tutorial](05-tutorial.md)
  - A complete worked example: highway doubles losing control on a downhill curve (creating the vehicles, environment and event; executing; viewing and printing results)
- [Chapter 6 — Messages](06-messages.md)
  - Complete catalog of EDVDS run-time messages for the current version
- [Chapter 7 — References](07-references.md)
  - Bibliography

> *(updated: the printed manual's Chapter 8, a page-number index, is superseded by full-text search of these Markdown files and is not reproduced.)*

<!-- NAV -->

---

Next: [Chapter 1 — EDVDS Program Description](01-program-description.md) →

<!-- /NAV -->
