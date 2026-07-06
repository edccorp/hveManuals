# Anti-Pitch Dialog

The Anti-Pitch properties for the selected wheel location are displayed and edited using this dialog box. Anti-pitch data are entered as a table of anti-pitch coefficient vs. suspension deflection. This dialog is available only when the suspension type is **Independent** (the Anti-Pitch button on the Suspension Data dialog is disabled for solid and tandem axles).

The dialog title identifies the current axle and side.

## Anti-Pitch Graph

Graph titled *Anti-Pitch vs. Jounce/Rebound*, plotting the anti-pitch coefficient against suspension jounce/rebound deflection using the values in the data grid.

## Data Grid

Table of anti-pitch data with two columns:

- **Jounce/Rebound (in)** — Suspension deflection (jounce negative, rebound positive).
- **Anti-Pitch (lb/ft-lb)** — Anti-pitch coefficient at that deflection.

Rows may be entered in any order; on Apply or OK the table is sorted by deflection and empty rows are removed. Each row must be complete, and duplicate deflection values are rejected.

## Apply

Validates the grid data and redraws the graph with the supplied data.

## Print

Prints the displayed graph.

---
*Source topic: AntiPitchDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Suspension & Steering](README.md)  |  [Index](README.md)  |  Next: [Camber vs Jounce/Rebound Dialog](CamberDlg.md) →

<!-- /NAV -->
