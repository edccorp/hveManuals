# SIMON Calculation Options

!!! note "HVE Studio"
    HVE's dialog reference has no page for SIMON's calculation options; this
    page documents HVE Studio's **SIMON Options** window. SIMON itself is
    described in the [SIMON program manual](../programs/SIMON/README.md).

In Event Information, with a SIMON event active, press **Method Options...**
under Calculation Method. The **SIMON Options** window opens. Changes take
effect immediately and are locked while the event's results are on screen.

## Time Settings

- **Duration (s)** and **Output Interval (s)** — the same values as *Duration*
  and *Output Timestep* in the [Simulation panel](../09-events-driver-controls/SimuCtrlDlg.md);
  editing either place changes both. An event that carries its own simulation
  controls (an imported HVE case does) runs with the Simulation panel's values,
  so edit them there.

## Integration

**Method** is shown greyed at *Fixed Runge-Kutta* and marked *(inert)*. SIMON
always integrates with a fixed-step Runge-Kutta method, in HVE as well as in
HVE Studio, whatever a case stores; an imported case's stored value is left as
the file has it. To change the step size, use *Trajectory Timestep* in the
Simulation panel.

!!! note "HVE Studio"
    The simulation clock is the exact sum of the steps taken, accumulated in
    double precision. HVE rounds its single-precision clock to the nearest
    integration step after each step, which can place an output frame or the
    start of a contact a fraction of a step off the grid; HVE Studio does not.
    The physics programs also compute in double precision (HVE: single), so
    an HVE Studio result differs from HVE's by rounding where everything else is
    equal; the knife-edge cases that rested in two different places on two
    machines are the ones that move.

## Steering Degree of Freedom

- **Off - prescribed steer table only** (default) — the road-wheel angles follow
  the driver steer table for the whole run, so a blown tire, damaged wheel or
  curb strike cannot pull the steering.
- **Normal - steer is free from t=0 (table ignored)** — the wheels find their
  own angle from the tires' aligning moments for the whole run; the driver steer
  table is ignored.
- **Append - follow the table, then free** — the steer table is followed to its
  end, then the steer degree of freedom takes over.
- **Auto start - free at first contact** — the steer table is followed until the
  first collision contact, then the steer degree of freedom starts with the
  current steer angle. Useful for modeling a driver's loss of steering control
  at impact.

## Tire model

**Semi-empirical V3** or **TMeasy (Rill)**.

- **Semi-empirical V3** — EDC's semi-empirical tire model, latest version. HVE's
  own default for a new event, and what a case reads when its file states no tire
  model. HVE also has V1 and V2. The versions agree on
  gentle forward maneuvers and differ at large slip angles and in reverse (V1
  uses sin of the slip angle where V2 and later use tan, V2 and later tie the
  lateral-force sign to the direction of travel, and V3 also clamps μ to its
  peak and softens cornering and camber stiffness at low wheel speed). The list
  does not offer V1 or V2, but a case imported from HVE that states one (cases
  saved by older HVE versions commonly store V2) runs it as HVE did, and the
  window says so; choosing from the list changes it.
- **TMeasy (Rill)** — the default for a new event in HVE Studio: one added with
  **+** in Event Information or built by Case Intake. A case imported from HVE
  keeps the model its file states. G. Rill's TMeasy tire model: a force
  curve in each direction (initial slope, peak, sliding) built from the tire
  inputs, with braking and cornering combined on one normalised slip. It uses
  three shape inputs of its own, the **TMeasy** rows of the Tire Properties
  table (see [TMeasy rows](../05-tires-wheels/TirePhyDataDlg.md#tmeasy-rows)).

## Hydroplaning

**Off** (default), **NASA**, **NASA-TTI**, **Gallaway** or **Blythe-Day (refuses
the run)**. Each model replaces each tire's friction multiplier with the
hydroplaning model's output every timestep; the models differ in the speed at
which each tire is predicted to hydroplane. See
[SIMON — Hydroplaning Model](../programs/SIMON/04-calculation-method.md#hydroplaning-model).

The models need standing water: a **Water Depth** stated on a surface (its
HVE Surface node in the Shader Editor), or, for ground with no surface of its
own, on the Environment panel's Default surface material. The window warns
when no surface states any standing water.

!!! warning "Refused by the engine"
    **Blythe-Day** is listed by HVE but not implemented by SIMON (in HVE either).
    An event that selects it does not run: SIMON refuses it at input with stop
    code −5520. HVE Studio offers it, marked, so that an imported case stating it
    shows why the run refused.

## Solid Axle Inertia

**Use Axle Only** or **Use Axle + Wheels** (default for a new event). Whether
each solid axle's roll inertia includes the wheels on it: *Use Axle + Wheels*
adds each wheel's parallel-axis term to its axle's roll inertia, which stiffens
the axle's roll response. Independent suspensions are skipped, so on a vehicle
with no solid axle the choice changes nothing; the window says how many solid
axles the event's vehicles have.

## Collision history and connections

**Accident history basis** — **Impact force** (default) or **Total acceleration**,
with **Threshold (g)** enabled only on Total acceleration (0 means the
environment's gravity, 1 g). This sets where SIMON considers the collision to
have ended, and so the window over which the PDOF and collision ranges in the
key results are accumulated. Under Total acceleration the collision also ends
once both vehicles' resultant acceleration falls below the threshold, even while
they are still touching.

!!! note "HVE Studio"
    EDSMAC4 has the same option, stored with the **opposite** meaning. Each
    window is labelled for its own engine; choose by the label.

**Connection constraint** — **Use both vehicles**, **Use heavier vehicle**
(default) or **Use tow vehicle properties**. The first two derive the hitch spring
and damper rates from the two units' sprung masses; the third takes them from
the tow vehicle's *Vehicle Connections › Properties* stiffness and damping.

**Connection failure start (s)** — the hitch is held together for this long
whatever the load (default 0.1 s). It has an effect only when the hitch has a
finite breakaway force or torque (0 there means it cannot fail).

Both apply only to an articulated pair and have no effect on a single vehicle.

## DyMESH (mesh-to-mesh collision)

**Enable DyMESH** collides the vehicles' body meshes instead of using the
crush-profile model. Every vehicle in the event needs a mesh file; a vehicle
without one collides as an 8-corner box, and the window says how many vehicles
are in that state.

With DyMESH enabled:

- **Smoothing** — **Version 1** or **Version 2**, HVE's names; both detect
  contact. Version 1 cannot be used with DyMESH wheel contact (**Event ›
  Wheels**): such a run is refused. A case that stores a value HVE would also
  print as Version 2 but at which DyMESH finds no contact is run as Version 2,
  and the window and the run status say so.
- **Search option** — **Automatic (size from the mesh)** or **Set box size**;
  **Search box** is the box size, read only with *Set box size*. A box that is
  too large for a detailed mesh makes the run refuse to start; Automatic
  cannot overflow.
- **Contact friction**, **Relaxation length**.
- **Force contact to the XY plane**, **Include the environment**.
- **Contact a vehicle's own trailer** — off (HVE's default) skips the pair of a
  tow vehicle and its own trailer.
- **Start time (s)**, **Environment start time (s)** — before these times DyMESH
  does not detect contact.

The complete DyMESH settings, including per-pair friction and relaxation
overrides, are in **Event › DyMESH Options...**.

!!! note "HVE Studio"
    In the DyMESH Options dialog the third search option, *Search all vertices
    (refuses the run)*, stops the run at setup (stop code −5400), in HVE as
    well. Several
    of HVE's DyMESH selectors — *Stop Search After*, *Search Method*,
    *Inside-Vehicle Test*, *Inside-Polygon Test*, the pushback direction and
    some restoration options — are carried to the engine but read by nothing,
    in HVE as well; the dialog labels them *Carried, not consumed*.

!!! note "HVE Studio"
    The DyMESH collision model has been updated in HVE Studio: every
    vehicle's wheel positions, tire and suspension forces are computed
    before the collision pairs, and the forces a DyMESH wheel passes to its
    vehicle are accounted for once. A case that involves DyMESH contact,
    and in particular contact with a DyMESH wheel, will give a different
    outcome than the existing HVE version. The result does not depend on
    the order in which the vehicles are listed, nor on the number of
    processor cores the calculation runs on: SIMON's DyMESH sweeps use every
    core of the machine and give the same answer on any count.

## Termination Velocity

**Linear** (units set in Preferences) and **Angular (rad/s)** — SIMON's stored
termination velocities. They are used only when the
[Simulation panel's](../09-events-driver-controls/SimuCtrlDlg.md) *Termination*
values are not set; the Simulation panel's values take precedence.
