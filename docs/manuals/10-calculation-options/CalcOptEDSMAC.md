# EDSMAC Calculation Options

EDSMAC (Engineering Dynamics Corporation Simulation Model of Automobile Collisions) is a simulation analysis of two-vehicle crashes, based on the SMAC program developed at Calspan for NHTSA. The Calculation Options dialog for an EDSMAC event exposes the collision-phase solution parameters described below. Each parameter is stored with the event and read by the physics engine when the event is executed.

The collision algorithm models each vehicle's periphery as a set of radial RHO vectors extending outward from the CG. During vehicle-to-vehicle contact the collision routine iteratively shortens the overlapping RHO vectors until the collision pressures acting between the two vehicles are in equilibrium; the shortened vectors define the crush profile.

## Vector Spacing (deg)

Default: 2.0 degrees. Range: 1.0 to 5.0 degrees (stored internally in radians, 0.0174 to 0.08727 rad).

This angle determines the angular interval between the RHO vectors that define each vehicle's crush perimeter. Smaller values give a finer damage profile at the cost of computation time (the number of RHO vectors per vehicle is 360°/spacing — 181 vectors at the 2-degree default).

## Vector Adjustment Increment (in)

Default: 0.20 in. Range: 0.01 to 0.5 in.

This increment determines the incremental adjustment applied to each RHO vector as the collision routine seeks to establish force equilibrium between the vehicles.

## Vector Force Tolerance (lb/in)

Default: 15.0 lb/in. Range: 5.0 to 50.0 lb/in.

The allowable difference in the collision pressure (force per unit width) computed along corresponding RHO vectors for each vehicle. A small value is preferable; in general it should not exceed 50 lb/in (about 100 N/cm). (In the current release this control is labeled *Max Pressure Error* in the dialog.)

## Inter-Vehicle Friction

Default: 0.55. Range: 0.05 to 2.0 (dimensionless).

The coefficient of sliding friction between the vehicle exteriors, used to compute the tangential (friction) component of the collision force.

*Note:* the original on-line help interchanged the descriptions of this option and *Min Velocity for Friction*, below. The descriptions given here are correct: this field is the inter-vehicle friction coefficient, and the field below is the minimum velocity at which that friction is fully developed.

## Min Velocity for Friction (in/sec)

Default: 5.0 in/sec. Slider range: 5.0 to 50.0 in/sec (values from 0.1 to 100 in/sec may be typed).

The minimum relative tangential surface velocity at which the full inter-vehicle friction is achieved. Below this velocity the friction force is scaled linearly with the relative sliding velocity, so the effective friction coefficient becomes $\mu\,(v_t / v_{min})$, where $\mu$ is the Inter-Vehicle Friction value, $v_t$ the relative tangential velocity and $v_{min}$ this minimum velocity. This prevents numerical chatter as the contact velocity approaches zero.

## Restitution Constant

Default: 0.04606. Range: 0.0 to 1.0.

The constant term of the parametric restitution model used by EDSMAC during the unloading (restitution) phase of the collision. The effective restitution applied to each damaged RHO vector is computed from that vector's change in length (crush depth) δ:

> e(δ) = c0 − c1·δ + c2·δ²

Restitution is applied only while δ is less than c1/(2·c2) (the vertex of the parabola); each damaged vector is allowed to "rebound" toward its undamaged length in proportion to e.

## Restitution Linear Coef (1/in)

Default: 0.0017547 1/in. Range: 0.0 to 0.1 1/in.

The linear (crush-depth proportional) term of the parametric restitution model.

## Restitution Quadratic Coef (1/in^2)

Default: 0.000016711 1/in². Range: 0.0 to 50.0 1/in².

The quadratic term of the parametric restitution model.

## Terrain Search Options (moved to the Get Surface Information dialog)

The old help listed *From First Polygon*, *From Previous Polygon* and *By Elevation* as EDSMAC calculation options, with no descriptions. These terrain-database search options are no longer part of the EDSMAC Calculation Options dialog: they are now set in the separate **Get Surface Information Options** dialog (Options menu), which applies to any simulation event. The **Method**, **Direction** and z-component settings made there are stored with each event. Case files older than version 63 automatically migrate their old EDSMAC terrain-search setting into the new dialog.

These options control how HVE searches the terrain polygon (triangle) database for the surface elevation, normal, friction and water depth beneath each tire at every timestep.

**Method** (default: From Previous Polygon, Sorted):

- **From First Polygon** — Every query searches the whole database in list order from the first polygon and uses the first polygon containing the search point. Simple, but slowest on large terrains.
- **From Previous Polygon** — Water polygons are checked first, then the search starts at the polygon found on the previous call and spreads outward (forward and backward) through the database, returning on the first hit. Fast on contiguous terrain meshes, but friction-zone precedence is not enforced.
- **From Previous Polygon, Sorted** (default) — Water, curb and friction-zone polygons are always checked first, so friction zones painted over a road surface correctly take precedence over the underlying road polygons; the remaining road polygons are then searched spreading outward from the previous polygon.
- **By Elevation** — Intended to search the entire database and keep the highest surface beneath the wheel center (for overlapping surfaces such as bridge decks). **Not currently implemented:** the radio button is disabled in the dialog, and if the option is ever selected EDSMAC reports a fatal error at execution and the event will not run.

**Direction** (default: Upward Facing Only) — controls which terrain triangles are admitted to the physics terrain database when the environment geometry is compiled:

- **All Directions** — All road/friction-zone/water triangles are usable regardless of the direction of their surface normal.
- **Upward Facing Only** (default) — Only triangles whose surface normal has an upward component are used. Curb polygons are exempt from the normal test.
- **Z Component, Greater Than** — Only triangles whose unit surface normal has a z-component greater than the user-entered value (allowed range −1.0 to 1.0, default 0.0) are used; the edit field is enabled only for this choice.

---
*Updated to match the current version of HVE.*

<!-- NAV -->

---

← Previous: [Calculation Options for EDGEN](CalcOptEDGENDlg.md)  |  [Index](README.md)  |  Next: [EDSMAC4 Calculation Options](CalcOptEDSMAC4.md) →

<!-- /NAV -->
