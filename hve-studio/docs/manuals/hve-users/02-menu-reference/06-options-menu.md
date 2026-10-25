# Chapter 6: Options Menu — Where It Went

*HVE User's Manual — Section Two: Menu Reference, HVE Studio edition. Replaces
HVE's Chapter 6, Options Menu.*

HVE Studio has no Options menu. HVE's Options menu mixed display switches, units,
calculation settings and preferences; in HVE Studio each of these lives next to
what it affects. This chapter takes HVE's Options menu item by item.

| HVE Options item | HVE Studio |
|---|---|
| Create DB | **Vehicle › Save Vehicle As...** › Save to Database ([details](#create-db)) |
| Show Key Results | **Output › Key Results...** or **View › Key Results** |
| Show Axes | **View › Scene Display › Axes** ([details](#show-axes)) |
| Show Contacts | **View › Scene Display › Occupant Equipment** |
| Show Belt Anchors | **View › Scene Display › Occupant Equipment** |
| Show Velocity Vectors | **View › Scene Display › Vectors › Velocity** |
| Show Skidmarks | **View › Scene Display › Skidmarks** |
| Show Tracks | **View › Scene Display › Tire Contact Patch Paths** |
| Show CGs / Show CG Paths | **View › Scene Display › CG Path** (no separate CG marker) |
| Show Accelerometers / Show Accelerometer Paths | **View › Scene Display › Accelerometer Path** |
| Show Position Sequences | Not in HVE Studio |
| Show Targets | **View › Scene Display › Scene Ghosts** |
| Show Connections | Not in HVE Studio as a display switch; connections are edited with **Connections...** in the Vehicles panel's Components section |
| Distance Tool | Not in HVE Studio |
| Show Path | The path follower's path is drawn while **Event › Path Follower...** is open |
| AutoPosition | **Auto Position (settle onto terrain)**, per vehicle, in Event Information's Vehicle Initial Conditions |
| Grid | Not in HVE Studio ([details](#grid)) |
| Units | **Tools › Preferences** › Units ([details](#units)) |
| Shadows | **View › Scene Display › Light & Shadow** (Shadow coverage); the sun is set in the Shader Editor's Sun & Sky panel and Event Information › Lighting |
| Render | **View › Scene Display › Rendering** ([details](#render)) |
| Playback | **Output › Playback Options...** |
| Simulation Controls | the **Simulation** panel (View › Simulation) ([details](#simulation-controls)) |
| Calculation Options | **Method Options...** in Event Information › Calculation Method ([details](#calculation-options)) |
| DyMESH | **Event › DyMESH Options...** ([details](#dymesh)) |
| Get Surface Information | Not in HVE Studio as a probe ([details](#get-surface-information)) |
| Preferences | **Tools › Preferences...** ([details](#preferences)) |
| Add Playback Window (legacy) | the **Playback (F6)** editor's **Playback Sequence** panel |

---

## CREATE DB

**HVE:** Options › Create DB · **HVE Studio:** Vehicle › Save Vehicle As...

The Save Vehicle As dialog sets the identification fields under which the vehicle
is saved (name, type, make, model, year, body style), its geometry file, version
information and security key, and the **Database File**, and **Save to Database**
writes the vehicle into it. The dialog notes that a database write needs the
vehicle's make, model, year and body style to match a loaded database record.
**Apply to Vehicle** copies the identification back to the vehicle.

![Save Vehicle As](../images/hvn-01-save-vehicle-as.png)
*Vehicle › Save Vehicle As...*

---

## SHOW AXES

**HVE:** Options › Show Axes · **HVE Studio:** View › Scene Display › Axes

Draws the environment's axes at the origin and each vehicle's own axes at its
CG, turning with the vehicle; on by default. The coordinate system is described
in [Appendix III](../11-appendices/appendix-03-coordinate-systems.md).

!!! note "HVE Studio"
    Axes are not drawn on humans.

---

## GRID

!!! warning "Not in HVE Studio"
    The viewport draws a ground grid, but there is no Grid dialog for its
    spacing, color or extent. (The Output Graph has its own
    gridline settings under **Format...**.)

---

## UNITS

**HVE:** Options › Units · **HVE Studio:** Tools › Preferences › Units

HVE Studio offers two unit systems: **Metric (m, km/h, kg, N)** and **Imperial
(ft/in, mph, lb, lbf)**. Fields that follow the setting change immediately;
the case itself is stored in SI units either way. HVE's Units dialog, which set
the unit of each quantity separately, is not reproduced.

![The Preferences dialog](../images/hvn-01-preferences.png)
*Tools › Preferences.*

!!! note "HVE Studio"
    The Preferences dialog notes that some fields still carry a fixed SI label
    while they are being converted.

---

## RENDER

**HVE:** Options › Render (Rendering Options dialog) · **HVE Studio:** View › Scene Display › Rendering

| HVE Rendering Options | HVE Studio |
|---|---|
| Show As, Render Method (shading) | **Phong**, **Flat** or **Wireframe** (Wireframe is HVE's Hidden Line) |
| Light sources | **Light Sources On** |
| Complexity, Show Only + Faces, Render Quality, Anti-aliasing Level | Not in HVE Studio |

A vehicle's own shading (as loaded, flat, smooth, auto smooth) is set in its
Vehicle Mesh window (Display tab), and the site's in the Environment panel's Terrain section.

---

## SIMULATION CONTROLS

**HVE:** Options › Simulation Controls · **HVE Studio:** the Simulation panel
(View › Simulation; docked beside Event Information)

The **Simulation Controls** at the top of the Simulation panel belong to the
active event:

- **Duration (s)**, **Trajectory Timestep (s)**, **Collision Timestep (s)**,
  **Separation Timestep (s)**, **Curb Impact Timestep (s)** (EDVSM), **Human
  Collision Timestep (s)** (EDHIS and EDGEN) and **Output Timestep (s)** —
  HVE's integration timesteps. A timestep the active method does not use is not shown, and the
  panel says so.
- **Termination** — linear and angular speed limits, each with an **On** switch;
  the run ends once every vehicle is below both armed limits. With both off the
  run integrates to the full duration.
- **Stopped Vehicle** — the linear and angular speeds below which a vehicle is
  reported at rest.
- **Integrator Convergence** — **Maximum Bisections** and **Velocity
  Convergence**, and for EDHIS the **Velocity Change Limit** and **Acceleration
  Change Limit**, shown only for the methods that read them.

Below them are the **Run** controls (status, progress, Run / Reset / Close and the
playback slider) and the **Last Result**.

![The Simulation panel](../images/hvn-01-simulation-panel.png)
*The Simulation panel.*

!!! note "HVE Studio"
    Some methods' option dialogs (for example SIMON Options) also carry the
    event's duration and output interval; they edit the same values.

See the dialog reference: [Simulation Controls](../../09-events-driver-controls/SimuCtrlDlg.md).

---

## CALCULATION OPTIONS

**HVE:** Options › Calculation Options · **HVE Studio:** Event Information ›
Calculation Method › **Method Options...**

Opens the options dialog of the active event's method: EDCRASH Options, EDSMAC
Options (also used for EDSMAC4), EDGEN Options, EDHIS Options, SIMON Options,
EDVSM Options, GATB Options or SINGLETRACK Options. EDSVS, EDVDS and EDVTS have
no options dialog in HVE Studio.

![SIMON Options](../images/hvn-01-method-options.png)
*Method Options... for a SIMON event.*

!!! note "HVE Studio"
    Some HVE options are offered with a note that the engine refuses them — for
    example SIMON's ABS Algorithms 3, 5 and 6 — and the dialog says the run will
    stop. SIMON's Blythe-Day hydroplaning model, which HVE's own SIMON does not
    implement either, is not offered; an imported case that states it is told so. The program manuals describe the
    options themselves.

See the dialog reference: [Calculation Options](../../10-calculation-options/README.md).

---

## DYMESH

**HVE:** Options › DyMESH · **HVE Studio:** Event › DyMESH Options...

HVE's DyMESH dialog had General and Advanced pages (search, pushback,
restitution, timesteps, debug output). HVE Studio's DyMESH Options dialog is one
page with **Start Times**, **Contact Search**, **Contact Model**,
**Restoration**, **Inter-Vehicle Contact (fallback)**, a **Per-pair
override** and **Contact Mesh Preparation (per vehicle)** (the event's own
tessellate, maximum triangle leg and weld distance for each vehicle, which in
HVE are set per event and vehicle with the mesh). The collision timestep is in the Simulation panel. Where the engine
stores an option but does not read it, the dialog says so beside the control.

!!! warning "Not in HVE Studio"
    DyMESH's debug output options are not offered.

---

## GET SURFACE INFORMATION

!!! warning "Not in HVE Studio"
    There is no tool that reports the surface under a picked point. In the
    Environment editor, clicking a surface in the viewport selects it, and the
    Environment panel's Selected Surface section shows its material.

---

## PREFERENCES

**HVE:** Options › Preferences · **HVE Studio:** Tools › Preferences...

| HVE preference | HVE Studio |
|---|---|
| Diagnostic Level | **Diagnostic Level** — grayed: nothing to control (a run's status always says what it assumed) |
| Auto Backup | **Enable Auto-Save** and **Interval (min)** — a recovery copy, `<case>.autosave.hvex`, written beside the case while there are unsaved changes |
| Date Style | **Date Format** — how dates are shown in the Audit Log, the file browser and the run report |
| Background Color | **Background Color** — the color of the main window behind the panels |
| Skidmark Height | Not in HVE Studio |
| Font Size | **Tools › Style Editor** (the interface's live style settings) |
| *(units)* | **Units** — see [UNITS](#units) |

!!! note "HVE Studio"
    Auto-Save never writes the case file itself: **Enable Auto-Save** (on by default) and **Interval (min)** write a recovery copy of the case, `<case>.autosave.hvex` beside it, while there are unsaved changes; the case file itself is never written. Saving the case removes the copy, and opening a case whose recovery copy is newer offers to open the copy.

<!-- NAV -->

---

← Previous: [Chapter 5: View Menu](05-view-menu.md)  |  [Index](README.md)  |  Next: [Chapter 6B: Tools Menu](06b-tools-menu.md) →

<!-- /NAV -->
