# Driver Controls Speed Follower

The Speed tab of the HVE Driver (Path Follower) page controls the speed follower. User-entered velocities at each path position are used to define an attempted speed at each point on the path; the driver model applies throttle and brake pedal inputs to achieve those speeds.

## Use Speed Follower

When checked, the speed follower is enabled and the throttle and brake parameters below become available. (The allowable speed error is entered as *Max Speed Error* on the Driver tab.)

## Throttle

- **Initial Throttle Pedal (%/100)** — Throttle pedal position at driver start time.
- **Max Throttle Pedal (%/100)** — Maximum allowable throttle pedal position.
- **Throttle Correction (%-sec/100-in)** — Amount of throttle pedal correction per unit of speed error.
- **Throttle Damping** — Throttle correction damping, used to limit throttle activity.

## Brake

- **Initial Brake Pedal Force (lb)** — Brake pedal force at driver start time.
- **Max Brake Pedal Force (lb)** — Maximum allowable brake pedal force.
- **Brake Correction (lb-sec/in)** — Amount of brake pedal force correction per unit of speed error.
- **Brake Damping** — Brake correction damping, used to limit braking activity.

## Delay To Switch Pedals (sec)

Time required for the driver to move between the throttle pedal and the brake pedal.

Each parameter is entered with a slider or by typing directly into the associated edit field.

---
*Source topic: DriverControls8.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Path Follower](DriverControls7.md)  |  [Index](README.md)  |  Next: [Event Information Dialog Box](EventInfo.md) →

<!-- /NAV -->
