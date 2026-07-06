# Slip vs Roll-Off Dialog

The tire longitudinal and lateral slip vs roll-off data tables for the selected wheel position are displayed and edited using this dialog (title: *Roll-Off Data: &lt;Mfr&gt; &lt;Model&gt; &lt;Size&gt;*).

Roll-off data are stored as a table of up to 6 longitudinal slip values by up to 6 slip angle values; a longitudinal and a lateral roll-off factor are entered for each combination.

This dialog contains the following items:

## Slip vs Roll-Off Graph

A graph showing the relationship between slip and roll-off, drawn from the current table. The graph is redrawn when Apply is pressed.

## Longitudinal Slip

Longitudinal tire slip at which the lateral roll-off values were obtained. The drop-down list contains the longitudinal slip breakpoints in the table (up to 6).

## Slip Angle

Lateral tire slip (slip angle) at which the longitudinal roll-off values were obtained. The drop-down list contains the slip angle breakpoints in the table (up to 6).

## Longitudinal Roll-Off

Reduction in lateral tire force (relative to the tire axis system) at the specified longitudinal slip.

## Lateral Roll-Off

Reduction in longitudinal tire force (relative to the tire axis system) at the specified lateral slip (slip angle).

## Add...

Adds a new Longitudinal Slip or Slip Angle breakpoint to the roll-off table (limited to 6 of each). Roll-off values for the new entry are seeded from the neighboring table entries and may then be edited. (New since the original help.)

## Delete...

Removes the selected Longitudinal Slip or Slip Angle breakpoint (and its associated roll-off data) from the table. (New since the original help.)

## Edit...

Changes the numeric value of an existing Longitudinal Slip or Slip Angle breakpoint; the table is re-sorted afterwards. (New since the original help.)

## Print...

Prints the currently displayed graph.

## Apply

Redraws the graph with the new values.

## OK / Cancel

OK validates the entries against their allowed ranges and stores the roll-off table for the tire. Cancel discards all changes.

---
*Source topic: SlipVsRollOffDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Fy vs Inclination Angle Dialog](FyVsInclAngDlg.md)  |  [Index](README.md)  |  Next: [Tire Friction Data Dialog](TireFrictDataDlg.md) →

<!-- /NAV -->
