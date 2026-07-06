# Lining Friction Properties Dialog

Brake factor is heavily influenced by the friction coefficient between the lining material and the rotor or drum. Lining friction, in turn, is influenced by temperature and sliding velocity at the interface between the lining and rotor or drum. The HVE Brake Designer allows the user to directly study these influences by allowing the user and/or simulation model to determine the correct value of lining friction as a function of brake temperature and sliding velocity.

The dialog title includes the current brake design type (e.g., "Pad/Lining Friction Properties: Duo Servo Brake").

This dialog box displays the following items:

## Lining Friction Graph
A plot of pad/lining friction vs. temperature. One curve is drawn for each row of the sliding-speed table (legend "Sp -1", "Sp -2", ...); each curve is the lining temperature-friction table scaled by that speed's friction multiplier. The graph is redrawn when Apply is clicked.

## Friction vs. Temperature Table
A two-column data grid defining lining friction as a function of temperature:

- **Lining Temp** — brake lining temperature (degrees F; normal range -100 to 800).
- **Lining Friction** — friction coefficient at that temperature (dimensionless; normal range 0.2–0.6).

Up to 6 rows may be entered. Rows are sorted automatically, empty rows are stripped, and duplicate temperature entries are rejected. An empty row is allowed, but not an empty cell within a row.

## Friction Multiplier vs. Sliding Speed Table
A two-column data grid defining the velocity sensitivity of lining friction:

- **Sliding Speed** — sliding velocity at the lining/rotor (or drum) interface (in/sec; normal range 0–1,200).
- **Friction Multiplier** — multiplier applied to the temperature-based friction at that speed (dimensionless; normal range 0.50–2.0).

Up to 6 rows may be entered, with the same sorting, empty-cell and duplicate-row checks as the temperature table.

## Print
Prints the current graph.

## Apply
Validates the table entries, saves them and redraws the graph using the latest data.

## OK / Cancel
OK validates and accepts the tables; Cancel discards the changes.

---
*Source topic: LinFriPropDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Environment Information Dialog](EnvtInfoDlg.md)  |  [Index](README.md)  |  Next: [Material Properties Dialog](MatPropDlg.md) →

<!-- /NAV -->
