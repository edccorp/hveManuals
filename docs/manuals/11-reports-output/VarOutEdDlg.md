# Variable Output Edit Dialog

The developer of a human or vehicle simulation model may choose to make certain simulation results editable by the HVE user. For example, a 2-D simulation may allow the user to edit the sprung mass Z position and roll and pitch orientations. By editing these non-calculated fields, the user can create a 3-D sequence using a 2-D program.

This dialog is displayed by pressing **Edit...** in the Variable Output report window. If the current event's simulation model exposes no editable variables, an error message is displayed instead.

## Data Grid

Spreadsheet-style table of the editable variables:

- The first column, **Time**, is read-only; one row is created for each output time step of the simulation.
- Each remaining column is one editable variable (with its units), containing the current value at each time step. Type new values directly into the cells.

## OK / Cancel

OK validates the entries, stores the edited values back into the event's variable output data and refreshes the Variable Output table; Cancel discards the edits.

---
*Source topic: VarOutEdDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Trajectory Report](TrajRepDlg.md)  |  [Index](README.md)  |  Next: [Variable Output: Graph Dialog](VarOutGraphDlg.md) →

<!-- /NAV -->
