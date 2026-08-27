# Calculation Options for EDHIS

EDHIS (Engineering Dynamics Corporation Human Impact Simulator) is a 3-D analysis of the response of a human occupant or pedestrian during a motor vehicle collision. EDHIS is based on the HSRI-3D model developed at the University of Michigan Transportation Research Institute, and includes several extensions and refinements produced by Engineering Dynamics Corporation. The model was developed as a tool to study advanced safety concepts and designs of seat restraint systems from the viewpoint of occupant protection. EDHIS employs airbag and belt (torso and lap) models useful for studying issues related to restraint system effectiveness. EDHIS is useful for predicting and visualizing occupant and pedestrian motion during impact. The model also provides important injury predictions, including HIC, Chest SI and Maximum Femur Load.

EDHIS computes human kinematics (position, velocity and acceleration vs. time), joint angles and torques, and contact force between the human and vehicle.

The EDHIS human model includes 12 degrees of freedom. The human is represented by three inertial segments (head, torso and lower extremities) and 2 joints (neck and hip). The body is visualized using the HVE 15-segment, 14-joint model by combining the head and neck into a single segment called the head; the HVE pelvis, abdomen and chest are combined to form the EDHIS torso; and the right and left upper legs, lower legs and feet are combined to form the lower extremities. 3-D ellipsoids may be attached to any of these three segments to sense force-producing interactions with the vehicle interior or exterior.

The motion of the vehicle is defined by a 6 degrees-of-freedom collision pulse (acceleration vs. time history). The vehicle has attached to it a number of planar contact surfaces that may be arranged to form interior surfaces, such as seats, dashboards and windshields, and exterior surfaces, such as bumper, grill, hood and windshield. Forces are applied to the human whenever interaction is sensed between the human ellipsoids and the vehicle contact surfaces.

The motion and forces resulting from human vs. vehicle interactions are recorded as EDHIS output tracks; the resulting motion is also visualized in the 3-D HVE visualization environment.

The EDHIS Calculation Options dialog controls the numerical integration method and two numerical thresholds, described below.

## Numerical Integration Method: Start

This radio button group selects the method used to start the numerical integration, i.e., to generate the solution history points required before the predictor-corrector method can take over. The default is *Modified Runge-Kutta*.

- **Euler** — Simple first-order Euler integration.
- **Modified Runge-Kutta** — Runge-Kutta-Ralston integration. This is the default.
- **Runge-Kutta** — Classical Runge-Kutta integration.

## Numerical Integration Method: Predictor-Corrector

This radio button group selects the predictor-corrector method used for the main integration once enough starting points are available. The default is *Milne-Hamming*.

- **Adams-Moulton** — Adams-Moulton predictor-corrector.
- **Milne-Hamming** — Milne-Hamming predictor-corrector. This is the default.

## Minimum Acceleration

Slider/edit entry for the minimum acceleration threshold. Segment acceleration components whose magnitude is at or below this threshold are set to zero, suppressing numerical noise in the solution. The test is performed only when the value is greater than zero. Default: 0.0000001 (1.0e-7).

## Minimum Time Criterion (sec)

Slider/edit entry for the minimum time precision (time epsilon) used by the integration and output control logic, e.g., when deciding whether the current simulation time has reached the next print time. If entered as 0.0 (the default), EDHIS computes the value automatically from the integration time step and the maximum number of timestep bisections.

Note: in the current release these two entries behave as though they were interchanged — the value entered as *Minimum Acceleration* is applied as the minimum time criterion and the value entered as *Minimum Time Criterion* is applied as the minimum-acceleration threshold — and the minimum time criterion is then reset unconditionally to 1.0e-7. The practical effect is that the minimum time criterion is always 1.0e-7, and the *Minimum Time Criterion* entry is what actually sets the minimum-acceleration threshold (with the acceleration-zeroing test disabled at its 0.0 default).

---
*Updated to match the current version of HVE.*

<!-- NAV -->

---

← Previous: [EDVTS Calculation Options](CalcOptEDVTS.md)  |  [Index](README.md)

<!-- /NAV -->
