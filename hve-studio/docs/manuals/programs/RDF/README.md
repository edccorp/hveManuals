# ReadDataFile — User's Manual

**Collision Engineering Associates, Inc. — for the HVE (Human Vehicle Environment) simulation environment**

Updated Markdown edition, converted from the legacy ReadDataFile manual (manual printed August 17, 2004) and revised to match the behavior of the current HVE release.

*(updated: the 2004 manual documents data-file format version 3.500. The current ReadDataFile calculation method reports program version 19.03, but still reads the version 3.200 and 3.500 data-file formats described in this manual. Within HVE, this manual is installed as `ReadDataFile.pdf` and opened from the Help > User Manuals menu.)*

*HVE is a trademark of Engineering Dynamics Corporation. ReadDataFile was written by Collision Engineering Associates, Inc. (Daniel J. Kuhn). Portions copyright Engineering Dynamics Corporation.*

## What is ReadDataFile?

ReadDataFile is an HVE-compatible physics program (calculation method) that imports time-based position and orientation data for vehicles and humans from a space-delimited ASCII data file, and turns that data into a normal HVE event. It is not a simulation: it interpolates externally generated motion data so that the standard HVE tools (Playback Editor, variable output tables, trajectory visualization) can be used with results from programs that have not been ported to HVE, from spreadsheets, or from any other calculation method.

## ReadDataFile in HVE Studio

HVE Studio runs ReadDataFile. HVE's own engine source is compiled as its own
isolated engine, and it reads the same `.dat` files, with the same header
rules and the same interpolation and differencing, as HVE does. What differs
is where the file is named and how a bad file is treated:

- **The data file is a field of the event**, not the event's name. In the
  **Event Information** panel, choose **READDATAFILE** as the **Method**; a
  **Data file** box and a **Browse...** button appear beneath it. A relative
  path is looked up as given (from the working directory) and then in the
  folder the case file is in. HVE instead takes the file name from the event
  name (*File:CarMotion.dat*) and looks for it in its install directory.
  When an HVE case is opened, each ReadDataFile event's **Data file** is filled
  from its name the same way HVE reads it: the first five characters
  (`File:`) are dropped. The case's own `.dat` files still have to be placed
  beside the case (or the path edited), because HVE does not store them in
  the case.
- **The file is checked before the run, and a bad one is refused** with the
  reason in the run status (stop code -5400): a missing file, a token that is
  not a number, a time block cut short, times that do not increase, a first
  time after 0, a vehicle count that differs from the event's, an axle count
  larger than the vehicle has, or a tire-data key the program does not
  recognize when the file has tire lines. HVE's program does not check these:
  it keeps the last values it read and reports the run as complete.
- **Humans are replayed.** Each human the file declares must be selected in
  the event (the counts must match, as in HVE) and must have a body. Its
  pelvis position and orientation are taken in the **first vehicle's** axes,
  as HVE's program places it, and the fourteen joint angles are each relative
  to the parent segment; the body is drawn from those angles on the human's
  own segments and joints. The run publishes the human output variables HVE's
  program publishes: the pelvis position and orientation and the fourteen
  joint angles. Other segment positions are not published by the program and
  read as unavailable; there are no human velocities or accelerations.
- If the file ends before the event's **Max Time**, the replay ends at the
  file's last time, as in HVE, and the run status says so.
- There is no debug file (HVE writes `ReadDataDebugFile.prn`).

The output is the same set of variables HVE's ReadDataFile publishes:
position and orientation, velocities and rates obtained by differencing, and
accelerations obtained by differencing again. For HVE's own case
*00TestingReadDataFile*, with each `.dat` rebuilt from the positions HVE
saved, every one of those derived variables matches HVE's saved values (the
original `.dat` files are not available, so this compares the differencing,
not the original files).

**The wheel variables carry ReadDataFile's own slot use, not their names.**
HVE's ReadDataFile writes each wheel's replayed **steer** angle into the
wheel variable the output tables call **Camber Angle**, the camber (a 3-D
file's wheel roll) into **Solid Axle Deflection** and the spin angle (a 3-D
file's wheel pitch) into **Solid Axle Roll**; **Steer Angle** is not written
and reads 0. HVE Studio keeps those variables exactly as HVE publishes them, so
to graph or tabulate a replayed steer angle, select **Camber Angle**. The
wheels drawn in the 3-D view are not affected by this: they take their steer,
camber and spin from the slots ReadDataFile actually writes, so a replayed
front wheel turns.

The chapters below describe HVE's ReadDataFile and its data-file format.
Where HVE Studio differs, the chapter says so.

## Contents

- [1 — Program Description and 2 — Program Input](01-program-description-and-input.md)
- [3 — Calculation Method](02-calculation-method.md)
- [4 — Data File Format (with examples)](03-data-file-format.md)

<!-- NAV -->

---

Next: [Chapter 1 — Program Description](01-program-description-and-input.md) →

<!-- /NAV -->
