# Driver Controls Wheel Data

Applies constant wheel forces and steer angles.

The Wheel Data page is the only tab of the [Driver Controls](DriverControls.md)
dialog for an **EDCRASH** event (it is not shown for any other method). Open it
from **Event › Driver Controls...**. The values belong to the vehicle's slot in
the active event; if the vehicle is not in the event the page says so.

![Driver Controls, Wheel Data page (EDCRASH)](images/hvn-driver-controls-wheel-data.png)

EDCRASH solves each vehicle's separation velocity backwards from its spinout,
so the drag the wheels produced over that path is an input, not a result. All
values are typed or dragged; lock-ups are clamped to 0–1.

## Pre-Impact

**Total Lock-up (%/100)**
The entered value is multiplied by the average tire-ground friction coefficient
to determine the total vehicle deceleration between the user-entered Begin
Braking and Impact positions. It is relevant only if a **Begin Braking** scene
position is set for the vehicle (Event Information, *Scene positions*).

!!! note "HVE Studio"
    The note under the field says whether it is used: EDCRASH reads it only
    when the vehicle has a Begin Braking position in the scene-position list
    (Event Information, *Scene positions*). Without one it has no effect, as
    in HVE.

## Post-Impact

**Rot / Lat Skidding**
Selects how EDCRASH solves the post-impact path: off takes the rollout
solution, on takes the rotating/lateral-skidding (spinout) solution — a
different solver, not a refinement.

!!! note "HVE Studio"
    When **Auto-set Rot/Lat Skidding** is on in the
    [EDCRASH calculation options](../10-calculation-options/CalcOptEDCRASHDlg.md)
    (the default), EDCRASH sets this flag itself from the spinout path length
    and the value entered here is overridden. Turn that option off to use it.

For each axle (Axle 1, Axle 2 and Axle 3; axles the vehicle does not have are
grayed), the following post-impact values are entered:

**Axle n - Right Lock-up (%/100)**
The wheel lock-up is multiplied by the available friction force to determine
the average longitudinal force at the right wheel. The entered value should not
account for lateral skidding; the program's tire model determines the tire slip
angle and the force associated with lateral skidding. The lock-ups of the
wheels are averaged into the spinout drag.

**Steer (deg)**
The steer angle at the right wheel, assumed constant during the post-impact
phase.

**Left Lock-up (%/100)**
As for the right wheel, at the left wheel.

**Steer (deg)**
The steer angle at the left wheel, assumed constant during the post-impact
phase.

!!! note "HVE Studio"
    EDCRASH reads the per-wheel **steer** angles only on the **Trajectory
    Simulation** separation-velocity basis (Calculation Options); on the other
    bases they have no effect.

<!-- NAV -->

---

← Previous: [Driver Controls Path Follower Method](DriverControls1.md)  |  [Index](README.md)  |  Next: [Driver Controls Brake](DriverControls3.md) →

<!-- /NAV -->
