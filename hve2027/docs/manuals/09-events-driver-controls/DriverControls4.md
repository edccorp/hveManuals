# Driver Controls Throttle

Applies longitudinal tire forces that attempt to accelerate the vehicle.

The **Throttle** tab of the [Driver Controls](DriverControls.md) dialog
(**Event › Driver Controls...**). For a SINGLETRACK event the tab is labelled
*(not read)*: the motorcycle model has no engine or drivetrain.

## Input Method

Selects the type of throttle table:

- **Pedal (AT_DRIVER)** — HVE's *Wide-open Throttle*: throttle position from
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

!!! warning "Not in HVE 2027"
    - The **Tractive Effort** table. An HVE case that uses one is imported with
      a note in Event Information that this part of its driver controls could
      not be represented.
    - HVE's **Copy Cell** and **Copy Row** buttons.

<!-- NAV -->

---

← Previous: [Driver Controls Brake](DriverControls3.md)  |  [Index](README.md)  |  Next: [Driver Controls Gear](DriverControls5.md) →

<!-- /NAV -->
