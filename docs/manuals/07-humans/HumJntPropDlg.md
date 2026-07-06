# Human Joint Properties Dialog Box

Each joint is defined by a number of physical properties. This dialog is used to view and edit those properties; it is opened with the Properties button in the [Joint Data Dialog Box](Human3.md). The dialog title bar shows the current human's name and the selected joint. Except for the joint type, each property is entered separately for rotation about the joint's i, j and k axes.

This dialog box contains the following items:

## Joint Type

**Ball and Socket**
Sets the joint type to ball and socket.

**Hinge**
Sets the joint type to hinge.

## Rotation About (i Axis / j Axis / k Axis)

**Stop Angle for + Axis Rotation (deg)**
The angle at which the joint stop is applied for positive i, j and k segment rotations.

**Stop Angle for - Axis Rotation (deg)**
The angle at which the joint stop is applied for negative i, j and k segment rotations.

**Stop Elasticity For + Axis Rotation (in-lb/deg)**
Joint stop linear elastic property for positive rotations about the i, j and k axes.

**Stop Elasticity For - Axis Rotation (in-lb/deg)**
Joint stop linear elastic property for negative rotations about the i, j and k axes.

**Stop Energy Dissipation**
Ratio of dissipated to total energy of the joint stop.

**Linear Elastic Coefficient (in-lb/deg)**
Joint linear elastic property during the normal range of motion for rotations about the i, j and k axes.

**Quadratic Elastic Coefficient (in-lb/deg²)**
Joint quadratic elastic property during the normal range of motion for rotations about the i, j and k axes.

**Cubic Elastic Coefficient (in-lb/deg³)**
Joint cubic elastic property during the normal range of motion for rotations about the i, j and k axes.

**Damping Constant (in-lb-sec/deg)**
Joint damping property during the normal range of motion for rotations about the i, j and k axes.

**Full Damping Angular Velocity (deg/sec)**
Angular velocity required to achieve full joint damping.

## Joint Injury Tolerance

**Max Angle For + Axis Rotation (deg)**
The positive joint angle which, if exceeded, is predicted to cause injury to the joint.

**Max Angle For - Axis Rotation (deg)**
The negative joint angle which, if exceeded, is predicted to cause injury to the joint.

All values are range-checked when OK is pressed; out-of-range values must be corrected before the dialog will close.

---
*Source topic: HumJntPropDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Human CG Dialog Box](HumCGDlg.md)  |  [Index](README.md)  |  Next: [Human Material Properties Dialog Box](HumMatProp.md) →

<!-- /NAV -->
