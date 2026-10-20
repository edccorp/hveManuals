# Chapter 13 — Environment Model Definition

This chapter provides a detailed definition of the HVE Environment Model.
The Environment Model's parameters define both the physical and the visual
characteristics used by the current reconstruction or simulation model.

## Overview

Chapter 13 is a very important chapter. One of HVE's most powerful features
is the ability of humans and vehicles to interact with (drive on or slide
on) the earth's surface. Another important feature is HVE's ability to view
scenes obstructed by smoke or fog. These features are part of HVE's
environment model. The mechanisms by which these features are implemented
are described in this chapter.

The subject of the environment is divided into three basic topics:

- **Earth's Surface** — Gravitational Constant and 3-D Driving Surfaces
  used to calculate interaction forces.
- **Atmosphere** — Sky Color, Temperature, Pressure, Wind Velocity and
  Direction, Fog and Sight Distance used to help visualize the scene.
- **Sun Position** — Latitude, Longitude, GMT, Time/Date and Angle of the
  Earth-fixed X-axis used to determine the location of the sun and its
  lighting effects on the scene.

Each of these topics is addressed in this chapter.

## Surface Model

The Environment Surface Model defines how humans and vehicles interact with
the environment to produce forces that affect motion. The two physical
factors in the Environment Surface Model are:

- 3-D Physical Surfaces
- Gravitational Constant

### 3-D Physical Surface Characteristics

Perhaps the single most powerful feature of HVE is the fact that HVE
actually views the 3-D environment as a physical surface. Humans and
vehicles may interact with this physical surface during execution to
determine tire and other forces. The importance of this simple statement
cannot be stressed enough! It means that, if the environment has a road, any
simulated human or vehicle will roll or drive on the surface; if the
environment has a hill, a simulated vehicle will naturally drive up the
hill; if it has a ditch, the vehicle may roll into it; if it has a cliff,
the vehicle may drive off it.

> **NOTE:** This capability of HVE must be taken advantage of by the human
> or vehicle simulation model, which queries HVE for the surface beneath
> each contact point. Refer to the individual calculation model's
> documentation to determine if this feature is included in the model.

!!! note "HVE Studio"
    HVE Studio runs HVE's own physics, so the surface model below is HVE's.
    The site geometry reaches the engines only when **Use surfaces as
    terrain (physics)** is checked in the Environment panel's Terrain
    section, and only the surfaces whose **Drive** switch is on (see
    [Chapter 12](12-creating-editing-environments.md)). With no site
    geometry, the engines run on flat, level ground.

#### How It Works

During execution, the reconstruction or simulation model may request the
following information for any earth-fixed X,Y coordinates of the HVE
environment (see Figure 13-1, Figure 13-2 and Table 13-1):

![Figure 13-1](../images/p461-figB13-1.png)
*Figure 13-1: 3-D Surface Model Definition.*

- **Elevation** — The Z-coordinate of the environment surface at X,Y.
- **Slope** — The surface normal vector, u<sub>x</sub>, u<sub>y</sub>,
  u<sub>z</sub>, of the environment at X,Y.
- **Material Name** — A user-editable name describing the terrain at X,Y.
- **Force Constant** — The force required to initiate deflection of the
  terrain at X,Y.
- **Linear Stiffness** — The first-order force-deflection coefficient of
  the terrain at X,Y.
- **Quadratic Stiffness** — The second-order force-deflection coefficient
  of the terrain at X,Y.
- **Cubic Stiffness** — The third-order force-deflection coefficient of the
  terrain at X,Y.
- **Damping Constant** — The velocity-dependent force contribution of the
  terrain at X,Y.
- **Friction Factor** — The friction multiplier for the environment surface
  at X,Y.

> **NOTE:** The Friction Factor is a multiplier, not a friction coefficient!
> See below for details.

- **Unloading Slope** — The first-order unloading force-deflection
  coefficient of the terrain at X,Y.
- **Bekker Soil Exponent, N** — The exponent of deformation used in the
  soil mechanics equations for the terrain at X,Y (used by the Soft Soil
  Tire-Terrain Model).
- **Frictional Soil Modulus, Kphi** — Frictional soil constant used in soil
  sinkage calculations for the terrain at X,Y (used by the Soft Soil
  Tire-Terrain Model).
- **Cohesive Soil Modulus, Kc** — Cohesive soil constant used in soil
  sinkage calculations for the terrain at X,Y (used by the Soft Soil
  Tire-Terrain Model).
- **Moisture Content** — The amount of moisture in the soil for the terrain
  at X,Y.
- **Macrotexture** — The surface macrotexture depth of the terrain at X,Y,
  used by tire-road friction (e.g., wet-road) calculations. *(updated: the
  current material model carries Macrotexture in place of the Clay Content
  parameter listed in earlier editions; see the [Environment Material
  Properties dialog](../../08-environment/EnvrMatPropDlg.md).)*

![Figure 13-2](../images/hvn-05-surface-node.png)
*Figure 13-2: A surface's contact material in HVE Studio — the HVE Surface node in the Shader Editor, opened with Edit in Shader Editor from the Environment panel's Selected Surface section.*

!!! note "HVE Studio"
    In HVE Studio these parameters are edited per surface on the **HVE
    Surface** node in the Shader Editor (select the surface, then **Edit in
    Shader Editor**), and for the fallback material on the **Default
    material** button of the Environment panel's Selected Surface section. The
    labels are: **Friction Multiplier**, **Force Constant**, **Linear
    Stiffness**, **Quadratic Stiffness**, **Cubic Stiffness**, **Damping
    Rate**, **Unloading Stiffness**, **Bekker Constant**, **Kphi**, **Kc**
    and **Moisture (%)**, then **Water Depth**, **Wet Friction** and
    **Texture Depth** under *Standing water* -- the Macrotexture above, the
    same twelfth material term HVE's older dialogs called Clay Content, and
    imported from an HVE site with each surface. The Bekker soil terms (Kphi, Kc) are
    always shown in HVE's English units, because their units depend on the
    Bekker exponent. The default material's Friction Multiplier is 1.0.

> **NOTE:** The Bekker Soil Exponent, Frictional Soil Modulus and Cohesive
> Soil Modulus are used by the Soft Soil Tire-Terrain Model. See the
> Tire-Terrain Model discussion in Chapter 4.

A vehicle simulation's tire model obviously can benefit from this
information: given a tire's current X,Y (earth-fixed) coordinates, the
simulation's tire model can learn all the above attributes for the terrain
in the vicinity of each tire. A human simulation's contact ellipsoids can
also include these effects when calculating forces on each human body
segment for pedestrians struck on the roadway. The same is true of the
vehicle's 3-D geometry; these data are used for rollover simulation.

**Table 13-1: Environment Terrain Material Parameters**

| Parameter | Unit Name | Description |
|---|---|---|
| Z-coord | UtEnvDispLength | Elevation at X,Y |
| u<sub>x</sub>, u<sub>y</sub>, u<sub>z</sub> | UtNone | Unit normal vector defining the slope at X,Y |
| Material Name | UtNone | User-editable material name for terrain at X,Y |
| Constant | UtEnvForce | Force required to initiate deflection at X,Y |
| Linear Stiffness | UtEnvMatLinear | Linear material deformation coefficient at X,Y |
| Quadratic Stiffness | UtEnvMatQuad | Quadratic material deformation coefficient at X,Y |
| Cubic Stiffness | UtEnvMatCubic | Cubic material deformation coefficient at X,Y |
| Damping Constant | UtEnvMatDamp | Material velocity-dependent deformation constant at X,Y |
| Friction Constant | UtNone | Friction multiplier at X,Y |
| Unloading Slope | UtEnvMatForce | Linear unloading slope beginning at maximum deflection |
| Bekker Soil Exponent | UtNone | Soil deformation exponent for sinkage calculations |
| Frictional Soil Modulus | UtEnvKphi | Frictional soil constant for sinkage calculations |
| Cohesive Soil Modulus | UtEnvKc | Cohesive soil constant for sinkage calculations |
| Moisture Content | UtEnvPercent | Percentage of moisture in the soil |
| Macrotexture | UtEnvDispLength | Surface macrotexture depth at X,Y *(updated: replaces the Clay Content (UtEnvPercent) row in earlier editions)* |

#### How to Define Surface Characteristics

The surface model characteristics are defined directly by the 3-D surface
polygons (sometimes called 3-D geometry) used to create the environment.
The 3-D geometry database often includes tens of thousands of polygons.
During execution, the simulation must test the entire list of polygons to
determine which polygon is currently beneath each tire or contact surface,
to determine the elevation, slope and friction factor of the polygon.

To reduce the number of polygons tested by the calculation model (and thus
reduce processing time), HVE's 3-D Editor allows the user to define several
types of objects. The following object types are available:

- **Human** — Object type for all human polygons
- **Vehicle** — Object type for all vehicle polygons
- **Road** — Default object type for all environment polygons
- **Friction Zone** — User-assignable object type for environment polygons
- **Other** — User-assignable object type for environment polygons

*(updated: the current environment model also supports* Curb *and* Water
*polygon types — water polygons include water depth, depth method and water
friction multiplier attributes used by water-related tire models.)*

Polygons of type Human are tested only for human vs. vehicle/road/friction
zone interaction. Polygons of type Vehicle are tested only for
human/road/friction zone interaction. Polygons of type Other are not tested
or used by the calculation model.

> **NOTE:** It makes no sense to test the red lens of a traffic signal, or
> the sides of a 10-story building, for interaction with a vehicle's tires!

> **NOTE:** If you know an environment object will not be in contact with a
> simulated human or vehicle, be sure to define its type as *Other* to
> reduce processing time.

!!! note "HVE Studio"
    HVE Studio has no 3-D Editor, and its humans and vehicles are not part of
    the site geometry, so only the environment types apply. A surface's
    **Surface Type** — Road, Friction Zone, Curb, Water or Other — is set on
    its HVE Surface node in the Shader Editor. A surface an imported file
    declares no type for is shown and treated as Road. To take a surface out
    of the calculation, clear its **Drive** switch in
    View › Outliner; clearing its
    **Draw** switch only hides it. Standing water is a **Water Depth** (with
    **Wet Friction** and **Texture Depth**) on each surface's HVE Surface
    node, and on the Default material for ground with no surface of its own
    (see [Chapter 12](12-creating-editing-environments.md)).

#### How Surfaces Are Tested for Physical Contact

So far, this section seems pretty straightforward. Now, let's ask a few
questions:

- Suppose the vehicle is on an overpass. What prevents the calculation
  model from using the elevation of the surface beneath the overpass?
- Alternatively, suppose the vehicle is on an underpass. What prevents the
  calculation model from using the elevation of the road surface on the
  overpass? How about the underside of the overpass?
- Suppose the user has created an oil slick and placed it on the road
  surface. What prevents the calculation model from using the road, instead
  of the oil slick surface?

#### Get Surface Information

!!! note "HVE Studio"
    HVE's Get Surface Information dialog is the **Road Surface Search**
    section of the Event Information panel, set per event (see
    [Chapter 15](../06-event-editor/15-creating-editing-events.md)). Its
    choices are: *Default for this method* (track the previous polygon —
    HVE's own default for the simulation engines), *All triangles - first
    hit in file order* (From First Polygon), *Track the previous polygon*
    (From Previous Polygon) and *Track the previous polygon, friction zones
    first*. EDCRASH, EDGEN, EDHIS and GATB do not drive on the road surface,
    and the single-track model reads the road polygons directly, so the
    section does not apply to them.

To answer these and similar questions, a strict definition is required. HVE
uses two different methods to determine which polygon gets used:

- **Surface search** — Used by the Point Contact and Soft Soil
  Tire-Terrain Models (see the Event Set-up Wheels option; Chapter 4). This
  method searches in the direction of the earth-fixed gravity vector (i.e.,
  straight down) to determine the desired terrain polygon.
- **Terrain search** — Used by the Radial Spring and Sidewall Impact
  Tire-Terrain Models (again, see the Event Set-up Wheels option; Chapter
  4). This method searches in a programmatically defined direction (i.e.,
  in the direction of a tire radial or sidewall spring) to determine the
  desired terrain polygon.

HVE's Get Surface Information dialog has four search methods:

- Use First Polygon
- Use Previous Polygon
- Use Previous Polygon, Sorted *(updated: current default)*
- Use Elevation

The following rules are used by either the surface search or the terrain
search, according to the selected option:

**From First Polygon**

- *The first surface found beneath the specified X,Y coordinates is used.*
  The search ends when a surface is found. This rule reduces calculation
  time. By returning the results for the first surface, it is not necessary
  to read every polygon in the database and then decide which one to use.
- *Friction Zones are used first.* This is an important rule. It means
  there is a hierarchy: if two polygons exist, one just above the other,
  the first one found in the database will be used. To ensure that the oil
  slick is used instead of the surface beneath it (see third bullet,
  above), assign its type as a *Friction Zone*. To ensure the top surface
  of the overpass is used instead of the underside of the overpass or the
  road below the underpass (see first and second bullets, above), assign
  its type as a *Friction Zone*.

**From Previous Polygon**

- *The surface used during the previous timestep is tried first.* If the
  wheel is still on that surface, that surface is used. This method has the
  potential for working much faster, because the chances are good that the
  tire is still on the same surface.
- *Search in both directions.* If the tire is not on the surface used
  during the previous timestep, try the next polygon in the database, then
  try the previous polygon (rather than starting over with the first
  polygon). This also helps to increase calculation speed because polygon
  databases are typically organized such that surfaces lying physically
  adjacent to each other are also stored next to each other in the
  database.

**From Previous Polygon, Sorted** *(updated)*

- Works like From Previous Polygon, but the polygon database is first
  sorted so that physically adjacent polygons are stored adjacently,
  making the previous-polygon search still more effective. This is the
  default search method in the current version.

**By Elevation**

- *The surfaces are searched by elevation.* The highest surface still
  beneath the wheel center is used. This method is the most robust, but is
  very time-consuming because the entire polygon database must be searched
  at every timestep. *(updated: this option remains in the dialog for
  compatibility but is not supported by the current physics models; use one
  of the polygon-search methods instead.)*

The Get Surface Information dialog also allows the user to define the
allowable direction for surface normals on each terrain polygon (see Figure
13-1). The options are:

- **All Directions** — All terrain polygons are used by the tire model,
  regardless of the direction of the Z-component of the terrain surface
  normal.

> **NOTE:** Use this option if you wish to simulate a stunt driver
> performing a loop-de-loop!

- **Upward Facing Only** — Only terrain polygons with a positive
  Z-component are included by the tire model.
- **User-Defined** — The tire model uses a range for surface Z-components
  that is defined by the user.

If User-Defined is selected, the user may enter the allowable range for the
Z-component of the surface normal.

> **NOTE:** This method is often required for curb impact simulation in
> which the curb face is not exactly vertical due to rounding error. Try
> entering 0.001.

!!! warning "Not in HVE Studio"
    The *By Elevation* search and the surface-normal direction options (All
    Directions, Upward Facing Only, User-Defined) have no control in
    HVE Studio. A *From Previous Polygon, Sorted* choice is not offered as
    such; *Track the previous polygon, friction zones first* is the
    remaining polygon-tracking option.

#### Assigning the Object Type Attribute

In HVE, Object Type is an attribute assigned using the 3-D Editor. The
default type for all environment 3-D geometry is Road.

In HVE Studio, a surface's type is assigned as follows:

1. Click the **Environment (F4)** tab.
2. Click the surface in the Viewport, or select its row in **View ›
   Outliner**.
3. Click **Edit in Shader Editor**. The Shader Editor opens on the
   surface's material, with its **HVE Surface** node.
4. Choose the **Surface Type**.

By default, all environment surfaces will be used by the calculation model.
To ensure a particular surface is used by a calculation model, assign its
type as Friction Zone.

#### Importing 3-D Files from Other Modeling Programs

HVE can import a variety of 3-D formats used by other programs. The
imported geometry will be used by the current calculation model. Thus, the
surface elevation and normal for each polygon will be assigned according to
the rules defined earlier.

Because other modeling programs do not assign a friction factor or surface
type, default values (Friction Factor = 1.0, Type = Road) will be assigned
and used: in HVE Studio, every polygon with no material of its own uses the
**Default material**, whose Friction Multiplier is 1.0.

To load 3-D files from other modeling programs and edit the default surface
attributes, perform the following steps:

1. Click the **Environment (F4)** tab.
2. In the Environment panel's **Terrain** section, click **Browse...** next
   to *Geometry File* and choose the file (see Table 12-1 for the supported
   formats).
3. Set the **Scale Factor** and the axis check boxes, leave **Use surfaces
   as terrain (physics)** checked, and click **Import**. The site is
   displayed in the Viewport.
4. Click the desired surface in the Viewport (or its row in the **Surface
   Materials** list) to select it.
5. Click **Edit in Shader Editor**, and on the **HVE Surface** node choose
   the **Surface Type** — for example *Friction Zone* to increase its
   priority.
6. Edit the surface's **Friction Multiplier** and other contact properties.
7. To remove a surface from the list of physical surfaces, clear its
   **Drive** switch in **View › Outliner**.
8. Click the **Event (F5)** tab to execute an event using the new surface
   attributes.

Surface edits are stored with the case and re-applied each time the
geometry is re-imported from its file.

> **NOTE:** It is crucial when creating a 3-D environment using another
> editor to consider the way the individual objects will be treated when
> imported. This is especially important when creating object groups and
> surfaces.

> **NOTE:** While creating a 3-D environment, it is quite possible to
> (accidentally) create two surfaces sharing the same space. Although the
> visual appearance will be unaffected, the surface search may use the
> wrong surface. Be careful!

### Gravitational Constant

The gravitational constant defines the natural acceleration of objects
towards the center of the earth (in the direction of the earth-fixed
Z-axis). The value of the gravitational constant varies only slightly as a
function of earth-fixed coordinates. However, if the human or vehicle being
simulated may be taken to the moon or Mars, it is simple (and important) to
determine the effect of differences in the gravitational constant.

To edit the gravitational constant, perform the following steps:

1. Click the **Environment (F4)** tab.
2. In the Environment panel's **Physical** section, enter the desired
   **Gravity** (see Table 13-2 for selected gravitational constants). It is
   shown in in/s² or m/s², following the units set in Tools › Preferences.

The entered value is assigned to the current environment. The default is
9.80665 m/s² (386.09 in/s²).

> **NOTE:** Because all inertial objects are stored according to mass, the
> correct weight will be displayed in the Human or Vehicle Editor. During
> Event mode, the correct inertial properties of the object will be used for
> the current environment.

**Table 13-2: Gravitational Constants for Selected Environments**

| Location | Gravitational Constant (in/sec²) |
|---|---|
| Earth — Common Range | 386.08 – 386.4 |
| Earth — At Equator | 385.06 |
| Earth — London (51°32') | 386.29 |
| Earth — Poles (90°) | 387.09 |
| Moon | 64.4 |
| Mars | 146.8 |
| Jupiter | 1024.0 |

## Atmospheric Model

### Physical Characteristics

The physical characteristics of the atmosphere include the following
parameters:

- Temperature
- Barometric Pressure
- Wind Velocity and Direction

These parameters may be used to determine the aerodynamic drag force on an
object by calculating the current level of dynamic pressure.

#### Air Density

Air density, δ, is calculated using the current temperature and pressure
according to the following formula:

    δ = p / (R·T)

where

| Symbol | Meaning |
|---|---|
| δ | Air Density, lb/in³ |
| p | Atmospheric Pressure, lb/in² |
| R | Gas Constant, 639.6 in-lb/lb-°R |
| T | Absolute Temperature, °R (°F + 460) |

#### Dynamic Pressure and Force

Given the current air density and wind velocity, the force, F<sub>air</sub>,
acting on a vehicle (or any object) due to aerodynamic pressure is as
follows:

    F_air = (c_a · δ · A · V_a²) / (2·g)

where

| Symbol | Meaning |
|---|---|
| F<sub>air</sub> | Air Resistance Force, lb |
| c<sub>a</sub> | Air Drag Coefficient, dimensionless |
| δ | Air Density, lb/in³ |
| A | Projected Area, in² |
| V<sub>a</sub> | Wind Velocity relative to vehicle, in/sec |
| g | Gravitational Constant, in/sec² |

> **NOTE:** The aerodynamic drag coefficient and projected area are vehicle
> parameters. Refer to Chapter 11, Vehicle Model Definition, for further
> details.

!!! note "HVE Studio"
    The temperature, pressure, wind speed and wind direction are entered in
    the Environment panel's **Physical** section. The **Air Density** there
    is not entered: it is shown as the engines compute it from the ambient
    temperature and pressure with the formula above. The wind direction is
    the direction the wind blows *from*.

### Visibility

The visual characteristics of the atmosphere include the following
parameters:

- Fog Type
- Maximum Sight Distance (graph of attenuation vs. distance)
- Sky and Fog Color

!!! warning "Not in HVE Studio"
    HVE Studio does not model visibility. Fog Type and Maximum Sight Distance
    have no control, and a value imported from an HVE case is only kept with
    the case. The viewport's **Distance Haze** (View › Scene Display ›
    Effects) fades far geometry toward the sky's horizon colour by the
    **Haze** of the World material's Sky Texture node (nothing while Haze is
    0, with no World material, or with Scene Lighting off); it is a picture,
    not a visibility distance. The rest of this
    section describes HVE's model. The sky's colour is part of the world
    material in the Shader Editor
    ([Materials and the Shader Editor](../../new-features/01-materials-and-shader-editor.md)).

#### Fog Type

HVE provides three types of atmospheric effects that limit visibility:

- **Fog** — The percentage of vision attenuation increases as a linear
  function of distance from the camera (see Figure 13-6).
- **Haze** — The percentage of vision attenuation increases as a quadratic
  function of distance from the camera (see Figure 13-6).
- **Smoke** — The percentage of vision attenuation increases as a cubic
  function of distance from the camera (see Figure 13-6).

*(Note: the legacy edition's text transposed the quadratic/cubic
assignments between its Chapter 12 and Chapter 13 discussions; the ordering
above — Fog linear, Haze quadratic, Smoke cubic — matches the Chapter 12
description and the rendering behavior.)*

These atmospheric effects determine how sight distance is attenuated.
Visual attenuation is determined algorithmically.

![Figure 13-6](../images/p472-figB13-6.png)
*Figure 13-6: Visibility vs. Distance for Fog, Smoke and Haze.*

#### Maximum Sight Distance

Maximum Sight Distance is used in the fog calculations to determine the
distance at which vision is 100 percent attenuated. In HVE, the Maximum
Sight Distance is entered using the Sky Attributes dialog.

#### Sky and Fog Color

Sky and Fog Color are used to create a visually accurate representation of
the environment. The assessment of color is qualitative, and is not subject
to objective calculations. In HVE, the Sky and Fog Color are entered using
the Sky Attributes dialog.

## Sun Position

The location of the sun is used to assign directional lighting to the
environment. The sun is also displayed as a sphere at the correct
astronomical location.

!!! note "HVE Studio"
    In HVE Studio the sun lights the scene and casts its shadows; it is not
    drawn as a sphere. It is placed from the location and time when **From
    location and time** is chosen on the Shader Editor's **Sun & Sky**
    panel, with either HVE's own method or the NOAA method, and can instead
    be set by hand (see [Chapter 12](12-creating-editing-environments.md)).
    Two conventions differ from the list below: HVE Studio enters latitude
    and longitude in **decimal degrees with east longitude positive** (a
    west longitude is negative), and offers a **Daylight saving** check box
    (leave it off to enter local standard time, as HVE requires). The
    hours-from-GMT value is the **UTC offset** (local time = UTC + offset),
    and HVE's Angle of X-Axis is **North**.

The following parameters are used to assign the sun position:

- **Latitude** — The angular distance from the equator, expressed in
  degrees, minutes and seconds north (+ or N) or south (- or S) from the
  equator.
- **Longitude** — The angular distance from the prime meridian, expressed
  in degrees, minutes and seconds west (+ or W) or east (- or E) from the
  prime meridian.
- **Hours from GMT** — The time, expressed in hours, from the prime
  meridian.

> **NOTE:** GMT stands for Greenwich Mean Time — the difference, in integer
> hours, from the time at Greenwich, England, to the local time zone. GMT
> for nearly any global location may be found in most world atlases and
> travel references.

- **Date** — The date of the event (month, day, year).
- **Time** — The time of the event (24-hour clock; e.g., 10:15 PM is 2215).

> **NOTE:** Daylight saving time is not considered! If an event occurred
> during daylight saving time, you need to subtract one hour from the stated
> time.

### Sun Azimuth and Zenith

Given the data above, HVE calculates the location of the sun in the current
environment. The sun location is used for determining the location of the
solar light source, resulting in the correct shading of objects, as well as
for displaying the sun in the environment. Figure 13-7 illustrates the sun
position calculations.

![Figure 13-7](../images/p474-figB13-7.png)
*Figure 13-7: Sun Azimuth and Zenith calculations.*

> **NOTE:** By displaying the sun, you might stumble onto the notion that a
> driver was looking into the sun at the time of an accident.

### Environment Location Database

The HVE Environment Editor includes a user-extendible database of
environment locations, stored according to the Location Name, Latitude,
Longitude and GMT.

!!! warning "Not in HVE Studio"
    HVE Studio has no location database. The Environment panel's Location
    section instead takes a pasted coordinate or map link, or looks an
    address up online (OpenStreetMap, with the time zone from timeapi.io);
    see [Chapter 12](12-creating-editing-environments.md).

**Table 13-3: Environment Model Parameters**

In HVE Studio, the Location fields are in the Environment panel's
**Location** section; GMT (**UTC offset**) and Angle of X-Axis (**North**)
are on the Shader Editor's **Sun & Sky** panel; the remaining parameters
are in the Environment panel's **Physical** section.

| Parameter | Unit Name | Description |
|---|---|---|
| Current Location | 30-character text string | City, State (or Province), Country (Location Database) |
| Latitude | UtEnvDispAngle | Latitude for the current location. The user-specified value is stored in the location database for future use. |
| Longitude | UtEnvDispAngle | Longitude for the current location. The user-specified value is stored in the location database for future use. |
| GMT | UtTime | The number of hours from Greenwich, England, to the specified location (conventionally +/- 24 hours; west of Greenwich is negative) |
| Environment Name | 30-character text string | User-entered name for the current environment |
| Date of Crash | Text string | Entered value is parsed according to month/day/year (or day/month/year, per the user's date-style preference) to determine the date relative to the solar calendar. |
| Time of Crash | Text string | Entered value is parsed according to a 24-hour clock (i.e., 2230 is 10:30 PM) to determine the time relative to midnight (standard time is used; daylight saving time is not considered). |
| Angle of X-Axis | UtEnvDispAngle | Angle of the user-specified earth-fixed X-axis relative to true north. The user must make any adjustments from magnetic north if a compass was used to identify direction. |
| Wind Speed | UtEnvVelLinear | Wind velocity |
| Wind Direction | UtEnvDispAngle | Wind direction relative to true north. The user must make any adjustments from magnetic north if a compass was used to identify direction. |
| Barometric Pressure | UtEnvPressure | Ambient barometric pressure |
| Temperature | UtEnvTemp | Ambient temperature |
| Gravitational Constant | UtEnvAccelLinear | Local gravitational constant |

---

*See also (dialog references):*
[Environment Information Dialog](../../08-environment/EnvtInfoDlg.md) ·
[Environment Material Properties](../../08-environment/EnvrMatPropDlg.md) ·
[Linear Friction Zone Properties](../../08-environment/LinFriPropDlg.md) ·
[Surface Editor](../../08-environment/SurfEdDlg.md)

<!-- NAV -->

---

← Previous: [Chapter 12 — Creating & Editing Environments](12-creating-editing-environments.md)  |  [Index](README.md)

<!-- /NAV -->
