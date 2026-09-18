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

In HVE, at each time step, the vehicle's roll, pitch and CG elevation are computed using HVE's surface-information search [25]. This approach allows the vehicle to sense when it is on a grade, and the equations of motion account for the grade. Surface slopes up to about 15 degrees are allowed (a message will be issued if this angle is exceeded). Thus, vehicle motion on hills, super-elevations, road crowns and even sloped shoulders may be modeled using EDSMAC4.

*(updated: the current version also includes an optional dynamic **steer degree of freedom** — when enabled via the Steer DOF calculation option, wheel steer angles are computed from the torques acting on the steering system (tire friction, steering stops, gyroscopic precession, steering column friction) instead of being read directly from the driver steer tables; see [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md#steer-dof).)*

### Collision Phase

The EDSMAC4 collision model is described in detail in reference 23.

During the collision phase, each vehicle's crush perimeter is described by a set of radial RHO vectors extending from the CG to the vehicle exterior, spaced at the user-entered **Vector Spacing** angle (default 2 degrees). When the perimeters of two vehicles overlap, the collision calculation iteratively adjusts the lengths of corresponding RHO vectors, in steps of the **Vector Adjustment Increment**, until force equilibrium between the two vehicles is achieved within the **Vector Force Tolerance**. Collision forces are computed from the A and B stiffness coefficients of the crushed surfaces; friction forces tangent to the crush surface are computed using the inter-vehicle friction coefficient (set per vehicle pair in the Vehicle Mesh dialog), reduced linearly below the **Minimum Velocity for Friction**. Restitution is applied using the parametric model with coefficients $C_0$, $C_1$ and $C_2$. *(See references 21–23 for the full derivation.)*

### Trajectory Phase

All of the external forces applied to the vehicle which direct its motion during the pre- and post-impact phases are applied at the tires.

> **NOTE:** The tire forces continue to exist during the collision phase.

Accurate computation of the tire forces is essential. Unfortunately, pneumatic tires do not behave in an easy-to-calculate manner. Rather, these properties are functions of several variables, and are extremely non-linear.

In order to calculate tire forces, EDSMAC4 uses the Fiala tire model [10]. This model has seen use in many popular simulations, and is used in EDSVS, EDVTS, and EDCRASH. The user supplies the tire cornering stiffness, $C_\alpha$, and tire/road slide friction data. The friction may be velocity dependent. A friction circle is used to limit longitudinal and lateral tire forces during combined braking and steering.

EDSMAC4 allows the vehicle to accelerate, brake and steer. The attempted acceleration, braking and steering are supplied by the user in tabular form using the Event Editor. It is important to understand these driver controls result in *attempted* forces; the Fiala tire model determines if these forces are sustainable at the tire-road interface and accounts for the condition if the available force is exceeded.

EDSMAC4 models quasi-static longitudinal and lateral load transfers. This is accomplished by applying the current inertial longitudinal and lateral forces at the vehicle's CG elevation, thus producing a pitch and/or roll moment. Lateral load transfer is apportioned to the front and rear axles using the vehicle's roll couple distribution. Roll couple distribution is primarily a function of the front-to-rear lateral stiffness ratio of the front and rear suspensions.

EDSMAC4's vehicle model allows the user to study vehicles with tandem axles and dual tires.

#### Tire force calculation

At each wheel, the friction coefficient is the tire's slide friction scaled by
the friction multiplier of the surface beneath it — which the hydroplaning
model further reduces when one is selected — and then adjusted for speed:

$$\mu = \mu_{Slide}\,f_{Surface}\left(1 + C_\mu\,s\right)$$

where $s$ is the wheel's total slip speed and $C_\mu$ the speed reduction
factor. A zero speed reduction factor leaves the friction speed-independent.
The force available at the tire-road interface is then

$$F_{Avail} = \mu\,F_z$$

The attempted longitudinal force is the sum of the throttle and brake table
entries at the current time; for the Percent Available Friction table method
those entries are fractions and are multiplied by $F_{Avail}$. The longitudinal
force developed, $F_c$, is the attempted force limited to what the tire can
supply. At forward speeds below 2 in/sec the braking force is scaled by
$\left|u\right|/2$, so that a nearly stopped wheel does not develop full braking
force; drive force is not reduced at low speed.

Whatever longitudinal force is used is unavailable laterally. The remaining
lateral capacity follows the friction circle:

$$F_{s,max} = \sqrt{F_{Avail}^2 - F_c^2}$$

The Fiala model is applied to that remaining capacity through the
non-dimensional sideslip parameter

$$\bar\beta = \frac{\left(1 + \delta_{dual}\right)C_\alpha\,\alpha}{F_{s,max}}$$

where $\delta_{dual}$ is 1 at a dual-tire wheel location and 0 otherwise, giving

$$F_s =
\begin{cases}
F_{s,max}\left(\bar\beta - \dfrac{\bar\beta\left|\bar\beta\right|}{3} + \dfrac{\bar\beta^3}{27}\right), & \left|\bar\beta\right| < 3\\[10pt]
F_{s,max}\,\mathrm{sgn}\,\bar\beta, & \left|\bar\beta\right| \ge 3
\end{cases}$$

The two components are then resolved through the wheel's steer angle, $\delta$,
into vehicle-fixed components:

$$F_y = F_s\cos\delta + F_c\sin\delta,\qquad F_x = -F_s\sin\delta + F_c\cos\delta$$

*(updated: earlier editions described the tire model in prose only. Note that
the dual-tire factor is applied to the cornering stiffness rather than to the
available force, which differs from EDSVS and EDVTS, where the factor multiplies
the force; and that the friction circle is built on the slide friction rather
than a peak friction value, so EDSMAC4 has no distinct peak-versus-slide
behavior.)*

*(updated: when the **Hydroplane Model** calculation option is set to NASA, the available tire friction is further modified at each tire travelling over a water polygon. The NASA model predicts the hydroplaning speed from the tire's inflation pressure ($182.16\sqrt{P}$ in/sec, $P$ in lb/in²); above that speed the tire's friction switches to the water polygon's friction value. The extra drag of displacing water is not modeled. See [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md#hydroplane-model).)*

### Impact and Separation Times

The impact and separation times reported in the Accident History bound the
collision phase. They are found by testing two conditions at every timestep.

The first condition is geometric: the original (undamaged) perimeter of one
vehicle must overlap the other, which is tested by checking whether any corner
of either vehicle lies inside the other. The second condition is selected by
the **Accident History Basis** calculation option:

- **Impact Force** (default) — inter-vehicle collision force is acting at one
  or more points on the two vehicles.
- **Acceleration** — the total acceleration of either vehicle exceeds the
  **Threshold** value (default 1 g).

The impact time is the first time at which *both* conditions hold. Note that
both are required: with the Acceleration basis, the collision phase still
cannot begin before the perimeters overlap. At this time the integration
timestep changes to the Vehicle Collision Integration Timestep.

The impact conditions stored for the Accident History — time, position,
heading, total speed, forward and lateral components and yaw rate for both
vehicles — are latched at that first detection and are never updated by later
contact between the same pair. In a multiple-impact event the impact row
therefore always describes the *first* contact between that pair. Impact and
separation are tracked separately for each pair of vehicles, so a three-vehicle
event produces one impact and one separation entry for each colliding pair.

The end of the collision phase uses the reverse test:

- **Impact Force** — no collision force is acting between the two vehicles.
- **Acceleration** — the total acceleration of *both* vehicles is below the
  Threshold.

The separation condition must be satisfied on consecutive timesteps before
separation is declared: **one** timestep with the Impact Force basis, **six**
with the Acceleration basis. Separation is then declared at the next time
falling on a Vehicle Separation Integration Timestep boundary, at which point
the timestep changes and the separation conditions are recorded. The reported
separation time consequently lags the true end of contact slightly — by about
one timestep with the Impact Force basis, and by up to six collision timesteps
plus one separation timestep with the Acceleration basis.

> **NOTE:** The acceleration used by the Acceleration basis is the vehicle's
> *total* acceleration, which includes tire forces. If the Threshold is set
> low enough that hard braking or cornering alone exceeds it, separation can
> never be declared and the event will remain in the collision phase — and at
> the collision timestep — for the rest of the run. The 1 g default is above
> what tires normally produce, but a reduced threshold on a high-friction
> surface can reach this condition.

#### Repeated impact and separation

Nothing restricts the collision phase to a single occurrence. If the vehicle
perimeters are still overlapping when contact resumes after separation has been
declared, the collision phase simply restarts: the integration timestep returns
to the Vehicle Collision Integration Timestep and the separation test begins
again. With the Impact Force basis, where one force-free timestep is enough to
declare separation, a disengagement in which contact flickers on and off can
cycle through this several times within a few tens of milliseconds.

Only the first and the last of these appear in the Accident History. The impact
conditions are recorded once, at first contact, and are never updated; the
separation conditions are re-recorded at every separation, so the values shown
are those of the **final** one. The report therefore spans the event as a whole —
first contact to last separation — and gives no indication of intermittent
contact in between.

### Collision Severity Results: PDOF, Delta-V and Peak Acceleration

The PDOF, delta-V and peak acceleration reported in the Damage Data report are
computed by one of two entirely separate methods, selected by the **Damage Data
Format** calculation option. The two methods do not produce identical numbers;
the Traditional format is retained for comparison with results from earlier
releases.

In both cases the PDOF is reported in the conventional CDC sense (see
reference 8) — a 12 o'clock PDOF is a force directed from front to rear, so the
reported angle is 180 degrees opposite the direction in which the force acts on
the vehicle. Angles are measured in the vehicle-fixed frame with zero forward
and positive toward the right side, and are reported in the range ±180 degrees.

#### Collision Data format (default)

Each row of the Collision Summary table is one **collision pulse** — one period
of sustained contact between that vehicle and one collision partner. For each
pulse the report gives the pulse number, the vehicle or environment struck, the
start and end times and the duration, the peak acceleration, the peak collision
force, the delta-V and the PDOF, followed by the CDC, damage width and offset,
maximum crush and the crush profile measurements.

##### How a pulse is delimited

The rule that decides where one pulse ends and the next begins is separate from
the one that fixes the impact and separation times in the Accident History, and
it is far less sensitive. The two reports can therefore describe the same
contact differently.

**Start.** A pulse opens on the first timestep at which any point on the vehicle
carries collision force from that partner. There is no force threshold — any
non-zero contact force opens the pulse.

**Continuation.** On every timestep that contact persists, a provisional closing
deadline is set 0.025 seconds ahead. The pulse is closed only once contact has
been absent continuously until that deadline passes. Because the deadline is
re-set on each contact timestep it is a rolling one: the pulse survives until a
full 0.025 seconds have elapsed with no contact at all, however many times
contact has come and gone before that. If contact resumes before the deadline,
the vehicle rejoins the pulse already in progress against that partner instead
of opening a new one.

The intent is that the intermittent contact typical of two vehicles disengaging
is reported as one collision rather than a string of small ones. The
consequence is that any contact separated from the previous one by less than
0.025 seconds is absorbed into it: its impulse contributes to that pulse's PDOF,
its acceleration to the pulse's delta-V, and the vertices it touches to the
pulse's CDC, with nothing in the report to show that a distinct contact
occurred.

> **NOTE:** This matters when the later contact is severe. A secondary strike
> reaching a third of the peak collision force, occurring twenty milliseconds
> after contact was lost, is merged into the preceding pulse and appears nowhere
> as an event of its own. If the trajectory suggests a separate secondary
> contact, examine the collision force in the Variable Output, Kinetics group
> rather than relying on the pulse count.

A gap longer than 0.025 seconds does close the pulse, and the next contact opens
a new one, producing a second row.

**End.** The time in the End column is **not** the time the pulse was closed. It
is the last timestep at which the vehicle had not been declared separated from
that partner, using the Accident History criterion described
[above](#impact-and-separation-times); Length is simply End minus Start. Because
the collision phase may be entered more than once, the End time follows the last
contact episode rather than the first separation. The pulse's own closure — 0.025
seconds after the final contact — governs only whether a later contact starts a
new row, and is never reported.

**Limits.** Up to ten pulses are tracked for each vehicle; an eleventh ends the
run with a message. A pulse still open when the run ends is counted as complete
and a diagnostic message is issued.

**PDOF.** The inter-vehicle collision forces acting on the vehicle are
accumulated over the pulse, giving the total collision impulse in vehicle-fixed
coordinates. The PDOF is the direction of that impulse:

$$\mathrm{PDOF} = \mathrm{atan2}\left(J_y,\,J_x\right) + 180^\circ$$

where $J_x$ and $J_y$ are the forward and lateral components of the accumulated
collision impulse. A zenith angle, the elevation of the impulse out of the
horizontal plane, is also stored, but since EDSMAC4 computes no vertical
collision force it is always zero. The clock direction used for the first two
characters of the CDC is this same angle rounded to the nearest hour. Both are
frozen once separation is declared.

> **NOTE:** The PDOF is derived from the collision force alone. Tire forces do
> not affect it.

**Delta-V.** The vehicle's acceleration components are integrated through the
pulse using the trapezoidal rule, accumulating a velocity-change vector in
vehicle-fixed coordinates. The reported delta-V is the largest magnitude that
vector reaches at any point during the pulse:

$$\Delta V = \max_{t_{Impact}\,\le\, t\,\le\, t_{Separation}}\;
            \left|\int_{t_{Impact}}^{t}\mathbf{a}\;dt\right|$$

Two properties of this calculation are worth understanding:

- The acceleration integrated is the vehicle's **total** acceleration, not the
  collision acceleration alone. Tire forces acting during contact therefore
  contribute to the reported delta-V. In a severe impact the contribution is
  negligible — a fraction of a g against tens of g — but in a low-severity
  sideswipe with heavy braking it is not.
- The components are integrated in the vehicle-fixed frame while the vehicle is
  yawing. For the short durations typical of a collision the yaw change is
  small and the result is very close to the change in the earth-fixed velocity
  vector, but a long, rotating sideswipe will accumulate a delta-V that differs
  from the vector difference between the velocities at impact and separation.

**Peak acceleration** is the largest total acceleration reached at any timestep
on which collision force was acting; **peak force** is the largest total
collision force, and the time at which it occurred is stored with it. As with
delta-V, the peak acceleration includes the tire contribution.

#### Traditional format

The Traditional format reproduces the original SMAC reporting, which works from
the acceleration history rather than from the contact force. It is available
only for events with more than one vehicle.

**Acceleration peaks.** A peak is recorded each time the vehicle's total
acceleration rises above the Threshold value and falls back below it. The peak
magnitude, its forward and lateral components and its time are stored. Up to
ten peaks are kept, after which a message is issued; the peaks are then sorted
into descending order of magnitude.

**Delta-V of a peak** is the integral of the acceleration **magnitude** over
the peak, again by the trapezoidal rule:

$$\Delta V = \int \left|\mathbf{a}\right|\,dt$$

Because this is a scalar integral rather than a vector one, a peak whose
direction rotates produces a larger delta-V than the corresponding change in
velocity. To limit this, the direction of the acceleration is tracked in
sectors, and the contribution of an acceleration that has changed sector is
suppressed.

**PDOF of a peak** is the direction of the acceleration at the instant of the
peak, converted to the conventional sense as described above.

**Matching peaks to damage.** Each damage range found on the crush profile is
matched to the acceleration peak whose clock direction is closest to the
mid-point of that range. If no peak lies within 60 degrees of the mid-point,
the largest peak is used instead and a message is issued — a common and
harmless outcome for sideswipes and secondary impacts.

**Total delta-V of a damage range** is the sum of the delta-Vs of *all*
acceleration peaks whose clock direction lies within one hour either side of
the matched peak's clock direction. Delta-V arising from separate impacts in
the same general direction is therefore combined into a single figure for that
damage range. If only one peak was found, all delta-V is assigned to it.

> **NOTE:** The Threshold value is used by the Traditional format regardless of
> the Accident History Basis. The dialog disables the Threshold field when the
> basis is Impact Force, but the stored value — 1 g by default — still sets the
> minimum acceleration at which an acceleration peak is recognized and delta-V
> is accumulated.

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
