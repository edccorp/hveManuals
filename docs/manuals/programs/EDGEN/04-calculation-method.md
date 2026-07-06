# Chapter 4 — Calculation Method

## Basis for Analysis

EDGEN is a 3-dimensional kinematic spreadsheet. It is similar to a simulation program, in that it requires initial conditions (positions and velocities). However, it differs significantly from a simulation program in that it does not compute forces and resulting accelerations to determine velocity and position. Rather, EDGEN requires a user-entered velocity for each assigned position, then computes the average acceleration between the assigned positions.

### Equations of Motion

The 6-degree of freedom analysis solves the equations of motion in three dimensions (*X, Y, Z, Yaw, Pitch, Roll*).

> **NOTE:** The order of rotations is Yaw, Pitch, Roll; because 3-D rotations are non-commutative, the order of rotations makes a difference.

Coordinate systems are described in detail in HVE Appendix III, Coordinate Systems; for more information, refer to SAE J670e - Vehicle Dynamics Terminology [6.2].

The required equations of motion are described below.

### Generalized Equations

In the following development, $s$ represents a generalized position vector. As a generalized vector, it may represent X, Y or Z coordinates or $\Phi$, $\Theta$, or $\Psi$ angles. Similarly, $v$ represents a generalized velocity vector and $a$ represents a generalized acceleration vector.

To solve the equations of motion, first calculate constant acceleration. In general, the constant acceleration between position $i$ and position $i+1$ is:

$$a_i = \frac{dv}{dt} = \frac{v_i^2 - v_{i+1}^2}{2\,(s_i - s_{i+1})}$$

The time, $dt$, from $s_i$ to $s_{i+1}$ (and from $v_i$ to $v_{i+1}$) is:

$$dt = \frac{dv}{a} = \frac{v_{i+1} - v_i}{a_i}$$

*(Updated: in the current code the segment time is computed equivalently and more robustly as $\Delta t = 2\,\Delta s_{total} / (v_{0,total} + v_{1,total})$ — see `ComputeLinearData()` in `Physics/Source/Edgen/genlinear.cpp` and `ComputeSplineData()` in `genspline.cpp`.)*

In general, given constant $a$, during time interval $dt$, the current velocity, $v$, and position, $s$, are:

$$v(t) = v_i + a\,(t - t_i)$$

$$s(t) = s_i + v_i\,(t - t_i) + \tfrac{1}{2}\,a\,(t - t_i)^2$$

where $a$, $v$ and $s$ are generalized coordinates describing all six degrees of freedom, as described earlier.

EDGEN solves these equations of motion at discrete time intervals specified by the vehicle trajectory integration timestep. The current values for $a$, $v$ and $s$ are written to the output tracks according to the specified output interval (integration time step and output interval are assigned using the Simulation Controls dialog — see User's Manual, Simulation Controls).

EDGEN views the object as a rigid body. Therefore, articulated vehicles are not allowed.

If a human is moved, EDGEN defines the motion of the pelvis segment CG, and articulation of the arms, legs and other HVE human segments is not calculated (the joint angles remain fixed according to the assigned angles).

The time interval between positions is defined by the change in linear velocities, not angular velocities. This assumption has several ramifications:

- The time for linear and angular velocity change are equal.
- The system is over-determined. Angular acceleration between two user-entered angular velocities cannot be calculated because the time increment is fixed.
- To solve the dilemma posed by the first two observations, the assumption is made that the angular acceleration between positions $i$ and $i+1$ is zero, and the angular velocity between positions $i$ and $i+1$ is constant.

*(Updated: the code computes the constant angular velocity for each segment directly from the entered angular positions, $\dot{s}_{ang} = (s_{ang,i+1} - s_{ang,i})/(t_{i+1} - t_i)$; any user-entered angular velocities are overwritten. See `genlinear.cpp`.)*

Finally, the angular position of an object relative to the earth-fixed coordinate system is defined by two angles, $\nu$ and $\alpha$, such that:

$$\nu = \text{Course Angle} = \mathrm{atan2}\!\left(s_{y,i} - s_{y,i-1},\; s_{x,i} - s_{x,i-1}\right)$$

$$\alpha = \text{Zenith Angle} = \arcsin\!\left(\frac{s_{z,i} - s_{z,i-1}}{s_{total}}\right)$$

Given the course angle, $\nu$, and the current heading angle, $s_{\psi,i}$, the current sideslip angle, $\beta$, can be calculated:

$$\beta = \text{Sideslip Angle} = \nu - s_{\psi,i}$$

Given these relationships, the current accelerations are:

$$a_x(t) = a_{total}\cos\beta\,\cos\alpha$$
$$a_y(t) = a_{total}\sin\beta\,\cos\alpha$$
$$a_z(t) = a_{total}\sin\alpha$$

Similarly, current linear velocities are:

$$v_x(t) = v_{total}\cos\beta\,\cos\alpha$$
$$v_y(t) = v_{total}\sin\beta\,\cos\alpha$$
$$v_z(t) = v_{total}\sin\alpha$$

and the current positions are:

$$s_x(t) = s_{x,i-1} + v_{total,i-1}\cos\nu\,\cos\alpha\,(t - t_{i-1}) + \tfrac{a_{total}}{2}\cos\nu\,\cos\alpha\,(t - t_{i-1})^2$$

$$s_y(t) = s_{y,i-1} + v_{total,i-1}\sin\nu\,\cos\alpha\,(t - t_{i-1}) + \tfrac{a_{total}}{2}\sin\nu\,\cos\alpha\,(t - t_{i-1})^2$$

$$s_z(t) = s_{z,i-1} + v_{total,i-1}\sin\alpha\,(t - t_{i-1}) + \tfrac{a_{total}}{2}\sin\alpha\,(t - t_{i-1})^2$$

## Path Interpolation Options

*(Updated: this section reflects the current source code. The equations above describe the default **Linear Interpolation** path model, `PathOption = 0` (`LINEAR`), implemented in `ComputeLinearData()` in `Physics/Source/Edgen/genlinear.cpp`.)*

When the **3-D Spline Interpolation** path model is selected (`PathOption = 1`, `SPLINE`, implemented in `InitializeSpline()` and `ComputeSplineData()` in `Physics/Source/Edgen/genspline.cpp`), EDGEN instead:

- Fits a 3-D spline through the user-entered positions (`Spline3D()`), producing a smooth, continuous path that is tangent-continuous at each node.
- Computes each segment's path length along the curve, `PathLength[i-1]`, and uses it (instead of the straight-line distance) to determine the segment time: $t_i = 2\,\Delta s / (v_{0,total} + v_{1,total}) + t_{i-1}$ and constant total acceleration $a_{total}$.
- At each timestep, evaluates the current distance travelled along the curve, then walks along the spline (using de Casteljau evaluation, `deCast()`, at up to 2000 sample points per segment in 1-inch increments) to locate the current position $X, Y, Z$ directly on the curve.
- Computes the course and zenith angles from the local path tangent vector, $\nu = \mathrm{atan2}(T_y, T_x)$ and $\alpha = \mathrm{atan2}(T_z, \sqrt{T_x^2 + T_y^2})$, rather than from the straight chord between positions.
- Applies the same velocity/acceleration resolutions ($v_x, v_y, v_z, a_x, a_y, a_z$ via $\beta$ and $\alpha$) and the same constant-angular-velocity treatment as the linear model, with one difference: in spline mode the user-entered sideslip angle is folded into the node's yaw orientation before interpolation (`s[...][5] += SlipAngle`, `Geninput.cpp:162-163` for vehicles, `251-252` for humans). The linear model does not apply this offset.

See [Calculation Options](02-program-input.md#calculation-options) and the dialog reference [Calculation Options for EDGEN](../../10-calculation-options/CalcOptEDGENDlg.md).

<!-- NAV -->

---

← Previous: [Chapter 3 — Program Output Results](03-program-output.md)  |  [Index](README.md)  |  Next: [Chapter 5 — EDGEN Tutorial](05-tutorial.md) →

<!-- /NAV -->
