# Variable Output: Graph Dialog

HVE's Variable Output Graph dialog plotted the first six selected output
variables against time. In HVE Studio this is the **Output Graph** panel: **Output ›
Output Graph...** (or **View › Output Graph**) in the Event (F5) or Playback (F6) editor.

Before a run the panel says *Run simulation to see output graph*. After a run it
plots the selected variables against simulation time, in the units set in
Preferences, each trace in its own color with a legend entry. A yellow vertical
line marks the current playback time.

Click anywhere in the plot to move playback to that time, or drag across it to
scrub; playback pauses first. A click past the end of the run (the time axis can
be longer when other events are overlaid) stops at the end.

Drag the legend to move it within the graph. Right-click it to put it in a
corner (**Top left**, **Top right**, **Bottom left**, **Bottom right**) or
choose **Hide legend**; the **Legend** check box beside **Close** shows it
again.

- **Select Variables...** — opens [Select Output Variables](VarSelDlg.md) for the
  graph's traces. The graph keeps its own selection, separate from the Key
  Results table.
- A line gives the number of traces and the sampling interval (the run's output
  step, or a coarser one if the graph is thinning a long run).
- **X axis** — **Time** (the default), or one of the selected variables. With
  a variable chosen, every other selected trace is drawn against it instead of
  against time: an X-Y plot. Choose **Fwd Accel** as the X axis with
  **Lateral Accel** selected to get the g-g diagram (lateral against forward
  acceleration), or plot a tire's lateral force against its slip angle. In an
  X-Y plot:
  - A yellow dot on each trace marks the current playback time. Click or drag
    in the plot to move playback to the time of the nearest drawn point.
  - The **Time axis** range (in **Format...**) chooses which part of the run is
    drawn, for example only the time spent skidding.
  - **Equal scale** makes one unit the same length across and down, so a
    friction circle draws round. It is meaningful when both axes are in the
    same unit.
  - The X variable is named at the plot's bottom right instead of in the legend.
- **New Graph** — opens another Output Graph (also **Output › New Output
  Graph**); see *More than one graph* below.
- **Format...** — the graph's formatting:
  - **Traces** — each trace's color (with **Reset**), and **Vehicle name in the
    legend**. A trace color is remembered for the session only.
  - **Value axis** — automatic or a fixed range, with **Fit**.
  - **Time axis** — the whole run or a chosen range, with **Whole run**.
  - **Gridlines and color**, and **Reset formatting**.
- **Close** closes the panel.

In the Playback editor, with a playback sequence selected, the graph follows
the **sequence**: its time axis is the master clock, from 0 to the end of the
sequence, and each vehicle's trace comes from whichever event places that
vehicle at each instant, as the 3-D view draws it. A dotted vertical line
labeled with the vehicle and the event's name marks where a vehicle passes
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

## More than one graph

**New Graph**, or **Output › New Output Graph**, opens another graph: *Output
Graph 2*, *Output Graph 3* and so on, up to six. Each has its own variables
(chosen per event, as for the first), X axis, axis ranges, trace colors,
legend and overlaid events, so a g-g diagram, speed against time and a tire
force can all be on screen at once. A new graph starts against time with the
default variables, in the first graph's style (gridlines, colors, line
width). All graphs follow the same playback: clicking in any of them moves
every one. Close a graph with its window's close button; which graphs are
open is remembered with the panel layout.
