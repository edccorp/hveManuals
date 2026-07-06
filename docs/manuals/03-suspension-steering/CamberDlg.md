# Camber vs Jounce/Rebound Dialog

The camber and half-track properties for the selected wheel location are displayed and edited using this dialog box. This dialog is used for **independent** suspensions; for solid and tandem axles the Camber button on the Suspension Data dialog opens a small dialog containing a single constant *Camber (deg)* value instead.

The dialog title identifies the current axle and side.

## Camber Graph

The upper graph, titled *Camber vs. Jounce/Rebound*, plots the wheel camber angle (deg) against suspension jounce/rebound deflection (in), using the values in the data grid.

## Half-Track Change Graph

The lower graph, titled *Half-track Change vs. Jounce/Rebound*, plots the half-track change (in) against suspension jounce/rebound deflection (in), using the values in the data grid.

## Data Grid

Table of camber data with three columns:

- **Jounce/Rebound (in)** — Suspension deflection (jounce negative, rebound positive).
- **Wheel Camber (deg)** — Camber angle at that deflection.
- **Half-track Change (in)** — Lateral movement of the wheel at that deflection.

Rows may be entered in any order; on Apply or OK the table is sorted by deflection and empty rows are removed. Each row must be complete (a row with missing entries produces an error), and duplicate deflection values are rejected.

## Apply

Validates the grid data and redraws both graphs with the given data.

## Print

Prints the displayed graphs.

---
*Source topic: CamberDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Anti-Pitch Dialog](AntiPitchDlg.md)  |  [Index](README.md)  |  Next: [Jounce and Rebound Stops Dialog](JouAndRebDlg.md) →

<!-- /NAV -->
