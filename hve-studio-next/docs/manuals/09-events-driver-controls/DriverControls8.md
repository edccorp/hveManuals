# Driver Controls Speed Follower

The **Speed Follower** section of the **Path Follower** dialog
(**Event › Path Follower...**) controls the speed follower. The speeds entered
for the waypoints in the **Path** section define an attempted speed at each point on
the path; the driver model applies throttle and brake pedal inputs to achieve
them. See [Driver Controls Path Follower](DriverControls7.md).

## Use Speed Follower

When checked, the speed follower is enabled and the parameters below become
available.

## Parameters

Max Velocity Error, Max Brake Pedal and Initial Brake are shown in the units
set in Preferences; the correction and damping rows are in the units their
labels state. Each value is typed or dragged.

- **Max Velocity Error** — allowable difference between the current speed and
  the desired speed (HVE's *Max Speed Error*, which HVE kept on its Driver tab).
- **Max Throttle (0-1)** — maximum allowable throttle pedal position.
- **Max Brake Pedal** — maximum allowable brake pedal force.
- **Initial Throttle** — throttle pedal position at driver start time (0–1).
- **Throttle Correction Rate (%/100 per mph)** — amount of throttle
  correction per unit of speed error.
- **Throttle Correction Damping (%/100-s per mph)** — throttle correction
  damping, used to limit throttle activity.
- **Initial Brake** — brake pedal force at driver start time.
- **Brake Correction Rate (lb/mph)** — amount of brake pedal force correction
  per unit of speed error.
- **Brake Correction Damping (lb-s/mph)** — brake correction damping, used to
  limit braking activity.
- **Pedal Delay (s)** — HVE's *Delay To Switch Pedals*: the time the driver needs
  to move between the throttle and the brake pedal.

<!-- NAV -->

---

← Previous: [Driver Controls Path Follower](DriverControls7.md)  |  [Index](README.md)  |  Next: [Event Information Dialog Box](EventInfo.md) →

<!-- /NAV -->
