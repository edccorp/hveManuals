# EDSMAC4 — Multi-Vehicle Collision Simulator

**Engineering Dynamics Corporation Simulation Model of Automobile Collisions, 4th Revision — Version 6**

Updated Markdown edition, converted from the Sixth Edition manual (January 2006) and brought up to date with the current version of the EDSMAC4 program, then adapted for HVE Studio.

## EDSMAC4 in HVE Studio

HVE Studio compiles HVE's own EDSMAC4 source, so the physics described in this manual — the collision model, the tire model, the equations of motion and the messages — is EDSMAC4's. What is different is the program around it:

- **Choosing EDSMAC4.** Open the **Event (F5)** editor, and in **Event Information › Calculation Method** pick **EDSMAC4** from the **Method** list. There is no separate EDSMAC4 program to start: the event's method selects the engine.
- **Calculation options** are in the **EDSMAC Options** window, opened with the **Method Options...** button under the Method list. EDSMAC and EDSMAC4 share this window; see [Chapter 2 — Calculation Options](02-program-input.md#calculation-options) for which settings each program reads.
- **Running and playback.** Press **Run** on the playback bar under the viewport (or **Output › Run Simulation**, Ctrl+R). The solved event plays back in the same viewport. To play it with other solved events on one timeline, use the **Playback (F6)** editor.
- **Reports.** EDSMAC4's own report pages (Accident History, Damage Data, Driver Data, Event Data, Environment Data, Messages, Program Data, References, Vehicle Data) are in **Output › HVE Reports**. Time histories are in **Output › Key Results** (the Variable Output table) and **Output › Output Graph**.
- **HVE cases.** **File › Open Case** reads HVE's own `.hve` files, including the EDSMAC4 tutorial case used in [Chapter 5](05-tutorial.md).

Where HVE Studio behaves differently from HVE, the page says so in a box marked **HVE Studio**. The differences that change an answer are:

- the HVE Driver Model (path follower) is switched off at impact **per vehicle**, not for every vehicle in the event, and can optionally keep following through an impact ([Chapter 2 — Driver Controls](02-program-input.md#driver-controls));
- a Steer DOF setting stored in an imported HVE case is not used: EDSMAC4 always runs with the steer degree of freedom off, so the steer table applies ([Chapter 2 — Calculation Options](02-program-input.md#calculation-options));

## How to Use This Manual

This manual is the user's manual for the EDSMAC4 simulation model. It describes the model's features and use. Input parameters and output reports are described at a high level. It is intended to be used together with the HVE Studio User's Manual, which covers the human, vehicle and environment models and the editors in detail.

## If You Have Questions

The physics questions this manual answers are EDSMAC4's. Questions about HVE Studio itself — a dialog, a file, a result that differs from HVE — belong with the HVE Studio project, not with Engineering Dynamics Corporation.

## Contents

- [1 — EDSMAC4 Program Description](01-program-description.md)
- [2 — EDSMAC4 Program Input](02-program-input.md)
- [3 — EDSMAC4 Program Output](03-program-output.md)
- [4 — Calculation Method](04-calculation-method.md)
- [5 — EDSMAC4 Tutorial](05-tutorial.md)
- [6 — Messages](06-messages.md)
- [7 — Technical References](07-references.md)

*The original manual's Chapter 8 (Index) is omitted; use text search in this Markdown edition instead.*

Related pages:

- [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md) — dialog-by-dialog reference for the EDSMAC4 Calculation Options.

<!-- NAV -->

---

Next: [Chapter 1 — EDSMAC4 Program Description](01-program-description.md) →

<!-- /NAV -->
