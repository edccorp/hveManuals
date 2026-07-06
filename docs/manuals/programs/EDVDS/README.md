# EDVDS — Vehicle Dynamics Simulator

**EDVDS** — Engineering Dynamics Corporation Vehicle Dynamics Simulator, Version 2

*User's Manual, Fourth Edition (January 2006), converted to Markdown and updated against the current HVE source code.*

Engineering Dynamics Corporation
8625 S.W. Cascade Boulevard, Suite 200
Beaverton, Oregon 97008 USA
phone 503.644.4500 / fax 503.526.0905
e-mail info@edccorp.com / http://www.edccorp.com

Copyright © Engineering Dynamics Corporation 1982-2006. All rights reserved.

> HVE, SIMON, DyMESH, EDSVS, EDVTS, EDCRASH, EDSMAC, EDSMAC4, EDVSM, EDHIS, EDVDS, EDGEN, HVE-2D and EDVAP are trademarks of Engineering Dynamics Corporation. Windows and NT are trademarks of Microsoft Corporation.

> *(updated: this edition has been verified against the current EDVDS source (`Physics/Source/Edvds/`, including `Vdsinput2.cpp`) and the current HVE user interface resources. Notable updates: the Tire Model Method calculation option is Linear (default) or Semi-Empirical — the Table Look-Up option is disabled in the dialog and rejected by the physics program; the terrain (GetSurfaceInfo) search options have moved to the separate Get Surface Information Options dialog, where the By Elevation method is unsupported; and the message catalog has grown from 7 to 12 messages. See the individual chapters for details, and the [EDVDS Calculation Options reference](../../10-calculation-options/CalcOptEDVDS.md) for the current dialog.)*

## How to Use This Manual

This manual is the user's manual for the EDVDS simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual. The HVE User's Manual provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor. For specific model definitions, the user is referred to the HVE Operations Manual.

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. Please call — we're glad to help!

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
  - Complete catalog of EDVDS run-time messages, verified against the current source
- [Chapter 7 — References](07-references.md)
  - Bibliography

> *(updated: the printed manual's Chapter 8, a page-number index, is superseded by full-text search of these Markdown files and is not reproduced.)*

<!-- NAV -->

---

Next: [Chapter 1 — EDVDS Program Description](01-program-description.md) →

<!-- /NAV -->
