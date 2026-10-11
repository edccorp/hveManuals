# Calculation Options for EDHIS

EDHIS (Engineering Dynamics Corporation Human Impact Simulator) is a 3-D analysis of the response of a human occupant or pedestrian during a motor vehicle collision. EDHIS is based on the HSRI-3D model developed at the University of Michigan Transportation Research Institute, and includes several extensions and refinements produced by Engineering Dynamics Corporation. The model was developed as a tool to study advanced safety concepts and designs of seat restraint systems from the viewpoint of occupant protection. EDHIS employs airbag and belt (torso and lap) models useful for studying issues related to restraint system effectiveness. EDHIS is useful for predicting and visualizing occupant and pedestrian motion during impact. The model also provides important injury predictions, including HIC, Chest SI and Maximum Femur Load.

EDHIS computes human kinematics (position, velocity and acceleration vs. time), joint angles and torques, and contact force between the human and vehicle.

The EDHIS human model includes 12 degrees of freedom. The human is represented by three inertial segments (head, torso and lower extremities) and 2 joints (neck and hip). The body is visualized using the HVE 15-segment, 14-joint model by combining the head and neck into a single segment called the head; the HVE pelvis, abdomen and chest are combined to form the EDHIS torso; and the right and left upper legs, lower legs and feet are combined to form the lower extremities. 3-D ellipsoids may be attached to any of these three segments to sense force-producing interactions with the vehicle interior or exterior.

The motion of the vehicle is defined by a 6 degrees-of-freedom collision pulse (acceleration vs. time history). The vehicle has attached to it a number of planar contact surfaces that may be arranged to form interior surfaces, such as seats, dashboards and windshields, and exterior surfaces, such as bumper, grill, hood and windshield. Forces are applied to the human whenever interaction is sensed between the human ellipsoids and the vehicle contact surfaces.

The motion and forces resulting from human vs. vehicle interactions are recorded as EDHIS output tracks; the resulting motion is also visualized in the 3-D HVE visualization environment.

## Opening the options

In Event Information, with an EDHIS event active, press **Method Options...**
under Calculation Method. The **EDHIS Options** window has two groups,
*Termination Criteria* and *Integration*.

## Min Acceleration (g)

A deadband: EDHIS sets to zero any segment acceleration whose magnitude is at or below this value, suppressing numerical noise in the solution. It is entered in **g**. Zero (the default, and HVE's) switches the deadband off.

## Min Time Criterion (s)

The minimum time precision (time epsilon) used by the integration and output control logic. The field is **greyed**: EDHIS overwrites it with 1.0e-7 s unconditionally after reading it, so no entered value can take effect — in HVE either. The stored value is kept for file fidelity.

!!! note "HVE 2027"
    HVE's help described these two entries as interchanged in its release. In
    HVE 2027 **Min Acceleration** is the acceleration deadband and nothing else,
    and the minimum time criterion is always 1.0e-7 s.

## Start Method

How the numerical integration starts, i.e. how the solution history points required before the predictor-corrector method can take over are generated:

- **Euler** — simple first-order Euler integration.
- **Runge-Kutta (Ralston)** — HVE's *Modified Runge-Kutta*.
- **Runge-Kutta** — classical Runge-Kutta integration.

## Predictor-Corrector

The predictor-corrector method used for the main integration once four starting points are available (below four points EDHIS uses Adams whatever this says):

- **Adams** — HVE's *Adams-Moulton*.
- **Milne** — HVE's *Milne-Hamming*.

!!! note "HVE 2027"
    A new EDHIS event in HVE 2027 starts with **Euler** and **Adams**, not
    HVE's dialog defaults of Modified Runge-Kutta and Milne-Hamming; these are
    the settings HVE's own saved EDHIS tutorial run used. A case imported from
    an HVE file also starts with Euler and Adams; check them against the HVE
    case if it used other methods. The two choices are separate controls, so
    any start method can be combined with either corrector.

## Other settings EDHIS reads

- The simulation controls, including **Maximum Bisections**, **Velocity
  Convergence**, **Velocity Change Limit** and **Acceleration Change Limit** —
  see [Simulation Controls](../09-events-driver-controls/SimuCtrlDlg.md).
- The collision pulse, which EDHIS reads as an **acceleration** table only — see
  [Collision Pulse](../11-reports-output/ColPulse.md).

<!-- NAV -->

---

← Previous: [EDVTS Calculation Options](CalcOptEDVTS.md)  |  [Index](README.md)

<!-- /NAV -->
