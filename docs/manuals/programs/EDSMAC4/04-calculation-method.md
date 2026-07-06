# Chapter 4 — Calculation Method

## Basis for Analysis

EDSMAC4 is a dynamic analysis of a crash sequence involving one or more vehicles. The program uses a tire model to calculate forces acting on the vehicle at the tire-road interface. If contact between vehicles is detected, collision forces are also computed. Newton's laws of motion are solved at discrete, user-entered time steps for each vehicle. The resulting accelerations are integrated to update the position and velocity at the end of each time step.

The mathematical model for EDSMAC4 was extended from EDC's EDSMAC model, which, in turn, was developed from the SMAC model originally developed and validated at Calspan [1-5, 11-13]. Extensions provided by EDC are explained in references 6, 7, 23 and 24.

To use EDSMAC4 successfully, a good understanding of vehicle dynamics is extremely useful and is recommended. However, the following discussion is limited to the general analytical approach. The discussion describes the solution procedure while the vehicles are in contact during the collision phase and while they are separated (before and after impact) during the trajectory phases. For a detailed treatise on the subject of vehicle dynamics and simulation programs, the user is referred to the references listed at the end of this manual ([Chapter 7](07-references.md)) as well as those listed in the User's Manual, Appendix VI.

### Equations of Motion

EDSMAC4 is a 3-degree-of-freedom analysis. Vehicle motion is calculated in the earth-fixed X and Y directions and rotation about the vertical Z axis. The vector velocity (amplitude and direction) is resolved in the vehicle-fixed coordinate system by resolving its components along the vehicle's forward (u-velocity) and lateral (v-velocity) directions. For more information, refer to SAE J670e — Vehicle Dynamics Terminology.

The required equations of motion, applicable to each vehicle, are:

$$\Sigma F_x = m(\dot{u} - vr)$$

$$\Sigma F_y = m(\dot{v} + ur)$$

$$\Sigma M_z = I_z \dot{r}$$

where:

- $m$ = mass
- $I_z$ = yaw moment of inertia
- $u$ = forward velocity
- $v$ = lateral velocity
- $r$ = angular yaw velocity about the z axis
- $\Sigma F_x$ = summation of external forces in the vehicle-fixed x-direction
- $\Sigma F_y$ = summation of external forces in the vehicle-fixed y-direction
- $\Sigma M_z$ = summation of external moments about the vehicle-fixed z axis

EDSMAC4 solves these equations of motion at discrete, user-entered time intervals (see Simulation Controls, Timesteps), then uses numerical integration to advance to the next time step, and the calculations are repeated.

There are no degrees of freedom (and hence, no equations of motion) for vertical translation nor pitch or roll rotation. Thus, roll, pitch and vertical accelerations are ignored.

In HVE, at each time step, the vehicle's roll, pitch and CG elevation are computed using `GetSurfaceInfo()` [25]. This approach allows the vehicle to sense when it is on a grade, and the equations of motion account for the grade. Surface slopes up to about 15 degrees are allowed (a message will be issued if this angle is exceeded). Thus, vehicle motion on hills, super-elevations, road crowns and even sloped shoulders may be modeled using EDSMAC4.

*(updated: the current version also includes an optional dynamic **steer degree of freedom** — when enabled via the Steer DOF calculation option, wheel steer angles are computed from the torques acting on the steering system (tire friction, steering stops, gyroscopic precession, steering column friction) instead of being read directly from the driver steer tables; see [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md#steer-dof).)*

### Collision Phase

The EDSMAC4 collision model is described in detail in reference 23.

During the collision phase, each vehicle's crush perimeter is described by a set of radial RHO vectors extending from the CG to the vehicle exterior, spaced at the user-entered Vector Spacing angle (`DELPSI`, default 2 degrees). When the perimeters of two vehicles overlap, the collision routine iteratively adjusts the lengths of corresponding RHO vectors (in increments of `DELRHO`) until force equilibrium between the two vehicles is achieved within the Vector Force Tolerance (`ALAMB`). Collision forces are computed from the A and B stiffness coefficients of the crushed surfaces; friction forces tangent to the crush surface are computed using the inter-vehicle friction coefficient (`AMU`, set per vehicle pair in the Vehicle Mesh dialog), reduced linearly below the minimum sliding velocity `ZETAV`. Restitution is applied using the parametric model with coefficients $C_0$, $C_1$ and $C_2$. *(This paragraph summarizes the algorithm implemented in `Physics/Source/Edsmac4/Coll2.cpp`; see references 21–23 for the full derivation.)*

### Trajectory Phase

All of the external forces applied to the vehicle which direct its motion during the pre- and post-impact phases are applied at the tires.

> **NOTE:** The tire forces continue to exist during the collision phase.

Accurate computation of the tire forces is essential. Unfortunately, pneumatic tires do not behave in an easy-to-calculate manner. Rather, these properties are functions of several variables, and are extremely non-linear.

In order to calculate tire forces, EDSMAC4 uses the Fiala tire model [10]. This model has seen use in many popular simulations, and is used in EDSVS, EDVTS, and EDCRASH. The user supplies the tire cornering stiffness, $C_\alpha$, and tire/road slide friction data. The friction may be velocity dependent. A friction circle is used to limit longitudinal and lateral tire forces during combined braking and steering.

EDSMAC4 allows the vehicle to accelerate, brake and steer. The attempted acceleration, braking and steering are supplied by the user in tabular form using the Event Editor. It is important to understand these driver controls result in *attempted* forces; the Fiala tire model determines if these forces are sustainable at the tire-road interface and accounts for the condition if the available force is exceeded.

EDSMAC4 models quasi-static longitudinal and lateral load transfers. This is accomplished by applying the current inertial longitudinal and lateral forces at the vehicle's CG elevation, thus producing a pitch and/or roll moment. Lateral load transfer is apportioned to the front and rear axles using the vehicle's roll couple distribution. Roll couple distribution is primarily a function of the front-to-rear lateral stiffness ratio of the front and rear suspensions.

EDSMAC4's vehicle model allows the user to study vehicles with tandem axles and dual tires.

*(updated: when the **Hydroplane Model** calculation option is set to NASA, the available tire friction and rolling resistance are further modified at each tire travelling over a water polygon, based on water depth, tire inflation pressure and the tire's hydroplaning speed; see `Physics/Source/Edsmac4/Hydroplane.cpp` and [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md#hydroplane-model).)*

## Assumptions

In order to provide a useful analysis without becoming burdensome and overly complex, EDSMAC4 makes several simplifying assumptions. If the user is to use EDSMAC4 properly, it is important these assumptions and their consequences be understood. In some cases, data which violate these assumptions will cause a fatal error, along with a message indicating the reason for the error. In other cases, the error is not with the data but with the use of the program under conditions which violate the assumptions inherent to the computations. EDSMAC4 will issue results which may not be valid for the circumstances of the accident. Before using EDSMAC4, be sure your accident is within the scope of EDSMAC4's original design.

A thorough list of assumptions and how to properly use the program can be found in the References [1-7, 11-13, 15]. Some of the major program assumptions are defined below.

### Surface Slope Up To 15 Degrees

The HVE physical environment allows EDSMAC4 to consider the general effects of roll and pitch, up to about 15 degrees (the limit is the result of the small angle assumption). Negotiating slopes within this range is generally well modeled. However, traveling off an embankment is completely beyond the scope of EDSMAC4.

### No Rollover Allowed

EDSMAC4 is a 3-degree-of-freedom analysis and does not consider roll or pitch degrees of freedom. If a vehicle rolls over, the equations of motion that apply during the trajectory phases no longer apply, since forces are no longer applied at the tires but are applied between the vehicle exterior and road. EDSMAC4 makes no provision for this condition.

### All External Forces Applied at Tires

Other than during the collision, all forces which affect vehicle motion are applied at the tire/road interface. Aerodynamic effects are ignored. This assumption may become a factor at excessive speeds. In addition, forces caused by contact between the undercarriage and ground (sometimes resulting from impact damage) are not considered.

### Homogeneous Vehicle Exterior

The collision phase analysis assumes there is a linear force vs crush relationship for each vehicle surface (front, sides or rear). The stiffness is assumed to be uniform for the entire surface. This means, for example, that the side stiffness is the same at the front fender, wheels, bumpers, doors and quarterpanel.

---
*Previous: [Chapter 3 — Program Output](03-program-output.md) — Next: [Chapter 5 — EDSMAC4 Tutorial](05-tutorial.md)*

<!-- NAV -->

---

← Previous: [Chapter 3 — EDSMAC4 Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDSMAC4 Tutorial](05-tutorial.md) →

<!-- /NAV -->
