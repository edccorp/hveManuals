# SINGLETRACK Calculation Options

!!! tip "New in HVE Studio"
    SINGLETRACK is HVE Studio's motorcycle model (a single-track, Whipple-type
    machine with a rider); it is not one of HVE's programs and has no HVE
    report pages.

In Event Information, with a SINGLETRACK event active, press **Method
Options...** under Calculation Method. The **SINGLETRACK Options** window opens.
Everything in it is a machine property or an evidence input; there are no
solver tuning controls. Changes take effect immediately and are locked while the
event's results are on screen.

## Steer table

**Table means** — what the driver **Steer** table in
[Driver Controls](../09-events-driver-controls/DriverControls.md) contains:

- **Steer torque (N.m)** (default) — the torque the rider's arms apply at the
  bars. The machine finds its own lean, and with the balance rider it is brought
  back upright, so use this for a disturbance, not a corner.
- **Commanded lean (deg)** — the lean the machine reached; the rider
  countersteers to establish and hold it. Use this when the evidence is a lean
  angle rather than a bar force, which is usual.

A single-track vehicle cannot be driven by a prescribed steer angle (that would
over-constrain it and remove the countersteer), so that choice is not offered.

## Machine

- **Steering damper (N.m.s/rad)** — 0 = none fitted. Sport machines typically
  4–10.
- **Tire crown radius** — negative means derive it from the front tire's section
  width. The tread is a torus, so at lean the contact point moves inboard and the
  machine must lean several degrees further than the textbook angle.

## Braking

**Front brake fraction** — negative means the ideal split for this machine and
surface, which a skilled rider approximates; 0 is rear only; 1 is front only.
Pitch-over may limit braking before friction does, and the run says which.

## After a fall

**Machine drag factor** and **Rider drag factor** — if the machine goes down, it
and the rider slide to rest independently at these drag factors. Left at zero, no
slide is computed. Values commonly cited on asphalt: machine 0.40–0.60, rider
0.60–0.80.
