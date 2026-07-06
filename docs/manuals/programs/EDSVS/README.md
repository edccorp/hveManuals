# EDSVS — Single Vehicle Simulator

**Engineering Dynamics Corporation Single Vehicle Simulator**

*Version 7 — Sixth Edition (January 2006), converted to Markdown and updated against the current HVE source code (July 2026 edition).*

EDSVS is a simulation analysis of the response of a motor vehicle (4-wheeled automobile, or truck having tandem axles and dual tires) to driver inputs (accelerating, braking and steering). It is based on the TBST program developed at the University of Michigan Transportation Research Institute. This manual describes the model features and use; input parameters and output reports are described at a high level. It is intended to be used in conjunction with the HVE-2D or HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and Playback Editor.

> Original publication: Engineering Dynamics Corporation, 8625 S.W. Cascade Boulevard, Suite 200, Beaverton, Oregon 97008 USA — www.edccorp.com. Copyright Engineering Dynamics Corporation 1982-2006. All rights reserved. HVE, HVE-2D, SIMON, DyMESH, EDSVS, EDVTS, EDCRASH, EDSMAC, EDSMAC4, EDVSM, EDHIS, EDVDS, EDGEN and EDVAP are trademarks of Engineering Dynamics Corporation. Windows and NT are trademarks of Microsoft Corporation.

## How to Use This Manual

EDSVS is compatible with both HVE-2D and HVE. If you are using EDSVS within the HVE environment, the Human, Vehicle and Environment Editors will have additional features that are not available in HVE-2D. These features are described in great detail in the HVE User's Manual. While some dialogs do look different, the required input for EDSVS is found in both. Where there are differences related to the use of EDSVS, these differences are noted in this manual. Information specific to HVE was designated with a grey background in the original manual; in this edition it is marked with **HVE:** prefixed blockquotes.

If you have questions, Engineering Dynamics Corporation provides technical assistance for supported users. When you call, have available: your user ID number (Help System), your System Hardware Profile report, HVE-2D or HVE Version Information (Help System), and EDSVS Version Information (from the EDSVS Program Data report).

## Contents

1. [Chapter 1 — EDSVS Program Description](01-program-description.md) — Overview, model inputs and outputs, validation, HVE-2D and HVE, basic procedure
2. [Chapter 2 — EDSVS Program Input](02-program-input.md) — Vehicles, environment, event set-up, driver controls, simulation controls, calculation options
3. [Chapter 3 — EDSVS Program Output](03-program-output.md) — Alpha-numeric reports, graphic reports, variable output table, trajectory simulations
4. [Chapter 4 — EDSVS Calculation Method](04-calculation-method.md) — Equations of motion, tire forces, antilock model, assumptions
5. [Chapter 5 — EDSVS Tutorial](05-tutorial.md) — A complete run-off-road study, from vehicle creation to printed reports
6. [Chapter 6 — EDSVS Messages](06-messages.md) — Complete list of EDSVS simulation messages (verified against the current message catalog)
7. [Chapter 7 — Technical References](07-technical-references.md)
8. [Chapter 8 — Index](08-index.md) — Topic-to-chapter guide (replaces the printed page index)

## Related pages

- [EDSVS Calculation Options (code-verified reference)](../../10-calculation-options/CalcOptEDSVS.md) — internal variable names, defaults, ranges and the current Get Surface Information Options dialog.

## Notes on this edition

This Markdown edition preserves the substance of the Sixth Edition manual and has been verified against the current physics engine (`Physics/Source/Edsvs/`, notably `Svsinput.cpp`, `Svsmain.cpp`, `Fct.cpp` and `EDSVS.rsc`) and the HVE user interface (`HVEINV-64`). Where the original manual was stale, the text follows the code and is marked with *(updated: ...)* notes. Key updates:

- The EDSVS engine does not present or use a Calculation Options dialog (`CalcOptionsDlgIsUsed = FALSE` in `Svsinput.cpp`); the Roll Couple Distribution used by the simulation is read from the vehicle's suspension data (`Suspension.RollCoupleDist`, default 0.55), not from `calcFloat[0]`.
- Terrain surface-search (GetSurfaceInfo) selection moved to the separate Get Surface Information Options dialog; the By Elevation method is not supported.
- The message catalog was verified against `Physics/Source/Edsvs/EDSVS.rsc`; the current catalog contains four termination messages (wheel lift-off, excessive roll/pitch, GetSurfaceInfo failure, integration error).

Screenshots from the original manual are not reproduced; italic placeholders give the figure caption for each.

<!-- NAV -->

---

Next: [Chapter 1 — EDSVS Program Description](01-program-description.md) →

<!-- /NAV -->
