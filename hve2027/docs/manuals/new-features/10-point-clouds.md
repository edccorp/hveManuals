# Survey Point Clouds

!!! tip "New in HVE 2027"
    HVE 2027 can show a laser scan or a photogrammetry point cloud of the real
    scene behind the simulation, so the tire marks, kerb lines and damaged
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

**LAZ** (compressed LAS) is refused: export it as uncompressed `.las`, or as
`.ply` or `.xyz`. The format is recognised from the file's content, not its
extension.

**Clear** removes the cloud.

## Placing it

A survey cloud is usually in a projected coordinate system (state plane, UTM, a
site grid), with coordinates in the millions. HVE 2027 re-bases each cloud on
its own centre, at full precision, and reports the offset, so a millimetre scan
is not rounded to the nearest quarter metre. On a fresh import, a cloud whose
coordinates lie within 20 km of the case's origin is put back at its own
coordinates; one farther away is centred, and the summary says so. A cloud you
have already placed is never moved by a re-import.

| Field | Meaning |
| --- | --- |
| **Scale (source -> m)** | Multiplier from the file's units to metres (a `.xyz` file carries no unit — for example 0.3048 for feet). Applies immediately. |
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

After the first successful load HVE 2027 keeps a compact copy of the points it
kept, and reads that on the next open of the case. A very large file (over
about 256 MB) with no such copy is not read when the case opens: the case opens
without the scan, the panel says so in orange with the file's name and size,
and **Import** reads it.

## How it looks

| Field | Meaning |
| --- | --- |
| **Colour** | **Auto (file colour, else elevation)**, **File colour**, **Intensity**, **Elevation**, or **Flat grey**. A mode the file cannot provide falls back visibly. |
| **Point size (px)** | The size of each dot on screen |
| **Visible** | Show or hide the cloud |

Points are drawn as fixed-size dots: they do not get denser as you approach,
and they are not lit or shadowed.

## In the case

The cloud is saved as a file reference, with its placement and display
settings, and re-read when the case opens — found the same way as the site
geometry (the case's own folder, then by name in the mesh library). A published
bundle names the cloud but does not copy the scan file into the bundle.

## A drivable surface from the scan

Under **Drivable Surface from Scan** in the same section, HVE 2027 can build a
ground surface from the loaded cloud and make it the case's site, which the
engines then drive on. See *Building a drivable surface from a scan* in the
Environment Editor chapter for the settings. The surface is saved as an `.obj`
file, and the cloud itself stays a picture.
