# Wheels — Damage (Displacement) Page

The wheel Damage page (formerly *Displacement*) of the Event Wheels property sheet is used to dynamically vary wheel position and orientation during the simulation, and — for physics models that support wheel damage — to model wheel lock-up and DyMESH-based wheel damage forces.

The page contains the following items:

## Axle No

Axle index. Only the axles that exist on the current vehicle (1, 2 or 3) are listed.

## Side

Side index (Left or Right).

## Displacement (Change in Coordinates)

**x** — Vehicle-fixed wheel displacement distance in the X coordinate.

**y** — Vehicle-fixed wheel displacement distance in the Y coordinate.

**z** — Vehicle-fixed wheel displacement distance in the Z coordinate.

## Change in Camber

Vehicle-fixed wheel camber change angle (deg).

## Wheel is Damaged

Check box indicating that the wheel at the selected position is displaced/damaged during the event. The remaining fields on the page are enabled only when this box is checked. (The original help listed this as "Wheel is displayed", a typographical error.)

## Auto Start

Check box indicating that the start time is set automatically by the simulation (e.g. at impact). When checked, the Start Time field is disabled.

## Start Time

Simulation time at which the wheel displacement starts (sec). Disabled when Auto Start is checked.

## Duration

Duration over which the wheel displacement occurs (sec).

## Peak Lock-up Torque

Peak wheel lock-up torque applied to the damaged wheel, as a fraction (%/100). Enabled only when the active physics model supports the wheel damage option. (New since the original help.)

## Use DyMESH

Check box enabling DyMESH-computed wheel damage for this wheel. Available only when the event uses DyMESH. Checking it enables the wheel damage force/moment parameters below. (New since the original help.)

## Use Environment

Check box enabling wheel contact with the environment mesh when DyMESH wheel damage is in use. Available only when the DyMESH "Use Environment" option is active for the event. (New since the original help.)

## Max No-Damage Force

Maximum contact force (lb) the wheel can sustain without being displaced/damaged. (New since the original help.)

## Displacement Rate

Rate at which wheel displacement grows with contact force above the no-damage threshold (lb/in). (New since the original help.)

## Max Force

Maximum contact force (lb) used by the wheel damage model. (New since the original help.)

## Max No-Damage Moment

Maximum contact moment (in-lb) the wheel can sustain without angular displacement/damage. (New since the original help.)

## Moment Displacement Rate

Rate at which wheel angular displacement grows with contact moment above the no-damage threshold (in-lb/rad). (New since the original help.)

## Max Moment

Maximum contact moment (in-lb) used by the wheel damage model. (New since the original help.)

---
*Source topic: WheelsDlg1.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Wheels — Blow-out Page](WheelsDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Brake Page](WheelsDlg2.md) →

<!-- /NAV -->
