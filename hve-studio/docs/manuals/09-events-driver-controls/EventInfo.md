# Event Information Dialog Box

The **Event Information** panel creates and edits events: it names the event,
chooses the calculation method, assigns the vehicles and humans that take part,
and holds each vehicle's initial conditions (or, for EDCRASH, its impact
reconstruction setup).

Open it from **Event › Event Information...** in the Event editor (F5). It is a
dockable panel (by default it shares a dock with the **Simulation** panel). Its
body is a list of collapsible sections; drag a section header onto another to
reorder them. Right-click a section header for **Move up**, **Move down**,
**Hide this section**, **Show all sections** and **Reset order**. Use
**Sections...** at the bottom to tick which sections are shown (the only way
back once every section is hidden), or for **Show all** and **Reset order**.

![Event Information panel for a SIMON event](images/hvn-event-info.png)

!!! note "HVE Studio"
    HVE's Event Information was a modal dialog used when creating an event,
    with separate Humans and Vehicles lists and a list of selected objects. In
    HVE Studio it is a panel that stays open, edits the active event directly,
    and also carries the initial conditions that HVE kept in the
    Position/Velocity dialog. While the active event's results are on screen
    its inputs are locked (a banner says so); **Reset** the run to edit them.
    Choosing a different event, adding an event and collapsing sections stay
    available while locked.

## Events

**Active Event** — a drop-down listing every event in the case as
*name [method]*. Choosing one makes it the active event; every Event-menu
dialog edits the active event.

**+** adds a new event (named *Event n*, with the active event's calculation
method) and makes it active. **−** deletes the active event; the remaining
events are renumbered. An event cannot be deleted while results for it are on
screen.

## Event (Event Name)

**Name** — the event's name. HVE Studio does not generate a name from the
selected objects; a new event is named *Event n*.

**Start time (s)** — the time shown at the event's start, for example −5 so
that the impact reads near 0. The results, the graphs, exported output, the
event's playback bar and the Results HUD read the event's clock, and a new
Playback track is placed at it. The run itself is unchanged: the engine still
integrates from 0. *(New in HVE Studio.)*

## Calculation Method

**Method** — a drop-down list of the calculation methods: EDCRASH, EDSMAC, EDGEN,
EDHIS, SIMON, EDSMAC4, GATB, EDSVS, EDVDS, EDVTS, SINGLETRACK, EDVSM and
READDATAFILE. The calculation method selects the physics engine that runs the
event.

- A method whose output has not yet been validated end to end in HVE Studio is
  marked *(unvalidated)*, and a line under the list says so for the active
  event.
- A method that cannot run the event's current vehicles (wrong number of
  vehicles, axles or connections) stays selectable but is marked
  *— N/A for these vehicles*; hover it for the reason. If the active event's
  method cannot run, a red *Cannot run:* line gives the reason.
- An event imported from an HVE case that uses a program HVE Studio does not have
  shows that method greyed and marked *— not ported*; it can be opened and
  saved but not run.

Unlike HVE, the method of an existing event can be changed at any time.

**Physics** — which physics runs the event:

- **HVE** — the physics as it now stands (the default).
- **HVE-reference** — the same engines frozen as they were validated against
  original HVE, run by their own solver program (`hve-solver-reference.exe`
  beside the program). Where that program is not present, or in the browser
  version, a red *Cannot run:* line says why.
- **HVE (imported)** — solves nothing: **Run** plays original HVE's own saved
  run of this event. Only a `.hve` saved after the event was executed carries
  one, and only while the case is open from that file; otherwise a red *Cannot
  play:* line says why.

Results solved by one are not the other's. **Output › Compare Runs...** runs
the event with two of them and compares the runs (see
[Compare Runs](../hve-users/02-menu-reference/04d-output-menu.md#compare-runs)).
*(New in HVE Studio.)*

**Method Options...** opens the active method's calculation options window
(see [Calculation Options](../10-calculation-options/README.md)). EDSVS, EDVDS,
EDVTS and READDATAFILE have no options window; the button is greyed for them.

!!! warning "Not in HVE Studio"
    HVE located the calculation-method programs in its calcMethods directory.
    HVE Studio has all the engines built in; there is nothing to install or
    browse for.

## Road Surface Search

How the engine searches the terrain polygons under each tire (HVE's Get Surface
Information options, which HVE Studio keeps per event):

- **Default for this method** — tracks the previous polygon (HVE's own default
  for the simulation engines).
- **All triangles - first hit in file order** — HVE's *From First Polygon*. On a
  site with stacked or adjacent surfaces the first hit is arbitrary.
- **Track the previous polygon** — HVE's *From Previous Polygon*.
- **Track the previous polygon, friction zones first** — HVE's *From Previous
  Polygon, Sorted*.

The control is disabled for EDCRASH, EDGEN, EDHIS, GATB and SINGLETRACK, which
do not drive on the road surface through this search.

!!! warning "Not in HVE Studio"
    HVE's *By Elevation* method and its search **Direction** settings (All
    Directions / Upward Facing Only / Z Component Greater Than) are not offered.

## Vehicles in Event

One row per vehicle **slot** (V1, V2, ...). The slot order is the object
numbering the engine uses; for EDVTS and EDVDS slot V1 is the tow vehicle.

- Click **V***n* to select that vehicle (the viewport selection and the gizmo
  follow).
- The drop-down in each row chooses which case vehicle occupies the slot.
  Changing it **keeps** every input on the slot (position, speed, crush, tire
  blowout, wheel damage, tire-terrain settings) — use it for a what-if swap.
- **Remove** drops the slot after a confirmation; its inputs are discarded.
- **Add Vehicle** adds a case vehicle to a new slot. It is disabled once the
  method's maximum number of vehicles is reached. Below the method's minimum
  the event can be edited but not run, and a red line says how many more are
  needed.

## Humans in Event

Shown for EDHIS, GATB, EDGEN and SIMON events (for SIMON the occupants are
bookkeeping only; SIMON does not solve occupant motion). One row per human
slot (H1, H2, ...):

- The drop-down chooses the human; pedestrians are marked *(pedestrian)*. A
  human with no seeded body model is flagged *no body*.
- **Remove** drops the slot; **Pose** opens the Body Pose dialog for that human.
- **Occupies** — the vehicle the human rides in for **this event**, or
  *Pedestrian (no vehicle)*.
- **Seat X / Y / Z from CG** (an occupant), **Scene X / Y / Z** (an EDHIS or
  EDGEN pedestrian) or **X / Y / Z from vehicle CG** (a GATB pedestrian) — the
  human's position, in the units set in Preferences. A position measured from
  a vehicle's CG is a vehicle dimension (in, or m in metric); a **Scene**
  position is a site length (ft, or m), the same unit as the vehicle positions
  and the EDGEN path rows. Z is SAE (+ down).
- **Restraint (this event)** — None, Lap Belt, 3-Point Belt or Airbag + Belt.
  Shown for occupants in EDHIS and GATB events.
- On an EDGEN event, the human's **Scene path**: HVE's eight named positions,
  each ticked to use it, with **X**, **Y**, **Z, + down**, **Yaw (deg)**,
  **Pitch**, **Roll**, **Sideslip (deg)** (read only under EDGEN's 3-D Spline
  path model) and **Speed stated** / **Speed**. EDGEN moves the human through
  the ticked positions at the speed stated at each.
- A read-only note lists any armed self-contact pairs.

**Add Human** adds a case human. If no human is listed, the event takes every
human that has a seeded body; a note names them.

For EDHIS and GATB events a **Combined Contact Materials** header lists, and
lets you edit, the combined occupant/surface material for each interior contact
surface of vehicle slot 1 (force constant, linear, quadratic and cubic
stiffness, damping, friction, maximum force and deflection, unloading
stiffness, maximum penetration and edge constant).

## Vehicle Initial Conditions

For every method except EDCRASH this section is titled **Vehicle Initial
Conditions (*method*)** and replaces HVE's Initial path location in the
Position/Velocity dialog. One block per vehicle slot, headed *V*n* -- name*:

- **X Position**, **Y Position** (units set in Preferences) and **Heading (deg)**.
  Moving a tow vehicle carries its trailer; a trailer is kept on its hitch.
- **Auto Position (settle onto terrain)** — 3-D methods only. On, the engine
  settles the vehicle onto the terrain, and a line reports the resulting
  height, roll and pitch (or why it fell back to flat ground). Off, **Z Height**
  is entered directly. Planar methods always settle. For SIMON (HVE
  physics), the run also starts 2 s early and settles the vehicle in place on
  its suspension and tires before the event begins (see
  [SIMON Program Input](../programs/SIMON/02-program-input.md)).
- **This height is the SETTLED ride height** — SIMON only, with Auto Position
  off. Off (the default), SIMON applies its static tire deflection once; on, the
  entered height is already the settled elevation.
- **Speed**, **Sideslip β (deg)** and **Yaw rate (deg/s)**.
- **Measured rest position** (EDSMAC4 only) — **Rest position known**, **Rest X**,
  **Rest Y**, **Rest heading (deg)**.
- **Advanced initial state** — **Vertical vel w**, **Roll angle (deg)**,
  **Pitch angle (deg)**, **Roll rate (deg/s)**, **Pitch rate (deg/s)**. Roll and
  pitch take HVE's own range, ±1800°, so a vehicle can start on its roof (roll
  180°). A pitch within about 1° of ±90° is flagged: SIMON's and EDVSM's
  Euler-angle equations are singular there and the run may stop.

For an EDVTS trailer the X and Y positions are shown greyed (EDVTS derives them
from the hitch) and **Articulation (deg)** relative to the tow vehicle replaces
the heading.

**Only the selected vehicle** collapses the other vehicles' blocks (a view
setting, not saved with the case).

!!! tip "New in HVE Studio"
    **Seed from a previous run** chains events: it takes where the vehicles
    were in a solved event — at the end of the run or at a **Handoff time** you
    choose — and writes that as this event's starting position, heading and
    speed (**Seed Initial Conditions**). Vehicles are matched by vehicle, not by
    slot. Nothing else is copied.

## Vehicle Impact Setup (EDCRASH)

For EDCRASH the section is titled **Vehicle Impact Setup**, with one block per
vehicle. It carries the damage data that HVE entered in its Damage Data dialog
and the scene positions from its Position/Velocity dialog:

![Vehicle Impact Setup for an EDCRASH event](images/hvn-event-info-edcrash.png)

- **Impact Speed**.
- **CDC**, **PDOF (deg)** and **Auto-calculate PDOF (from the other vehicle)**.
  Only one vehicle may auto-calculate; if both do, EDCRASH refuses the event
  (stop code −5443).
- **Basis** (EES / Damage Profile) shown greyed, with the EES value: EDCRASH
  always reconstructs from the crush profile, and no engine reads the basis or
  the EES speed.
- **A Stiffness**, **B Stiffness**, and **Derive impulse center from damage
  profile** (uncheck to enter **Impulse Center X / Y**).
- **Scene positions** — HVE's eight named path locations (Initial, Begin
  Perception, Begin Braking, Impact, Separation, Point On Curve, End of Rotation,
  Final/Rest). Each one that is set is drawn as a ghost in the viewport. Impact
  and Final/Rest are edited in the fields below the list.
- **Scene positions known (impact + rest)** — with it on, **Impact X / Y /
  heading**, **Impact sideslip (deg)**, **Rest X / Y / heading** and **Velocity
  at rest**. With it off the run is a damage-only reconstruction (delta-V from
  crush alone).
- **Measured Crush** — number of crush depths, **C1**...**Cn**, **Damage width**,
  **Damage offset**, and per-zone A/B stiffness.

See [Damage Data](../11-reports-output/DamageData.md) for how these map to
HVE's Damage Data dialog, and [Position/Velocity](PosVelDlg.md) for what each
scene position does in EDCRASH.

## Lighting

A summary of the sun and sky used to light the 3-D view, with a link to where it
is edited. Display only; it stays editable while results are on screen.

<!-- NAV -->

---

← Previous: [Driver Controls Speed Follower](DriverControls8.md)  |  [Index](README.md)  |  Next: [Event Setup Menu](EventSetup.md) →

<!-- /NAV -->
