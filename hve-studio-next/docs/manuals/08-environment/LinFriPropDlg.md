# Lining Friction Properties Dialog

Brake factor is heavily influenced by the friction coefficient between the
lining material and the rotor or drum. Lining friction, in turn, is influenced
by temperature and by sliding velocity at the interface between the lining and
the rotor or drum. The HVE Brake Designer lets the user study these influences
by giving lining friction as a function of brake temperature and sliding
velocity.

!!! note "HVE Studio"
    In the Vehicle editor (F3) choose **Vehicle › Editors › Brakes › Brake Designer...** and expand
    the **Lining Friction Properties** section of the **Brake Designer**
    window. It edits the brake design of the wheel (the **Wheel:** button) and
    **Brake Design** type selected in that window, and appears only for a
    design type other than **Generic (torque ratio)**.

## Friction vs. Temperature (µ)

A table defining lining friction as a function of temperature:

- **Temp (°C)** — brake lining temperature.
- **Friction µ** — friction coefficient at that temperature.

The **x** at the end of a row deletes it (a table keeps at least one row).
**Add Row** appends a row 100 degrees above the last, with the same friction.

!!! note "HVE Studio"
    The temperature column is always in degrees Celsius; it does not follow the
    unit setting in Preferences.

## Friction Multiplier vs. Sliding Speed

A table defining the velocity sensitivity of lining friction:

- **Speed** — sliding velocity at the lining/rotor (or drum) interface, in the
  units set in Preferences.
- **Multiplier** — multiplier applied to the temperature-based friction at that
  speed.

**x** deletes a row; **Add Row** appends one above the last speed with the same
multiplier.

## Graph

A plot of lining friction against temperature over the table's range, scaled by
the multiplier at zero sliding speed, drawn as you edit; there is no Apply
button.

!!! note "HVE Studio"
    HVE draws one curve for each sliding-speed row; HVE Studio draws one.

The Brake Designer uses these tables when it computes the brake factor, and
through it the torque ratio the brake assembly carries to the physics.

!!! warning "Not in HVE Studio"
    - Automatic sorting and the duplicate-row and empty-cell checks: enter the
      rows in increasing temperature and speed.
    - **Print**, **Apply** and **OK / Cancel**: edits apply immediately.

!!! warning "Not in HVE Studio"
    HVE's separate **Brake Material Properties** library is not in HVE Studio:
    no physics program reads it (see
    [Brake Designer Material Properties](../04-brakes-powertrain/BrkMatPropDlg.md)).
    The lining friction a brake design uses is this section of the Brake
    Designer.

<!-- NAV -->

---

← Previous: [Environment Information Dialog](EnvtInfoDlg.md)  |  [Index](README.md)  |  Next: [Material Properties Dialog](MatPropDlg.md) →

<!-- /NAV -->
