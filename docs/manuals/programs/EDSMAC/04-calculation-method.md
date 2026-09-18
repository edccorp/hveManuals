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

The collision phase occurs when interference is detected between the vehicles. This condition is confirmed using simple geometry. Given interference exists, the widest damage range that is geometrically possible is bracketed between a beginning and a final azimuth angle measured from the vehicle CG, and the search for contact is confined to that range. The inter-vehicle force is then computed. The resulting acceleration of each vehicle is computed using Newton's second law (force equals the product of mass and acceleration), and is integrated twice in order to compute the changes in velocity and position.

The procedure for computing the inter-vehicle force is based on the concept of a linear spring. The exterior of each vehicle is surrounded by such springs with the user-entered spring constant, or stiffness.

When the vehicles are in contact, the springs of each vehicle press against each other. From this simple fact, several important observations can be made. First, the force between them is equal (Newton's third law). Second, since the displacement of each spring is proportional to the force, the crush (damage) profile of a given vehicle is defined by the end of its springs. Third, the motion of each vehicle resulting from the forces and moments can be computed. This is all the information EDSMAC needs at a given time step. The results determine how the vehicles respond during the impact phase.

To implement the collision model, the user must provide data which describe the vehicle exterior and control the simulation at each collision time interval.

The vehicle exterior is described by its crush stiffness, $K_v$. This parameter has the properties of a linear spring. However, since the spring properties are distributed around the vehicle exterior, the stiffness spring rate has units of pound per inch of crush depth per inch of crush length. The resulting units for stiffness are lb/in². Note that this is not a true "pressure", since the two-dimensional analysis results in a body exterior that has no vertical dimension and, therefore, has no area. The apparent units of area in the denominator result from the crush depth dimension related to the spring rate, lb/in.

Default values for $K_v$ are assigned to each vehicle and may be edited using the HVE-2D Vehicle Editor. Values for $K_v$ may also be computed from crash test data. The method is described in the literature [14].

*(updated: EDSMAC takes the vehicle's **frontal** stiffness and applies it to the
entire perimeter — the side and rear stiffness values stored with the vehicle are
not read. A vehicle struck in the side or rear is therefore modeled with its
frontal stiffness. A fixed barrier is given a stiffness of 500 lb/in².)*

> NOTE: When computing $K_v$ from crash test data, remember EDSMAC assumes the force vs deflection curve goes through the origin (i.e., $b_0 = 0$).

Three simulation control parameters are required for the collision model. The **Vector Spacing**, $\Delta\psi$, is the incremental angular spacing of each of the springs distributed about the vehicle exterior. The crush displacement of each spring is produced along radial vectors from the vehicle center of gravity to the locations on the original (before damage) vehicle exterior defined by the incremental spring spacing. The force on each vehicle is proportional to the crush displacement. Since the forces on each vehicle must be equal (Newton's third law — for every action there is an equal and opposite reaction), the current crush displacement is adjusted between both vehicles along each of the radial vectors. The user-entered increment of each radial vector adjustment, the **Vector Adjustment Increment**, $\Delta\rho$, is subtracted from one vehicle and added to the other until the forces on the vehicles are approximately equal.

Because the adjustments are finite increments of crush displacement, the forces on the two vehicles will not be exactly equal. EDSMAC will continue to adjust the length of each radial vector until the difference in the forces is less than the user-entered **Max Pressure Error** (also labelled Vector Force Tolerance), $\lambda$. For solution stability, there must be a RHO vector length tested for which the difference in inter-vehicle forces is less than the Max Pressure Error. This requires you to select a Max Pressure Error such that $\lambda > K_v\,\Delta\rho$ — that is, greater than the crush stiffness times the Vector Adjustment Increment — for the stiffnesses of both vehicles. Failure to meet this criterion may result in an error message (see [Chapter 6 — Messages](06-messages.md)).

> **NOTE:** EDSMAC does not adjust the Max Pressure Error for you. (EDSMAC4 does
> raise it automatically when it is too small for the stiffnesses in use.) If the
> value is too small, the iterative adjustment simply fails to converge and the
> run stops with a fatal message after 200 attempts.

Tangential forces are developed due to inter-vehicle sliding friction and intermingling between individual vehicle components. This effect is accounted for by the user-entered inter-vehicle friction coefficient, the **Inter-vehicle Friction** option, $\mu$. A friction force is transmitted whenever there is relative motion between the vehicles. The user-entered **Minimum Velocity for Friction**, $\zeta_v$, is the minimum relative velocity at which full inter-vehicle friction is developed; below it the friction force is scaled linearly with the sliding velocity.

EDSMAC allows for the effect of restitution after impact, thus giving the vehicle exterior some elasticity. This elasticity is modeled by allowing the length of each spring to increase slightly after it reaches its deflected length. The restitution varies non-linearly with the degree of deformation. Three values, $C_0$, $C_1$ and $C_2$, provide a 2nd-order polynomial fit that gives a restitution fraction between zero and one, used at the end of each timestep to blend each RHO vector between its crushed length and its original undeformed length:

$$e(\delta) = C_0 - C_1\,\delta + C_2\,\delta^2$$

where $\delta$ is the change in length (crush depth) of the RHO vector. The restored vector length is

$$\rho_{Restored} = e(\delta)\,\rho_{Original} + \left(1 - e(\delta)\right)\rho_{Crushed}$$

so $e = 0$ leaves the vector fully crushed and $e = 1$ restores it completely.

Restitution is not computed for **J-points** — points on the damage profile that
could not be established from the vehicle's own radial vector and had to be
constructed from the other vehicle's CG instead. These points are marked with a
double asterisk in the Vehicle Damage Summary table of the Damage Data report.

*(updated: earlier editions gave the polynomial without saying how its value is
used. It is a blend fraction, not a length.)* *(Note: restitution is applied only while $\delta < C_1/(2C_2)$, the vertex of the parabola; see the [EDSMAC Calculation Options](../../10-calculation-options/CalcOptEDSMAC.md) reference.)*

### Trajectory Phase

All of the external forces applied to the vehicle which direct its motion during the pre- and post-impact phases are applied at the tires.

> NOTE: The tire forces continue to exist during the collision phase.

Accurate computation of the tire forces is essential. Unfortunately, pneumatic tires do not behave in an easy-to-calculate manner. Rather, these properties are functions of several variables, and are extremely non-linear.

In order to calculate tire forces, EDSMAC uses the Fiala tire model [10]. This model has seen use in many popular simulations, and is used in EDSVS, EDVTS, and EDCRASH. The user supplies the tire cornering stiffness, $C_\alpha$, and tire/road slide friction data. The friction may be velocity dependent. A friction circle is used to limit longitudinal and lateral tire forces during combined braking and steering.

EDSMAC allows the vehicle to accelerate, brake and steer. The attempted acceleration, braking and steering are supplied by the user in tabular form using the Event Editor. It is important to understand these driver controls result in *attempted* forces; the Fiala tire model determines if these forces are sustainable at the tire-road interface and accounts for the condition if the available force is exceeded.

*(updated: earlier editions stated that EDSMAC's vehicle model allows the user to
study vehicles with dual tires. It does not. A vehicle with dual tires at any
wheel position is rejected at event initialization with a fatal error and the
event will not run. Use EDSMAC4, which does support dual tires, for such a
vehicle.)*

#### Tire force calculation

At each wheel, the friction coefficient is the tire's slide friction scaled by
the friction multiplier of the surface beneath that wheel, then adjusted for
speed:

$$\mu = \mu_{Slide}\,f_{Surface}\left(1 + C_\mu\,s\right)$$

where $s$ is the wheel's total speed and $C_\mu$ the speed reduction factor. A
zero speed reduction factor leaves the friction speed-independent. The surface
beneath each wheel is looked up separately, so the vehicle can straddle a
friction change. The force available at the tire-road interface is then

$$F_{Avail} = \mu\,F_z\,n_z$$

where $F_z$ is the wheel load and $n_z$ the vertical component of the surface
normal, which reduces the available force on a sloped surface.

The attempted longitudinal force is the sum of the throttle and brake table
entries at the current time. For the Percent Available Friction table method,
those entries are fractions and are multiplied by $F_{Avail}$. The longitudinal
force actually developed, $F_c$, is the attempted force limited by what the tire
can supply:

$$F_c = \mathrm{sgn}(u)\min\left(\left|F_{Attempt}\right|,\; F_{Avail}\cos\alpha\right)$$

for braking, and limited to $F_{Avail}$ for acceleration. At forward speeds
below 2 in/sec the braking force is scaled by $\left|u\right|/2$, so that a
nearly stopped wheel does not develop full braking force. The scaling applies to
braking only; drive force is not reduced at low speed.

Whatever longitudinal force is used is unavailable laterally. The remaining
lateral capacity follows the friction circle:

$$F_{s,max} = \sqrt{F_{Avail}^2 - F_c^2}$$

The Fiala model is then applied to that remaining capacity through the
non-dimensional sideslip parameter

$$\bar\beta = \frac{C_\alpha\,\alpha}{F_{s,max}}$$

giving the lateral force

$$F_s =
\begin{cases}
F_{s,max}\left(\bar\beta - \dfrac{\bar\beta\left|\bar\beta\right|}{3} + \dfrac{\bar\beta^3}{27}\right), & \left|\bar\beta\right| < 3\\[10pt]
F_{s,max}\,\mathrm{sgn}\,\bar\beta, & \left|\bar\beta\right| \ge 3
\end{cases}$$

The lateral force is set to zero, and the wheel is flagged as skidding, when
either the longitudinal force has consumed essentially all of the available
friction or the wheel's speed components are both below half an inch per second.
A wheel is also flagged as skidding when the Fiala model saturates.

Finally the two components are resolved through the wheel's steer angle,
$\delta$, into vehicle-fixed components:

$$F_y = F_s\cos\delta + F_c\sin\delta,\qquad F_x = -F_s\sin\delta + F_c\cos\delta$$

*(updated: earlier editions described the tire model in prose only. The
equations above are given for comparison with the other EDC programs. Note that
EDSMAC applies the Fiala polynomial to the slip angle directly, and normalizes
by the friction-circle remainder rather than by the peak friction force, so its
lateral force differs from the EDSVS and EDVTS form even for identical tire
data.)*

### Impact and Separation Times

The impact and separation times reported in the Accident History bound the
collision phase.

**Impact** is declared on the first timestep at which the two vehicle
perimeters interfere, which is tested geometrically by checking whether any
corner of either vehicle lies inside the other. At that moment the time,
position, heading, forward and lateral velocities and yaw rate of both vehicles
are recorded for the Accident History, and the integration timestep changes to
the Vehicle Collision Integration Timestep. These impact conditions are recorded
only once; a later contact between the vehicles does not update them, so in a
multiple-impact event the impact row always describes the first contact.

> **NOTE:** Unlike EDSMAC4, EDSMAC offers no choice of criterion. The
> acceleration threshold used below is fixed at 1 g and cannot be changed.

**Separation** is declared by either of two routes:

- **The vehicles are no longer interfering.** Separation follows at the next
  time falling on a Vehicle Separation Integration Timestep boundary.
- **The vehicles are still interfering, but neither is accelerating.** If the
  total acceleration of *both* vehicles is 1 g or less, a counter is advanced.
  Once that counter reaches six, separation is declared at the next separation
  timestep boundary. The delay exists because numerical integration can produce
  a single quiet timestep in the middle of a collision, and the program should
  not mistake it for the end of contact.

In both cases the separation time, positions and velocities are recorded, the
timestep changes to the separation timestep, and the trajectory timestep resumes
100 timesteps later.

Because the acceleration test uses the vehicle's *total* acceleration, tire
forces count toward it. This matters only at the 1 g threshold, which hard
braking on a high-friction surface can approach.

**A second impact** after separation requires both that the perimeters
interfere again and that at least one vehicle's total acceleration exceed 1 g.
The collision phase therefore restarts slightly after renewed contact, once the
contact has built up enough force to register.

> **NOTE:** The counter described above is not reset when the acceleration rises
> back above the threshold, so the six timesteps need not be consecutive. In a
> long collision whose acceleration crosses 1 g repeatedly, separation is
> declared after six sub-threshold timesteps in total.

### Collision Severity Results: PDOF, Delta-V and Peak Acceleration

The PDOF, delta-V and peak acceleration reported for each damage range are
derived from the vehicle's acceleration history, not from the inter-vehicle
contact force.

The PDOF is reported in the conventional CDC sense (see reference 8) — a
12 o'clock PDOF is a force directed from front to rear, so the reported angle is
180 degrees opposite the direction in which the force acts on the vehicle.
Angles are measured in the vehicle-fixed frame with zero forward and positive
toward the right side.

**Acceleration peaks.** A peak is recorded each time a vehicle's total
acceleration rises above 1 g and falls back below it. The peak magnitude, its
forward and lateral components and its time are stored. Up to ten peaks are
kept, after which a message is issued; the peaks are then sorted into descending
order of magnitude.

**Delta-V of a peak** is the integral of the acceleration **magnitude** over the
peak, computed by the trapezoidal rule:

$$\Delta V = \int \left|\mathbf{a}\right|\,dt$$

Because this is a scalar integral rather than a vector one, a peak whose
direction rotates produces a larger delta-V than the corresponding change in
velocity. To limit this, the direction of the acceleration is tracked in
sectors, and the contribution of an acceleration that has changed sector is
suppressed.

**PDOF of a peak** is the direction of the acceleration at the instant of the
peak, converted to the conventional sense described above.

**Matching peaks to damage.** Each damage range found on the crush profile is
matched to the acceleration peak whose clock direction is closest to the
mid-point of that range. The search widens in 15-degree steps; if no peak lies
within 60 degrees of the mid-point, the largest peak is used instead and a
message is issued. This is a common and harmless outcome for sideswipes and
secondary impacts.

**Total delta-V of a damage range** is the sum of the delta-Vs of *all*
acceleration peaks whose clock direction lies within one hour either side of the
matched peak's clock direction, so delta-V arising from separate impacts in the
same general direction is combined into a single figure for that range. If only
one peak was found, all delta-V is assigned to it.

**Peak acceleration** reported for a range is the magnitude of the matched
acceleration peak, and the reported time is the time at which it occurred. As
with delta-V, it is the vehicle's total acceleration and so includes the tire
contribution.

## Assumptions

In order to provide a useful analysis without becoming burdensome and overly complex, EDSMAC makes several simplifying assumptions. If the user is to use EDSMAC properly, it is important these assumptions and their consequences be understood. In some cases, data which violate these assumptions will cause a fatal error, along with a message indicating the reason for the error. In other cases, the error is not with the data but with the use of the program under conditions which violate the assumptions inherent to the computations. EDSMAC will issue results which may not be valid for the circumstances of the accident. Before using EDSMAC, be sure your accident is within the scope of EDSMAC's original design.

A thorough list of assumptions and how to properly use the program can be found in the References [1-7, 11-13, 15]. Some of the major program assumptions are defined below:

### No Rollover Allowed

EDSMAC is a 3-degree of freedom analysis and does not consider roll or pitch degrees of freedom. If a vehicle rolls over, the equations of motion that apply during the trajectory phases no longer apply since forces are no longer applied at the tires but are applied between the vehicle exterior and road. EDSMAC makes no provision for this condition.

### All External Forces Applied at Tires

Other than during the collision, all forces which affect vehicle motion are applied at the tire/road interface. Aerodynamic effects are ignored. This assumption may become a factor at excessive speeds. In addition, forces caused by contact between the undercarriage and ground (sometimes resulting from impact damage) are not considered.

### Homogeneous Vehicle Exterior

The collision phase analysis assumes the same linear force vs crush relationship for all vehicle surfaces (front, sides or rear) — specifically, the vehicle's frontal stiffness, applied everywhere. The stiffness is assumed to be uniform for the entire surface. This means, for example, that the side stiffness is the same at the front fender, wheels, bumpers, doors and quarterpanel.

---

[Previous: Chapter 3 — Program Output](03-program-output.md) | [Next: Chapter 5 — EDSMAC Tutorial](05-tutorial.md)

<!-- NAV -->

---

← Previous: [Chapter 3 — EDSMAC Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDSMAC Tutorial](05-tutorial.md) →

<!-- /NAV -->
