# Chapter 3 — EDVDS Program Output

This chapter defines the outputs available from an EDVDS event. In HVE the reports produced by EDVDS are available in the Playback Editor.

!!! note "HVE Studio"
    HVE Studio has no Report Window Information dialog, and the reports are not in the **Playback** editor (F6), which plays several events in sequence. After an EDVDS event is run (**Run** on the playback bar, or **Output › Run Simulation…**), its outputs are on the **Output** menu of the Event editor:

    | HVE output | HVE Studio |
    |---|---|
    | Messages, Accident History, Driver Controls, Environment Data, Program Data, Vehicle Data | **Output › HVE Reports…** — the pages EDVDS itself builds, one tab per page, with a field and button to save the page as a text file |
    | Variable Output | **Output › Key Results…**, with the variables chosen in **Output › Variable Selection…**; **Output › Output Graph…** plots variables chosen with its own **Select Variables…** button; **Output › Export Variables…** writes the Key Results variables to a file |
    | Key Results | **Output › Key Results…** |
    | Trajectory Simulation | the Event editor's own viewport, driven by the playback bar |

    The EDVDS Accident History page is the ACCIDENT HISTORY tab of **Output › HVE Reports…**. There is no Print command; save a report page as text or HTML (**Save This Page**, **Save Page as HTML**), or export variables, and print from another program or a browser.

## Overview

EDVDS produces three types of output reports:

- **Alpha-Numeric Reports** — Reports containing text and numeric information, such as vehicle dimensional parameters
- **Variable Output Tables** — Reports containing tabular simulation results as a function of time
- **Trajectory Simulations** — Viewers containing dynamic, 3-D visual simulations

## Alpha-Numeric Reports

EDVDS produces the following alpha-numeric reports:

- **Messages** — A list of messages produced by the current run
- **Accident History** — A table of initial and final positions and velocities
- **Driver Controls** — A table of user-entered vehicle driver controls
- **Environment Data** — A table describing the environment physical and geometrical properties
- **Program Data** — A table containing program control information for the current run
- **Vehicle Data** — A series of tables containing the vehicle data used by EDVDS

Examples of these reports from EDC's tutorial case, as HVE Studio shows them in **Output › HVE Reports**, are reproduced below.

!!! note "HVE Studio"
    HVE Studio shows the pages as plain text in one font, so column alignment depends on the font. In the Program Data page, the HVE Version, EDVDS Version and Date / Time of Execution lines are blank.

### Messages

A typical Messages Report is shown in Figure 3-1. For a complete listing of messages issued by EDVDS, see [Chapter 6](06-messages.md).

```text
                                  MESSAGES

                                 No Messages
```
*Figure 3-1: The Messages page for EDC's tutorial event, as shown by Output › HVE Reports in HVE Studio.*

!!! note "HVE Studio"
    Problems HVE Studio finds in a case before or after the run (a refused vehicle combination, a payload dropped from a dolly, an option it does not honor) are reported in the run status shown on the playback bar under the viewport, not on this page.

### Accident History

The Accident History Report displays a table of initial and final positions and velocities for each vehicle (tow vehicle and trailers). A typical Accident History Report is shown in Figure 3-2.

```text
                                                                        ACCIDENT HISTORY

Total Distance Travelled :   434.32
Time :                       5.0056

                                                       Position                                                     Velocity
                                ----------------------------------------------------     -------------------------------------------------------------
Initial Conditions:                    X         Y        Z     Roll    Pitch  Heading    V-tot    u-vel    v-vel    w-vel      p-vel      q-vel      r-vel
                                    (ft)      (ft)     (ft)    (deg)    (deg)    (deg)    (mph)    (mph)    (mph)    (mph)  (deg/sec)  (deg/sec)  (deg/sec)
Tutorial - Freightliner FLD       446.00   -945.00   -75.26     6.09    -9.19    65.00    55.00    55.00     0.00     0.00       0.00       0.00       0.00
Trailer 1                         432.25   -972.73   -81.65     5.77    -9.28    63.02    55.00    55.00     0.00     0.00       0.00       0.00       0.00
Trailer 2                         409.56  -1017.36   -89.90     5.17    -9.42    63.02    55.00    55.00     0.00     0.00       0.00       0.00       0.00

Final Conditions:
Tutorial - Freightliner FLD       459.02   -532.68     3.74  -178.33    11.55   161.85    57.60    16.54    42.55   -35.13    -153.20     -10.25     -22.95
Trailer 1                         486.84   -546.66     7.03  -184.13    -2.40   147.45    66.30    35.59    48.22   -28.35    -144.74      -6.37     -39.08
Trailer 2                         519.88   -581.53     9.06  -195.34    -2.62   113.61    82.36    67.04    40.19   -25.96    -146.97      -8.87       0.35
```
*Figure 3-2: The Accident History page for EDC's tutorial event, as shown by Output › HVE Reports in HVE Studio (U.S. units). Dollys are not listed.*

### Driver Controls

The Driver Controls report displays a table of user-entered driver control tables for steering, braking and throttle for each vehicle in the event. A portion of a typical Driver Data report is displayed in Figure 3-3.

```text
----------------------------- DRIVER CONTROL TABLES ------------------------------


          Driver Controls for Tutorial - Freightliner FLD
            Steer Table ('At Driver' Option):
Time       Angle
(sec)      (deg)
 0.0000    75.00
 2.0000   180.00
 5.0000   220.00

            Brake Table ('At Driver' Option):
Time     Pressure
(sec)
 0.0000      0.00
 3.5000      0.00
 3.6000     65.00

            Throttle Table ('At Driver' Option):
Time     Percent WOT
(sec)
 0.0000         0.00

 (No Gear Table)


          Driver Controls for Trailer 1
 (No Steer Table)

 (No Brake Table)

 (No Throttle Table)

 (No Gear Table)


          Driver Controls for Trailer 2
 (No Steer Table)

 (No Brake Table)

 (No Throttle Table)

 (No Gear Table)
```
*Figure 3-3: The Driver Data page for EDC's tutorial event, as shown by Output › HVE Reports in HVE Studio.*

### Environment Data

The Environment Data report displays the physical and visual information describing the environment. This information is displayed in two sections:

- **General Environment Data** — Physical parameters describing the environment (Temperature and Pressure are not used in the EDVDS calculations) *(updated: the original manual said "EDSMAC4" here, a typographical error carried over from another manual)*
- **3-D Environment Terrain Data** — Geometric parameters describing the terrain, including the 3-D geometry filename, number of polygons, the current Get Surface Information method (From First Polygon, From Previous Polygon, From Previous Polygon Sorted, or By Elevation) and the minimum/maximum terrain elevations.

In HVE Studio this page is the **ENVIRON DATA** tab of **Output › HVE Reports**.

> **NOTE:** A detailed description of the terrain vertex information is not practical owing to its large size (a terrain is often composed of several thousand vertices). However, it is possible to view the terrain information (friction multiplier, slope, elevation, and so forth) beneath each tire at each timestep during the simulation by selecting the tire terrain outputs in the Variable Output, Tires output group (see Variable Output later in this chapter).

### Program Data

The Program Data Report includes the following information:

- **General Information** — EDVDS version number and model options used for the current event (HVE version, EDVDS version, date and time of execution, Tire Model Method and dimension basis)
- **Simulation Controls** — Integration parameters used for the current event (Maximum Simulation Time, Integration Time Step, Output Interval, Linear Termination Velocity, Velocity Convergence Criterion, Maximum Bisections)

A typical Program Data Report is shown in Figure 3-5.

```text
                             GENERAL INFORMATION

HVE Version:
EDVDS Version:
Date of Execution:
Time of Execution:
Tire Model Method:  Semi-empirical
Dimension Basis:    Sprung Mass CG


                             SIMULATION CONTROLS

Maximum Simulation Time :        5.0000
Integration Time Step :          0.0025
Output Interval :                0.1000
Linear Termination Velocity :    2.0000
Velocity Convergence Crit:       0.1200
Maximum Bisections:                  12
```
*Figure 3-5: The Program Data page for EDC's tutorial event, as shown by Output › HVE Reports in HVE Studio. The Tire Model Method line always reads Semi-empirical in HVE Studio.*

### Vehicle Data

The Vehicle Data Report includes the following information:

- **Vehicle Dimensional and Inertial Properties** — The dimensional and inertial parameters used by EDVDS in the current event.

  > **NOTE:** The Total Yaw Inertia adds the effect of the unsprung masses (i.e., the wheel and axle masses) to the sprung mass; thus, the value printed is greater than the one displayed in the Vehicle Editor's Inertias dialog.

- **Suspension Properties** — The suspension parameters used by EDVDS in the current event.
- **Tire Properties** — The tire parameters used by EDVDS in the current event.
- **Brake Properties** — The wheel brake parameters used by EDVDS in the current event.

> **NOTE:** The entire Vehicle Data report can be quite lengthy, especially for a combination vehicle with several trailers and dollys.

In HVE Studio this page is the **VEHICLE DATA** tab of **Output › HVE Reports**. It lists, for each unit, the sprung mass, payload, accelerometer and drivetrain parameters, then each axle's suspension and the tire, wheel and brake parameters, as described above.

!!! note "HVE Studio"
    Some unit labels on this page are not filled in (they print as `%s`). Check the unit against the parameter's own dialog when in doubt.

## Graphic Reports

EDVDS produces no Graphic Output Reports.

> **NOTE:** Graphs of simulation results vs time may be produced using the Variable Output window (see next section).

## Variable Output Table

EDVDS produces a Variable Output table containing the time-based simulation results. The Variable Output groups produced by EDVDS are as follows:

### Vehicle Output Groups

- **Kinematics** — Position, velocity and acceleration for the vehicle
- **Kinetics** — Forces and moments acting on the sprung mass
- **Accelerometers** — Linear accelerations at user-specified locations on the vehicle
- **Tire** — The tire output parameters existing at the tire contact patch (compare with Wheel Output, below)
- **Wheel** — The wheel output parameters existing at the wheel's hub. Information about the position of each wheel (compare with Tire output, above)
- **Connections** — The articulation angles and inter-vehicle connection forces
- **Driver** — Current levels of driver inputs (steering, braking, throttle and gear ratios)

A detailed listing of each Variable Output parameter produced by EDVDS is found in Table 3-1. For more information about HVE Variable Output parameters, refer to the HVE User's Manual, Chapter 16, Event Model.

!!! note "HVE Studio"
    The same variables are chosen in **Output › Variable Selection…** (the **Select Output Variables** dialog, searchable by name or group, for example "Kinematics" or "Tire") and shown in **Output › Key Results…**; **Output › Output Graph…** plots variables chosen with its own **Select Variables…** button. Values follow the units set in **Tools › Preferences**. A channel that EDVDS does not compute carries "(not computed)" in its name.

**Table 3-1: Vehicle Variable Output Data**

| Parameter | Description |
|---|---|
| Vehicle Kinematic Data | X,Y,Z position of CG; $\Phi,\Theta,\Psi$ orientation; Total linear velocity, u,v,w components; Sideslip, course angles; p,q,r angular velocity; Total linear accel, fwd, side, vert components; u-dot, v-dot, w-dot linear components; p-dot, q-dot, r-dot angular components |
| Kinetic Data | $\Sigma F_x$, $\Sigma F_y$, $\Sigma F_z$ (Suspension); $\Sigma M_x$, $\Sigma M_y$, $\Sigma M_z$ (Suspension); $\Sigma F_x$, $\Sigma F_y$, $\Sigma F_z$ (Connection); $\Sigma M_x$, $\Sigma M_y$, $\Sigma M_z$ (Connection) |
| Accelerometer Data | Total linear acceleration; forward, lateral, vertical components for each accelerometer |
| Tire Data | X,Y,Z position of tire contact patch; $F_x'$, $F_y'$, $F_z'$ of tire contact patch; Loaded Tire Radius; Longitudinal Slip; Slip Angle; Skid Flag |
| Wheel Data | x,y,z location of wheel; Camber, Steer angle of wheel; Wheel Spin Velocity; $F_x$, $F_y$, $F_z$ of wheel; Jounce/Rebound displacement, velocity; Spring, Damping and Anti-pitch Suspension Force; Drive and Brake Torque at wheel; Brake Pressure at wheel |
| Connection Data | Articulation roll, pitch, yaw; Articulation p,q,r angular velocity; Articulation p-dot, q-dot, r-dot angular acceleration; Connection $F_x$, $F_y$, $F_z$; Connection $M_x$, $M_y$, $M_z$ |
| Drivetrain Data | Engine Speed, Power and Torque; Transmission and Differential Numeric Ratio |
| Driver Data (*) | Steering wheel angle; Throttle position; Brake Pedal Force and Master Cylinder Pressure; Transmission and Differential Gear Selection |

(*) If Driver Control option was 'At Driver'


## Trajectory Simulations

EDVDS produces a trajectory simulation of the current event. The trajectory simulation is a 3-D visualization of the data displayed in the Variable Output table (see previous section).

*Figure 3-8 of the printed manual, a screenshot of HVE's trajectory simulation viewer, is not reproduced. In HVE Studio the trajectory plays in the Event editor's viewport (Figure 2-5 shows that editor).*

### Displaying a Trajectory Simulation

In HVE Studio the trajectory is played back in the Event editor's viewport as soon as the event has been run. It is controlled with the playback bar under the viewport (Figure 3-9):

- **|<** — Jump to the start of the simulation
- **<<** / **>>** — Step back / forward one output step
- **Play** / **Pause** — Play the simulation forwards, or pause it
- **>|** — Jump to the end of the simulation
- **Reset** — Clear the results (the event can then be edited and run again)

There is no reverse-play button. **Output › Playback Options…** sets the playback rate and frame step, and the **Playback (F6)** editor plays several events in sequence. The camera list on the bar (*Free view* by default) selects a saved camera; see **Tools › Cameras**.

![Figure 3-9](images/hvn-playback-bar.png)
*Figure 3-9: The HVE Studio playback bar.*

<!-- NAV -->

---

← Previous: [Chapter 2 — EDVDS Program Input](02-program-input.md)  |  [Index](README.md)  |  Next: [Chapter 4 — Calculation Method](04-calculation-method.md) →

<!-- /NAV -->
