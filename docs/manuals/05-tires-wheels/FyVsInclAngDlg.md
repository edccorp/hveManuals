# Fy vs Inclination Angle Dialog

The tire F<sub>y</sub> vs inclination (camber) angle data for the selected wheel position are displayed and edited using this dialog (title: *Fy vs Inclination Angle: &lt;Mfr&gt; &lt;Model&gt; &lt;Size&gt;*).

Camber thrust data are stored as tables of up to 3 test loads by up to 3 test speeds; a separate camber angle vs lateral force table (up to 9 points) is maintained for each load/speed combination.

This dialog contains the following items:

## Fy vs Inclination Angle Graph

A graph of lateral force F<sub>y</sub> versus camber (inclination) angle, drawn from the current data table and camber stiffness. The graph is redrawn when Apply is pressed.

## Load

Vertical tire load at which the camber stiffness values were obtained. The drop-down list contains the test loads in the table (up to 3).

## Speed

Road speed at which the camber stiffness values were obtained. The drop-down list contains the test speeds in the table (up to 3).

## Data Grid

Editable table of *Camber Angle (deg)* vs *F<sub>y</sub> (lb)* points for the selected load and speed (up to 9 rows). Rows are automatically sorted; incomplete rows and duplicate camber angle entries are rejected when the dialog is accepted or applied.

## Camber Stiffness

Slope of the F<sub>y</sub> vs Camber Angle curve at the graph's origin.

## In-Use Factor

Global multiplier for the dependent values (F<sub>y</sub> and camber stiffness). Applies to the entire camber table.

## Add...

Adds a new test Load or Speed value to the table (limited to 3 loads and 3 speeds). Data for the new entry are seeded from the neighboring table entries and may then be edited. (New since the original help.)

## Delete...

Removes the selected test Load or Speed (and its associated data table) from the table. (New since the original help.)

## Edit...

Changes the numeric value of an existing test Load or Speed; the table is re-sorted afterwards. (New since the original help.)

## Print...

Prints the displayed graph.

## Apply

Redraws the graph using the given data.

## OK / Cancel

OK validates the grid and parameter entries against their allowed ranges and stores the camber data for the tire. Cancel discards all changes.

---
*Source topic: FyVsInclAngDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Tires & Wheels](README.md)  |  [Index](README.md)  |  Next: [Slip vs Roll-Off Dialog](SlipVsRollOffDlg.md) →

<!-- /NAV -->
