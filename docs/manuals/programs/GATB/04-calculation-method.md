# Chapter 4 — Calculation Method

*(This section was marked "to be added" in the printed Fifth Edition manual. The summary below is drawn from Chapter 1 and from the behavior of the current GATB release.)*

## Overview of the GATB Calculation Pipeline

GATB is a graphical HVE front-end for the ATB (Articulated Total Body) rigid-body dynamics program (this version is based upon ATB-V.1, June 1998). The calculation proceeds as follows:

1. **Data extraction** — GATB extracts the human, vehicle, environment and event data from HVE and writes a complete ATB input file (`gatb.ain`), automatically selecting the appropriate ATB options, card images (A-, B-, C-, D-, F- and H-cards), contact panels, belt/harness and airbag data.
2. **ATB solution** — The embedded ATB solver integrates the equations of motion of the 15-segment, 14-joint articulated body. Segment-vs-panel, segment-vs-segment, belt and airbag forces are evaluated each time step. GATB always uses a fixed ATB integration time step of 0.002 sec, which it writes into the time-step field of the A4 card; the number of steps is the maximum simulation time divided by 0.002. The other values on the A4 card (.00050, .00100, .0000625) are ATB minimum-time-step and print/integration-control fields — the .00050 is *not* a "human-collision" step. Within each step the integration is handled by the variable-step Runge-Kutta/predictor-corrector integrator internal to ATB.
3. **Output return** — The solver's standard output (`gatb.aou`), structured output (`.sal`) and time-history (tape 8) files are read back and converted into the HVE reports described in Chapter 3 (Accident History, Human Data, Injury Data, Program Data, Results, Vehicle Data, Variable Output and Trajectory Simulation).

The human model is the HVE human data set: 15 mass segments, each with up to 3 contact ellipsoids, connected by 14 joints (up to 4 joints attach to a single segment). Injury measures (HIC, HSI, CSI) are computed by the ATB post-processor.

## What GATB computes, and what ATB computes

The division is worth being explicit about, because it determines where to look
when a result is questioned.

**ATB** computes all of the physics: the equations of motion of the articulated
body, the joint models, the segment-versus-panel and segment-versus-segment
contact forces, and the harness and airbag models. None of that is GATB's, and
none of it is described in this manual — see the CVS/ATB documentation.

**GATB** computes the translation from HVE's data model into ATB's. Most of that
translation is a direct transfer of a value from one place to another, with unit
conversion where the two differ — ATB takes angles in degrees, for instance,
where HVE stores them in radians. A few quantities, however, are genuinely
constructed by GATB, and those are given below because they are not recoverable
from either program's documentation alone.

### Contact panels

An HVE contact surface is stored as three corner points. ATB expects a panel
expressed as semi-axis lengths, so GATB forms them from the edge lengths:

$$a = \frac{\left|\mathbf{P}_3 - \mathbf{P}_2\right|}{2},
  \qquad
  b = \frac{\left|\mathbf{P}_1 - \mathbf{P}_2\right|}{2}$$

> **NOTE:** The panel's third semi-axis — its thickness — is not derived from the HVE surface. It is set to a fixed 2 inches for every panel. A contact surface whose real thickness differs substantially from that will behave accordingly in the ATB contact model.

### The lap belt contact ellipsoid

ATB applies a lap belt against a contact ellipsoid, and HVE's human carries no
such ellipsoid. Where a lap belt is in use, GATB synthesizes one from the
segments either side of it: the two transverse semi-axes are taken from the
abdomen ellipsoid, and the vertical semi-axis is twice that of the pelvis
ellipsoid:

$$a = a_{Abdomen}, \qquad b = b_{Abdomen}, \qquad c = 2\,c_{Pelvis}$$

It is centred on the pelvis ellipsoid, offset downward by the pelvis semi-axis:

$$z = z_{Pelvis} - c_{Pelvis}$$

The result is a single ellipsoid spanning the abdomen and pelvis, which is what
the lap belt bears against. It exists only for the belt calculation and is not
part of the human's own contact geometry.

### Integration timestep

GATB always writes a fixed ATB integration timestep of 0.002 sec, and the number
of steps is the maximum simulation time divided by it. Within each step, ATB's
own variable-step Runge-Kutta/predictor-corrector integrator controls the
solution.

For the underlying theory of the ATB model — the equations of motion, joint models, contact force model and restraint (harness and airbag) models — see the four-volume CVS/ATB documentation and the ATB-V.1 documentation listed in [Chapter 7, Technical References](07-references.md).

<!-- NAV -->

---

← Previous: [Chapter 3 — Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — Tutorial](05-tutorial.md) →

<!-- /NAV -->
