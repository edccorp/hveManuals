# EDSVS — Single Vehicle Simulator

**Engineering Dynamics Corporation Single Vehicle Simulator**

*Version 7 — Sixth Edition (January 2006), converted to Markdown and updated to match the current HVE software (July 2026 edition).*

EDSVS is a simulation analysis of the response of a motor vehicle (4-wheeled automobile, or truck having tandem axles and dual tires) to driver inputs (accelerating, braking and steering). It is based on the TBST program developed at the University of Michigan Transportation Research Institute. This manual describes the model features and use; input parameters and output reports are described at a high level. It is intended to be used in conjunction with the HVE-2D or HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and Playback Editor.

## EDSVS in HVE 2027

HVE 2027 compiles EDSVS from HVE's own source, so the model, equations and messages in this manual describe what runs. HVE 2027 is a 3-D program like HVE, so the notes marked **HVE:** below apply; the HVE-2D notes do not. What changes is how you reach the program:

- **Choosing it.** Select **EDSVS** as the **Method** in the event's **Event Information** panel (Event editor, F5). EDSVS takes exactly one vehicle, with two or three axles. Run on the HVE tutorial case `EdsvsTutorialEDC.hve`, HVE 2027 reproduces HVE's saved result to within a millimetre (see [Chapter 5](05-tutorial.md)).
- **No calculation options.** EDSVS reads none. The **Method Options…** button in Event Information is greyed for an EDSVS event. The surface-search method is the **Road Surface Search** section of Event Information, and the roll couple distribution is a vehicle value (**Vehicle › Suspension Data**, *Roll Couple Dist*).
- **Simulation controls** (maximum time, integration timestep, output interval, termination velocity, and the integrator's Maximum Bisections and Velocity Convergence) are in the **Simulation** panel, docked beside Event Information.
- **Running.** **Run** on the playback bar under the viewport, or **Output › Run Simulation**. The result plays back in the same viewport; the **Playback** editor (F6) is for playing several events in sequence.
- **Reports.** **Output › HVE Reports** shows the pages EDSVS itself writes (Accident History, Environment Data, Messages, Program Data, Vehicle Data). Time histories are in **Output › Key Results** (the variables chosen with **Output › Variable Selection**) and **Output Graph**.
- **Differences from HVE** are marked with *HVE 2027* notes in the chapters. HVE 2027's default *Roll Couple Dist* for a new vehicle is 0.50, not 0.55; and **Event › Payload** cannot be opened for an EDSVS event, although EDSVS uses a payload (see [Chapter 2](02-program-input.md#payload)).

## How to Use This Manual

EDSVS is compatible with both HVE-2D and HVE. If you are using EDSVS within the HVE environment, the Human, Vehicle and Environment Editors will have additional features that are not available in HVE-2D. These features are described in great detail in the HVE User's Manual. While some dialogs do look different, the required input for EDSVS is found in both. Where there are differences related to the use of EDSVS, these differences are noted in this manual. Information specific to HVE was designated with a grey background in the original manual; in this edition it is marked with **HVE:** prefixed blockquotes.

If you have questions, Engineering Dynamics Corporation provides technical assistance for supported users. When you call, have available: your user ID number (Help System), your System Hardware Profile report, HVE-2D or HVE Version Information (Help System), and EDSVS Version Information (from the EDSVS Program Data report).

## Contents

1. [Chapter 1 — EDSVS Program Description](01-program-description.md) — Overview, model inputs and outputs, validation, HVE-2D and HVE, basic procedure
2. [Chapter 2 — EDSVS Program Input](02-program-input.md) — Vehicles, environment, event set-up, driver controls, simulation controls, calculation options
3. [Chapter 3 — EDSVS Program Output](03-program-output.md) — Alpha-numeric reports, graphic reports, variable output table, trajectory simulations
4. [Chapter 4 — EDSVS Calculation Method](04-calculation-method.md) — Equations of motion, tire forces, antilock model, assumptions
5. [Chapter 5 — EDSVS Tutorial](05-tutorial.md) — A complete run-off-road study, from vehicle creation to printed reports
6. [Chapter 6 — EDSVS Messages](06-messages.md) — Complete list of EDSVS simulation messages
7. [Chapter 7 — Technical References](07-technical-references.md)
8. [Chapter 8 — Index](08-index.md) — Topic-to-chapter guide (replaces the printed page index)

## Related pages

- [EDSVS Calculation Options](../../10-calculation-options/CalcOptEDSVS.md) — current defaults, ranges and the Get Surface Information Options dialog.

## Notes on this edition

This Markdown edition preserves the substance of the Sixth Edition manual and has been checked against the behavior of the current EDSVS simulation program and the current HVE user interface. Where the original manual was stale, the text describes the current software and is marked with *(updated: ...)* notes. Key updates:

- EDSVS does not present or use a Calculation Options dialog; the Roll Couple Distribution used by the simulation is read from the vehicle's **Roll Couple Distribution** suspension value (default 0.55), not from a per-event calculation option.
- The terrain surface-search method is now selected in the separate **Get Surface Information Options** dialog; the **By Elevation** method is not supported.
- The message catalog now contains four termination messages (wheel lift-off, excessive roll/pitch, surface information failure, integration error).

Screenshots from the original manual are not reproduced; italic placeholders give the figure caption for each.

**HVE 2027 edition:** screenshots of HVE's windows have been replaced with captures of HVE 2027 (file names beginning `hvn-`), and every page that describes using the program has been rewritten for HVE 2027's interface. The path diagram of the tutorial is HVE's.

<!-- NAV -->

---

Next: [Chapter 1 — EDSVS Program Description](01-program-description.md) →

<!-- /NAV -->
