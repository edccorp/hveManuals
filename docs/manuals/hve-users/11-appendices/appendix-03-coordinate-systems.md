# Appendix III — Coordinate Systems

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Appendix III, pages III-1 through III-8.*

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

<!-- NAV -->

---

← Previous: [Appendix II — Messages](appendix-02-messages.md)  |  [Index](README.md)  |  Next: [Appendix IV — Units](appendix-04-units.md) →

<!-- /NAV -->
