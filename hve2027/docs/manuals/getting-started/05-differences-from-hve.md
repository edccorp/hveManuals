# Differences from HVE

This page lists, in one place, where HVE 2027 is not HVE: the interface, the
three deliberate changes to the physics, options the programs refuse, what
HVE 2027 adds, and what it does not have. Everything not listed here behaves as
HVE does.

## User interface differences

| In HVE | In HVE 2027 |
| --- | --- |
| Separate Human, Vehicle, Environment and Event editors | Four tabs under the menu bar: **Human (F2)**, **Vehicle (F3)**, **Environment (F4)**, **Event (F5)**. The menu bar shows the menus of the active tab. See [Interface Tour](03-interface-tour.md#editor-tabs) |
| Playback Editor with report and playback windows | No separate editor. **Run** on the playback bar under the Event editor's viewport; the solved event plays back in the same viewport. Reports, graphs and tables are on the **Output** menu (Key Results, Output Graph, Timestep Data Table, Variable Report, Accident History Report, HVE Reports) |
| Video Creator (several events on one timeline, written to video) | The **Playback (F6)** editor builds a timeline from several solved events; **File › Record Animation** writes the 3-D playback to a Motion-JPEG AVI — through any saved camera, between the start and end times you choose, in real time or slow motion, with the [Results HUD](../new-features/11-results-hud.md) burned in if you wish — and **File › Play Video** plays one; Record Animation can also **ray-trace** every frame (and add motion blur), and **File › Render Image (Ray Traced)** makes a still; for full control of a render, use Blender with the glTF export or the Blender Live Link (see [Video and Playback Sequences](../new-features/07-video-and-playback-sequences.md)) |
| Options menu: show/hide velocity vectors, skidmarks, targets, paths… | **View** menu: Vectors (Velocity Vectors, Collision Force (PDOF), Tire Force Vectors), Skidmarks, CG Path, Accelerometer Path, Tire Contact Patch Paths, **Scene Ghosts** (HVE's targets, drawn as outlines, translucent vehicles or both), Axes (the origin's, and each vehicle's at its CG), North Arrow, Vehicle Extents |
| Render dialog (Phong, Flat, Wireframe, Hidden Line; light sources) | **View › Scene Display › Rendering**: Phong, Flat, Wireframe, Light Sources On. Hidden Line is not offered: in this renderer it would draw the same picture as Wireframe |
| Camera Setup | **Tools › Cameras** — saved cameras and a Viewport View tab in one dialog; the **Cam** button and right-click menu in the viewport; **C** / **Shift+C** cycle cameras |
| Units dialog (US, SI, Custom) | **Tools › Preferences › Units**: Imperial or Metric. No custom mix |
| 3-D editor manipulators | A gizmo, plus Blender-style keys: **G** move, **R** rotate, **X/Y/Z** axis lock, typed values, **Ctrl** snap. See [Interface Tour](03-interface-tour.md#moving-objects-the-gizmo) |
| Path Follower | **Event › Path Follower** — it is per event and per vehicle, so it is on the Event menu, not the Vehicle menu |
| Body Torsion | **Vehicle › Body Torsion** (a property of the vehicle, whichever event is open) |
| Transform Vehicle Geometry, Move CG of the geometry | **Vehicle › Vehicle Mesh** (also offered on the Event menu): scale, move and rotate the body, and its other mesh options |
| Use Ackermann Steering, set per event in Driver Controls | Ackermann / parallel steer is chosen in the vehicle's **Steering System** |
| Contact surfaces, airbags, belts | **Vehicle › Contact Surfaces**, **Airbag Restraint**, **Belt Restraint**; per event, **Event › Restraints** |
| GEBOD Human Information | **Occupant › Human Information** (the Occupants panel) |
| Damage Studio | **Output › Damage Studio Options** and **Damage Studio Report**; crush is drawn on the vehicle's 3-D body as the run plays |
| Impact Plane / Barrier (EDCRASH) | Greyed in the Event menu. Model a barrier as a vehicle of type **Fixed Barrier** in Vehicle Information |
| An input a program does not use is greyed | The same, and in addition HVE 2027 says **why** where it matters (for example, which program reads a field). Inputs are locked while results are on screen; press **Reset** to edit |
| `.hve` case files | `.hvc` or `.json`; `.hve` files open directly but are not written. See [Cases and Files](04-cases-and-files.md) |

Most of HVE's dialogs are ported field for field. Where a dialog page in this
manual set describes a field HVE 2027 does not have, the page marks it
**Not in HVE 2027**.

## Physics differences by design

HVE 2027 runs HVE's own physics source. Three calculations were changed on
purpose. The second and third make no difference on any of EDC's tutorial and
validation cases, because none of them uses the situation they change; the
first is active on every EDVDS tandem-axle event.

**1. EDVDS tandem-axle load equalizer.** On a tandem axle with a
load-equalizing (four-spring) suspension, HVE applies the whole load-levelling
correction at every evaluation. HVE 2027 does the same at ordinary time steps,
but below a 5 ms step it spreads the correction over 5 ms, because at very
small steps HVE's form oscillates until the run aborts. On EDC's tandem-axle
validation cases and the EDVDS tutorial the results lie within about 2.5 cm of
HVE's saved results; two of HVE's tutorial lessons are sensitive enough to the
time step that neither HVE nor HVE 2027 gives a repeatable answer for them. See
the [EDVDS manual](../programs/EDVDS/README.md).

**2. Path follower switched off per vehicle at impact (SIMON and EDSMAC4).** In
HVE the first collision anywhere in an event turns off the driver model (path
follower) of **every** vehicle. In HVE 2027 a collision turns off the follower
of the vehicles that collide; a following vehicle not involved in the
collision keeps following its path. Results differ only in a multi-vehicle
event with a path follower on a vehicle that is not in the collision — no case
in EDC's corpus is such a case. See the [SIMON](../programs/SIMON/README.md)
and [EDSMAC4](../programs/EDSMAC4/README.md) manuals.

**3. Differential type (SIMON).** HVE stores a differential type (Open,
Limited Slip, Locked) but greys the control and solves every differential as
open. HVE 2027's **Drivetrain** dialog enables the type, and SIMON applies a
torque bias for Limited Slip and Locked. **Open** gives HVE's answer, and every
vehicle imported from HVE is open.

!!! note "HVE 2027"
    Besides these three, a few changes stop a run that HVE would hang or crash
    on: the run ends with an error message instead. They do not change the
    result of a run that completes.

## Options the programs refuse

HVE offers some options that its own physics programs do not implement. HVE 2027
offers them too (an imported case may state them) but **marks them in the
list**, and the program stops the run with an error message rather than quietly
running something else:

| Where | Option | What happens |
| --- | --- | --- |
| SIMON Method Options › Hydroplaning | Blythe-Day *(refuses the run)* | SIMON implements Off, NASA, NASA-TTI and Gallaway |
| EDSMAC4 Method Options › Hydroplane Model | NASA-TTI, Gallaway *(not supported by EDSMAC4)* | EDSMAC4 implements Off and NASA |
| Vehicle › ABS / Brake Design › ABS algorithm | Algorithm 3, 5 and 6 *(not implemented)* | The run stops when the ABS first acts. Tire Slip, Bosch Version 1 and Algorithm 4 are implemented |
| EDCRASH Method Options › Separation Velocity Basis | Iterate on Sideslip | EDCRASH refuses it. Normal, Trajectory Simulation and Sustained Contact work |
| Event › DyMESH Options › Search Option | Search all vertices *(refuses the run)* | Automatic box size and Set box size work |

!!! warning "Not in HVE 2027"
    GATB's **Use external ATB input file** is shown greyed. HVE 2027 passes the
    ATB input to the solver directly, not through a `GATB.ain` file, so an
    external file cannot reach it.

## New in HVE 2027

!!! tip "New in HVE 2027"
    Each of these is an addition; none of them changes a case that does not
    use it.

| Feature | Where | What it does |
| --- | --- | --- |
| Single-track (motorcycle) program | Calculation Method **SINGLETRACK**; **Tools › Motorcycle Analysis** | A motorcycle model with lean as a degree of freedom, countersteer, load transfer and pitch-over, validated against the published benchmark. HVE's programs can only approximate a two-wheeler as a narrow four-wheeled vehicle |
| Prescribed lean (SIMON) | **Event › Driver Controls › Lean** tab (shown for a motorcycle) | Makes SIMON's body follow a lean-angle table, for a motorcycle that would otherwise fall over |
| Path follower through impact (SIMON, EDSMAC4) | **Event › Path Follower › Keep following through an impact** | Keeps a vehicle's path follower active after it collides. Off by default, and always off in a case imported from HVE |
| Per-axle steer degree of freedom (SIMON) | **Vehicle › Steering System**, Steer DOF (SIMON) | Sets SIMON's steer degree of freedom — Normal (free), Append (free after the table) or Auto start (free at contact) — for each axle separately, instead of one setting for the whole event; for example, a free castoring axle |
| Limited-slip and locked differentials (SIMON) | **Vehicle › Drivetrain** | See [Physics differences](#physics-differences-by-design) |
| Monte Carlo analysis | **Tools › Monte Carlo Analysis** | Runs the event many times with uncertain inputs (Normal, Uniform, Triangular or Lognormal; Random or Latin Hypercube sampling) through the real physics programs, and reports confidence intervals, sensitivity and convergence, with a CSV, an HTML report and an audit record |
| Quick Case | **Tools › Quick Case (Text)** | Builds a case from a typed sentence, such as "SIMON event, vehicle 1 at (0,0) heading 0 speed 50 mph, vehicle 2 at (12,-3) heading 180 speed 30 mph", with a preview before it is applied |
| Vehicle Package | **Tools › Vehicle Package** | Builds a case vehicle from its VIN (checked offline, or decoded by NHTSA on request) or year, make and model: the matching database record, or a generic scaled to the vehicle's stated weight, dimensions and CG height; with its occupants (GEBOD) and cargo. See [Case Intake and Vehicle Data](../new-features/12-case-intake-and-vehicle-data.md) |
| Case Intake and Provenance | **Tools › Case Intake**, **Tools › Provenance** | Builds an event from the case documents through your own AI tool (HVE 2027 sends nothing anywhere), and keeps, with the case, where every value these tools set came from: stated, looked up, estimated, a generic's default or unknown |
| Occupants and cargo aboard a vehicle | **Inertia / Mass** dialog, *Aboard* | A load the vehicle carries into every event and engine, added to its mass, CG and inertia, or handed to SIMON and EDVDS as payload |
| Crush stiffness from crash tests | **Vehicle › Crush Stiffness › From crash tests** | CRASH3 A and B from staged barrier tests, typed in or read from an NHTSA test file, put on a side of the vehicle and on its EDCRASH events |
| EDR import | **Tools › EDR Import** | An event data recorder's pre-crash record into an event vehicle's initial speed and driver-control tables, and the recorded delta-V against the run's |
| Node materials | **View › Shader Editor** | Blender-style material graphs for vehicles, road surfaces and the sky. Display only: a surface's friction stays in the Environment editor |
| Keyframes | **View › Dope Sheet**; **I** in the viewport | Animate material values and cameras over the playback time. Display only |
| Blender | **File › Export Scene for Blender** (glTF), **File › Blender Live Link** | Take the solved scene into Blender; the live link updates the objects already in Blender after each re-run, keeping the materials and cameras set up there |
| Publish Bundle, viewer and web builds | **File › Publish Bundle**; see [Installing and Running](02-installing-and-running.md) | Share a solved case as a folder or a link, viewable without an installation |
| Embedded site | **File › Embed the environment in the case** | Carry the terrain and aerial photograph inside the case file |
| Outliner, undo history | **View › Outliner**, **Edit › Undo History** | See [Interface Tour](03-interface-tour.md) |

## Not available in HVE 2027

!!! warning "Not in HVE 2027"
    - **Writing `.hve` files.** Cases are saved as `.hvc` or `.json`.
    - **Calculation programs HVE 2027 does not have.** An event whose program is
      not one of HVE 2027's opens, keeps its inputs, and does not run; the run
      status says so. (Read Data File runs: it replays the event's data file.)
    - **The Impact Plane / Barrier dialog** (EDCRASH). Use a Fixed Barrier
      vehicle.
    - **HVE's Distance Tool.**
    - **Hidden Line rendering** and **custom units**.
    - **A vehicle database creator.** Vehicles can be saved into a `.db` file
      with Vehicle › Save Vehicle As, but there is no tool to create a database.
    - **Accounts, shared workspaces and cloud computing.**

For the physics behind every program, see the program manuals:
[EDCRASH](../programs/EDCRASH/README.md), [EDSMAC](../programs/EDSMAC/README.md),
[EDSMAC4](../programs/EDSMAC4/README.md), [EDGEN](../programs/EDGEN/README.md),
[EDHIS](../programs/EDHIS/README.md), [SIMON](../programs/SIMON/README.md),
[DyMESH](../programs/DyMESH/README.md), [EDSVS](../programs/EDSVS/README.md),
[EDVDS](../programs/EDVDS/README.md), [EDVTS](../programs/EDVTS/README.md),
[EDVSM](../programs/EDVSM/README.md) and [GATB](../programs/GATB/README.md).
