# Variable Output: Graph Dialog

HVE's Variable Output Graph dialog plotted the first six selected output
variables against time. In HVE 2027 this is the **Output Graph** panel: **Output ›
Output Graph...** (or **View › Output Graph**) in the Event editor (F5).

Before a run the panel says *Run simulation to see output graph*. After a run it
plots the selected variables against simulation time, in the units set in
Preferences, each trace in its own colour with a legend entry.

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

!!! note "HVE 2027"
    The graph is not limited to six variables. There is no **Print...**; to keep
    the data, use **Export CSV...** in Key Results, or **Output › Export
    Variables...**.

<!-- NAV -->

---

← Previous: [Variable Output Edit Dialog](VarOutEdDlg.md)  |  [Index](README.md)  |  Next: [Variable Output Report](VarOutRepDlg.md) →

<!-- /NAV -->
