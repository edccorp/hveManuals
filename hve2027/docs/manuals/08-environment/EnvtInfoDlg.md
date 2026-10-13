# Environment Information Dialog

The environment holds the scene a case runs in: its name, date and location, the
terrain geometry the vehicles drive on, the sky, the physical constants of the
site, and its friction zones.

!!! note "HVE 2027"
    In the Environment editor (F4) choose **Environment › Environment...**. The
    **Environment** window has five collapsible sections in place of HVE's
    tabs: **Location**, **Terrain**, **Sky**, **Physical** and **Friction
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

The location is recorded with the case; it does not position or scale the
scene geometry. It places the sun (see **Sky**).

!!! tip "New in HVE 2027"
    The coordinate paste box and the address search.

!!! warning "Not in HVE 2027"
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

!!! tip "New in HVE 2027"
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

!!! warning "Not in HVE 2027"
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

!!! tip "New in HVE 2027"
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

### Surface Materials

Shown once geometry is loaded. It lists the scene's surfaces grouped by layer,
as in the **Outliner** (View › Outliner): the eye switch draws a surface, the
road switch sends it to the solver; clearing both removes it from the picture
and the solver. Click a surface in the 3-D view, or pick a row, to select it.

For the selected surface the section shows its name, type and friction, with
**Edit in Shader Editor** and **Deselect**. A surface's **type, friction,
stiffness and soil properties** are edited on its material in the Shader
Editor, on the **HVE Surface** node — see
[Environment Material Properties](EnvrMatPropDlg.md).

When the surface clicked is stored twice by the case — once as the drivable
surface and once as the drawn one — the section shows both, each with its own
switch; the material belongs to the drivable half.

Selecting **Default surface material** in the Outliner edits here the material
applied to any drivable polygon that has none of its own.

## Sky

A summary of the sun's direction and strength and the ambient light, and
**Edit the sun and sky...**, which opens the Shader Editor's world, where the
sun and sky are set.

!!! note "HVE 2027"
    The sun is placed from the location, date, time and UTC offset (or set by
    hand), by NOAA's method or HVE's own. The **North** angle there is HVE's
    *Angle of X Axis* (the compass bearing of the case's +X axis).

!!! warning "Not in HVE 2027"
    Sky image, sky dome and its rotation, fog (type and visibility).

## Physical

There is no friction on this page: for every engine, the single-track model
included, friction is each tire's own times the Friction Multiplier of the
surface (Surface Materials) or friction zone it is on.

**Rolling Resistance** — Used only for tires that state no rolling resistance of
their own.

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

!!! note "HVE 2027"
    The *Angle of X Axis* is in the Shader Editor's Sun & Sky panel as
    **North** (see Sky).

## Friction Zones

A friction zone is a patch of different grip — spilled oil, loose gravel, a wet
strip — laid over the road in plan. The run cuts it out of the road beneath, so
it lies on the terrain, and its **Friction Multiplier** replaces the road's
there.

The list shows each zone's **On** switch, name, **Friction Mult.** and status;
**Add Zone**, **Duplicate** and **Delete** manage it. For the selected zone:
**Name**, **Applied to the run**, **Friction Multiplier**, a **Rectangle**
(**Centre X**, **Centre Y**, **Length**, **Width**, **Heading (deg)**, and **Set
Outline to Rectangle**) and its **Corners** (up to 16): **Click corners in the
3-D view**, **Clear Corners**, the corners' X and Y, and **Add Corner**. A zone
the run cannot apply says why.

Under HVE's default road surface search, which tracks each tire's previous
polygon, a zone lying on the road is mostly stepped over. The section names
each event that searches that way, with a button that switches it to
friction zones first (see
[Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search)).

!!! note "HVE 2027"
    HVE draws a friction zone as a polygon of its own in its geometry editor;
    HVE 2027 draws it here, in plan.

## Signals

!!! warning "Not in HVE 2027"
    HVE's traffic signals — its list of individual signals in the environment,
    with their type, layout, repeating cycle and Start Time / Follow / Overlap
    timing. HVE 2027 has no traffic signals; no physics program models a
    traffic light.

## OK / Cancel

There are none: edits apply immediately, and **Edit › Undo** (Ctrl+Z) takes one
back.

<!-- NAV -->

---

← Previous: [Environment Material Properties Dialog](EnvrMatPropDlg.md)  |  [Index](README.md)  |  Next: [Lining Friction Properties Dialog](LinFriPropDlg.md) →

<!-- /NAV -->
