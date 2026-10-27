# Installing and Running

HVE Studio is supplied by EDC. This page describes what the preview
consists of, how to start it and open a case, where it keeps its settings and
its log, and the tasks it can run from the command line.

| Edition | What it is | In the preview |
| --- | --- | --- |
| Desktop program, Windows | The full program: the editors, every physics program, playback, reports and export | Yes: an installer for 64-bit Windows (or, from EDC, a folder of the same files) |
| Desktop program, Linux | The same program for Linux | Not packaged for the preview |
| Browser version | The same program running inside a web browser tab, on your own computer | Not part of the Windows package; see [The browser version](#the-browser-version) |
| Read-only viewer | Opens solved cases and plays back their saved results, with no editors and no physics programs | Not part of the Windows package; see [The read-only viewer](#the-read-only-viewer) |

All of them read the same case files.

## Installing on Windows

Run the installer, **`HVEStudio-<version>-setup.exe`**.

- **For yourself (the default).** It installs into
  `%LOCALAPPDATA%\Programs\EDC\HVE Studio\<version>` and needs no administrator
  rights. Install this way unless you have a reason not to.
- **For every user.** Run the installer with **`/ALLUSERS`** from a command
  prompt opened as an administrator; it installs into `Program Files\EDC\HVE
  2027\<version>`. **`/S`** installs without asking anything.
- **Side by side.** Each version installs into its own folder, with its own
  Start menu entry, **HVE Studio <version>**, and its own entry in Windows'
  installed-apps list. **HVE Studio** in the Start menu, and double-clicking an
  `.hvex` case, open the version installed last.
- **Classic HVE is left alone.** The installer never takes over `.hve` files;
  they stay with HVE.
- **Uninstalling** a version (from Windows' installed-apps list) removes that
  version's folder, and only that one. Your license, settings, saved vehicles
  and cases are kept: none of them is in a version's folder (see
  [Where the program keeps its settings](#where-the-program-keeps-its-settings)).

!!! note "HVE Studio"
    An installed release needs a **license** that covers the program of the
    event you run: activate it under **Help › License...** with your EDC
    Software secret (see [Help › License](../hve-users/02-menu-reference/07-help-menu.md#online-licensing)).
    Without one, **Run** is refused and the run status says why. The program
    does not check for new versions of itself. With an activated license it
    does check, at most once a day, for a newer edition of EDC's vehicle data
    (see [Help › Check for Vehicle Data Updates](../hve-users/02-menu-reference/07-help-menu.md#check-for-vehicle-data-updates)).

## What is in the program folder

Installed or copied, the program is one folder. Keep its contents together:

| File or folder | Purpose |
| --- | --- |
| `HVEStudio.exe` | The program |
| `HVESolver.exe` | The physics solver. On Windows every **Run** is solved by this program in a separate process, so it must stay in the same folder as `HVEStudio.exe` |
| `SDL2.dll` | A library the program needs for its window, keyboard and mouse |
| `hve-solver-reference.exe` | Where present: the HVE-reference physics, used when an event's **Physics** is *HVE-reference* (Event Information) and by **Output › Compare Runs...**. Without it, an HVE-reference event says it cannot run |
| `db\` | The vehicle databases. An installed release carries `Generic.hvedb` only (HVE's generic vehicles and the generic motorcycle, with its mesh inside); EDC's vehicle data (`EDCVehicles.hvedb`, with its meshes and wheel images inside it) is licensed separately and installed in its own folder (below). A preview folder from EDC may carry `EDCVehicles.hvedb` here as well |
| `vehicles\` | 3-D vehicle geometry files that classic `.db` databases name. An installed release carries none: the generic motorcycle's mesh is inside `Generic.hvedb` |

EDC's vehicle data is a separate download, installed once per computer in
**`%ProgramData%\EDC\HVE\data`**, outside every version's folder: every
installed version reads it, and uninstalling a version does not touch it. Among
the folders that come with the program it is searched first. **Help › Check for
Vehicle Data Updates** installs a newer edition there (see
[Vehicle databases](04-cases-and-files.md#vehicle-databases)).

The program file is `HVEStudio.exe` and the solver `HVESolver.exe` (in a
preview folder from EDC they may still be called `hve-next.exe` and
`hve-solver.exe`, which work the same). All the physics programs, GATB
included, are part of them.

!!! note "HVE Studio"
    If EDC gives you the preview as a **folder** rather than an installer, copy
    the whole folder (below); removing it is deleting the folder. Whether such
    a copy needs a license is shown in **Help › License...**.

### What the computer needs

- **64-bit Windows.**
- **A graphics driver with OpenGL 3.3.** If the driver cannot provide it, the
  program stops when it starts with an *OpenGL 3.3 required* message that names
  the renderer Windows supplied. This happens over Remote Desktop, in a virtual
  machine, or with an out-of-date graphics driver; update the driver, or run
  the program on the computer itself.
- **A mouse with a wheel or middle button** is recommended for moving the 3-D
  view (see the [Interface Tour](03-interface-tour.md#the-viewport)).

### Using a preview folder instead of the installer

1. Copy the whole folder anywhere, for example `C:\HVE Studio` or a
   folder under *Documents*. The program keeps nothing of yours in it: your
   settings and saved vehicles are kept in the same place as an installed
   version's (see below), so they are shared with it.
2. If you want a desktop shortcut, right-click `HVEStudio.exe` and choose
   **Send to › Desktop (create shortcut)**.

The preview does not change HVE or its files and can be used on the same
computer as HVE. It opens HVE's `.hve` case files but never writes them, and it
does not take over the `.hve` file type: double-clicking a `.hve` file still
opens HVE.

## Starting the program and opening a case

Double-click `HVEStudio.exe` (or its shortcut). The window's title bar reads
**HVE Studio**, followed by the open case's file (*Untitled* until a case
is opened or saved) and its number of vehicles; a `*` in front means unsaved
changes.

To open a case:

- **File › Open Case...** (**Ctrl+O**) opens an HVE case (`.hve`) or an
  HVE Studio case (`.hvex` or `.json`). **File › Open Recent** lists the cases
  opened or saved most recently.
- A case can also be named when the program is started, for example from a
  Command Prompt in the program's folder:

    ```bat
    HVEStudio.exe "C:\Cases\Intersection.hve"
    ```

An HVE case names its vehicles' geometry files by file name only. The program
looks for them beside the case, then in the `vehicles` folder beside the
program and in any folders you add. A vehicle whose geometry cannot be found is
drawn, and collides in DyMESH, as a box, and a **Geometry Not Found** message
lists the missing files when the case opens. See
[Cases and Files](04-cases-and-files.md#opening-hve-cases-hve) for what is
imported from a `.hve` and [Vehicle databases](04-cases-and-files.md#vehicle-databases)
for where databases are found.

To run an event, switch to the Event editor (**F5**) and press **Run** on the
playback bar under the viewport, or choose **Output › Run Simulation**
(**Ctrl+R**), which opens the Event Designer on its **Run** stage. The
[Interface Tour](03-interface-tour.md) describes the window.

## Where the program keeps its settings

The window layout, the recent-files list, the style and the preferences are
kept in small files in your own application-data folder,
**`%APPDATA%\EDC\HVE Studio`** (type that into Explorer's address bar to open
it), beside your license (`license.json`):

| File | Holds |
| --- | --- |
| `imgui.ini` | The window and panel layout |
| `hvenext.panels` | Which panels are open, the editor last used, and most display settings |
| `hvenext.recent` | The recent-files list |
| `hvenext.style` | The settings made in **Tools › Style Editor** |
| `hve_prefs.ini` | Other preferences, such as **Tools › Preferences › Auto-Save** |
| `hvenext.meshlib`, `hvenext.vdblib` | Geometry and database folders you have added |
| `hve_limits.ini` | Written when the **Limits Editor** saves to a file |
| `hve_report_text.json` | Your own wording for report strings, set in **Tools › Report Text...** |

Deleting `imgui.ini` restores the default panel layout the next time the
program starts.

Your own vehicle databases are kept in its `userdb` folder: `MyVehicles.hvedb`
and any other database written by **Vehicle › Save to My Vehicles...**, the
databases copied in with **Import database...** in the Add Vehicle dialog, and,
unless you choose another file, `user.db`, written by **Vehicle › Save Vehicle
As**. They appear in the vehicle database picker of every version.

This folder is **shared by every installed version** and is **not touched when
a version is uninstalled**, so a new version starts with your layout,
preferences and saved vehicles, and removing an old one loses none of them.
Cases are wherever you saved them. A cache of imported point clouds is kept
separately, in `%LOCALAPPDATA%\EDC\HVE Studio\pccache`; deleting it only makes
the next import of each scan slower.

## Log and crash files

When the program is started from Explorer or a shortcut, it writes everything
it reports to **`hve-next.log`** in `%APPDATA%\EDC\HVE Studio`, beside the
settings above. The file is started afresh each time the program starts, so
copy it before restarting if you need it. A line near the top beginning
`[hve] build` names the build. What the physics program itself reported during
the last run is in `hve-solver.log` in the same folder.

If the program crashes it also writes **`hve-next.crash.txt`** in the same
folder.

Started from a Command Prompt or PowerShell window instead, the program prints
its messages in that window and writes no log file.

Two things the log answers that the window may not:

- **Run seems to do nothing.** The log says whether `HVESolver.exe` was found
  beside the program and what it returned. A run that a physics program refused
  also shows the reason in red at the right of the playback bar.
- **The window opens and closes, or stays black.** The last lines of the log say
  how far the program got.

Questions and problem reports about the preview go to EDC. With a problem
report, send the case file, the steps that produce the problem, the version
shown in **Help › About HVE Studio...**, and `hve-next.log` (and
`hve-next.crash.txt`, if there is one).

## The browser version

The same program, with all of its editors and physics programs, also runs in a
web browser. It is not part of the Windows preview package; if you have been
given a link to it, it opens in the browser tab with nothing to install.
Nothing is sent to a server: the case is opened, edited and solved inside the
tab, on your own computer.

What is different in a browser:

- **Opening files** uses the browser's file picker. Select the case **and its
  geometry files** (`.h3d` and so on) together, since a browser has no folder
  to look in for them. Vehicle databases and whole geometry folders are
  uploaded from the **Load Vehicle from Database** and **Vehicle Geometry
  Library** dialogs (**Upload database files...** and
  **Upload a whole db folder...**; **Upload mesh files...** and
  **Upload a whole folder...**). Uploading geometry does not reach a case that
  is already open, because it found its geometry when it was loaded: when the
  open case still has vehicles without geometry, the Geometry Library offers
  **Reload case to use the uploaded geometry** (if the case has unsaved
  changes, save it and reopen it instead).
- **Saving and exporting** downloads the file.
- **What you upload is remembered** in the browser's storage for that site,
  together with the case that was open, so a page refresh brings the case back
  as last saved. A private window, or blocked site storage, forgets everything
  on reload; the program says so. Clearing the browser's site data also
  removes it, so keep your own copy of every case you save.
- **View › Panels Outside the Main Window** is not available: the page is one
  canvas.
- A published case opens from a link ending in `?case=<folder>` (see
  [Publish Bundle](04-cases-and-files.md#publish-bundle)).
- On a phone the program loads and plays back; landscape is the usable
  orientation, and a tap acts as a mouse click (there are no pinch or
  two-finger gestures).

!!! note "HVE Studio"
    Accounts, shared workspaces and cloud computing are not part of
    HVE Studio. Every edition computes on your own computer.

## The read-only viewer

A separate viewer edition of the program opens cases and plays back their
saved results. It has no editors and no physics programs at all, so it cannot
change or re-run a case. It is not part of the Windows preview package.

A case opened in the viewer shows results only if they were saved with it (a
`.hver` results file beside the case, or a bundle published with its results;
see [Cases and Files](04-cases-and-files.md)). A bundle published without
results opens with a message saying so. The viewer shows one event's results —
the event that was on screen when the case was saved — and a case with several
solved events says how many it holds; saving it from the viewer keeps all of
them.

A solved case can also be passed to someone else as a published bundle, which
opens in HVE Studio itself or, from a link, in the browser version (see
[Publish Bundle](04-cases-and-files.md#publish-bundle)).

## Command-line tasks

Besides opening a case, the program accepts a few tasks on its command line.
Run them from a Command Prompt or PowerShell window opened in the program's
folder; their messages appear in that window. All but the last run without
opening the program's window.

| Command | Does |
| --- | --- |
| `HVEStudio.exe --version` | Prints which build this is: the same build identifier that **Help › About HVE Studio...** shows |
| `HVEStudio.exe --convert-case <in> <out>` | Opens a case (for example an HVE `.hve`) and writes it as `.hvex` (if `<out>` ends in `.hvex`) or JSON. Stops if a vehicle's geometry cannot be found; add `--allow-missing-geometry` after `<out>` to write it anyway |
| `HVEStudio.exe --export-bundle <case> <folder> [title] [--inputs-only] [--with-capture]` | Solves the case and publishes it as a self-contained folder; refuses if the case cannot be solved, unless `--inputs-only` is given. See [Publish Bundle](04-cases-and-files.md#publish-bundle) |
| `HVEStudio.exe --serve=PORT` | Starts the program normally, with the Blender live link already listening on PORT (`--serve` alone uses port 17690). See [Exporting to Blender and glTF](../new-features/06-exporting-to-blender-and-gltf.md) |
