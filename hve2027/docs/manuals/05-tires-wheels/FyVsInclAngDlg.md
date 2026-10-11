# Fy vs Inclination Angle Dialog

Camber thrust data for one wheel position: the camber (inclination) stiffness,
stored at a set of test loads and road speeds.

!!! note "HVE 2027"
    This is the **Camber** tab of the **Tire Friction Data** window, opened in the
    Vehicle editor (F3) with **Vehicle › Tire Tables...**. **Axle** and **Side**
    at the top of the window choose the wheel (see the
    [Tire Friction Data](TireFrictDataDlg.md) page). Loads, speeds and the
    stiffness are shown in the units set in Tools › Preferences.

With no camber points, camber thrust is off for that wheel: the physics' camber
table defaults to zero.

## Point

The load/speed points of the camber table, listed as "Load … @ …". Select one to
edit its stiffness. **Delete** removes the selected point.

## Camber Stiffness

Slope of the F<sub>y</sub> vs Camber Angle curve at the origin, for the selected
point (entered per degree in US units).

## Load / Speed / Add

Enter the test **Load** and road **Speed** of a new point and press **Add**. The
point is inserted in load-then-speed order. A new point starts at a small
placeholder stiffness (500 N/rad, about 2 lb/deg); enter the real value.

## Seed from Tire Data scalar

**Seed This Wheel** / **Seed All Wheels** create three load rows, at one half,
one and one and a half times the vehicle's nominal wheel load, with the camber
stiffness derived from the wheel's cornering stiffness (about 9 percent of it,
the ratio found across EDC's reference vehicles). Disabled until the vehicle
has a mass.

!!! tip "New in HVE 2027"
    Seeding is not in HVE. There is no scalar camber stiffness to seed from, so
    the table is derived from the cornering stiffness.

## Fy vs Camber Angle plot

F<sub>y</sub> against camber angle from 0 to 10 degrees for the selected point,
drawn as you edit.

!!! warning "Not in HVE 2027"
    - The **data grid** of camber angle vs F<sub>y</sub> points for each
      load/speed is not available; each point carries its stiffness only.
    - **In-Use Factor**: the camber table has none in HVE 2027.
    - **Edit...** (changing an existing load or speed): delete the point and add
      it again.
    - **Print...**, **Apply** (the plot is live) and **OK / Cancel** (edits apply
      immediately; **Edit › Undo**, Ctrl+Z, takes one back).

<!-- NAV -->

---

← Previous: [Tires & Wheels](README.md)  |  [Index](README.md)  |  Next: [Slip vs Roll-Off Dialog](SlipVsRollOffDlg.md) →

<!-- /NAV -->
