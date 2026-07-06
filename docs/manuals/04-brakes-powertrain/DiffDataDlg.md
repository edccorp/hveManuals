# Differential Data Dialog Box

The HVE vehicle differential is modeled by up to 3 ratios. The differential is edited using the Differential Data dialog, opened from the Drivetrain dialog.

This dialog box contains the following items:

## Gears
Drop-down list selecting the number of differential (final drive) ratios: 1, 2 or 3 speeds.

## Gear Data Grid
This data grid contains one row per differential speed and the following columns:

- **Gear** — Name of each differential speed (High, and depending on the number of gears, Med and Low). This column is read-only.
- **Ratio** — Final drive ratio for each speed.

## Type
Radio buttons for the differential type: **Standard** (open), **Limited Slip** and **Locked**. These options are currently disabled: the HVE drivetrain model assumes an open (standard) differential, and Limited Slip and Locked are not yet implemented, so Standard is always selected. *(New group; not documented in the previous manual.)*

---
*Source topic: DiffDataDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Brake System Pressure vs Pedal Force Dialog Box](BrkSysVsPedFrcDlg.md)  |  [Index](README.md)  |  Next: [Disk Brake Dialog Box](DiskBreakDlg.md) →

<!-- /NAV -->
