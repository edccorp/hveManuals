# EDSVS Calculation Options

EDSVS (Engineering Dynamics Corporation Single Vehicle Simulator) is a simulation analysis of the response of a motor vehicle (4-wheeled automobile, or truck having a tandem axle and dual tires) to driver inputs (accelerating, braking and steering). It is based on a program called TBST developed at the University of Michigan Transportation Research Institute. EDSVS determines how the vehicle responds to the inputs by generating the path, velocity, acceleration, tire force and other data as a function of time.

Accident investigators can use EDSVS to determine how a driver may have lost vehicular control. By repeated adjustments of the throttle, braking and steering input tables, the user will converge on those driver inputs which match accident site evidence. EDSVS can also be used to study the handling effects due to changes in vehicle weight distribution, wheelbase, track width, CG height, tire friction, cornering stiffness and other parameters.

An extremely useful feature of EDSVS is the ability to quickly and accurately review the results generated from different input scenarios. Termed *what if* analysis, changes can be made to an isolated variable or set of variables and the effects are displayed immediately. For example, the sensitivity of the trajectory to various front/rear tire combinations can be studied simply by changing the tire data; the sensitivity to CG location can be studied by moving its position. However, the major purpose of EDSVS can be realized by changing the driver input tables (throttle, braking and steering) until the resulting trajectory matches the actual trajectory produced by the vehicle during a particular maneuver. Thus, the user learns how a driver's inputs may have affected the outcome of an accident.

The EDSVS engine does not present or use a Calculation Options dialog. It sets `CalcMethodHeader.Options.CalcOptionsDlgIsUsed = FALSE` (`Svsinput.cpp`), so no calculation-options dialog is shown for EDSVS and the engine reads no `calcFloat`/`calcInt`/`calcOption` value. The one parameter historically exposed here — Roll Couple Distribution — is now taken from the vehicle's suspension data instead.

## Roll Couple Distribution

Roll Couple Distribution sets the fraction of the total lateral load transfer (roll couple) that is reacted by the front axle; the remainder is reacted by the rear axle. It is expressed as a fraction (units %/100) in the range 0.00 to 1.00. The default value is 0.55 (55 percent of the roll couple carried by the front axle).

For EDSVS this value is **not** entered through a Calculation Options dialog. It is set on the vehicle editor's suspension screen and read by the physics engine from the vehicle's suspension data, `Vehicle[0].Wheel[0][0].Suspension.RollCoupleDist` (`Svsinput.cpp`).

Within the physics model, this parameter corresponds to the FORTRAN-heritage lateral load transfer coefficients `gam1` (front axle) and `gam2 = 1 - gam1` (rear axle), which apportion the lateral weight shift used to compute the individual tire normal loads during cornering.

Note: An event still carries a legacy calculation-options field (`calcOptions.calcFloat[0]`, default 0.55), but the current EDSVS engine does not read it. Because `CalcOptionsDlgIsUsed = FALSE`, `gam1` is assigned only from `Suspension.RollCoupleDist`, so the roll couple distribution used by the simulation follows the vehicle editor's suspension setting.

## Removed Options

Earlier versions of this help topic listed the terrain surface-search choices **From First Polygon**, **From Previous Polygon** and **By Elevation** as EDSVS calculation options. These are no longer part of the EDSVS Calculation Options dialog. The surface-search method is now selected in the separate Get Surface Information Options dialog (Options menu), which offers From First Polygon, From Previous Polygon, From Previous Polygon (Sorted) and By Elevation.

---
*Source topic: CalcOptEDSVS.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [EDSMAC4 Calculation Options](CalcOptEDSMAC4.md)  |  [Index](README.md)  |  Next: [EDVDS Calculation Options](CalcOptEDVDS.md) →

<!-- /NAV -->
