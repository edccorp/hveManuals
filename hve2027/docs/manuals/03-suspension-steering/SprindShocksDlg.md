# Springs and Shocks Dialog

HVE edits a wheel's springs and shock absorbers in a separate Springs and Shocks dialog opened from the Suspension Data dialog. HVE 2027 has no separate dialog: the same parameters are rows of the **Suspension Data** dialog (**Vehicle › Suspension Data...** in the Vehicle Editor), one column per axle, under **Spring & Damper** and **Solid Axle**. See [Suspension Data Dialog](SuspDlg.md). Values are per axle and are shown in the units set in Preferences.

## Springs

**Spring Rate** (HVE: Wheel Rate)
Spring rate (force per unit of wheel travel) at the selected wheel due to the spring.

**Aux Roll Stiffness** (HVE: Aux. Roll Stiffness)
Roll stiffness (torque per unit of sprung mass roll) added by the addition of an anti-sway bar.

**Roll Ctr Below CG** (HVE: Roll Center Height)
Vertical distance from the sprung mass CG down (+) to the suspension roll center. Applies to solid axles. A value of 0 lets HVE 2027 estimate it, and the run says so.

**Lat. Spring Space** (HVE: Lateral Spring Spacing)
Lateral distance between the left and right suspension springs of a solid axle; together with the ride rate it determines the axle's roll stiffness. A value of 0 lets HVE 2027 estimate it from the track width.

## Shock Absorbers

**Damp Rate** (HVE: Damping at Wheel)
Velocity-dependent suspension force due to shock absorbers.

**Coulomb Friction**
Friction force required to initiate suspension travel.

**Friction Null Band**
Minimum suspension velocity required for full coulomb friction force.

!!! warning "Not in HVE 2027"
    - A separate Springs and Shocks dialog per wheel; the values are per axle.
    - HVE disables Roll Center Height and Lateral Spring Spacing for an independent suspension. HVE 2027 leaves them editable.

<!-- NAV -->

---

← Previous: [Spindle Axis Dialog](SpndleAxisDlg.md)  |  [Index](README.md)  |  Next: [Steering System Dialog](SteerSysDlg.md) →

<!-- /NAV -->
