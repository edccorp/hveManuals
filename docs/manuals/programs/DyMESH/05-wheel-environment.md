# DyMESH Wheel vs. Environment

This chapter describes the **wheel vs. environment** extension of the DyMESH
Wheels collision model: each selected wheel's cylindrical mesh collides with the
**environment (terrain) mesh** as a full DyMESH contact pair. Wheel-to-curb
strikes, ditch impacts, and ground contact during rollover are then computed by
the DyMESH contact algorithm rather than by the point-contact tire model alone,
which loses validity at large camber angles and large radial deflections.

Because the tire is now touching the ground through *two* models at once — the
classic radial-spring tire model and the DyMESH wheel mesh — the model includes
an explicit **handoff** between the two so the ground force is not
double-counted. That handoff is described in detail in
[The handoff between the tire model and DyMESH](#the-handoff-between-the-tire-model-and-dymesh),
which is the heart of this chapter.

The description below reflects the behavior of the current version of HVE.

## Enabling the model

Wheel vs. environment contact runs for a given wheel only when **all** of the
following are true:

| Level | Setting | Where |
|---|---|---|
| Event | **Use DyMESH** | DyMESH Options dialog |
| Event | **Include Environment** | DyMESH Options dialog |
| Event | **Environment start time** reached | DyMESH Options dialog |
| Wheel | **Wheel is Displaced** | Set-up → Wheels → Damage tab |
| Wheel | **Use DyMesh** | Set-up → Wheels → Damage tab |
| Wheel | **Use DyMesh Environment** | Set-up → Wheels → Damage tab |
| Wheel | Wheel damage start time reached | Set-up → Wheels → Damage tab |

Notes:

- If *Include Environment* is off, or the environment has no tessellated mesh,
  the environment start time is internally set to $1.0\times10^{8}$ s, so
  environment contact never occurs.
- With **Auto Start** checked on the Damage tab, the wheel participates
  immediately; with an explicit start time the wheel joins the collision model
  only after that time.
- The *Use DyMesh Environment* checkbox is enabled in the dialog only when the
  wheel is displaced, DyMESH is on, *Use DyMesh* is checked, and the event's
  *Include Environment* is on.

## The wheel as a DyMESH object

During initialization one mesh is built per selected wheel:

- **Object list.** The DyMESH objects are ordered vehicles first, then the
  environment, then the wheels. Each selected wheel keeps a stable object index
  for the whole run.
- **Geometry.** A closed cylinder with **80 angular slices**:
  $6\times80 + 2 = 482$ vertices and $12\times80 = 960$ triangles. From the hub
  outward: two hub-center vertices, two **rim disk** rings at the rim radius
  $r_\mathrm{rim}$ (parsed from the tire size designation), two **near-rim**
  rings at $r_\mathrm{near} = \left[\,r_\mathrm{rim} + 4\,(0.98\,r_\mathrm{tire})\,\right]/5$
  — that is, four-fifths of the way out from the rim radius to the tread radius
  — and two **tread-edge** rings at $0.98\,r_\mathrm{tire}$, where
  $r_\mathrm{tire}$ is the tire **static loaded radius**. Dual tires are modeled
  as one wide cylinder whose width is the tire width plus the dual-tire spacing.
- **Vertex materials.** Each vertex carries an A (constant) and B (linear)
  stiffness, a friction coefficient, two restitution coefficients, and a
  saturation deflection:

| Region | B stiffness | Friction | Restitution vs. vehicle | Restitution vs. environment | Saturation |
|---|---|---|---|---|---|
| Hub / rim disks | Wheel *Displacement Rate* ÷ wheel disc area | 0.55 | 0.05 | 0.05 | wheel width |
| Near-rim rings | average of rim and tread stiffness | 0.75 | 0.05 | 0.05 | wheel width |
| Tread ring | tire *Initial Ride Rate* ÷ contact-patch area | 0.75 | 0.05 | **1.00** | static loaded radius ÷ 4 |

Restitution here controls **permanent deformation**: a coefficient of 1.0
springs the vertex fully back each step (elastic), while 0.05 retains ~95% of
the crush (plastic). Against the environment the tread is therefore fully
elastic — the tire does not accumulate crush from ground contact — while the
rim deforms permanently, as a real wheel does. The vs.-environment restitution
value is selected automatically whenever the contact partner is the environment.
Friction for any wheel contact is a fixed 0.75 for the tread and near-rim
vertices (0.55 for the rim disks); the environment material's own friction
value is not used for wheels.

## The environment as a DyMESH object

- The GUI tessellates the environment geometry into an environment mesh; at
  initialization its vertices and faces are copied into the environment object
  slot, with per-vertex A/B stiffness taken from the environment surface
  materials.
- The environment is **immutable**: it never deforms, and the rebound
  (unloading) pass skips it entirely.
- A flat terrain is treated as a **solid block of earth**, not a thin shell:
  its bounding extents are padded downward — 60 in when the object extents are
  updated, and 120 in in the polygon-search bounding boxes — so a wheel cannot
  pass through a zero-thickness ground plane between timesteps.

## The simulation loop

Each derivative evaluation of the vehicle dynamics model treats the environment
as the last collision partner of every vehicle, in this order:

1. **Proximity test.** Bounding spheres are built — one for the sprung mass and
   one per active DyMESH wheel — and each wheel sphere that touches the partner
   is flagged as interfering.
2. **Body contact.** The standard DyMESH contact runs for the sprung-mass mesh
   against the environment.
3. **Wheel contact.** The wheel loop runs over the interfering wheels that pass
   the enable and time gates. For each wheel:
   - The wheel's transform is formed from its vehicle-fixed center position,
     camber angle, spin angle (the negative of the accumulated wheel rotation),
     and steer angle, plus their rates — the mesh physically spins, so vertex
     velocities include tread surface speed and friction acts in the correct
     direction.
   - The damaged and undamaged wheel meshes are placed in vehicle space.
   - The standard DyMESH contact algorithm is run between the environment and
     the wheel mesh (contact search, penetration, node force
     $F = \left(A + B\,\delta + C\,\delta^{2} + D\,\delta^{3}\right) A_v$,
     restitution, friction), with two wheel-specific rules:
     - a blown tire's stiffness multiplier is applied to the wheel mesh;
     - **hub, rim, and near-rim vertices produce no vertical force** — their
       earth-fixed z force component is zeroed, so only the tread ring carries
       vertical load. Longitudinal and lateral forces still come from every
       vertex, so a rim striking a curb face pushes back horizontally.
   - The resulting wheel force is accumulated into the vehicle's wheel collision
     force totals.
   - The deformed mesh is mapped back into wheel space (persisting damage across
     steps) and the wheel-fixed force and the camber/spin/steer moments are
     summed. The largest movement of any wheel-mesh vertex during the step — the
     **maximum wheel-mesh contact movement** — is also recorded.
   - The permanent wheel displacement/bending model is applied, capped by that
     contact movement (see the [Version 3 chapter](03-version-3.md));
     displacement is horizontal (x, y) only, since vertical wheel motion is a
     suspension degree of freedom.
4. **Smoothing.** Each wheel's force and moment is averaged with the previous
   step's values (two-point moving average). The smoothed previous vertical
   force is what the tire-model handoff (below) reads.

## Force paths into the vehicle dynamics

| Quantity | Path |
|---|---|
| Wheel collision Fx, Fy | Directly onto the sprung mass |
| Wheel collision Mz (yaw) | Directly onto the sprung mass |
| Wheel collision **Fz** | Into the **unsprung-mass equation of motion**, i.e., through the suspension |
| Spin moment (My′) | Into the wheel-spin equation as a collision torque |
| Camber / steer moments | Permanent camber/steer change via the wheel displacement model |
| Permanent x/y displacement | Added to the wheel's vehicle-fixed center position each step, with solid-axle side coupling |

Because collision loads can legitimately exceed the normal suspension limits,
the excessive-deflection, excessive-velocity, and excessive-force suspension
error stops are suppressed for DyMESH wheels, as is the excessive-tire-deflection
stop in the tire/terrain model.

## The handoff between the tire model and DyMESH

With wheel vs. environment active, the same tire touches the ground through two
models. Left uncorrected, the radial-spring tire force and the DyMESH tread
force would both push the vehicle up and the total would be roughly double the
correct load. The model therefore hands authority from one model to the other in
three coordinated pieces, all gated on the wheel having *Use DyMesh Environment*
selected and on both the event's environment start time and the wheel's damage
start time having been reached.

### 1. Tire deflection rate limiting

The point-contact model computes the radial tire deflection
$\delta_\mathrm{tire}$ geometrically from the terrain under the wheel center.
During a hard vertical event (curb face, ditch wall, rollover touchdown) that
geometric deflection can jump in a single timestep. When the wheel is a DyMESH
environment wheel, the growth of $\delta_\mathrm{tire}$ is limited per timestep:

- $\delta_\mathrm{tire}$ may not exceed last step's deflection plus the tire's
  secondary-stiffness breakpoint deflection;
- if the tire carried **no** deflection on the previous step,
  $\delta_\mathrm{tire}$ is forced to zero — a suddenly deep penetration produces
  *no* point-contact force at all, and the DyMESH wheel mesh carries the impact
  instead.

The tire radius used by the rest of the tire model is recomputed from the
limited deflection, keeping the two models geometrically consistent.

### 2. Vertical force blending

After the radial tire force $F_\mathrm{tire}$ is computed, it is blended with
the DyMESH result using three reference quantities:

- $F_\mathrm{DyMESH}$ — the previous step's **smoothed DyMESH vertical wheel
  force** (taken with the sign convention that upward ground reaction is
  positive), divided by the number of tires at the wheel;
- $W_\mathrm{static}$ — the **static load** carried at that wheel (static
  suspension force minus wheel weight, and minus half the solid-axle mass where
  applicable);
- $F_\mathrm{spring}$ — last step's deflection times the current radial
  stiffness (the force the tire spring "should" be carrying).

The blend then works case by case:

| Case | Resulting radial force |
|---|---|
| Tire force below both the DyMESH force and static load | $F_\mathrm{DyMESH} + F_\mathrm{tire}$ |
| Tire force below DyMESH force, at/above static load | $F_\mathrm{DyMESH} + W_\mathrm{static}$ |
| Tire force ≥ DyMESH force, DyMESH force ≥ static load | $F_\mathrm{DyMESH} + \min(W_\mathrm{static}, F_\mathrm{spring})$ |
| Tire force ≥ DyMESH force, DyMESH force < static load (and > 0) | $F_\mathrm{DyMESH} + \min(W_\mathrm{static}, F_\mathrm{tire})$ |
| Deflection > 15% of tire radius while DyMESH is carrying load | $\min(F_\mathrm{tire}, F_\mathrm{DyMESH})$, or 0 if the DyMESH force ≤ 0 |

The intent in every branch is the same: **the DyMESH force is authoritative,
and the point-contact tire model contributes at most its static share on top of
it.** In quiet rolling (DyMESH force ≈ 0) the ladder reduces to the ordinary
tire force; in a hard strike the DyMESH force dominates and the tire spring is
prevented from stacking a second full reaction on top.

Two additional rules close the loop:

- beyond the maximum roll angle the radial tire force is zeroed entirely —
  the DyMESH mesh is then the only ground contact;
- the final blended force is converted back into an equivalent deflection,
  $\delta_\mathrm{tire} = F_\mathrm{tire}/K_t$ using the radial tire stiffness
  $K_t$, capped at the tire's maximum deflection, so that outputs and the next
  step's rate limiter see a consistent state.

### 3. Shear-force fade near rollover

The friction-circle tire model produces Fx/Fy from slip at the contact patch —
meaningless once the wheel plane approaches the ground plane. For a non-DyMESH
wheel, tire forces are simply zeroed when the cosine of the wheel-to-ground
inclination angle $\gamma_g$ falls below the minimum-inclination threshold
$c_\mathrm{min} = 0.17365$ (inclination beyond ≈80°). For a DyMESH environment
wheel they are instead **faded smoothly**: each of the contact-patch forces
$F_x$, $F_y$ and $F_z$, the plough forces, the slips, and the roll moment is
scaled by

$$
f = \frac{2}{\dfrac{\cos\gamma_g}{c_\mathrm{min}} + \dfrac{c_\mathrm{min}}{\cos\gamma_g}}
\qquad (\text{Eq. 1})
$$

which equals 1.0 exactly at the threshold and falls toward 0 as the tire goes
flat. This avoids the force discontinuity of the hard cutoff while the DyMESH
tread/rim contact takes over the shear loads through its own friction model.

### Summary of the handoff

| Regime | Ground normal force | Ground shear force |
|---|---|---|
| Normal rolling | Tire model (DyMESH ≈ 0) | Tire model |
| Curb/obstacle strike | DyMESH tread force + capped tire share | Tire model + DyMESH friction |
| Near/at rollover (>~80° inclination) | DyMESH tread force (tire force faded/zeroed) | DyMESH friction (tire forces faded) |

## Outputs

- The per-wheel collision impulses (**Fx Imp**, **Fy Imp**, **Fz Imp**,
  **Mx Imp**, **My Imp**, **Mz Imp**) appear in the Key Results output, and the
  smoothed wheel collision forces and wheel-fixed moments drive the Output vs.
  Time wheel channels.
- The program-data output tables list each DyMESH wheel's mesh size and its
  first/last vertex A and B stiffnesses (the rim and tread values).

## Quick reference

| Parameter | Value / source | Meaning |
|---|---|---|
| Angular slices | 80 | Angular increments in the wheel mesh |
| Wheel mesh size | 482 verts / 960 triangles | Per wheel |
| Tread radius | 0.98 × static loaded radius | Outer ring radius |
| Tread restitution vs. environment | 1.0 | Fully elastic (no permanent tire crush) |
| Rim restitution | 0.05 | Plastic (permanent rim deformation) |
| Wheel contact friction | 0.75 (tread/near-rim), 0.55 (rim disks) | Fixed values |
| Rim B stiffness | *Displacement Rate* ÷ wheel disc area | From Damage tab |
| Tread B stiffness | *Initial Ride Rate* ÷ contact-patch area | From tire data |
| Minimum-inclination threshold | 0.17365 (cos ≈ 80°) | Shear-fade threshold |
| Environment depth padding | 60–120 in | Prevents ghosting through flat terrain |
| Environment start time | DyMESH Options dialog | Earliest wheel/body vs. environment contact |

<!-- NAV -->

---

← Previous: [DyMESH — Facts of Life](04-facts-of-life.md)  |  [Index](README.md)

<!-- /NAV -->
