# Key Results Dialog Box

HVE displays a separate Key Results window, titled *Key Results-\<object name\>*, for each human and vehicle in the event. HVE 2027 has **one Key Results panel** for the active event, with a column per vehicle. Open it with **View › Key Results** or **Output › Key Results...** in the Event or Playback editor; it is not available in the Human, Vehicle or Environment editors. Like every panel it can be docked or floated. Values are shown in the units set in Preferences.

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

## In the Playback editor

With a playback sequence selected, the panel follows the **sequence** rather than the active event:

- **The columns are the sequence's vehicles**, in the order they first appear over its tracks, so a vehicle that only a later event moves still has a column.
- **Summary** shows one block per event on the timeline, headed with the event's name and the time it starts on the master clock. An event that has not been solved says so; run it with **Run All Events** in Playback, or in the Event editor.
- **Trajectory** is sampled on the sequence's master clock, and its time column is that clock: the same time the transport, the playback cursor and **Follow playback time** use. Each vehicle's value comes from the event that places that vehicle at that instant, exactly as the 3-D view draws it, so a row can hold values from two events.
- Occupant variables are read from the active event, at that event's own time on its track, and are blank where the active event is not on the timeline.
- **vs. original HVE** compares one event with HVE's saved run, so it is not shown here; open the event in the Event editor to see it.

With no sequence selected, the Playback editor shows the active event as the Event editor does.

Click a row to move playback to that instant. A value the run did not compute (for example a channel that is not finite) is shown as `--` rather than a number. Variable names that no engine computes carry *(not computed)* in their name, and they read zero for every run — in HVE as well.

Position (X, Y), heading and speed are chosen with **Select Variables...** like any other channel. **Output › Export Variables...** writes the selected variables to a file, with a choice of format, interval and coordinate system.

!!! note "HVE 2027"
    One panel for the event instead of one window per object, and a full time history instead of the value at the current time step. The **Select Variables...** button is available for every event.

!!! tip "New in HVE 2027"
    The **Summary** and **vs. original HVE** sections, and CSV export.

See also the *Key Results* preference in HVE's User Preferences dialog, which HVE 2027 does not have ([User Preferences Dialog Box](PrefDlg.md)).

<!-- NAV -->

---

← Previous: [Camera Setup Dialog Box](CameraSetDlg.md)  |  [Index](README.md)  |  Next: [Light Editor Dialog Box](LightEdDlg.md) →

<!-- /NAV -->
