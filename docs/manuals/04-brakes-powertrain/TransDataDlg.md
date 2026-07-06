# Transmission Data Dialog Box

The HVE vehicle transmission is modeled by a reverse gear, neutral and up to 12 forward gears. The transmission is edited using the Transmission Data dialog, opened from the Drivetrain dialog.

This dialog box contains the following items:

## Gears
Drop-down list specifying the number of forward gears (2 through 12 speeds).

## Data Grid
A grid containing one row for Reverse plus one row for each forward gear, with the following columns:

- **Gear** — Name of each gear (Rev, 1, 2, ... up to 12). This column is read-only.
- **Ratio** — Gear ratio for each gear.

## Type
Radio buttons selecting the transmission type: **Standard** (manual) or **Automatic**. Selecting Automatic enables the Shift Points group below. *(New option; not documented in the previous manual.)*

## Shift Points
Parameters defining the automatic transmission shift schedule. These controls are enabled only when the transmission type is Automatic. *(New group; not documented in the previous manual.)*

**Engine Speed (RPM)**
Low and high engine speeds bounding the shift schedule.

**Upshift Point (%WOT)**
Throttle positions (percent of wide open throttle) at the low and high engine speeds above which an upshift occurs.

**Downshift Point (%WOT)**
Throttle positions (percent of wide open throttle) at the low and high engine speeds below which a downshift occurs.

## Shift Graph
Graphical display of the shift schedule: throttle position vs engine speed, showing the upshift and downshift lines between the low- and high-speed shift points. The graph is redrawn after pressing Apply. *(New item; not documented in the previous manual.)*

## Apply
Validates the entered values and redraws the shift graph.

---
*Source topic: TransDataDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Duplex Brake Dialog Box](DuplexBrkDlg.md)  |  [Index](README.md)

<!-- /NAV -->
