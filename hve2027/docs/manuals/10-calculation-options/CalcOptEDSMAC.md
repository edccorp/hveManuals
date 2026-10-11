# EDSMAC Calculation Options

EDSMAC (Engineering Dynamics Corporation Simulation Model of Automobile Collisions) is a simulation analysis of two-vehicle crashes, based on the SMAC program developed at Calspan for NHTSA. Its calculation options are the collision-phase solution parameters described below. Each parameter is stored with the event and read by the physics engine when the event is executed.

The collision algorithm models each vehicle's periphery as a set of radial RHO vectors extending outward from the CG. During vehicle-to-vehicle contact the collision routine iteratively shortens the overlapping RHO vectors until the collision pressures acting between the two vehicles are in equilibrium; the shortened vectors define the crush profile.

## Opening the options

In Event Information, with an EDSMAC event active, press **Method Options...**
under Calculation Method. The **EDSMAC Options** window opens. EDSMAC and EDSMAC4
share this window; the groups below the restitution coefficients
(*Inter-Vehicle Connection*, *Hydroplane Model*, *Accident History*,
*Connection Model*, *Damage Data Format* and the rho-vector initialization) are
read by EDSMAC4 only and are described in
[EDSMAC4 Calculation Options](CalcOptEDSMAC4.md). Lengths, forces and speeds are
shown in the units set in Preferences.

## Angular Sweep Interval (deg)

HVE's *Vector Spacing*. Default: 2.0 degrees. HVE 2027 accepts 0.05 to 45 degrees
(HVE's dialog allowed 1.0 to 5.0).

This angle determines the angular interval between the RHO vectors that define each vehicle's crush perimeter. Smaller values give a finer damage profile at the cost of computation time (the number of RHO vectors per vehicle is 360°/spacing — 181 vectors at the 2-degree default).

## Radial Depth Interval

HVE's *Vector Adjustment Increment*. Default: 0.20 in. (HVE's range: 0.01 to 0.5 in.)

This increment determines the incremental adjustment applied to each RHO vector as the collision routine seeks to establish force equilibrium between the vehicles.

## Max Pressure Error

HVE's *Vector Force Tolerance*. Default: 15.0 lb/in. (HVE's range: 5.0 to 50.0 lb/in.)

The allowable difference in the collision pressure (force per unit width) computed along corresponding RHO vectors for each vehicle. A small value is preferable; in general it should not exceed 50 lb/in (about 100 N/cm).

## Min Friction Velocity

HVE's *Min Velocity for Friction*. Default: 5.0 in/sec.

The minimum relative tangential surface velocity at which the full inter-vehicle friction is achieved. Below this velocity the friction force is scaled linearly with the relative sliding velocity, so the effective friction coefficient becomes $\mu\,(v_t / v_{min})$, where $\mu$ is the Inter-Vehicle Friction value, $v_t$ the relative tangential velocity and $v_{min}$ this minimum velocity. This prevents numerical chatter as the contact velocity approaches zero.

## Inter-Vehicle Friction

Default: 0.55 (dimensionless).

The coefficient of sliding friction between the vehicle exteriors (the two bodies, not the tires or the road), used to compute the tangential (friction) component of the collision force.

*Note:* the original on-line help interchanged the descriptions of this option and *Min Velocity for Friction*. The descriptions given here are correct.

## Restitution (crho = c0 − c1·d + c2·d², d = crush depth)

The parametric restitution model used by EDSMAC during the unloading (restitution) phase of the collision. The effective restitution applied to each damaged RHO vector is computed from that vector's change in length (crush depth) δ:

> e(δ) = c0 − c1·δ + c2·δ²

Restitution is applied only while δ is less than c1/(2·c2) (the vertex of the parabola); each damaged vector is allowed to "rebound" toward its undamaged length in proportion to e. A line under the coefficients gives that crush depth for the values entered.

- **Restitution Constant** — Default: 0.04606.
- **Restitution Linear Coef (1/in)** — Default: 0.0017547 1/in.
- **Restitution Quadratic Coef (1/in²)** — Default: 0.000016711 1/in².

!!! note "HVE 2027"
    The two coefficients are shown per inch or per centimetre, following the
    length unit set in Preferences, as HVE shows them in its vehicle length
    unit.

## Per-pair override

With two or more vehicles in the event, a grid lists each vehicle pair with an
**Inter-Vehicle Friction** override (blank = use the value above). HVE stores
this per pair. EDSMAC, a two-vehicle program with a single friction value, uses
the override for the V1–V2 pair if one is entered.

## Terrain Search Options

The old help listed *From First Polygon*, *From Previous Polygon* and *By Elevation* as EDSMAC calculation options. In HVE 2027 the terrain search is chosen per event in the **Road Surface Search** section of [Event Information](../09-events-driver-controls/EventInfo.md#road-surface-search), which offers first polygon, previous polygon and previous polygon with friction zones first.

!!! warning "Not in HVE 2027"
    *By Elevation* and the search **Direction** settings (All Directions /
    Upward Facing Only / Z Component Greater Than) are not offered.

<!-- NAV -->

---

← Previous: [Calculation Options for EDGEN](CalcOptEDGENDlg.md)  |  [Index](README.md)  |  Next: [EDSMAC4 Calculation Options](CalcOptEDSMAC4.md) →

<!-- /NAV -->
