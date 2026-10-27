# Driver Controls Path Follower Method

The path follower corrects the vehicle's path by **steering**: HVE's Variable
Steering method. Its parameters are the **Steering** section of the **Path
Follower** tab of Driver Controls (**Event › Path Follower...**). See
[Driver Controls Path Follower](DriverControls7.md) for the dialog as a whole.

## Variable Steering

The path correction is accomplished by means of a steering correction:

- **Initial Steer (deg)** — initial steering-wheel angle at driver start time.
- **Max Steer Vel (deg/s)** — limit on steering-wheel velocity (how fast the
  driver can turn the wheel).
- **Steering Correction Rate (deg/s)** — amount of steering correction per
  unit of path error.
- **Steering Correction Damping (deg)** — steering correction damping, used to
  limit steering activity.

!!! warning "Not in HVE Studio: Variable Torque"
    HVE's second method, Variable Torque, corrects the path with a
    steering-wheel torque. HVE's own dialog disables it, and it does not work
    in the engine: the torque the driver model computes is handed to the
    vehicle as a steer *angle*. Measured on a SIMON path follower at 13 m/s,
    every torque setting tried turned the front wheels 15° to 154° within
    0.1 s and stopped the run on the driver comfort level. HVE Studio does not
    offer it. A case imported from HVE that chose it runs as Variable Steering,
    and the import notes say so.

<!-- NAV -->

---

← Previous: [Driver Controls](DriverControls.md)  |  [Index](README.md)  |  Next: [Driver Controls Wheel Data](DriverControls2.md) →

<!-- /NAV -->
