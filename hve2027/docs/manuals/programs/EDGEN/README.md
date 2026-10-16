# EDGEN — General Analysis Tool

**Engineering Dynamics Corporation General Analysis Tool, Version 2**

Third Edition (January 2006) — converted to Markdown and updated to match the current HVE release (July 2026).

EDGEN is a 3-dimensional kinematics spreadsheet for the HVE (Human Vehicle Environment) simulation environment. It moves one human or one vehicle through up to eight user-specified positions and velocities, computing the average accelerations and the position/velocity time histories between them.

This manual is intended to be used in conjunction with the HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor.

> **Note on HVE-2D:** EDGEN is compatible with both HVE and HVE-2D. When using HVE-2D the user is restricted to studying planar motion and the Human Editor is not available. Because these restrictions are not imposed by the physics program, this manual includes all features available in HVE.

## EDGEN in HVE 2027

HVE 2027 runs HVE's own EDGEN physics source, so the kinematic model and its
messages are the ones this manual describes. The program around it differs:

- **Setting up a vehicle event.** Choose **EDGEN** as the **Method** in the
  **Event Information** panel (Event editor, F5) and add one vehicle. Its
  first path position is its initial position and speed (the panel's
  **Vehicle Initial Conditions (EDGEN)** section, or **Event › Position /
  Velocity**); the remaining positions are up to seven waypoints in **Event ›
  Path Follower**, **Path** tab. See [Chapter 2](02-program-input.md).
- **A human subject.** An EDGEN event that selects one human and no vehicle
  moves that pedestrian along its path, as HVE's tutorial does with the
  child. The human's path is entered under the human in the Event
  Information panel's **Humans in Event** section, and is read from an HVE
  case.
- **Path Model.** Linear or 3-D Spline Interpolation, under **Method
  Options...**, is passed to the engine.
- **Running and reviewing.** **Run** on the playback bar executes the event
  and the viewport plays it back. Results are in **Key Results** and **Output ›
  Output Graph**; HVE's own report pages
  (Accident History, Messages, Program Data) are in **Output › HVE
  Reports**. Several events are combined in the **Playback** editor (F6),
  **Playback › Playback Sequence...**. See [Chapter 3](03-program-output.md).
- **Opening HVE cases.** **File › Open Case** reads HVE's `.hve` files,
  including EDGEN events for a vehicle or a human.
- **Validation status.** On HVE's EDGEN tutorial case every event reproduces
  the track HVE saved in the case; the child's 15-segment track to within
  0.05 mm.

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

## Related documentation

- [Calculation Options for EDGEN (dialog reference)](../../10-calculation-options/CalcOptEDGENDlg.md)

## Source

Converted from the legacy printed manual (~88 pages). Screenshots of HVE's windows have been replaced by captures of HVE 2027 (file names beginning `hvn-`) or removed where HVE 2027 has no equivalent. Where the printed manual differed from the current release, the text follows the current program behaviour and is marked with *(updated: ...)* notes.

<!-- NAV -->

---

Next: [Chapter 1 — Program Description](01-program-description.md) →

<!-- /NAV -->
