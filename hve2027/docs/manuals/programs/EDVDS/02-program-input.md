# Chapter 2 — EDVDS Program Input

This chapter defines the objects (humans, vehicles and environment) and the event set-up parameters (positions, damage profiles, driver controls, and so forth) used by the EDVDS analysis. In general, the chapter is divided into the following sections:

- **Objects** — The number of humans and vehicles, and the specific human and vehicle parameters actually used by EDVDS.
- **Events** — The various HVE options available for setting up and executing an EDVDS event.

## Objects Overview

The objects used by the EDVDS model are:

- **Humans** — Humans are not simulated by EDVDS.
- **Vehicles** — Up to six vehicles (a tow vehicle and up to three trailers and two dollys) may be included in an EDVDS event.
- **Environment** — Like the *real* world, EDVDS has exactly one environment.

> **NOTE:** The environment is used in any HVE-compatible reconstruction or simulation model.

!!! note "HVE 2027"
    An EDVDS event in HVE 2027 holds at most **four** vehicles (tow vehicle, semitrailer, dolly, semitrailer). The Event Information panel stops offering **Add Vehicle** at four, so the six-object triple cannot be set up. The engine accepts 1, 2, 4 or 6 vehicles; an event of three is refused when it runs.

The following sections describe how the vehicle and environment provide the required inputs to the EDVDS calculation model.

## Vehicles

EDVDS uses up to six vehicles created using the Vehicle editor (see Figure 2-1). Vehicles are selected from the Vehicle Database by choosing the following attributes:

- **Type** — EDVDS supports the following vehicle types: *Passenger Car, Pickup, Van, Sport-Utility, Truck, Trailer* and *Dolly*.
- **Make** — EDVDS supports all available vehicle makes.
- **Model** — EDVDS supports all available vehicle models, within the limits defined by number of axles and drive axles; see below.
- **Year** — EDVDS supports all available vehicle years.
- **Body Style** — EDVDS supports all available vehicle body styles.

Each vehicle also has the following additional user-editable parameters:

- **Driver Location** — The *Driver Location* is not used by EDVDS. However, *Driver Location* for the tow vehicle must not be *None*; otherwise, the Driver Controls (Steering, Brakes, Throttle, Gear Selection) will not be available during Event mode.
- **Engine Location** — The *Engine Location* is not used by EDVDS. However, *Engine Location* for the tow vehicle must not be *None*; otherwise, the Throttle Table will not be available during Event mode.
- **Number of Axles** — The tow vehicle may include two or three axles; trailers and dollys may have either one or two axles.
- **Drive Axle(s)** — EDVDS supports all drive axles.

!!! note "HVE 2027"
    In HVE 2027 the Driver Controls dialog is available for every vehicle in the event, whatever its Driver Location or Engine Location.

To add a vehicle to the current case in HVE 2027, perform the following steps:

1. Choose the **Vehicle (F3)** editor tab.
2. Click **Add…** on the **Vehicles** panel. The vehicle picker is displayed; it searches the loaded vehicle databases and also offers HVE's Generic vehicles by type and class (a Generic *Trailer* or *Dolly* is chosen this way).
3. Pick the vehicle. It is added to the case (not to an event: that is done under **Vehicles in Event**, below), and its data are shown in the **Vehicles** panel under **Identity** (Name, Vehicle Type, Make, Model, Year, Body Style, Color) and **Configuration** (Number of Axles, Driver Location, Engine Location, Drive Axle(s)).
4. If desired, modify the *Number of Axles*, *Driver Location*, *Engine Location* and *Drive Axle(s)*, and edit the *Name*. The name does not affect calculations.

![Figure 2-1](images/hvn-edvds-vehicle-editor.png)
*Figure 2-1: The HVE 2027 Vehicle editor with EDC's tutorial tractor selected. The Vehicles panel (left) lists the case's tow vehicle, two trailers and dolly; the viewport (right) shows the selected vehicle.*

The following Vehicle Parameter groups are used by EDVDS:

- Sprung Mass
  - Inertias
  - Move CG
  - Inter-vehicle Connections
- Unsprung Mass
  - Wheel Location
  - Tire Data
  - Suspension Data
  - Brake Data
- Steering System
- Brake System
- Drivetrain

> **NOTE:** The Exterior Data Group (Overall Dimensions, Structural Stiffness Coefficients) is not used by EDVDS.

> **NOTE:** Be sure both vehicles have the proper connections (King Pin/Fifth Wheel, Pintle Hook/Eye, or Ball/Hitch). If the connections are not compatible, or if connections are not supplied, a message will be issued during Event Set-up.

!!! note "HVE 2027"
    HVE 2027 checks the whole vehicle train when EDVDS is chosen. In **Event Information › Calculation Method**, a method the current vehicles cannot run is marked "N/A for these vehicles" in the Method list (hover it for the reason), and the panel prints **Cannot run:** followed by the problem — for example an independent suspension, a 3-axle tow vehicle without a tandem rear suspension, or connection heights that do not match. The same check runs again when you press **Run**.

The specific vehicle data used in each of the above parameter groups are defined in Tables 2-1 through 2-5.

### Sprung Mass

The Sprung Mass parameter groups used by EDVDS are shown in Table 2-1. Information on each group is provided below.

**Table 2-1: Vehicle Sprung Mass Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Sprung Weight | Weight of sprung mass |
| Sprung Mass Roll, Pitch and Yaw Inertia | Rotational inertias of sprung mass about the vehicle-fixed x, y and z axes, respectively |
| Move CG x,z | Relocates the CG in the vehicle-fixed x and z directions (lateral relocation is not supported by EDVDS). This entry causes an automatic adjustment of all vehicle coordinate-related parameters (e.g., contact surface, belt anchor points). |
| Inter-vehicle Connections | Vehicle-fixed x,y,z connection coordinates; rear connections also include maximum articulation angle. |

#### Inertias

EDVDS uses the total vehicle weight (converted to mass according to the current gravitational constant; see Environment), and the roll, pitch and yaw rotational inertias of the sprung mass.

The total weight is used because it is the value traditionally obtained from data sources. The equations of motion require that the sprung mass be known. To obtain this value, EDVDS simply deducts the weight of the suspensions and wheels.

!!! note "HVE 2027"
    Weight is edited in the **Vehicles** panel (**Size & Weight**); weight and inertias in the **Inertia / Mass** dialog (**Edit…** in the panel's **Inertia** section), which shows each value on both the total and the sprung basis.

> **NOTE:** The inertial contributions of the front and rear suspensions are added to calculate the total yaw inertia reported in the Vehicle Data output report.

#### Move CG

Move CG is not directly used by EDVDS. Its current value does not show up in the results. However, the Move CG fields may be used to quickly move the vehicle's center of gravity; the x,y,z coordinates for the wheels are updated to reflect the new CG location.

#### Geometry File

The Geometry File is not used by EDVDS.

!!! note "HVE 2027"
    The 3-D model is set in the **Vehicles** panel's **3D Geometry** section or on the File & Placement tab of **Vehicle › Editors › Vehicle Mesh…**. It is used for display only in an EDVDS event.

#### Contact Surfaces

Contact Surface parameters are not used by EDVDS.

#### Belt Restraints

Belt Restraint parameters are not used by EDVDS.

#### Airbag Restraints

Airbag Restraint parameters are not used by EDVDS.

#### Inter-vehicle Connections

Inter-vehicle Connection parameters define the type, location and properties of the front and rear vehicle connections. The x,z location is specified relative to the vehicle CG. The z coordinates for each vehicle determine the elevation at the connection point, and thus establish the pitch angle of the trailer.

Dollys may be either *fixed* or *converter* dollys. A fixed dolly is permanently attached to the front of the trailer and normally has a hinged drawbar. A converter dolly is removable. It normally has a hinged fifth wheel and a fixed drawbar. See [Chapter 4](04-calculation-method.md) for more information about drawbar types and their characteristics.

*Maximum Articulation Angle* is only supplied for rear connections.

> **NOTE:** Every trailer will have a pre-defined front connection. However, not every tow vehicle has a pre-defined rear connection. Use the Vehicle Editor to confirm the vehicle has a connection.

> **NOTE:** If no connection is supplied, EDVDS cannot be executed; a message will be displayed during Event Set-up.

> **NOTE:** The rear connection of the first tow vehicle must be a fifth wheel. If it is not, a message will be displayed during Event Set-up.

!!! note "HVE 2027"
    In the Vehicle editor, open the **Vehicles** panel's **Components** section and click **Connections…**. The **Vehicle Connections** dialog has a **Front Connection** and a **Rear Connection**, each with a type and X / Y / Z coordinates (relative to the CG; Z is measured down from the CG). Below each Z the dialog shows the connection's height above ground.

    **Properties…** (under Rear Connection) opens **Connection Properties**: Radius, Friction, Free Play, Stiffness, Damping and Breakaway Force, and the Max Articulation Roll, Pitch and Yaw. EDVDS uses the **Yaw** limit: a run in which a trailer exceeds it stops with the maximum-articulation message (see [Chapter 6](06-messages.md)).

    **Connection heights must match.** EDVDS does not adjust connection heights: when the tow vehicle's rear connection and the trailer's front connection differ in height above ground by more than 0.1 in, the event is refused. HVE 2027 reports this before running and names both vehicles and both heights.

#### Drag Forces

Drag Force parameters are not used by EDVDS.

### Unsprung Mass

The Unsprung Mass parameters used by EDVDS are shown in Table 2-2. Information on each group is provided in this section.

**Table 2-2: Vehicle Unsprung Mass Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Wheel Location | Vehicle-fixed x,y,z coordinates for each wheel |
| Brake Time Lag | Time required for brake system pressure to reach the brake actuation chamber |
| Brake Time Rise | Time required for air to fill the brake actuation chamber and begin stroking the pushrod |
| Brake Torque Ratio | The ratio of effective brake torque at the wheel to fluid pressure in the wheel cylinder |

#### Wheel Location

For each vehicle in the simulation, EDVDS uses the following wheel location parameters:

- **X_wheel** — the longitudinal distance from the CG to each axle.

  > **NOTE:** X_wheel is assumed to be the same for left and right-side tires. If different values are entered, EDVDS uses the average.

- **Y_wheel** — the lateral distance from the CG to each axle.

  > **NOTE:** Y_wheel is assumed to be the same for left and right-side tires. If different values are entered, EDVDS uses the average (thus, bilateral symmetry is assumed).

- **Z_wheel** — the vertical distance from the CG to each axle.

  > **NOTE:** Z_wheel is initially assumed to be the same for left and right-side tires.

#### Brake

EDVDS uses the wheel brake system *Time Lag, Time Rise* and *Brake Torque Ratio*. The specific parameters used by EDVDS are shown in Table 2-2.

EDVDS also fully supports the HVE Brake Designer. Refer to the Brake Designer section of the HVE User's Manual for more information.

!!! note "HVE 2027"
    Time Lag, Time Rise and Torque Ratio are edited per wheel in **Vehicle › Editors › Brakes › Brake Assembly…**; the Brake Designer is **Vehicle › Editors › Brakes › Brake Designer…**.

#### Tire

EDVDS allows the user to choose from three tire models:

- **Linear** — A simplified model, useful for non-limit maneuvers
- **Tire Model (Semi-Empirical)** — A good, general purpose tire modeling method
- **Tire Table** — The most sophisticated tire modeling technique *(updated: the **Table Look-Up** method is not currently available; it is greyed out in the Calculation Options dialog, and if it is ever selected the event terminates with a fatal error.)*

The modeling technique selected is dependent upon the particular needs of the analysis. The desired tire model is an EDVDS calculation option (see [Event](#calculation-options)).

!!! warning "Not in HVE 2027"
    HVE 2027 does not offer a choice of tire model for EDVDS: every EDVDS event runs the **Semi-Empirical** model. The Table Look-Up model is refused by EDVDS's own input check in HVE as well (message code −5504), and the Linear model is not offered.

The HVE tire parameters provide the following data groups:

- Physical Data
- Friction Table
- Cornering Stiffness Table
- Camber Stiffness Table
- Slip-vs Rolloff Table

EDVDS's use of these parameters is described below.

##### Physical Data

The Tire Physical Data used by EDVDS are shown in Table 2-3. When AutoPosition is *On*, the tires' unloaded radii are used to establish the vehicle's initial CG elevation.

##### Friction Table

The Friction Data used by EDVDS are shown in Table 2-3. The EDVDS tire model includes load- and speed-dependent friction properties.

The *In-use Factor* is a convenient way to reduce or increase the dependent friction values (peak and slide friction) by making just one adjustment.

**Table 2-3: Vehicle Unsprung Mass, Tire Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Tire Unloaded Radius | Radius of the undeflected tire |
| Tire Initial and Secondary Deflection Rates, the Deflection at Secondary Rate and Maximum Deflection | The initial spring rate of the tire, and the spring rate after a specified amount of tire deflection. The maximum deflection is used to determine when tire deflection exceeds an allowable value. |
| Pneumatic Trail | The distance from the center of the contact patch to the center of pressure |
| Aligning Torque Coefficient | Moment about tire's vertical axis as a result of slip angle |
| Weight, Spin Inertia | The weight and rotational inertia (about the spin axis) of the tire/wheel/brake assembly |
| Tire Friction Table, Test Load/Speed | The load and speed for a given set of friction results |
| Peak Longitudinal and Lateral Friction, Slide Friction, Slip at Peak Friction and Longitudinal Stiffness | Tire frictional properties at the specified load and speed |
| Friction In-use Factor | Multiplier for Longitudinal, Lateral and Slide friction and Longitudinal Stiffness |
| Tire Cornering Stiffness Table, Test Load and Speed | The load and speed for a given cornering stiffness result |
| Cornering Stiffness | Tire lateral force per unit of tire lateral slip for small amounts of lateral slip |
| Cornering Stiffness In-use Factor | Multiplier for Cornering Stiffness values |
| Tire Camber Stiffness Table, Test Load and Speed | The load and speed for a given camber stiffness result |
| Camber Stiffness | Tire lateral force per unit of camber angle for small camber angles |
| Camber Stiffness In-use Factor | Multiplier for Camber Stiffness values |
| Slip vs Rolloff Data | Reduction in longitudinal tire force as a result of lateral slip, and the reduction in lateral tire force as a result of concurrent longitudinal tire slip |

##### Cornering Stiffness Table

The Cornering Stiffness data used by EDVDS are shown in Table 2-3. EDVDS uses the $F_y$ vs Slip Angle table if the Tire Table modeling option is selected; otherwise, the cornering stiffness is used. Cornering stiffness data may be load- and speed-dependent.

The *In-use Factor* is a convenient way to reduce or increase the dependent cornering stiffness values for all speeds and loads by making just one adjustment.

> **NOTE:** If you are simulating a vehicle with a flat tire, you probably want to reduce the In-use Factor to about 0.1.

##### Camber Stiffness Table

The Camber Stiffness data used by EDVDS are shown in Table 2-3. EDVDS uses the $F_y$ vs Camber Angle table if the Tire Table modeling option is selected; otherwise, the Camber Stiffness is used. Camber stiffness data may be load- and speed-dependent.

The *In-use Factor* is a convenient way to reduce or increase the dependent camber stiffness values for all speeds and loads by making just one adjustment.

> **NOTE:** If you are simulating a vehicle with a flat tire, you'll probably want to reduce the In-use Factor to about 0.1.

##### Slip vs Rolloff Table

The Longitudinal and Lateral Slip vs Rolloff Tables are used if the Tire Table tire model method is used. The longitudinal slip vs rolloff table defines the loss of longitudinal tire force when the tire is steered (compared to an un-steered tire). The lateral slip vs rolloff table defines the loss in lateral tire force when the tire is braked or accelerated (compared to a free-rolling tire).

*(updated: because the Table Look-Up tire model method is currently disabled, the $F_y$ vs Slip Angle, $F_y$ vs Camber Angle and Slip vs Rolloff tables are not used by the current version of EDVDS.)*

#### Suspension

The HVE Suspension Model provides the following data groups:

- Springs and Shocks
- Inertia
- Jounce/Rebound Stops
- Spindle Axis
- Camber Table
- Anti-pitch Table
- Roll Steer Table

EDVDS supports only solid axle suspensions. EDVDS's use of the suspension parameters is described below.

!!! note "HVE 2027"
    Suspension parameters are edited in **Vehicle › Editors › Suspension Data…** (Suspension Type, Roll Couple Distribution and Inter-Tandem Load Transfer rows, per axle, and its Jounce / Rebound, Camber, Roll Steer and Anti-Pitch tabs). An *Independent* suspension on any axle is refused for EDVDS, and on a 3-axle tow vehicle the rear axles must be a tandem type (*4-Spring Tandem* or *Walking Beam Tandem*); HVE 2027 reports both before running.

##### Inter-tandem Load Transfer

If three axles are supplied for the tow vehicle, or two axles are supplied for the trailer or dolly, the vehicle is assumed to have tandem axles. In this case, a longitudinal load transfer due to braking may be simulated by supplying an Inter-tandem Load Transfer Coefficient.

##### Springs and Shocks

EDVDS uses the individual spring rates for the right and left springs on an axle. They need not be equal.

Roll Center Height and Lateral Spring Spacing apply for each axle.

> **NOTE:** Remember that roll center height is measured from the sprung mass CG, and is positive downwards.

Damping properties, like spring rates, are applied to the right and left sides of each axle; they need not be equal.

The Spring and Shock data used by EDVDS are shown in Table 2-4.

##### Inertias

Inertial mass parameters do not include the weight of the brake assemblies or wheels (brake and wheel inertias are included with the tire). The Suspension Inertia data used by EDVDS are shown in Table 2-4.

**Table 2-4: Vehicle Unsprung Mass, Suspension Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Suspension Type | Solid Axle, Tandem Axles (4-Spring or Walking Beam) |
| Ride Rate, Front and Rear | Linear spring rate for the selected suspension |
| Auxiliary Roll Stiffness | Roll stiffness from an anti-sway bar |
| Roll Center Height | For solid axle suspensions, the distance from the CG to the roll axis at the suspension |
| Lateral Spring Spacing | The lateral distance between springs |
| Damping Rate | Velocity-dependent suspension damping rate |
| Coulomb Friction | Force required to initiate suspension movement |
| Friction Null Band | Suspension velocity required for full coulomb friction |
| Suspension Weight | For solid axle suspensions, the weight of the axle, not including tires, wheels and brakes |
| Suspension Roll/Yaw Inertia | For solid axle suspensions, the rotational inertia about the vehicle-fixed x and z axes |
| Jounce/Rebound Stop, Max Deflection | Deflection from equilibrium to jounce and rebound stops |
| Jounce/Rebound Stop Linear, Cubic Stiffness | Stiffness constants for suspension stops |
| Jounce/Rebound Stop Energy Ratio | Restitution for stop, defined as the ratio of the non-conserved energy to total energy absorbed by the suspension stop |
| Camber | Camber value |
| Roll Steer | The ratio of axle steer to sprung mass roll angle |

##### Jounce and Rebound Stops

The linear and cubic deflection rate of the suspension stops is used to limit the travel of each suspension. The values need not be exact; their primary purpose is to prevent excessive excursion of an axle. The Jounce and Rebound Stop data used by EDVDS are shown in Table 2-4.

##### Spindle Axis

The Spindle Axis data are not used by EDVDS.

##### Camber and Half-Track Change Tables

Solid axle camber may be assigned to each wheel. The camber data used by EDVDS are shown in Table 2-4. Half-track change tables are not used by EDVDS.

##### Anti-pitch

The Anti-pitch tables are not used by EDVDS.

##### Roll Steer

The roll steer constant is used by each axle. Roll steer defines the amount of steering produced as the sprung mass rolls about the roll axis.

### Exterior

The Vehicle Exterior Data (Exterior Dimensions, Stiffness) are not used by EDVDS.

### Steering System Data

EDVDS uses the steering gear ratio if the *At Driver* Steering Table option is used during Event set-up. See Table 2-5. Otherwise the steering system data are not used.

!!! note "HVE 2027"
    The steering gear ratio is in **Vehicle › Editors › Steering System…**; the pedal ratio is in **Vehicle › Editors › Brakes › Brake System Pressure…**; engine, transmission and differential data are in **Vehicle › Editors › Drivetrain…**.

### Brake System Data

The brake system pedal ratio (system pressure per unit of pedal force) is used if the *At Driver* Brake Table option is used during Event set-up. See Table 2-5. Otherwise the Brake System Data are not used by EDVDS.

**Table 2-5: Vehicle Steering, Brake System and Drivetrain Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Steering Gear Ratio | Ratio of the angle at the steering wheel to the angle at the tire |
| Brake Master Cylinder Ratio | Brake system pressure produced per unit of pedal force applied by the driver |
| Engine Table | Engine Torque vs Speed Table for Wide-open and Closed Throttle Tables for Torque vs speed. Defines range from idle to maximum RPM. |
| Transmission Gear Table | Table of numeric ratio for each of up to 12 forward speeds plus reverse |
| Differential Gear Table | Differential numeric ratio (only single speed is supported) |

> **NOTE:** For vehicles with air brake systems, the Pedal Ratio is assigned a value of 1.0; thus, the entered pedal force is the same as the system brake application pressure.

> **NOTE:** See also Wheel Brake Data (Unsprung Mass Parameters) for related information about the vehicle's brake system parameters.

### Drivetrain Data

Engine power as a function of engine speed is defined for both wide-open throttle and closed throttle positions. The Drivetrain data (engine power vs. speed, transmission ratio, differential ratio, drivetrain inertia) are used if the *Percent Wide-open Throttle* option is used during Event set-up (see Table 2-7).

The drivetrain data used by EDVDS are shown in Table 2-5.

The user-entered Power vs. Engine Speed Table defines the valid range of engine speeds for a given event. If the maximum engine speed in the table is exceeded, the simulation terminates with an error message (see [Messages](06-messages.md)).

> **NOTE:** The typical solution to this problem is to shift sooner.

The transmission may have up to 12 forward ratios, plus reverse and neutral. The differential may have up to three ratios.

## Environment

EDVDS uses the environment created by the Environment editor (see Figure 2-4). The environment is created by defining the following groups of attributes:

- Visual Data
- Physical Data

### Creating an Environment

A case in HVE 2027 always has exactly one environment; there is nothing to add. To edit it:

1. Choose the **Environment (F4)** editor tab.
2. The **Environment** panel is displayed (**Environment › Environment…** reopens it).
3. In **Location**, set the location (search an address, paste a coordinate, or enter latitude and longitude) and the date and time of the event.
4. In **Terrain › Scene Geometry**, open the site's 3-D geometry (`.h3d`, DXF, `.iv`, OBJ or glTF) with **Browse…** and **Import**.
5. In **Physical**, enter the ambient temperature and pressure, the wind and the **Gravity**.

Values are shown in the units set in **Tools › Preferences**.

![Figure 2-4](images/hvn-edvds-environment-editor.png)
*Figure 2-4: The HVE 2027 Environment editor showing the Rowena Point site from EDC's EDVDS tutorial case.*

### Visual Data

The following visual parameters may be edited:

- **Environment Location** — A database containing the name (City/State/Country), Latitude and Longitude and GMT for the selected location.
- **Time and Date** — The local standard time and date for the event.

The visual data are not used by the event; they are provided for studies related to visibility at the time of an event (e.g., avoidability of an accident).

> **NOTE:** The visual data (Location, Time, Date and Angle of earth-fixed X axis) affect the lighting of the event! Depending on your view (Camera Position) the scene may be shaded and difficult to see. If the time is after sundown, the view will be dark.

### Physical Data

The Physical Data groups are:

- Angle of X Axis
- Wind Speed and Direction
- Atmospheric Temperature and Pressure
- Gravity Constant
- 3-D Surface Geometry

The specific physical environment data used by EDVDS are described below; see also Table 2-6.

**Table 2-6: Environment Model Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Gravitational Constant | Local gravitational constant |
| 3-D Surface Geometry (Elevation, Surface Normal, Friction Factor) | The polygon database used to create the 3-D environment |

#### Angle Of X Axis

The angle of the X axis is used to position the earth-fixed coordinate system on the surface of the earth.

> **NOTE:** The angle is specified relative to true north. If you are using a compass to determine direction at the scene of an accident, you should provide a correction factor before entering this angle.

> **NOTE:** The angle of the X axis affects how you visualize an EDVDS event because it affects the location of the sun.

#### Wind Speed and Direction

Wind Speed and Direction are not used by EDVDS.

#### Atmospheric Temperature and Pressure

Atmospheric temperature and pressure are not used by EDVDS unless the HVE Brake Designer is used. If the Brake Designer is used, atmospheric temperature and pressure are used in the calculation of brake temperatures.

#### Gravity Constant

The gravity constant converts mass to force. An object's mass and rotational inertias are properties that are the same throughout the universe; however the weight of an object is dependent on the local gravitational constant.

#### 3-D Surface Geometry

The 3-D Surface Geometry is used by the tire model in EDVDS to calculate the elevation, slope and friction multiplier for the current X,Y position of the tire.

!!! note "HVE 2027"
    A case with no site geometry still has a flat ground plane for the tires to run on.

## Event

EDVDS uses the Event editor (see Figure 2-5) to create, set up and execute an event. Each of these topics is described below.

![Figure 2-5](images/hvn-edvds-event-editor.png)
*Figure 2-5: The HVE 2027 Event editor with EDC's EDVDS tutorial case loaded: the Event Information panel (left) and the viewport (right), with the playback bar beneath it.*

### Creating An Event

An EDVDS event is created in the Event editor's **Event Information** panel.

To create an EDVDS event:

1. Choose the **Event (F5)** editor tab. The **Event Information** panel is displayed.
2. Click **+** beside **Active Event** to add an event.
3. In **Calculation Method**, choose **EDVDS** from the **Method** list.
4. In **Vehicles in Event**, click **Add Vehicle** and choose the tow vehicle; it becomes slot **V1**. Add the trailer, and for a double the dolly and second trailer, in that order (V2, V3, V4).

   > **NOTE:** The slot order is the order of the vehicle train. A vehicle in the wrong slot is corrected with its slot's drop-down list, which keeps that slot's inputs.

5. Enter the event name in the **Name** field of the panel's **Event** section. The name does not affect calculations.

   > **NOTE:** If you choose a vehicle that is not compatible with EDVDS, or if the tow vehicle connections are incompatible with the trailer, the panel shows **Cannot run:** and the reason, and the Method list marks EDVDS "N/A for these vehicles". The event can still be edited; it cannot be run until the problem is fixed.

!!! note "HVE 2027"
    EDVDS runs its own engine; on HVE's tractor-semitrailer validation cases its tracks end within about 2 cm of HVE's saved runs. The **Method Options…** button is greyed for EDVDS, which has no options in HVE 2027.

**Table 2-7: Event Set-up Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Vehicle Initial Position | The earth-fixed X,Y,Z coordinates and roll, pitch, yaw angles of the vehicle at the start of the simulation |
| Vehicle Initial Velocity | The forward, lateral and vertical linear velocities, and the roll, pitch and yaw angular velocities at the start of the run |
| Driver Controls, Steer Table | Steer Table Option; Steering Wheel Angle vs Time or Tire Steer Angle vs Time |
| Driver Controls, Brake Table | Brake Table Option; Brake Pedal Force vs Time |
| Driver Controls, Throttle Table | Throttle Table Option; Throttle Position vs Time |
| Driver Controls, Gear Table | Transmission Gear, Differential Gear vs. Time |
| Driver Controls, HVE Driver Model | Path Follower parameters; see HVE User's Manual |
| Payload Data | Payload Exists Option; Payload CG x,z coordinates; Payload Weight; Payload Roll, Pitch and Yaw Rotational Inertias |

### Setting Up an Event

EDVDS uses the following *event set-up* options:

- Position/Velocity
- Driver Controls
- Payloads

The specific Event Set-up data used by EDVDS are defined in Table 2-7.

!!! note "HVE 2027"
    In HVE 2027 these are on the **Event** menu (shown in the Event editor) and in the Event Information panel:

    - **Position / Velocity** — each vehicle's initial conditions are listed in **Event Information › Vehicle Initial Conditions**; **Event › Position / Velocity…** (Ctrl+P) opens them for the selected vehicle.
    - **Driver Controls** — **Event › Driver Controls…** (Ctrl+D).
    - **Payload** — **Event › Payload…** edits each unit's payload for this event. A payload on a dolly, which EDVDS refuses, is dropped with a notice in the run status.

#### Position/Velocity

Like all simulations, EDVDS requires initial positions and velocities to be supplied by the user.

The tow vehicle is positioned relative to the earth-fixed coordinate system by supplying the X,Y,Z coordinates of its CG, and roll ($\Phi$), pitch ($\Theta$) and yaw ($\Psi$) angles about vehicle x, y and z axes, respectively.

> **NOTE:** Z, roll and pitch may be supplied automatically by HVE using AutoPosition.

!!! note "HVE 2027"
    Each vehicle in **Vehicle Initial Conditions** has X and Y Position, Heading, an **Auto Position (settle onto terrain)** checkbox, Z Height, Speed, Sideslip and Yaw rate; roll, pitch and the other rates are under **Advanced initial state**. In the viewport, select the tow vehicle and press **G** to move it or **R** to rotate it; the trailers and dolly move with it as a rigid train. EDVDS reads the position and velocity of the tow vehicle only. For each trailer it reads the roll, pitch and heading (and their rates); for a dolly it reads nothing, because the dolly's pose follows from its two connections.

The trailer is positioned relative to the tow vehicle by supplying the initial roll, pitch and yaw articulation angles. The default articulation angles are 0.0 degrees.

The tow vehicle linear velocities are supplied in the form of a total velocity and sideslip angle.

> **NOTE:** The vehicle-fixed u (forward) and v (side) velocity components are calculated using the total velocity and sideslip angle.

The trailer articulation angular velocities are assigned relative to the tow vehicle. Zero angular velocity is assumed as a default, and values need not be entered.

#### Driver Controls

EDVDS uses the following Driver Controls:

- **Steering** — A table of steering inputs as a function of time. The *At Driver* and *At Axle* options are supported.
- **Braking** — A table of braking inputs as a function of time. The *Wheel Force* and *Percent Available Friction* options are supported.
- **Throttle** — A table of throttle inputs as a function of time. The *Wheel Force* and *Percent Available Friction* options are supported.
- **Gears** — A table of transmission and differential gear selections as a function of time.
- **HVE Driver Model** — A closed-loop model that determines the driver steering inputs required to cause the vehicle to follow the desired path. The HVE Driver Model is described in the HVE User's Manual and in Reference [29].

The Driver Controls Data used by EDVDS are shown in Table 2-7.

!!! note "HVE 2027"
    **Event › Driver Controls…** has **Throttle**, **Brake**, **Steer** and **Gear** tabs and a **Vehicle** list for choosing the unit. Throttle and Brake each have an **Input Method** list (*Pedal (AT_DRIVER)*, *Wheel Force* for the brake, *% of Friction*). The Steer tab is a steering-wheel-angle table; a table of road-wheel angles (HVE's *At Axle* option) is shown and used when the case already contains one, for example an imported HVE case, but there is no control to start one. The HVE Driver Model is **Event › Path Follower…**.

    EDVDS reads the steering, braking and throttle tables of the tow vehicle and the first trailer only. Tables entered for a dolly or a second trailer are not used.

#### Damage Profile

The Damage Profile Data are not used by EDVDS.

#### Payload

The Payload Data used by EDVDS include the payload coordinates relative to the vehicle's CG, and the payload rotational inertias.

> **NOTE:** Lateral payload offset is not supported.

> **NOTE:** Payload positioning is relative to the vehicle CG, not the rear suspension.

#### Collision Pulse

The Collision Pulse data are not used by EDVDS.

#### Contacts

The Contacts data are not used by EDVDS.

#### Restraints

The Restraints data are not used by EDVDS.

### Simulation Controls

EDVDS uses the current simulation control parameters. The Simulation parameters used by EDVDS are shown in Table 2-8.

!!! note "HVE 2027"
    The simulation controls are in the **Simulation** panel, a tab beside **Event Information**: **Duration**, **Trajectory Timestep** and **Output Timestep**, a **Termination** section (linear and angular termination velocities, each with an **On** checkbox) and an **Integrator Convergence** section (**Maximum Bisections**, **Velocity Convergence**). The collision and separation timesteps are hidden for EDVDS, which does not use them. The values belong to the event.

**Table 2-8: Simulation Control Parameters Used By EDVDS**

| Parameter | Description |
|---|---|
| Vehicle Trajectory Integration Timestep | The integration timestep used by the numerical integration routine |
| Output Interval | The timestep used to send output results back to HVE |
| Maximum Simulation Time | Maximum length of the run |
| Minimum Linear Velocity | The linear velocity used to terminate the run (if the linear and angular velocities are simultaneously less than these termination velocities, the run terminates) |
| Minimum Angular Velocity | The angular velocity used to terminate the run (if the linear and angular velocities are simultaneously less than these termination velocities, the run terminates) |

> **NOTE:** The output time interval should be an even multiple of the vehicle trajectory integration timestep. For example, if the integration timestep is 0.0025 sec, the output interval might be 20 x 0.0025, or 0.0500 sec.

### Executing An Event

#### Calculation Options

EDVDS has one calculation option; for full details see [EDVDS Calculation Options](../../10-calculation-options/CalcOptEDVDS.md):

- **Tire Model Method** — Select from three methods: **Linear** (the default; to be used only for simple, non-limit maneuvers), **Semi-Empirical** (the most robust method) and **Table Look-Up** (not currently implemented; the choice is greyed out in the dialog, and selecting it produces a fatal error and the event will not run).

> **NOTE:** EDVDS will terminate with an error message if you select the Linear tire model method for an event that results in tire longitudinal or lateral slip beyond the linear range.

!!! warning "Not in HVE 2027"
    HVE 2027 has no EDVDS Calculation Options dialog. Every EDVDS event runs the **Semi-Empirical** tire model; Linear and Table Look-Up cannot be selected. (Run with the Linear model, EDC's tutorial case stops early with the excessive-tire-deflection message, so it is not a usable alternative for a limit maneuver.)

#### Get Surface Information

This option determines how EDVDS selects the current terrain properties from the environment 3-D geometry file. The default value is *From Previous Polygon*. This option results in fastest execution, but does not work for all environments.

!!! note "HVE 2027"
    The search method is in **Event Information › Road Surface Search**: *Default for this method* (tracks the previous polygon, HVE's default), *All triangles - first hit in file order* (HVE's From First Polygon), *Track the previous polygon*, and *Track the previous polygon, friction zones first*. HVE's **By Elevation** method, which EDVDS refuses, is not offered.

#### Event Execution

To execute an EDVDS event, use the playback bar under the viewport (Figure 2-7) or **Output › Run Simulation…** (Ctrl+R). The playback bar's buttons have the following functions:

- **Run** — Execute the event (greyed while the event's results are on screen)
- **Reset** — Clear the results so the event can be edited and run again
- **|<** — Jump to the start of the simulation
- **<<** / **>>** — Step back / forward one output step
- **Play** / **Pause** — Play the simulation forwards, or pause it
- **>|** — Jump to the end of the simulation

While a run is in progress the bar shows **Cancel** (and, where available, **Pause** / **Resume**) in place of **Run**. There is no reverse-play button; use the time slider or the step buttons.

![Figure 2-7](images/hvn-playback-bar.png)
*Figure 2-7: The HVE 2027 playback bar, used for starting event execution and for replaying an executed event.*

> **NOTE:** After an event is executed, its inputs are locked while the results are on screen. Press **Reset** to edit the event and run it again.

> **NOTE:** Key Results is on the **View** and **Output** menus; velocity vectors and skidmarks are in **View › Scene Display**.

<!-- NAV -->

---

← Previous: [Chapter 1 — EDVDS Program Description](01-program-description.md)  |  [Index](README.md)  |  Next: [Chapter 3 — EDVDS Program Output](03-program-output.md) →

<!-- /NAV -->
