# Variable Output Report

HVE's Variable Output table showed the simulation results of an event as a
function of time, for the variables chosen in the Variable Selection dialog.

In HVE 2027 this table is the **Trajectory** section of the **Key Results**
panel: **Output › Key Results...** (or **View › Key Results**) in the Event
editor (F5). Two related windows cover other parts of the same need — see
[Variable Report and Timestep Data](#variable-report-and-timestep-data) below.

The panel has three collapsible sections (right-click a header to move or hide
it):

- **Summary** — the run's key results per vehicle: impact speed, delta-V (both
  acceleration-based and velocity-based), PDOF, impact duration and force,
  energies, separation speeds, final position, speeds, peak accelerations,
  occupant peaks, and so on, in the units set in Preferences. A value the run
  did not compute is shown as `--`.
- **vs. original HVE** — for a case imported from HVE that carries HVE's own
  saved results, those results beside HVE 2027's.
- **Trajectory** — the time table described below.

Before a run the panel says *Run simulation to see results*.

## Trajectory table

The first column is **Time (s)**, one row per output step. Each further column is
one selected variable for one vehicle, with the vehicle, the variable name and
its units in the header. Only a limited number of columns are displayed at
once; scroll sideways for the rest, and a line says how many are shown.

- **Select Variables...** — opens [Select Output Variables](VarSelDlg.md) for this
  table's columns (each event keeps its own selection).
- **Export CSV...** — writes the table, with every selected column, to a CSV
  file.
- **Copy CSV** — copies the same text to the clipboard, ready to paste into a
  spreadsheet.
- Click a row to move playback to that instant; **Follow playback time** keeps
  the table scrolled to the current playback time.
- **Group columns by** — **Variable** or **Vehicle**; **Vehicle name in column
  titles** adds the vehicle's name to each header.

!!! note "HVE 2027"
    A value the run did not compute (for example a channel that is not finite)
    is shown as `--` rather than a number. Variable names that no engine
    computes carry *(not computed)* in their name, and they read zero for every
    run — in HVE as well.

## Graph...

Use the **Output Graph** panel — see [Variable Output: Graph](VarOutGraphDlg.md).

## Edit...

!!! warning "Not in HVE 2027"
    Editing non-calculated output variables is not available — see
    [Variable Output Edit](VarOutEdDlg.md).

## Variable Report and Timestep Data

- **Output › Variable Report...** opens the **Variable Output Report** window: a
  short summary table with one row per variable per vehicle (**Variable**,
  **Vehicle**, **Min**, **Max**, **Final**, **Units**) — speed and heading, final X
  and Y, and for the first two vehicles delta-V, impact speed, PDOF and damage
  energy. A file name and **Save** write it to a text file.
- **Output › Timestep Data Table...** opens the **Timestep Data** window: every
  vehicle's **X**, **Y**, heading and speed at every output step, with no
  variable selection. **Export CSV...** and **Copy** write it out; the exported
  values are always in SI (m, km/h), and each CSV header names its unit.
- **Output › Export Variables...** writes the selected variables of the event
  on screen to a file, with a choice of format, interval and coordinate
  system.

<!-- NAV -->

---

← Previous: [Variable Output: Graph Dialog](VarOutGraphDlg.md)  |  [Index](README.md)  |  Next: [Selecting Variables](VarSelDlg.md) →

<!-- /NAV -->
