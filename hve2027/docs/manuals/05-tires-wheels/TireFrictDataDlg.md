# Tire Friction Data Dialog

The tire friction table for one wheel position: friction parameters stored at a
set of test loads and road speeds, interpolated by the physics at run time.

!!! note "HVE 2027"
    There is no separate window. The tables are the **Load & Speed Tables**
    panel at the bottom of the **Tire Properties** window, opened in the
    Vehicle editor (F3) with **Vehicle › Editors › Tires...** (see
    [Tire Information](TireInfoDlg.md)). The panel holds HVE's four tire-table
    dialogs as tabs: **Friction** (this page), **Cornering** (F<sub>y</sub> vs
    slip angle), **Camber** ([F<sub>y</sub> vs inclination
    angle](FyVsInclAngDlg.md)) and **Fy Roll-off** ([slip vs
    roll-off](SlipVsRollOffDlg.md)). Loads, speeds and stiffnesses are shown in
    the units set in Tools › Preferences; each column heading carries its unit.

![Tire Friction Data window](images/hvn-tire-tables.png)

*The screenshot shows the earlier separate window; the same tables are now
the panel under the Tire Properties grid.*

The buttons in the **Load & Speed Dependence** rows of the Tire Properties grid
(**Friction Table**, **Cornering Table**, **Camber Table**, **Fy Roll-off**)
select that wheel and that tab in the panel; the button for the table on
screen is highlighted. The bar between the grid and the panel drags to trade
height between them.

While a solved run is on screen the panel is read-only; reset the run to edit
it. Edits apply immediately; **Edit › Undo** (Ctrl+Z) takes one back.

## Wheel

The **Wheel:** row of buttons (**A1 Right**, **A1 Left**, **A2 Right**, ...)
chooses the wheel whose tables are shown, on every tab. The selected wheel's
button is highlighted.

**Copy to Axle** copies the selected wheel's four tables to the other wheel on
its axle. **Copy to All Wheels** copies them to every wheel of the vehicle.

!!! note "HVE 2027"
    **Right** is listed first because the calculation models number the right
    wheel (+y) first; it matches the column order of the Tire Properties grid.

## Friction table

Every point of the selected wheel's table is a row: a load and a speed with its
own set of friction parameters. The columns are **#**, **Load**, **Speed**,
**Peak Long.**, **Peak Lat.**, **Slide**, **Slip at Peak**, **Long. Stiffness**,
**In-Use** and an **x** button that deletes the row. Every cell is editable.
After a **Load** or **Speed** is changed the table re-sorts by load, then
speed. Clicking a row's number selects it for the plot below.

To add a point, enter its **Load** and **Speed** under the table and press
**Add Row**. The new row is seeded from the wheel's scalar friction values (the
Friction rows of the Tire Properties grid) and inserted in order. A table holds
at most 20 rows. With no rows at all the physics uses the scalar values.

!!! note "HVE 2027"
    HVE limits the table to 3 loads × 3 speeds and adds, deletes or edits a
    whole load or speed at a time. HVE 2027 keeps a list of individual
    load/speed points instead.

## Seed from Tire Data scalars

Builds a realistic table from the scalar values in one step. **Seed This
Wheel** replaces the selected wheel's table; **Seed All Wheels** does every
wheel of the vehicle. The table gets three load rows at one half, one and one
and a half times the vehicle's nominal wheel load (the rows are listed beside
the buttons); with the **with a speed axis (0 / 30 / 60 mph)** box checked it also
gets three speed columns. The buttons are disabled until the vehicle has a mass.

!!! tip "New in HVE 2027"
    HVE has no seeding. Every vehicle in EDC's reference cases carries three load
    rows, and a single point claims friction is independent of load and speed.
    SIMON interpolates both axes; EDSMAC and EDSMAC4 read the middle load row and
    reduce speed to a single slope, so for them a speed axis changes the answer
    and the load axis does not.

## Friction Values

The columns of each row:

**Peak Long.** — Maximum value of F<sub>x</sub>/F<sub>z</sub> at the
given load and speed.

**Peak Lat.** — Maximum value of F<sub>y</sub>/F<sub>z</sub> at the
given load and speed.

**Slide** — Value of F<sub>x</sub>/F<sub>z</sub> at 100 percent
longitudinal slip. It is held at or below Peak Long.

**Slip at Peak** — Longitudinal slip at which the peak longitudinal friction is
reached.

**Long. Stiffness** — Slope of the Friction vs. Slip curve at the origin, as a
force per unit slip.

**In-Use** — The In-Use Factor: multiplier for the dependent values (peak and slide
friction, longitudinal stiffness).

!!! note "HVE 2027"
    In HVE the In-Use Factor applies to the whole table. In HVE 2027 it is
    stored with each point.

## Friction vs. Longitudinal Slip

A preview of friction against longitudinal slip for the selected row, with the
In-Use Factor applied: a rise to the peak at the slip at peak, then a straight
fall to the slide value at full slip. It redraws as you edit; there is no Apply
button. It shows the longitudinal curve only.

!!! warning "Not in HVE 2027"
    **Print...** (use a screen capture), **Apply** (the preview is live) and
    **OK / Cancel** (edits apply immediately; **Edit › Undo**, Ctrl+Z, takes one
    back).

## Cornering tab

HVE's *F<sub>y</sub> vs Slip Angle* dialog. Cornering stiffness is stored per
load/speed point, in the same way as the friction table. Each point is a row
with columns **#**, **Load**, **Speed**, **Cornering Stiffness**, **In-Use** and
**x** (delete); every cell is editable and the table re-sorts by load, then
speed. Add rows with **Load**, **Speed** and **Add Row**; a new row starts at
the wheel's scalar Cornering Stiffness. **Seed This Wheel** / **Seed All
Wheels** create three load rows from the scalar. Clicking a row's number
selects it for the plot.

With no rows, most engines use the scalar Cornering Stiffness from Tire
Properties. EDVSM needs three load rows; it fits its stiffness-vs-load curve
over them and seeds them itself at run time if the case has fewer.

The plot shows F<sub>y</sub> against slip angle from 0 to 20 degrees: linear at
the stiffness, limited at Peak Lat. Friction times the selected row's load.

!!! warning "Not in HVE 2027"
    HVE's table of slip angle vs F<sub>y</sub> points for each load/speed is
    not available; each row carries its stiffness only.

<!-- NAV -->

---

← Previous: [Slip vs Roll-Off Dialog](SlipVsRollOffDlg.md)  |  [Index](README.md)  |  Next: [Tire Information Dialog](TireInfoDlg.md) →

<!-- /NAV -->
