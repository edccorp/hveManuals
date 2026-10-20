# Simulation Controls Dialog Box

In HVE Studio the simulation controls are the **Simulation Controls** group at the
top of the **Simulation** panel, which also holds the **Run** controls and a
summary of the last result. Open it from **View › Simulation**, or with
**Output › Run Simulation...**; by default it is docked beside Event
Information.

The values belong to the active event. *Event-owned* is shown when the event
(for example an imported HVE case) states its own duration or timesteps. The
controls are locked while the event's results are on screen; **Reset** to edit
them. Each value is typed or dragged; there are no sliders.

!!! note "HVE Studio"
    Only the timesteps and tests the active event's engine actually reads are
    shown. A line says which timesteps the method does not use, and the
    convergence controls appear only for methods that read them.

## Integration Timesteps

- **Duration (s)** — the maximum simulation time (HVE's *Maximum Time*, which HVE
  listed under Termination Conditions).
- **Trajectory Timestep (s)** — integration timestep for the trajectory phase
  (HVE's *Vehicle Trajectory*).
- **Collision Timestep (s)** — integration timestep for the collision phase
  (HVE's *Vehicle Collisions*). EDSMAC and EDSMAC4 use it for the collision and
  separation phases; SIMON switches to it for any step in which an impact is
  detected. 0 means derive it. Shown for SIMON, EDSMAC and EDSMAC4.
- **Separation Timestep (s)** — integration timestep for the start of the
  post-impact phase (HVE's *Vehicle Separation*). 0 means use the collision
  timestep. Shown for EDSMAC and EDSMAC4.
- **Curb Impact Timestep (s)** — EDVSM's curb-impact integration timestep
  (HVE's *Curb Impact*); with EDVSM's steer degree of freedom on, the run
  integrates at it. 0 means use the integration timestep. Shown for EDVSM.
- **Human Collision Timestep (s)** — EDHIS's integration timestep, and EDGEN's
  when the event moves a human (HVE's *Human Collisions*). HVE's tutorial
  occupant events use 0.0002 s. 0 means use the output timestep. Shown for EDHIS
  and EDGEN. (GATB ignores it, as in HVE: its ATB step is fixed.)
- **Output Timestep (s)** — how often results are sampled for the trajectory,
  Key Results and playback (HVE's *Output Time Interval*).

## Termination

**Termination** (collapsible) ends the run once every vehicle is below both armed
limits:

- **On** + **Linear** — minimum linear velocity (units set in Preferences).
- **On** + **Angular (deg/s)** — minimum angular velocity.

With both off the run always integrates to the full duration.

!!! tip "New in HVE Studio"
    **Stopped Vehicle** (collapsible) sets the **Linear** and **Angular (deg/s)**
    speeds below which a vehicle is *reported* at rest. These are separate from
    the termination limits; left at zero they track the termination limits
    plus HVE's margin.

## Integrator Convergence

Shown only for the methods that read these (EDSVS, EDVDS, EDVTS and EDHIS):

- **Maximum Bisections** — how many times the integrator may halve its step
  before giving up; exceeding it ends the run with an integration error. HVE's
  default is 12.
- **Velocity Convergence** — the error bound the corrector must meet before a step
  is accepted. HVE's default is 0.12.
- **Velocity Change Limit** and **Acceleration Change Limit** — EDHIS only.
  0 turns that test off, which is HVE's default for both.

!!! note "HVE Studio"
    SIMON and EDSMAC4 read none of the convergence controls (SIMON always
    integrates with a fixed-step Runge-Kutta method), and EDVSM uses its own
    integrator, so the group is hidden for them.

## Run and Last Result

Below the controls, **Run** starts the active event (with progress, cancel and
**Reset**), and **Last Result** shows the run status and each vehicle's delta-V
and PDOF.

<!-- NAV -->

---

← Previous: [Position/Velocity Dialog Box](PosVelDlg.md)  |  [Index](README.md)

<!-- /NAV -->
