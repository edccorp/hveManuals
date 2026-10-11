# Chapter 3 — EDVTS Program Output

This chapter defines the outputs available from an EDVTS event. In HVE the reports produced by EDVTS are available in the Playback Editor.

!!! note "HVE 2027"
    HVE 2027 has no Playback Editor and no Report Window Information dialog. After an EDVTS event is run (**Run** on the playback bar, or **Output › Run Simulation…**), its outputs are on the **Output** menu of the Event editor:

    | HVE output | HVE 2027 |
    |---|---|
    | Accident History, Messages, Program Data, Vehicle Data (and Environment Data) | **Output › HVE Reports…** — the pages EDVTS itself builds, one tab per page, with a field and button to save the page as a text file |
    | Variable Output | **Output › Timestep Data Table…**, **Output › Variable Report…** and **Output › Output Graph…**; the variables are chosen in **Output › Variable Selection…**; **Output › Export Variables…** writes them to a file |
    | Key Results | **Output › Key Results…** |
    | Trajectory Simulation | the Event editor's own viewport, driven by the playback bar |

    **Output › Accident History Report…** opens HVE Reports on its ACCIDENT HISTORY tab — the EDVTS page of the same name. There is no Print command; save a report page as text or HTML (**Save This Page**, **Save Page as HTML**), or export variables, and print from another program or a browser.

## Overview

EDVTS produces three types of output reports:

- **Alpha-Numeric Reports** — Reports containing text and numeric information, such as vehicle dimensional parameters
- **Variable Output Tables** — Reports containing tabular simulation results as a function of time
- **Trajectory Simulations** — Viewers containing dynamic, visual simulations

## Alpha-Numeric Reports

EDVTS produces the following alpha-numeric reports:

- **Accident History** — A table of initial and final positions and velocities
- **Messages** — A list of messages produced by the current run
- **Program Data** — A table containing program control information for the current run
- **Vehicle Data** — A series of tables containing the vehicle data used by EDVTS

Examples of these reports from EDC's EDVTS tutorial case, as HVE 2027 shows them in **Output › HVE Reports**, are reproduced below.

!!! note "HVE 2027"
    HVE 2027 shows the pages as plain text in one font, so column alignment depends on the font. EDVTS also builds an Environment Data page. In the Program Data page the HVE Version, EDVTS Version and Date / Time of Execution lines are blank.

### Accident History

The Accident History Report displays a table of initial and final positions and velocities for the vehicle. A typical Accident History Report is shown in Figure 3-1.

The report includes the Total Distance Travelled and Time, followed by Position (X, Y, PSI — and, for the trailer, GAMMA) and Velocity (V-tot, u-vel, v-vel, Yaw Vel — and, for the trailer, Gam Vel) at the Initial and Final positions.

```text
                                    ACCIDENT HISTORY

Total Distance Travelled :   417.39
Time :                       5.2900

                    Position                            Velocity
            ------------------------       -----------------------------------
                X        Y      PSI    V-tot    u-vel    v-vel    Yaw Vel
             (ft)     (ft)    (deg)    (mph)    (mph)    (mph)  (deg/sec)
Initial:   152.66   -47.97   180.00    55.00    55.00     0.00       0.00
Final:    -261.24   -91.85   196.44    50.53    50.52    -1.06       5.15
```
*Figure 3-1: The Accident History page for EDC's EDVTS tutorial event, as shown by Output › HVE Reports in HVE 2027 (U.S. units).*

### Messages

A typical Messages Report is shown in Figure 3-2. For a complete listing of messages issued by EDVTS, see [Chapter 6 — Messages](06-messages.md).

```text
                            MESSAGES

The simulation was terminated because the current roll or pitch
angle exceeded 15 degrees. EDSVS is a quasi-3-D analysis. The
small angle assumption is used.
```
*Figure 3-2: The Messages page for EDC's EDVTS tutorial event, as shown by Output › HVE Reports in HVE 2027. The message text names "EDSVS"; that is the wording of EDVTS's own message file.*

### Program Data

The Program Data Report includes the following information:

- **Simulation Controls** — Integration parameters used for the current event (Max Simulation Time, Trajectory Phase dt, Output Interval, Linear Termination Velocity)

*(updated: In the current version the Program Data report also includes a General Program Information section — HVE Version, EDVTS Version, Date and Time of Execution, Dimension Basis — and General Environment Data / 3-D Environment Terrain Data sections reporting the environment name, gravity constant, 3-D geometry filename, number of polygons, the Get Surface Information method in use, and terrain elevation limits.)*

A typical Program Data Report is shown in Figure 3-3.

```text
                     GENERAL PROGRAM INFORMATION

HVE Version:
EDVTS Version:
Date of Execution:
Time of Execution:
Dimension Basis:    Total Mass CG


                         SIMULATION CONTROLS
Max Simulation Time :  20.0000
Trajectory Phase dt :   0.0200
Output Interval :       0.1000
Linear Term Vel :         2.00
```
*Figure 3-3: The Program Data page for EDC's EDVTS tutorial event, as shown by Output › HVE Reports in HVE 2027.*

### Vehicle Data

The Vehicle Data Report includes the following information:

- **Vehicle Dimensional and Inertial Properties** — The dimensional and inertial parameters used by EDVTS in the current event.

> NOTE: The Total Yaw Inertia adds the effect of the unsprung masses (i.e., the wheel and axle masses) to the unsprung mass; thus, the value printed is greater than the one displayed in the Vehicle Editor's Inertias dialog.

- **Tire Properties** — The tire parameters used by EDVTS in the current event (peak friction, slide friction, slip at peak mu, cornering stiffness and antilock efficiency, per axle, right and left).
- **Driver Tables** — Individual Driver Control tables for steering, braking, throttle and gear selection used by EDVTS in the current event.

A portion of a typical Vehicle Data Report is shown in Figure 3-4. Dimensional entries include Overall Length and Width, CG to Front/Rear End, Wheelbase, Front/Rear Overhang, CG to Front/Rear Axle, Front/Rear Trackwidth, Inter-tandem Distance and Load Transfer, CG Height Above Ground, Connection Height Above Ground, Lateral Load Transfer, Mass, Weight and Yaw Inertia.

In HVE 2027 this page is the **VEHICLE DATA** tab of **Output › HVE Reports**.

!!! note "HVE 2027"
    In the driver tables at the end of this page, the brake table's Time column prints the time of the table's second row on every row. This is how EDVTS's own report code prints it (HVE's source does the same); the table the simulation uses is correct. Check brake-table times in **Event › Driver Controls…**.

## Graphic Reports

EDVTS produces no Graphic Output Reports.

> NOTE: Graphs of simulation results vs time may be produced using the Variable Output window (see next section).

## Variable Output Table

EDVTS produces a Variable Output table containing the time-based simulation results. The Variable Output groups produced by EDVTS are as follows:

### Vehicle Output Groups

- **Kinematics** — Position, velocity and acceleration for the vehicle
- **Kinetics** — Forces and moments at the vehicle CG due to inter-vehicle connections
- **Tire** — The tire output parameters existing at the tire contact patch (compare with Wheel Output, below)
- **Wheel** — The wheel output parameters existing at the wheel's hub. Information about the position of each wheel (compare with Tire output, above)
- **Connections** — The articulation angles and inter-vehicle connection forces
- **Driver** — Current levels of driver inputs (steering, braking, throttle and gear ratios)

A detailed listing of each Variable Output parameter produced by EDVTS is found in Table 3-1. For more information about Variable Output parameters, refer to the User's Manual, Chapter 16, Event Model.

!!! note "HVE 2027"
    The same variables are chosen in **Output › Variable Selection…** (the **Select Output Variables** dialog, searchable by name or group), and shown in **Output › Timestep Data Table…**, **Output › Variable Report…** or **Output › Output Graph…**. Values follow the units set in **Tools › Preferences**. A channel that EDVTS does not compute carries "(not computed)" in its name.

**Table 3-1: Vehicle Variable Output Data**

| Parameter | Description |
|---|---|
| Vehicle Kinematic Data | X,Y,Z position of CG; $\Phi,\Theta,\Psi$ orientation; Path Radius of CG; $\nu$ (Course Angle); Total linear velocity, u,v,w components; Sideslip angle; r angular velocity; Total linear accel, fwd, side components; u-dot, v-dot linear components; r-dot angular components |
| Vehicle Kinetic Data | $F_x$, $F_y$, $F_z$ from Connections about CG; $M_z$ from Connections about CG |
| Tire Data | X,Y,Z position of tire contact patch; Slip Angle; $F'_x$, $F'_y$, $F'_z$; Skid Flag |
| Wheel Data | x,y,z location of each wheel; $F_x$, $F_y$, $F_z$; Steer Angle ($\delta$) at each steerable wheel |
| Connection Data | $\gamma$ Articulation Angle; $F_x$, $F_y$, $F_z$ at Connection |
| Driver Data (*) | Steering wheel angle |

(*) If Driver Control option was 'At Steering Wheel'


## Trajectory Simulations

EDVTS produces a trajectory simulation of the current event. The trajectory simulation is a visualization of the data displayed in the Variable Output table (see previous section).

*Figure 3-6 of the printed manual, a screenshot of HVE's trajectory simulation viewer, is not reproduced. In HVE 2027 the trajectory plays in the Event editor's viewport (Figure 2-4 shows that editor).*

### Displaying a Trajectory Simulation

In HVE 2027 the trajectory is played back in the Event editor's viewport as soon as the event has been run. It is controlled with the playback bar under the viewport (Figure 3-7):

- **|<** — Jump to the start of the simulation
- **<<** / **>>** — Step back / forward one output step
- **Play** / **Pause** — Play the simulation forwards, or pause it
- **>|** — Jump to the end of the simulation
- **Reset** — Clear the results (the event can then be edited and run again)

There is no reverse-play button. **Output › Playback Options…** sets the playback rate and frame step, and the **Playback (F6)** editor plays several events in sequence. **File › Record Animation…** makes a movie file.

![Figure 3-7](images/hvn-playback-bar.png)
*Figure 3-7: The HVE 2027 playback bar.*

---

[Previous: Chapter 2 — Program Input](02-program-input.md) | [Contents](README.md) | [Next: Chapter 4 — Calculation Method](04-calculation-method.md)

<!-- NAV -->

---

← Previous: [Chapter 2 — EDVTS Program Input](02-program-input.md)  |  [Index](README.md)  |  Next: [Chapter 4 — Calculation Method](04-calculation-method.md) →

<!-- /NAV -->
