# Chapter 4 — Calculation Method

## Basis for Analysis

EDSMAC is a dynamic analysis of a crash sequence involving one or two vehicles moving in the horizontal (yaw) plane. The program uses a tire model to calculate forces acting on the vehicle at the tire-road interface. If contact between vehicles is detected, collision forces are also computed. Newton's laws of motion are solved at discrete, user-entered time steps for each vehicle. The resulting accelerations are integrated to update the position and velocity at the end of each time step.

The mathematical model for EDSMAC was developed and validated at Calspan [1-5, 11-13]. Extensions provided by EDC are explained in references 6 and 7.

To use EDSMAC successfully, a good understanding of vehicle dynamics is extremely useful and is recommended. However, the following discussion is limited to the general analytical approach. The discussion describes the solution procedure while the vehicles are in contact during the collision phase and while they are separated (before and after impact) during the trajectory phases. For a detailed treatise on the subject of vehicle dynamics and simulation programs, the user is referred to the references listed at the end of this Physics Manual as well as those listed in HVE-2D User's Manual, Appendix VI.

### Equations of Motion

EDSMAC is a 3-degree of freedom analysis. Vehicle motion is calculated in the earth-fixed X and Y directions and rotation about the vertical Z axis. The vector velocity (amplitude and direction) is resolved in the vehicle-fixed coordinate system by resolving its components along the vehicle's forward (u-velocity) and lateral (v-velocity) directions. For more information, refer to SAE J670e — Vehicle Dynamics Terminology, portions of which are found in the Help Index.

The required equations of motion, applicable to each vehicle, are written below:

$$\Sigma F_x = m(\dot{u} - vr)$$

$$\Sigma F_y = m(\dot{v} + ur)$$

$$\Sigma M_z = I_z \dot{r}$$

where:

| Symbol | Meaning |
|---|---|
| $m$ | mass |
| $I_z$ | yaw moment of inertia |
| $u$ | forward velocity |
| $v$ | lateral velocity |
| $r$ | angular yaw velocity about z axis |
| $\Sigma F_x$ | summation of external forces in the vehicle-fixed x-direction |
| $\Sigma F_y$ | summation of external forces in the vehicle-fixed y-direction |
| $\Sigma M_z$ | summation of external moments about the vehicle-fixed z axis |

EDSMAC solves these equations of motion at discrete, user-entered time intervals (see Simulation Controls, Timesteps), then uses numerical integration to advance to the next time step and the calculations are repeated.

There are no degrees of freedom (and hence, no equations of motion) for vertical translation nor pitch or roll rotation. Thus, roll, pitch and vertical accelerations are ignored.

### Collision Phase

The collision phase occurs when interference is detected between the vehicles. This condition is confirmed using simple geometry. Given interference exists, the maximum possible damage range is defined between azimuth vectors, *PSIBPB* and *PSIBPF*. The inter-vehicle force is then computed. The resulting acceleration of each vehicle is computed using Newton's second law (force equals the product of mass and acceleration), and is integrated twice in order to compute the changes in velocity and position.

The procedure for computing the inter-vehicle force is based on the concept of a linear spring. The exterior of each vehicle is surrounded by such springs with the user-entered spring constant, or stiffness.

When the vehicles are in contact, the springs of each vehicle press against each other. From this simple fact, several important observations can be made. First, the force between them is equal (Newton's third law). Second, since the displacement of each spring is proportional to the force, the crush (damage) profile of a given vehicle is defined by the end of its springs. Third, the motion of each vehicle resulting from the forces and moments can be computed. This is all the information EDSMAC needs at a given time step. The results determine how the vehicles respond during the impact phase.

To implement the collision model, the user must provide data which describe the vehicle exterior and control the simulation at each collision time interval.

The vehicle exterior is described by its crush stiffness, $K_v$. This parameter has the properties of a linear spring. However, since the spring properties are distributed around the vehicle exterior, the stiffness spring rate has units of pound per inch of crush depth per inch of crush length. The resulting units for stiffness are lb/in². Note that this is not a true "pressure", since the two-dimensional analysis results in a body exterior that has no vertical dimension and, therefore, has no area. The apparent units of area in the denominator result from the crush depth dimension related to the spring rate, lb/in.

Default values for $K_v$ are assigned to each vehicle and may be edited using the HVE-2D Vehicle Editor. Values for $K_v$ may also be computed from crash test data. The method is described in the literature [14].

> NOTE: When computing $K_v$ from crash test data, remember EDSMAC assumes the force vs deflection curve goes through the origin (i.e., $b_0 = 0$).

Three simulation control parameters are required for the collision model. *DELPSI* is the incremental spacing of each of the springs distributed about the vehicle exterior. The crush displacement of each spring is produced along radial vectors from the vehicle center of gravity to the locations on the original (before damage) vehicle exterior defined by the incremental spring spacing. The force on each vehicle is proportional to the crush displacement. Since the forces on each vehicle must be equal (Newton's third law — for every action there is an equal and opposite reaction), the current crush displacement is adjusted between both vehicles along each of the radial vectors. The user-entered increment of each radial vector adjustment, *DELRHO*, is subtracted from one vehicle and added to the other until the forces on the vehicles are approximately equal.

Because the adjustments are finite increments of crush displacement, the forces on the two vehicles will not be exactly equal. EDSMAC will continue to adjust the length of each radial vector until the difference in the forces is less than the user-entered value of *ALAMB*. For solution stability, there must be a value of RHO tested for which the difference in inter-vehicle forces is less than ALAMB. This requires your selection of ALAMB such that ALAMB > STIFFNESS × DELRHO for the stiffnesses of both vehicles. Failure to meet this criterion may result in an error message (see Messages).

Tangential forces are developed due to inter-vehicle sliding friction and intermingling between individual vehicle components. This effect is accounted for by the user-entered value of the inter-vehicle friction coefficient, *AMU*. A friction force is transmitted whenever there is relative motion between the vehicles. The user-entered value, *ZETAV*, is the minimum relative velocity at which full inter-vehicle friction is developed; below it the friction force is scaled linearly with the sliding velocity.

EDSMAC allows for the effect of restitution after impact, thus giving the vehicle exterior some elasticity. This elasticity is modeled by allowing the length of each spring to increase slightly after it reaches its deflected length. The restitution varies non-linearly with the degree of deformation. Three values, $C_0$, $C_1$ and $C_2$, provide a 2nd-order polynomial fit that describes the relaxation of the RHO vectors at the end of each timestep:

$$e(\delta) = C_0 - C_1\,\delta + C_2\,\delta^2$$

where $\delta$ is the change in length (crush depth) of the RHO vector. *(Code note: restitution is applied only while $\delta < C_1/(2C_2)$, the vertex of the parabola; see `COLL.CPP` and the [EDSMAC Calculation Options](../../10-calculation-options/CalcOptEDSMAC.md) reference.)*

### Trajectory Phase

All of the external forces applied to the vehicle which direct its motion during the pre- and post-impact phases are applied at the tires.

> NOTE: The tire forces continue to exist during the collision phase.

Accurate computation of the tire forces is essential. Unfortunately, pneumatic tires do not behave in an easy-to-calculate manner. Rather, these properties are functions of several variables, and are extremely non-linear.

In order to calculate tire forces, EDSMAC uses the Fiala tire model [10]. This model has seen use in many popular simulations, and is used in EDSVS, EDVTS, and EDCRASH. The user supplies the tire cornering stiffness, $C_\alpha$, and tire/road slide friction data. The friction may be velocity dependent. A friction circle is used to limit longitudinal and lateral tire forces during combined braking and steering.

EDSMAC allows the vehicle to accelerate, brake and steer. The attempted acceleration, braking and steering are supplied by the user in tabular form using the Event Editor. It is important to understand these driver controls result in *attempted* forces; the Fiala tire model determines if these forces are sustainable at the tire-road interface and accounts for the condition if the available force is exceeded.

EDSMAC's vehicle model allows the user to study vehicles with dual tires.

## Assumptions

In order to provide a useful analysis without becoming burdensome and overly complex, EDSMAC makes several simplifying assumptions. If the user is to use EDSMAC properly, it is important these assumptions and their consequences be understood. In some cases, data which violate these assumptions will cause a fatal error, along with a message indicating the reason for the error. In other cases, the error is not with the data but with the use of the program under conditions which violate the assumptions inherent to the computations. EDSMAC will issue results which may not be valid for the circumstances of the accident. Before using EDSMAC, be sure your accident is within the scope of EDSMAC's original design.

A thorough list of assumptions and how to properly use the program can be found in the References [1-7, 11-13, 15]. Some of the major program assumptions are defined below:

### No Rollover Allowed

EDSMAC is a 3-degree of freedom analysis and does not consider roll or pitch degrees of freedom. If a vehicle rolls over, the equations of motion that apply during the trajectory phases no longer apply since forces are no longer applied at the tires but are applied between the vehicle exterior and road. EDSMAC makes no provision for this condition.

### All External Forces Applied at Tires

Other than during the collision, all forces which affect vehicle motion are applied at the tire/road interface. Aerodynamic effects are ignored. This assumption may become a factor at excessive speeds. In addition, forces caused by contact between the undercarriage and ground (sometimes resulting from impact damage) are not considered.

### Homogeneous Vehicle Exterior

The collision phase analysis assumes the same linear force vs crush relationship for all vehicle surfaces (front, sides or rear). The stiffness is assumed to be uniform for the entire surface. This means, for example, that the side stiffness is the same at the front fender, wheels, bumpers, doors and quarterpanel.

---

[Previous: Chapter 3 — Program Output](03-program-output.md) | [Next: Chapter 5 — EDSMAC Tutorial](05-tutorial.md)

<!-- NAV -->

---

← Previous: [Chapter 3 — EDSMAC Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDSMAC Tutorial](05-tutorial.md) →

<!-- /NAV -->
