# Wheels — Blow-out Page

The Event Wheels option displays a tabbed property sheet. The tabs shown depend on the options supported by the active physics (calculation) model:

- **Blow-out** — the tire blow-out model (this topic)
- **Damage** — wheel displacement/damage (see [Wheels — Damage Page](WheelsDlg1.md))
- **Brake** — per-wheel brake adjustment and failure (see [Wheels — Brake Page](WheelsDlg2.md))
- **Tire-Terrain** — per-wheel tire-terrain friction options (new since the original help)

## Blow-out

The HVE Tire Blow-out Model is set up using the Blow-out page. The tire blow-out model allows the user to vary tire performance parameters (cornering, camber and radial stiffness and rolling resistance) while the simulation is running.

The page contains the following items:

## Axle No

Axle index. Only the axles that exist on the current vehicle (1, 2 or 3) are listed.

## Side

Side index (Left or Right).

## Location

Tire location index (Inner or Outer). Enabled only when the selected wheel position uses dual tires.

## Tire is Blown

Check box indicating whether the tire at the selected position blows out during the event. The remaining blow-out parameters are enabled only when this box is checked.

## Auto Start

Check box indicating that the blow-out start time is set automatically by the simulation. When checked, the Start Time field is disabled.

## Start Time

Simulation time at which the blow-out starts (sec). Disabled when Auto Start is checked.

## Duration

Duration over which the air loss occurs (sec).

## Stiffness Factor

Multiplier applied to the tire stiffness parameters (cornering, camber and radial stiffness) of the blown tire.

## Rolling Resistance Factor

Multiplier for the tire rolling resistance of the blown tire. This field is enabled only when the event's driver controls use pedal-force braking (the rolling resistance effect requires that brake option).

---
*Source topic: WheelsDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Tire Save As Dialog](TireSaveAsDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Damage (Displacement) Page](WheelsDlg1.md) →

<!-- /NAV -->
