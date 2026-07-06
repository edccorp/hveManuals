# Collision Pulse Options Dialog Box

The user may need to select a portion of the total pulse for use in a simulation. For example, an entire left turn may last 3 seconds, while the resulting collision with an oncoming vehicle lasts perhaps only 125 milliseconds. Thus, the user would like to extract that portion of the total pulse during which the collision occurs. This task can be performed using the Pulse Options dialog (title: *Collision Pulse Options: [vehicle name]*). The Pulse Options dialog is also used for assigning the impulse center for a 3-D impulse when the Force/Moment pulse type is used.

## Threshold Accel

Minimum total acceleration required for a data point to be considered part of the collision pulse (applies only to acceleration pulses). Entered with a slider or edit field.

## Tstart (sec)

Starting time of the pulse. Entered with a slider or edit field.

## Impulse Center (in) - x

The X coordinate of the impulse center. Enabled only when the current pulse type is Force/Moment.

## Impulse Center - y

The Y coordinate of the impulse center. Enabled only when the current pulse type is Force/Moment.

## Impulse Center - z

The Z coordinate of the impulse center. Enabled only when the current pulse type is Force/Moment.

## OK / Cancel

OK validates and assigns the options; Cancel discards the changes. The options are reset to zero when **New** is pressed in the Collision Pulse dialog.

---
*Source topic: ColPulOptDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Collision Pulse In-Use Factors Dialog Box](ColPulFact.md)  |  [Index](README.md)  |  Next: [Collision Pulse](ColPulse.md) →

<!-- /NAV -->
