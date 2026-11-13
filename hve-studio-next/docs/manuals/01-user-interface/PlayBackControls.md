# Playback Controls (Toolbar)

As in HVE, the playback controls run the current event and then replay it: the **playback controls** in the toolbar at the top, after the editor buttons (on a row of their own when the window is narrow; **View › Playback Controls in Toolbar** off puts them in a strip along the bottom of the Viewport panel instead; **View › Playback Controls in a Window** puts them, with the toolbar's event and vehicle pickers, in a **Playback Controls** window that can be docked above or below the 3-D view). Until the event is executed, **Play** is its only control and it runs the event; while the run is going the same button pauses it, and **Play** continues it from the same instant; once executed, the bar plays the results. An event can also be run from the **Run** stage of the **Event Designer** (**Event › Event Designer...**, or **Ctrl+R**). The **Playback** editor (**Playback (F6)**) plays a multi-event playback sequence with the same bar, with **Run All** (solve every event the sequence uses) in place of the state. The controls, from left to right:

## Run state
The active event's run, in words: **Not run**, **Running *n*%**, **Paused at *t* s**, **Completed**, **Stopped early** (the run ended before its duration; the status text says why), **Failed**, **Canceled** (or **Canceled (partial)** when it kept what it had solved), or **Saved results** (shown from the case's saved results file, not re-solved). Click it to open the Run stage. While a run is in progress **Stop** follows it: it ends the run there, and what was solved is kept and can be played. Once the event has been run, **Reset** follows it (HVE's Stop button): it throws the results away so the inputs can be edited, and **Play** then runs the event again.

## Run simulation and Reset (the Run stage)
On the Run stage, **Run simulation** runs the active event. It is the stage's one primary button, at the top of the stage and drawn in the accent color. The stage has no playback buttons of its own: they are the toolbar's. It is grayed when the event is already solved; press **Reset** to run it again. **Reset** discards the results on screen and returns the simulation to its starting conditions; it is grayed when the event has not been run. The inputs a run was solved from are locked while its results are on screen, and Reset unlocks them, so editing can never make old results look like the inputs' own. Above **Run simulation** a line says whether the event is **Ready** or how many Guidance items there are **to fix** (marked **!**) and **to consider**, with the first of them; neither kind stops the run.

## |<  (Jump to start)
Places the playback at the starting time.

## <<  (Step back)
Steps back one output step (or the number of output steps set as the frame step in **Output › Playback Options...**, Event Editor), and pauses.

## Play / Pause
Before the event is executed, runs it (it is the only control then). While the run is going, **Pause** parks it at the current time and **Play** continues it from there (a run solving in another process cannot be paused; **Stop** ends it). Once executed, starts (or resumes) playback, or pauses it.

## >>  (Step forward)
Steps forward one output step (or the frame step), and pauses.

## >|  (Jump to end)
Places the playback at the end of the run.

## Time slider
A slider to set the playback time directly; drag it to move to any point in the event, or turn the mouse wheel over it to step one frame (one output step). It takes what the row leaves. In the toolbar, beside **<<** and **>>**, it has no step buttons of its own (they did the same thing, 2026-11-10); in the strip at the bottom of the Viewport, a row of its own away from the transport, the small **<** and **>** buttons beside it step one frame back or forward.

## Time entry
Type a time in seconds and press Enter to jump there.

## Status text
After the playback time: the run's duration, the event's calculation method and, for a run with a result, a headline Delta-V; or why the run stopped or failed. Before a run it reads *[method] Not executed -- Play runs it*; while a run is going it reads *[method] running: t = 1.23 of 2.50 s (49%)* -- the event time the engine has reached, of its duration -- or *PAUSED at ...*.

!!! note "HVE Studio"
    The times HVE shows on its toolbar (maximum simulation time, integration time step, output time interval) are on the **Run** stage of the **Event Designer** (**Event › Event Designer...**), where they are also edited. The current frame number is not shown.

!!! warning "Not in HVE Studio"
    **Reverse** (playing the event backwards).

<!-- NAV -->

---

← Previous: [Overlays Dialog Box](OverLayDlg.md)  |  [Index](README.md)  |  Next: [User Preferences Dialog Box](PrefDlg.md) →

<!-- /NAV -->
