# EDCRASH — Collision Reconstruction

**Engineering Dynamics Corporation Reconstruction of Accident Speeds on the Highway**

Version 7 — Updated Markdown edition, based on the Sixth Edition (January 2006) printed manual and verified against the current HVE/EDCRASH source code.

EDCRASH is an analysis used to reconstruct single and two vehicle accidents. It determines the conditions of impact, including the impact speeds and delta-V of the vehicles, using information obtained from vehicle and accident site inspections. EDCRASH is compatible with both HVE-2D and HVE.

## How to Use This Manual

This manual describes the EDCRASH model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and Playback Editor.

## Contents

| Chapter | File | Description |
|---|---|---|
| 1 — Program Description | [01-program-description.md](01-program-description.md) | Overview, model inputs/outputs, validation, HVE-2D and HVE, basic procedure |
| 2 — Program Input | [02-program-input.md](02-program-input.md) | Vehicles, environment, event set-up, calculation options, executing an event |
| 3 — Program Output | [03-program-output.md](03-program-output.md) | Alpha-numeric reports (Accident History, Damage Data, Event Data, Messages, Program Data, Vehicle Data) and graphic reports (Damage Profiles, Momentum Diagrams, Site Drawing) |
| 4 — Calculation Method | [04-calculation-method.md](04-calculation-method.md) | Impact phase (collinear and oblique), impact-to-rest phase, trajectory simulation, assumptions |
| 5 — EDCRASH Tutorial | [05-tutorial.md](05-tutorial.md) | Complete worked example: intersection collision between a Ford Escort and a Nissan Sentra |
| 6 — Messages | [06-messages.md](06-messages.md) | All Fatal, Diagnostic and Informative messages issued by EDCRASH, with recommended actions |
| 7 — Technical References | [07-technical-references.md](07-technical-references.md) | Bibliography |

## Related Documentation

- [Calculation Options for EDCRASH](../../10-calculation-options/CalcOptEDCRASHDlg.md) — code-verified reference for every control in the EDCRASH Calculation Options dialog (Program Options, Separation Velocity Basis, Consistency Checks, Simulation Convergence Criteria).

## Notes on This Edition

This Markdown edition preserves the substance of the original printed manual. Where the printed manual has become stale relative to the current source code (`Physics/Source/Edcrash/`, `HVEINV-64/`), the text has been updated and marked with an italic *(updated: ...)* note. Key updates:

- The Calculation Options dialog now includes a fourth Program Options check box, *Include Angular Momentum Solution* (default off, currently disabled), and a fourth Separation Velocity Basis choice, *Iterate on Sideslip*, which is rejected by the current physics engine.
- Default Consistency Check thresholds (PDOF ±10 deg, Delta-V ±0.10, K.E. ±0.50, Newton's 3rd Law ±1.00) and Simulation Convergence Criteria (5 runs; rest 0.10/0.10, EOR 0.15/0.15, POC 0.15) are confirmed against the current code.
- Figures and report screenshots from the original are referenced by placeholder.
- The original Chapter 8 (Index) is omitted; use full-text search across the chapter files instead.

<!-- NAV -->

---

Next: [Chapter 1 — EDCRASH Program Description](01-program-description.md) →

<!-- /NAV -->
