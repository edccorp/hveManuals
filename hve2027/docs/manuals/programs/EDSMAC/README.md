# EDSMAC — Vehicle Collision Simulator

**Engineering Dynamics Corporation Simulation Model of Automobile Collisions**

*Version 4 — Fifth Edition (January 2006), converted to Markdown and updated to match the current HVE release (July 2026 edition).*

EDSMAC is a simulation analysis of single- or two-vehicle crashes, based on the SMAC program developed at Calspan for NHTSA, with extensions by Engineering Dynamics Corporation. This manual describes the model features and use; input parameters and output reports are described at a high level. It is intended to be used in conjunction with the HVE-2D User's Manual, which provides in-depth coverage of the vehicle and environment models, as well as the Event Editor and Playback Editor.

## EDSMAC in HVE 2027

HVE 2027 compiles HVE's own EDSMAC source, so the physics described in this manual — the linear-crush collision model, the tire model and the equations of motion — is EDSMAC's. What is different is the program around it. EDSMAC was an HVE-2D program; in HVE 2027 it runs in the same 3-D editors as every other method:

- **Choosing EDSMAC.** In the **Event (F5)** editor, pick **EDSMAC** from the **Method** list in **Event Information › Calculation Method**. HVE 2027 checks EDSMAC's own limits there: one or two vehicles, each with exactly two axles.
- **Calculation options** are in the **EDSMAC Options** window (**Method Options...** under the Method list). EDSMAC shares this window with EDSMAC4, and only some of its settings reach EDSMAC; see [Chapter 2 — Calculation Options](02-program-input.md#calculation-options).
- **Running and playback.** Press **Run** on the playback bar under the viewport (or **Output › Run Simulation**, Ctrl+R). The solved event plays back in the same viewport; there is no separate Playback Editor.
- **Reports.** EDSMAC's own report pages (Accident History, Damage Data, Messages, Program Data, References, Vehicle Data) are in **Output › HVE Reports**; time histories are in **Output › Key Results**, **Output › Output Graph** and **Output › Timestep Data Table**.

Where HVE 2027 behaves differently from HVE, the page says so in a box marked **HVE 2027**. Two things to know before you start:

- **Use % of Friction for brake and throttle tables (or Wheel Force for brakes).** EDSMAC has no pedal input; HVE 2027 runs a **Pedal (AT_DRIVER)** table as % of Friction and the run status says so ([Chapter 2 — Driver Controls](02-program-input.md#driver-controls)).
- **Kv** is shown in lbf/in² (N/m² in metric units), the unit EDSMAC reads ([Chapter 2 — Exterior](02-program-input.md#exterior)).

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

- [EDSMAC Calculation Options](../../10-calculation-options/CalcOptEDSMAC.md) — dialog reference giving defaults, ranges and the current Get Surface Information Options dialog.

## Notes on this edition

This Markdown edition preserves the substance of the Fifth Edition manual and has been checked against the current EDSMAC physics model, then adapted for HVE 2027. Where the original manual was stale, the text follows the current program behaviour and is marked with *(updated: ...)* notes. Key updates:

- Calculation option defaults and labels (Vector Spacing default 2.0 deg; the vector force tolerance is now labelled "Max Pressure Error").
- Corrected descriptions of the two friction options (Inter-vehicle Friction is the friction coefficient; Minimum Velocity for Friction is the minimum relative velocity).
- The restitution model $e = C_0 - C_1\delta + C_2\delta^2$ with current default coefficients.
- Terrain search options are set separately from the calculation options; the "By Elevation" method is not supported.

Figures of HVE-2D's dialogs have been replaced with captures of HVE 2027, or removed where HVE 2027 has no equivalent.

<!-- NAV -->

---

Next: [Chapter 1 — EDSMAC Program Description](01-program-description.md) →

<!-- /NAV -->
