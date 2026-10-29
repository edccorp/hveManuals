# Survey Point Clouds

!!! tip "New in HVE Studio"
    HVE Studio can show a laser scan or a photogrammetry point cloud of the real
    scene behind the simulation, so the tire marks, curb lines and damaged
    roadside objects the scan recorded can be compared with the reconstruction.

!!! warning "A point cloud is a picture, not a surface"
    Vehicles cannot drive on a point cloud, settle onto it or collide with it.
    Every engine asks the ground for an elevation, a normal and a friction at a
    point, and a set of points has none of those. Loading a cloud changes no
    result. Import a site surface for what the vehicles drove on, or build one
    from the scan (see *A drivable surface from the scan* below), and use the
    cloud for what the scene looked like; a case can, and usually should, carry
    both. There is deliberately no "use as terrain" option on the cloud itself.

## Loading a cloud

1. In the **Environment** editor, open **Environment › Environment...**, and in
   its *Terrain* section expand **Survey Point Cloud (scan)**.
2. Type the path in **Point Cloud File**, or press **Browse...**.
3. Press **Import**. While the file is read the window is busy, and the panel
   says so.
4. Check the summary line below the buttons: how many points were read and
   kept, and the offset applied (below).

**Formats:**

| Format | Notes |
| --- | --- |
| LAS 1.0–1.4 (uncompressed) | The survey standard; what a scanner or its software exports |
| PLY (ASCII or binary) | The common interchange format |
| E57 | The scanner exchange standard (ASTM E2807). Every scan in the file is loaded, each placed by its own registration; points the scanner marked invalid are skipped and counted. A damaged file is refused, naming where. |
| XYZ / PTS / TXT / CSV | `x y z [intensity] [r g b]`, space- or comma-separated |

**Gaussian splats.** A Gaussian-splat `.ply`, such as one exported by 3D Gaussian
Splatting software or a scanner's "GS" mode, loads as the splats' center points
in each splat's base color. Splats below 1% opacity, which cannot be seen, are
left out, and the summary line says how many. The splats' shapes and their
color changes with viewing angle are not drawn. A splat model is fitted to
photographs, so treat it as a picture of the scene. Measure from the scanner's
own point cloud where you have one. A splat model's size is only as good as its
scale: unless the capture recorded real-world scale, the dimensions are in whatever
units the training software chose. Models made by common training software can
also arrive upside down.

**LAZ** (compressed LAS) is read directly, LAS 1.0 to 1.4 and every point format
the USGS publishes (0 and 6 were checked against real 3DEP tiles). The whole file
is held in memory while it decodes, so a very large tile takes that much RAM. LAZ
carries no checksum: a damaged file loads the points before the damage and the
count read says it stopped short, but points decoded just before the damage can
be wrong. The format is recognized from the file's content, not its extension.

**Clear** removes the cloud.

## Placing it

A survey cloud is usually in a projected coordinate system (state plane, UTM, a
site grid), with coordinates in the millions. HVE Studio re-bases each cloud on
its own center, at full precision, and reports the offset, so a millimeter scan
is not rounded to the nearest quarter meter. On a fresh import, a cloud whose
coordinates lie within 20 km of the case's origin is put back at its own
coordinates; one farther away is centered, and the summary says so. A cloud you
have already placed is never moved by a re-import.

| Field | Meaning |
| --- | --- |
| **Scale (source -> m)** | Multiplier from the file's units to meters (a `.xyz` file carries no unit — for example 0.3048 for feet). Applies immediately. |
| **Source is Y-up**, **Source is Z-down** | The file's axis convention. Applies on the next Import. |
| **Offset X / Y / Z (m)** | Moves the cloud |
| **Yaw**, **Pitch**, **Roll (deg)** | Turns it. Pitch and roll are there because a scan is often a degree or two off level, which no amount of yaw fixes |

## How many points

| Field | Meaning |
| --- | --- |
| **Points loaded (for the surface)** | A hard limit on how many points are **loaded** (default 20 million; a survey scan is routinely 50–500 million points). The drivable surface is built from these, so more gives a finer surface. Above the limit the cloud is thinned evenly and repeatably when it is read, and the summary says by how much. Takes effect on the next Import. |
| **Points drawn per frame** | How many of the loaded points are drawn each frame on this computer (default 3 million). Lower it if the view stutters. This setting belongs to the computer, not the case. |
| **More detail near the camera** | Spends the drawn points where the scan fills the screen: close up you see it nearly whole, and distant parts thin out. Off, every part is thinned alike. |
| **Shown (%)** | Thins what is loaded, evenly, before drawing. Applies immediately. |

Below the slider the panel always says what you are looking at — *Drawing N of
M loaded (P% of the T in the file)* — so a thinned picture is never mistaken for
the whole scan.

After the first successful load HVE Studio keeps a compact copy of the points it
kept, and reads that on the next open of the case. A very large file (over
about 256 MB) with no such copy is not read when the case opens: the case opens
without the scan, the panel says so in orange with the file's name and size,
and **Import** reads it.

## How it looks

| Field | Meaning |
| --- | --- |
| **Color** | **Auto (file color, else intensity, else elevation)**, **File color**, **Intensity**, **Elevation**, **Flat gray**, or **Classification** (the file's own point classes in the usual survey colors: ground brown, vegetation green, buildings red). A mode the file cannot provide falls back visibly. |
| **Edit in Shader Editor** | Opens the Shader Editor on the cloud, to adjust its colors with a node tree — hue, saturation, brightness and contrast, gamma, invert, a color ramp — starting from the color chosen in **Color** (see *Coloring the points with nodes* below). When the cloud has a material the panel names it. |
| **Point size (px)** | The size of each dot on screen |
| **Visible** | Show or hide the cloud |
| **Eye-dome lighting (shade by depth)** | Darkens each point where its neighbors on screen are nearer the camera, so curbs, steps and edges read as shape instead of flat color. **Strength** sets how dark. Drawing only, and a setting of this computer rather than of the case. |
| **Clip box** | Draws only the scan inside the box (Min / Max x, y, z, in meters; x forward, y right, z up). **Fit to the scan** sets it to the whole cloud, to narrow from. For looking under a canopy, into a building or along one lane. Not saved, and the surface and measurements still use every point. |

Points are drawn as fixed-size dots: they do not get denser as you approach.
They are lit by the scene's sun, sky and lamps, but not shadowed.

### Coloring the points with nodes

The cloud can wear a **node material**, as a vehicle or a road surface can
(see *Point clouds* in [Materials and the Shader Editor](01-materials-and-shader-editor.md)).
Press **Edit in Shader Editor**, or choose **Point cloud** under *Survey scan*
in the Shader Editor's object list, then **+ New**: the new material passes the
point's color straight through, so nothing changes until a node is added. Put
a **Hue/Saturation/Value** node between the **Color Attribute** and the
Principled BSDF's **Base Color** to shift the hue or wash the colors out; a
**Brightness/Contrast**, **Gamma** or **Invert Color** node works the same way.
The **Point Info** node gives each point's **Intensity**, its **Elevation**
across the cloud (0 lowest, 1 highest) and its **Height** in meters, to drive a
**Color Ramp** of your own.

The node tree starts from the color **Color** gives the point, so the two work
together: choose *Intensity*, then ramp it; or keep the file's colors and lift
their contrast. With no material the cloud draws exactly as before. Display
only, like every material; it is saved with the case.

## Measuring on the scan

Under **Measure on the Scan**, tick **Click two points on the scan** and click
twice in the 3-D view. Each click picks the scan point under the cursor -- the
nearest one along the line of sight, so a car's roof is picked rather than the
road beneath it. The panel shows both points and, between them, the distance,
the distance in plan, the rise and the grade.

**Ground profile A to B** then reads the scan's ground along the line between
the two points: every **Station spacing**, the **Ground percentile** (a low
one, as the surface uses, so a car on the line is not a hump) of the points
within **Corridor half-width** of the line. It is drawn as a graph (hover for
a station's height and how many points stand behind it), with the best-fit
grade and how far the ground rises above or dips below that line -- a road's
crown, a dip, a curb. A station with no points is a gap in the graph, not a
line drawn across it. **Copy as CSV** puts the stations on the clipboard.

Measurements read the points themselves, not the drivable surface, and change
nothing in the case.

## In the case

The cloud is saved as a file reference, with its placement and display
settings, and re-read when the case opens — found the same way as the site
geometry (the case's own folder, then by name in the mesh library). A published
bundle names the cloud but does not copy the scan file into the bundle.

## A drivable surface from the scan

Under **Drivable Surface from Scan** in the same section, HVE Studio can build a
ground surface from the loaded cloud and make it the case's site, which the
engines then drive on. See *Building a drivable surface from a scan* in the
Environment Editor chapter for the settings. The surface is saved as an `.obj`
file, and the cloud itself stays a picture.
