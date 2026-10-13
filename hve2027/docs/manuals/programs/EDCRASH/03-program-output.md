# Chapter 3 — EDCRASH Program Output

This chapter defines the outputs available from an EDCRASH event. In HVE the reports are available in the Playback Editor; in HVE 2027 they are on the **Output** menu once the event has been run.

## Output Overview

EDCRASH produces two types of output reports:

- **Alpha-Numeric Reports** — Reports containing text and numeric information, such as vehicle dimensional parameters
- **Graphic Reports** — Reports containing static visual information, such as momentum diagrams and damage profiles

To view the alpha-numeric reports in HVE 2027:

1. Run the event (Chapter 2, Executing an Event).
2. Choose **Output › HVE Reports...**. The **HVE Reports** window shows the pages EDCRASH built during the run, one tab per report: **ACCIDENT HISTORY**, **DAMAGE DATA**, **EVENT DATA**, **MESSAGES**, **PROGRAM DATA**, **REFERENCES** and **VEHICLE DATA**.
3. Click a tab to show that report.

The pages are EDCRASH's own, built from its resource strings in HVE's layout and in HVE's units. They describe the most recent run of the active event.

!!! note "HVE 2027"
    - **Printing.** HVE 2027 does not print. **Save This Page** writes the
      page shown to the text file named in the field beside it (default
      `hve_report.txt`); **Save All Pages** writes every page to that file.
      A name without a folder is saved beside the case file (in the folder
      the program was started from for a case never saved), and the line
      under the buttons shows the full path.
    - **Key Results.** The **Key Results** panel (View › Key Results, docked
      under the viewport by default) lists the principal results for both
      vehicles in the units set in Tools › Preferences: impact speed,
      initial (begin braking) velocity, delta-V, PDOF, impact force, damage
      energy, separation speed and angular velocity, brake deceleration and
      impact sideslip. **Select Variables...**, **Export CSV...** and
      **Copy CSV** are in its **Trajectory** section.
    - **Output › HVE Reports...** (its **ACCIDENT HISTORY** tab) shows the
      EDCRASH page described below. Save it with
      **Save This Page** or **Save Page as HTML**.
    - If the run is refused, the HVE Reports window says so, and the reason
      (with the EDCRASH stop code) is in the run status on the Simulation
      panel.

## Alpha-Numeric Reports

EDCRASH produces the following alpha-numeric reports:

- **Accident History** — A table of initial and final positions and velocities computed by EDCRASH; also includes restitution information
- **Damage Data** — A table of damage-based results produced by EDCRASH
- **Event Data** — A table of all the user-entered scene data used by EDCRASH
- **Messages** — A list of messages produced by the current run
- **Program Data** — A table containing program control information for the current run
- **Vehicle Data** — A series of tables containing the vehicle data used by EDCRASH

### Accident History

The Accident History Report displays a table of initial and final positions and velocities for the vehicle.

![Figure 3-1](images/hvn-edcrash-report-accident-history.png)

*Figure 3-1: Accident History report in HVE 2027's HVE Reports window (EDCRASH Tutorial case).*

- **Begin Braking** — Total velocity, forward and lateral velocity components, and sideslip angle for each vehicle for which a begin braking position was given.
- **Impact** — Total velocity, forward and lateral velocity components, and sideslip angle for each vehicle at impact.

  > **NOTE:** The total velocity is the vector sum of the forward and lateral components, i.e.: $\vec{V} = \vec{V}_{fwd} + \vec{V}_{lat}$

  > **NOTE:** A sideslip angle greater than +90 degrees or less than −90 degrees implies the vehicle is moving backwards (i.e., the forward velocity component is negative) at impact.

  Next to "Impact Velocity" is the basis for results. It specifies which delta-V calculation method (damage or linear momentum) was used in the computation of impact speed. For collinear impact, the results will be based on impact-to-rest phase calculations (trajectory) and vehicle damage. Otherwise, the results will be based on trajectory and the conservation of linear momentum.

- **Delta-V** — The change in velocity and forward and lateral components of velocity change for each vehicle due to the collision. Also, Principal Direction of Force, PDOF.

  If the collision was collinear, only the damage-based delta-V will be displayed. If the collision was oblique, a delta-V computed from scene data (i.e., linear momentum) will be displayed in addition to the damage-based delta-V.

  > **NOTE:** If a fatal error occurred, impact speed will not be reported; the calculated results will be limited to the damage-based delta-V.

  When the momentum solution is used, two important means of helping to ensure valid results are available (see also Warning Messages):

  - the delta-V computed by momentum should be approximately equal to (within ±10% of) the delta-V computed by damage
  - the value of the momentum-based PDOF should be approximately equal to (within ±10% of) the damage-based PDOF

- **Separation Velocity** — Total velocity, forward and lateral velocity components, and sideslip angle for each vehicle at separation.

  > **NOTE:** Separation velocity is only computed when scene data are entered (see Calculation Method).

- **Relative Velocity** — The closing velocity of the vehicles at impact and the coefficient of restitution.

  By definition, the relative velocity is computed in a direction defined by the line between the vehicle CGs. The coefficient of restitution should be positive (a negative value results in a warning message; see Warning Messages).

### Damage Data

The Damage Data Report includes the following information:

- **CDC** — User-entered Collision Deformation Classification for each vehicle.
- **PDOF** — User-entered Principal Direction of Force for each vehicle. This is the direction in which the peak collision force (see below) acts.
- **Damage Width** — User-entered Damage Width for each vehicle.
- **Crush Depths** — User-entered Crush Depths for up to nine crush zones on each vehicle.
- **Damage Midpoint Offset** — User-entered distance from the vehicle CG to the middle of the damage region for each vehicle.
- **Damage Energy** — The calculated damage energy for each vehicle.

  The energy dissipated by damage is based on the damage data (damage profile and crush stiffness coefficients) and not on the conservation of energy. A check for agreement with the conservation of energy is performed. If the results are not consistent, a warning message is issued (see Messages). This is also an important means of helping to ensure valid results.

- **Peak Collision Force** — The calculated peak collision force for each vehicle. The peak collision force acts through the impulse center in the direction of the PDOF.
- **Moment Arm of PDOF** — Perpendicular distance from the vehicle CG to the peak collision force.

  > **NOTE:** A positive moment arm produces clockwise rotation; a negative moment arm produces counter-clockwise rotation. These directions should normally be consistent with the user-entered rotation directions. Otherwise a warning message will be issued (see Warning Messages).

- **Impulse Center** — The vehicle-fixed x,y coordinates for the center of impulse for each vehicle.

  The impulse center is calculated from the summation of forces and moments acting on the vehicle. The peak collision force acts through the impulse center in the direction of the PDOF.

  > **NOTE:** For a homogeneous vehicle (i.e., equal stiffness coefficients in all crush zones), the impulse center is the same as the damage centroid.

![Figure 3-2](images/hvn-edcrash-report-damage-data.png)

*Figure 3-2: Damage Data report (EDCRASH Tutorial case).*

### Event Data

The Event Data Report includes the following scene information for each vehicle if scene data were entered:

- **Impact Information** — The user-entered impact position and orientation for each vehicle. Also includes angular velocity and sideslip angle at impact.

  > **NOTE:** The angular rotation rate at impact will always be zero.

  > **NOTE:** For collinear collisions, the pre-impact sideslip angle may be modified by EDCRASH to be consistent with the user-entered PDOFs and calculated separation velocities. If the modified sideslip angles are inconsistent with other information, you should carefully review, and perhaps modify, the PDOFs and/or departure angles.

- **Separation Information** — The separation position and orientation for each vehicle. Also includes departure angle and separation linear and angular velocities at separation.

  > **NOTE:** The separation positions and headings are identical to the impact positions and headings — the result of assuming a quasi-instantaneous impact.

  Separation linear and angular velocities are displayed in the vehicle-fixed coordinate system (the forward and lateral velocity components are relative to the vehicle heading). The separation angle of the velocity vector (or departure angle) is relative to the earth-fixed coordinate system and is the angle used by the momentum analysis to establish the momentum-based delta-V.

  The separation velocities are the results of the impact-to-rest phase computations (see Calculation Method). If no rotational or lateral skidding was specified, the angular velocity will be zero and the linear velocity will be based on simple energy relationships. Otherwise, special calculations will be performed which account for simultaneous linear and angular velocity. If a trajectory simulation has been performed, the linear and angular velocities may be modified if the simulation did not converge on the first run.

- **Point-on-curve (POC) Information** — The user-entered X,Y POC position for each vehicle (if entered).

  > **NOTE:** When a Separation position is entered (HVE 2027 passes it to EDCRASH), the separation position and heading are the entered ones rather than the impact values.
- **End-of-rotation (EOR) Information** — The user-entered X,Y EOR position and orientation for each vehicle (if entered).
- **Final/Rest Information** — The user-entered final/rest position and orientation for each vehicle. Also includes final velocity.

![Figure 3-3](images/hvn-edcrash-report-event-data.png)

*Figure 3-3: Event Data report (EDCRASH Tutorial case).*

### Messages

The Messages Report lists all Fatal, Warning and Note messages produced by the current run. For a complete listing of messages issued by EDCRASH, see Chapter 6.

![Figure 3-4](images/hvn-edcrash-report-messages.png)

*Figure 3-4: Messages report (EDCRASH Tutorial case).*

### Program Data

The Program Data Report displays general program control information for the current run, including:

- **EDCRASH Version Number** — The version of the EDCRASH calculation model used for the run.
- **Program Options** — The status (Yes/No) of the Common Velocity Check, Modify Departure Angle, Auto-set Rot/Lat Skid and Include Angular Momentum options, and the selected Separation Velocity Basis (e.g., Normal).
- **Consistency Checks** — The current PDOF Range (deg), Delta-V Range, K.E. Range and Newton's 3rd Law Range values.
- **Trajectory Simulation Results** — If Trajectory Simulation was selected as the Separation Velocity Basis, the convergence results for the simulation are also displayed.

The Program Data report is a useful record of exactly which calculation options (see Chapter 2 and [Calculation Options for EDCRASH](../../10-calculation-options/CalcOptEDCRASHDlg.md)) were in effect for the current event.

![Figure 3-5](images/hvn-edcrash-report-program-data.png)

*Figure 3-5: Program Data report (EDCRASH Tutorial case).*

### Vehicle Data

The Vehicle Data Report includes the following information:

- **Dimensional, Inertial and Crush Stiffness Properties** — The vehicle dimensional, inertial and crush stiffness parameters that were used by EDCRASH in the current event.

  > **NOTE:** The Yaw Inertia value displayed in the Vehicle Data report includes the additional rotational inertia created by the unsprung masses (wheels and axles); thus the value printed is greater than the one displayed in the Vehicle Editor's Inertias dialog.

- **Tire Data** — The tire parameters, cornering stiffness and percent wheel lock-ups used by EDCRASH in the current event.

![Figure 3-6](images/hvn-edcrash-report-vehicle-data.png)

*Figure 3-6: A portion of the Vehicle Data report (EDCRASH Tutorial case).*

## Graphic Reports

EDCRASH produces the following Graphic reports:

- **Damage Profiles** — A plan view of the vehicles showing their damage profiles (damage width, depth and midpoint offset).
- **Momentum Diagrams (Scene and Damage)** — A vector diagram showing the pre-impact and post-impact momentum vectors for each vehicle. The scene-based diagram uses impact velocity calculated from the momentum-based delta-V; the damage-based diagram uses the impact velocity calculated from the damage-based delta-V.
- **Site Drawing** — A static perspective view of the accident site showing the vehicles at their user-entered positions.

!!! warning "Not in HVE 2027"
    HVE 2027 does not produce EDCRASH's graphic reports. EDCRASH sends them
    to HVE as drawing data rather than as report pages, and HVE 2027 does
    not draw them. What it offers instead:

    - **Site drawing.** The viewport outlines each vehicle at every scene
      position that is set (View › Scene Display › Scene Ghosts: None, Outline, Translucent
      vehicle or Both). Use the Top view for a plan.
    - **Momentum.** The viewport's **Momentum** view draws a simple vector
      sketch of each vehicle's impact speed, departure and delta-V from the
      Key Results. It is HVE 2027's own drawing, not EDCRASH's scene or
      damage momentum diagram, and should not be used in their place.
    - **Damage profiles.** The damage width, depths, offset and impulse
      center are listed in the Damage Data report.

The descriptions below are of HVE's reports.

### Damage Profiles

The Damage Profile Graphic Report includes the following information:

- **Plan View** — Vehicle outline and damage profile shown in plan view. The vehicles are drawn to scale (the scale is determined such that the vehicle(s) fit into the allotted space). The damage profile shows the width, crush depths, damage midpoint offset, PDOF, and center of impulse.

The Damage Profiles are very useful for confirming the damage data were entered properly (see Warning Messages). This is extremely helpful in debugging.

### Momentum Diagram

The Momentum Diagram Report includes the following information:

- **Pre-impact and Post-impact Momentum Vectors** — Vectors displayed to scale (the scale is determined by HVE to allow the vectors to fill the viewer) representing each vehicle's momentum (mass × velocity) at the instant before and after the collision.
- **Impulse Vector** — A vector showing the earth-fixed direction of the impulse vector, labeled with an "I".
- **Total Momentum** — A vector showing the total system momentum (before and after impact; they are, of course, the same).

### Site Drawing

The Site Drawing Graphic Report includes the following information:

- **Crash Site Environment** — A user-selectable view (plan or perspective) of the environment where the crash occurred.
- **Vehicle Positions** — The vehicles are displayed at each position supplied for the event.

The Site Drawing is very useful for confirming that the scene data were entered properly (see Warning Messages).

![Scene positions in HVE 2027](images/hvn-edcrash-scene-ghosts.png)

*The EDCRASH Tutorial event in HVE 2027, seen from above after the run: each vehicle at rest, with its Begin Braking and Impact positions outlined (View › Scene Display › Scene Ghosts). The Ford Escort is blue, the Nissan Sentra red.*

---

*Previous: [Chapter 2 — Program Input](02-program-input.md) · Next: [Chapter 4 — Calculation Method](04-calculation-method.md)*

<!-- NAV -->

---

← Previous: [Chapter 2 — EDCRASH Program Input](02-program-input.md)  |  [Index](README.md)  |  Next: [Chapter 4 — Calculation Method](04-calculation-method.md) →

<!-- /NAV -->
