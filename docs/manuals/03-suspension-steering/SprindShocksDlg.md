# Springs and Shocks Dialog

The Springs and Shocks properties for the selected wheel location are displayed and edited using this dialog box. The dialog title identifies the current axle and side.

This dialog box contains the following parameters:

## Springs

**Wheel Rate (lb/in)**
Spring rate (force per unit of wheel travel) at the selected wheel due to the spring.

**Aux. Roll Stiffness (in-lb/deg)**
Roll stiffness (torque per unit of sprung mass roll) added by the addition of an anti-sway bar.

**Roll Center Height (in)**
Vertical distance from the sprung mass CG down (+) to the suspension roll center. Applies to solid axles only; the field is disabled when the suspension type is *Independent*.

**Lateral Spring Spacing (in)**
Lateral distance between the left and right suspension springs of a solid axle; together with the ride rate it determines the axle's roll stiffness. Applies to solid axles only; the field is disabled when the suspension type is *Independent*.

*(The original help mislabeled this field "Lateral Space Spring" and described it incorrectly; the label and description above match the current code.)*

## Shock Absorbers

**Damping at Wheel (lb-sec/in)**
Velocity-dependent suspension force due to shock absorbers.

**Coulomb Friction (lb)**
Friction force required to initiate suspension travel.

**Friction Null Band (in/sec)**
Minimum suspension velocity required for full coulomb friction force.

---
*Source topic: SprindShocksDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Spindle Axis Dialog](SpndleAxisDlg.md)  |  [Index](README.md)  |  Next: [Steering System Dialog](SteerSysDlg.md) →

<!-- /NAV -->
