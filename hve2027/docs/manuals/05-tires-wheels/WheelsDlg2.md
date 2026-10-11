# Wheels — Brake Page

The **Brake** tab of the event Wheels dialog sets the condition of each wheel's
brake at the start of the event — initial pad/lining and rotor/drum temperature
and initial stroke (adjuster slack) — and simulates per-wheel brake failure
during the event.

!!! note "HVE 2027"
    In the Event editor (F5) choose **Event › Wheels...** (Ctrl+W) and the
    **Brake** tab. Each wheel is a column (**A1-R**, **A1-L**, …) instead of
    HVE's Axle No / Side selectors; see [Wheels — Blow-out Page](WheelsDlg.md)
    for the layout and the link groups. Temperatures and the stroke follow the
    units set in Tools › Preferences. Only SIMON reads the brake-failure rows.

## Antilock brakes

!!! tip "New in HVE 2027"
    A list above the table overrides the vehicle's own antilock setting for this
    event only: **Use the vehicle's setting**, **Force OFF for this event** or
    **Force ON for this event**. The vehicle's own setting is made in
    **Vehicle › ABS / Brake Design...**. When a case imported from HVE recovered
    ABS from HVE's saved run, or the vehicle's own ABS flag is off while this
    event forces it on, a note says so.

## Initial pad/lining temp

Temperature of the brake pad or lining at the start of the simulation.

## Initial rotor/drum temp

Temperature of the brake rotor or drum at the start of the simulation.

!!! warning "Not in HVE 2027"
    The brake temperature model also needs the rotor/drum thickness, density
    and specific heat, which HVE 2027 does not pass to the engine. The two
    temperatures are stored and passed on, but the brake temperature output
    channels have no data: treat these values as stored data rather than a
    working thermal model.

## Initial stroke

Initial actuator stroke at the start of the simulation, reflecting the state of
brake adjustment (adjuster slack). Enabled only for a wheel whose brake
assembly is an S-cam, dual-wedge or single-wedge brake.

## Brake is failed

Check box indicating that the brake at this wheel fails during the event. The
failure rows below are enabled only when it is checked.

## Start at first contact

The failure starts automatically at the vehicle's first contact. When checked,
Failure start is disabled. HVE's *Auto Start*.

## Failure start (s)

Simulation time at which the brake failure starts. HVE's *Start Time*.

## Failure duration (s)

Duration over which the brake failure develops. HVE's *Duration*.

## Failure extent (fraction)

Fraction of the wheel's line pressure lost: the pressure is bled away over the
failure duration, ending at (1 − extent) of the pressure the driver asks for.
1.0 is a wheel with no brake left. HVE's *Amount of Failure*.

!!! note "HVE 2027"
    Checking **Brake is failed** alone does nothing while the extent is 0 — the
    pressure is reduced by the extent, not by the check box. Enter an extent.

<!-- NAV -->

---

← Previous: [Wheels — Damage (Displacement) Page](WheelsDlg1.md)  |  [Index](README.md)  |  Next: [Wheel Properties Dialog](WheelsPropDlg.md) →

<!-- /NAV -->
