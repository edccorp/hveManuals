# EDSMAC Calculation Options

EDSMAC (Engineering Dynamics Corporation Simulation Model of Automobile Collisions) is a simulation analysis of two-vehicle crashes, based on the SMAC program developed at Calspan for NHTSA. The Calculation Options dialog for an EDSMAC event (dialog `IDD_CALC_OPTIONS_EDSMAC`, class `CEdSmacDlg`) exposes the collision-phase solution parameters described below. Each parameter is stored with the event (`CalcOptions.calcFloat[]`) and read by the physics engine in `Physics/Source/Edsmac/SMAINPUT.CPP`.

The collision algorithm models each vehicle's periphery as a set of radial RHO vectors extending outward from the CG. During vehicle-to-vehicle contact the collision routine iteratively shortens the overlapping RHO vectors until the collision pressures acting between the two vehicles are in equilibrium; the shortened vectors define the crush profile.

## Vector Spacing (deg)

Internal variable: `delpsi` (DELPSI), `calcFloat[0]`. Default: 2.0 degrees. Range: 1.0 to 5.0 degrees (stored internally in radians, 0.0174 to 0.08727 rad).

This angle determines the angular interval between the RHO vectors that define each vehicle's crush perimeter. Smaller values give a finer damage profile at the cost of computation time (the number of RHO vectors per vehicle is 360°/spacing — 181 vectors at the 2-degree default).

## Vector Adjustment Increment (in)

Internal variable: `delrho` (DELRHO), `calcFloat[1]`. Default: 0.20 in. Range: 0.01 to 0.5 in.

This increment determines the incremental adjustment applied to each RHO vector as the collision routine seeks to establish force equilibrium between the vehicles.

## Vector Force Tolerance (lb/in)

Internal variable: `alamb` (ALAMB), `calcFloat[2]`. Default: 15.0 lb/in. Range: 5.0 to 50.0 lb/in.

The allowable difference in the collision pressure (force per unit width) computed along corresponding RHO vectors for each vehicle. A small value is preferable; in general it should not exceed 50 lb/in (about 100 N/cm). (In the current resource file, `Language.rsc` entry `EDSMACOptionsLamda`, this control is labeled *Max Pressure Error* at run time.)

## Inter-Vehicle Friction

Internal variable: `amu` (AMU), `calcFloat[3]`. Default: 0.55. Range: 0.05 to 2.0 (dimensionless).

The coefficient of sliding friction between the vehicle exteriors, used to compute the tangential (friction) component of the collision force.

*Note:* the original help attributed this option to the variable ZETAV; in the source code (`SMAINPUT.CPP`, `COLL.CPP`) the friction coefficient is `amu`, and ZETAV is the minimum velocity, below.

## Min Velocity for Friction (in/sec)

Internal variable: `zetav` (ZETAV), `calcFloat[4]`. Default: 5.0 in/sec. Slider range: 5.0 to 50.0 in/sec (values from 0.1 to 100 in/sec may be typed).

The minimum relative tangential surface velocity at which the full inter-vehicle friction is achieved. Below this velocity the friction force is scaled linearly with the relative sliding velocity (`frict = amu*(vtmvt/zetav)`), which prevents numerical chatter as the contact velocity approaches zero.

## Restitution Constant

Internal variable: `c0`, `calcFloat[5]`. Default: 0.04606. Range: 0.0 to 1.0.

The constant term of the parametric restitution model used by EDSMAC during the unloading (restitution) phase of the collision. The effective restitution applied to each damaged RHO vector is computed from that vector's change in length (crush depth) δ:

> e(δ) = c0 − c1·δ + c2·δ²

Restitution is applied only while δ is less than c1/(2·c2) (the vertex of the parabola); each damaged vector is allowed to "rebound" toward its undamaged length in proportion to e (`COLL.CPP`).

## Restitution Linear Coef (1/in)

Internal variable: `c1`, `calcFloat[6]`. Default: 0.0017547 1/in. Range: 0.0 to 0.1 1/in.

The linear (crush-depth proportional) term of the parametric restitution model.

## Restitution Quadratic Coef (1/in^2)

Internal variable: `c2`, `calcFloat[7]`. Default: 0.000016711 1/in². Range: 0.0 to 50.0 1/in².

The quadratic term of the parametric restitution model.

## Terrain Search Options (moved to the Get Surface Information dialog)

The old help listed *From First Polygon*, *From Previous Polygon* and *By Elevation* as EDSMAC calculation options, with no descriptions. These terrain-database search options are no longer part of the EDSMAC Calculation Options dialog: they are now set in the separate **Get Surface Information Options** dialog (Options menu, dialog `IDD_GETSURFACEINFO`, class `CGetSurfaceInfoDlg`), which applies to any simulation event and is stored per event as `GetSurfaceInfo` (`Method`, `Direction`, `NormalZ`). Case files older than version 63 automatically migrate the old `calcInt[0]` value into the new structure (`Calc.cpp`).

These options control how `GetSurfaceInfo()` (`Physics/Source/LibHve/Surface.cpp`) searches the terrain polygon (triangle) database for the surface elevation, normal, friction and water depth beneath each tire at every timestep.

**Method** (default: From Previous Polygon, Sorted):

- **From First Polygon** (`USE_ALL_TRIANGLES`, 0) — Every query searches the whole database in list order from the first polygon and uses the first polygon containing the search point. Simple, but slowest on large terrains.
- **From Previous Polygon** (`USE_PREVIOUS_WITHOUT_FRICT_ZONES`, 1) — Water polygons are checked first, then the search starts at the polygon found on the previous call and spreads outward (forward and backward) through the database, returning on the first hit. Fast on contiguous terrain meshes, but friction-zone precedence is not enforced.
- **From Previous Polygon, Sorted** (`USE_PREVIOUS_WITH_FRICT_ZONES`, 2 — default) — Water, curb and friction-zone polygons are always checked first, so friction zones painted over a road surface correctly take precedence over the underlying road polygons; the remaining road polygons are then searched spreading outward from the previous polygon.
- **By Elevation** (`USE_ELEVATION`, 3) — Intended to search the entire database and keep the highest surface beneath the wheel center (for overlapping surfaces such as bridge decks). **Not currently implemented:** the radio button is disabled in the dialog, and EDSMAC rejects the option at execution with `ERROR_BAD_EVENT_GETSURFACE_OPT3_NOT_SUPPORTED`.

**Direction** (default: Upward Facing Only) — controls which terrain triangles are admitted to the physics terrain database when the environment geometry is compiled (`EnvironNode::figureTrianglesForPhysics()`, `HVEINV-64/Environ.cpp`):

- **All Directions** (0) — All road/friction-zone/water triangles are usable regardless of the direction of their surface normal.
- **Upward Facing Only** (1, default) — Only triangles whose surface normal has an upward component are used. Curb polygons are exempt from the normal test.
- **Z Component, Greater Than** (2) — Only triangles whose unit surface normal has a z-component greater than the user-entered value (`GetSurfaceZValue`, allowed range −1.0 to 1.0, default 0.0) are used; the edit field is enabled only for this choice.

---
*Source topic: CalcOptEDSMAC.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Calculation Options for EDGEN](CalcOptEDGENDlg.md)  |  [Index](README.md)  |  Next: [EDSMAC4 Calculation Options](CalcOptEDSMAC4.md) →

<!-- /NAV -->
