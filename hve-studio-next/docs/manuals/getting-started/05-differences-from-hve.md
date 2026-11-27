# Differences from HVE

This page lists, in one place, where HVE Studio is not HVE: the interface, the
deliberate changes to the physics, options the programs refuse, what
HVE Studio adds, and what it does not have. Everything not listed here behaves as
HVE does.

## User interface differences

| In HVE | In HVE Studio |
| --- | --- |
| Separate Human, Vehicle, Environment, Event and Playback editors | Five tabs under the menu bar: **Human (F2)**, **Vehicle (F3)**, **Environment (F4)**, **Event (F5)**, **Playback (F6)**. The menu bar shows the menus of the active tab. See [Interface Tour](03-interface-tour.md#editor-tabs) |
| Playback Editor with report and playback windows | The **Playback (F6)** editor plays several solved events on one timeline: its **Playback** menu has Playback Sequence, Playback Options and **Run All Events**, which solves every event the sequence uses. One event also plays back where it is set up: **Run** on the playback bar under the Event editor's viewport. Reports, graphs and tables are on the Event editor's **Output** menu (Key Results, Output Graph, HVE Reports — which holds the Accident History — and Export Variables); Key Results, the Results HUD and Output Graph are also on the **View** menu in every editor |
| Video Creator (several events on one timeline, written to video) | The **Playback (F6)** editor's timeline (above) takes the Video Creator's place; **File › Record Animation** writes the 3-D playback to a Motion-JPEG AVI — through any saved camera, between the start and end times you choose, in real time or slow motion, with the [Results HUD](../new-features/11-results-hud.md) burned in if you wish — and **File › Play Video** plays one; Record Animation can also **ray-trace** every frame (and add motion blur), and **File › Render Image (Ray Traced)** makes a still; for full control of a render, use Blender with the glTF export or the Blender Live Link (see [Video and Playback Sequences](../new-features/07-video-and-playback-sequences.md)) |
| Options menu: show/hide velocity vectors, skidmarks, targets, paths… | **View › Scene Display** panel: Vectors (Velocity, Acceleration, Collision force and moments, Tire Fx', Fy' and Fz'), Skidmarks, CG Path, Accelerometer Path, Tire Contact Patch Paths, **Scene Ghosts** (HVE's targets, drawn as outlines, translucent vehicles or both), Axes (the origin's, and each vehicle's at its CG), North Arrow, Vehicle Extents |
| Render dialog (Phong, Flat, Wireframe, Hidden Line; light sources) | **View › Scene Display › Rendering**: Phong, Flat, Wireframe, Light Sources On. Hidden Line is not offered: in this renderer it would draw the same picture as Wireframe |
| Camera Setup | **Tools › Cameras** — saved cameras and a Viewport View tab in one dialog; the **Camera** button under the viewport's view cube (click to look through the scene camera, right-click for Camera Properties) and the viewport's right-click menu; **C** / **Shift+C** cycle cameras |
| Units dialog (US, SI, Custom) | **Options › Preferences › Units**: Imperial or Metric. No custom mix |
| 3-D editor manipulators | A gizmo, plus Blender-style keys: **G** move, **R** rotate, **X/Y/Z** axis lock, typed values, **Ctrl** snap. See [Interface Tour](03-interface-tour.md#moving-objects-the-gizmo) |
| Path Follower | **Event › Path Follower** — it is per event and per vehicle, so it is on the Event menu, not the Vehicle menu |
| Body Torsion | **Vehicle › Editors › Body Torsion** (a property of the vehicle, whichever event is open) |
| Transform Vehicle Geometry, Move CG of the geometry | **Vehicle › Editors › Vehicle Mesh** (also offered on the Event menu): scale, move and rotate the body, and its other mesh options; Move CG is on the Vehicle Designer's **Size, Mass & CG** stage |
| Use Ackermann Steering, set per event in Driver Controls | Ackermann / parallel steer is chosen in the vehicle's **Steering System** |
| Contact surfaces, airbags, belts | **Vehicle › Editors › Contact Surfaces**, **Airbags**, **Belt Restraint**; per event, **Event › Restraints** |
| GEBOD Human Information | **Human › Human Information** (the Humans panel) |
| Damage Studio | **Output › Damage Studio Options** and **Damage Studio Report**; crush is drawn on the vehicle's 3-D body as the run plays |
| Impact Plane / Barrier (EDCRASH) | Grayed in the Event menu. Model a barrier as a vehicle of type **Fixed Barrier** (Vehicles panel, Identity) |
| An input a program does not use is grayed | The same, and in addition HVE Studio says **why** where it matters (for example, which program reads a field) |
| Inputs are read-only while an event's results are shown | A solved event's inputs, its vehicles and the site stay editable. The results stay on screen and are marked **out of date** (a note naming what changed, and a count in the window title) until the event is run again; **Restore inputs as run** puts back the inputs the run used. Deleting or reordering vehicles, deleting humans, Quick Case, and an Undo step that changes a solved event's inputs still wait for **Reset**. To keep the old behavior, turn on **Lock inputs while results are shown** in **Options › Preferences** (see [Options Menu](../hve-users/02-menu-reference/06-options-menu.md)) |
| `.hve` case files | `.hvex` or `.json`; `.hve` files open directly but are not written. Like a `.hve`, a saved case carries its site (geometry and aerial photograph) inside it; **File › Embed the environment in the case** turns that off for a case that should only name its site file. See [Cases and Files](04-cases-and-files.md) |

Most of HVE's dialogs are ported field for field. Where a dialog page in this
manual set describes a field HVE Studio does not have, the page marks it
**Not in HVE Studio**.

## Physics differences by design

HVE Studio runs HVE's own physics source. A number of calculations were changed
on purpose, each where HVE's form can be shown to be wrong: a vehicle at rest
that does not stay at rest, a force counted twice, a step that overshoots. Every
change is recorded with its evidence, and each is listed below. To see what
HVE would have answered, set an event's **Physics** to **HVE-reference**: the
same programs as they were validated against HVE's saved results, in HVE's
single precision and without the changes below except the per-vehicle path
follower and the differential types. **Output › Compare Runs...** solves an
event both ways and shows the differences (see
[Event Information](../09-events-driver-controls/EventInfo.md#calculation-method)
and [Compare Runs](../hve-users/02-menu-reference/04d-output-menu.md#compare-runs)).

### Changes that affect every run of a program

**Double precision (every program).** HVE's programs compute in single
precision; HVE Studio's compute in double. Results differ in their last digits,
and a case that sits on a knife edge (two vehicles that barely touch, a vehicle
that barely tips) can part from HVE's answer. The HVE-reference physics keeps
HVE's single precision.

**SIMON wheel spin.** Each wheel's spin is stepped semi-implicitly, using the
tire model's own slope, in at least 16 sub-steps per step. HVE's explicit step
overshot on a settled wheel and made the tire force swing by its own size
between evaluations, which showed as a low-speed chatter in braked stops.
Every SIMON run moves: on EDC's cases braked stops end up to about 0.35 m
longer, and launches from rest are up to 6% slower at the case's time step.

**SIMON static axle loads on a combination vehicle.** The static axle loads are
computed from the rear unit forward, as HVE's original code did, so a trailer's
kingpin load reaches its tow vehicle's axles, suspension and hitch at the start
of the run. In current HVE that load is dropped, and a tractor-trailer at rest
started with a nearly unloaded hitch and moved as the run began. Every
articulated SIMON event moves; a rig at rest now starts at rest.

**EDVDS tandem-axle load equalizer.** On a tandem axle with a load-equalizing
(four-spring) suspension, HVE applies the whole load-leveling correction at
every evaluation. HVE Studio does the same at ordinary time steps, but below a
5 ms step it spreads the correction over 5 ms, because at very small steps
HVE's form oscillates until the run aborts. On EDC's tandem-axle validation
cases and the EDVDS tutorial the results lie within about 2.5 cm of HVE's saved
results; two of HVE's tutorial lessons are sensitive enough to the time step
that neither HVE nor HVE Studio gives a repeatable answer for them. See the
[EDVDS manual](../programs/EDVDS/README.md).

**GBF stopping distance.** The units move along the lead unit's heading as the
stop proceeds (HVE drew them standing at the start), the last step ends on the
termination speed instead of overshooting it, and *find the speed* matches the
stated distance against the whole stop, including the first half second. See
the [GBF manual](../programs/GBF/README.md).

### Changes that affect particular situations

**Path follower switched off per vehicle at impact (SIMON and EDSMAC4).** In
HVE the first collision anywhere in an event turns off the driver model (path
follower) of **every** vehicle. In HVE Studio a collision turns off the follower
of the vehicles that collide; a following vehicle not involved in the
collision keeps following its path. Results differ only in a multi-vehicle
event with a path follower on a vehicle that is not in the collision — no case
in EDC's corpus is such a case. See the [SIMON](../programs/SIMON/README.md)
and [EDSMAC4](../programs/EDSMAC4/README.md) manuals.

**A stopped vehicle (SIMON).** HVE froze a vehicle it judged stopped by zeroing
its velocities at every step. HVE Studio does not: the tires hold a vehicle at
rest on its wheels, and DyMESH holds one resting on its body. No vehicle is
judged stopped in the first 0.1 s of a run, which is what the shipped HVE
build does (HVE's source uses two time steps).

**A vehicle on its side or roof (SIMON with DyMESH).** Against the site, a
DyMESH node reloads gradually as it is pushed back in, and holds by static
friction until it slides. In HVE an overturned vehicle hopped on its roof and
crept down a slope. Between two vehicles, contact is as in HVE. A tire pushed
past 1.2 times its maximum deflection while the body is in contact with the
site bottoms out and the run continues; HVE stopped the run (message -6910).
The run status says when this happens.

**Curbs and DyMESH wheels (SIMON).** A tire's sidewall springs meet any steep
face, even a curb whose surface is typed as road; HVE tested only surfaces
typed as curb. A DyMESH wheel's tire is a ring of radial springs that turns
with the wheel, so it sees a curb's face. See
[DyMESH: wheels and the environment](../programs/DyMESH/05-wheel-environment.md).

**A wheel's collision moment (SIMON with DyMESH).** The yaw moment of a
collision force on a wheel is counted once. HVE counted it twice for the
second vehicle of each contacting pair.

**A blown tire (EDVSM).** Past the blow-out, the tire keeps its intact
secondary stiffness and loses only the air spring. HVE's expression made the
tire stiffer than intact while it deflated.

**A flat (zero-area) triangle in the site (every program).** A triangle with
no plan area is not ground. HVE treated it as ground along its line, or
everywhere when its corners coincide. The run status counts any such
triangles a run met.

**Airbags (GATB).** The bag inflates and acts on the occupant, and a vented bag
shrinks as it loses gas. In ATB as HVE runs it, the bag never inflates. See
[GATB Program Input](../programs/GATB/02-program-input.md).

### A choice HVE did not offer

**Differential type (SIMON).** HVE stores a differential type (Open,
Limited Slip, Locked) but grays the control and solves every differential as
open. HVE Studio's **Drivetrain** dialog enables the type, and SIMON applies a
torque bias for Limited Slip and Locked. **Open** gives HVE's answer, and every
vehicle imported from HVE is open.

!!! note "HVE Studio"
    Besides these, a few changes stop a run that HVE would hang or crash on:
    the run ends with an error message instead. They do not change the result
    of a run that completes.

## Options the programs refuse

HVE offers some options that its own physics programs do not implement. HVE Studio
offers them too (an imported case may state them) but **marks them in the
list**, and the program stops the run with an error message rather than quietly
running something else:

| Where | Option | What happens |
| --- | --- | --- |
| SIMON Method Options › Hydroplaning | Blythe-Day *(refuses the run)* | SIMON implements Off, NASA, NASA-TTI and Gallaway |
| EDSMAC4 Method Options › Hydroplane Model | NASA-TTI, Gallaway *(not supported by EDSMAC4)* | EDSMAC4 implements Off and NASA |
| Vehicle › Editors › Brakes › ABS / Brake Design › ABS algorithm | Algorithm 3, 5 and 6 *(not implemented)* | The run stops when the ABS first acts. Tire Slip, Bosch Version 1 and Algorithm 4 are implemented |
| EDCRASH Method Options › Separation Velocity Basis | Iterate on Sideslip | EDCRASH refuses it. Normal, Trajectory Simulation and Sustained Contact work |
| Event › DyMESH Options › Search Option | Search all vertices *(refuses the run)* | Automatic box size and Set box size work |

!!! warning "Not in HVE Studio"
    GATB's **Use external ATB input file** is shown grayed. HVE Studio passes the
    ATB input to the solver directly, not through a `GATB.ain` file, so an
    external file cannot reach it.

## New in HVE Studio

!!! tip "New in HVE Studio"
    Each of these is an addition; none of them changes a case that does not
    use it.

| Feature | Where | What it does |
| --- | --- | --- |
| Single-track (motorcycle) program | Calculation Method **SINGLETRACK**; **Tools › Motorcycle Analysis** | A motorcycle model with lean as a degree of freedom, countersteer, load transfer and pitch-over, validated against the published benchmark. HVE's programs can only approximate a two-wheeler as a narrow four-wheeled vehicle |
| Lean command (SIMON motorcycle) | **Event › Driver Controls › Lean** tab (shown for a motorcycle) | The lean the single-track rider holds while the machine rides the single-track model, until its first contact; SIMON has no forced lean |
| Path follower through impact (SIMON, EDSMAC4) | **Event › Path Follower › Keep following through an impact** | Keeps a vehicle's path follower active after it collides. Off by default, and always off in a case imported from HVE |
| Per-axle steer degree of freedom (SIMON) | **Vehicle › Editors › Steering System**, Steer DOF (SIMON) | Sets SIMON's steer degree of freedom — Normal (free), Append (free after the table) or Auto start (free at contact) — for each axle separately, instead of one setting for the whole event; for example, a free castoring axle |
| Limited-slip and locked differentials (SIMON) | **Vehicle › Editors › Drivetrain** | See [Physics differences](#physics-differences-by-design) |
| HVE-reference physics and Compare Runs | Event Information › **Physics**; **Output › Compare Runs...** | Solves an event with the programs as they were validated against HVE (or plays HVE's own saved run of an imported event) and compares the two runs channel by channel. See [Physics differences](#physics-differences-by-design) |
| Monte Carlo analysis | **Event › Monte Carlo** (the Event Designer's Results stage) | Keeps a list of analyses per event, saved with the case, each drawn in the 3-D view in its own colors. Each runs the event many times with uncertain inputs (Normal, Uniform, Triangular or Lognormal; Random or Latin Hypercube sampling) through the real physics programs, and reports confidence intervals, sensitivity and convergence, with a CSV, an HTML report and an audit record |
| Quick Case | **Tools › Automatic Tools › Quick Case (Text)** | Builds a case from a typed sentence, such as "SIMON event, vehicle 1 at (0,0) heading 0 speed 50 mph, vehicle 2 at (12,-3) heading 180 speed 30 mph", with a preview before it is applied |
| Vehicle Package | **Tools › Automatic Tools › Vehicle Package** | Builds a case vehicle from its VIN (checked offline, or decoded by NHTSA on request) or year, make and model: the matching database record, or a generic scaled to the vehicle's stated weight, dimensions and CG height; with its occupants (GEBOD) and cargo. See [Case Intake and Vehicle Data](../new-features/12-case-intake-and-vehicle-data.md) |
| Case Intake and Provenance | **Tools › Automatic Tools › Case Intake**, **Tools › Automatic Tools › Provenance** | Builds an event from what the case documents state, typed in with where each value is stated (HVE Studio sends nothing anywhere), and keeps, with the case, where every value these tools set came from: stated, looked up, estimated, a generic's default or unknown |
| Occupants and cargo aboard a vehicle | **Inertia / Mass** dialog, *Aboard* | A load the vehicle carries into every event and engine, added to its mass, CG and inertia, or handed to SIMON and EDVDS as payload. An occupant can be a human from the Human editor: drawn seated in the vehicle, its weight added in the vehicle programs (once, in SIMON), and seated there by default for EDHIS and GATB |
| Crush stiffness from crash tests | **Tools › Automatic Tools › Crush Stiffness from Crash Tests**, or **Vehicle › Editors › Crush Stiffness › From crash tests** | CRASH3 A and B from staged barrier tests, typed in, read from an NHTSA test file or fetched from NHTSA's database by test number, put on a side of the vehicle and on its EDCRASH events |
| EDR import | **Tools › Automatic Tools › EDR Import** | An event data recorder's pre-crash record (from the report's PDF or tables, or typed in) into an event vehicle's initial speed and driver-control tables; for SIMON, the driver solved to follow the recorded speed; and the recorded yaw rate, accelerations and delta-V against the run's |
| Node materials | **View › Shader Editor** | Blender-style material graphs for vehicles, road surfaces and the sky. Display only: a surface's friction stays in the Environment editor |
| Keyframes | **View › Dope Sheet**; **I** in the viewport | Animate material values and cameras over the playback time. Display only |
| Blender | **File › Export Scene for Blender** (glTF), **File › Blender Live Link** | Take the solved scene into Blender; the live link updates the objects already in Blender after each re-run, keeping the materials and cameras set up there |
| Publish Bundle, viewer and web builds | **File › Publish Bundle**; see [Installing and Running](02-installing-and-running.md) | Share a solved case as a folder or a link, viewable without an installation |
| Outliner, undo history list | **View › Outliner**, **Edit › Undo History** | HVE has Undo and Redo; the list of edits, any of which can be returned to, is new. See [Interface Tour](03-interface-tour.md) |

## Not available in HVE Studio

!!! warning "Not in HVE Studio"
    - **Writing `.hve` files.** Cases are saved as `.hvex` or `.json`.
    - **Calculation programs HVE Studio does not have.** An event whose program is
      not one of HVE Studio's opens, keeps its inputs, and does not run; the run
      status says so. (Read Data File runs: it replays the event's data file.)
    - **The Impact Plane / Barrier dialog** (EDCRASH). Use a Fixed Barrier
      vehicle.
    - **HVE's Distance Tool.**
    - **Hidden Line rendering** and **custom units**.
    - **Traffic signals** (the environment's signals and their timing in an
      event).
    - **Saving an edited vehicle into a database.** Vehicle › Save Vehicle As
      copies the database record the vehicle was loaded from, under new keys;
      changes made to the vehicle in HVE Studio are saved with the case, not in
      the database. See [Saving Vehicles](../02-vehicles/VehSaveAs.md).

For the physics behind every program, see the program manuals:
[EDCRASH](../programs/EDCRASH/README.md), [EDSMAC](../programs/EDSMAC/README.md),
[EDSMAC4](../programs/EDSMAC4/README.md), [EDGEN](../programs/EDGEN/README.md),
[EDHIS](../programs/EDHIS/README.md), [SIMON](../programs/SIMON/README.md),
[DyMESH](../programs/DyMESH/README.md), [EDSVS](../programs/EDSVS/README.md),
[EDVDS](../programs/EDVDS/README.md), [EDVTS](../programs/EDVTS/README.md),
[EDVSM](../programs/EDVSM/README.md) and [GATB](../programs/GATB/README.md).
