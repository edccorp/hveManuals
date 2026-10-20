# Variable Output: Graph Dialog

HVE's Variable Output Graph dialog plotted the first six selected output
variables against time. In HVE Studio this is the **Output Graph** panel: **Output ›
Output Graph...** (or **View › Output Graph**) in the Event (F5) or Playback (F6) editor.

Before a run the panel says *Run simulation to see output graph*. After a run it
plots the selected variables against simulation time, in the units set in
Preferences, each trace in its own colour with a legend entry.

Drag the legend to move it within the graph. Right-click it to put it in a
corner (**Top left**, **Top right**, **Bottom left**, **Bottom right**) or
choose **Hide legend**; the **Legend** check box beside **Close** shows it
again.

- **Select Variables...** — opens [Select Output Variables](VarSelDlg.md) for the
  graph's traces. The graph keeps its own selection, separate from the Key
  Results table.
- A line gives the number of traces and the sampling interval (the run's output
  step, or a coarser one if the graph is thinning a long run).
- **Format...** — the graph's formatting:
  - **Traces** — each trace's colour (with **Reset**), and **Vehicle name in the
    legend**. A trace colour is remembered for the session only.
  - **Value axis** — automatic or a fixed range, with **Fit**.
  - **Time axis** — the whole run or a chosen range, with **Whole run**.
  - **Gridlines and colour**, and **Reset formatting**.
- **Close** closes the panel.

In the Playback editor, with a playback sequence selected, the graph follows
the **sequence**: its time axis is the master clock, from 0 to the end of the
sequence, and each vehicle's trace comes from whichever event places that
vehicle at each instant, as the 3-D view draws it. A dotted vertical line
labelled with the vehicle and the event's name marks where a vehicle passes
from one event to the next. Occupant traces come from the active event on its
own track. Overlaying other events is not offered there, because the sequence
already puts its events on one timeline. With no sequence selected the graph
shows the active event, as in the Event editor.

!!! note "HVE Studio"
    The graph is not limited to six variables. There is no **Print...**; to keep
    the data, use **Export CSV...** in Key Results, or **Output › Export
    Variables...**.

<!-- NAV -->

---

← Previous: [Variable Output Edit Dialog](VarOutEdDlg.md)  |  [Index](README.md)  |  Next: [Selecting Variables](VarSelDlg.md) →

<!-- /NAV -->
