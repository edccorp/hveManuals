# Position/Velocity Dialog Box

This dialog box allows the user to assign positions and velocities for each human and vehicle in the current event. Positions and velocities may be entered for one or more locations along the object's path, according to the requirements of the event's calculation method.

This dialog box contains the following items.

## Path Location

The combo box contains the following items:

- **Initial** — Position and velocity of the selected human or vehicle at the beginning of execution.
- **Begin Perception** — Position and velocity of the selected human or vehicle at the beginning of perception (normally the initial part of the perception/reaction period for a driver about to begin an accident avoidance maneuver).
- **Begin Braking** — Position and velocity of the selected human or vehicle when the brakes are applied.
- **Impact** — Position and velocity of the selected human or vehicle at the time of impact.
- **Separation** — Position and velocity of the selected human or vehicle at the time of separation.
- **Point On Curve** — Position and velocity of the selected human or vehicle on a curved path following separation.
- **End of Rotation** — Position and velocity of the selected human or vehicle at the end of the rotating/lateral skidding phase.
- **Final/Rest** — Position and velocity of the selected human or vehicle at the end of the post-impact path.

Which path locations may be edited depends on the current calculation method; locations not used by the method are disabled.

## Position

The Position group contains the following items:

- **X** — Linear X distance from the earth-fixed origin (vehicles and human pedestrians) or vehicle-fixed origin (human occupants).
- **Y** — Linear Y distance from the earth-fixed origin (vehicles and human pedestrians) or vehicle-fixed origin (human occupants).
- **Z** — Linear Z distance from the earth-fixed origin (vehicles and human pedestrians) or vehicle-fixed origin (human occupants).
- **Roll** — Angular displacement about the vehicle-fixed X or human segment-fixed X axis. For trailers and human segments other than the pelvis, these angles are articulation angles relative to the upstream vehicle or human segment.
- **Pitch** — Angular displacement about the vehicle-fixed Y or human segment-fixed Y axis. For trailers and human segments other than the pelvis, these angles are articulation angles relative to the upstream vehicle or human segment.
- **Yaw** — Angular displacement about the vehicle-fixed Z or human segment-fixed Z axis. For trailers and human segments other than the pelvis, these angles are articulation angles relative to the upstream vehicle or human segment.

## Velocity is Assigned

If you want to assign the velocity of the human or vehicle at the current path location, check this box and enter the velocity. When unchecked, all velocity fields are disabled. When checked for a vehicle whose total velocity is zero, an initial velocity vector is created for on-screen editing.

## Velocity

This group contains the following items:

- **Total** — Total linear velocity of the vehicle or human. The U and V components are computed automatically from the Total velocity and the Sideslip angle.
- **U** — Linear velocity component in the vehicle-fixed or human segment-fixed forward direction. This field is auto-computed from Total, Sideslip and W, but remains editable.
- **V** — Linear velocity component in the vehicle-fixed or human segment-fixed lateral direction. This field is auto-computed from Total, Sideslip and W, but remains editable.
- **W** — Linear velocity component in the vehicle-fixed or human segment-fixed vertical direction.
- **Sideslip** — Angle (deg) between the total velocity vector and the vehicle-fixed (or segment-fixed) x-axis heading. Editing the sideslip angle recomputes the U and V velocity components.
- **Roll** — Angular velocity about the vehicle-fixed X or human segment-fixed X axis. For trailers and human segments other than the pelvis, these are articulation rates relative to the upstream segment.
- **Pitch** — Angular velocity about the vehicle-fixed Y or human segment-fixed Y axis. For trailers and human segments other than the pelvis, these are articulation rates relative to the upstream segment.
- **Yaw** — Angular velocity about the vehicle-fixed Z or human segment-fixed Z axis. For trailers and human segments other than the pelvis, these are articulation rates relative to the upstream segment.

> **Note:** For 2-dimensional calculation methods, the W, Roll rate and Pitch rate fields are disabled.

## Apply

Applies the currently displayed position and velocity values to the selected object and updates the object's display in the event editor.

---
*Source topic: PosVelDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Inter-Vehicle Connections Dialog](IntrVehConnsDlg.md)  |  [Index](README.md)  |  Next: [Simulation Controls Dialog Box](SimuCtrlDlg.md) →

<!-- /NAV -->
