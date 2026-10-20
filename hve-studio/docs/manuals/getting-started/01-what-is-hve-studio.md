# What is HVE Studio?

HVE Studio is the next version of HVE: HVE's own physics programs in a new
interface. The physics programs — EDCRASH, EDSMAC, EDSMAC4, EDGEN, EDHIS,
SIMON (with DyMESH), EDSVS, EDVDS, EDVTS, EDVSM and GATB — are HVE's own code.
The user interface, the case file formats, the 3-D rendering and the way the
programs are started are new.

## What "Preview" means

This release is **HVE Studio**, and the program says so in its title bar
and its About box. HVE Studio does not yet do everything the current release of
HVE does; "Preview" is dropped from the name when it does. Until then:

- everything HVE does that HVE Studio does not is listed in one place,
  [Not available in HVE Studio](05-differences-from-hve.md#not-available-in-hve-studio),
  and every page of this manual set that describes such a feature carries a
  **Not in HVE Studio** box saying so;
- the current release of HVE remains the program to use for anything on that
  list. HVE Studio can be used on the same computer: it opens HVE's `.hve` cases
  but never writes them (see [Installing and Running](02-installing-and-running.md)).

Questions and problem reports about the preview go to EDC.

## The physics is HVE's

HVE's physics is a set of C++ libraries that Engineering Dynamics Company
builds into the shipped HVE program. HVE Studio compiles **the same source code**
(the HVE source release from which the shipped HVE binaries are built) into one
physics library, with the Windows/MFC dependencies removed.

This has been checked file by file, not assumed. Every physics source file that
is not identical to HVE's is listed and classified, and the differences fall
into a small number of kinds:

- changes needed to build the code without Microsoft's MFC library and on
  compilers other than Visual C++;
- diagnostic printouts that are off unless switched on for debugging;
- fixes for crashes and endless loops (a run that HVE would hang on stops with
  an error message instead);
- **three deliberate changes to a calculation**, described in
  [Differences from HVE](05-differences-from-hve.md#physics-differences-by-design).

So the program manuals in this set — program descriptions, calculation
methods, equations and messages — apply to HVE Studio as written, except where a
page is marked otherwise.

!!! note "HVE Studio"
    Results are the physics programs' own. HVE Studio does not re-implement or
    approximate an HVE program: a SIMON event is solved by SIMON, an EDCRASH
    reconstruction by EDCRASH. HVE Studio's results are compared, case by case,
    with the results HVE itself saved in EDC's tutorial and validation cases,
    and every difference found is recorded together with its cause.

## What is new

| Area | In HVE | In HVE Studio |
| --- | --- | --- |
| User interface | MFC dialogs and Open Inventor 3-D editors, Windows only | One window with dockable panels and an OpenGL 3-D view, on Windows and in a web browser |
| Editors | Separate Human, Vehicle, Environment, Event and Playback editors | Five editor tabs in one window — Human, Vehicle, Environment, Event and Playback. A solved event plays back in the Event editor's viewport; the Playback editor plays several solved events on one timeline |
| Case files | `.hve` | `.hvex` (binary) or `.json` (text). HVE's `.hve` files open directly; HVE Studio does not write `.hve` |
| Running a program | The event's program runs inside HVE | The event's **Calculation Method** chooses the program. On Windows each run is solved by `HVESolver.exe`, a separate program beside `HVEStudio.exe`; you do not start it yourself |
| 3-D view | Open Inventor | OpenGL renderer with node-based materials, shadows, cameras and keyframes (display only — nothing here changes a result) |

HVE Studio also adds a few capabilities HVE does not have: a single-track
(motorcycle) program, Monte Carlo uncertainty analysis, a text "Quick Case"
builder, a live link to Blender, and several additions to the physics inputs.
All of them are listed in
[Differences from HVE](05-differences-from-hve.md#new-in-hve-studio).

## Who it is for

- **HVE users** who want to open their existing `.hve` cases in the next
  version of HVE and run, inspect or present them there.
- **Reviewers and recipients** of a case. A solved case can be published as a
  self-contained folder that opens in HVE Studio, in the browser version or in
  the read-only viewer (see [Installing and Running](02-installing-and-running.md)).
- **Analysts who want to look inside a run.** HVE Studio exposes every output
  channel the programs write, marks the ones the programs never compute, and
  says when an input was not used or could not be represented, instead of
  silently substituting a default.

## What to expect if you know HVE

- **The inputs are HVE's inputs.** Vehicle, human, environment and event data
  are organised the way HVE organises them, under HVE's names, and most dialogs
  are ports of HVE's own dialogs. A few are merged, moved or split; the
  [Differences](05-differences-from-hve.md#user-interface-differences) page
  lists them.
- **Open your `.hve` cases directly.** **File › Open Case** reads HVE case files.
  Vehicles, the environment (including its terrain and aerial photograph),
  events, driver controls, calculation options and occupant data are imported.
  What is not imported is listed in [Cases and Files](04-cases-and-files.md).
- **The editors are tabs.** Press **F2**–**F6** (Human, Vehicle, Environment,
  Event, Playback) instead of choosing an editor from a menu. The menu bar
  changes with the tab: the **Occupant** menu appears in the Human editor, the
  **Vehicle** menu in the Vehicle editor, the **Event** and **Output** menus in
  the Event editor, and so on.
- **A single event plays back where it is set up.** Press **Run** on the
  playback bar under the viewport (or **Output › Run Simulation**) and the
  solved event plays back in the Event editor's own viewport. Reports, graphs
  and tables are on the **Output** menu. Several events on one timeline — HVE's
  Video Creator — is the **Playback (F6)** editor (see
  [Video and Playback Sequences](../new-features/07-video-and-playback-sequences.md)).
- **A solved event is locked.** While results are on screen, the inputs they
  were computed from are read-only, so the results and the inputs shown can
  never disagree. Press **Reset** to edit again.
- **Units.** The display is US customary or SI, set in **Tools › Preferences**.
  There is no custom unit mix.
- **HVE Studio tells you when it had to assume something.** When an import could
  not represent a value, an engine was handed a default, or an option is not
  read by the selected program, the dialog or the run status says so. Longer
  explanatory notes are hidden by default and shown with
  **View › Show Guidance Text**; a note about a problem with the open case is
  always shown.
