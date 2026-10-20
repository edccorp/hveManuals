# Environment Information Dialog

The environment holds the scene a case runs in: its name, date and location, the
terrain geometry the vehicles drive on, the sky, the physical constants of the
site, and its friction zones.

!!! note "HVE Studio"
    In the Environment editor (F4) choose **Environment › Environment...**. The
    **Environment** window has six collapsible sections in place of HVE's
    tabs: **Location**, **Terrain**, **Sky**, **Lights**, **Physical** and **Friction
    Zones**. Terrain and Physical — what the solver reads — open by default,
    and Friction Zones when the case has any. All five are always present;
    there is no 2-D/3-D distinction. Lengths, speeds, temperature and pressure
    follow the units set in Tools › Preferences. While a solved run is on
    screen, Terrain, Physical and Friction Zones are read-only; Location and
    Sky are description and stay editable.

![Environment window](images/hvn-environment.png)

## Location

**Name** — The name of the scene. HVE's *Environment Name*.

**Date** — The date of the crash or test. HVE's *Date of Crash*. Typed as text
(mm/dd/yyyy, as HVE writes it, or yyyy-mm-dd).

**Time** — The local standard time of day. HVE's *Time of Crash (24 Hr)*.

**Latitude (°)** / **Longitude (°)** — The site's latitude and longitude in
decimal degrees, north and east positive (HVE enters them as dd.mm.ss with
N/S, E/W).

**Elevation** — The site's elevation.

**Set from a pasted coordinate** — Paste a coordinate in decimal degrees, in
degrees-minutes-seconds, or a map link; the box shows how it reads, and
**Apply** sets Latitude and Longitude. A pair given longitude-first is
reordered, and the box says so.

**Search an address** — Type an address or place and press **Search**; pick a
result to set Latitude and Longitude. **Set UTC offset from location** looks up
the time zone of the coordinate. Both send what you type, or the coordinate, to
online services (OpenStreetMap's Nominatim and timeapi.io).

The results are a numbered list beside numbered pins on the **Map** below it.
Choosing a result shows it on the map; **Use this place** (or a double-click on
the result) sets the case's Latitude and Longitude to it and looks up its time
zone. **Clear results** empties the list. On the map, drag to pan, use the
wheel to zoom, and double-click anywhere to put the case's location there.

Under the map, choose the tile source. When it is an aerial source, choose a
size (50 to 800 m square) and press **Download aerial image**: the yellow
square on the map, centred on the map's centre and aligned to the case's axes,
is downloaded and laid on the ground as the case's aerial site image
(**Environment › Aerial Image...**). It is placed assuming the case origin is at
this location and +X points along its North angle. The button needs the case's
location to be set first.

The location is recorded with the case; it does not position or scale the
scene geometry. It places the sun (see **Sky**).

!!! tip "New in HVE Studio"
    The coordinate paste box and the address search.

!!! warning "Not in HVE Studio"
    HVE's location database (**Current Location**, **New Location**, **Add New
    Location**). The **GMT** offset is the **UTC offset** in the Shader Editor's
    Sun & Sky panel.

## Terrain

### Embedded terrain

When the case was opened from an HVE case file (`.hve`) that stores its site in
the case itself, the section says the terrain is embedded and names its source.
There is then no file, scale or axis option to set; the polygon count and
extents are shown. **Use a geometry file instead** discards the embedded
terrain so a file can be chosen.

### Shading

**Flat**, **Smooth** or **Auto Smooth**, with **Auto Smooth Angle (deg)**
(enabled for Auto Smooth). Flat uses one normal per face; Smooth averages the
normals where faces meet, so a graded road stops showing its triangles; Auto
Smooth averages only between faces within the angle, so curbs and building
edges stay sharp. Display only.

!!! tip "New in HVE Studio"
    The shading modes.

### Geometry File

The terrain geometry file, typed or chosen with **Browse...**: DXF, HVE geometry
(`.h3d`), Inventor (`.iv`), VRML (`.wrl`), OBJ or glTF (`.gltf`, `.glb`).

**Scale Factor** — scale applied to the imported geometry, to metres. For an
`.h3d` the field is **Extra Scale**, since an `.h3d` states its own units
(inches) and frame, which are applied automatically.

**File is Y-up (rotate to Z-up)** — for a file whose vertical axis is Y.

**File is Z-down (Flip About X-Axis)** — for a file whose vertical axis points
down. For an `.h3d` it reads **Flip About X-Axis (file's vertical sense is
reversed)** and only
corrects a file that is not what it claims. For DXF, OBJ and glTF nothing in
the geometry can tell a valley from a hill, so check the elevation range in the
summary against the site.

**Use surfaces as terrain (physics)** — the imported surfaces are what the
vehicles drive on. Unchecked, the geometry is drawn only.

**Import** reads the file; **Clear** removes the geometry. After an import the
section shows the number of surfaces and lines and the X, Y and Z extents, or an
error.

**Outside the site** — what a tire finds where there is no site surface: past
the edge of the mesh, or in a hole in it.

- **As HVE** (the default): a point-contact tire rides a flat ground at
  elevation 0; a radial-spring tire finds nothing, so the vehicle falls.
- **Flat ground**: every tire model drives on a flat ground at **Ground
  elevation** (up is positive, in the site's own frame), friction multiplier 1.
- **Nothing (vehicles fall)**: no tire model finds ground.

Whichever is chosen, a tire off the site no longer searches every surface of
the site on every step, so a run no longer slows to a crawl once a vehicle
leaves the mesh. A large site also solves faster with radial-spring tires.
Results are unchanged by the speed-up (ctest `site_bounds_ab` compares every
step).

A **zero-area triangle** in the site (its corners on one line, or at one point)
is not ground. HVE reads a flat one as ground along its line, or under the whole
scene; here it is ignored, and the run status says how many the site has.

!!! warning "Not in HVE Studio"
    - The **Type** choice (None / Terrain Map / Aerial Photo). An aerial photo is
      set separately with **Environment › Aerial Image...** (the **Aerial Image
      Options** window: **Image File**, **Visible**, **Opacity** and the
      image's upper-left and lower-right world coordinates).
    - **Save As...** of the environment geometry to `.h3d`. (A saved case keeps
      its site inside it while **File › Embed the environment in the case** is
      ticked, as it is by default.)
    - **Use As Default**, and the **Default Type** given to imported polygons:
      an imported polygon with no type is a road. Change a surface's type on its
      material (below).
    - DWG files.

### Survey Point Cloud (scan)

!!! tip "New in HVE Studio"
    A collapsed section that loads a survey scan (LAS, PLY, E57, XYZ, PTS, TXT or
    CSV; a LAZ file must first be exported as LAS) as a picture of the scene.
    A point cloud is **display only**: vehicles cannot drive on it, settle onto
    it or collide with it. Import a site surface for that, or build one from
    the scan with **Drivable Surface from Scan**. The section has the
    file, **Scale (source -> m)**, **Source is Y-up**, **Source is Z-down**,
    **Points loaded (for the surface)**, **Points drawn per frame**, **More detail
    near the camera**, **Shown (%)**, **Colour** (Auto, File colour,
    Intensity, Elevation, Flat grey), **Point size (px)**, **Visible**, a
    **Placement** offset and rotation (to level a scan), and **Import** /
    **Clear**.

### Selected Surface

Shown once geometry is loaded. The scene's surfaces, grouped by layer, are
listed in the **Outliner** (View › Outliner; **Open Outliner** here opens it):
the eye switch draws a surface, the road switch sends it to the solver;
clearing both removes it from the picture and the solver. Click a surface in
the 3-D view, or pick its row in the Outliner, to select it.

For the selected surface this section shows its name, type and friction, with
**Edit in Shader Editor** and **Deselect**, and its **Placement** (move, turn
and scale it on its own). A surface's **type, friction,
stiffness and soil properties** are edited on its material in the Shader
Editor, on the **HVE Surface** node — see
[Environment Material Properties](EnvrMatPropDlg.md).

When the surface clicked is stored twice by the case — once as the drivable
surface and once as the drawn one — the section shows both, each with its own
switch; the material belongs to the drivable half.

**Default material** (a button here, or the *Default material* row in the
Outliner) edits here the material applied to any drivable polygon that has
none of its own.

## Sky

A summary of the sun's direction and strength and the ambient light, and
**Edit the sun and sky...**, which opens the Shader Editor's world, where the
sun and sky are set.

!!! note "HVE Studio"
    The sun is placed from the location, date, time and UTC offset (or set by
    hand), by NOAA's method or HVE's own. The **North** angle there is HVE's
    *Angle of X Axis* (the compass bearing of the case's +X axis).

!!! warning "Not in HVE Studio"
    Sky image, sky dome and its rotation, fog (type and visibility).

## Lights

Lights of the site itself — street lights, work lights, a floodlight on a
pole — not attached to any vehicle. **Add Light** places one 8 m above the
ground at the middle of the view; **Duplicate** and **Delete** manage the list.

For the selected light: **Name**; **On**; **On in daylight too**; **Type**
(**Point (every way)** or **Spot (a cone)**); **X (forward)** and **Y (right)**
in the site's plan; **Height above the ground** (the ground beneath it is found
where the light stands, so it stays on its pole when moved; with no ground under
it the field reads **Height (no ground under it)**); for a spot, **Aim (deg,
right of forward)**, **Tilt down (deg, 90 = straight down)**, **Cone (deg,
half-angle)** and **Edge softness**; **Color** and **Intensity (1 = a
headlamp)**. A light in the list that is switched off reads "(off)".

The lights belong to the site: when the site is moved, turned or scaled (its
placement), they move with it, and a spot's aim turns with it.

A site light comes on as the sky darkens, as a vehicle's lamps do; tick
**On in daylight too** for one that should also light the scene by day. In
the 3-D view each light is marked by a star with a dotted line to the ground
(and, for a spot, a line along its aim) while the Environment is selected.

The 3-D view lights the scene with up to 32 lamps at once, site lights and
vehicle lamps together. Site lights take at most sixteen of them, the ones
nearest the middle of the view, so the vehicles' lamps always have the rest.
The ray-traced render, the glTF export (as KHR_lights_punctual lights) and the
Blender live link (as lights named HVE_Site_<name>) carry every one. Site
lights are display only: no engine reads them.

!!! note "HVE Studio"
    HVE made site lights with the 3-D Editor's Light tool; HVE Studio has no 3-D
    Editor, so they are made here and stored in the case (JSON
    `environment.lights`).

## Physical

There is no friction on this page: for every engine, the single-track model
included, friction is each tire's own times the Friction Multiplier of the
surface (Selected Surface) or friction zone it is on.

Rolling resistance is not on this page either: it is each tire's own
(**Vehicle › Editors › Tires...**, Rolling Resistance), as in HVE.

**Ambient Temperature** — The ambient temperature. Feeds the air density used by
the aerodynamic model.

**Ambient Pressure** — The ambient barometric pressure.

**Wind Speed** — The ambient wind speed.

**Wind Direction (deg)** — The direction the wind blows **from**, measured from
the earth-fixed X axis (HVE's convention).

**Air Density** — Derived from Ambient Temperature and Pressure, as the engines
compute it; display only.

**Gravity** — The local acceleration of gravity (m/s² or in/s²).

### Standing Water

Standing water is set per surface, on each surface's HVE Surface node in the
Shader Editor, and on the **Default surface material** for ground with no
surface of its own — see [Environment Material Properties](EnvrMatPropDlg.md).

!!! note "HVE Studio"
    The *Angle of X Axis* is in the Shader Editor's Sun & Sky panel as
    **North** (see Sky).

## Surface Generator

The Surface Generator draws a surface over the site in plan: a road, a
friction zone, standing water or another surface. Each lies on the ground
beneath its outline, draped over a bank or a ramp exactly as that ground lies.
Its **Type** decides what it does in a run:

| Type | In the run |
|---|---|
| **Road** | Replaces the ground beneath its outline. A tire there drives on the surface's own material, under every road-surface search. |
| **Other** | The same as **Road**. HVE's engines treat an Other surface as road; only the label differs. |
| **Friction Zone** | A patch of different grip (spilled oil, loose gravel, a wet strip) laid on the ground. It keeps the ground's material with only the friction replaced, or uses its own material. |
| **Water** | Water standing on the ground. The ground keeps its own material; the hydroplaning models of SIMON and EDSMAC4 read the depth and the wet friction. |

The list shows each surface's **On** switch, name, **Type**, **Layer** and
status. Pick a type and click **Add Surface** to make one; **Duplicate** and
**Delete** manage the list. For the selected surface:

- **Name**, **Type**, **Applied to the run** and **Show**. Show only draws it:
  a hidden surface still acts in the run while it is applied.
- **Layer**: the layer it is drawn on, as an imported surface's is. Hiding the
  layer hides it. A layer takes nothing out of the run. Create layers in the
  [Outliner](../01-user-interface/OverLayDlg.md).
- **Material**, for a road or other surface: the material library, **Condition
  preset**, **Friction Multiplier**, the force terms, the soil terms and
  standing water, as for any surface. A new road starts as the default
  material (**Terrain**) at a multiplier of 1.
- **Material**, for a friction zone: **Ground's material, friction replaced**
  (with its **Friction Multiplier**) or **Its own material** (the full
  material rows).
- **Water**, for water: **Water Depth** and **Wet Friction**.
- **Appearance**: **Own color**, the color the 3-D view draws it. Display only.
- A **Rectangle** (**Center X**, **Center Y**, **Length**, **Width**,
  **Heading (deg)**, and **Set Outline to Rectangle**, which replaces the
  outline with that rectangle; length runs along the heading, 0 = +x) and its
  **Corners** (up to 16): **Click corners in the 3-D view**, **Clear Corners**,
  the corners' X and Y, and **Add Corner**.

A surface the run cannot apply says why. The 3-D view draws each surface where
the run put it; one switched off for the run is drawn faint.

Under HVE's default road surface search, which tracks each tire's previous
polygon, a friction zone lying on the road is mostly stepped over. The section
names each event that searches that way, with a button that switches it to
friction zones first (see
[Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search)).
A road, other or water surface is met under every search.

Each generated surface is also a row of the
[Outliner](../01-user-interface/OverLayDlg.md), under its layer or under
**Generated surfaces**.

!!! note "HVE Studio"
    HVE draws its surfaces as polygons of their own in its geometry editor;
    HVE Studio draws them here, in plan. A case saved before the Surface
    Generator existed opens with its friction zones as Friction Zone surfaces.

## Signals

!!! warning "Not in HVE Studio"
    HVE's traffic signals — its list of individual signals in the environment,
    with their type, layout, repeating cycle and Start Time / Follow / Overlap
    timing. HVE Studio has no traffic signals; no physics program models a
    traffic light.

## OK / Cancel

There are none: edits apply immediately, and **Edit › Undo** (Ctrl+Z) takes one
back.

<!-- NAV -->

---

← Previous: [Environment Material Properties Dialog](EnvrMatPropDlg.md)  |  [Index](README.md)  |  Next: [Lining Friction Properties Dialog](LinFriPropDlg.md) →

<!-- /NAV -->
