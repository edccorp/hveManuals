# Playback Controls (Toolbar)

In HVE the playback controls on the toolbar control execution of the current event during Event mode, and replay during Playback mode. In HVE Studio an event is run and played back in the Event Editor's **Viewport**, with a **playback bar** along the bottom of the Viewport panel; the **Playback** editor (**Playback (F6)**) plays a multi-event playback sequence with the same bar, with **Run All** (solve every event the sequence uses) in place of **Run** and **Reset**. The controls, from left to right:

## Run
Runs the active event (also **Output › Run Simulation...** in the Event Editor, **Ctrl+R**). It is greyed when the event is already solved; press **Reset** to run it again. While a run is in progress, **Run** is replaced by **Pause** / **Resume** (when the engine allows pausing) and **Cancel**.

## Reset
Discards the results on screen and returns the simulation to its starting conditions. The inputs a run was solved from are locked while its results are on screen; Reset unlocks them.

## |<  (Jump to start)
Places the playback at the starting time.

## <<  (Step back)
Steps back one output step (or the number of output steps set as the frame step in **Output › Playback Options...**, Event Editor), and pauses.

## Play / Pause
Starts (or resumes) playback, or pauses it.

## >>  (Step forward)
Steps forward one output step (or the frame step), and pauses.

## >|  (Jump to end)
Places the playback at the end of the run.

## Camera list
The active saved camera; see [Camera Setup Dialog Box](CameraSetDlg.md). **C** and **Shift+C** cycle the saved cameras.

## Time slider, < and >
A slider to set the playback time directly; drag it to move to any point in the event. The small **<** and **>** buttons beside it step one frame (one output step) back or forward.

## Time entry
Type a time in seconds and press Enter to jump there.

## Status text
After the playback time: the run's duration, the event's calculation method and, for a run with a result, a headline Delta-V; or why the run stopped or failed. Before a run it reads *[method] Press Run to execute*.

!!! note "HVE Studio"
    The times HVE shows on its toolbar (maximum simulation time, integration time step, output time interval) are in the **Simulation** panel (**View › Simulation**), where they are also edited. The current frame number is not shown.

!!! warning "Not in HVE Studio"
    **Reverse** (playing the event backwards).

<!-- NAV -->

---

← Previous: [Overlays Dialog Box](OverLayDlg.md)  |  [Index](README.md)  |  Next: [User Preferences Dialog Box](PrefDlg.md) →

<!-- /NAV -->
