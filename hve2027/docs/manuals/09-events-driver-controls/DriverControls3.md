# Driver Controls Brake

Applies longitudinal tire forces that attempt to slow the vehicle.

The **Brake** tab of the [Driver Controls](DriverControls.md) dialog
(**Event › Driver Controls...**).

## Input Method

Selects the type of brake table (HVE's *Table* choice):

- **Pedal (AT_DRIVER)** — HVE's *Pedal Force*. The vehicle's brake system model
  converts the pedal input to brake torque, and thus longitudinal force, at
  each wheel. This is the only option that engages the vehicle's brake system
  (and Brake Designer) data. In SIMON it is also the only method under which
  the yaw stability control runs.
- **Wheel Force** — a table of brake force (attempted longitudinal force
  decelerating the vehicle) versus time at each wheel, one column per wheel
  (*A1-R*, *A1-L*, ...), in the units set in Preferences. Enter magnitudes. The
  force is applied as entered and does not scale with the wheel's load, so an
  unloaded inside wheel keeps its full force.
- **% of Friction** — HVE's *Available Friction*: the fraction (0 to 1) of the
  currently available tire friction force used for braking. The simulation
  multiplies the entered value by the current tire friction and vertical load.

A note beside the method says what the values mean.

## Data Grid

- Under **Pedal**, a case authored in HVE 2027 has a *Time (s) → Brake* table
  from 0 (released) to 1 (full apply), scaled to the vehicle's brake-pressure
  curve (its full-pedal force). A case imported from HVE carries HVE's real
  **pedal force** table, *Time (s) → Pedal force* in the units set in
  Preferences; it is used as entered and replaces the 0–1 table.
  **Discard pedal-force table** converts it back to a 0–1 table. A pedal-force
  table whose entries are all zero is labelled as a driver who never braked —
  it is real data and is sent to the engine.
- Under **Wheel Force**, the per-wheel force table, with **Add** and an **X**
  per row. With no rows entered, the run falls back to % of friction.
- Under **% of Friction**, a single *Time (s) → Brake* table (0–1) applied to
  every wheel, or — when the case carries one — HVE's per-wheel table, which
  overrides it.

See [Driver Controls](DriverControls.md#editing-a-table) for editing tables.

Anti-lock is set on the vehicle, per wheel in Brake Assembly and in the ABS /
Brake Design dialog (Vehicle menu); the **Brake** tab of **Event › Wheels...**
can force it on or off for one event.

!!! warning "Not in HVE 2027"
    HVE's **Copy Cell** and **Copy Row** buttons.

<!-- NAV -->

---

← Previous: [Driver Controls Wheel Data](DriverControls2.md)  |  [Index](README.md)  |  Next: [Driver Controls Throttle](DriverControls4.md) →

<!-- /NAV -->
