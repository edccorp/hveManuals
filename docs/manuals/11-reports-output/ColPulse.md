# Collision Pulse

The Collision Pulse dialog (title: *Collision Pulse: [vehicle name]*) is used to assign a collision pulse to the selected vehicle, for use by occupant simulation models. The top of the dialog contains a graph of the current pulse versus time; below it is a data grid containing the numeric pulse table.

## Pulse Data Source

Drop-down list selecting where the pulse data come from. The list contains:

- The current file name (or an *Untitled* entry for manually entered data). Pulse data may be typed directly into the data grid or loaded from a file using **Open...**.
- Each other event in the current case that (a) includes the same vehicle and (b) produces the currently selected pulse type. Selecting an event imports the pulse calculated by that event's simulation.

## Pulse Type

Drop-down list selecting the type of pulse. Possible entries are:

- **Position** — position vs. time (X, Y, Z, Roll, Pitch, Yaw)
- **Velocity** — velocity vs. time (u, v, w, roll, pitch and yaw velocities)
- **Acceleration** — acceleration vs. time (linear and angular acceleration components)
- **Force/Moment** — force and moment vs. time (Fx, Fy, Fz, Mx, My, Mz)

Only the pulse types supported by the current event's physics program are shown. The columns in the data grid (Time plus six degrees of freedom) change according to the selected type. Changing the type after entering data prompts for confirmation because the existing table is discarded.

## Data Grid

Editable table of pulse values: one row per time point, with a Time column followed by the six degree-of-freedom columns for the selected pulse type. Data may also be pasted from the clipboard.

## Apply

Validates the entered table and saves it to the event without closing the dialog, then redraws the graph.

## Print...

Saves the current table and prints the pulse graph.

## Factors...

Displays the Collision Pulse In-Use Factors dialog, used to assign a multiplier to each degree of freedom of the pulse.

## New

Clears the pulse table (after confirmation if data have been entered), resets the data source to *Untitled*, resets the pulse options (threshold, Tstart, impulse center) to zero and the in-use factors to 1.0, and redraws the graph.

## Open...

Displays a file dialog for loading a pulse from a file. The file filter depends on the selected pulse type: `*.PosPulse` (position), `*.VelPulse` (velocity), `*.AccPulse` (acceleration) or `*.ImpPulse` (force/moment).

## Save As...

Saves the current pulse table to a `.PosPulse`, `.VelPulse`, `.AccPulse` or `.ImpPulse` file, according to the selected pulse type.

## Options...

Displays the Collision Pulse Options dialog, used to extract a portion of the total pulse and, for a Force/Moment pulse, to assign the impulse center.

## OK / Cancel

OK validates and saves the pulse data and closes the dialog; Cancel discards the changes.

---
*Source topic: ColPulse.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Collision Pulse Options Dialog Box](ColPulOptDlg.md)  |  [Index](README.md)  |  Next: [Common Reports Dialog Box](CommRepDlg.md) →

<!-- /NAV -->
