# Chapter 2 — EDCRASH Program Input

This chapter defines the objects (vehicles and environment) and the event set-up parameters (positions, damage profiles, wheel lock-ups, and so forth) used by the EDCRASH analysis. In general, the chapter is divided into the following sections:

- **Objects** — The number of vehicles, and the specific vehicle parameters actually used by EDCRASH.
- **Events** — The various options available for setting up and executing an EDCRASH event.

## Objects Overview

The objects used by the EDCRASH model are:

- **Vehicles** — One or two vehicles may be studied by EDCRASH.
- **Environment** — Like the real world, EDCRASH has exactly one environment.

> **NOTE:** The environment is used in any reconstruction or simulation model.

The following sections describe how the vehicle and environment provide the required inputs to the EDCRASH calculation model.

## Vehicles

EDCRASH uses one or two vehicles created using the Vehicle Editor. Vehicles are selected from the Vehicle Database by choosing the following attributes:

- **Type** — EDCRASH supports the following vehicle types: Passenger Car, Pickup, Van, Sport-Utility, Truck, Movable Barrier and Fixed Barrier.
- **Make** — EDCRASH supports all available vehicle makes.
- **Model** — EDCRASH supports all available vehicle models, within the limits defined by number of axles and drive axles; see below.
- **Year** — EDCRASH supports all available vehicle years.
- **Body Style** — EDCRASH supports all available vehicle body styles.

Each vehicle also has the following additional user-editable parameters:

- **Driver Location** — The Driver Location is not used by EDCRASH. *(In HVE, Driver Location must not be None, or the Wheel Data is unavailable in Event mode. HVE Studio offers the Wheel Data page for every vehicle in an EDCRASH event.)*
- **Engine Location** — The Engine Location is not used by EDCRASH.
- **Number of Axles** — EDCRASH supports only 2-axled vehicles.
- **Drive Axle(s)** — The Drive Axle is not used by EDCRASH.

To add a vehicle to the current case in HVE Studio:

1. Choose the **Vehicle** editor tab (F3).
2. In the **Vehicles** panel, click **Add...**. The **Add Vehicle** dialog lets you search the loaded vehicle databases or pick one of HVE's generic vehicles by type and class.
3. Choose the vehicle and add it. The new vehicle is added to the case and selected; it is not put in any event (add it to the event under **Vehicles in Event**, below).
4. If desired, edit its name and attributes (type, number of axles, driver and engine location, drive axles) in the **Identity** and **Configuration** sections of the Vehicles panel. The name does not affect calculations.

![Figure 2-1](images/hvn-vehicle-editor.png)

*Figure 2-1: The Vehicle editor in HVE Studio (EDCRASH Tutorial case).*

The following Vehicle Parameter groups are assigned in the Vehicle editor:

- Sprung Mass
  - Inertias
  - Move CG
- Unsprung Mass
  - Wheel Location
  - Tire Data
  - Suspension Data
  - Brake Data
- Steering System
- Exterior
  - Overall Dimensions
  - Crush Stiffness Coefficients

The specific data used in each of the above parameter groups are defined in Tables 2-1 through 2-3.

### Sprung Mass

**Table 2-1: Vehicle Sprung Mass Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| Total Weight | Total vehicle weight |
| Total Yaw Inertia | Total rotational inertia about the vehicle-fixed z axis |
| Move CG x | Relocates the CG in the vehicle-fixed x direction. This entry causes an automatic adjustment of all other vehicle dimensions to reflect the new CG location. |

#### Inertias

EDCRASH uses the total vehicle weight (converted to mass according to the current gravitational constant; see Environment), and the total yaw rotational inertia.

Because EDCRASH does not have separate degrees of freedom for the unsprung masses, the yaw moment of inertia used by EDCRASH is the sum of the sprung mass yaw inertia plus the additional yaw inertia created by the individual wheels. See also EDCRASH Output, Vehicle Data report.

#### Move CG

Move CG is not directly used by EDCRASH. Its current value does not show up in the results. However, the Move CG fields may be used to quickly move the vehicle's center of gravity. The x,y,z coordinates for the wheels are updated to reflect the new CG location.

> **NOTE:** Bilateral symmetry is assumed. Moving the CG in the +y or −y direction will have no effect on the EDCRASH calculations.

#### Geometry File

The Geometry File is not used by EDCRASH.

### Unsprung Mass

**Table 2-2: Vehicle Unsprung Mass Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| Wheel Location | The vehicle-fixed x,y,z wheel center coordinates |
| Tire Slide Friction | The slide coefficient of friction for each tire |
| Tire Friction Table, Test Load/Speed | The load and speed for a given set of friction results (EDCRASH uses the middle load and middle speed) |
| Friction In-use Factor | Multiplier for Slide Friction |
| Tire Cornering Stiffness | Tire lateral force per unit of tire lateral slip for small amounts of slip |
| Cornering Stiffness In-use Factor | Multiplier for Cornering Stiffness |

#### Wheel Location

Although HVE-2D provides values for the vehicle-fixed x,y,z coordinates of each wheel, EDCRASH uses the following parameters: $a$, the distance from the CG to the front axle; $b$, the distance from the CG to the rear axle; and $t_w$, the average of the front and rear track widths.

> **NOTE:** EDCRASH uses the average $x_{wheel}$ for the front wheels to calculate $a$ and the average $x_{wheel}$ for the rear wheels to calculate $b$. Similarly, EDCRASH uses the total distance between right-side and left-side tires to calculate track width. Bilateral symmetry is assumed. Finally, EDCRASH does not use $z_{wheel}$ for calculations.

#### Tire

The tire parameters provide the following data groups:

- Physical Data
- Friction Table
- Cornering Stiffness Table
- Slip-vs-Rolloff Table

EDCRASH's use of these parameters is described below.

#### Physical Data

EDCRASH does not use the Tire Physical Data.

#### Friction Data

The Friction Data used by EDCRASH are shown in Table 2-2. EDCRASH uses the slide friction coefficient.

Because EDCRASH's tire model does not include a load or speed dependence, if friction data for more than one load or speed is supplied in the HVE Tire Data dialog, EDCRASH uses the friction coefficient for the middle load and/or speed.

> **NOTE:** If there is any doubt about which value is actually used by EDCRASH, you can check the Vehicle Data output report.

The In-use Factor, available in HVE, is a convenient way to reduce or increase the dependent friction value for a specific case.

#### Cornering Stiffness Data

If (and only if) the Trajectory Simulation option is selected, EDCRASH uses the Cornering Stiffness value.

Like the Friction Table, EDCRASH's tire model does not include a load or speed dependence. If more than one load or speed is supplied in the HVE Tire Data dialog, EDCRASH uses the cornering stiffness for the middle load and/or speed.

> **NOTE:** If there is any doubt about which value is actually used by EDCRASH, you can check the Vehicle Data output report.

The In-use Factor is a convenient way to reduce or increase the cornering stiffness.

> **NOTE:** If you are simulating a vehicle with a flat tire, you'll probably want to reduce the In-use Factor to about 0.1.

#### Slip-vs-Rolloff Table

EDCRASH does not use the Tire Slip-Rolloff data.

#### Suspension

EDCRASH does not use the Suspension data.

#### Brake

EDCRASH does not use the Brake data.

### Exterior

EDCRASH uses the following Vehicle Exterior Data:

- Exterior Dimensions
- A and B Stiffness Coefficients

!!! note "HVE Studio"
    In HVE Studio EDCRASH takes the A and B stiffness coefficients from the
    **event** (Event Information, Vehicle Impact Setup — see Damage Profile
    below), not from the vehicle. The per-side A and B values of the
    vehicle (Vehicle › Editors › Crush Stiffness... and the **Crush & Geometry** dialog,
    Event › Crush Profile...) are used by the simulation programs, not by
    EDCRASH. A case opened from HVE carries the stiffness HVE stored in
    the event.

**Table 2-3: Vehicle Exterior Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| CG to Front, Right, Back and Left | The vehicle's exterior dimensions |
| A Stiffness Coefficient | The force per unit width required to initiate permanent deformation |
| B Stiffness Coefficient | The vehicle crush rate, that is, the force per unit of permanent crush depth per unit of damage width |

### Steering System Data

EDCRASH does not use the Steering System data.

### Brake System Data

EDCRASH does not use the Brake System data.

## Environment

EDCRASH uses the case's environment. The environment is created by defining the following groups of attributes:

- Visual Data
- Physical Data

### Creating an Environment

In HVE Studio every case has exactly one environment, so there is nothing to add. To edit it:

1. Choose the **Environment** editor tab (F4).
2. Choose **Environment › Environment...**. The Environment dialog is displayed.
3. Enter the name, date, time, latitude and longitude of the site. (The location can also be set from a pasted coordinate or an address search.)
4. Under **Scene Geometry**, choose the site file with **Browse...** and **Import** it (DXF, `.h3d`, `.iv`, `.wrl`, OBJ or glTF). A case opened from HVE brings its own site with it.
5. Enter the wind and the atmosphere, including the gravity constant, in the **Ambient** and **Atmosphere** sections.
6. The angle of the earth-fixed X axis from true north is the **North** setting of the sun and sky, opened with **Edit the sun and sky...**.

See [Environment Information](../../08-environment/EnvtInfoDlg.md) for the dialog.

### Visual Data

The following visual parameters may be edited:

- **Environment Location** — A database containing the name (City/State/Country), Latitude and Longitude and GMT for the selected location.
- **Time and Date** — The local standard time and date for the event.

The visual data are not used by the event; they are provided for studies related to visibility at the time of an event (e.g., avoidability of an accident).

> **NOTE:** The visual data (Location, Time, Date and Angle of earth-fixed X axis) affect the lighting of the event! Depending on your view the scene may be shaded and difficult to see. If the time is after sundown, the view will be dark.

### Physical Data

The Physical Data groups are:

- Angle of X Axis
- Wind Speed and Direction
- Atmospheric Temperature and Pressure
- Gravity Constant
- Surface Geometry

**Table 2-4: Environment Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| Gravitational Constant | The local acceleration of gravity |
| 3-D Surface Geometry (Friction Factor, Elevation, Slope) | The polygon database used to create the 3-D environment |

#### Angle of X Axis

The angle of the X axis is used to position the earth-fixed coordinate system on the surface of the earth.

> **NOTE:** The angle is specified relative to true north. If you are using a compass to determine direction at the scene of an accident, you should provide a correction factor before entering this angle.

> **NOTE:** The angle of the X axis affects how you visualize an EDCRASH event because it affects the location of the sun.

#### Wind Speed and Direction

EDCRASH does not use the Wind Speed and Direction.

#### Atmospheric Temperature and Pressure

EDCRASH does not use the atmospheric temperature and pressure.

#### Gravitational Constant

The gravitational constant converts mass to force. An object's mass and rotational inertias are properties that are the same throughout the universe; however, the weight of an object is dependent on the local gravitational constant.

#### Surface Geometry

If the Trajectory Simulation option is used, EDCRASH uses the geometry to calculate the friction multiplier for the current X,Y position of each tire during the simulation.

In HVE, it is also used to calculate the elevation and slope.

> **NOTE:** Geometry is used only if a trajectory simulation is requested. The traditional, energy-based analysis does not use the surface geometry.

## Event

An EDCRASH event is created, set up and executed in the **Event** editor (F5). Each of these topics is described below.

![Figure 2-3](images/hvn-edcrash-event-information.png)

*Figure 2-3: The Event Information panel for an EDCRASH event (EDCRASH Tutorial case). Units follow Tools › Preferences; this capture is in Imperial units.*

### Creating an Event

An EDCRASH event is created in the **Event Information** panel.

To create an EDCRASH event:

1. Choose the **Event** editor tab (F5). The Event Information panel is displayed.
2. Under **Events**, click **+** to add an event. It becomes the active event.
3. Under **Calculation Method**, choose **EDCRASH** in the **Method** list.
4. Under **Vehicles in Event**, click **Add Vehicle** to add one or two vehicles. EDCRASH takes at most two.
5. Under **Event**, enter a name. The name does not affect calculations.

   > **NOTE:** If the vehicles are not compatible with EDCRASH, the method is marked "N/A for these vehicles" in the Method list and the panel states the reason ("Cannot run: ..."). Unlike HVE, HVE Studio lets you keep the method selected while you fix the vehicles; the event will not run until they are compatible.

### Setting Up an EDCRASH Event

EDCRASH uses the following event set-up options:

- Position/Velocity
- Driver Controls
- Damage Profiles

**Table 2-5: Event Set-up Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| Vehicle Position: Begin Braking, Impact, Separation, Point-on-curve, End-of-rotation, Final/Rest | The earth-fixed X,Y coordinates and heading angles of each vehicle for each of the selected positions |
| Driver Controls, Wheel Data | Pre-impact Drag Factor, Rotation/Lateral Skidding Flag, % Wheel Lock-up, Steer Angle\* |
| Damage Profile | CDC, PDOF, x,y Impulse Coordinates, Damage Width, up to 10 crush depths, damage Midpoint Offset, A and B Stiffness Coefficients for each crush zone |

\* Steer Angle applies only if the Trajectory Simulation option was selected.

#### Position/Velocity

Each vehicle is positioned relative to the earth-fixed coordinate system by supplying the X,Y,Z coordinates of its CG, and roll ($\phi$), pitch ($\theta$) and yaw ($\psi$) angles about the vehicle x, y and z axes, respectively (Table 2-5).

!!! note "HVE Studio"
    For an EDCRASH event the scene positions are entered in the **Event
    Information** panel, **Vehicle Impact Setup** section, for each vehicle
    (Event › Position / Velocity is not used by EDCRASH and is greyed):

    - Tick **Scene positions known (impact + rest)** and enter **Impact X**,
      **Impact Y**, **Impact heading**, **Rest X**, **Rest Y** and **Rest
      heading**. The impact position can also be dragged in the viewport
      (G to move, R to rotate). With the box unticked the event is a
      damage-only reconstruction: delta-V from the crush alone, no impact
      speed.
    - Open **Scene positions** to see all eight of HVE's named positions.
      Impact and Rest are listed there read-only (they are edited in the
      fields above); tick any other position to enter its X, Y and heading.
      Every position that is set is outlined in the viewport (View › Scene
      Display › Scene Ghosts).
    - X and Y are in the length unit set in Tools › Preferences; headings
      are in degrees.

![Scene positions in HVE Studio](images/hvn-edcrash-scene-positions.png)

*The Ford Escort's scene positions in the EDCRASH Tutorial case: Begin Braking is ticked and entered here; Impact and Final/Rest are shown read-only and entered in the fields below.*

> **NOTE:** In EDCRASH, +230 degrees is not the same as −130 degrees because the relative magnitude between two angles implies the rotation direction! For example, if the impact heading angle is 180 degrees and the rest heading angle is 230 degrees, the change in heading angle between impact and rest is +50 degrees clockwise; if the rest heading angle is −130 degrees, the change in heading angle is −310 degrees and the direction of rotation is counter-clockwise. Refer to the HVE or HVE-2D User's Manual for more information.

> **NOTE:** In HVE-2D, Z is equal to the CG height above ground, and roll and pitch are equal to 0.0.

> **NOTE:** In HVE, Z, roll and pitch are supplied automatically using AutoPosition.

EDCRASH uses the following positions:

- **Begin Braking** — The X,Y coordinates and heading angle of the vehicle when the brakes are applied before impact. With it, EDCRASH back-calculates the speed at the start of braking from the impact speed, the distance from Begin Braking to Impact and the pre-impact lock-up (Driver Controls, below).
- **Impact** — The X,Y coordinates and heading angle of the vehicle at impact.

  > **NOTE:** The positions of two vehicles at impact should overlap such that they share the same impulse center.

- **Separation** — The X,Y coordinates and heading angle of the vehicle at separation. If it is not entered, EDCRASH assumes separation at the impact position and heading.
- **Point-on-curve (POC)** — The X,Y coordinate on a curved path between impact and end-of-rotation or rest. With it, the post-impact path becomes a curve through this point instead of a straight line (see Curved Path, under Calculation Options).

  > **NOTE:** Only the X,Y coordinate is required; the heading angle is not used.

- **End-of-rotation (EOR)** — The X,Y coordinate and heading angle that specify where the vehicle's motion changed from rotating/lateral skidding to pure rollout. With it, the spinout ends at the EOR and the EOR-to-rest distance is analyzed as a separate rollout.
- **Final/Rest** — The X,Y coordinates and heading angle of the vehicle at its rest position. In HVE a velocity may also be entered; this value is used as the final velocity at the end of the path.

Positions are not required. However, if an estimate of impact speed is desired, Impact and Rest positions must be supplied. Begin Braking, Separation, End-of-rotation and Point-on-curve positions are optional.

!!! note "HVE Studio"
    HVE's other two named positions, **Initial** and **Begin Perception**,
    can be set and are drawn in the viewport, but EDCRASH does not use them.
    Point on Curve and End of Rotation interact: the curved path runs to
    the end of the path, which is the rest position unless an End of
    Rotation is entered.

!!! note "HVE Studio"
    - **Impact sideslip** and **Velocity at rest** are fields under the
      impact and rest positions in the Event Information panel (shown when
      *Scene positions known* is ticked). Both are read from an HVE case.
      The sideslip is the angle from where the vehicle points to where it is
      travelling at impact (0 = straight ahead); it moves both vehicles'
      Delta-V and PDOF. The velocity at rest is the speed EDCRASH's spinout
      and rollout analysis runs down to (0 = the vehicle stopped).
    - **Impact Speed field.** The *Impact Speed* shown for each vehicle in
      Vehicle Impact Setup is not an EDCRASH input. EDCRASH calculates the
      impact speed.

#### Driver Controls

EDCRASH uses the Driver Controls, Wheel Data option. In HVE Studio choose **Event › Driver Controls...**; for an EDCRASH event the dialog has a single **Wheel Data** tab, with the vehicle chosen in the **Vehicle** list at the top. It allows the user to enter the following parameters:

![Wheel Data in HVE Studio](images/hvn-edcrash-wheel-data.png)

*Wheel Data page in HVE Studio (Ford Escort, EDCRASH Tutorial case). Lock-ups are entered as fractions (%/100); the right wheel of each axle is listed first.*

**Pre-impact Wheel Lock-up** — The total combined wheel lock-up (percent of available friction used by all wheels) by the vehicle during its travel from the user-entered Begin Braking position to the Impact position. *(HVE Studio: the **Total Lock-up** field under Pre-Impact. It is used whenever a Begin Braking position is set, and the Accident History then reports a Begin Braking velocity; the note under the field says whether this vehicle has one.)*

Typical values for non-braking rolling resistance for passenger car tires are provided for reference in Table 2-6 [11]. These values should be entered in the Driver Controls – Brakes dialog using the Percent Available Friction option. Representative values for locked-wheel (slide) friction coefficients for passenger car tires on a variety of surfaces are also provided, in Table 2-7 [10]. While the table is very complete, EDC makes no claim as to the accuracy of the data. The user is urged to perform thorough research in order to supply EDCRASH with the best possible data.

**Rot/Lat Skidding** — A checkbox (**Rot / Lat Skidding** in HVE Studio). Choose this option if the vehicle's sideslip angle was changing during the post-impact phase. *(When Auto-set Rot/Lat Skidding is on in the Calculation Options — the default — EDCRASH sets this flag itself and the value entered here is overridden.)*

> **NOTE:** If Rot/Lat Skidding is selected, EDCRASH uses the modified Marquard analysis to account for vehicle spinning.

**% Lock-up** — The percent of available longitudinal friction used by each tire. The entered value is assumed constant during the entire post-impact phase.

> **NOTE:** Enter only the longitudinal component! If the vehicle is sliding laterally, EDCRASH will determine that condition and account for it. If you also account for the lateral sliding, it will be accounted for twice!

**Steer Angles** — The constant steer angle at each tire. *(Used only on the Trajectory Simulation separation-velocity basis.)*

**Table 2-6: Rolling Resistance Braking Inputs for Pavement [11]**

| Tire/Wheel Condition | % Available Friction |
|---|---|
| Normal Inflation | $0.010/\mu$ |
| Partial Inflation | $0.013/\mu$ |
| Damaged | 0.0 to 1.0 |
| Engine Braking — High Gear | $0.150/\mu$ to $0.200/\mu$ |
| Engine Braking — Low Gear | $0.200/\mu$ to $0.400/\mu$ |

**Table 2-7: Tire-Ground Friction Coefficients on Various Surfaces [10]**

| Surface | Dry <30 mph | Dry >30 mph | Wet <30 mph | Wet >30 mph |
|---|---|---|---|---|
| **Portland Cement** | | | | |
| — New, Sharp | 0.80–1.20 | 0.70–1.00 | 0.50–0.80 | 0.40–0.75 |
| — Traveled | 0.60–0.80 | 0.60–0.75 | 0.45–0.70 | 0.45–0.65 |
| — Polished | 0.55–0.75 | 0.50–0.65 | 0.45–0.65 | 0.45–0.60 |
| **Asphalt or Tar** | | | | |
| — New, Sharp | 0.80–1.20 | 0.65–1.00 | 0.50–0.80 | 0.45–0.75 |
| — Traveled | 0.60–0.80 | 0.55–0.70 | 0.50–0.80 | 0.45–0.75 |
| — Polished | 0.55–0.75 | 0.45–0.65 | 0.45–0.65 | 0.40–0.60 |
| — Excess Tar | 0.50–0.60 | 0.35–0.60 | 0.30–0.60 | 0.25–0.55 |
| **Gravel** | | | | |
| — Packed, Oiled | 0.55–0.85 | 0.50–0.80 | 0.40–0.80 | 0.40–0.60 |
| — Loose | 0.40–0.70 | 0.40–0.70 | 0.45–0.75 | 0.45–0.75 |
| **Cinders** | | | | |
| — Packed | 0.50–0.70 | 0.50–0.70 | 0.65–0.75 | 0.65–0.75 |
| **Rock** | | | | |
| — Crushed | 0.55–0.75 | 0.55–0.75 | 0.55–0.75 | 0.55–0.75 |
| **Ice** | | | | |
| — Smooth | 0.10–0.25 | 0.07–0.20 | 0.05–0.10 | 0.05–0.10 |
| **Snow** | | | | |
| — Packed | 0.30–0.55 | 0.35–0.55 | 0.30–0.60 | 0.30–0.60 |
| — Loose | 0.10–0.25 | 0.10–0.20 | 0.30–0.60 | 0.30–0.60 |

#### Damage Profile

EDCRASH uses the CDC to assign an initial damage profile (Damage Width, Crush Depths, Midpoint Offset). The Collision Deformation Classification (CDC) is a seven-character code which describes the vehicle damage. The characters in the CDC identify the Principal Direction of Force (PDOF) in clock direction, the impacted surface (front, right, back, or left), the shape of the damage profile, and the extent of maximum penetration. If a more accurate direction than the clock direction is known, the PDOF may be entered in degrees after the CDC. Detailed explanations of the parameters making up the CDC definitions are found in the HVE-2D User's Manual, Appendix V.

![Figure 2-4](images/p039-004.png)

*Figure 2-4: Definition of each column within the seven-character CDC code.*

After entering the CDC, the damage profile may be edited by over-riding the default width, crush depths and damage offset. In addition, up to 10 crush depths may be entered, and up to 9 sets of A and B stiffness coefficients may be supplied. To delete the damage profile, enter *None* in the CDC field.

> **NOTE:** The Damage Profile dialog displays barrier results (Delta-V, damage energy and force) for the current vehicle. Please note these results do not apply to a 2-vehicle collision!

**Use Newton's 3rd Law** — Clicking on this checkbox causes EDCRASH to calculate the PDOF for the selected vehicle based on the vehicles' impact heading angles and the PDOF for the other vehicle. This is a convenient way to assign the PDOF for one vehicle.

> **NOTE:** You cannot use this checkbox for both vehicles.

!!! note "HVE Studio"
    The damage profile is entered in the **Event Information** panel,
    **Vehicle Impact Setup** section, under each vehicle's name. **Event › Damage
    Profiles...** (Ctrl+M) opens that section, as HVE's menu item opens its
    dialog. (The vehicle's per-side crush stiffness, which EDCRASH does not
    use, is Vehicle › Editors › Crush Stiffness....)

    - **CDC** — the seven-character code. If no usable crush profile is
      entered, EDCRASH derives the default width, offset and depths from it,
      as in HVE. HVE Studio replaces a CDC that is not a valid seven-character
      code with `12FDEW4` and says so in the run status.
    - **PDOF (deg)**.
    - **Auto-calculate PDOF (from the other vehicle)** — HVE's *Use
      Newton's 3rd Law*. While it is ticked the PDOF field is ignored. If it
      is ticked for both vehicles EDCRASH refuses the event; a barrier always
      has its PDOF calculated, so the other vehicle must not use it.
    - **A Stiffness** and **B Stiffness** — applied to every crush zone
      that has no zone value of its own (shown in lbf/in and lbf/in² in
      Imperial units, N/m and N/m² in Metric).
    - **Derive impulse center from damage profile** — on, EDCRASH computes
      the impulse center from the profile (the default). Off, enter
      **Impulse Center X** and **Y**.
    - **Measured Crush (drives Delta-V)** — **# crush depths** (2 to 10),
      the depths **C1**, **C2**, ..., **Damage width** and **Damage
      offset**, and **Per-zone A/B** with one A and B per zone (zones =
      depths − 1) and an **All same as zone 1** button. Depths are spaced
      evenly across the width. **Measure from a scan...** opens *Crush
      Profile from Scan* for this vehicle (below), which fills the depths,
      width and offset from a scan of the damaged vehicle.

    HVE Studio does not display barrier results while you enter the profile;
    the damage energy and force appear in Key Results and the Damage Data
    report after the run.

    The **Basis** radio buttons (EES or Damage Profile) are shown read-only:
    EDCRASH always reconstructs from the crush profile and no part of it
    reads the basis or the EES speed, in HVE either.

![Damage profile in HVE Studio](images/hvn-edcrash-damage-escort.png)

*Vehicle Impact Setup for the Ford Escort in the EDCRASH Tutorial case, with Measured Crush open.*

#### Crush Profile from Scan

*(New in HVE Studio.)* **Measure from a scan...** under Measured Crush, or
**Tools › Automatic Tools › Crush Profile from Scan...**, measures the crush
profile off a scan of the damaged vehicle (LAS, PLY, E57 or a text point file)
instead of a tape.

- **Vehicle** (the vehicle picker at the top of the window, offering the
  active event's vehicles; picking one selects it everywhere, and **Measure
  from a scan...** opens the window on its own vehicle) and **Damaged face**:
  the event vehicle the profile is written to, and the face, which comes from
  the CDC's third character (F, B, R, L) unless you choose one. EDCRASH takes the face from the CDC, so a different
  choice is warned about.
- **The damaged vehicle's scan**: the file, read like a scanned vehicle body:
  x forward, y to the LEFT, z up, with the vehicle's CG at the origin. The
  placement starts from the case vehicle's own body placement; **Scale
  Factor**, **Center on CG**, **CG in the scan** and **Turn about vertical**
  move it. The line under it gives the scan's size and how far its front is
  ahead of the CG, to check against the vehicle.
- **Undamaged reference**: what the face would have been without damage.
  **The vehicle's own 3-D body** uses the body the case vehicle collides with
  (its mesh, or its generic body when it has none -- the window says which; a
  generic body is the vehicle's size, not its shape). The scan must be placed
  on the same CG. **Exemplar scan** reads an undamaged vehicle of the same model the same way,
  so a curved bumper's bow is not counted as crush. **String line** draws a
  straight line across the face's two undamaged ends, as a tape line does in
  the field; on a bowed bumper it lies behind the centre and misses the bow's
  depth. **Plane** uses the vehicle's own exterior extent.
- **Measure**: where in height the crush is read. EDCRASH takes no height;
  this is how the measurement is taken.
  - **At one height**: a 5 cm slice centred on a **Height above ground** (a
    bumper's, a sill's).
  - **Deepest crush in a height band** (the default): the band is cut into
    5 cm slices, and at each place across the face the deepest crush of any
    slice is used, so a bumper that survived over a crushed rail does not hide
    it. The result line says at what height the deepest crush was found.
  - **Average crush over a height band**: the same slices, averaged at each
    place across the face -- the practice of averaging crush measured at
    several heights.
  - **Outermost surface of a height band**: the face is the outermost surface
    anywhere in the band, which is its least crushed height.

  **Crush stations** sets how many depths (2 to 10). **Smallest crush that is damage** sets where the damaged width
  ends.

**Measure** draws the face, the reference and the crush at each station, and
lists the stations with the damage width and offset. The face is the
outermost surface of the scan in the band, read in 2 cm slices. The damaged
width is the longest stretch crushed more than the smallest crush, and the
stations are spaced equally across it in EDCRASH's own order: C1 is the LEFT
end of a front or back and the REAR end of a side, and the offset is the
centre of the width from the CG (positive to the right for a front or back,
forward for a side). **Apply to the event** writes the depths, width and
offset into Measured Crush; it is locked while results are on screen.

#### Payload

The Payload Data are not used by EDCRASH. Payload inertias may be added to the vehicle inertias and the CG may be moved longitudinally using the Move CG dialog. *(In HVE Studio, Event › Payload is greyed for EDCRASH.)*

> **NOTE:** Lateral and vertical relocation of the CG are not supported by EDCRASH.

### Simulation Controls

If the Trajectory Simulation option is selected, EDCRASH uses the Vehicle Trajectory integration timestep and the maximum simulation time parameters in the Simulation Controls dialog. *(In HVE Studio these are in the **Simulation** panel, docked beside Event Information: **Duration (s)**, **Trajectory Timestep (s)**, **Output Timestep (s)** and the termination velocities. They belong to the event.)*

**Table 2-8: Simulation Control Parameters Used By EDCRASH**

| Parameter | Description |
|---|---|
| Vehicle Trajectory Integration Timestep | The integration timestep used by the numerical integration routine |
| Output Interval | The timestep used to send output results back to HVE |
| Maximum Simulation Time | The maximum simulation time determines how long the simulation is allowed to run before normal termination |
| Min Linear Velocity | The linear velocity used to terminate the run (if the linear and angular velocities for both vehicles are simultaneously less than these termination velocities, the run terminates) |
| Min Angular Velocity | The angular velocity used to terminate the run (see above) |

### Calculation Options

EDCRASH has the following calculation options:

- Program Options
- Separation Velocity Basis
- Consistency Checks
- Simulation Convergence Criteria

These options control the basic execution of an EDCRASH event. The current EDCRASH calculation options are displayed in the EDCRASH Program Data output report (refer to the following chapter). Each of these options is described below. For a complete description of every control in the dialog, see [Calculation Options for EDCRASH](../../10-calculation-options/CalcOptEDCRASHDlg.md).

In HVE Studio the options are in the **EDCRASH Options** window, opened with **Method Options...** in the Event Information panel. **Apply Defaults** restores HVE's defaults. HVE Studio adds a fifth group, **Curved Path**, described below.

![Figure 2-5](images/hvn-edcrash-options.png)

*Figure 2-5: The EDCRASH Options window in HVE Studio. The Curved Path group is below the convergence criteria (scroll down); the convergence criteria are greyed because the basis is Normal.*

#### Program Options

During execution of an EDCRASH event, certain features may be turned on or off. These features are:

- **Common Velocity Check** (default = TRUE) — The EDCRASH damage procedure assumes the vehicles' impulse centers reach a common earth-fixed velocity at the end of the collision phase. The Common Velocity Check compares the separation velocities for both vehicles to determine if this condition is satisfied. EDCRASH produces a warning or error message if the condition is not satisfied (see Chapter 6, Messages, for more information).

  > **NOTE:** The Common Velocity Check is performed during a normal CRASH3 run.

  *(HVE Studio: passed to the engine. Turning it off changes the result.)*

- **Modify Departure Angle** (default = TRUE) — If a point on curve is not entered, but a vehicle's post-impact phase has an angular separation velocity and a change in heading angle between separation and end of rotation (or rest), EDCRASH modifies the departure angle using an empirical relationship [3].

  > **NOTE:** Modify Departure Angle is performed during a normal CRASH3 run.

  *(HVE Studio: passed to the engine, and it behaves as in HVE. While Common Velocity Check is on it has no effect, because the check recomputes the departure angle from the separation velocity right after this adjusts it. With the check off it changes the reported departure angle; delta-V then moves only on the Trajectory Simulation basis. A Spiral curved path switches it off; see Curved Path below.)*

- **Auto-set Rot/Lat Skidding** (default = TRUE) — The Event Wheel Data dialog includes a check box, labeled Rot/Lat Skidding. That check box is used by EDCRASH to invoke the modified Marquard analysis [3, 15] for vehicles spinning after impact. Enabling this option causes EDCRASH to automatically assign the status for that program option. When enabled, EDCRASH sets the Rot/Lat Skidding flag to TRUE under the following circumstances: (a) the change in heading angle requires a tighter turn radius than the vehicle is capable of (as defined by its wheel base and maximum steer angle), or (b) the departure sideslip angle exceeds 10 degrees.

  > **NOTE:** The Auto-set Rot/Lat Skidding feature is not included in CRASH3.

- **Include Angular Momentum Solution** (default = FALSE) — When checked, EDCRASH includes a conservation of angular momentum solution in addition to the standard linear momentum solution. *(updated: this fourth check box appears in the current Calculation Options dialog but is disabled (grayed out) and cannot be changed.)* *(HVE Studio: greyed as in HVE. EDCRASH only prints the setting in the Program Data report; no angular-momentum solution is implemented.)*

If all of the above options are turned off, EDCRASH performs a simplistic analysis comparable to what is traditionally done on a hand-held calculator.

#### Separation Velocity Basis

EDCRASH has the following user-selectable trajectory model options:

- **Normal** — Choosing Normal causes EDCRASH to perform its standard, energy-based calculations to provide an estimate for separation forward, lateral and angular velocities and departure angle.
- **Trajectory Simulation** — Choosing Trajectory Simulation causes EDCRASH to perform its standard, energy-based calculations (same as choosing Normal, above), and then use these separation velocities and departure angles as the initial conditions for a trajectory simulation. *(updated: this option does not support vehicles with dual tires — a dual tire at any wheel position is rejected with a fatal error at event initialization. The other three choices are unaffected.)*
- **Sustained Contact** — Choosing Sustained Contact causes EDCRASH to use a weighted drag factor based on the wheel lock-ups and weights of the individual vehicles.
- **Iterate on Sideslip** — *(updated: the current dialog offers a fourth radio button, Iterate on Sideslip, which requests an iterative solution on vehicle sideslip angle. This option is not supported by the current EDCRASH physics engine; selecting it causes the event to terminate with an error.)*

!!! warning "Not in HVE Studio: Iterate on Sideslip"
    HVE Studio offers the button because HVE does, and marks it as not
    implemented. A run with it selected is refused by EDCRASH with stop code
    −5504 and produces no results.

!!! note "HVE Studio"
    Normal, Trajectory Simulation and Sustained Contact are all passed to
    the engine and each gives a different answer. Trajectory Simulation with
    **Number of Runs** = 1 gives exactly the Normal answer, since one
    trajectory run is the closed-form solution. The per-wheel steer angles
    in Wheel Data are read only on the Trajectory Simulation basis.

> **NOTE:** You cannot choose both Sustained Contact and Trajectory Simulation because the EDCRASH Trajectory Simulation does not account for the inter-vehicle contact force during the post-impact phase.

#### Consistency Checks

EDCRASH performs a series of internal consistency checks to confirm that various individual pieces of data are consistent with each other. When results are found to be inconsistent, as determined by these user-editable ranges, messages are produced and displayed in the Messages Output Report (refer to Chapter 6, Messages). The following internal consistency checks are performed:

- **PDOF Range** (default = ±10 deg) — If the collision type is oblique and the user also enters damage data for both vehicles, EDCRASH can compare the PDOFs computed by the momentum analysis with the values entered by the user. If the difference between the momentum-based and user-entered values exceeds the PDOF Range, a message is displayed in the Messages Output Report.
- **Delta-V Range** (default = ±10%, entered as 0.10) — If the collision type is oblique and the user also enters damage data for both vehicles, EDCRASH can compare the delta-Vs computed by the momentum analysis with the results computed by the damage analysis. If the difference between the momentum-based and damage-based results exceeds the Delta-V Range, a message is displayed in the Messages Output Report.
- **K.E. Range** (default = ±50%, entered as 0.50) — If the collision type is oblique and the user also enters damage data for both vehicles, EDCRASH can compare the kinetic energy loss computed using the momentum-based impact speeds with the kinetic energy loss computed using the damage-based impact speeds. This difference is also directly compared with the damage energy calculated from the damage analysis. If the difference in kinetic energy from the momentum-based or damage-based impact speeds differs from the damage energy computed from the damage analysis by more than the K.E. Range, a message is displayed in the Messages Output Report.
- **Newton's 3rd Law Range** (default = ±100%, entered as 1.00) — If damage data are entered for two vehicles in a collision, EDCRASH can compare the peak forces computed independently for each vehicle. If the difference in peak forces exceeds the Newton's 3rd Law Range, a message is displayed in the Messages Output Report.

  > **NOTE:** For barriers, the collision force is not calculated independently; the force on the barrier is set equal to the force on the deformable vehicle.

#### Simulation Convergence Criteria

If the Separation Velocity Basis was selected as Trajectory Simulation (see above), a series of tests are performed comparing the simulated path with the actual path (i.e., the path defined by the user-entered path positions). EDCRASH then reports the difference between the simulated path and actual path by calculating the distance between the individual simulated and actual path positions. The difference is reported as an error for each path position entered by the user (i.e., point on curve, end of rotation and rest). If one or more errors exceeds the allowable value(s), the separation velocities are adjusted and the simulation is re-executed.

For the simulation to successfully converge, each error must be less than that specified in the Simulation Convergence Criteria. When the difference between the simulated and actual paths is acceptable for all positions, the trajectory simulation is said to have converged. The simulation will be re-executed (up to 5 runs by default) in an effort to achieve convergence. If, after the specified number of runs, the simulation has not converged, the separation conditions that produced the smallest total error are used by EDCRASH.

The default convergence tolerances are: Rest Error X-Y = 0.10, Rest Error Heading = 0.10, EOR Error X-Y = 0.15, EOR Error Heading = 0.15, POC Error X-Y = 0.15 (all as fraction, %/100). See [Calculation Options for EDCRASH](../../10-calculation-options/CalcOptEDCRASHDlg.md) for details.

In HVE Studio the **Number of Runs** and the five error tolerances are greyed unless the basis is Trajectory Simulation, because EDCRASH reads them only then.

#### Curved Path

*(HVE Studio.)* When a vehicle has a **Point on Curve** position, EDCRASH draws its post-impact path through that point using HVE's curved-path settings, which HVE Studio shows in the EDCRASH Options window under **Curved Path (through a Point On Curve)**. The group is greyed when no vehicle in the event has a Point on Curve.

- **Path Type** — **Circular arc** or **Spiral (spline)**. A spiral takes the path length and the departure angle from the spline and switches Modify Departure Angle off; a circular arc uses the arc geometry and leaves it on. The choice can change the result substantially.
- **Tangent** — **Heading vector** or **Velocity vector**. It is passed to the engine; on the one reference case that has a Point on Curve it did not change the result.

The Program Data report displays all the calculation options used for the current EDCRASH event (see also Chapter 3). The results for the trajectory simulation, if selected, are also displayed in the Program Data Output Report.

### Executing an Event

In HVE Studio an event is executed from the **playback bar** under the viewport, or with **Output › Run Simulation...**.

![Figure 2-6](images/hvn-playback-bar.png)

*Figure 2-6: The playback bar after an EDCRASH run. Run and Reset are at the left; the transport buttons, the time slider and the active method follow.*

The playback bar's buttons have the following functions:

- **Run** — Execute the active event
- **Reset** — Discard the results so the event's inputs can be edited and the event run again
- **|<**, **<<**, **Play**, **>>**, **>|** — Rewind to start, step back, play, step forward and advance to end of the playback

Because EDCRASH is a reconstruction program (as opposed to a simulation program), it performs a single set of calculations and terminates. Pressing **Run** causes the EDCRASH calculations to be performed. Pressing **Reset** erases the event output (next chapter); it does not affect the event input.

!!! note "HVE Studio"
    - While an event's results are on screen its inputs are locked, and the
      Event Information panel says so ("Showing results for this event --
      inputs are locked..."). Press **Reset** (or **Reset Run to Edit** in
      the panel) to edit and re-run.
    - After the run the viewport plays a path for each vehicle drawn through
      its surveyed positions (Begin Braking, Impact, Separation, Point on
      Curve, End of Rotation, Rest) at the speeds EDCRASH solved, and labels
      it "Showing the reconstruction". The path is an interpolation for
      viewing, not EDCRASH output. With no rest position (a damage-only reconstruction)
      the placement is drawn but not measured. Every vehicle reaches the
      impact at the same moment: one whose surveyed approach is shorter is
      shown driving toward its first surveyed position, at that position's
      speed and heading, until it does.
    - Results appear in **Key Results** and **Output › HVE Reports**; see
      [Chapter 3](03-program-output.md).

> **NOTE:** EDCRASH is fundamentally a reconstruction program, not a simulation program. In HVE, pressing Play executes the calculations but nothing appears to move; watch the Key Results to see the effects of execution.

> **NOTE:** You will probably find it very useful to execute an EDCRASH run, make changes to the event set-up options (see previous section), and re-execute the event. You will very quickly discover the event-related parameters to which the analysis is sensitive.

> **NOTE:** If the Trajectory Simulation option is selected, the simulation is performed, but not visualized.

> **NOTE:** Remember to use the View menu to open useful panels, such as Key Results, and the Scene Display panel (View › Scene Display) for options such as Scene Ghosts.

---

*Previous: [Chapter 1 — Program Description](01-program-description.md) · Next: [Chapter 3 — EDCRASH Program Output](03-program-output.md)*

<!-- NAV -->

---

← Previous: [Chapter 1 — EDCRASH Program Description](01-program-description.md)  |  [Index](README.md)  |  Next: [Chapter 3 — EDCRASH Program Output](03-program-output.md) →

<!-- /NAV -->
