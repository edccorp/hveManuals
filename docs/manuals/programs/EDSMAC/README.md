# EDSMAC — Vehicle Collision Simulator

**Engineering Dynamics Corporation Simulation Model of Automobile Collisions**

*Version 4 — Fifth Edition (January 2006), converted to Markdown and updated against the current HVE source code (July 2026 edition).*

EDSMAC is a simulation analysis of single- or two-vehicle crashes, based on the SMAC program developed at Calspan for NHTSA, with extensions by Engineering Dynamics Corporation. This manual describes the model features and use; input parameters and output reports are described at a high level. It is intended to be used in conjunction with the HVE-2D User's Manual, which provides in-depth coverage of the vehicle and environment models, as well as the Event Editor and Playback Editor.

> Original publication: Engineering Dynamics Corporation, 8625 S.W. Cascade Boulevard, Suite 200, Beaverton, Oregon 97008 USA — www.edccorp.com. Copyright Engineering Dynamics Corporation 1982-2006. All rights reserved. HVE, HVE-2D, SIMON, DyMESH, EDSVS, EDVTS, EDCRASH, EDSMAC, EDSMAC4, EDVSM, EDHIS, EDVDS, EDGEN and EDVAP are trademarks of Engineering Dynamics Corporation.

## Contents

1. [Chapter 1 — EDSMAC Program Description](01-program-description.md) — Overview, model inputs and outputs, validation, basic procedure
2. [Chapter 2 — EDSMAC Program Input](02-program-input.md) — Vehicles, environment, event set-up, driver controls, simulation controls, calculation options, barrier collisions
3. [Chapter 3 — EDSMAC Program Output](03-program-output.md) — Alpha-numeric reports, variable output tables, trajectory and damage profile simulations
4. [Chapter 4 — Calculation Method](04-calculation-method.md) — Equations of motion, collision phase, trajectory phase, assumptions
5. [Chapter 5 — EDSMAC Tutorial](05-tutorial.md) — A complete visibility/avoidability study, from vehicle creation to printed reports
6. [Chapter 6 — Messages](06-messages.md) — Complete list of fatal, diagnostic and informative messages
7. [Chapter 7 — Technical References](07-technical-references.md)
8. [Chapter 8 — Index](08-index.md) — Topic-to-chapter guide (replaces the printed page index)

## Related pages

- [EDSMAC Calculation Options (code-verified reference)](../../10-calculation-options/CalcOptEDSMAC.md) — internal variable names, defaults, ranges and the current Get Surface Information Options dialog.

## Notes on this edition

This Markdown edition preserves the substance of the Fifth Edition manual and has been verified against the current physics engine (`Physics/Source/Edsmac/`, notably `SMAINPUT.CPP` and `COLL.CPP`) and the HVE user interface (`HVEINV-64/EdSmacDlg.cpp`, `Language.rsc`). Where the original manual was stale, the text follows the code and is marked with *(updated: ...)* notes. Key updates:

- Calculation option defaults and labels (Vector Spacing default 2.0 deg, "Max Pressure Error" label for ALAMB).
- Corrected AMU/ZETAV variable attribution (AMU = inter-vehicle friction; ZETAV = minimum velocity for friction).
- The restitution model $e = C_0 - C_1\delta + C_2\delta^2$ with current default coefficients.
- Terrain search options are now in the separate Get Surface Information Options dialog; the "By Elevation" method is not supported.

Screenshots from the original manual are not reproduced; italic placeholders give the figure caption for each.

<!-- NAV -->

---

Next: [Chapter 1 — EDSMAC Program Description](01-program-description.md) →

<!-- /NAV -->
