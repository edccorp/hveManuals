# Chapter 5: View Menu

*HVE User's Manual — Section Two: Menu Reference, HVE 2027 edition. Replaces
HVE's Chapter 5, View Menu, and takes over most of the display switches of HVE's
Options menu (see [Chapter 6](06-options-menu.md)).*

The View menu is on the menu bar in every editor. It shows and hides panels, and
holds two settings that are not about the scene. What the viewport draws is chosen
in the **Scene Display** panel, which **View › Scene Display** opens; its switches
change what is drawn, never a result.

![The View menu](../images/hvn-02-view-menu.png)
*The View menu.*

HVE's View menu items map as follows:

| HVE item | HVE 2027 |
|---|---|
| Toolbar | Not in HVE 2027 — see [TOOLBAR](#toolbar) |
| Status Bar | Not in HVE 2027 — see [STATUS BAR](#status-bar) |
| Set Camera | **Tools › Cameras...**, or right-click the viewport › **Camera Properties...** — see [SET CAMERA](#set-camera) |
| Overlays | **View › Outliner** for site layers; **Environment › Aerial Image...** for a scanned image — see [OVERLAYS](#overlays) |

---

## PANELS

| Item | Shows or hides |
|---|---|
| **Viewport** | The 3-D viewport |
| **Scene Display** | The panel holding every switch that changes what the scene draws — see [SCENE DISPLAY](#scene-display) |
| **Shader Editor** | The node-material editor for vehicles, road surfaces and the world (display only) |
| **Dope Sheet** | Every keyframed material and camera value on one time axis |
| **Key Results** | The Key Results panel (Event editor) |
| **Results HUD** | The Results HUD window: boxes of solved numbers drawn over the viewport and into recorded videos, saved with the case (every editor) — see [Results HUD](../../new-features/11-results-hud.md) |
| **Output Graph** | The Output Graph panel (Event editor) |
| **Timestep Table** | The Timestep Data panel (Event editor) |
| **Simulation** | The Simulation panel: simulation controls, Run / Reset and the last result (Event editor) |
| **Outliner** | The site's layers and surfaces — see [OUTLINER](#outliner) |

Key Results, Output Graph, Timestep Table and Simulation are drawn only in the
Event editor. Panels dock: drag a panel's tab to move it to another dock position
or to float it.

!!! tip "New in HVE 2027"
    The Shader Editor, Dope Sheet and Results HUD are new in HVE 2027. They
    change only what the scene shows, never a result.

---

## SCENE DISPLAY

**View › Scene Display** opens the panel that holds every switch changing what
the scene draws, so they can be left on screen beside the Viewport. It is in
every editor, docks like any other panel, and remembers whether it was open.
These switches are only in this panel, not on the View menu.

Its groups are **Paths & Overlays** (the paths, Axes, North Arrow, Skidmarks,
occupant equipment, the two Through Bodywork switches and Path thickness),
**Vehicle** (Vehicle Extents, DyMESH Wheel Mesh), **Vectors** (with the arrow
scales), **Scene Ghosts**, **Shadow Coverage**, **Effects** and **Rendering**.
Click a group's header to fold it away. A greyed switch says why when you point
at it.

The sections below describe each group. Panels, **Outliner**, **Panels Outside
the Main Window** and **Show Guidance Text** stay on the View menu, because they
do not change the scene.

---

## PATHS AND MARKS

In the Scene Display panel's **Paths & Overlays** group. These draw what a solved
run leaves behind, and the case's axes.

| Item | Draws |
|---|---|
| **Accelerometer Path** | One path per installed accelerometer, at the device's own position (HVE: Show Accelerometer Paths) |
| **Tire Contact Patch Paths** | Where each tire actually touched the ground, one path per wheel (HVE: Show Tracks) |
| **Axes** | The case's axes at the origin, and each vehicle's own axes at its CG (X red, Y green, Z blue, drawn up). On by default |
| **North Arrow** | A compass in the corner of the viewport pointing to the case's north, which is set in the Shader Editor's Sun & Sky panel or read from an imported `.hve` |
| **Skidmarks** | The contact-patch path, only where the tire was marking. SIMON grades the mark's opacity; EDSMAC4, EDVSM, EDSVS and EDVDS report a tire as skidding or not, so their marks are all-or-nothing (HVE: Show Skidmarks) |
| **CG Path** | Each vehicle's CG path up to the current playback time, in its paint colour (HVE: Show CG Paths) |
| **Path thickness (m)** | A slider: the thickness of the CG and accelerometer paths; 0 draws hairlines. Skidmarks are drawn at the width of the tire |

---

## OCCUPANTS AND VEHICLES

The occupant switches are in **Paths & Overlays**; Vehicle Extents and DyMESH
Wheel Mesh are in **Vehicle**.

| Item | Does |
|---|---|
| **Occupant Equipment** | Draws the active vehicle's contact surfaces, airbags, belt anchors and webbing, in the Event editor as well as the Vehicle editor, without opening their dialogs (HVE: Show Contacts, Show Belt Anchors) |
| **Occupant Equipment Through Bodywork** | Draws that equipment over the vehicle instead of hidden inside it. Turn it off to judge what is in front of what |
| **Humans Through Bodywork** | Draws the occupant figure over the vehicle, so a seated occupant can be seen from outside. A human that draws nothing with this on has no body yet: generate one in the Human editor |
| **Vehicle Extents** | A translucent box at the CG-to-front, CG-to-rear, width and height the engine is given, to compare with the drawn body |
| **DyMESH Wheel Mesh** | The DyMESH contact body built for each tire, drawn deformed by the run, with crushed vertices in red. Greyed until a SIMON event with DyMESH has been run |

---

## WINDOW

| Item | Does |
|---|---|
| **Panels Outside the Main Window** | Lets a panel dragged out of the main window become a window of its own (for example, the Shader Editor on a second monitor). Takes effect the next time HVE 2027 starts. Not available in the browser build |
| **Show Guidance Text** | Shows the longer explanatory notes in the dialogs. Off by default. A message about a problem with the open case is always shown, whatever this is set to |

---

## SHADOW COVERAGE

**Menu Option:** View › Scene Display › Shadow Coverage › Vehicles (sharp) · Whole scene

**Description:** **Vehicles (sharp)** fits the shadow to the vehicles, so their
shadows are as sharp as possible but site geometry outside that region casts
none. **Whole scene** lets everything cast a shadow, with softer edges. The panel
shows the current shadow resolution in centimetres per texel.

---

## VECTORS

**Menu Option:** View › Scene Display › Vectors › …

| Item | Draws |
|---|---|
| **Velocity Vectors** | Each vehicle's velocity, from its forward and lateral velocity rotated into the earth frame — not along the heading, so a sideslip shows (HVE: Show Velocity Vectors) |
| **Collision Force (PDOF)** | While the vehicles are in contact only, an arrow that turns and grows with the engine's collision force sample by sample. It points into the CG from the direction the force came from, HVE's PDOF convention |
| **Tire Force Vectors** | Each tire's Fx' (red, longitudinal) and Fy' (green, lateral) at the contact patch |
| **…include vertical Fz'** | Adds the normal load (blue), drawn up from the patch on the same scale |
| **Draw Vectors Through Bodywork** | Draws the arrows over the vehicles instead of hidden by them |

Each arrow is scaled against the run's own peak, so lengths compare within a
run, not between runs.

---

## RENDERING

**Menu Option:** View › Scene Display › Rendering › Phong · Flat · Wireframe · Light Sources On

**Description:** **Phong** (smooth shading, the default), **Flat** (one normal
per face, showing the real tessellation) and **Wireframe** (edges only, depth
tested — what HVE calls Hidden Line). **Light Sources On** turns the sun's
contribution off and on; with it off, the ambient light is raised so the scene
stays readable. Wireframe is not available in the browser build.

See [Chapter 6](06-options-menu.md#render) for the mapping from HVE's Rendering
Options dialog.

---

## OUTLINER

**Menu Option:** View › Outliner

**Description:** The site's layers with their surfaces under them. Each surface
has a **draw** switch (show it in the viewport) and a **drive** switch (give it to
the engine as road); drag a surface onto a layer to move it. It is the same tree
as the Environment panel's Surface Materials section.

---

## SCENE GHOSTS

**Menu Option:** View › Scene Display › Scene Ghosts › None · Outline · Translucent vehicle · Both

**Description:** How each vehicle is drawn at its measured scene positions
(Initial, Begin Perception, Begin Braking, Impact, Separation, Point On Curve, End
of Rotation, Rest) — HVE's *targets* (Options › Show Targets). The positions are
entered in Event Information (see [Chapter 4](04a-setup-menu.md#target-positions)).

---

## TOOLBAR

!!! warning "Not in HVE 2027"
    HVE 2027 has no toolbar. Its commands are on the menus; the editors are the
    tabs under the menu bar, and Run, Reset and the playback buttons are on the
    playback bar under the viewport.

---

## STATUS BAR

!!! warning "Not in HVE 2027"
    There is no status bar. The case name (with `*` when modified) is at the
    right of the menu bar; the run status is in the Simulation panel and on the
    playback bar; hovering over most controls shows a tooltip; and **Tools ›
    Audit Log** keeps a record of what was done.

---

## SET CAMERA

**HVE menu option:** View › Set Camera · **HVE 2027:** Tools › Cameras...;
right-click the viewport › Camera Properties...

**Description:** The **Cameras** dialog keeps the case's named cameras. Its
**Saved Cameras** page adds, deletes and renames them; its **Viewport View** page
sets the view through the current camera — **View From** and **Look At** (each
attached to the earth or to an object, so a camera can ride with a vehicle), roll,
and the **Lens**. **Save as New** keeps the current view as a named camera. The
camera list on the playback bar switches between *Free view* and the saved
cameras; **C** and **Shift+C** step through them.

![The Cameras dialog](../images/hvn-01-cameras.png)
*The Cameras dialog.*

The viewport's own buttons — **Top**, **Front**, **Side**, **Momentum** and
**3D** — choose the view type, and the number keys (or keypad) set standard
views: **1** front (Ctrl+1 rear), **3** right (Ctrl+3 left), **7** top (Ctrl+7
bottom), **9** the opposite side, **5** perspective/orthographic, **4**/**6**
and **8**/**2** orbit in 15° steps, and **.** frames the selection. Double-click the viewport,
or right-click › **Reset Camera**, to reset the view.

See the dialog reference: [Camera Set-up](../../01-user-interface/CameraSetDlg.md).

---

## OVERLAYS

**HVE menu option:** View › Overlays

**Description:** HVE's overlays were user-named sets of 3-D Editor objects that
could be shown or hidden. In HVE 2027:

- the site's **layers** are shown and hidden in **View › Outliner** (each
  surface's draw switch);
- a **scanned image** of the site is laid over the ground with **Environment ›
  Aerial Image...**.

!!! warning "Not in HVE 2027"
    Named overlay sets of 3-D Editor objects, and a scanned image registered to
    a camera position and focal length, are not available.

<!-- NAV -->

---

← Previous: [Chapter 4D: Output Menu](04d-output-menu.md)  |  [Index](README.md)  |  Next: [Chapter 6: Where HVE's Options Menu Went](06-options-menu.md) →

<!-- /NAV -->
