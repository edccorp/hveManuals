# Fy vs Inclination Angle Dialog

Camber thrust data for one wheel position: the camber (inclination) stiffness,
stored at a set of test loads and road speeds.

!!! note "HVE 2027"
    This is the **Camber** tab of the **Load & Speed Tables** panel at the
    bottom of the **Tire Properties** window, opened in the Vehicle editor (F3)
    with **Vehicle › Tire Data (Detailed)...**, or by a wheel's **Camber Table**
    button in the grid's **Load & Speed Dependence** rows. The **Wheel:**
    buttons at the top of the panel choose the wheel (see the
    [Tire Friction Data](TireFrictDataDlg.md) page). Loads, speeds and the
    stiffness are shown in the units set in Tools › Preferences.

With no camber rows, camber thrust is off for that wheel: the physics' camber
table defaults to zero.

## Table

Each point of the camber table is a row with columns **#**, **Load**,
**Speed**, **Camber Stiffness** and **x** (delete). Every cell is editable;
after a **Load** or **Speed** is changed the table re-sorts by load, then
speed.

**Camber Stiffness** — Slope of the F<sub>y</sub> vs Camber Angle curve at the
origin, for that row (entered per degree in US units).

## Load / Speed / Add Row

Enter the test **Load** and road **Speed** of a new row under the table and
press **Add Row**. The row is inserted in load-then-speed order. A new row
starts at a small placeholder stiffness (500 N/rad, about 2 lb/deg); enter the
real value.

## Seed from Tire Data scalar

**Seed This Wheel** / **Seed All Wheels** create three load rows, at one half,
one and one and a half times the vehicle's nominal wheel load, with the camber
stiffness derived from the wheel's cornering stiffness (about 9 percent of it,
the ratio found across EDC's reference vehicles). Disabled until the vehicle
has a mass.

!!! tip "New in HVE 2027"
    Seeding is not in HVE. There is no scalar camber stiffness to seed from, so
    the table is derived from the cornering stiffness.

!!! warning "Not in HVE 2027"
    - The **data grid** of camber angle vs F<sub>y</sub> points for each
      load/speed is not available; each row carries its stiffness only.
    - **In-Use Factor**: the camber table has none in HVE 2027.
    - The **Fy vs Camber Angle** plot.
    - **Print...**, **Apply** and **OK / Cancel** (edits apply immediately;
      **Edit › Undo**, Ctrl+Z, takes one back).

<!-- NAV -->

---

← Previous: [Tires & Wheels](README.md)  |  [Index](README.md)  |  Next: [Slip vs Roll-Off Dialog](SlipVsRollOffDlg.md) →

<!-- /NAV -->
