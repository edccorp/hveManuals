# Installing and Running

HVE 2027 Preview is supplied by EDC. This page describes what the preview
consists of, how to start it and open a case, where it keeps its settings and
its log, and the tasks it can run from the command line.

| Edition | What it is | In the preview |
| --- | --- | --- |
| Desktop program, Windows | The full program: the editors, every physics program, playback, reports and export | Yes: a folder of files for 64-bit Windows |
| Desktop program, Linux | The same program for Linux | Not packaged for the preview |
| Browser version | The same program running inside a web browser tab, on your own computer | Not part of the Windows package; see [The browser version](#the-browser-version) |
| Read-only viewer | Opens solved cases and plays back their saved results, with no editors and no physics programs | Not part of the Windows package; see [The read-only viewer](#the-read-only-viewer) |

All of them read the same case files.

## What is in the Windows package

The preview is a folder. Keep its contents together:

| File or folder | Purpose |
| --- | --- |
| `hve-next.exe` | The program |
| `hve-solver.exe` | The physics solver. On Windows every **Run** is solved by this program in a separate process, so it must stay in the same folder as `hve-next.exe` |
| `SDL2.dll` | A library the program needs for its window, keyboard and mouse |
| `hve-rsc\` | The text each physics program uses to lay out its report pages (**Output › HVE Reports**) |
| `db\` | HVE's vehicle databases: `EDC.db`, `VMSTANDARD_7_00.db` and `Generic.db` |
| `vehicles\` | The 3-D vehicle geometry those databases name |

The program file is still called `hve-next.exe`; on screen the program calls
itself **HVE 2027 Preview**. All the physics programs, GATB included, are part
of it.

!!! note "HVE 2027"
    The preview has **no installer** and no update check, and it does not need a
    license to run (**Help › License...** shows the license and is where one is
    activated).
    Installing it is copying the folder; removing it is deleting the folder.
    A newer preview comes from EDC as a new folder.

### What the computer needs

- **64-bit Windows.**
- **A graphics driver with OpenGL 3.3.** If the driver cannot provide it, the
  program stops when it starts with an *OpenGL 3.3 required* message that names
  the renderer Windows supplied. This happens over Remote Desktop, in a virtual
  machine, or with an out-of-date graphics driver; update the driver, or run
  the program on the computer itself.
- **A mouse with a wheel or middle button** is recommended for moving the 3-D
  view (see the [Interface Tour](03-interface-tour.md#the-viewport)).

### Putting it on your computer

1. Copy the whole folder to a folder you can write to, for example
   `C:\HVE 2027 Preview` or a folder under *Documents*. Do not put it under
   *Program Files*: the program keeps its settings and its log in the folder it
   is started from (see below), and an ordinary user cannot write there.
2. If you want a desktop shortcut, right-click `hve-next.exe` and choose
   **Send to › Desktop (create shortcut)**. A shortcut made this way starts the
   program in its own folder, so the settings stay in one place.

The preview does not change HVE or its files and can be used on the same
computer as HVE. It opens HVE's `.hve` case files but never writes them, and it
does not take over the `.hve` file type: double-clicking a `.hve` file still
opens HVE.

## Starting the program and opening a case

Double-click `hve-next.exe` (or its shortcut). The window's title bar reads
**HVE 2027 Preview**, followed by the open case's file (*Untitled* until a case
is opened or saved) and its number of vehicles; a `*` in front means unsaved
changes.

To open a case:

- **File › Open Case...** (**Ctrl+O**) opens an HVE case (`.hve`) or an
  HVE 2027 case (`.hvc` or `.json`). **File › Open Recent** lists the cases
  opened or saved most recently.
- A case can also be named when the program is started, for example from a
  Command Prompt in the program's folder:

    ```bat
    hve-next.exe "C:\Cases\Intersection.hve"
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
(**Ctrl+R**). The [Interface Tour](03-interface-tour.md) describes the window.

## Where the program keeps its settings

The window layout, the recent-files list, the style and the preferences are
kept in small files in the folder the program is started from, which is the
program's own folder when you start it by double-clicking it or from a shortcut
made as above:

| File | Holds |
| --- | --- |
| `imgui.ini` | The window and panel layout |
| `hvenext.panels` | Which panels are open, the editor last used, and most display settings |
| `hvenext.recent` | The recent-files list |
| `hvenext.style` | The settings made in **Tools › Style Editor** |
| `hve_prefs.ini` | Other preferences, such as **Tools › Preferences › Auto-Save** |
| `hvenext.meshlib`, `hvenext.vdblib` | Geometry and database folders you have added |
| `hve_limits.ini` | Written when the **Limits Editor** saves to a file |

Deleting `imgui.ini` restores the default panel layout the next time the
program starts.

Vehicles saved with **Vehicle › Save Vehicle As** go, unless you choose another
file, into `userdb\user.db` in the same folder. Keep that folder (copy it
aside) if you remove or replace the preview.

## Log and crash files

When the program is started from Explorer or a shortcut, it writes everything
it reports to **`hve-next.log`** in the folder it was started from. The file is
started afresh each time the program starts, so copy it before restarting if
you need it. A line near the top beginning `[hve] build` names the build.

If the program crashes it also writes **`hve-next.crash.txt`** in the same
folder.

Started from a Command Prompt or PowerShell window instead, the program prints
its messages in that window and writes no log file.

Two things the log answers that the window may not:

- **Run seems to do nothing.** The log says whether `hve-solver.exe` was found
  beside the program and what it returned. A run that a physics program refused
  also shows the reason in red at the right of the playback bar.
- **The window opens and closes, or stays black.** The last lines of the log say
  how far the program got.

Questions and problem reports about the preview go to EDC. With a problem
report, send the case file, the steps that produce the problem, the version
shown in **Help › About HVE 2027...**, and `hve-next.log` (and
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
  Library** dialogs (**Upload database files...**, **Upload mesh files...**,
  and the whole-folder buttons beside them).
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

!!! warning "Not in HVE 2027"
    Accounts, shared workspaces and cloud computing are not part of
    HVE 2027. Every edition computes on your own computer.

## The read-only viewer

A separate viewer edition of the program opens cases and plays back their
saved results. It has no editors and no physics programs at all, so it cannot
change or re-run a case. It is not part of the Windows preview package.

A case opened in the viewer shows results only if they were saved with it (a
`.hvr` results file beside the case, or a bundle published with its results;
see [Cases and Files](04-cases-and-files.md)). A bundle published without
results opens with a message saying so. The viewer shows one event's results —
the event that was on screen when the case was saved — and a case with several
solved events says how many it holds; saving it from the viewer keeps all of
them.

A solved case can also be passed to someone else as a published bundle, which
opens in HVE 2027 itself or, from a link, in the browser version (see
[Publish Bundle](04-cases-and-files.md#publish-bundle)).

## Command-line tasks

Besides opening a case, the program accepts a few tasks on its command line.
Run them from a Command Prompt or PowerShell window opened in the program's
folder; their messages appear in that window. All but the last run without
opening the program's window.

| Command | Does |
| --- | --- |
| `hve-next.exe --version` | Prints which build this is: the same build identifier that **Help › About HVE 2027...** shows |
| `hve-next.exe --convert-case <in> <out>` | Opens a case (for example an HVE `.hve`) and writes it as `.hvc` (if `<out>` ends in `.hvc`) or JSON. Stops if a vehicle's geometry cannot be found; add `--allow-missing-geometry` after `<out>` to write it anyway |
| `hve-next.exe --export-bundle <case> <folder> [title] [--inputs-only] [--with-capture]` | Solves the case and publishes it as a self-contained folder; refuses if the case cannot be solved, unless `--inputs-only` is given. See [Publish Bundle](04-cases-and-files.md#publish-bundle) |
| `hve-next.exe --serve=PORT` | Starts the program normally, with the Blender live link already listening on PORT (`--serve` alone uses port 17690). See [Exporting to Blender and glTF](../new-features/06-exporting-to-blender-and-gltf.md) |
