# EDCRASH — Collision Reconstruction

**Engineering Dynamics Corporation Reconstruction of Accident Speeds on the Highway**

Version 7 — Updated Markdown edition, based on the Sixth Edition (January 2006) printed manual and revised to match the current HVE/EDCRASH release.

EDCRASH is an analysis used to reconstruct single and two vehicle accidents. It determines the conditions of impact, including the impact speeds and delta-V of the vehicles, using information obtained from vehicle and accident site inspections. EDCRASH is compatible with both HVE-2D and HVE.

## EDCRASH in HVE 2027

HVE 2027 runs HVE's own EDCRASH physics source, so the reconstruction model,
its equations and its messages are the ones this manual describes. What
differs is the program around it:

- **Setting up the event.** Choose **EDCRASH** as the **Method** in the
  **Event Information** panel (Event editor, F5). The damage and scene inputs
  are in that panel's **Vehicle Impact Setup** section; the per-wheel lock-ups
  and Rot/Lat Skidding flag are in **Event › Driver Controls** (its Wheel Data
  page); the Calculation Options are under **Method Options...**. See
  [Chapter 2](02-program-input.md).
- **Running and reviewing.** **Run** on the playback bar (or **Output › Run
  Simulation**) executes the reconstruction. Results appear in **Key
  Results**; HVE's own report pages (Accident History, Damage Data, Event
  Data, Messages, Program Data, Vehicle Data) are in **Output › HVE Reports**.
  There is no Playback Editor. See [Chapter 3](03-program-output.md).
- **Opening HVE cases.** **File › Open Case** reads an HVE `.hve` case directly,
  including every EDCRASH input this manual describes.
- **Inputs that reach the result.** Besides Impact and Rest, the Begin
  Braking, Separation, Point on Curve and End of Rotation positions all change
  the reconstruction; an impact sideslip angle read from an HVE case is used;
  and the Separation Velocity Basis, Program Options and curved-path options
  are passed to the engine. Chapters 2 and 4 say which control does what.
- **Not available.** The graphic reports (Damage Profiles, Momentum Diagrams,
  Site Drawing), the Impact Plane / Barrier dialog and the Iterate on Sideslip
  separation-velocity basis (refused by the engine). The EES damage basis is
  shown read-only, because no part of EDCRASH reads it.

## How to Use This Manual

This manual describes the EDCRASH model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and Playback Editor.

## Contents

| Chapter | Description |
|---|---|
| [1 — Program Description](01-program-description.md) | Overview, model inputs/outputs, validation, HVE-2D and HVE, basic procedure |
| [2 — Program Input](02-program-input.md) | Vehicles, environment, event set-up, calculation options, executing an event |
| [3 — Program Output](03-program-output.md) | Alpha-numeric reports (Accident History, Damage Data, Event Data, Messages, Program Data, Vehicle Data) and graphic reports (Damage Profiles, Momentum Diagrams, Site Drawing) |
| [4 — Calculation Method](04-calculation-method.md) | Impact phase (collinear and oblique), impact-to-rest phase, trajectory simulation, assumptions |
| [5 — EDCRASH Tutorial](05-tutorial.md) | Complete worked example: intersection collision between a Ford Escort and a Nissan Sentra |
| [6 — Messages](06-messages.md) | All Fatal, Diagnostic and Informative messages issued by EDCRASH, with recommended actions |
| [7 — Technical References](07-technical-references.md) | Bibliography |

## Related Documentation

- [Calculation Options for EDCRASH](../../10-calculation-options/CalcOptEDCRASHDlg.md) — reference for every control in the EDCRASH Calculation Options dialog (Program Options, Separation Velocity Basis, Consistency Checks, Simulation Convergence Criteria).

## Notes on This Edition

This Markdown edition preserves the substance of the original printed manual. Where the printed manual has become stale relative to the current release, the text has been updated and marked with an italic *(updated: ...)* note. Key updates:

- The Calculation Options dialog now includes a fourth Program Options check box, *Include Angular Momentum Solution* (default off, currently disabled), and a fourth Separation Velocity Basis choice, *Iterate on Sideslip*, which is rejected by the current physics engine.
- Default Consistency Check thresholds (PDOF ±10 deg, Delta-V ±0.10, K.E. ±0.50, Newton's 3rd Law ±1.00) and Simulation Convergence Criteria (5 runs; rest 0.10/0.10, EOR 0.15/0.15, POC 0.15) match the current release.
- Screenshots of HVE's windows have been replaced by captures of HVE 2027 (file names beginning `hvn-`) or removed where HVE 2027 has no equivalent; physics figures are kept.
- The original Chapter 8 (Index) is omitted; use full-text search across the chapter files instead.

<!-- NAV -->

---

Next: [Chapter 1 — EDCRASH Program Description](01-program-description.md) →

<!-- /NAV -->
