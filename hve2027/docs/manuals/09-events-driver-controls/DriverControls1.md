# Driver Controls Path Follower Method

The path correction method is chosen on the **Method** tab of the
**Path Follower** dialog (**Event › Path Follower...**), and its parameters are
entered on the **Steering** tab. See
[Driver Controls Path Follower](DriverControls7.md) for the dialog as a whole.

**Path Method** (Method tab) — **Variable Steer** or **Variable Torque**.

## Variable Steering

The path correction is accomplished by means of a steering correction. On the
**Steering** tab:

- **Initial Steer (deg)** — initial steering-wheel angle at driver start time.
- **Max Steer Vel (deg/s)** — limit on steering-wheel velocity (how fast the
  driver can turn the wheel).
- **Steer Correction** — amount of steering correction per unit of path error.
- **Steer Damping** — steering correction damping, used to limit steering
  activity.

## Variable Torque

The path correction is accomplished by means of a torque applied at the
steering wheel. On the **Steering** tab:

- **Initial Torque** — initial steering-wheel torque at driver start time.
- **Max Steer Torque** — limit on steering-wheel torque.
- **Torque Correction** — amount of steering torque correction per unit of path
  error.
- **Torque Damping** — torque correction damping, used to limit steering
  activity.

Torques are shown in the units set in Preferences.

!!! note "HVE 2027"
    **Variable Torque** can be selected in HVE 2027 (HVE disabled it). Its
    **Initial Torque** is carried to the engine but no engine reads it — in HVE
    either; the dialog says so. The other three torque parameters are read.

<!-- NAV -->

---

← Previous: [Driver Controls](DriverControls.md)  |  [Index](README.md)  |  Next: [Driver Controls Wheel Data](DriverControls2.md) →

<!-- /NAV -->
