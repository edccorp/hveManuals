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

## Dynamics model

**Dynamics model** — which equations the method solves:

- **Whipple (linearized benchmark)** (default) — the published Whipple model,
  exact for small lean about upright straight running and validated against
  its benchmark. Braking is a deceleration limited by the friction available.
- **Nonlinear (four-body, slip tires)** — the same four bodies and parameters
  with nine rigid degrees of freedom and slip-based tires (TMeasy, with camber
  thrust inside the friction ellipse and the rounded tread's contact point).
  Lean is exact at any angle; braking, load transfer, wheel lift and flight are
  solved rather than imposed. The run reports the slip angles and slip ratios
  reached, the range of each wheel's load and the peak lateral acceleration.
  It has no hard-point ground contact yet, so a fall ends the run as the
  Whipple model's does; the drag-factor slide stays available.

The nonlinear model reads the tire data the Whipple model does not: the
cornering and camber stiffness tables (a stated camber curve is used point for
point), the lateral peak friction, the tire's spring rates, rolling resistance,
pneumatic trail and relaxation length, and the steering head's friction. Where
the tires state no camber table, a camber stiffness of 0.9 per radian of the
static load is assumed and disclosed. In a SIMON event a motorcycle still rides
the Whipple model whichever is selected, and the run says so.

It also reads more of the driver controls and the vehicle: the **Throttle** table
as a fraction of the rear tire's grip, the **Brake** tab's per-wheel **% of
Friction** and **Wheel Force** tables (each wheel against its own tire), the
steering stops (the Steering System's angles and stiffness, with no damping, as SIMON has them), and each
surface's **Friction Multiplier** under each tire. The Whipple model reads none of
these, and a run that states them says which it did not read. The nonlinear run's
output adds each wheel's drive and brake torque and the force each asks of the
tire (**Attempted Tractive Fx**, **Attempted Brake Fx**) beside the force the tire
gave (**Fx'**), and the **Friction Multiplier** under each tire.

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
