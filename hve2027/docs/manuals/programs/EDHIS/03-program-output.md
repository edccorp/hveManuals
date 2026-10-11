# Chapter 3 — EDHIS Program Output

This chapter defines the outputs available from an EDHIS event. In HVE 2027 the reports produced by EDHIS are on the **Output** menu once the event has been run; there is no separate Playback Editor.

## Overview

EDHIS produces four types of output reports:

- **Alpha-Numeric Reports** — Reports containing text and numeric information, such as vehicle dimensional parameters
- **Graphic Reports** — Reports containing static, visual data, such as vehicle damage profiles
- **Variable Output Tables** — Reports containing tabular simulation results as a function of time
- **Trajectory Simulations** — Viewers containing dynamic, 3-D visual simulations

!!! note "HVE 2027"
    In HVE 2027 the four kinds of output are reached as follows:

    | Output | HVE 2027 |
    |---|---|
    | Alpha-numeric reports | **Output › HVE Reports** — EDHIS's own report pages, one tab each |
    | Graphic reports | (EDHIS produces none) |
    | Variable output | **Output › Key Results** and **Output › Output Graph**, for the vehicle's and the occupant's variables (chosen in **Output › Variable Selection**); **Timestep Data Table** and **Variable Report** for the vehicle — see [Variable Output Table](#variable-output-table) |
    | Trajectory simulation | the 3-D viewport, with the playback bar |

    There is no printing from HVE 2027. **Save This Page** and **Save All Pages** in the HVE Reports window write the report text to a file you can print or attach.

To view the EDHIS reports in HVE 2027:

1. Run the EDHIS event (see [Chapter 2, Executing An Event](02-program-input.md#executing-an-event)).
2. Choose **Output › HVE Reports**. The *HVE Reports* window shows the pages EDHIS built during the run, one tab per report, headed by the engine, the event and the number of pages.
3. Click a tab to read that report. To keep it, enter a file name and click **Save This Page**, or **Save All Pages** for every page in one file.

The pages are built by the engine itself from its own report text, so they read as EDHIS's reports read in HVE. If the run was refused or aborted, the window says that no pages were built.

## Alpha-Numeric Reports

EDHIS produces the following alpha-numeric reports:

- **Messages** — A list of messages produced by the current run
- **Accident History** — A table of initial and final positions and velocities
- **Event Data** — A series of tables of the collision pulse, contact inhibition, airbag and belt data
- **Human Data** — A series of tables containing the human data used by EDHIS
- **Injury Data** — A table containing the injury tolerances, followed by a table containing values exceeding the allowable tolerances during the current run
- **Vehicle Data** — A series of tables containing the vehicle data used by EDHIS
- **Program Data** — A table containing program control information for the current run

An example of each of these numeric output reports from EDHIS is shown below.

### Messages

A typical Messages Report simply lists any messages produced by the run (often "No Messages"). For a complete listing of messages issued by EDHIS, see [Chapter 6](06-messages.md).

!!! note "HVE 2027"
    The run's outcome is also summarized in the run status shown in the Simulation panel and Key Results — for an EDHIS run, the peak head and torso accelerations and the number of injury tolerances exceeded — together with any input HVE 2027 had to supply or could not pass on (for example, a missing collision pulse or occupant contact pairs that were left untested).

### Accident History

The Accident History Report displays a table of initial and final positions and velocities for the human and vehicle. The table includes linear position (x, y, z, in) and velocity (mph) columns and angular position (deg: yaw, pitch, roll) and velocity (deg/sec) rows for the Vehicle and for the human Torso, Head and Legs segments.

> **NOTE:** **Output › Accident History Report** opens HVE Reports on this EDHIS page; there is no separate HVE 2027 accident history.

### Human Data

The Human Data Report includes the following information:

- **Segment Properties** — Inertial properties and joint locations for the Head, Torso and Leg segments.
- **Joint Properties** — Elastic, damping and stop angles for the Neck and Hip joints
- **Ellipsoid Properties** — Name, Segment, center coordinates and semi-axis lengths for each human ellipsoid


### Event Data

- **Collision Pulse** — Linear and angular acceleration pulse applied to the vehicle.
- **Contact Inhibitions** — Ellipsoid-to-Contact Surface contacts that are inhibited during the event.
- **Airbag Event History** — Airbag inflation, contact, and collapse parameters and steering column collapse parameters
- **Belt Event History** — Belt attachment points, slack, and contacts


### Injury Data

The Injury Data Report includes the following information:

- **User-assigned Injury Tolerances** — Human tolerances to impact injury.
- **User-assigned Joint Range** — Human range of normal motion for the Neck and Hip joints
- **Predicted Injuries** — Table of injury tolerances that were exceeded, the maximum value achieved, and the time interval during which the value exceeded the tolerance.

The tolerances listed include Head Injury Criterion (HIC), Head Pitch Concussion (deg/sec²), Head Side Acceleration (g), Chest Force (lb), Chest A-P Acceleration (g), Chest Severity Index, Axial Femur Load (lb), Torso Belt Load (combined, lb) and Lap Belt Load (combined, lb). *(updated: in the current human model the torso and lap belt tolerances are held separately for the left and right belt sections, rather than as the single combined values shown in the original report figure.)*

> **NOTE:** Three of these headings are narrower than their names suggest, and [Chapter 4](04-calculation-method.md#injury-measures) gives the quantity behind each one. In summary: *Head Injury Criterion* is a Gadd severity index accumulated over the whole run from the fore-aft component of head acceleration, not the FMVSS 208 sliding-window HIC; *Chest Severity Index* is the superior-inferior (vertical) chest acceleration, not a severity index; and *Axial Femur Load* is the largest contact force on the knee ellipsoid, not a load computed within the femur. Compare each reported value against the tolerance carried by the human, which is expressed on the same basis. The Joint Injury table lists maximum range of motion (flexion and extension, in degrees) for yaw, pitch and roll of the Neck and Hip joints. The Predicted Injuries table lists each exceeded quantity, its peak value, and the start time, end time and duration of the interval during which the tolerance was exceeded.


### Vehicle Data

The Vehicle Data Report includes the following information:

- **Contact Surface Properties** — Name, elastic and damping properties, penetration limit, edge constant, maximum force, unloading slope and relative initial position of the human with respect to the contact surface.
- **Contact Surface Location** — Name and corner coordinates for each contact surface.
- **Belt Restraints** — If in use, this section displays the name, location and mechanical properties for each installed belt segment. In addition, this section also displays the human attachment point and initial belt slack.
- **Airbag Restraints** — If in use, this section displays the location, mechanical and thermodynamic properties of the airbag, as well as its deployment time and fill duration.


### Program Data

The Program Data Report includes the following information:

- **Simulation Controls** — Integration parameters used for the current event
- **Collision Pulse** — The acceleration vs time history for the current event.
- **Contacts** — A list of all human ellipsoid vs vehicle contact surface interactions that were ignored for the current event.

The General Information section reports the EDHIS Version Number. The Simulation Controls section reports Max Simulation Time, Max Timestep, Output Interval, Starting Method, Predictor-Corrector Method, Velocity Change Limit, Acceleration Change Limit, Min Acceleration, Velocity Convergence Criterion, Maximum Bisections and Time Epsilon.


## Graphic Reports

EDHIS produces no Graphic Output Reports.

> **NOTE:** Graphs of simulation results vs time may be produced using the Variable Output window (see next section). In HVE 2027, **Output › Output Graph**.

## Variable Output Table

EDHIS produces a Variable Output table containing the time-based simulation results. The Variable Output groups produced by EDHIS are as follows:

### Human Output Groups

- **Human Kinematics** — Position, velocity, acceleration and kinetic energy for each human segment
- **Joints** — Articulation angles and torque for the Neck and Hip joints
- **Contacts** — Contact force, deflection and x,y contact coordinate for each human ellipsoid vs vehicle contact impingement
- **Belts** — Belt tension and stretch for each belt segment
- **Airbag** — Airbag pressure, radius, contact force and deflection

### Vehicle Output Groups

- **Vehicle Kinematics** — Position, velocity and acceleration for the vehicle
- **Wheel** — The position of each wheel (required only to visualize the wheels during an event; not used in the calculations)
- **Contacts** — Contact force, deflection and x,y contact coordinate for each human ellipsoid vs vehicle contact impingement
- **Belts** — Belt tension and stretch for each belt segment
- **Airbag** — Airbag pressure, radius, contact force and deflection

> **NOTE:** The Contacts, Belts and Airbag results for Human and Vehicle output groups are identical (Newton's 3rd law at work!)

!!! note "HVE 2027"
    The **human** output groups — Human Kinematics, Joints, Contacts, Belts and Airbag — are offered as variables. In **Output › Variable Selection** they appear as the **Occupant** groups (one per body segment, one per joint, the contacts, belts and airbag) with a check-box column for the occupant (**H1** and the human's name), and from there they can be tabulated in **Output › Key Results**, graphed in **Output › Output Graph** and written by **Output › Export Variables** — see [Selecting Variables](../../11-reports-output/VarSelDlg.md#occupant-variables). Names and units are HVE's own.

    - EDHIS computes three segments — the torso (HVE's *Pelvis* slot), the head and the legs (both upper-leg slots) — so the other segments read **--**, as do EDHIS's unwritten slots: the head's and legs' *Acc Tot* (use **Acc Resultant (from Fwd/Lat/Vert)**, which is the head acceleration the run's *Occ. Peak Head Accel* is taken from).
    - The belt and airbag variables are the restraint at the occupant's seat; EDHIS writes the belt's attachment point, stretch and tension and the bag's pressure, radius, contact force and deployment point.
    - **Timestep Data Table** and **Variable Report** remain vehicle-only.

    Also for the occupant:

    - **Output › Key Results** — *Occ. Peak Head Accel*, *Occ. Peak Torso Accel*, *Occ. HIC (exceedance)* and *Occ. Tol. Exceedances* (rows appear only for an occupant run);
    - the EDHIS report pages in **Output › HVE Reports**, including the Injury Data report and the tolerances exceeded; and
    - the occupant's motion in the 3-D viewport.

A detailed listing of each Variable Output parameter produced by EDHIS is found in Tables 3-1 and 3-2.

**Table 3-1 — Human Variable Output Data**

| Parameter | Description |
|---|---|
| Human Kinematic Data (for Hip, Head and Leg segments) | x, y, z coordinates; $\phi, \theta, \psi$ angles; total velocity, fwd, side, vert components; $\dot\phi, \dot\theta, \dot\psi$ angular velocities; total acceleration, fwd, side, vert components; $\ddot\phi, \ddot\theta, \ddot\psi$ angular accelerations (see note below) |
| Joint Data (for Neck and Hip joints) | $\phi, \theta, \psi$ joint articulation angles; $\phi, \theta, \psi$ joint elastic moments |
| Contact Data (for each human ellipsoid and vehicle contact surface) | Contact surface x,y contact coordinate; Contact Normal Force; Contact deflection |
| Belts (for each belt section) | Belt tension and stretch |
| Airbag | Airbag pressure, radius; Airbag contact force, deflection |

> **NOTE:** For human occupants, the human segment kinematics are defined relative to the vehicle-fixed coordinate system; for human pedestrians, the segment kinematics are defined relative to the earth-fixed coordinate system.

**Table 3-2 — Vehicle Variable Output Data**

| Parameter | Description |
|---|---|
| Vehicle Kinematic Data | X, Y, Z position of CG; $\Phi, \Theta, \Psi$ orientation; total linear velocity, u, v, w components; sideslip, course angles; p, q, r angular velocity; total linear accel, fwd, side, vert components; $\dot u, \dot v, \dot w$ linear components; $\dot p, \dot q, \dot r$ angular components |
| Wheel Data | x, y, z location of each wheel |
| Contact Data (for each human ellipsoid and vehicle contact surface) | Contact surface x,y contact coordinate; Contact Normal Force; Contact deflection |
| Belts (for each belt section) | Belt tension and stretch |
| Airbag | Airbag pressure, radius; Airbag contact force, deflection |

## Trajectory Simulations

EDHIS produces a trajectory simulation of the current event. The trajectory simulation is a 3-D visualization of the data displayed in the Variable Output table (see previous section). In HVE 2027 it plays in the viewport after the run.

![Figure 3-9](images/hvn-edhis-pedestrian.png)
*Figure 3-9: EDHIS trajectory simulation in HVE 2027 — the EDHIS tutorial's pedestrian on the van's hood at t = 0.12 s.*

### Displaying a Trajectory Simulation

The Trajectory Simulation is controlled using the playback bar under the viewport:

- **Reset** — Clears the results (and unlocks the event's inputs for editing).
- **|<** — Jump to the start of the simulation
- **<<** — Step back one output step
- **Play / Pause** — Play the simulation forwards, or pause it
- **>>** — Step forward one output step
- **>|** — Jump to the end of the simulation

> **NOTE:** **Output › Playback Options** sets the playback rate and step. **File › Record Animation** records a movie, and the camera list beside the playback bar chooses the view (or **Tools › Cameras**). **View › Scene Display › Humans Through Bodywork** draws the occupant through the vehicle body.

---
*Previous: [Chapter 2 — Program Input](02-program-input.md) | Next: [Chapter 4 — Calculation Method](04-calculation-method.md)*

<!-- NAV -->

---

← Previous: [Chapter 2 — EDHIS Program Input](02-program-input.md)  |  [Index](README.md)  |  Next: [Chapter 4 — Calculation Method](04-calculation-method.md) →

<!-- /NAV -->
