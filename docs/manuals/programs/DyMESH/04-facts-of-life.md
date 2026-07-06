# DyMESH — Facts of Life

Practical guidance, caveats, and limitations for users of DyMESH, drawn from the
EDC *DyMESH — Important Notes* presentation (2026 HVE Forum). These are the
things to keep in mind before, during, and after a DyMESH run.

## 1. You are doing 3-D collision simulation

When using DyMESH, you're doing three-dimensional collision simulation. This is
technically a very difficult task. **Don't expect it to be simple.** Setting up a
credible DyMESH case takes care with geometry, stiffness, and impact
configuration.

## 2. DyMESH will not work on every crash

DyMESH is a powerful general-purpose tool, but **it is not going to work on every
crash.** Some impact configurations, geometries, or data quality problems will
not yield a good simulation. Be prepared to fall back to other methods when a
case is unsuitable.

## 3. Computer horsepower matters

**Computer horsepower means everything to DyMESH.** The contact search and
force computation run every collision time step over the vehicle meshes, so CPU
speed and memory directly determine how quickly (and how finely) a case can be
run.

## 4. Be patient during a run

**Be patient.** HVE is *resting* in between integration time steps while DyMESH
is executing, so quickly punching a bunch of buttons during a run may result in
unexpected behavior. Let the run proceed rather than clicking through the
interface while DyMESH is working.

## 5. No induced damage

**Induced damage is not included.** No damage will be displayed unless one or
more vertices on one vehicle were *actually in contact* with the other vehicle.
DyMESH represents only direct-contact (direct) damage — it does not model the
secondary/induced structural deformation that propagates away from the contact
region. (This is the same limitation noted in the technical overview: "local
behavior of structure not captured in all cases; no induced damage.")

*(updated: This is consistent with the code — a vertex only enters the damage
profile once it has penetrated a master surface and been restored; see the
`IsDamaged` / `DamageThisTimeStep` handling and `MakeProfile()` in `Dymesh.cpp`.)*

## 6. Mesh quality is a factor

The quality of the vehicle mesh directly affects the result:

- **Poorly tessellated meshes do not work well.** The contact algorithm relies
  on reasonably uniform, well-formed triangles.
- **Early EDC meshes do not meet all criteria**, especially on the **bottom** of
  the vehicle.
- **Use the *Tessellation* option** to improve a mesh before running DyMESH.

*(updated: The Tessellation / "Vehicle Mesh Options" controls in the current code
include a *Tessellate* toggle, a *Vertex Weld Distance*, and a *Max Side Length*
— these are the levers referred to here for cleaning up a mesh.)*

## 7. Generic vehicles must be tessellated

**Generic Vehicles' meshes *must* be tessellated** before use with DyMESH. Their
as-delivered meshes are not suitable for the contact algorithm without
tessellation.

---
*Source: DyMESH Important Notes (2026 HVE Forum) — organized and verified against DYMESH.H / Dymesh.cpp, 2026-07-05.*

<!-- NAV -->

---

← Previous: [DyMESH Version 3](03-version-3.md)  |  [Index](README.md)

<!-- /NAV -->
