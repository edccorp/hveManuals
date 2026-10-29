# Cameras

!!! tip "New in HVE Studio"
    HVE saves named camera views, which can ride on a vehicle and be aimed at
    one. HVE Studio keeps up to 16 named cameras in the case, each carried by
    nothing or by a vehicle and aimed where it points, at a vehicle or at a
    fixed point, and adds what HVE
    does not have: cameras animated with keyframes, set up the way a Blender
    camera is — the same lens, sensor and display settings — and carried to
    Blender and glTF.

!!! warning "Display only"
    No engine reads a camera. Adding, moving or keying one never invalidates a
    solved run.

## The Cameras dialog

Open **Tools › Cameras...**. The dialog has two tabs:

- **Saved Cameras** — the cameras stored in the case (this page).
- **Viewport View** — the controls for the live view itself: Orbit or Free,
  the view presets (Top, Front, Rear, Left, Right, Persp), the projection and
  **Reset Camera**. See [Camera Setup](../01-user-interface/CameraSetDlg.md).

![The Cameras dialog, Saved Cameras tab](images/hvn-cameras.png)

### Making and choosing cameras

| Control | Does |
| --- | --- |
| Camera list | Chooses which saved camera the dialog edits. The camera being looked through is marked *(active)*. |
| **Add** | A new camera, framed as the viewport is now |
| **Delete**, **Rename** | Act on the selected camera |
| **Activate** / **Deactivate** | Look through the selected camera (it drives the viewport), or stop |
| **Capture Current View** | Copy the viewport's current framing into the selected camera |

**Looking through a camera.** Only the **active** camera drives the viewport.
Press **Activate** in the dialog, pick the camera in the viewport bar's camera
list, or press **C** (next camera) or **Shift+C** (previous) when no text field
is being edited. In the Dope Sheet, double-click a camera's header.

**Re-framing a saved camera.** While you look through a camera, orbiting,
panning, dollying or zooming the viewport does **not** silently rewrite it. The
dialog shows the working view as **Current — re-framed from "name", not
saved**, with three buttons: **Save as New**, **Overwrite "name"**, **Revert**.

## Position and Aim

A camera is set up the way a Blender camera is, with two independent settings:
**what carries it** (Blender's *parent*) and **what it points at** (Blender's
*Track To* target). Each can be anything, so a camera can ride one car and watch
another, stand on a tripod and watch a car, or ride a car looking where it points.

### Position

| Field | Meaning |
| --- | --- |
| **Carried by** | **None (placed in the scene)**, or the vehicle the camera rides on. A vehicle carries it through playback, and holds it at its start layout before a run |
| **Inherit** | How much of the vehicle's motion the camera takes (shown when a vehicle carries it) |
| **Eye X fwd / Y right / Z up** | Where a camera placed in the scene stands |
| **Offset X fwd / Y right / Z down** | Where a carried camera sits, from the vehicle's CG |

| Inherit | Effect |
| --- | --- |
| **Position only** | The camera travels with the vehicle; its offset stays in world axes, so it keeps its compass direction from the vehicle — a tracking shot. After a right turn you are watching the vehicle's left side |
| **Position and heading** | The offset turns with the vehicle's heading, so *behind* stays behind through a turn — a chase shot. The horizon stays level |
| **Position, heading, pitch and roll** | Bolted to the vehicle: it pitches and rolls with it, and the picture banks with it |

The **Offset** is in the vehicle's own frame (SAE: z down, so a camera above the
CG is negative), or in world axes for **Position only**.

### Aim

| Points at | The camera looks | Fields |
| --- | --- | --- |
| **Its own direction** | where it is pointed, turning with what carries it | **Heading** (from the vehicle's nose, or in the scene for a camera placed there) and **Tilt (+ up)** |
| A vehicle | at a point on that vehicle, which travels and turns with it | **Aim X fwd / Y right / Z down**, from that vehicle's CG in its own frame; **Look ahead** sets 30 m ahead at about eye height, **Aim at the vehicle** the CG, 0.7 m up |
| **A fixed point** | at a point in the scene (HVE's *Picture Center*) | **Center X fwd / Y right / Z up** |

For a camera **placed in the scene** both ways of aiming it are shown and kept
in step: with its own direction, the point it is **Looking at**; with a fixed
point, the **Heading**, **Tilt** and **Distance** from the eye to it. Editing
either moves the aim and leaves the eye where it is — HVE's *Camera Coordinates*
and *Picture Center*, alongside Blender's location and rotation.

**Roll (deg)** turns the picture about the view axis, on top of any bank from
the vehicle.

Changing **Carried by**, **Inherit** or **Points at** keeps the camera where it
is and looking where it looks at the playback time, as far as the new setting
allows; a newly chosen vehicle target is aimed at its body.

**Dragging in the view** while you look through a camera (with Lock Camera to
View on) edits the same fields: aimed at a vehicle or a point, the view orbits
about the target and the eye it leaves is the new position, and a pan moves the
target; with its own direction the eye stays fixed, a drag turns the camera,
and the mouse wheel dollies along the view axis by editing the Offset.

A camera carried by a vehicle is a **vehicle camera**: the Vehicle editor's
Outliner lists it under the vehicle (**Vehicle Cameras**), and right-clicking
that group adds one at the driver's eye looking straight ahead (**Add
Driver's-Eye Camera**).

A case saved before these settings existed (View From, Look At and a Follow,
Chase or Aim mode) opens with each camera converted to the same shot: a Look At
camera in Follow or Chase is carried by its vehicle (position only, or position
and heading) and aimed at it, an onboard camera aiming down its own vehicle has
its own direction, and a Look At camera in Fixed is placed in the scene and aimed
at the vehicle. A Follow camera whose aim point was off the vehicle's vertical
axis is exact at heading 0 and close elsewhere.

An edit in the dialog to the **active** camera shows in the view at once, and
the camera stays active and keeps its name: only moving the view itself leaves
the camera (or, with Lock Camera to View on, makes it **Current**).

Lengths are shown in the units set in Preferences. Before a run, an attached
camera tracks the vehicles' **start** positions, so it can be aimed before
anything is solved; after a run it follows the motion.

## Lens, Camera and Viewport Display

These are Blender's camera settings, under Blender's names, and the 3-D view
honors them while you look through the camera:

| Section | Field | Meaning |
| --- | --- | --- |
| Lens | **Type** | Perspective or Orthographic |
| | **Lens Unit** | Millimeters (focal length) or Field of View |
| | **Focal Length (mm)** / **Field of View (deg)** | Taken along the sensor's axis, as Blender takes them |
| | **Orthographic Scale** | How much of the scene the frame spans, across its longer side (orthographic only) |
| | **Shift X**, **Shift Y** | Moves the frame sideways or up without turning the camera, as a fraction of its longer side — a view camera's shift |
| | **Clip Start**, **Clip End** | The nearest and farthest distances drawn |
| Camera | **Sensor Fit** | Auto, Horizontal or Vertical |
| | **Size / Width / Height (mm)** | The sensor size the focal length is measured against. Vertical 24 mm is the 35 mm-equivalent HVE Studio has always used; Blender's default is Auto, 36 mm |
| Viewport Display | **Show in Viewport**, **Size**, **Show Name**, **Show Limits** | How the camera is drawn in the 3-D view (Show Limits draws the clip range) |

**Depth of Field** (with **Focus Distance** and **F-Stop**) blurs what is nearer
or farther than the focus distance while you look through the camera; it is
display only. Panoramic lenses are not offered: nothing in HVE Studio renders
them.

## Keyframed cameras

A saved camera can be animated over playback time.

1. **Activate** the camera (look through it).
2. Set the playback time, frame the view — orbit, pan, dolly, zoom, roll — and
   press **I** (when no text field is being edited), or **Insert Key (I)** in the dialog's
   **Keyframes** section.
3. Move the playback time, re-frame, and press **I** again. Repeat.

The **Keyframes** section also has the playback **Time** with ◀ ▶ to jump
between this camera's keys, **Delete Key** (at the current time), **Clear
Keys**, and one row per key time with its interpolation (and easing) to the
next key, plus the camera's extrapolation and cycles. These are the same
choices as for materials — see
[Keyframes and the Dope Sheet](04-keyframes-and-dope-sheet.md). The keys also
appear in the Dope Sheet, where they can be moved and edited.

**What a key records** depends on how the camera is attached, so no key fights
the attachment:

| Camera | Keys |
| --- | --- |
| Placed in the scene, aimed at a fixed point | the Picture Center (look-at point) and the orbit (azimuth, polar angle, distance) |
| Any other camera | the Eye or Offset, and the aim: the point, the Aim offset, or the heading and tilt |

Every camera also keys its field of view and roll; the orthographic scale when
orthographic; the shift when it is not zero; and every channel already keyed.
Angles are keyed the short way round, so a pan past 180° does not spin the long
way.

- **A keyed camera is still carried and still aimed.** A keyed camera carried
  with the heading still turns with its car; the keys animate its offset.
- **Re-framing without keying is temporary.** If you re-frame an animated camera
  and do not press I, the change lasts until the playback time moves, then the
  camera returns to its curve — as in Blender.
- **The dialog's fields show the camera at the playback time**, and editing a
  keyed field keys it there.

## In Blender and glTF

- **glTF export** writes every saved camera as a glTF camera. A camera that
  rides a vehicle, or is keyed, is animated per frame; its lens is a single
  value, so a keyed lens is exported at t = 0, and lens **shift** cannot be
  carried at all — the export status says so, camera by camera.
- **Blender Live Link** creates real Blender camera objects in an *HVE Cameras*
  collection, with the lens (focal length, orthographic scale, shift) and the
  motion keyed per frame. The camera HVE Studio looks through becomes Blender's
  scene camera.

See [Exporting to Blender and glTF](06-exporting-to-blender-and-gltf.md).
