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
contact surface. A surface is a plane with a defined extent, and each surface
carries a flag stating which side of it the occupant is expected to be on.
Where an ellipsoid has passed into the surface, the **penetration**, $\delta$, is
the depth of that intrusion measured along the surface normal, reduced by the
surface's **edge constant**, which offsets the point at which force begins to
develop.

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

## Airbag Model

When an airbag is specified, its inflation is solved alongside the occupant
equations rather than prescribed. The bag is treated as a volume of gas with a
mass inflow rate, inflating until either its maximum volume is reached or the
gas shut-off time arrives, whichever comes first. A vent opens once the internal
pressure exceeds the user-entered vent pressure, and discharges through the vent
area modified by the discharge coefficient, with the flow depending on the ratio
of atmospheric to internal pressure and on the ratio of vent radius to bag
radius. Once the occupant contacts the bag, the bag's deformation and the
occupant's motion are coupled, and the contact force follows from the current
bag pressure and contact area.

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

The timestep is halved when the solution fails to meet the convergence
requirement and restored when it is comfortably met, so the effective step
follows the severity of the contact.

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
| Head pitch concussion | Head pitch angular acceleration |
| Head side acceleration | Lateral component of head acceleration |
| Chest force | Largest contact force on the chest ellipsoid at this timestep |
| Chest forward acceleration | Anterior-posterior component of chest acceleration |
| Chest SI | **Superior-inferior** (vertical) component of chest acceleration — despite the abbreviation, this is an acceleration and not a severity index |
| Knee load | Largest contact force on the knee ellipsoid |
| Torso belt load, lap belt load | Sum of the tensions in the belt segments |
| Joint angles | Each joint angle against separate flexion and extension tolerances |

*(updated: this chapter previously consisted of a short summary with no equations. The relationships above were taken from the current EDHIS engine. Note in particular the two naming points called out above — the head measure is a severity index rather than HIC, and Chest SI is the superior-inferior acceleration.)*

---
*Previous: [Chapter 3 — Program Output](03-program-output.md) | Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md)*

<!-- NAV -->

---

← Previous: [Chapter 3 — EDHIS Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDHIS Tutorial](05-tutorial.md) →

<!-- /NAV -->
