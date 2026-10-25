# Appendix III — Coordinate Systems

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Appendix III, pages III-1 through III-8, adapted for HVE Studio.*

Coordinate systems are used to define the locations of objects, such as
humans and vehicles. HVE uses the following coordinate systems:

- **Earth-fixed** — Used to define the location of objects relative to the
  earth
- **Vehicle-fixed** — Used to define the location of objects relative to a
  vehicle
- **Tire-fixed** — Used to define the position and orientation of a tire
- **Human-fixed** — Used to define the location of objects relative to a
  human

These coordinate systems are described in detail below.

!!! note "HVE Studio"
    HVE Studio uses these coordinate systems unchanged: positions, headings and every input and output of the calculation models are in HVE's SAE frames. A few HVE Studio dialogs and exports use other frames for display; they are listed in [Display and Export Frames](#display-and-export-frames) below.

## Earth-fixed

The earth-fixed coordinate system may be thought of as a large coordinate
system attached to the surface of the earth. It is never moved. It locates
objects (vehicles and human pedestrians) on or above the earth's surface.

The origin of the earth-fixed coordinate system may be placed anywhere, and
the Z axis points down, towards the center of the earth (in the direction of
the gravity vector). The X-Y plane is normal to the Z axis; the X axis may
point in any direction in this plane and the Y axis points to the right
(i.e., clockwise 90 degrees) from X.

All angles are defined relative to the X, Y, Z axes. The heading angle
($\Psi$) is defined about the Z axis; roll ($\Phi$) and pitch ($\Theta$) are
about the X and Y axes, respectively.

*Figure III-1 — Earth-fixed coordinate system. Z is in the direction of
gravity (down); X and Y are orthogonal to each other, as well as to Z.*

Vehicle and pedestrian path coordinates and heading angles are defined
relative to the earth-fixed coordinate system.

> **NOTE:** Because Z points down, a positive heading change (about +Z) is
> clockwise when viewed from above — a right turn.

## Vehicle-fixed

The vehicle-fixed coordinate system may be thought of as a smaller
coordinate system attached firmly to the vehicle; it never moves with
respect to the vehicle, but moves along with the vehicle with respect to the
earth-fixed coordinate system.

*Figure III-2 — Vehicle-fixed coordinate system.*

The orientation of the vehicle-fixed coordinate system is not arbitrary. Its
origin is at the vehicle's center of gravity (CG). The x axis points towards
the front of the vehicle, and defines the vehicle's heading angle with
respect to the earth-fixed coordinate system. The y axis points to the
right, and the z axis points down. *(The original printing said "the y axis
points towards the front"; per SAE J670e and Figure III-2, the longitudinal
forward axis is x.)*

> **NOTE:** Consistent with SAE J670e, the earth-fixed axes are denoted by
> upper-case characters (X, Y, Z), while the vehicle-fixed axes are denoted
> by lower-case characters (x, y, z).

All vehicle-related data, such as wheel locations, steer angles and sideslip
angles, are defined relative to the vehicle-fixed coordinate system.

!!! note "HVE Studio"
    The calculation models number the two wheels of an axle with the **right** wheel (+y) first. HVE Studio's per-wheel output channels follow that order. Its per-wheel tables show each axle the way a vehicle is pictured from behind, left then right — columns read A1 Left, A1 Right, A2 Left, and so on; the order of the columns changes nothing in the data.

### Articulated Vehicles

*Figure III-3 — Articulated vehicles. Roll, pitch and yaw articulation
angles are defined about the vehicle-fixed x, y and z axes, respectively.*

Articulated vehicles (i.e., vehicle trailers and dollies) are positioned
using the vehicle-fixed coordinate system, using their roll, pitch and yaw
articulation angles with respect to the towing vehicle.

## Tire-fixed

The tire axis system is attached to the vehicle and defines the orientation
of a tire. The origin of the tire axis system is the center of the tire
contact patch.

The X' axis is the intersection of the wheel plane and the road surface
plane, with the positive direction pointing forward. The Z' axis is normal
to the X' axis with the positive direction downward, normal to the road
surface plane. The Y' axis is in the road surface plane, its direction
chosen to be orthogonal to X' and Z'.

*Figure III-4 — Tire Coordinate Axis System [6.2].*

## Human-fixed

The human-fixed coordinate system may be thought of as a smaller coordinate
system attached firmly to the human; it never moves with respect to the
human, but moves along with the human with respect to the earth-fixed
coordinate system.

The human model is composed of 15 segments and 14 joints. Each segment has
an i, j, k coordinate axis system with its origin at the segment CG. Joints
and contact ellipsoids are positioned relative to the i, j, k coordinate
axis system. Roll, pitch and yaw rotations are defined about the i, j and k
segment axes, respectively.

*Figure III-5 — Human-fixed coordinate system.*

Human positions are defined relative to either the earth-fixed (for human
pedestrians) or vehicle-fixed (for human occupants) coordinate systems. The
origin of the human-fixed coordinate system is the center of gravity (CG) of
the pelvis segment. Its forward (x), lateral (y) and vertical (z) directions
are coincident with the i, j, k axes for the pelvis segment (see Figure
III-5). Thus, when you position a human relative to either the earth or
vehicle, you are really positioning the pelvis. The position and orientation
of the other 14 segments are defined by their yaw, pitch and roll
articulation angles with respect to adjacent upstream segments (i.e., the
articulation angles for the upper leg are relative to the pelvis, the
articulation angles for the lower leg are relative to the upper leg, and so
on).

## Your Coordinate Convention

!!! tip "New in HVE Studio"
    **Preferences > Coordinates** chooses how positions, headings and angles are shown and typed, and you can leave it on one choice for good. It changes what you see and enter, never what is stored: the case, its files and every calculation stay SAE, so switching it cannot change a result.

    | | SAE (default) | Conventional |
    |---|---|---|
    | x | forward | forward |
    | y | right | **left** |
    | z | down | **up** |
    | Heading / yaw | clockwise from above | **counter-clockwise** from +x |
    | Pitch | nose up positive | **nose down** positive |
    | Roll | right side down positive | right side down positive |

    Conventional is the SAE frame turned 180 degrees about x, so x and roll are the same in both. Exact zeros stay zero, and the values stored in the case are identical whichever you pick.

    - **Follows the setting:** event start position and heading (X, Y, Heading, Articulation, Sideslip, Yaw rate, Pitch), the Named Positions table, the driver and human path tables, wheel and connection positions, accelerometer, airbag, light, aboard and cargo positions, camera positions, targets, mounts and aim points, environment placement and light positions, the numbers typed into the viewport's G and R tools, and the output channels (the key results, graph, timestep table and CSVs of those panels). The channels follow the rule above: the y and z components of every vector, yaw and pitch change sign, and x components, roll, scalars and magnitudes do not. A reverse gear stays negative. **Output > Export Variables > Coordinate System** offers the same rule as **Conventional**, whose choice follows this setting by default, and keeps HVE's own sign list as **Traditional**; the two differ on about two dozen variables, described under Export Variables.
    - **Also follows the setting:** the point cloud's pitch and roll (a stored cloud pitch is nose-down positive and a stored roll right-side-up positive, so SAE shows pitch nose up and roll right side down), the wind direction and the EDCRASH PDOF (both clockwise-positive angles, counter-clockwise under Conventional).
    - **Fixed, and said so beside the field:** an occupant segment's own axes, the belt anchors, an airbag's yaw and roll, and camera keyframes in the Dope Sheet.
    - **Heights stay heights:** Z Height (the CG above the ground), site elevation, light height and crush depths are positive up in both conventions.
    - **Labels:** a field that states a direction ("Y right", "Z down") shows the direction the current setting uses.
    - **Always SAE:** the engine report pages and the **Plan View** in the run report keep SAE and say so.
    - **Imported site files** keep their fixed frame rules (below); only the offsets and placement you type follow the setting. A Z-up site file already uses the Conventional axes, so its coordinates read the same on screen under **Conventional**.

## Display and Export Frames

!!! tip "New in HVE Studio"
    Where HVE Studio shows or exchanges positions outside the calculation models, it states the frame:

    | Where | Frame |
    |---|---|
    | Case data, all stored values, and the engine report pages | Earth-fixed and vehicle-fixed SAE: x forward, y right, z **down**. Event Information, Position / Velocity and the output channels show this by default and follow **Preferences > Coordinates** |
    | Cameras (eye, target, onboard mount and aim point); Viewport View camera target | stored x forward, y right, z **up**; shown in the convention chosen in **Preferences > Coordinates** |
    | Environment geometry imported from DXF, OBJ or glTF | read as z **up** (or Y-up with **File is Y-up**) and converted |
    | Environment `.h3d` | converted from the file's own frame (**Flip About X-Axis** corrects a file whose vertical sense is reversed) |
    | Vehicle `.h3d` meshes | z **down**, as in HVE |
    | glTF export | glTF's +Y up: glTF (x, y, z) = (−Y, −Z, X) of the SAE coordinates — a proper rotation, not a mirror |
    | Blender live link | Blender's Z up: Blender (x, y, z) = (Y, X, −Z) of the SAE coordinates; rotations are sent as quaternions (W, X, Y, Z) |

    Rotations carried into another frame are converted as rotations, so a right turn in HVE Studio is a right turn in Blender.

<!-- NAV -->

---

← Previous: [Appendix II — Messages](appendix-02-messages.md)  |  [Index](README.md)  |  Next: [Appendix IV — Units](appendix-04-units.md) →

<!-- /NAV -->
