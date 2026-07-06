# Spindle Axis Dialog

The spindle axis geometry properties for the selected wheel location are displayed and edited using this dialog box. The dialog is available only for steerable axles (the Spindle Axis button on the Suspension Data dialog is disabled otherwise). The dialog title identifies the current axle and side.

This dialog box contains the following parameters:

## Alignment

**Caster (deg)**
The fore-aft angle of the spindle axis. This angle is largely responsible for the self-aligning properties of a steerable axle.

**King Pin Inclination (deg)**
The sideways angle of the spindle axis. This angle, along with the caster angle, is responsible for the self-aligning properties of the steerable axle.

**Steering Offset (in)**
The distance from the center of the tire contact patch to the point where the steering axis intersects the ground at equilibrium conditions. This distance produces a steering torque (positive or negative, depending on the sign of the scrub radius) due to longitudinal tire force (either braking or driving).

**Stub Axle Length (in)**
The length of the stub axle (spindle) from the steering axis to the wheel plane.

*(This parameter was added since the original help topic was written.)*

**Toe-In (in)**
The difference in distance between the center of the tire plane at the spindle and the front of the tire.

**Steer Axis Friction Torque (ft-lb)**
Constant (coulomb) friction torque about the steer axis. Rotation of the wheel about the steering axis is resisted by this torque, which must be overcome before the wheel steers.

*(The original help left this entry blank; the description above is derived from the code.)*

## Steering Stops

Separate stop data are stored for right and left steer; the two radio buttons select which stop's parameters are displayed in the fields below.

**Steering: Right (+)**
Selects the right (positive) steering stop for display and editing.

**Steering: Left (−)**
Selects the left (negative) steering stop for display and editing.

**Stop Angle (deg)**
The vehicle-fixed steering angle at which the stop is reached.

**Stop Linear Stiffness (ft-lb/deg)**
The mechanical stiffness of the steering stop. Additional steering beyond the stop angle is resisted by a torque that attempts to return the wheel towards zero steer.

**Stop Energy Ratio**
The ratio of conserved to total energy of the selected steering stop, between 0 and 1 (this property is analogous to the Jounce and Rebound stop energy ratio). This parameter keeps the wheel from bouncing off the steering stop.

---
*Source topic: SpndleAxisDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Roll Steer Properties](RollSteerNewDlg.md)  |  [Index](README.md)  |  Next: [Springs and Shocks Dialog](SprindShocksDlg.md) →

<!-- /NAV -->
