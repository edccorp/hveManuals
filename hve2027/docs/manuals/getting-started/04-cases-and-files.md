# Cases and Files

## Case files

HVE 2027 saves a case in one of two formats. Both hold the whole case — humans,
vehicles, environment and events — and either one opens with
**File › Open Case**.

| File | What it is | Saved by |
| --- | --- | --- |
| `<name>.hvex` | The case, in a binary file. The format of record | **File › Save Case**, **File › Save Case As** |
| `<name>.json` | The same case as text: readable, and comparable line by line between two versions | **File › Save Case As JSON** (or Save Case As with a name ending in `.json`) |
| `<name>.hver` | The results of every solved event, saved beside the case | Written automatically by Save when there is a solved run |
| `<name>.hves` | A **sealed case** for an outside party: the solved case, its results and report pages, the site and the vehicle meshes (encrypted) in one file, opened read only and never re-run | **File › Seal Case for Handoff...** (see [Sealed cases](#sealed-cases-hves)) |

**Save Case As** writes the binary format unless the file name ends in `.json`.
**Open Case** does not go by the extension: it reads a file whose content is
JSON as JSON, an `.hvex` as `.hvex`, a sealed case as a sealed case, and
anything else as an HVE `.hve` case.

Case files are stored in SI units whatever the unit setting, so a case saved in
one unit system opens unchanged in the other.

!!! note "HVE 2027"
    HVE 2027 reads HVE's `.hve` case files but does not write them. A case
    opened from a `.hve` is saved as `.hvex` or `.json`.

### Saved results (`.hver`)

When you save a case that has been run, the results of **every event you have
solved** are written beside it as `<name>.hver` — trajectories, the variable
output, damage, occupant motion and the report pages — so a playback sequence
plays straight away when the case is opened again, without **Run All Events**.
Each event's results carry a fingerprint of the inputs that event was solved
from. When the case is opened again:

- an event whose inputs are unchanged comes back solved, labelled with when it
  was computed and by which build — nothing is run;
- an event that was edited since is opened unsolved, and the program names it,
  so a case can never show results that do not belong to it. Editing one event
  leaves the others' results alone; editing something every event uses (a
  vehicle, the environment) discards them all.

If you edit an event after running it and then save without running it again,
that event's results are not saved, and the save message says which event was
left out.

Opening a case never re-runs it on its own. A case with no `.hver` simply opens
unsolved, and saving a case that has no results removes an old `.hver` beside it.
Moving or changing the camera, materials, lights, Results HUD boxes or other display settings —
or selecting a different event, or rearranging a playback sequence — does not
discard saved results; changing an input does. Saving into another folder
rewrites the case's file references so they still name the same files, and that
does not discard them either.

Saving also clears the undo history.

## Opening HVE cases (`.hve`)

**File › Open Case** reads HVE's own case files directly. The import has been
developed against cases saved by HVE versions 10.1 to 11.1, including all of
EDC's tutorial and validation cases.

**What is imported:**

- **Vehicles** — the complete vehicle record: dimensions, weights and
  inertias, CG, exterior crush stiffness, frame torsion, connections,
  aerodynamics, engine, transmission and differential, wheel locations,
  suspension (springs, shocks, stops, steer-axis geometry, camber and roll
  steer), tires (physical data and the friction, cornering and camber tables),
  brakes (per wheel, including the Brake Designer data and the ABS
  controllers), steering system, payload, traction control and yaw stability
  control, interior contact surfaces,
  belt anchors and airbags, and the name of the vehicle's geometry file.
- **Environment** — the site's terrain and drawn geometry, its surfaces,
  layers and aerial photograph, and the environment's location, date, time
  and sun direction.
- **Events** — every event with its calculation method, the vehicles and
  humans in it, initial, impact, separation and rest positions and the other
  surveyed positions, driver controls (steer, throttle, brake, gear), path
  follower, calculation options and time steps, wheel blow-out and damage,
  DyMESH options and mesh preparation, payload, collision pulse, EDCRASH damage
  data (and HVE's own reconstruction results, for comparison), occupant
  restraints and occupant contact pairs.
- **Humans** — body, segments, joints and their pose in each event, and a
  pedestrian's initial velocity.

**What is not imported, or not used:**

- A driver-control table HVE expresses as tractive effort against speed cannot
  be represented; the import says so rather than approximating it.
- The brake-lining material block of HVE's thermal brake model (lining
  thickness, density, specific heat, conduction and convection coefficients) is
  not read. Drum and lining initial temperatures are.
- HVE's ESP switch is not kept: HVE 2027's programs model traction control and
  yaw stability control only, and the import notes name any vehicle that has
  ESP switched on.
- An event whose method has no program in HVE 2027 opens under its own method
  name and is shown, but **Run** refuses it. It is never run as a different
  program. (A Read Data File event runs: it replays the event's data file.)
- A case that states no events opens without an event, and says so.
- Some values are read but deliberately not passed to the programs, because
  HVE does not pass them either; where that is so the dialog concerned says
  why.

Notes about an import appear in the Event Information panel. The longer
explanatory ones are shown only with **View › Show Guidance Text**; anything
specific to the case — a value that could not be represented, a default that
had to be supplied — is always shown.

### Geometry

HVE names a vehicle's geometry file (and some site files) by file name only,
so HVE 2027 has to find the file. It looks beside the case, then in the
vehicle geometry folders (a `vehicles` folder beside the program, and any
folders you add).

When a case names geometry that cannot be found, a **Geometry Not Found**
message lists the files as the case opens. The case is still loaded with all
its inputs, but the site draws as flat ground and a vehicle whose geometry is
missing draws — and, in DyMESH, collides — as a box. Put the files back beside
the case, or add their folder under **Search folders** in the **Vehicle
Geometry Library** (Vehicle › Vehicle Mesh › **Library...**). Its **Rescan**
button re-reads the folders.

!!! note "HVE 2027"
    For an imported `.hve`, HVE 2027 keeps a reference to the original `.hve`.
    A case saved from it carries the site inside it (see
    [Embedding the environment](#embedding-the-environment)). Saved with that
    option off, the case re-reads the site's terrain from the `.hve` each time
    it opens, and on another machine without the `.hve` its vehicles open with
    no ground under them.

## Vehicle databases

HVE 2027 reads HVE's classic vehicle database files (`.db`), such as
`Generic.db`, and its own databases (`.hvedb`), which carry each vehicle's mesh
and wheel images inside them:

- `EDCVehicles.hvedb` — EDC's licensed vehicle data, installed as a separate
  data pack (see below). Where it is present, the classic `EDC.db` and
  `VMSTANDARD_7_00.db` it replaces are listed as superseded and not read.
- `MyVehicles.hvedb` and any other database you name — your own vehicles,
  written by **Vehicle › Save to My Vehicles...** (see
  [Save to My Vehicles](../hve-users/04-vehicle-editor/10-creating-editing-vehicles.md#save-to-my-vehicles)).

A program package carries only `Generic.db`.

- **Adding a vehicle.** In the Vehicle editor, **Add...** on the Vehicles panel
  opens a search of every vehicle in the loaded databases, plus HVE's generic
  vehicles by type and class (the **Generics** button) and a few built-in
  vehicles that need no database. **Replace...** replaces the selected
  vehicle's data with a database record.
- **Where databases are found.** Any folders added under **Database folders**
  in the same dialog; your own `userdb` folder (on Windows, in
  `%APPDATA%\EDC\HVE 2027`);
  the EDC vehicle data folder; and a `db` folder beside the program. Your
  `userdb` folder is where **Save to My Vehicles** writes `MyVehicles.hvedb`
  and your other databases, where **Import database...** copies a database
  someone gave you, and where **Save Vehicle As** writes unless you choose
  another file. It is shared by every installed version and kept when one is
  uninstalled.
- **The EDC vehicle data folder.** EDC's vehicle data pack is installed once
  per computer, for every installed version, in `%ProgramData%\EDC\HVE\data`
  on Windows (`~/Library/Application Support/EDC/HVE/data` on macOS,
  `~/.local/share/hve/data` on Linux). Uninstalling a version does not touch
  it. Among the folders that come with the program it is searched first, ahead
  of the program's own `db` folder. **Help › Check for Vehicle Data Updates**
  installs a newer edition there (see
  [Help menu](../hve-users/02-menu-reference/07-help-menu.md#check-for-vehicle-data-updates)).
- **Saving a vehicle.** **Vehicle › Save Vehicle As** sets the name, type,
  make, model, year and body style and either writes a copy of the database
  record the vehicle was loaded from into a `.db` file under those keys
  (**Save to Database**), or applies those fields to the vehicle only
  (**Apply to Vehicle**). Other changes made to the vehicle are saved with the
  case, not in the database (see [Saving Vehicles](../02-vehicles/VehSaveAs.md)).

There are no human database files. A human is created in the Human editor
(**Add Occupant** on the Occupants panel) with a GEBOD-generated body, or
comes in with an imported `.hve` case.

## Geometry formats

| Used for | Formats | Where |
| --- | --- | --- |
| Vehicle body | `.h3d`, `.iv`, `.wrl`, `.obj`, `.gltf`, `.glb`, and point-cloud scans `.las`, `.ply`, `.e57`, `.xyz`, `.pts` (drawn as points, collided as a closed surface rebuilt from them) | The Mesh File of the Vehicles panel's 3D Geometry section, or the Vehicle Mesh window (Vehicle › Vehicle Mesh, also on the Event menu); the Library... button lists the geometry folders |
| Site (terrain and scene) | `.dxf`, `.h3d`, `.iv`, `.wrl`, `.obj`, `.gltf`, `.glb` | Environment panel › Terrain › Geometry File; with scale factor, Y-up / Z-down options and **Use surfaces as terrain (physics)** |
| Survey point cloud | `.las`, `.ply`, `.e57`, `.xyz`, `.pts`, `.txt`, `.csv` | Environment panel › Survey Point Cloud (scan) |
| Aerial photograph | image file | Environment › Aerial Image (with its world-bounds corners) |
| Material textures | `.png`, `.jpg`, `.bmp`, `.tga`, `.hdr` | View › Shader Editor |

An `.h3d` file is read in HVE's own frame (inches, Z down) automatically.

## Embedding vehicle meshes

**File › Embed vehicle meshes in the case**, a tick-box remembered between
sessions and **off** by default, stores each vehicle's own mesh inside the case
file when it is saved, so the case opens with its vehicle bodies on a computer
that does not have those files. EDC's licensed meshes are never stored: they
stay references to the vehicle database. The menu tooltip says how many meshes
the case carries and their size. Unticking it and saving removes the stored
meshes, and the case names the files again.

## Embedding the environment

Like an HVE `.hve`, a saved case carries its site's geometry, surfaces, layers
and photograph **inside the case file**, so it opens with its ground on a
machine that has neither the source `.hve` nor the geometry file. **File ›
Embed the environment in the case** is the switch, a tick-box remembered
between sessions and **on** by default; untick it and a save names the site
file instead. The photograph is stored losslessly (as PNG) and is most of the
cost: a large city site adds about 1.7 MB to the case. Switching the option off
again removes the embedded site at the next save. While the case carries a
site, the File menu shows its size under the option.

Embedding is display and terrain data only; it does not change a result.

## Publish Bundle

**File › Publish Bundle...** writes a case, the geometry it names and its
results into one folder that opens anywhere — in HVE 2027 on another machine,
in the read-only viewer, or in the browser build from a link.

The dialog offers:

- **Include the per-channel output capture** — every output channel of the
  run. It is optional because it is by far the largest part (tens of MB against
  well under one for everything else); playback does not need it.
- For a solved case, **Publish...**, which asks for a folder.
- For an unsolved case, **Run, then publish** (solves first) or **Publish
  inputs only**, for a recipient who will run it on a full installation. A
  bundle without results opens in the viewer on an empty scene, with a message
  saying it was published without results.

The bundle is written into a new subfolder named after the case, holding the
case as JSON, only the geometry files the case uses (renamed to plain file
names so they are found wherever the folder is unpacked), the results and a
`manifest.json`. Copied to a web server beside the browser build, it opens from
a link ending in `?case=<path to the folder>`.

The same thing from the command line, which solves the case first and refuses
to publish one it cannot solve:

```sh
hve-next --export-bundle <case> <output folder> [title] [--inputs-only] [--with-capture]
```

## Sealed cases (`.hves`)

**File › Seal Case for Handoff...** writes a case that is to be turned over to
an outside party as one file ending `.hves`. It carries the case, every
event's results and report pages, the site and the vehicle meshes, so it
opens on a computer that has none of the case's files. It opens read only: it
cannot be edited, re-run or saved, and its geometry cannot be exported.

- **Every event must be solved first**, with results that still match its
  inputs, because a sealed case can never be re-run. The dialog lists the
  events and greys **Seal...** until they all are; run an unsolved event or
  delete it.
- **Licensed vehicle data stays out.** Each vehicle keeps only what it takes
  to draw it; its weights, inertias, suspension, tires, brakes, drivetrain and
  stiffness are not in the file, and its dialogs say their values are
  placeholders. The values the run used are on **Output › HVE Reports**. The
  vehicle meshes are encrypted, so they cannot be copied out of the file with
  a zip tool or a file manager.
- **A sealed case says if it has been changed.** A band along the bottom of
  the window says the case is sealed, when, and that the seal verifies. A
  file changed since it was sealed still opens, but the band turns red and
  says it has been modified and cannot be trusted.

The recipient opens it with **File › Open Case...** and can play it back and
save images, videos, channel data and report pages. Opening another case
leaves sealed mode. The solver alone (`hve-solver`) refuses a sealed case.
See [Seal Case for Handoff](../hve-users/02-menu-reference/03-files-menu.md#seal-case-for-handoff)
for the dialog. The same is available from the command line:

```sh
hve-next --seal-case <case> <out.hves> [--solve]
```

Without `--solve` it seals the results saved with the case (its `.hver`);
with it, every event is solved first.

## Recent files

**File › Open Recent** lists the last 12 cases opened or saved, newest first,
by file name; hover over an entry for its full path. **Clear Recent** empties
the list. The menu is greyed while the list is empty. If the open case has
unsaved changes, opening another one (by any route) first asks whether to
discard them.

## Saving and unsaved changes

The case file itself is never saved automatically.

!!! note "HVE 2027"
    HVE's auto-backup is **Tools › Preferences › Auto-Save**. **Enable Auto-Save** (on by default) and **Interval (min)** write a recovery copy of the case, `<case>.autosave.hvex` beside it, while there are unsaved changes; the case file itself is never written. Saving the case removes the copy, and opening a case whose recovery copy is newer offers to open the copy. **File › Exit**,
    closing the window, **New Case** and **Open Case** all ask before discarding
    unsaved changes.

## Other files the program writes

| Menu | Writes |
| --- | --- |
| File › Export Scene for Blender | The solved scene as glTF, `.glb` (recommended, one file) or `.gltf`. Available after a run |
| File › Blender Live Link | No file: Blender reads the scene from the running program |
| File › Record Animation | The 3-D playback as a Motion-JPEG `.avi` video, between the start and end times you choose, through the camera you choose, in real time or slow motion. Available after a run. Tick **Burn in key results (Results HUD)** to draw the case's [Results HUD](../new-features/11-results-hud.md) boxes into every frame. Panels and dialogs are not recorded. A file name without a folder is written to the folder the program was started from (see [Recording a video](../new-features/07-video-and-playback-sequences.md#recording-a-video)) |
| Output › Export Variables | The selected variables of the event on screen, one column each, at the chosen interval: CSV, tab-separated text or a MATLAB `.m` script, in SAE or HVE's Traditional signs |
| Key Results › Export CSV | The channels chosen with **Select Variables...** (position, heading and speed among them) at every output step |
| Output › HVE Reports | Reports of the run, the Accident History among them. HVE Reports saves its pages as text (`hve_report.txt`) or HTML (`hve_report.html`), and HVE 2027's own run summary as `run_report.html`; a file name without a folder is saved beside the case file (in the folder the program was started from, for a case never saved), and the window shows the full path (see [Common Reports](../11-reports-output/CommRepDlg.md)) |
