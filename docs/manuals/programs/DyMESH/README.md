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

The technical content has been verified against the current HVE source code
(`Physics/Include/DYMESH.H`, `Physics/Source/LibHve/Dymesh.cpp`,
`Physics/Source/Simon/PHYMODEL.CPP`, and the `CDyMeshOptionsDlg` dialog in
`HVEINV-64`). Where the current code differs from the slide decks, the
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

## Related documentation

- **SIMON manual** — [`../SIMON/`](../SIMON/) — the primary vehicle dynamics
  model that hosts DyMESH.
- **Calculation options (EDSMAC4)** —
  [`../../10-calculation-options/CalcOptEDSMAC4.md`](../../10-calculation-options/CalcOptEDSMAC4.md).
- **Options menu (DyMESH Options dialog)** —
  [`../../hve-users/02-menu-reference/06-options-menu.md`](../../hve-users/02-menu-reference/06-options-menu.md).
- **Wheel damage / displacement** —
  [`../../05-tires-wheels/WheelsDlg1.md`](../../05-tires-wheels/WheelsDlg1.md) —
  the wheel-data inputs used by the DyMESH Wheels model.

---
*Source: DyMESH Collision Simulation, DyMESH Version 3, and DyMESH Important Notes (2026 HVE Forum) — organized and verified against DYMESH.H / Dymesh.cpp, 2026-07-05.*

<!-- NAV -->

---

Next: [DyMESH Overview](01-overview.md) →

<!-- /NAV -->
