# Chapter 3: File Menu

*HVE User's Manual — Section Two: Menu Reference, HVE 2027 edition. Replaces
HVE's Chapter 3, File Menu.*

The File menu opens, saves and publishes cases, and exports a solved scene to
Blender. It is on the menu bar in every editor.

![The File menu](../images/hvn-02-file-menu.png)
*The HVE 2027 File menu.*

| HVE 2027 item | Shortcut | What it does |
|---|---|---|
| **New Case** | Ctrl+N | Starts a new, empty case |
| **Open Case...** | Ctrl+O | Opens an HVE 2027 case (`.hvc` or `.json`) or an HVE case (`.hve`) |
| **Open Recent** › | — | The most recently opened and saved cases; **Clear Recent** empties the list |
| **Save Case** | Ctrl+S | Saves the case to its current file (asks for a name the first time) |
| **Save Case As...** | — | Saves the case under a new name (binary `.hvc` unless the name ends in `.json`) |
| **Save Case As JSON...** | — | Saves the case under a new name as a `.json` text file |
| **Embed the environment in the case** | — | A switch: when ticked, the next save stores the site geometry and photograph inside the case |
| **Publish Bundle...** | — | Writes the case, its geometry and its results into one folder for the viewer product |
| **Export Scene for Blender** › | — | Writes the solved scene as glTF (`.glb` or `.gltf`) for Blender |
| **Blender Live Link...** | — | Lets Blender read the case directly while HVE 2027 runs |
| **Record Animation...** | — | Records the 3-D playback of a solved event or sequence to a Motion-JPEG `.avi` video (see [VIDEO CREATOR](#video-creator)) |
| **Render Image (Ray Traced)...** | — | Traces the 3-D view as it is now into a still picture |
| **Play Video...** | — | Plays a Motion-JPEG `.avi` video (see [VIDEO CREATOR](#video-creator)) |
| **Exit** | — | Closes HVE 2027 |

The HVE File menu items map as follows:

| HVE item | HVE 2027 |
|---|---|
| New | File › **New Case** |
| Open | File › **Open Case...** |
| Save | File › **Save Case** |
| Save As | File › **Save Case As...** / **Save Case As JSON...** |
| Export Preview Case | File › **Publish Bundle...** (for HVE 2027's own viewer, not for HVE Preview) |
| Print, Print All | Not in HVE 2027 — see [PRINT](#print) |
| Video Creator | File › **Record Animation...** and **Play Video...** — see [VIDEO CREATOR](#video-creator) |
| Export | **Output › Export Variables...** (Event editor) — see [Chapter 4D](04d-output-menu.md#export-variables) |
| FBX Export | Not in HVE 2027; File › **Export Scene for Blender** writes glTF instead |
| Recent file list | File › **Open Recent** |
| Exit | File › **Exit** |

---

## NEW

**Menu Option:** File › New Case (Ctrl+N)

**Purpose:** Start a new case.

**Description:** Clears the current case and starts an empty one. If the open
case has unsaved changes, HVE 2027 first asks **Discard changes?** — choose
**Save** to save it, **Discard** to throw the changes away, or **Cancel** to
keep working on it.

---

## OPEN

**Menu Option:** File › Open Case... (Ctrl+O)

**Purpose:** Open an existing case.

**Description:** Displays HVE 2027's file browser. Choose a file and open it.
HVE 2027 reads three kinds of case file:

- **`.hvc`** — HVE 2027's binary case file
- **`.json`** — HVE 2027's text case file (see [Cases and files](../../getting-started/04-cases-and-files.md))
- **`.hve`** — an HVE case file, read directly: its humans, vehicles, events
  and the site geometry stored in it are imported. HVE 2027 does not write
  `.hve` (see the note under [SAVE](#save)). What the import reads, and what
  it cannot, is described in [Cases and files](../../getting-started/04-cases-and-files.md).

If the file is not a case, HVE 2027 says so in a **Cannot Open File** message
and leaves the current case unchanged. If the case names geometry files that
cannot be found, the case still opens: a missing site draws as flat ground and a
missing vehicle mesh draws as a box, and a **Geometry Not Found** message lists
what is missing. Files are named relative to the case, so keep geometry beside
the case when you move it.

When a case was saved together with its results, those results are restored on
opening — but only if the case's inputs have not changed since they were
solved. Otherwise they are discarded and the panel says so. Opening a case never
re-runs it.

![The file browser](../images/hvn-02-open-case.png)
*Open Case uses HVE 2027's own two-pane file browser.*

---

## OPEN RECENT

**Menu Option:** File › Open Recent

**Purpose:** Re-open a recently used case.

**Description:** Lists recent cases by file name (hover over one to see its full
path). **Clear Recent** empties the list. The item is greyed when the list is
empty. This replaces HVE's recent-file list at the bottom of the File menu.

---

## SAVE

**Menu Option:** File › Save Case (Ctrl+S)

**Purpose:** Save the current case to its file.

**Description:** Saves to the file the case was opened from or last saved to.
A case that has never been saved asks for a name, defaulting to `case.hvc`.
A file whose name ends in `.json` is written as JSON; any other name is written
in HVE 2027's binary format.

!!! note "A case opened from an HVE `.hve` file"
    HVE 2027 does not write HVE's format, so it never saves over a `.hve`.
    **Save Case** (Ctrl+S) on a case opened from a `.hve` opens the save
    dialog with the same name ending `.hvc`; after that, Save Case writes the
    `.hvc`. The original `.hve` is left untouched. HVE 2027 also refuses to
    save a case over any existing file that is not an HVE 2027 case.

When the case has been run, a results file with the same name and the
extension `.hvr` is written beside it. It holds the results of every event
that has been run, each tied to the inputs it was solved from (see
[OPEN](#open)); an event edited since its run is left out, and the save
message says so.

---

## SAVE AS

**Menu Option:** File › Save Case As... · File › Save Case As JSON...

**Purpose:** Save the case under a new name.

**Description:** **Save Case As...** suggests the current name (or `case.hvc`)
and writes the binary format unless the name you give ends in `.json`. **Save
Case As JSON...** suggests the current name with a `.json` extension and writes
the case as text, which is readable and comparable with a text tool; it opens
again exactly like a `.hvc`. The saved file becomes the case's current file and
is added to Open Recent.

---

## EMBED THE ENVIRONMENT IN THE CASE

**Menu Option:** File › Embed the environment in the case

**Purpose:** Make a case self-contained.

**Description:** A check item. When ticked, the next save stores the site's
geometry and photograph inside the case file, so the case opens with its ground
on a computer that has neither the original `.hve` nor the geometry file.
Hovering shows how many triangles and image pixels the site has; the photograph
is the larger part of the cost. When the case already carries a site, the menu
shows its size. Untick it and save again to remove the embedded site.

!!! note "HVE 2027"
    An HVE `.hve` case carries its site inside the case already. An HVE 2027
    case normally names its geometry file instead; this switch makes it carry
    the site the way a `.hve` does.

---

## PUBLISH BUNDLE

**Menu Option:** File › Publish Bundle...

**Purpose:** Package a case so someone without your files can watch it.

**Description:** A bundle is one folder holding the case, the geometry it names
and the solved results. It opens in HVE 2027's viewer product, which plays a
case back but cannot run one. The **Publish Bundle** box offers:

- **Publish...** — publish with the solved run that is in memory
- **Run, then publish** — when the case has no results yet
- **Publish inputs only** — for a recipient who has the full workstation and
  will run it
- **Include the per-channel output capture** — also carry the full output
  channels, not just the trajectories

The item is greyed while a simulation is running.

!!! note "HVE 2027"
    This takes the place of HVE's **Export Preview Case**, which wrote a case
    for the HVE Preview program. A bundle is for HVE 2027's viewer only.

---

## EXPORT SCENE FOR BLENDER

**Menu Option:** File › Export Scene for Blender › glTF Binary (.glb) — recommended · glTF Text (.gltf)

**Purpose:** Export the solved scene, with its motion, for rendering.

**Description:** Writes the environment, the vehicles and their animated motion
as a glTF file that Blender (and other 3-D programs) can import. It is greyed
until the event has been run, because the export carries the motion.

!!! note "HVE 2027"
    This replaces HVE's **FBX Export**. HVE 2027 writes glTF, not FBX.

---

## BLENDER LIVE LINK

**Menu Option:** File › Blender Live Link...

**Purpose:** Let Blender read the case directly.

**Description:** Instead of exporting a file, HVE 2027 listens on a local port
(on this computer only) and a Blender add-on reads the case from it. When the
case is run again, the add-on updates the motion of the objects it already made,
so materials, cameras and lights set up in Blender are kept. Choose a **Port**
and **Start Link**; while running, the dialog shows the address, whether Blender
is connected and how many requests it has served. The link is read-only:
Blender cannot change the case. A tick beside the menu item shows the link is
running.

!!! tip "New in HVE 2027"
    The live link has no counterpart in HVE's menus.

---

## PRINT

**HVE menu options:** File › Print, File › Print All

!!! warning "Not in HVE 2027"
    HVE 2027 does not print. Reports and tables are saved to files and printed
    from another program: the Variable Report has a **Save** button, HVE
    Reports (which holds the Accident History) has **Save This Page** and
    **Save All Pages** for text, **Save Page as HTML** and **Save All Pages as
    HTML** for a page a browser can print or save as PDF, and **Export Run
    Report (HTML)** for HVE 2027's own printable run summary, and Key
    Results and the Timestep Data Table export CSV. See
    [Chapter 4D](04d-output-menu.md). The **Print...** buttons in the Damage
    Studio Report and the Audit Log do nothing in HVE 2027 Preview.

---

## VIDEO CREATOR

**HVE menu option:** File › Video Creator · **HVE 2027:** File › Record Animation..., File › Play Video...

!!! note "HVE 2027"
    **Record Animation...** writes the 3-D playback of the solved event (or of
    the active playback sequence) to a Motion-JPEG AVI file, at the width,
    height, frame rate and JPEG quality set in its window, through the camera
    chosen there (the view you are looking through, or any saved camera),
    between a start and an end time, in real time or slow motion, optionally
    ray traced or motion-blurred, and with the case's
    [Results HUD](../../new-features/11-results-hud.md) burned in when
    **Burn in key results (Results HUD)** is ticked. It is unavailable, with
    the reason shown, until an event has been run. See
    [Recording a video](../../new-features/07-video-and-playback-sequences.md#recording-a-video). **Play Video...** plays a Motion-JPEG AVI with
    play/pause, frame steps and a frame slider. There is no Video Creator
    window: several events are combined in the **Playback (F6)** editor and
    recorded the same way, from that editor. For a rendered movie, export the solved scene
    to Blender ([EXPORT SCENE FOR BLENDER](#export-scene-for-blender) or
    [BLENDER LIVE LINK](#blender-live-link)) and render it there.

---

## EXPORT

**HVE menu option:** File › Export

In HVE 2027, exporting output variables is **Output › Export Variables...**, in
the Event editor. See [Chapter 4D](04d-output-menu.md#export-variables).

---

## EXIT

**Menu Option:** File › Exit

**Purpose:** Close HVE 2027.

**Description:** If the case has unsaved changes, HVE 2027 asks **Quit without
saving?** with **Save**, **Discard** and **Cancel**. Closing the main window
does the same.

<!-- NAV -->

---

← Previous: [HVE User's Manual — Section Two: Menu Reference](README.md)  |  [Index](README.md)  |  Next: [Chapter 3B: Edit Menu](03b-edit-menu.md) →

<!-- /NAV -->
