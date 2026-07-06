# Driver Controls Path Follower

The HVE Driver page allows the vehicle simulation to determine the steering, throttle and braking inputs required to follow a user-defined path (and, optionally, user-defined speeds along the path).

## Use Path Follower

When checked, the HVE Driver model is enabled for the current vehicle and the tabs below become available. When unchecked, the driver inputs come from the Steer, Brake and Throttle tables.

## Model

Selects the version of the HVE Driver model to use: **Ver. 1** or **Ver. 2**. These radio buttons are enabled only when *Use Path Follower* is checked.

The page contains five tabs:

## Path Source

Selects the source of the target path data:

- **Position/Velocity Dialog** — the path is defined by the positions entered in the [Position/Velocity Dialog](PosVelDlg.md) (path points placed in the event editor).
- **Table** — reserved for entering path coordinates in a table. This option is currently disabled.

## Driver

Driver properties (each entered with a slider or edit field):

- **Driver Start Time (sec)** — Time at which the driver model begins acting.
- **Driver Sample Interval (sec)** — Interval at which the driver model samples the vehicle's position relative to the path.
- **Driver Preview Time (sec)** — How far ahead of the vehicle (in time) the driver is looking when computing the path correction.
- **Driver Minimum Preview Distance (ft)** — Lower limit on the preview point distance ahead of the vehicle, used at low speeds.
- **Path Error Null Distance (ft)** — Maximum allowable lateral path error; the driver steers to null path errors within this distance.
- **Max Speed Error (mph)** — Allowable difference between the current speed and the desired speed (used by the speed follower).
- **Driver Comfort Level (g)** — Maximum lateral acceleration the driver will tolerate when following the path.

## Method

Path correction method (Variable Steering or Variable Torque). See [Driver Controls Path Follower Method](DriverControls1.md).

## Speed

Speed follower parameters. See [Driver Controls Speed Follower](DriverControls8.md).

## Filter

Neuro-muscular filter parameters. See [Driver Controls Filter](DriverControls6.md).

---
*Source topic: DriverControls7.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Filter](DriverControls6.md)  |  [Index](README.md)  |  Next: [Driver Controls Speed Follower](DriverControls8.md) →

<!-- /NAV -->
