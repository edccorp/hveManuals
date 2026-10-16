# Slip vs Roll-Off Dialog

The roll-off table for one wheel position: how much the tire's lateral force is
reduced as longitudinal slip increases.

!!! note "HVE 2027"
    This is the **Fy Roll-off** tab of the **Load & Speed Tables** panel at the
    bottom of the **Tire Properties** window, opened in the Vehicle editor (F3)
    with **Vehicle › Tire Data (Detailed)...**, or by a wheel's **Fy Roll-off**
    button in the grid's **Load & Speed Dependence** rows. The **Wheel:**
    buttons at the top of the panel choose the wheel (see the
    [Tire Friction Data](TireFrictDataDlg.md) page).

The table is read by EDVTS and EDSVS. With no table the multiplier is 1.0 (no
roll-off).

## Table

Each row is one breakpoint:

**Long. Slip (0-1)** — Longitudinal slip, as a fraction (0 = free rolling,
1 = locked).

**Fy Multiplier** — Lateral force multiplier at that slip: the reduction in
lateral tire force (in the tire axis system) at the given longitudinal slip.
HVE's *Longitudinal Roll-Off*.

The **x** button at the end of a row deletes it. **Add Row** appends a row 0.1
slip beyond the last one, with the same multiplier, ready to edit. A table holds
at most 20 rows.

## Roll-off vs slip plot

The multiplier against longitudinal slip over the table's range, linearly
interpolated between rows. It is drawn once the table has two rows and redraws
as you edit.

!!! warning "Not in HVE 2027"
    HVE's table is two-dimensional — longitudinal slip × slip angle, with a
    **Longitudinal Roll-Off** and a **Lateral Roll-Off** for each combination.
    HVE 2027 stores a one-dimensional table of longitudinal roll-off against
    longitudinal slip, because that is all any engine reads (the engines take
    the first slip-angle column of HVE's table). The **Slip Angle** axis and the
    **Lateral Roll-Off** values have no consumer and are not kept. The table
    imported from an HVE vehicle is that first column.

    Also not available: **Print...**, **Apply** (the plot is live) and
    **OK / Cancel** (edits apply immediately; **Edit › Undo**, Ctrl+Z, takes one
    back). Rows are not sorted or checked for duplicate slip values; enter them
    in increasing slip.

<!-- NAV -->

---

← Previous: [Fy vs Inclination Angle Dialog](FyVsInclAngDlg.md)  |  [Index](README.md)  |  Next: [Tire Friction Data Dialog](TireFrictDataDlg.md) →

<!-- /NAV -->
