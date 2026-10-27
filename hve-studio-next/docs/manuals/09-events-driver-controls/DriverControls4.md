# Driver Controls Throttle

Applies longitudinal tire forces that attempt to accelerate the vehicle.

The **Throttle** tab of the [Driver Controls](DriverControls.md) dialog
(**Event › Driver Controls...**). For a SINGLETRACK event the tab is not shown:
the motorcycle model has no engine or drivetrain.

## Input Method

Selects the type of throttle table:

A vehicle added to a SIMON, EDVDS or EDVSM event, however it is added (Event
Information, Quick Case, the vehicle library or Case Intake), or an event switched
to one of them, starts with **At Driver** for both throttle and brake until its
tables are edited; the other methods have no pedal path and start with **% of Friction**.

- **At Driver** — HVE's *Wide-open Throttle*: throttle position from
  0 (closed) to 1 (wide open) versus time. The drivetrain model converts it to
  engine torque through the engine torque curve, and thus to tractive force at
  each drive wheel. This option engages the vehicle's engine and drivetrain
  data (and, in SIMON, engine braking and traction control).
- **% of Friction** — HVE's *Available Friction*: the fraction (0 to 1) of the
  available tire friction used to accelerate the vehicle. The engine torque
  curve is not consulted.

## Data Grid

*Time (s) → Throttle* (0 = closed, 1 = full open). When an imported case carries
HVE's per-wheel % of friction table it is shown above, with a note that it
overrides the single-value table. See
[Driver Controls](DriverControls.md#editing-a-table) for editing tables.

## Use Clutch / Torque Converter

When checked, the drivetrain model includes the clutch (manual transmission) or
torque converter (automatic transmission) when computing the drive torque. It is
enabled only under **Pedal**; under % of Friction it reaches no engine. With it
off the engine is locked to the wheels, so a vehicle starting from rest reads its
torque at idle and can barely pull away.

!!! warning "Not in HVE Studio"
    - The **Tractive Effort** table. An HVE case that uses one is imported with
      a note in Event Information that this part of its driver controls could
      not be represented.
    - HVE's **Copy Cell** and **Copy Row** buttons.

## For a SINGLETRACK event (nonlinear dynamics model)

With the event's **Dynamics model** set to **Nonlinear** the tab shows only the
table: there is no engine or drivetrain in that model, so there is no **Input
Method** and no **Use Clutch / Torque Converter**. Each value is a fraction of
the rear tire's grip at that instant -- its peak friction at its load and speed,
times the surface's Friction Multiplier, at its effective radius -- so 0 is
closed and 1 asks for all the grip the rear tire has. Whether the wheel then
spins is the tire's business. A per-wheel table's rear wheel drives the rear
tire. A case that states **At Driver** has its table read the same way, and the
run says so. Leaving the table as a new event has it (one point at 0) states no
throttle: a cruise torque then holds the start speed, as the Whipple model's
constant speed does, and the run says so.

<!-- NAV -->

---

← Previous: [Driver Controls Brake](DriverControls3.md)  |  [Index](README.md)  |  Next: [Driver Controls Gear](DriverControls5.md) →

<!-- /NAV -->
