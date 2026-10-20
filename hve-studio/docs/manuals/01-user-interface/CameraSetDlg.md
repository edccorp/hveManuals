# Camera Setup Dialog Box

HVE's Camera Setup dialog uses a camera metaphor to determine how a scene is viewed: viewing a scene is much like looking through a camera. It also saves and deletes named views, so several views can be defined and re-used.

In HVE Studio the same job is done by the **Cameras** window: **Tools › Cameras...**. It has two tabs, **Saved Cameras** (named cameras stored with the case) and **Viewport View** (the live view of the Viewport). A saved camera can also be chosen from the camera list on the playback bar under the Viewport, and **C** / **Shift+C** cycle through the saved cameras without opening the window. Lengths are shown in the units set in Preferences.

![Cameras window](images/hvn-cameras.png)

## Saved Cameras tab

### Camera
A drop-down list of the saved cameras; *(active)* marks the one driving the Viewport and *(modified)* one that has been re-framed in the Viewport without being saved. **Add** creates a new camera from the current view, **Delete** deletes the selected camera, and **Rename** renames it.

When the active camera has been re-framed in the Viewport, the window shows it as *Current -- re-framed from "<name>", not saved*, with **Save as New**, **Overwrite "<name>"** and **Revert** buttons.

### Attachment

**View From**
The vehicle the camera rides on, or **Fixed** for a camera that does not ride on a vehicle. Attaching the camera to a vehicle makes the view move with it.

**Look At**
The vehicle at which the camera is aimed, or **Fixed**. The camera can, for example, ride on one vehicle while aimed at another.

**Follow** (camera not riding on a vehicle, aimed at one)
**Fixed** — the camera does not move; the vehicle drives through the shot. **Follow** — the camera keeps its offset in world axes (a tracking or panning shot). **Chase** — the offset turns with the vehicle's heading, so *behind* stays behind through a turn.

**Aim** (camera riding on a vehicle)
**Rides with the vehicle** or **Stays on a fixed world point**.

An orange note reminds that only the **active** camera drives the Viewport.

### Onboard Mount (vehicle frame)
Shown when View From is a vehicle. **Mount X fwd**, **Mount Y right**, **Mount Z up**: the camera's position relative to that vehicle's CG (+X forward, +Y right, +Z up). The camera rotates with the vehicle. For example, 0, 0, 0 views the scene from the vehicle's CG, wherever the vehicle is.

A camera mounted this way is a **vehicle camera**: the Vehicle editor's Outliner lists it under the vehicle (**Vehicle Cameras**), and right-clicking that group adds one at the driver's eye (**Add Driver's-Eye Camera**). Before a run, a vehicle the active event does not place is taken at the origin heading forward, where the Vehicle editor draws it.

### Aim Point
Shown when the camera is aimed at a vehicle. **Aim X fwd**, **Aim Y right**, **Aim Z up**: the point the camera looks at, relative to the aimed-at vehicle's CG; it turns with the vehicle, so a point ahead stays ahead through a turn. **Look ahead** and **Aim at the vehicle** set typical values.

### Camera Coordinates
**Eye X fwd**, **Eye Y right**, **Eye Z up**: the camera position in the scene (greyed when the camera rides on a vehicle).

### Picture Center
**Center X fwd**, **Center Y right**, **Center Z up**: the point at the center of the view (greyed when the camera is aimed at a vehicle).

### Roll (deg)
Rotates the camera about its viewing axis, tilting (banking) the picture. 0 keeps the horizon level. HVE's *Camera Tilt Angle*.

### Lens
**Type**: **Perspective** or **Orthographic**. For a perspective camera, **Lens Unit** chooses between **Millimeters** (enter a **Focal Length (mm)**) and **Field of View** (enter a **Field of View (deg)**); 50 mm is a normal view, shorter focal lengths are wide-angle and longer ones telephoto. For an orthographic camera, **Orthographic Scale** sets how much of the scene the frame spans across its longer side. **Shift X** and **Shift Y** shift the picture. **Clip Start** and **Clip End** are the near and far clipping distances: anything closer than Clip Start or farther than Clip End is not drawn.

### Camera
**Sensor Fit** (Auto, Horizontal or Vertical) and the sensor size, which only change how a field of view reads as a focal length.

### Viewport Display
**Show in Viewport** draws the camera in the 3-D view, at the given **Size**; **Show Name** labels it and **Show Limits** draws its clip range.

### Keyframes
Animates the camera over the playback time: step to the previous or next key, set the time, **Insert Key (I)**, **Delete Key** and **Clear Keys**, and choose each key's interpolation and easing and the camera's extrapolation and cycling.

### Activate / Deactivate, Capture Current View
**Activate** makes the selected camera drive the Viewport (**Deactivate** releases it). **Capture Current View** copies the Viewport's current view into the selected camera.

## Viewport View tab

Controls for the live Viewport camera, without saving it: **View Controls** (**Orbit** or **Free (Euler)**), **View Preset** buttons (**Top**, **Front**, **Rear**, **Left**, **Right**, **Persp**), the orbit azimuth, elevation, distance and target (or, in Free mode, the eye position and pitch, yaw and roll), **Projection** (**Perspective** or **Orthographic**, with a focal length or field of view), and **Reset Camera**.

In Orbit mode, **Eye / Orientation** (linked) shows, read-only, the eye position and the pitch and yaw that the orbit settings give, as the Free mode would show them.

!!! warning "Not in HVE Studio"
    - **View From / Look At a human or the environment**: a camera rides on, or aims at, a vehicle or nothing (Fixed).
    - **Use Vehicle's Vertical** and **Make Glass Clear**.
    - **OK / Cancel / Apply**: changes take effect as they are made.

!!! tip "New in HVE Studio"
    Follow and Chase modes, orthographic cameras, lens shift and sensor fit, camera keyframe animation, drawing cameras in the Viewport, and the quick camera list on the playback bar.

<!-- NAV -->

---

← Previous: [3-D Editor Menu](3dEditor.md)  |  [Index](README.md)  |  Next: [Key Results Dialog Box](KeyResDlg.md) →

<!-- /NAV -->
