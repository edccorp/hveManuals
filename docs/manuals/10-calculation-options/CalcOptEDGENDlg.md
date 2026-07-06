# Calculation Options for EDGEN

EDGEN (**E**ngineering **D**ynamics Corporation **GEN**eral Analysis Tool) is a 3-dimensional kinematics spreadsheet developed by Engineering Dynamics Corporation. EDGEN uses positions and velocities supplied at up to eight user-specified locations (e.g., *Initial, Pre-braking, Impact,* etc.) to determine the time required to travel between each location, and then calculates the current velocity and position at each time step between the user-entered positions.

EDGEN has several applications. For example:

- Time vs. distance studies involving a human or vehicle
- Move a human or vehicle between two or more known positions
- A *reality check* to confirm that data used in key frame animations are reasonable.

As a kinematics model, forces acting on the human or vehicle are not computed.

It is up to the user of EDGEN to review the resulting accelerations and decide if they are reasonable.

When used for a human, EDGEN calculates the motion of the pelvis. Six degrees of freedom (X,Y,Z linear motion, and roll, pitch and yaw angular motion of the pelvis) are calculated. Joint articulations are not included. Therefore, arm and leg motion cannot be simulated.

When used for a vehicle, EDGEN calculates the motion of the sprung mass. Again, six degrees of freedom (X,Y,Z linear motion, and roll, pitch and yaw angular motion) are calculated. Suspension deflection and tire spin degrees of freedom are not included.

The resulting motion is recorded as EDGEN human or vehicle output tracks; the motion is visualized in the 3-D HVE visualization environment.

## Path Model

This radio button group selects how EDGEN interpolates the path between the user-entered positions (internal physics variable `PathOption`, where 0 = `LINEAR` and 1 = `SPLINE`; see `Geninput.cpp` and `genspline.cpp`). The default is *Linear Interpolation*.

- **Linear Interpolation** — EDGEN interpolates position and velocity along straight-line segments between successive user-entered positions (implemented by `ComputeLinearData()` in `genlinear.cpp`).
- **3-D Spline Interpolation** — EDGEN fits a 3-D spline through the user-entered positions and interpolates position and velocity along the resulting smooth, curved path (implemented by `ComputeSplineData()` in `genspline.cpp`).

---
*Source topic: CalcOptEDGENDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Calculation Options for EDCRASH](CalcOptEDCRASHDlg.md)  |  [Index](README.md)  |  Next: [EDSMAC Calculation Options](CalcOptEDSMAC.md) →

<!-- /NAV -->
