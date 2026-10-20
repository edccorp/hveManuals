# DyMESH Reference Manual

**DyMESH** (Dynamic Mechanical Shell) is the three-dimensional dynamic-mesh
collision and damage model used by HVE's simulation models. It computes
inter-vehicle (and vehicle-environment) contact forces, moments, and damage
directly from the polygon meshes that describe the exterior surfaces of the
vehicles and objects in an event. The resulting collision forces are combined
with the other external forces acting on each vehicle (tires, aerodynamic drag,
etc.) and the six-degree-of-freedom equations of motion are integrated to
produce the collision dynamics and the resulting damage (crush) profile.

DyMESH is invoked primarily by **SIMON** (and is also available to **EDSMAC4**).
It replaces the idealized impulse-momentum treatment of impact with a true
force-based, time-stepped collision simulation.

## DyMESH in HVE Studio

HVE Studio compiles HVE's own DyMESH source, so the collision model described in
this manual — mesh contact, the node force law, crush sharing, restitution, the
DyMESH Wheels model and wheel-vs-environment contact — is the model HVE Studio
runs. What differs is where the controls are and how the results are shown:

- **Which events use it.** DyMESH runs on **SIMON** events. On an EDSMAC4
  event the DyMESH settings are stored with the case but not used: EDSMAC4
  computes its collision with its own planar crush model (it still deforms the
  vehicle mesh for display).
- **Settings.** **Event › DyMESH Options** holds the event's DyMESH settings
  (enable, environment contact, start times, search option, smoothing,
  version, restoration options and the per-pair friction and relaxation
  length). The same core settings, plus **Contact a vehicle's own trailer**,
  also appear in the DyMESH section of **Event Information › Method Options**
  (SIMON Options). No license is needed.
- **Options carried but not used.** Several DyMESH Options settings are kept
  with the case but reach no code in the engine — in HVE's own engine source as
  well as in HVE Studio. The dialog marks each one; see
  [Collision Model](02-collision-model.md) and [Version 3](03-version-3.md).
- **Mesh preparation** (tessellate, maximum triangle leg, weld distance) is set
  per event per vehicle in **Event › DyMESH Options**, under *Contact Mesh
  Preparation (per vehicle)*, with the vehicle's defaults on the Collision tab
  of **Vehicle › Editors › Vehicle Mesh**; see [Facts of Life](04-facts-of-life.md).
- **Wheels.** The per-wheel DyMESH inputs are on the *Wheel Damage* tab of
  **Event › Wheels**; the **Mesh** box of the **DyMESH Wheel** row (**View › Scene Display**,
  Vehicle group) draws the wheel contact meshes after a run, and its **Nodes**
  box labels each wheel's contact model and tire law.
- **Results.** The crushed mesh is drawn in the viewport and follows the
  playback time. HVE's DamageStudio window is not available; see
  [DamageStudio](../DamageStudio/README.md) for what HVE Studio offers instead.

## Provenance

This manual was organized from three 2026 HVE Forum presentations by
**Allen R. York** and **Terry D. Day** of the Engineering Dynamics Company
(EDC):

- **DyMESH Collision Simulation** (York & Day, March 2026) — the core technical
  overview: history, mesh model, contact algorithm, force/damage computation,
  and coupling to the vehicle dynamics.
- **DyMESH Version 3** (EDC, 2026 HVE Forum) — the Version 3 additions, chiefly
  the *DyMESH Wheels* collision model (forces and moments from impact at the
  wheels).
- **DyMESH — Important Notes / Facts of Life** (EDC, 2026 HVE Forum) — practical
  guidance, caveats, and limitations for users.

The technical content has been brought up to date with the current version of
HVE, covering the DyMESH collision model, its use by SIMON, and the DyMESH
Options dialog. Where the current program differs from the slide decks, the
discrepancy is called out with an italic *(updated: ...)* note.

## Contents

1. [Overview](01-overview.md) — what DyMESH is and does; where it sits in HVE;
   which models use it; history.
2. [Collision Model](02-collision-model.md) — the technical model: mesh
   representation, contact (Location) and restoration detection, force and
   moment computation, 3-D force-deflection stiffness, vertex displacement
   (crush depth), restitution, and coupling to the equations of motion.
3. [Version 3](03-version-3.md) — the DyMESH Wheels collision model and other
   Version 3 capabilities.
4. [Facts of Life](04-facts-of-life.md) — practical notes, caveats, and
   limitations.
5. [Wheel vs. Environment](05-wheel-environment.md) — the DyMESH wheel vs.
   environment contact model: the wheel and terrain as DyMESH objects, the
   simulation loop, and the handoff between the point-contact tire model and
   DyMESH.

## Related documentation

- **[SIMON manual](../SIMON/README.md)** — the primary vehicle dynamics model
  that hosts DyMESH.
- **[EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md)**.
- **[Options menu (DyMESH Options dialog)](../../hve-users/02-menu-reference/06-options-menu.md)**
  — HVE's location; in HVE Studio the dialog is **Event › DyMESH Options**.
- **[Wheel damage / displacement](../../05-tires-wheels/WheelsDlg1.md)** — the
  wheel-data inputs used by the DyMESH Wheels model.

---
*Source: DyMESH Collision Simulation, DyMESH Version 3, and DyMESH Important Notes (2026 HVE Forum). Updated to match the current version of HVE.*

<!-- NAV -->

---

Next: [DyMESH Overview](01-overview.md) →

<!-- /NAV -->
