# EDGEN — General Analysis Tool

**Engineering Dynamics Corporation General Analysis Tool, Version 2**

Third Edition (January 2006) — converted to Markdown and updated against the current HVE source code (July 2026).

EDGEN is a 3-dimensional kinematics spreadsheet for the HVE (Human Vehicle Environment) simulation environment. It moves one human or one vehicle through up to eight user-specified positions and velocities, computing the average accelerations and the position/velocity time histories between them.

This manual is intended to be used in conjunction with the HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor.

> **Note on HVE-2D:** EDGEN is compatible with both HVE and HVE-2D. When using HVE-2D the user is restricted to studying planar motion and the Human Editor is not available. Because these restrictions are not imposed by the physics program, this manual includes all features available in HVE.

## Contents

- [Chapter 1 — Program Description](01-program-description.md)
  - Overview, Model Inputs, Model Outputs, HVE and HVE-2D, Validation, Basic Procedure
- [Chapter 2 — Program Input Parameters](02-program-input.md)
  - Objects Overview, Humans, Vehicles, Environment, Event (Position/Velocity, Simulation Controls, Calculation Options, Executing an Event)
- [Chapter 3 — Program Output Results](03-program-output.md)
  - Alpha-Numeric Reports (Messages, Accident History, Program Data), Variable Output, Trajectory Simulations
- [Chapter 4 — Calculation Method](04-calculation-method.md)
  - Basis for Analysis, Equations of Motion, Generalized Equations, Path Interpolation Options (Linear / 3-D Spline)
- [Chapter 5 — EDGEN Tutorial](05-tutorial.md)
  - School bus / child pedestrian / oncoming vehicle visibility study
- [Chapter 6 — Messages](06-messages.md)
- [Chapter 7 — Technical References](07-references.md)
- [Chapter 8 — Index](08-index.md)

## Related code-verified documentation

- [Calculation Options for EDGEN (dialog reference)](../../10-calculation-options/CalcOptEDGENDlg.md)
- Physics source: `Physics/Source/Edgen/` (`genlinear.cpp`, `genspline.cpp`, `Geninput.cpp`, `Output.cpp`, `gendef.h`)

## Source

Converted from the legacy printed manual (~88 pages). Figures and screenshots from the printed manual are referenced by italic placeholders. Where the printed manual differed from the current source code, the text follows the code and is marked with *(updated: ...)* notes.

<!-- NAV -->

---

Next: [Chapter 1 — Program Description](01-program-description.md) →

<!-- /NAV -->
