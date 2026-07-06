# Chapter 4 — Calculation Method

*(This section was marked "to be added" in the printed Fifth Edition manual. The summary below is drawn from Chapter 1 and the current GATB source code.)*

## Overview of the GATB Calculation Pipeline

GATB is a graphical HVE front-end for the ATB (Articulated Total Body) rigid-body dynamics program (this version is based upon ATB-V.1, June 1998). The calculation proceeds as follows (verified against `Physics/Source/GATB/`):

1. **Data extraction** — GATB extracts the human, vehicle, environment and event data from HVE (`GATBinput.cpp`) and writes a complete ATB input file (`gatb.ain`), automatically selecting the appropriate ATB options, card images (A-, B-, C-, D-, F- and H-cards), contact panels, belt/harness and airbag data.
2. **ATB solution** — The embedded ATB solver (the Fortran routines in `Physics/Source/GATB/*.for`, built as the GATB Fortran function library) integrates the equations of motion of the 15-segment, 14-joint articulated body. Segment-vs-panel, segment-vs-segment, belt and airbag forces are evaluated each time step. GATB hard-codes the ATB integration time step at a fixed 0.002 sec (`GATBinput.cpp:538`, `ATBTimeStep = 0.002f`, written into the `%8.5f` field of the A4 card at `GATBinput.cpp:563`); the number of steps is derived from `Tmax / 0.002`. The other values on the A4 card (`.00050`, `.00100`, `.0000625`) are ATB minimum-time-step and print/integration-control fields — the `.00050` is *not* a "human-collision" step. Within each step the integration is handled by the variable-step Runge-Kutta/predictor-corrector integrator internal to ATB (`dintg.for`, `daux*.for`).
3. **Output return** — The solver's standard output (`gatb.aou`), structured output (`.sal`) and time-history (tape 8) files are read back (`GATBoutpt.cpp`, `read_tape_8.for`) and converted into the HVE reports described in Chapter 3 (Accident History, Human Data, Injury Data, Program Data, Results, Vehicle Data, Variable Output and Trajectory Simulation).

The human model is the HVE human data set: 15 mass segments, each with up to 3 contact ellipsoids, connected by 14 joints (up to 4 joints attach to a single segment) — see `Physics/Include/HUMAN.H`. Injury measures (HIC, HSI, CSI) are computed by the ATB post-processor (`postpr.for`, `hiccsi.for`).

For the underlying theory of the ATB model — the equations of motion, joint models, contact force model and restraint (harness and airbag) models — see the four-volume CVS/ATB documentation and the ATB-V.1 documentation listed in [Chapter 7, Technical References](07-references.md).

<!-- NAV -->

---

← Previous: [Chapter 3 — Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — Tutorial](05-tutorial.md) →

<!-- /NAV -->
