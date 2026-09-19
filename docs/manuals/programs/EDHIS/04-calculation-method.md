# Chapter 4 — Calculation Method

In the original Fifth Edition manual this chapter was marked *(Reserved For Future Use)*.

> **NOTE:** See Reference 2 (Robbins, Bennett & Bowman, *User-Oriented Mathematical Crash Victim Simulator*, HSRI, University of Michigan) for the original derivation of the model on which EDHIS is based — see [Chapter 7 — References](07-references.md). The description below documents what the current EDHIS engine computes.

## Basis for Analysis

EDHIS is a rigid-body simulation of an occupant inside a vehicle whose motion
is prescribed. The occupant is a three-segment, two-joint body with twelve
degrees of freedom, derived from the HSRI-3D crash victim simulator. The
vehicle itself is **not** simulated: its motion comes from the collision pulse
the user supplies, so EDHIS solves only for the occupant's response to that
pulse.

At each timestep the program locates contact between the occupant's ellipsoids
and the vehicle's contact surfaces, evaluates the resulting forces, adds joint,
belt, airbag and gravity effects, and solves for the segment accelerations.

## The Human Model

### Condensing the HVE human to three segments

HVE's human is a 15-segment model. EDHIS uses three segments — **head**,
**torso** and **legs** — so the HVE segments are lumped into those three. Masses
add directly, and the moments of inertia are transferred to the EDHIS segment
reference using the parallel axis theorem:

$$I = \sum_i \left(I_{i} + m_i\,d_i^2\right)$$

where $d_i$ is the distance from each contributing segment's centre of mass to
the EDHIS segment reference. The transfer is applied to the pitch and roll axes;
the yaw axis is left as the direct sum of the contributing inertias.

Each EDHIS segment carries up to 25 contact ellipsoids in total across the body,
which are the geometry actually tested against the vehicle interior.

## Equations of Motion

The model is formulated in generalized coordinates. Writing $\mathbf{q}$ for the
twelve generalized coordinates, the equations of motion are assembled as a mass
matrix acting on the generalized accelerations, balanced against the sum of the
generalized forces:

$$\mathbf{M}(\mathbf{q})\,\ddot{\mathbf{q}} =
   \mathbf{Q}_{Inertial} + \mathbf{Q}_{Contact} + \mathbf{Q}_{Joint}
 + \mathbf{Q}_{Gravity} + \mathbf{Q}_{Belt}$$

where

| Term | Meaning |
|---|---|
| $\mathbf{M}(\mathbf{q})$ | Generalized mass matrix. Part of it is constant; the remainder depends on the current joint angles and is rebuilt every timestep. |
| $\mathbf{Q}_{Inertial}$ | Coriolis and centrifugal terms arising from the rotating segment frames |
| $\mathbf{Q}_{Contact}$ | Contact surface forces, including airbag forces |
| $\mathbf{Q}_{Joint}$ | Neck and hip joint torques |
| $\mathbf{Q}_{Gravity}$ | Segment weights |
| $\mathbf{Q}_{Belt}$ | Belt and harness tensions |

The system is solved for $\ddot{\mathbf{q}}$ each timestep by Gaussian
elimination. A singular mass matrix is a fatal error and terminates the run.

> **NOTE:** Where the **Minimum Acceleration** calculation option is non-zero, any generalized acceleration whose magnitude falls below it is set to zero before integration. This suppresses numerical noise in a body at rest; setting it too high will suppress real response.

## Contact Forces

### Detecting contact

Each of the occupant's ellipsoids is tested every timestep against each vehicle
contact surface. A surface is a plane bounded by its four corner coordinates.
Where an ellipsoid has passed through that plane, the **penetration**,
$\delta$, is the depth of the intrusion measured along the surface normal.

Two further tests decide whether a penetration develops any force.

**Which side the occupant came from.** Each ellipsoid/surface pair records the
side from which contact was made. If, at a step where front-side contact has not
already been established, the ellipsoid lies behind the plane by more than the
surface's **maximum penetration**, the pair is marked as approached from the
back and no force is computed. That status is permanent for the pair, so a
surface the occupant began behind never pushes them forward — which is what
allows surfaces to be placed around the occupant without trapping them.

**Where the contact falls on the surface.** The contact point is expressed as
two dimensionless coordinates $s$ and $r$, each running from 0 at one edge of
the plane to 1 at the opposite edge. The surface's **edge constant**,
$\varepsilon$, is also dimensionless and defines a border of that width inside
and outside each edge:

- If either coordinate lies outside $[-\varepsilon,\,1+\varepsilon]$ the
  contact is off the surface altogether and no force is computed.
- If both lie in the interior, $[\varepsilon,\,1-\varepsilon]$, the full force
  is applied.
- In the border, the force is scaled by a factor falling linearly from 1 at the
  inner boundary to 0 at the outer one, evaluated independently in each
  direction:

$$k_s = \frac{s + \varepsilon}{2\varepsilon}\ \ (s < 0.5),
  \qquad
  k_s = \frac{1 + \varepsilon - s}{2\varepsilon}\ \ (s \ge 0.5)$$

with $k_r$ formed the same way from $r$. The contact force computed below is
multiplied by $k_s\,k_r$. The effect is that an ellipsoid sliding off the edge
of a surface loses its force gradually rather than having it vanish in one
timestep, which would otherwise show up as a spike in the accelerations.

> **NOTE:** The edge constant scales the force; it does not alter the penetration. A larger edge constant therefore widens the taper — it softens the surface near its boundary and extends the surface's reach slightly beyond its corner coordinates, but it does not change the force developed in the middle of the surface.

### The force-deflection law

While the penetration is increasing, the contact force is a cubic in the
penetration depth plus a damping term proportional to the penetration rate:

$$F = C_3\,\delta^3 + C_2\,\delta^2 + C_1\,\delta
    + C_d\,\dot{\delta}\,\min\left(\delta,\,1\right)$$

where $C_1$, $C_2$ and $C_3$ are the surface's linear, quadratic and cubic force
coefficients and $C_d$ is its rate damping coefficient.

The $\min(\delta, 1)$ on the damping term is important to understand: the
damping contribution is faded in linearly over the first inch of penetration and
is at full strength thereafter. Without it, a contact that begins at a high
closing speed would produce a force discontinuity at the instant of touch.

The force is limited to the surface's **maximum force**; once that value is
reached the surface is treated as saturated and the force is held there.

### Unloading and permanent deformation

When the penetration rate becomes negative after saturation, the force does not
retrace the loading curve. It falls along a straight line of the user-entered
**unloading slope**, drawn through the point at which saturation occurred:

$$F = F_{Max} + S\left(\delta - \delta_{Max}\right)$$

where $S$ is the unloading slope and $\delta_{Max}$ the penetration at
saturation. The line reaches zero force at

$$\delta_{0} = \delta_{Max} - \frac{F_{Max}}{S}$$

and $\delta_0$ is the permanent deformation left in the surface: below it no
force is developed, and a later contact at that location begins from the
deformed shape rather than the original one. A negative permanent deformation is
not physically meaningful and is reported as a fatal error.

Where no maximum force and unloading slope are entered, the surface is fully
elastic and unloads back down the cubic loading curve.

## Joint Torques

Each of the two joints — neck and hip — is a ball-and-socket carrying a torque
about each of its three axes. The total is an elastic term plus a joint-stop
term:

$$T = T_{Elastic} + T_{Stop}$$

The elastic term is a linear spring referred to the joint's **initial** angle,
so an undisturbed occupant is in equilibrium:

$$T_{Elastic} = k\left(\theta_{Initial} - \theta\right)$$

The joint stop acts only once the joint has rotated past its permitted range.
Writing $\theta_{Stop}$ for that limit and

$$\varepsilon = \left|\theta\right| - \theta_{Stop}$$

for the amount of over-rotation, the stop contributes nothing while
$\varepsilon \le 0$, and while $\varepsilon > 0$,

$$T_{Stop} = -k_{Stop}\,\varepsilon\,\mathrm{sgn}\,\theta
             - c\,\dot{\theta}\,\min\left(\frac{\varepsilon}{0.1},\,1\right)$$

where $k_{Stop}$ is the joint-stop elasticity and $c$ the joint damping. As with
the contact damping, the damping contribution is faded in — here over the first
0.1 radian of over-rotation — so that the stop engages smoothly.

A sign test is applied afterwards: if the damping term is large enough to
reverse the sign of the total stop torque, the stop torque is set to zero
instead. A joint stop can therefore resist over-rotation but can never drive the
joint.

> **NOTE:** The pitch axis is treated asymmetrically, because flexion and extension of the neck and hip are not symmetric. It carries two separate limits with their own stop elasticities — one reached in positive rotation and one in negative — while the yaw and roll axes use a single limit applied to the magnitude of the angle.

The joint torques enter the equations of motion as generalized forces through
the joint articulation geometry:

$$\mathbf{Q}_{Joint} = \sum_{Joints}\ \sum_{Axes} T\,
   \frac{\partial \theta}{\partial \mathbf{q}}$$

## Vehicle Motion

The vehicle is not simulated. Its six acceleration components come from the
user's collision pulse table, and within each table interval the acceleration is
taken to vary linearly with time — that is, at constant jerk. Integrating that
assumption gives the vehicle's velocity and position directly:

$$a(t) = a_0 + \dot{a}\,t$$

$$v(t) = v_0 + a_0\,t + \tfrac{1}{2}\dot{a}\,t^2$$

$$s(t) = s_0 + v_0\,t + \tfrac{1}{2}a_0\,t^2 + \tfrac{1}{6}\dot{a}\,t^3$$

where $t$ is measured from the start of the current table interval and
$\dot{a}$ is the slope of the acceleration across it. Each of the six components
is scaled independently by its own pulse factor before integration, which is
what the pulse scaling controls in the Event Editor adjust.

## Belts

A belt segment runs between an anchor on the vehicle and a point on the
occupant. Its **initial length** is the geometric length at the start of the run
plus the user-entered slack, so a belt with slack develops no tension until the
occupant has moved far enough to take the slack up. The **stretch** is the
amount by which the current length exceeds that initial length:

$$\delta = L - \left(L_0 + Slack\right)$$

Tension follows the same force law as a contact surface — cubic in the
deformation with a rate-damping term, limited by a maximum force, and unloading
along a straight line of the entered slope:

$$F = C_3\,\delta^3 + C_2\,\delta^2 + C_1\,\delta
    + C_d\,\dot{\delta}\,\min\left(\delta,\,1\right)$$

using the belt's own stiffness and damping coefficients. The stretch rate is the
component of the relative velocity between the two ends resolved along the
belt's current direction, so a belt lying slack across a moving occupant
develops no damping force either.

The tension acts along the belt's direction cosines, and enters the equations of
motion as a generalized force through them:

$$\mathbf{Q}_{Belt} = -\sum_{Segments} F\,\frac{\partial L}{\partial \mathbf{q}}$$

The belt angles reported in the output are the direction cosines of each segment
expressed as angles.

> **NOTE:** Because belt tension uses the same law as contact, a belt also carries a permanent set: once its maximum force has been exceeded it unloads along the entered slope rather than back down the loading curve, and does not recover its original stiffness.

## Airbag Model

When an airbag is specified, its inflation is **solved** alongside the occupant
equations rather than prescribed. A driver bag is modelled as a sphere and a
passenger bag as a cylinder of the entered length. The bag carries two state
variables of its own — its internal pressure and its radius — and they are
integrated on their own sub-step within each occupant timestep.

### Gas state and mass balance

The gas is treated as isentropic, so its density follows the pressure:

$$\rho = \rho_0\left(\frac{P}{P_0}\right)^{1/\kappa}$$

where $P$ is the **absolute** pressure (gauge pressure plus atmospheric) and
$\kappa$ the ratio of specific heats. The governing equation is conservation of
mass in the bag:

$$\frac{d}{dt}\left(\rho V\right) = \dot{m}_{In} - \dot{m}_{Out}$$

Carrying out the differentiation, with the bag volume $V$ depending on both the
radius and — after contact — on how far the occupant has pushed into the bag:

$$\frac{1}{\kappa}P^{\frac{1}{\kappa}-1}V\,\dot{P}
 + P^{\frac{1}{\kappa}}\dot{V}
 = \frac{P_0^{1/\kappa}}{\rho_0}\left(\dot{m}_{In} - \dot{m}_{Out}\right)$$

The inflow $\dot{m}_{In}$ is the entered mass flow rate, held constant until the
gas is shut off. Shut-off occurs at whichever comes first: the bag reaching its
entered maximum volume, or the end of the entered inflation time.

### The vent

The vent stays closed, and the outflow is zero, while the internal pressure is
below the entered **vent pressure**. Once it is exceeded, the outflow is the
standard compressible orifice discharge:

$$\dot{m}_{Out} = C_d\,A_{Vent}\,\Phi\,\sqrt{2\,P_{Gauge}\,\rho}$$

where $C_d$ is the discharge coefficient, $A_{Vent}$ the vent area and $\Phi$
the compressibility factor:

$$\Phi = \sqrt{\frac{\kappa}{\kappa-1}\,
   \bar{P}^{\,2/\kappa}
   \left(1 - \bar{P}^{\,(\kappa-1)/\kappa}\right)
   \frac{1-\bar{R}}{\left(1-\bar{P}\right)\left(1-\bar{R}\,\bar{P}^{\,2/\kappa}\right)}}$$

in which $\bar{P}$ is the ratio of atmospheric to absolute bag pressure and
$\bar{R}$ is the fourth power of the ratio of vent radius to bag radius. The
second of these is the approach-velocity correction: it matters only when the
vent is not small compared with the bag.

### The fabric

The second equation closing the system is the bag's own stiffness. The fabric is
treated as a membrane whose stress is the entered elastic modulus times its
**true** (logarithmic) strain. For the spherical driver bag the membrane stress
is $PR/2h$ and for the cylindrical passenger bag $PR/h$, giving

$$\frac{P\,R}{2h} = E\,\ln\!\left(\frac{R}{R_0}\right)
  \qquad\text{(driver)}, \qquad
  \frac{P\,R}{h} = E\,\ln\!\left(\frac{R}{R_0}\right)
  \qquad\text{(passenger)}$$

where $h$ is the fabric thickness and $R_0$ the unstretched radius. It is the
time derivative of this relation, together with the mass balance above, that is
solved each sub-step for the rate of change of pressure and of radius.

### Contact with the occupant

Contact begins when the torso, head or hip reaches the bag surface, allowing for
half the occupant's chest depth. From that instant the bag is treated as
flattened against the occupant: its radius is reduced by half the distance the
torso has travelled since contact, and the diameter of the flattened patch
becomes the second state variable in place of the free radius. The volume is
then a sphere with a spherical cap replaced by a flat disc,

$$V = \tfrac{4}{3}\pi a^3 + \tfrac{1}{2}\pi\,a\,d^2 \qquad\text{(driver)}$$

$$V = \pi a^2 L + 2\,a\,d\,L \qquad\text{(passenger)}$$

with $a$ the current bag radius, $d$ the contact patch dimension and $L$ the
entered bag length.

The force on the occupant is the bag pressure acting over the contact patch,

$$F = P_{Gauge}\;\frac{\pi}{4}\,d\,w$$

with $w$ equal to $d$ for a driver bag (a circular patch) and to the occupant's
chest width for a passenger bag (an elliptical patch). This force is then faded
in linearly over the entered **Bag Penetration For Force**, so that a bag which
the occupant has only just touched does not apply its full pressure force at the
first step:

$$F_{Applied} = F\,\min\!\left(\frac{\delta}{\delta_{Bag}},\,1\right)$$

and it is scaled by the same edge factors as any other contact surface.

### Bottoming out and rebound

If the bag radius reaches zero the bag has **bottomed out**: the gas model no
longer governs and the force rises linearly from its value at bottoming out,
with the entered bottomed-out stiffness, as the occupant continues forward.
Separately, once the occupant begins to move away from the bag the fabric
modulus is switched to the entered **rebound** modulus, so that the bag does not
return energy along its loading curve.

Where a steering column is set to collapse, the column collapse is tracked
alongside, and after collapse the force decays with the remaining collapse
distance.

> **NOTE:** The airbag model turns itself off, with a message, in two circumstances: if the computed bag pressure goes negative, and if the computed rates of change of pressure or radius become very large, which is taken as numerical instability. In both cases the bag stops producing force for the remainder of the run and the simulation continues without it, so any run carrying one of these messages should be re-examined — the occupant kinematics after that point are those of an unrestrained occupant. See the Vehicle Data Report for the airbag parameters in use.

## Numerical Integration

Integration proceeds in two stages, both selectable in the calculation options
(see [Calculation Options for EDHIS](../../10-calculation-options/CalcOptionsEDHIS.md)).

A **starting method** generates the first few points, since a
predictor-corrector method needs a history before it can run. The choices are
Euler, Runge-Kutta-Ralston (the default, listed in the dialog as *Modified
Runge-Kutta*) and classical fourth-order Runge-Kutta.

A **predictor-corrector method** then carries the solution forward. The choices
are Adams-Bashforth/Adams-Moulton, and Milne with Hamming's modification (the
default). The Hamming modification blends the predicted and corrected values
rather than accepting the corrector outright, which suppresses the instability
that the plain Milne corrector is prone to.

The step size is controlled by comparing the predictor against the corrector.
The measure is a weighted sum, over the degrees of freedom, of the difference
between the predicted and corrected velocities:

$$\varepsilon = \sum_i w_i\left|v_i - \hat{v}_i\right|$$

and it is tested against the user-entered **Velocity Convergence** parameter:

- $\varepsilon$ **greater than** the parameter — the step is rejected, the
  timestep is halved and the step retried. Exceeding the allowed number of
  halvings ends the run with an integration error.
- $\varepsilon$ **at or below** the parameter — the step is accepted.
- $\varepsilon$ **at or below one fiftieth** of the parameter — the step is
  accepted and the timestep is then **doubled**, on the grounds that the
  solution is far more converged than it needs to be.

Two guards restrain the doubling: at least seven points must have been accepted
at the current step size, and the doubled step must not skip past the next
output time. The effective timestep therefore contracts sharply through a hard
contact and relaxes again afterwards, without the output interval drifting.

### The two change limits

Before the corrector is evaluated, two further stability tests are applied.
Either one, if failed, halves the timestep and retries the step in exactly the
same way as a convergence failure; neither one stops the run.

The first compares the velocity change implied by the current accelerations
over the current step against the **Acceleration Change Limit**:

$$\Delta t\sum_i w_i\left|a_i\right| > Limit_{Accel} \;\Rightarrow\; \text{halve}$$

The second compares the current accelerations against a four-point
extrapolation of them, and so measures how far the acceleration is departing
from a smooth curve. Writing $\tilde{a}$ for the extrapolated value, the step is
halved when

$$\sum_i w_i\left|\tilde{a}_i - a_i\right| > Limit_{Vel}
  \quad\text{and}\quad
  \frac{\sum_i w_i\left|\tilde{a}_i - a_i\right|}{\sum_i w_i\left|a_i\right|}
  > Limit_{Vel}$$

that is, both the absolute departure and its size relative to the accelerations
themselves must exceed the **Velocity Change Limit**. Entering zero for either
limit turns that test off.

> **NOTE:** Both parameters are stability tolerances rather than physical limits, and the quantity each is compared against — given by the equations above — is not the one its name would suggest. Use the equations, not the names, when choosing values: tighten a limit if a run shows a sudden unphysical jump, and loosen it if the timestep is being driven down without benefit.

## Injury Measures

EDHIS accumulates several measures during the run and compares each against the
corresponding tolerance carried by the human. Where a measure exceeds its
tolerance, the time and magnitude are recorded and reported.

### Head severity index

The measure the report labels *Head Injury Criterion* is computed as

$$SI = \int_0^T \left|a_{AP}\right|^{2.5}\,dt$$

where $a_{AP}$ is the **anterior-posterior component** of the head acceleration.

> **NOTE:** This is the Gadd Severity Index form, and three properties of it are worth knowing before quoting the number as HIC. It is accumulated over the **whole run** rather than maximized over a sliding window; it uses the fore-aft **component** of head acceleration rather than the resultant; and it is not divided by the averaging interval. The Head Injury Criterion as defined in FMVSS 208 differs on all three points and will not generally produce the same value. Compare the reported figure against the tolerance carried by the human, which is expressed on the same basis, rather than against a published HIC limit.

### Other measures

| Reported as | What is actually compared |
|---|---|
| Head pitch concussion | Pitch angular acceleration of the head relative to the torso — that is, of the neck articulation, not of the head in space |
| Head side acceleration | Lateral component of head acceleration |
| Chest force | Largest contact force on the chest ellipsoid at this timestep |
| Chest forward acceleration | Anterior-posterior component of chest acceleration |
| Chest SI | **Superior-inferior** (vertical) component of chest acceleration — despite the abbreviation, this is an acceleration and not a severity index |
| Axial femur load | Largest contact force on the knee ellipsoid at this timestep — no load is computed within the femur itself |
| Torso belt load, lap belt load | Sum of the tensions in the belt segments |
| Joint angles | Each joint angle against separate flexion and extension tolerances |

*(updated: this chapter previously consisted of a short summary with no equations. The relationships above were taken from the current EDHIS engine. Note in particular the two naming points called out above — the head measure is a severity index rather than HIC, and Chest SI is the superior-inferior acceleration.)*

---
*Previous: [Chapter 3 — Program Output](03-program-output.md) | Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md)*

<!-- NAV -->

---

← Previous: [Chapter 3 — EDHIS Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md) →

<!-- /NAV -->
