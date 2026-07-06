# Tire Friction Data Dialog

The tire frictional properties for the selected wheel position are displayed and edited using this dialog (title: *Friction Table: &lt;Mfr&gt; &lt;Model&gt; &lt;Size&gt;*).

Friction data are stored as a table of up to 3 test loads by up to 3 test speeds; the parameters below are entered for each load/speed combination. The physics models interpolate between table entries at run time.

This dialog contains the following items:

## Tire Friction Graph

A graph of *Friction vs. Slip* (friction, F<sub>x</sub>/F<sub>z</sub>, versus longitudinal slip) drawn from the current parameters, showing both the longitudinal and lateral curves. The graph is redrawn when Apply is pressed.

## Load

Vertical tire load at which the frictional values were obtained. The drop-down list contains the test loads in the friction table (up to 3); selecting a load displays the friction parameters for that load at the current speed.

## Speed

Road speed at which the frictional values were obtained. The drop-down list contains the test speeds in the friction table (up to 3); selecting a speed displays the friction parameters for the current load at that speed.

## Peak Longitudinal Friction

Maximum value of F<sub>x</sub>/F<sub>z</sub> achieved during the test at the given load and speed.

## Peak Lateral Friction

Maximum value of F<sub>y</sub>/F<sub>z</sub> achieved during the test at the given load and speed.

## Slide Friction

Value of F<sub>x</sub>/F<sub>z</sub> at 100 percent longitudinal slip achieved during the test at the given load and speed.

## Slip at Peak Long. Friction

Longitudinal slip at which the peak longitudinal friction was achieved at the given load and speed.

## Longitudinal Stiffness

Slope of the Friction vs. Slip curve at the graph's origin (lb/slip).

## In-Use Factor

Global multiplier for the dependent values (peak and slide friction, longitudinal stiffness). Applies to the entire friction table.

## Add...

Adds a new test Load or Speed value to the friction table. A prompt asks whether the new value is a Load or a Speed; the table is limited to 3 loads and 3 speeds. Data for the new entry are seeded from the neighboring table column/row and may then be edited. (New since the original help.)

## Delete...

Removes the selected test Load or Speed (and its associated friction data) from the table. (New since the original help.)

## Edit...

Changes the numeric value of an existing test Load or Speed; the table is re-sorted afterwards. (New since the original help.)

## Print...

Prints the currently displayed graph.

## Apply

Redraws the graph with the given data.

## OK / Cancel

OK validates the entries against their allowed ranges and stores the friction table for the tire. Cancel discards all changes.

---
*Source topic: TireFrictDataDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Slip vs Roll-Off Dialog](SlipVsRollOffDlg.md)  |  [Index](README.md)  |  Next: [Tire Information Dialog](TireInfoDlg.md) →

<!-- /NAV -->
