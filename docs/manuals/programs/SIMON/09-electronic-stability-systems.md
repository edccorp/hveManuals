# Electronic Stability Systems (TCS and YSC)

SIMON models two electronic stability systems as part of each vehicle's
drivetrain: **Traction Control (TCS)** and **Yaw Stability Control (YSC)**,
collectively referred to as the vehicle's **ESS (Electronic Stability
Systems)**. Each system is enabled individually per vehicle and configured with
its own activation thresholds and rates in the Vehicle Editor. The Anti-Lock
Brake System (ABS) is a separate model, described with the brake system; where
both are present, YSC acts on the brake pressures first and ABS then modulates
the result.

The ESS model is structured the way a production controller is: a **sensor
layer** synthesizes the signals an ECU would measure — a speedometer signal,
a yaw-rate signal, and per-wheel speed signals — and two **control laws** act on
the resulting errors. TCS intervenes by redistributing drive torque; YSC
intervenes by redistributing drive torque *and* modulating individual wheel
brake pressures.

The description below reflects the behavior of the current version of HVE.

## Sensor models

The sensor signals are recomputed on every pass through the wheel-torque
calculation:

- **Speedometer.** The vehicle speed signal $V$ is the average of the
  wheel-speed sensors on the **drive wheels** (spin velocity × tire static
  loaded radius).

- **Yaw-velocity error.** The expected yaw velocity follows from the driver's
  steering input and the vehicle geometry,

$$
\dot\psi_{expected} = \frac{V \tan\delta}{L}
$$

  where $\delta$ is the front-wheel steer angle (steering-wheel angle ÷ column
  ratio) and $L$ is the wheelbase computed from the axle positions (for a
  3-axle vehicle, the distance to the midpoint of the rear tandem). The yaw
  velocity error is the sensed yaw velocity minus this expectation:

$$
e_{\dot\psi} = \dot\psi_{sensor} - \dot\psi_{expected}
$$

  A positive error means the vehicle is rotating faster than the driver's
  steering asks for.

- **Per-wheel spin comparisons.** For each wheel, the expected spin velocity
  accounts for the wheel's lateral position $y$ during a turn:

$$
\omega_{expected} = \frac{V - \dot\psi\, y}{R_{SLR}}
$$

  where $R_{SLR}$ is the tire static loaded radius. From the wheel-speed
  sensors the model then forms, per wheel: the **spin-velocity error**
  ($\omega_{sensor} - \omega_{expected}$), the **difference from the other side**
  of the same axle, the difference from the axle average, the **difference
  between axle averages** (axle-to-axle), and the difference from the
  whole-vehicle average.

## Traction Control (TCS)

TCS runs during the drive-torque split calculation and is considered only when
the total drive torque (engine torque × transmission ratio × final drive
ratio) is at or above the **Minimum Drive Torque** threshold. Starting from an
even split among the drive axles, it makes two corrections:

1. **Axle-to-axle.** If the average wheel speed of a drive axle differs from
   another drive axle's average by at least the **Axle Difference** threshold,
   that axle's torque fraction is reduced in proportion to the difference:

$$
S_{axle} \mathrel{-}= R_{Tq}\,\Delta\omega_{axle}
$$

   where $R_{Tq}$ is the user-set **Drive Torque Rate**. The fraction is
   clamped between 0 and 1, so torque migrates away from a spinning axle
   toward the axle(s) with traction.

2. **Side-to-side.** If the left and right wheel speeds on a drive axle differ
   by at least the **Side Difference** threshold, the axle's torque is
   re-split between the sides. The right-side share is adjusted by
   $R_{Tq}\,S_{axle}\,\Delta\omega_{side}$ — proportional to both the axle's
   current torque fraction $S_{axle}$ and the right-minus-left wheel speed
   difference — and the left side receives the remainder, clamped so neither
   side goes below zero or above the axle's total. This mimics a brake- or
   clutch-based limited-slip intervention.

When either correction fires, the **TCS active** flag is set — the equivalent
of the TCS indicator lamp — and reported in the Variable Output.

## Yaw Stability Control (YSC)

YSC runs per wheel inside the brake-pressure calculation, after the pedal
force, proportioning, push-out and rise-time effects and **before ABS**. It is
gated twice:

- The vehicle speed must be at or above the **Minimum Velocity** threshold.
- Either the yaw-velocity error magnitude must reach the **Yaw Velocity
  Error** threshold, or the wheel's spin-velocity error magnitude must reach
  **twice** the **Spin Velocity Error** threshold.

Once active, YSC makes two interventions:

1. **Drive-torque side shift.** If drive torque is at or above the **Minimum
   Drive Torque** threshold and the axle's side-to-side wheel speed difference
   reaches the **Side Difference** threshold, the wheel's share of the axle
   torque is adjusted by $R_{Tq}\,S_{axle}\,\Delta\omega_{side}$ (proportional
   to the axle's torque fraction, as in TCS), clamped to the axle total. Note
   that the signed side difference of the **right-hand wheel** is used when
   adjusting either side of the axle, so the left- and right-side corrections
   are not exact mirror images of one another.

2. **Brake modulation.** If the driver's brake system pressure is at or above
   the **Minimum Brake Pressure** threshold and the wheel's spin-velocity
   error magnitude reaches the **Spin Velocity Error** threshold, the wheel's
   brake pressure is adjusted in proportion to the error:

$$
P \mathrel{+}= R_{P}\, e_{\omega}
$$

   where $R_P$ is the **Brake Pressure Rate**. A wheel spinning faster than
   expected receives more brake pressure; a wheel turning slower than expected
   (approaching lock) receives less. Pressure is floored at zero.

When either intervention fires, the **YSC active** flag is set — the YSC
indicator lamp — and reported in the Variable Output.

## User parameters

Both systems are configured in the Vehicle Editor's drivetrain ESS dialog.
The thresholds gate when the systems may act; the rates set how aggressively
they act per unit of error.

| Parameter | Used by | Meaning |
|-----------|---------|---------|
| Minimum Velocity | YSC | Vehicle speed below which YSC never intervenes |
| Yaw Velocity Error | YSC | Yaw-rate error that activates YSC |
| Spin Velocity Error | YSC | Wheel spin error for brake modulation (2× this value also activates YSC) |
| Side Difference | TCS, YSC | Left/right wheel-speed difference that triggers a side torque shift |
| Axle Difference | TCS | Axle-to-axle average speed difference that triggers an axle torque shift |
| Minimum Drive Torque | TCS, YSC | Drive torque below which no torque redistribution occurs |
| Minimum Brake Pressure | YSC | System brake pressure below which no brake modulation occurs |
| Drive Torque Rate | TCS, YSC | Change in torque split per unit wheel-speed error |
| Brake Pressure Rate | YSC | Change in brake pressure per unit wheel-speed error |

## Outputs

- The **Variable Output** drivetrain group includes the TCS and YSC active
  flags, so the timing of each intervention can be plotted against the vehicle
  response — the simulation equivalent of watching the dash lamps.
- The **Program Data** report lists the vehicle's ESS configuration: which
  systems are fitted, and the threshold and rate values in effect for the run.

## Notes and limitations

- The vehicle data structure also carries an **ESP** (Electronic Stability
  Program) flag, but no combined ESP control law is implemented in the current
  version of HVE — TCS and YSC are the two active systems. In particular there
  is no engine-torque cut and no yaw-moment-targeted braking of a specific
  corner based on the yaw error alone.
- TCS is purely wheel-speed based; the yaw-velocity error influences only
  YSC, and there only as an activation gate — the magnitude of every
  correction is driven by wheel-speed errors.
- The sensor models are idealized: the yaw-rate signal is the true simulated
  yaw velocity, with no noise, bias, or latency.
- The corrections are proportional with clamping. There is no integral or
  derivative action, and interventions persist only as long as the triggering
  error persists.

<!-- NAV -->

---

← Previous: [Chapter 8 — Index](08-index.md)  |  [Index](README.md)

<!-- /NAV -->
