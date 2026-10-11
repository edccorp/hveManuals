# Video and Playback Sequences

This chapter covers two things HVE did in its Playback editor: combining
several events on one timeline (HVE's *Video Creator*), and writing a video
file. HVE 2027 has a Playback editor too: the **Playback (F6)** tab.

## Playback sequences

!!! tip "New in HVE 2027"
    In HVE the timing of each event lived on the event itself, was reset when
    the Video Creator closed, and only one arrangement could exist. In HVE 2027
    a **playback sequence** belongs to the case: up to eight named sequences
    can be kept, each arranging the same events differently, and they are saved
    with the case.

A playback sequence plays several **solved** events on one timeline, each with
its own start offset and trim: event A plays, then event B; or both at once;
or two reconstructions of the same crash aligned at their impact instants for
comparison.

### Making a sequence

1. Click the **Playback (F6)** tab. Its **Playback Sequence** panel opens with
   the other editors' panels (**Playback › Playback Sequence...** reopens it).
2. Press **New**. The new sequence takes every event in the case, laid end to
   end, and becomes the active sequence. (Its default name is *Sequence N*;
   change it in **Name**.)
3. Press **Run All Events** to solve every event the sequence uses, one after
   another. The window is busy until they finish; an event that has no result
   yet shows **not solved** in the *Result* column and contributes nothing.
4. Arrange the tracks (below), and play with the playback bar as usual.

![The Playback Sequence window](images/hvn-playback-sequence.png)

### The track table

One row per track:

| Column | Meaning |
| --- | --- |
| **On** | Include this track. A track switched off is ignored, and does not count toward the duration. |
| **Event** | Which event the track plays (with a colour key matching the timeline strip) |
| **Start (s)** | Where the track starts on the sequence timeline |
| **End (s)** | Where it ends on the sequence timeline |
| **Offset (s)** | Where the event's own t = 0 sits on the sequence timeline |
| **Result** | The event's solved duration, or **not solved** |
| **Remove** | Drop the track |

Start and End are entered in **sequence** time, but stored as a trim of the
event's own time, so changing **Offset** slides the whole track without
changing which part of the event it plays. An End at the event's own end keeps
following the event: if the event is re-solved longer, the track grows with it.

The **Duration** beside the name is the latest track end among the tracks
switched on.

### The timeline strip

Under the table, each track is a coloured bar on the sequence timeline, with
the playback position marked in red.

- **Drag a bar** to slide that event in time (hold **Ctrl** to snap). One drag
  is one undo step.
- **Click elsewhere** in the strip to scrub.

### Arranging buttons

| Button | Does |
| --- | --- |
| **Add Event** | A new track (for the first event; change it in the Event column) |
| **Add All Events** | A track for every event not already in the sequence |
| **Stack Sequentially** | Lays every track that is switched on end to end, in table order |
| **Align at Impact** | Slides every track so its impact instant falls at the same sequence time — for comparing reconstructions. Tracks with no known impact time stay put. |
| **Run All Events** | Solves every event the sequence uses, one at a time |

The **Sequence** list at the top chooses the active sequence; **Delete**
removes it. There is no *single-event* entry: playing one event on its own is
what the **Event** editor does, whatever sequence is chosen.

### Which timeline is playing

The editor decides, and nothing else does:

| Editor | The viewport, the playback bar, Record Animation, glTF and the Blender link play |
| --- | --- |
| **Event (F5)** | the active event, on its own |
| **Playback (F6)** | the active playback sequence |

In the Playback editor:

- A **header** at the top of the viewport names the sequence and the time, and
  lists every track with its state at that time: **PLAYING** (marked `>`, with
  the event's own time), *waiting*, *done*, *off*, or **UNSOLVED** — an event
  with no result, which places nobody until **Run All Events** solves it.
- The **playback bar** reads *[sequence: name]*. Its left-hand button is
  **Run All**; there is no **Reset**, which throws away the active event's run
  and belongs to the Event editor.
- The vehicles are the sequence's: a vehicle no track places, or whose event is
  unsolved, is not drawn. Wheels steer and spin with the event holding the
  vehicle.
- **Occupants, trails and the velocity, collision and tire-force vectors are
  drawn only in the Event editor.** Each belongs to one event's run; on a
  sequence's clock they would show one event's data at another event's time.
  The header says so.

### How vehicles behave on a sequence

- **Outside its own track a vehicle holds a pose**, rather than disappearing:
  parked at its start position before its track begins, at rest after it ends.
  This is how HVE sequenced events too.
- **Overlapping tracks are allowed.** Where two tracks that use the same vehicle
  overlap, the later-starting one takes the vehicle over; when a track nested
  inside another ends, the enclosing one resumes. These are HVE's own rules.
- A vehicle is the same vehicle in every event (HVE 2027's case has one vehicle
  list shared by all events), so no name matching is involved.
- **Damage carries forward on screen.** A vehicle entering a later event is
  drawn already crushed from the earlier one, and crush still forms
  progressively during each event.

!!! warning "Display only — each event is still solved on its own"
    A sequence is an arrangement for playback. It is not an input to any
    engine. Each event solves from its own initial conditions and an
    **undamaged** vehicle; no event's rest position, speed or damage is fed into
    the next one's solve.

- The playback step is the finest output interval of the tracks switched on,
  so every step lands on a recorded frame of every event.
- A [glTF export](06-exporting-to-blender-and-gltf.md) or the Blender live link
  made from the Playback editor carries the whole sequence; made from the Event
  editor, the active event.

!!! note "HVE 2027"
    The solved results of the other events are kept in memory only. When a case
    is saved and reopened, the results of one event are restored, as always;
    press **Run All Events** again before playing a sequence.

## Recording a video

**File › Record Animation...** writes what the playback bar plays to a video
file: the solved event from the Event editor, the active playback sequence from
the Playback editor. It records the **3-D scene**
between a start and an end time you choose (the whole playback unless you
change them), through the camera you choose: the view you are looking through
(the free view as you have framed it, or the saved camera chosen on the
playback bar), or any saved camera (see **Tools › Cameras...**), including an
attached or keyframed one. The case's [Results HUD](11-results-hud.md) boxes
can be drawn into every frame.

1. Run the event (or, for a sequence, press **Run All** in the Playback editor).
2. Choose **File › Record Animation...**. The **Record Animation (AVI)** window
   opens.
3. Set the **Output File** (default `output.avi`), or choose it with **...**.
   A name without a folder is written to the folder HVE 2027 was started from,
   not beside the case, so give a full path to put the video somewhere else.
4. Under **Video Settings**, set the frame **Width** and **Height** (64 to 4096
   pixels, rounded to even numbers; default 1280 × 720), the **FPS** (1 to
   1000; default 30) and the **JPEG Quality** (1 to 100; default 85).

   Tick **Slow motion** to take frames from the run faster than the video
   plays them, as a high-speed camera does. The **Capture rate (frames per s
   of the run)** (1 to 10000; default 1000) is how many frames are taken per
   second of the run; the **FPS** is how fast the video plays. Captured at 1000
   and played at 100, one second of the crash lasts ten seconds of video, and
   the window says so. A capture rate below the FPS speeds the video up
   instead. With **Slow motion** off, frames are taken at the FPS and the video
   plays in real time.
5. Under **Camera and Time**, choose the **Camera** — *The view you are looking
   through* (the default) or a saved camera by name — and the **Start (s)** and
   **End (s)** times. **Now** beside each takes the playback bar's current
   time; **End of run** (ticked by default) records to the end whatever the
   run's length, and greys the End field. Recording through a saved camera
   does not change your own view: it is put back when the recording ends.
6. Under **Rendering**, choose the **Renderer**. **Viewport (fast)** records the
   3-D view's own picture. **Ray traced** traces every frame with the built-in
   path tracer (see below) at the **Samples** given (default 64), which takes
   seconds a frame instead of milliseconds. Tick **Motion blur** to make each
   frame the average of several instants (**Steps**, default 8) across the
   **Shutter** (default 0.50 of a frame): 0.5 of a frame is a film camera's
   look, where a spinning wheel blurs and an impact smears.
7. Tick **Burn in key results (Results HUD)** to draw the case's Results HUD
   boxes into every frame. Ticking it switches every box on for the movie (and
   in the viewport), and adds a *Key results* box — Time, then Speed and
   Delta-V for each vehicle — if the case has none; unticking it takes every
   box out of the movie. Choose the rows, style and placement in **View ›
   Results HUD** (see [Results HUD](11-results-hud.md#in-a-recorded-movie)).
   Under motion blur the HUD is drawn once over the blurred frame, so it stays
   sharp.
8. Check the line under the switch, which gives the part of the playback
   recorded and the number of frames — for example *Recording 0.000 s to
   4.500 s of 4.50 s -> 136 frames at 30 fps.* With slow motion it also says
   how much slower (or faster) than real time the video plays and how long it
   will last.
9. Press **Record**. The viewport steps through the playback a frame at a time
   while a progress bar (*frame n / N*) fills; **Cancel** stops and leaves no
   file. When the recording finishes, the window reports the frames written,
   the length, the size and the file, and the playback returns to the time it
   was at before.

If the output file already exists, **Record** first asks whether to overwrite
it (**Overwrite** / **Keep**). Closing the window during a recording cancels
it.

!!! warning "Frames faster than the run's output are drawn, not computed"
    The engine saves the vehicles' state once per output interval. When the
    capture rate (the FPS, or the **Capture rate** under slow motion) is
    faster than that, the window warns in orange and says how many of every
    so many frames fall between saved states. Those frames are in-betweens:
    the vehicles move in a straight line between two saved poses, and crush
    and occupant bodies change only at saved states. For real detail, lower
    the event's output interval (for example to 0.001 s for 1000 frames a
    second of the run) and run it again.

!!! note "HVE 2027"
    The file is a **Motion-JPEG AVI**: each frame is a JPEG picture, in an
    ordinary AVI file. VLC, Windows Media Player, ffmpeg and common video
    editors open it without extra software. HVE used Windows' own video
    library and offered its compressors; HVE 2027 writes this one format on
    every platform. A video longer or larger than an AVI file can hold (about
    1 GB) stops with a message — lower the size, frame rate or quality.

!!! note "HVE 2027"
    The 3-D scene is recorded, with the Results HUD when it is burned in.
    Panels, dialogs and the playback bar are not in the video, and HVE's
    *Include UI Overlay* option is not offered. Record is unavailable, with the
    reason shown in the window, until there is a solved event to play, while a
    simulation is running, and when the start time is after the end time. A
    recording stops, and writes no file, if the run is reset or solved again
    while it is being recorded. The window's settings last for the session;
    they are not saved with the case.

### Playing a video

**File › Play Video...** opens a *Video Playback* window. Type or browse to a
file (**...**) and press **Load**. The picture is shown at the file's own frame
rate with **Play**/**Pause**, single-frame steps (**<** and **>**), **|<** and
**>|** for the first and last frame, a frame slider, a speed control and
**Loop**. After a recording, **Show in Play Video** in the Record Animation
window opens the file just written.

!!! note "HVE 2027"
    Play Video plays Motion-JPEG AVI files — what Record Animation writes, and
    the same format written by other programs. Other compressions
    (H.264 and so on) are not decoded; open those in a media player.

### A ray-traced picture

**File › Render Image (Ray Traced)...** traces the 3-D view as it is now: its
camera, the playback instant, the case's sun and sky, and the vehicles' lamps as
the run switched them. You get soft shadows from a sun disc of real size,
reflections, and light bounced off the road. Set the **Width** (the height
follows the view), the **Samples** (64–256 for a clean picture) and the
**Bounces**, then press **Render**. The picture sharpens pass by pass; **Stop**
at any point and **Save PNG**.

| Control | Default | Range |
| --- | --- | --- |
| **Width** (pixels) | 960 | 64–7680 |
| **Samples** | 128 | 1–16384 |
| **Bounces** | 6 | 0–32 |

The settings are locked while a render runs. The file box beside **Save PNG**
starts as `render.png`; a name without a folder is saved in the folder the
program was started from, and the status line names the file. Closing the
window stops a render in progress.

!!! note "HVE 2027"
    HVE has no built-in ray tracer. This one reads its scene from the same
    description the glTF export writes and lights it the way the viewport
    does. A traced picture and the viewport's picture of the same instant
    therefore show the same scene and materials, lit two ways. Glass is a thin
    pane (no refraction), and procedural node textures travel as the constant
    the glTF bake gives them.

### Rendering a video in Blender

For full control of a rendering — your own lighting and materials, Cycles,
a longer or larger video — export the scene to Blender:

1. The [Blender Live Link](06-exporting-to-blender-and-gltf.md#the-blender-live-link)
   if you will iterate, or a [glTF export](06-exporting-to-blender-and-gltf.md#exporting-gltf)
   for a one-off. Both carry the motion, the humans, the cameras (keyed) and,
   through the live link, the materials and sky.
2. In Blender, choose the camera, set the output format (for example FFmpeg
   video) and render the animation.
