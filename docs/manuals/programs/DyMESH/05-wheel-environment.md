# DyMESH Wheel vs. Environment

This chapter describes the **wheel vs. environment** extension of the DyMESH
Wheels collision model: each selected wheel's cylindrical mesh collides with the
**environment (terrain) mesh** as a full DyMESH contact pair. Wheel-to-curb
strikes, ditch impacts, and ground contact during rollover are then computed by
the DyMESH contact algorithm rather than by the point-contact tire model alone,
which loses validity at large camber angles and large radial deflections.

Because the tire is now touching the ground through *two* models at once — the
classic radial-spring tire model and the DyMESH wheel mesh — the implementation
includes an explicit **handoff** between the two so the ground force is not
double-counted. That handoff is described in detail in
[The handoff between the tire model and DyMESH](#the-handoff-between-the-tire-model-and-dymesh),
which is the heart of this chapter.

All statements below are verified against the current source code
(`Physics/Source/LibHve/Dymesh.cpp`, `Physics/Source/Simon/PHYMODEL.CPP`,
`Physics/Source/Simon/Road.cpp`, `Physics/Source/Simon/Tire.cpp`,
`Physics/Source/Simon/suspension.cpp`, `Physics/Source/Simon/MATRIX.CPP`).

## Enabling the model

Wheel vs. environment contact runs for a given wheel only when **all** of the
following are true:

| Level | Setting | Where | Code |
|---|---|---|---|
| Event | **Use DyMESH** | DyMESH Options dialog | `DyMeshIsTrue` |
| Event | **Include Environment** | DyMESH Options dialog | `DyMeshOptions.UseEnvironment` |
| Event | **Environment start time** reached | DyMESH Options dialog | `tSim >= tDymeshEnvMin` (`calcFloat[7]`) |
| Wheel | **Wheel is Displaced** | Set-up → Wheels → Damage tab | `IsDisplaced` |
| Wheel | **Use DyMesh** | Set-up → Wheels → Damage tab | `DyMeshWheelIsUsed[veh][axle][side]` |
| Wheel | **Use DyMesh Environment** | Set-up → Wheels → Damage tab | `DyMeshWheelEnvIsUsed[veh][axle][side]` |
| Wheel | Wheel damage start time reached | Set-up → Wheels → Damage tab | `tSim >= MovedWheelT[veh][axle][side]` |

Notes:

- If *Include Environment* is off, or the environment has no tessellated mesh
  (`Environment.EnvironMesh` empty), the environment start time is internally
  set to `1.0e8` s so environment contact never occurs
  (`PHYINPUT.CPP`, `LoadSimControlData()`).
- With **Auto Start** checked on the Damage tab, the wheel participates
  immediately; with an explicit start time the wheel joins the collision model
  only after that time.
- The *Use DyMesh Environment* checkbox is enabled in the dialog only when the
  wheel is displaced, DyMESH is on, *Use DyMesh* is checked, and the event's
  *Include Environment* is on (`EvtWheelDisplacementPage.cpp`).

## The wheel as a DyMESH object

`InitializeDyMeshWheels()` and `calcWheelMesh()` (`Dymesh.cpp`) build one mesh
per selected wheel:

- **Object table.** DyMESH object indices `0..NumVehicles-1` are the vehicles,
  index `NumVehicles` is the environment (`EnvironIndex`), and indices
  `NumVehicles+1...` are the wheels (`WheelIndex`). Each wheel keeps a stable
  index `DyMeshWheelNdx[veh][axle][side]`.
- **Geometry.** A closed cylinder with `NUM_DYMESH_WHEEL_INC = 80` angular
  slices: `6·80 + 2 = 482` vertices and `12·80 = 960` triangles. From the hub
  outward: two hub-center vertices, two **rim disk** rings at the rim radius
  (parsed from the tire size designation), two **near-rim** rings at
  `(wheelRad + 4·0.98·tireRad)/5`, and two **tread-edge** rings at
  `0.98·tireRad`, where `tireRad` is the tire **static loaded radius**
  (`tireSLR`). Dual tires are modeled as one wide cylinder
  (`width = tireWidth + TireSpace`).
- **Vertex materials.** Each vertex carries an A (constant) and B (linear)
  stiffness, a friction coefficient, two restitution coefficients, and a
  saturation deflection:

| Region | B stiffness | Friction | Restitution vs. vehicle | Restitution vs. environment | Saturation |
|---|---|---|---|---|---|
| Hub / rim disks | Wheel *Displacement Rate* ÷ wheel disc area | 0.55 | 0.05 | 0.05 | wheel width |
| Near-rim rings | average of rim and tread stiffness | 0.75 | 0.05 | 0.05 | wheel width |
| Tread ring | tire *Initial Ride Rate* ÷ contact-patch area | 0.75 | 0.05 | **1.00** | `tireRad/4` |

Restitution here controls **permanent deformation**: a coefficient of 1.0
springs the vertex fully back each step (elastic), while 0.05 retains ~95% of
the crush (plastic). Against the environment the tread is therefore fully
elastic — the tire does not accumulate crush from ground contact — while the
rim deforms permanently, as a real wheel does. `GetRestitutionCoef()`
(`Dymesh.cpp`) selects the vs.-environment value whenever the contact partner
is the environment. Friction for any wheel contact is a fixed 0.75 in
`GetFrictionCoef()`; the environment material's friction is not used for
wheels.

## The environment as a DyMESH object

- The GUI tessellates the environment geometry into `Environment.EnvironMesh`
  (`HVEINV-64/EnvironMesh.cpp`); `DyMeshInitialize()` copies its vertices and
  faces into the `EnvironIndex` mesh slot, with per-vertex A/B stiffness taken
  from the environment surface materials.
- The environment is **immutable**: it never deforms, and `ReboundDamagedVerts()`
  skips it entirely.
- A flat terrain is treated as a **solid block of earth**, not a thin shell:
  its bounding extents are padded downward (+60 in in `UpdateVehicleExtents()`,
  +120 in in the polygon-search bounding boxes) so a wheel cannot pass through
  a zero-thickness ground plane between timesteps.

## The simulation loop

Each derivative evaluation (`Daux()` in `PHYMODEL.CPP`) treats the environment
as the last collision partner of every vehicle:

1. **Proximity test.** `CollisionTest(i, j)` builds bounding spheres — one for
   the sprung mass and one per active DyMESH wheel — and marks
   `WheelInterference[veh][axle][side]` for each wheel sphere that touches the
   partner.
2. **Body contact.** `DyMesh(vehicle, environment)` runs for the sprung-mass
   mesh.
3. **Wheel contact.** `DyMeshWheels()` loops over the interfering wheels that
   pass the enable and time gates. For each wheel:
   - `GetWheelMatrices()` forms the wheel's transform from its vehicle-fixed
     center `WheelCoord`, camber `Gamma`, spin `-Omega`, and steer `Delta`,
     plus their rates — the mesh physically spins, so vertex velocities include
     tread surface speed and friction acts in the correct direction.
   - `UpdateWheelMesh()` places the (damaged and undamaged) wheel mesh in
     vehicle space.
   - `DyMesh(environment, wheel)` runs the standard DyMESH contact algorithm
     (contact search, penetration, node force
     `F = (A + B·δ + C·δ² + D·δ³)·area`, restitution, friction), with two
     wheel-specific rules:
     - a blown tire's stiffness multiplier is applied to the wheel mesh
       (`ReDefineVertStiffness()`);
     - **hub, rim, and near-rim vertices produce no vertical force** — their
       earth-fixed z force component is zeroed, so only the tread ring carries
       vertical load (`SlaveNodeForce()`, `Dymesh.cpp`). Longitudinal and
       lateral forces still come from every vertex, so a rim striking a curb
       face pushes back horizontally.
   - `AddWheelForceToSprungMass()` accumulates the wheel force into
     `FsumColWheel[veh][axle][side]`.
   - `UpdateWheelMeshDamage()` maps the deformed mesh back into wheel space
     (persisting damage across steps) and sums the wheel-fixed force and the
     camber/spin/steer moments; it also records the largest vertex movement,
     `MaxContactDispl`.
   - `DyMeshWheelDispl()` applies the permanent wheel displacement/bending
     model (see the [Version 3 chapter](03-version-3.md)); displacement is
     horizontal (x, y) only, since vertical wheel motion is a suspension
     degree of freedom.
4. **Smoothing.** `SmoothCollisionForce()` averages each wheel's force and
   moment with the previous step's values (two-point moving average). The
   smoothed previous vertical force, `FsumColWheelPrev[..][2]`, is what the
   tire-model handoff (below) reads.

## Force paths into the vehicle dynamics

| Quantity | Path |
|---|---|
| Wheel collision Fx, Fy | Directly onto the sprung mass (`FsumCol`) |
| Wheel collision Mz (yaw) | Directly onto the sprung mass (`TsumCol`) |
| Wheel collision **Fz** | Into the **unsprung-mass equation of motion** (`MATRIX.CPP`), i.e., through the suspension |
| Spin moment (My′) | Into the wheel-spin equation as a collision torque (`TORQUE.CPP`) |
| Camber / steer moments | Permanent camber/steer change via `DyMeshWheelDispl()` |
| Permanent x/y displacement | Added to `WheelCoord` each step (`WHEELPOS.CPP`), with solid-axle side coupling |

Because collision loads can legitimately exceed the normal suspension limits,
the excessive-deflection, excessive-velocity, and excessive-force error stops
in `suspension.cpp` are suppressed for DyMESH wheels, as is the
excessive-tire-deflection stop in `Road.cpp`.

## The handoff between the tire model and DyMESH

With wheel vs. environment active, the same tire touches the ground through two
models. Left uncorrected, the radial-spring tire force and the DyMESH tread
force would both push the vehicle up and the total would be roughly double the
correct load. The code therefore hands authority from one model to the other in
three coordinated pieces, all gated on
`DyMeshWheelEnvIsUsed && tSim >= tDymeshEnvMin && tSim >= MovedWheelT`.

### 1. Tire deflection rate limiting (`TireDefl()`, `Road.cpp`)

The point-contact model computes the radial deflection `trh` geometrically from
the terrain under the wheel center. During a hard vertical event (curb face,
ditch wall, rollover touchdown) that geometric deflection can jump in a single
timestep. When the wheel is a DyMESH environment wheel, the growth of `trh` is
limited per timestep:

- `trh` may not exceed `TireDeltPrev + TireDelt` (last step's deflection plus
  the tire's secondary-stiffness breakpoint deflection);
- if the tire carried **no** deflection on the previous step, `trh` is forced
  to zero — a suddenly deep penetration produces *no* point-contact force at
  all, and the DyMESH wheel mesh carries the impact instead.

The tire radius used by the rest of the tire model is recomputed from the
limited deflection, keeping the two models geometrically consistent.

### 2. Vertical force blending (`TireDefl()`, `Road.cpp`)

After the radial force `TireFr` is computed, it is blended with the DyMESH
result using three reference quantities:

- `PrevFzDyMESH` — the previous step's **smoothed DyMESH vertical wheel force**
  (`−FsumColWheelPrev[..][2]`), divided by the number of tires at the wheel;
- `TestWt` — the **static load** carried at that wheel (static suspension force
  minus wheel weight, and minus half the solid-axle mass where applicable);
- `TestWt2` — last step's deflection times the current radial stiffness (the
  force the tire spring "should" be carrying).

The blend then works case by case:

| Case | Resulting radial force |
|---|---|
| Tire force below both the DyMESH force and static load | `PrevFzDyMESH + TireFr` |
| Tire force below DyMESH force, at/above static load | `PrevFzDyMESH + TestWt` |
| Tire force ≥ DyMESH force, DyMESH force ≥ static load | `PrevFzDyMESH + min(TestWt, TestWt2)` |
| Tire force ≥ DyMESH force, DyMESH force < static load (and > 0) | `PrevFzDyMESH + min(TestWt, TireFr)` |
| Deflection > 15% of tire radius while DyMESH is carrying load | `min(TireFr, PrevFzDyMESH)`, or 0 if DyMESH force ≤ 0 |

The intent in every branch is the same: **the DyMESH force is authoritative,
and the point-contact tire model contributes at most its static share on top of
it.** In quiet rolling (DyMESH force ≈ 0) the ladder reduces to the ordinary
tire force; in a hard strike the DyMESH force dominates and the tire spring is
prevented from stacking a second full reaction on top.

Two additional rules close the loop:

- beyond the maximum roll angle the radial tire force is zeroed entirely —
  the DyMESH mesh is then the only ground contact;
- the final blended force is converted back into an equivalent deflection
  (`trh = TireFr/Kt`, capped at the tire's maximum deflection) so that outputs
  and the next step's rate limiter see a consistent state.

### 3. Shear-force fade near rollover (`Tire()`, `Tire.cpp`)

The friction-circle tire model produces Fx/Fy from slip at the contact patch —
meaningless once the wheel plane approaches the ground plane. For a non-DyMESH
wheel, tire forces are simply zeroed when
`cos(GammaGround) < MIN_INCLINATION` (inclination beyond ≈80°). For a DyMESH
environment wheel they are instead **faded smoothly**: each of `TireFxp`,
`TireFyp`, `TireFzp`, the plough forces, slips, and the roll moment is scaled
by

```
factor = 2 / ( cos(GammaGround)/MIN_INCLINATION + MIN_INCLINATION/cos(GammaGround) )
```

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

- The per-wheel collision impulses (`Fx Imp`, `Fy Imp`, `Fz Imp`, `Mx Imp`,
  `My Imp`, `Mz Imp`) appear in the Key Results output, and the smoothed wheel
  collision forces (`FsumColWheelOut`) and wheel-fixed moments
  (`SumWheelMomentOut`) drive the Output vs. Time wheel channels.
- The program-data output tables list each DyMESH wheel's mesh size and its
  first/last vertex A and B stiffnesses (rim and tread values) under
  `tireDyMeshWheelStiffA/B` (`PHYINPUT.CPP`).

## Quick reference

| Constant / parameter | Value / source | Meaning |
|---|---|---|
| `NUM_DYMESH_WHEEL_INC` | 80 | Angular slices in the wheel mesh |
| Wheel mesh size | 482 verts / 960 triangles | Per wheel |
| Tread radius | 0.98 × static loaded radius | Outer ring radius |
| Tread restitution vs. environment | 1.0 | Fully elastic (no permanent tire crush) |
| Rim restitution | 0.05 | Plastic (permanent rim deformation) |
| Wheel contact friction | 0.75 (tread/near-rim), 0.55 (rim disks) | Fixed values |
| Rim B stiffness | *Displacement Rate* ÷ wheel disc area | From Damage tab |
| Tread B stiffness | *Initial Ride Rate* ÷ contact-patch area | From tire data |
| `MIN_INCLINATION` | 0.17365 (cos ≈ 80°) | Shear-fade threshold |
| Environment depth padding | 60–120 in | Prevents ghosting through flat terrain |
| Environment start time | DyMESH Options (`calcFloat[7]`) | Earliest wheel/body vs. environment contact |
