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

The resulting motion is recorded as EDGEN human or vehicle output tracks; the motion is visualized in the 3-D viewport.

## Opening the options

In Event Information, with an EDGEN event active, press **Method Options...**
under Calculation Method. The **EDGEN Options** window opens.

## Interpolation Method (Path Model)

This radio button group selects how EDGEN interpolates the path between the user-entered positions. The default is *Linear Interpolation*.

- **Linear Interpolation** — EDGEN interpolates position and velocity along straight-line segments between successive user-entered positions.
- **3D Spline Interpolation** — EDGEN fits a 3-D spline through the user-entered positions and interpolates position and velocity along the resulting smooth, curved path.

!!! note "HVE 2027"
    The group is titled *Interpolation Method* rather than HVE's *Path Model*.
    The value stored in an imported HVE case is kept.

!!! warning "Not in HVE 2027"
    For a **human** driven by EDGEN, *3D Spline Interpolation* currently gives
    the same path as *Linear*: the spline uses a sideslip angle at each path
    node that the imported human path does not carry. Vehicle paths are
    affected as described above.

<!-- NAV -->

---

← Previous: [Calculation Options for EDCRASH](CalcOptEDCRASHDlg.md)  |  [Index](README.md)  |  Next: [EDSMAC Calculation Options](CalcOptEDSMAC.md) →

<!-- /NAV -->
