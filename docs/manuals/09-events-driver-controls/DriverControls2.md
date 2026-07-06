# Driver Controls Wheel Data

Applies constant wheel forces and steer angles.

The Wheel Data page is available for reconstruction models. This page allows the user to enter the following information.

## Pre-Impact

**Total Lock-up (%/100)**
The entered value is multiplied by the average tire-ground friction coefficient to determine the total vehicle deceleration between the user-entered Begin Braking and Impact positions. This value is relevant only if the user has supplied a Begin Braking position for the current vehicle.

## Post-Impact

**Rot/Lat Skidding**
This check box may be used by reconstruction models to trigger special calculations for vehicles that spin (rotate/laterally skid) between separation and rest.

For each axle (Axle 1, Axle 2 and Axle 3, as applicable to the current vehicle), the following post-impact values are entered:

**Right Lock-up (%/100)**
The wheel lock-up is multiplied by the available friction force to determine the average longitudinal force at the right wheel. The entered value should not account for lateral skidding; the program's tire model will determine the tire slip angle and account for the force associated with lateral skidding.

**Steer (deg)**
The entered value is used to determine the steer angle at the right wheel. This angle is assumed to remain constant, and applies only during the post-impact phase.

**Left Lock-up (%/100)**
The wheel lock-up is multiplied by the available friction force to determine the average longitudinal force at the left wheel. The entered value should not account for lateral skidding; the program's tire model will determine the tire slip angle and account for the force associated with lateral skidding.

**Steer (deg)**
The entered value is used to determine the steer angle at the left wheel. This angle is assumed to remain constant, and applies only during the post-impact phase.

All values are entered with a slider or by typing directly into the associated edit field.

---
*Source topic: DriverControls2.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Path Follower Method](DriverControls1.md)  |  [Index](README.md)  |  Next: [Driver Controls Brake](DriverControls3.md) →

<!-- /NAV -->
