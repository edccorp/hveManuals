# Variable Output Report

The Variable Output table is a special output table of simulation results for an individual event, displayed as a function of time. The Variable Output table can show a tremendous amount of data and is scrollable both horizontally and vertically. The window is resizable.

## Select...

Pressing Select displays the Variable Selection dialog, used to choose the variables (per object and output group) displayed in the table.

## Graph...

The Graph button produces a graph of the first six selected variables in the Variable Output table (see the Variable Output Graph dialog).

## Edit...

Each HVE simulation event produces results calculated by the simulation model. Certain non-calculated results may also be assigned by the simulation model; these non-calculated results are editable by the user. Pressing Edit displays the Variable Output Edit dialog for those variables. If the model exposes no editable variables, an error message is displayed.

## Data Grid

Table of output values. The first column is Time (one row per output interval); each remaining column is one selected variable, with a multi-line column header showing the object name, the variable name and its units (tire variables include an additional axle/side line).

Selected cells may be copied to the clipboard by pressing **Ctrl+C**; the copied block is tab-separated and includes the column headers, ready for pasting into a spreadsheet.

---
*Source topic: VarOutRepDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Variable Output: Graph Dialog](VarOutGraphDlg.md)  |  [Index](README.md)  |  Next: [Selecting Variables](VarSelDlg.md) →

<!-- /NAV -->
