# Playback Controls (Toolbar)

In HVE the playback controls on the toolbar control execution of the current event during Event mode, and replay during Playback mode. In HVE Studio an event is **run** on the **Run** stage of the **Event Designer** (**Event › Event Designer...**, or **Ctrl+R**), and **played back** with the **playback bar** along the bottom of the Viewport panel. The bar shows the run's state where HVE had its execution buttons; the **Playback** editor (**Playback (F6)**) plays a multi-event playback sequence with the same bar, with **Run All** (solve every event the sequence uses) in place of the state. The controls, from left to right:

## Run state
The active event's run, in words: **Not run**, **Running *n*%**, **Paused at *t* s**, **Completed**, **Stopped early** (the run ended before its duration; the status text says why), **Failed**, **Canceled** (or **Canceled (partial)** when it kept what it had solved), or **Saved results** (shown from the case's saved results file, not re-solved). Click it to open the Run stage. While a run is in progress, **Pause** / **Resume** (when the engine allows pausing) and **Cancel** follow it, so a run can be stopped from where it is watched.

## Run simulation and Reset (the Run stage)
On the Run stage, **Run simulation** runs the active event. It is the stage's one primary button and is drawn in the accent color, set apart from the playback buttons beside it. It is grayed when the event is already solved; press **Reset** to run it again. **Reset** discards the results on screen and returns the simulation to its starting conditions; it is grayed when the event has not been run. The inputs a run was solved from are locked while its results are on screen, and Reset unlocks them, so editing can never make old results look like the inputs' own. Above **Run simulation** a line says whether the event is **Ready** or how many Guidance items there are **to fix** (marked **!**) and **to consider**, with the first of them; neither kind stops the run.

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
After the playback time: the run's duration, the event's calculation method and, for a run with a result, a headline Delta-V; or why the run stopped or failed. Before a run it reads *[method] Press Run to execute* (the Run stage's **Run simulation**).

!!! note "HVE Studio"
    The times HVE shows on its toolbar (maximum simulation time, integration time step, output time interval) are on the **Run** stage of the **Event Designer** (**Event › Event Designer...**), where they are also edited. The current frame number is not shown.

!!! warning "Not in HVE Studio"
    **Reverse** (playing the event backwards).

<!-- NAV -->

---

← Previous: [Overlays Dialog Box](OverLayDlg.md)  |  [Index](README.md)  |  Next: [User Preferences Dialog Box](PrefDlg.md) →

<!-- /NAV -->
