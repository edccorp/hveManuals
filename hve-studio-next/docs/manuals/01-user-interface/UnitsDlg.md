# Units Dialog Box

HVE's Units dialog specifies the current system of units. HVE maintains two basic sets of units: program units and user units. Program units are always pounds, inches and seconds (and derivatives of these basic quantities); the user sees user units, converted with the proper conversion factors.

HVE Studio has no separate Units dialog. The system of units is chosen with **Units** in **Tools › Preferences...** (see [User Preferences Dialog Box](PrefDlg.md)):

## Metric (m, km/h, kg, N)
Sets SI (metric) units as the current system of units. HVE's **S.I**.

## Imperial (ft/in, mph, lb, lbf)
Sets US units as the current system of units. HVE's **U.S**.

The change takes effect at once in every dialog, panel, table and report that shows a converted value.

!!! note "HVE Studio"
    HVE Studio stores the case in SI units; the engines still work in HVE's program units (pounds, inches, seconds), and the conversion between the two is made when an event is run. As in HVE, the display unit of each quantity follows the quantity: for example lengths on a vehicle are shown in inches and distances in the scene in feet, brake torque in in-lb and engine torque in ft-lb in US units.

    A few fields are always shown in fixed units and say so in their labels (for example the airbag's **Bag Mass (kg)** and the brake material **Heat Capacity (J/kg·K)**).

!!! warning "Not in HVE Studio"
    **Custom** units (a user-defined mix of unit choices).

<!-- NAV -->

---

← Previous: [Text Editor Dialog Box](TextEdDlg.md)  |  [Index](README.md)

<!-- /NAV -->
