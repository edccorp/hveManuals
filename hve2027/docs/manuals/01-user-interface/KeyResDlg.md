# Key Results Dialog Box

HVE displays a separate Key Results window, titled *Key Results-\<object name\>*, for each human and vehicle in the event. HVE 2027 has **one Key Results panel** for the active event, with a column per vehicle. Open it with **View › Key Results**, or with **Output › Key Results...** in the Event Editor. Like every panel it can be docked or floated. Values are shown in the units set in Preferences.

The panel has three collapsible sections. Their order can be changed and is remembered.

## Summary

The event's headline results, one column per vehicle: for example impact speed, initial velocity, Delta-V (acceleration based and velocity based), PDOF, impact duration and force, collision energy loss, damage energy, separation speed, final speed, maximum speed, distance traveled, heading change, maximum accelerations, yaw rate and side slip, final position, time to rest, occupant peak accelerations and HIC exceedance, and the number of damaged vertices. Which rows appear depends on the event's calculation method: a reconstruction shows its reconstruction results, a simulation its trajectory results.

## vs. original HVE

When the case was opened from an HVE file that carries HVE's own saved results, this section compares HVE 2027's results with HVE's: **Vehicle / quantity**, **Ours**, **Original HVE**, **Difference** and **at t** (the time compared).

## Trajectory

A table of the variables chosen for this event, one row per output time step. It is HVE's key variable grid, shown for the whole run rather than for one instant.

### Select Variables...
Opens the [Variable Selection Dialog Box](../11-reports-output/VarSelDlg.md) to choose the table's columns. Each event keeps its own selection, and the Output Graph keeps a separate one.

### Export CSV..., Copy CSV
Write the table to a CSV file, or copy it to the clipboard. The export includes every selected variable even when the table shows only the first ones.

### Follow playback time
Highlights the row at the current playback time and keeps it in view.

### Group columns by Variable / Vehicle, Vehicle name in column titles
Arrange the columns by variable or by vehicle, and prefix each column title with its vehicle.

!!! note "HVE 2027"
    One panel for the event instead of one window per object, and a full time history instead of the value at the current time step. The **Select Variables...** button is available for every event.

!!! tip "New in HVE 2027"
    The **Summary** and **vs. original HVE** sections, and CSV export.

See also the *Key Results* preference in HVE's User Preferences dialog, which HVE 2027 does not have ([User Preferences Dialog Box](PrefDlg.md)).

<!-- NAV -->

---

← Previous: [Camera Setup Dialog Box](CameraSetDlg.md)  |  [Index](README.md)  |  Next: [Light Editor Dialog Box](LightEdDlg.md) →

<!-- /NAV -->
