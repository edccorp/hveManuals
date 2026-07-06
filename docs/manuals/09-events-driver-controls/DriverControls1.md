# Driver Controls Path Follower Method

The Method tab of the HVE Driver (Path Follower) page selects how the path correction is accomplished. Two methods are defined:

## Variable Steering

The path correction is accomplished by means of a steering correction. The user supplies the following data:

- **Initial Angle (deg)** — Initial steering wheel angle at driver start time.
- **Max Velocity (deg/sec)** — Limit on steering wheel velocity (how fast the driver can turn the wheel).
- **Correction Factor (deg/sec)** — Amount of steering correction per unit of path error (steering correction rate).
- **Correction Damp (deg)** — Steering correction damping, used to limit steering activity.

## Variable Torque

The path correction is accomplished by means of a torque application at the steering wheel. In this case the user supplies the following data:

- **Initial Steering Torque (in-lb)** — Initial steering wheel torque at driver start time.
- **Max Steering Torque (in-lb)** — Limit on steering wheel torque.
- **Torque Correction Factor (in-lb/in)** — Amount of steering torque correction per unit of path error.
- **Torque Damping (in-lb-sec/in)** — Torque correction damping, used to limit steering activity.

> **Note:** The Variable Torque option is currently disabled in the user interface; Variable Steering is the available path follower method.

---
*Source topic: DriverControls1.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls](DriverControls.md)  |  [Index](README.md)  |  Next: [Driver Controls Wheel Data](DriverControls2.md) →

<!-- /NAV -->
