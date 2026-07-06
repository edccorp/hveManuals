# Chapter 4 — EDSVS Calculation Method

## Basis for Analysis

EDSVS is a dynamic analysis of vehicle motion in the horizontal (yaw) plane. Using the standard engineering approach, the equations of motion are written from a free-body analysis. The mathematical model for EDSVS was developed and validated at the University of Michigan Transportation Research Institute [1-3, 14], and extended by EDC [25].

For successful use of EDSVS, a good understanding of vehicle dynamics is extremely useful and is recommended. However, the following discussion is limited to the general analytical approach. For a detailed treatise on the subject of vehicle dynamics and simulation programs, the user is referred to the references listed at the end of this Physics Manual as well as those listed in HVE-2D Appendix VII, References.

### Equations of Motion

The 3-degree of freedom analysis solves the equations of motion in the horizontal (yaw) plane. In this plane, the vehicle x- and y- linear motion can be analyzed, as well as angular rotation about the z-axis, where the coordinates are specified with respect to the vehicle-fixed coordinate system (see HVE-2D Appendix III, Coordinate Systems; for more information, refer to SAE J670e - Vehicle Dynamics Terminology [6.2], portions of which are found in the Help Index).

The required equations of motion are written below:

$$m(\dot{u} - vr) = \Sigma F_x$$

$$m(\dot{v} + ur) = \Sigma F_y$$

$$I_{zz}\dot{r} = \Sigma M_z$$

where:

| Symbol | Meaning |
|---|---|
| $m$ | total mass |
| $I_{zz}$ | total yaw moment of inertia |
| $u$ | forward velocity (vehicle-fixed component) |
| $v$ | lateral velocity (vehicle-fixed component) |
| $r$ | angular yaw velocity |
| $\Sigma F_x$ | summation of external forces in the x-direction |
| $\Sigma F_y$ | summation of external forces in the y-direction |
| $\Sigma M_z$ | summation of external moments about the z-axis |

EDSVS solves these equations of motion at discrete time intervals (specified by the vehicle trajectory integration timestep, see User's Manual, Simulation Controls). The current accelerations are integrated, using numerical integration, to predict velocity and position at the start of the next timestep. EDSVS uses a *predictor-corrector* integration method that helps to ensure stable results. A predictor-corrector method estimates the future position and velocity based on the current acceleration history, and then, once they are calculated, compares the predicted results with the calculated results.

There are no degrees of freedom (and hence no equations of motion) for vertical motion, or pitch or roll rotation. Therefore, suspension dynamics cannot be studied directly. However, EDSVS considers the suspension as it affects tire forces by using the *roll couple distribution* (the ratio of lateral load transferred at the front and rear suspensions during cornering). The CG elevation above ground is used in conjunction with longitudinal and lateral accelerations to compute quasi-static load transfers due to pitch and roll, respectively.

## Tire Forces

All of the external forces applied to the vehicle which direct its motion are applied at the tires. Therefore, accurate computation of these forces is essential. Unfortunately, pneumatic tires do not behave in an easy-to-calculate manner. Rather, these properties are functions of several variables and are extremely non-linear.

Historically, two methods have been used to compute tire forces. Either formulas utilizing experimental coefficients are used (this method is referred to as a *tire model*) or tables containing test data at various speed and load conditions are applied according to the current speed and load conditions (this method is referred to as a *table look-up*). EDSVS uses the Fiala tire model [5] to compute the lateral forces on a free rolling tire. This model has been used in many popular simulations developed at Calspan [8]. Using this model, the tire forces are computed for the current integration timestep as follows:

| Symbol | Meaning |
|---|---|
| $C_\alpha$ | tire cornering stiffness (lb/radian) |
| $\alpha$ | tire slip angle (radians) |
| $F_z$ | tire vertical force (lb) |
| $F_{sx}$ | attempted brake or acceleration force (lb) |
| $\mu_p$ | peak coefficient of friction |
| $\mu_s$ | slide coefficient of friction |
| $\mu_{slip}$ | % slip at $\mu_p$ |
| $IsDual$ | flag (1 if dual tires; 0 otherwise) |
| $sign.fsx$ | determines direction of wheel force relative to vehicle |

At the current simulation time, the force is computed for each tire, one tire at a time. If the percent wheel lock-up method was used to supply wheel forces when entering the Brake and/or Throttle Table, the percent lock-up must be converted into the actual wheel force:

$$\text{if } |F_{sx}| < 1.0 \text{ then } F_{sx} = F_{sx}\,\mu_p F_z (1 + IsDual)$$

The attempted wheel force is assigned as the longitudinal wheel force (lb),

$$F_x = F_{sx} \cdot sign.fsx$$

where $sign.fsx$ determines the direction of the wheel force relative to the vehicle-fixed coordinate system.

Next, the non-dimensional sideslip parameter, $\bar{\alpha}$, is determined as

$$\bar{\alpha} = C_\alpha \sin(\alpha) / (\mu_p F_z)$$

If $|\bar{\alpha}|$ is equal to or greater than 3, the tire's ability to produce a cornering force, $F_y$ (lb), is saturated. In this case,

$$F_y = -\mu_p F_z (1 + IsDual)\,\text{sign}(\bar{\alpha})$$

Since the tire is saturated, it is assumed to be generating a scuff mark due to the excessive lateral forces, and the skid flag is turned on.

Otherwise, $|\bar{\alpha}|$ is less than 3, and the Fiala tire model computes the lateral force, $F_y$, using a 3rd-order polynomial in $\bar{\alpha}$:

$$F_y = -\mu_p F_z \left(\bar{\alpha} - \frac{\bar{\alpha}\,|\bar{\alpha}|}{3} + \frac{\bar{\alpha}^3}{27}\right)(1 + IsDual)$$

In this case, the tire is operating within its traction limits, and the skid flag is turned off.

In either case, the direction of the lateral force, $F_y$, is determined by the sign of $\bar{\alpha}$.

Next, a potential reduction in tire forces, $F_x$ and $F_y$, due to the amount of lateral tire slip is determined. $\mu_p$ is modified by the tire slip angle, $\alpha$:

$$\mu_{mod} = \mu_p (1 - 1.72\,|\alpha|)$$

If $\mu_{mod} < |\mu_s \cos(\alpha)|$ then

$$\mu_{mod} = |\mu_s \cos(\alpha)|$$

The attempted longitudinal wheel force, $F_x$ (see above), is compared to available force at the current slip angle, $\alpha$. This available force, $F_{max}$ (lb) is

$$F_{max} = \mu_{mod} F_z (1 + IsDual)$$

If the attempted force, $F_x$, is less than $F_{max}$, the skid flag is turned off and the amount of longitudinal tire slip, $S$, is computed:

$$\mu_x = \left| F_x / (F_z\,(1 + IsDual)) \right|$$

$$S = (\mu_x / \mu_p)\,\mu_{slip}$$

The longitudinal tire slip, $S$, is used in the slip vs. rolloff table to determine the reduction in lateral tire force, $F_y$. The following table illustrates this effect for typical tires [14]:

| Slip, S | Rolloff |
|---|---|
| 0.00 | 1.00 |
| 0.05 | 0.88 |
| 0.10 | 0.64 |
| 0.15 | 0.46 |
| 0.20 | 0.33 |

Linear interpolation is used to determine the amount of rolloff for values of slip between the table values of $S$. The computed lateral force, $F_y$, is then adjusted by the rolloff:

$$F_y = F_y \cdot Rolloff$$

If the attempted longitudinal wheel force, $F_x$, is greater than $F_{max}$, the longitudinal slip exceeds the slip at $\mu_p$ and the tire is either locked (braking) or spinning (accelerating). The skid flag is turned on and the forward and lateral tire forces are:

$$F_x = \mu_s \cos(\alpha) F_z (1 + IsDual)\,sign.fsx$$

$$F_y = -\mu_s \sin(\alpha) F_z (1 + IsDual)$$

## Antilock Model

EDSVS allows the use of a simple antilock model to study the effects of improvements due to *perfect braking*. Perfect braking is defined as "braking which maintains the longitudinal braking force at the level associated with the peak friction coefficient". Under normal conditions (without antilock), it is nearly impossible to hold this level of braking. The tire locks up, thus causing a reduction in brake force from that associated with the peak friction coefficient to that associated with the slide friction coefficient.

The Vehicle Brake Model includes an antilock effectiveness coefficient, $\eta_a$, which defines the effectiveness of the antilock system; an antilock coefficient equal to 0.0 is the same as no antilock, while a coefficient equal to 1.0 defines the perfect system. The same antilock coefficient applies to both longitudinal and lateral tire forces. The antilock parameters are assigned using the Vehicle Editor's Wheel Brake dialog (see User's Manual, Section 4 (Vehicle Editor) for more information).

The antilock model is only applicable if the attempted brake force, $F_x$, is greater than $F_{max}$ (see above). Under this condition, an additional amount of force, $\Delta F$, is generated because of the difference between $\mu_p$ and $\mu_s$. For longitudinal tire force:

$$\Delta F_x = (\mu_p - \mu_s)\cos(\alpha)\,F_z\,sign.fsx\,(1 + IsDual)\,\eta_a$$

$$F_x = \mu_s F_z (1 + IsDual)\cos(\alpha)\,sign.fsx + \Delta F_x$$

For lateral tire force:

$$\Delta F_y = \left(F_y + \mu_s F_z (1 + IsDual)\sin(\alpha)\right)\eta_a$$

$$F_y = -\mu_s F_z (1 + IsDual)\sin(\alpha) + \Delta F_y$$

## Assumptions

In order to provide a useful analysis without becoming burdensome and overly complex, EDSVS makes several simplifying assumptions. If EDSVS is to be properly used, it is important these assumptions and their consequences be understood. In some cases, data which violate these assumptions will cause a fatal error, along with a message indicating the reason for the error. In other cases, the error is not with the data but with the use of the program under conditions which violate the assumptions inherent to the computations. EDSVS will issue results which may not be valid for the given circumstances.

Before using EDSVS, be sure the events you wish to simulate are within the scope of the program analysis defined by the following assumptions:

### No Rollover Allowed

EDSVS is a yaw plane analysis and does not consider roll or pitch degrees of freedom. The analysis is only valid while all wheels are generating a positive (downward) force on the road surface. As soon as a wheel load becomes negative, wheel lift-off is assumed and computations are halted. A warning message will be displayed indicating the time at which wheel lift-off occurred and the wheel that lifted.

### No Suspension Effects

EDSVS assumes the wheels remain vertical at all times. Therefore, camber stiffness does not contribute to lateral force generation. There is no roll degree of freedom, so bump steer and roll steer are also ignored. (See Roll Couple Distribution for information about how the suspension affects the front/rear distribution of lateral forces.)

### All External Forces Applied At Tires

Aerodynamic effects are ignored. This assumption may become a significant factor at excessive speeds. In addition, undercarriage contact with the ground caused by impact-related damage is not considered.

### Small Angle Assumption for Roll and Pitch

> **HVE:** EDSVS has been extended for use in the HVE 3-D environment to include a gravity vector. Thus, vehicle motion on sloped surfaces may be accommodated. However, the model is valid only for small roll and pitch angles. If the allowable angle (normally 15 degrees) is exceeded, a message is issued (*Excessive Roll or Pitch*) and the run is terminated (see below).

### Roll/Pitch Not Greater Than 15 Degrees

> **HVE:** EDSVS uses the small angle assumption; if the roll and/or pitch exceed about 15 degrees, errors may become significant. To prevent this problem, EDSVS returns a fatal message under this condition.

---

[Previous: Chapter 3 — Program Output](03-program-output.md) | [Contents](README.md) | [Next: Chapter 5 — EDSVS Tutorial](05-tutorial.md)

<!-- NAV -->

---

← Previous: [Chapter 3 — EDSVS Program Output](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDSVS Tutorial](05-tutorial.md) →

<!-- /NAV -->
