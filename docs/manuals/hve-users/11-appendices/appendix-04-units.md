# Appendix IV — Units

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Appendix IV, pages IV-1 through IV-14. Several obviously mis-copied descriptions in the original
Environment Units table have been corrected; corrections are noted.*

HVE allows the user to define the current system of units by selecting Units
from the Options menu (see Menu Reference). Every input and output variable
in HVE has a unit name. For example, `UtVehForce` is the unit name for force
applied to the vehicle and `UtHumForce` is the unit name for force applied
to humans. Inside HVE, the program units for force will always be lb.
However, if desired, they can be assigned different user units.

> **NOTE:** *Program Units* are the units stored and used inside HVE.
> Program units are always pounds, seconds and inches (and their
> derivatives). However, the user sees all input and output values in *User
> Units*. User units are completely programmable by the user.

In general, HVE allows the user to assign units to the following object
groups:

- **General** — General-purpose units
- **Brake System** — Units related to the brake system
- **Engine** — Units related to the engine
- **Environment** — Units related to the environment
- **Human** — Units related to humans
- **Steering System** — Units related to the steering system
- **Suspension** — Units related to the suspension
- **Tire** — Units related to the vehicle's tires
- **Vehicle** — Units related to vehicles

This appendix describes how to assign units to any parameter.

## Units Files

HVE has two units files, `units.us` and `units.si`. These files contain the
unit names (e.g., `UtHumDispAngle`) and current value (e.g., `deg`). A
file named `language.rsc` contains the associated program unit (e.g.,
`rad`) and conversion factor (e.g., 57.29577951).

To assign a unit to any parameter, perform the following steps:

1. Identify the unit name. The unit names are identified in the Human
   Model, Vehicle Model, Environment Model and Event Model sections of this
   manual.
2. Identify the Program Units for the selected parameter. The Program Units
   for each parameter group are listed in this appendix (see Tables IV-1
   through IV-11).
3. Modify the `units.us` or `units.si` file by editing the desired unit.
   For example, to change vehicle velocity from mph to ft/sec, edit
   `units.us`: find `UtVehVelLinear` and simply change the corresponding
   string from `mph` to `ft/sec`.
4. Confirm the conversion factor exists in the `language.rsc` file. In this
   case, the following lines may be found in the `language.rsc` file:

   ```
   Convert    in/sec    in/sec    1.0
   Convert    in/sec    ft/sec    0.083333333
   Convert    in/sec    mph       0.056818182
   Convert    in/sec    km/h      0.091440000
   Convert    in/sec    cm/sec    2.540000000
   Convert    in/sec    m/sec     0.025400000
   ```

> **NOTE:** If `ft/sec` were not already in the `language.rsc` file, it
> would need to be added before HVE could fulfill the user's request.

The remainder of this appendix lists the individual unit names and program
units for each group.

## General Purpose Units

**Table IV-1 — General-purpose Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtNone | N/A | Used for dimensionless parameters |
| UtTime | sec | Simulation time units (see also UtHumTime, UtVehTime, UtSteTime, UtEnvTime, UtBraTime, UtEngTime) |
| UtFrequency | sec⁻¹ | Inverse of the period of oscillation for harmonic motion |
| UtVelAngular | rad/sec | Angular velocity units (see also UtHumVelAngular, UtVehVelAngular, UtEnvVelAngular, UtEngSpeed, UtSusVelAngular, UtTirVelAngular) |
| UtVelLinear | in/sec | Linear velocity units (see also UtHumVelLinear, UtVehVelLinear, UtEnvVelLinear, UtSusVelLinear, UtTirVelLinear) |

## Brake System Units

**Table IV-2 — Brake System Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtBraForce | lb | Units of force used for brake system parameters |
| UtBraExpansionCoef | in/degF | Coefficient for increasing stroke in S-cam brake assemblies due to thermal expansion |
| UtBraPedalRatio | lb/in²-lb | Ratio of brake system pressure to brake pedal force |
| UtBraPercent | %/100 | Percent units used for brake system parameters |
| UtBraPress | lb/in² | Units of pressure |
| UtBraTime | sec | Brake system time |
| UtBraTorque | in-lb | Brake system torque |
| UtBraTorqueRatio | in-lb-in²/lb | Brake system torque ratio |
| UtBraPressRate | lb/in²-sec | Rate of change in wheel brake pressure |

## Engine Units

**Table IV-3 — Engine Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtEngForce | lb | Units of force used for engine parameters |
| UtEngPercent | %/100 | Percent units used for engine parameters |
| UtEngPower | in-lb/sec | Units of power (rate of work) for engine parameters |
| UtEngSpeed | rad/sec | Units of rotational velocity for engine parameters |
| UtEngTime | sec | Engine time |
| UtEngTorque | in-lb | Engine torque |

## Environment Units

**Table IV-4 — Environment Units** *(several descriptions in the original
table were mis-copied from the Engine table; they are corrected here)*

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtEnvTime | sec | Units of time used for environment parameters |
| UtEnvCameraFocalLength | in | Camera focal length units |
| UtEnvDensity | lb/in³ | Weight per unit volume |
| UtEnvDispLength | in | Linear displacement units for the environment |
| UtEnvDispAngle | rad | Angular displacement units for the environment |
| UtEnvEnergy | in-lb | Energy units for the environment |
| UtEnvForce | lb | Force units for the environment |
| UtEnvGravity | in/sec² | Gravitational acceleration units |
| UtEnvKc | lb/in^(N+2) | Cohesive soil constant for sinkage |
| UtEnvKphi | lb/in^(N+1) | Frictional soil constant for sinkage |
| UtEnvPercent | %/100 | Percent units for the environment |
| UtEnvPress | lb/in² | Units of pressure for the environment |
| UtEnvShear | lb/in² | Units of shear stress for the environment |
| UtEnvTemp | Fahrenheit | Units of temperature for the environment |
| UtEnvTorque | in-lb | Units of torque for the environment |
| UtEnvVelAngular | rad/sec | Units of angular velocity for objects in the environment |
| UtEnvVelLinear | in/sec | Units of linear velocity for objects in the environment |
| UtEnvVolume | in³ | Units of environment volume |

## Human Units

**Table IV-5 — Human Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtHumAccelAngular | rad/sec² | Angular acceleration for humans |
| UtHumAccelLinear | in/sec² | Linear acceleration for humans |
| UtHumChestSI | in/sec² | Chest Severity Index |
| UtHumDamp | in-lb-sec/rad | Damping for humans |
| UtHumDispAngle | rad | Angular displacements for humans |
| UtHumDispLength | in | Linear distances for humans |
| UtHumElastLinear | in-lb/rad | Linear elastic torque |
| UtHumElastQuad | in-lb/rad² | Second-order elastic torque |
| UtHumElastCubic | in-lb/rad³ | Third-order elastic torque |
| UtHumEnergy | in-lb | Energy units for humans |
| UtHumForce | lb | Force units for humans |
| UtHumInertia | lb-sec²-in | Rotational inertia units for humans |
| UtHumMass | lb-sec²/in | Mass units for humans |
| UtHumPercent | %/100 | Units of percentage for humans |
| UtHumTime | sec | Time units for humans |
| UtHumTorque | in-lb | Torque units for humans |
| UtHumVelAngular | rad/sec | Angular velocity units for humans |
| UtHumVelLinear | in/sec | Linear velocity units for humans |

## Steering System Units

**Table IV-6 — Steering System Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtSteDispAngle | rad | Steering system angular displacement units |
| UtSteTime | sec | Time units for steering |
| UtSteVel | rad/sec | Steer velocity units |
| UtSteVelRate | rad/in | Steer correction rate units |
| UtSteVelDamp | rad-sec/in | Steer correction damping units |
| UtSteTorque | in-lb | Steer torque units |
| UtSteTorqueRate | in-lb/in | Steer torque correction rate units |
| UtSteTorqueDamp | in-lb-sec/in | Steer torque correction damping units |

## Suspension System Units

**Table IV-7 — Suspension System Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtSusAccelAngular | rad/sec² | Angular acceleration units for suspension |
| UtSusAccelLinear | in/sec² | Linear acceleration units for suspension |
| UtSusAntiPitch | lb/in-lb | Anti-pitch units for suspension |
| UtSusDispAngle | rad | Angular displacement units for suspension |
| UtSusDispLength | in | Linear displacement units for suspension |
| UtSusRateLinear | lb/in | Units for suspension linear rate |
| UtSusRateQuadratic | lb/in² | Units for suspension second-order rate |
| UtSusRateCubic | lb/in³ | Units for suspension third-order rate |
| UtSusDamp | lb-sec/in | Suspension damping units |
| UtSusPercent | %/100 | Units of percentage for suspension |
| UtSusRollConst | rad | Roll constant units for suspension |
| UtSusRollLinear | rad/in | Linear roll rate units for suspension |
| UtSusRollQuad | rad/in² | Second-order roll rate units for suspension |
| UtSusRollCubic | rad/in³ | Third-order roll rate units for suspension |
| UtSusRollStiff | in-lb/rad | Roll stiffness units for suspension |
| UtSusVelAngular | rad/sec | Suspension angular velocity units |
| UtSusVelLinear | in/sec | Suspension linear velocity units |

## Tire Units

**Table IV-8 — Tire Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtTirAccelAngular | rad/sec² | Tire angular acceleration units |
| UtTirAccelLinear | in/sec² | Tire linear acceleration units |
| UtTirAlignTorque | in-lb/rad | Tire aligning torque units |
| UtTirCalfa | lb/rad | Tire cornering stiffness units |
| UtTirCgamma | lb/rad | Tire camber stiffness units |
| UtTirDispAngle | rad | Tire angular displacement units |
| UtTirDispLength | in | Tire linear distance units |
| UtTirForce | lb | Tire force units |
| UtTirInertia | lb-sec²-in | Tire rotational inertia units |
| UtTirLongSlip | %/100 | Tire longitudinal slip units |
| UtTirLongStiff | 1/lb | Tire longitudinal stiffness units |
| UtTirPercent | %/100 | Tire percentage units |
| UtTirRateLinear | lb/in | Tire linear rate units |
| UtTirRolloff | %/100 | Tire rolloff units |
| UtTirTorque | in-lb | Tire torque units |
| UtTirVelAngular | rad/sec | Tire angular velocity units |
| UtTirVelDependence | sec/in | Tire velocity dependence units for friction |
| UtTirVelLinear | in/sec | Tire linear velocity units |

## Vehicle Units

**Table IV-9 — Vehicle Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtVehAccelAngular | rad/sec² | Vehicle angular acceleration units |
| UtVehAccelLinear | in/sec² | Vehicle linear acceleration units |
| UtVehArea | in² | Vehicle area units |
| UtVehConduction | in-lb/in-sec-degF | Vehicle material conduction units |
| UtVehConvection | in-lb/in²-sec-degF | Vehicle static convection units |
| UtVehConvectionVel | in-lb-sec/in²-sec-degF-in | Vehicle velocity-dependent convection units |
| UtVehDensity | lb/in³ | Vehicle density units |
| UtVehDispAngle | rad | Vehicle angle units |
| UtVehDispLength | in | Vehicle length units |
| UtVehDragConst | lb | Vehicle drag constant units |
| UtVehDragLinear | 1/sec | Vehicle velocity-dependent drag units |
| UtVehDragQuad | in² | Vehicle second-order velocity-dependent drag units |
| UtVehEnergy | in-lb | Vehicle energy units |
| UtVehForce | lb | Vehicle force units |
| UtVehInertia | lb-sec²-in | Vehicle rotational inertia units |
| UtVehInvLength | 1/in | Vehicle inverse length units |
| UtVehInvLength2 | 1/in² | Vehicle inverse length-squared units |
| UtVehLightBright | cd | Vehicle light power units |
| UtVehMass | lb-sec²/in | Vehicle mass units |
| UtVehMassRate | lb/sec | Vehicle mass rate units |
| UtVehMatStiffLinear | lb/in | Vehicle material linear stiffness units |
| UtVehMatStiffQuad | lb/in² | Vehicle material second-order stiffness units |
| UtVehMatStiffCubic | lb/in³ | Vehicle material third-order stiffness units |
| UtVehMatDamp | lb-sec/in | Vehicle material damping units |
| UtVehPercent | %/100 | Vehicle percentage units |
| UtVehPress | lb/in² | Vehicle pressure units |
| UtVehRelativeVelLinear | in/sec | Vehicle relative velocity units |
| UtVehSpecHeat | in-lb/lbm-°R | Vehicle specific heat units |
| UtVehSteeringRatio | rad/rad | Vehicle steering ratio units |
| UtVehSteeringStiffness | in-lb/rad | Vehicle steering torsional stiffness units |
| UtVehStiffnessAstf | lb/in | Vehicle A stiffness units |
| UtVehStiffnessBstf | lb/in² | Vehicle B stiffness units |
| UtVehStiffnessKstf | lb/in² | Vehicle Kv stiffness units |
| UtVehTime | sec | Vehicle time units |
| UtVehTorque | in-lb | Vehicle torque units |
| UtVehVelAngular | rad/sec | Vehicle angular velocity units |
| UtVehVelLinear | in/sec | Vehicle linear velocity units |
| UtVehVolume | in³ | Vehicle volume units |

## Combined Material Units

**Table IV-10 — Combined Material Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtComForce | lb | Combined material force units |
| UtComMatLinear | lb/in | Combined material linear stiffness units |
| UtComMatQuad | lb/in² | Combined material second-order stiffness units |
| UtComMatCubic | lb/in³ | Combined material third-order stiffness units |
| UtComMatDamp | lb-sec/in | Combined material damping units |
| UtComDispLength | in | Combined material length units |

## Miscellaneous Units

**Table IV-11 — Miscellaneous Units**

| Unit Name | Program Units | Description |
| --- | --- | --- |
| UtHardwareLength | in | Length units for hardware (e.g., printer paper dimensions) |

<!-- NAV -->

---

← Previous: [Appendix III — Coordinate Systems](appendix-03-coordinate-systems.md)  |  [Index](README.md)  |  Next: [Appendix V — Collision Deformation Classification (CDC)](appendix-05-cdc.md) →

<!-- /NAV -->
