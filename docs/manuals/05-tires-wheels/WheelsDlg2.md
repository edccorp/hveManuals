# Wheels — Brake Page

The wheel Brake page of the Event Wheels property sheet allows the user to simulate the effects of brake adjustment on brake systems by specifying initial stroke (adjuster slack) and pad/lining and rotor/drum temperatures at each wheel, and — for physics models that support it — to simulate per-wheel brake failure during the event.

The page contains the following items:

## Axle No

Axle index. Only the axles that exist on the current vehicle (1, 2 or 3) are listed.

## Side

Side index (Left or Right).

## Brake Designer

**Initial Pad/Lining Temp** — Temperature of the brake pad/lining at the start of the simulation.

**Initial Rotor/Drum Temp** — Temperature of the brake rotor/drum at the start of the simulation.

**Initial Stroke (Adjuster Slack)** — Initial actuator stroke (in) at the start of the simulation, reflecting the state of brake adjustment.

These fields are enabled according to the brake temperature and brake adjustment options supported by the active physics model.

## Brake Failure

This group is new since the original help. It is enabled only when the active physics model supports the wheel brake failure option.

**Brake Is Failed** — Check box indicating that the brake at the selected wheel position fails during the event. The failure parameters below are enabled only when this box is checked.

**Auto Start** — Check box indicating that the failure start time is set automatically by the simulation. When checked, the Start Time field is disabled.

**Start Time** — Simulation time at which the brake failure starts (sec).

**Duration** — Duration over which the brake failure develops (sec).

**Amount of Failure (Failure Extent)** — Fraction of braking capacity lost at the wheel (%/100); 1.0 represents complete loss of braking at that wheel.

---
*Source topic: WheelsDlg2.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Wheels — Damage (Displacement) Page](WheelsDlg1.md)  |  [Index](README.md)  |  Next: [Wheel Properties Dialog](WheelsPropDlg.md) →

<!-- /NAV -->
