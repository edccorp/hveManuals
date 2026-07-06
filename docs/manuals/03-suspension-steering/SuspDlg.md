# Suspension Data Dialog

The suspension parameters of the vehicle are displayed and edited using the Suspension Data dialog. The dialog title identifies the current vehicle, axle number and side (e.g., *Suspension Data: ... (Axle No. 1, Left Side)*).

This dialog contains the following items:

## Suspension Type

The HVE Vehicle Model includes the following suspension types:

- **Independent** — The right and left wheels move independently from each other.
- **Solid Axle** — The right and left wheels are rigidly connected.
- **Tandem 4 Spring** — A set of two solid axle suspensions sharing an articulated spring support, such that the force on the rear of the leading spring is transferred to the front of the trailing spring.
- **Tandem Walking** — A set of two solid axle suspensions connected by a rigid link.

The tandem types are offered in the list only where a tandem axle set is possible: on rear axles of vehicles with more than two axles, and on trailers or dollies with more than one axle. Otherwise the list contains only *Independent* and *Solid Axle*.

The selected type also controls which of the buttons below are available (see individual entries).

## Lateral Load Transfer Coef (%/100)

Slider/edit field for the fraction of the total sprung mass roll couple (lateral load transfer) reacted at the selected axle. Values at the individual axles are automatically balanced so that the distribution over all axles totals 1.0 (for example, changing the value at a rear axle adjusts the front axle share accordingly; on three-axle vehicles the remainder is split between the other axles). The controls are disabled if the vehicle has fewer than two axles, or if the vehicle has no driver location defined (except movable barriers).

*(This option was added since the original help topic was written.)*

## Inter-Tandem Load Transfer Coef (%/100)

If the selected suspension type is a tandem axle (either *4-Spring* or *Walking Beam*), the Inter-tandem Load Transfer parameter is enabled, allowing the user to enter a value for the inter-tandem load transfer for the selected axle set. For *Independent* and *Solid Axle* types this field is disabled.

## Mechanical Group

**Springs and Shocks...**
Displays the [Springs and Shocks Dialog Box](SprindShocksDlg.md).

**Inertia...** (Axle Inertia)
Displays the Inertia dialog box (solid axle weight and roll/yaw inertia). Enabled only when the suspension type is *not* Independent.

**Jounce/Rebound...**
Displays the [Jounce/Rebound Stops Dialog Box](JouAndRebDlg.md).

## Geometry Group

**Spindle Axis...**
Displays the [Spindle Axis Dialog Box](SpndleAxisDlg.md). Enabled only if the current axle is steerable (see the Steering System dialog).

**Camber...**
Displays the [Camber Dialog Box](CamberDlg.md). For *Independent* suspensions this opens the full Camber vs. Jounce/Rebound table/graph dialog; for solid and tandem axles it opens a small dialog containing a single constant *Camber (deg)* value.

**Anti-Pitch...**
Displays the [Anti-Pitch Dialog Box](AntiPitchDlg.md). Enabled only when the suspension type is *Independent*.

**Roll Steer...**
Displays the Roll Steer dialog. For *Independent* suspensions this is the [Roll Steer Dialog Box](RollSteerDlg.md) (constant/linear/quadratic/cubic coefficients vs. jounce/rebound); for solid and tandem axles it is the single-coefficient [Roll Steer Properties dialog](RollSteerNewDlg.md).

## Copy to Other Side

Check this box to copy all the suspension properties of this wheel to the wheel on the other side of the same axle when you click OK.

## Copy to Other Axle(s)

Check this box to copy the suspension properties of this axle to the vehicle's other axle(s) when you click OK.

*(This option was added since the original help topic was written.)*

---
*Source topic: SuspDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Steering System Dialog](SteerSysDlg.md)  |  [Index](README.md)  |  Next: [Wheel Location Dialog](WheelLocDlg.md) →

<!-- /NAV -->
