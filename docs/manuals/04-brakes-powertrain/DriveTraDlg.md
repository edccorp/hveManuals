# Drive Train Dialog Box

The Drivetrain parameters for the current vehicle are displayed and edited using the Drivetrain dialog box. The drivetrain is composed of three components that are edited individually:

- Engine
- Transmission
- Differential

This dialog box contains the following items:

## Chart
Graphical display of the current engine table (engine output vs engine speed). The chart is redrawn to reflect edits made in the data grid after pressing Apply.

## Engine Name
User-editable description of the engine (drivetrain) for the current vehicle.

## Throttle Position
Radio buttons selecting which engine table is displayed and edited in the data grid:

**Wide Open Throttle**
Engine output table at full (wide open) throttle.

**Closed Throttle**
Engine output table at closed throttle (engine braking).

## Data Grid
A grid containing the engine table for the selected throttle position. Each row contains an Engine Speed (RPM) and the corresponding engine Power; the Torque column is calculated automatically from the speed and power entries. Rows are sorted by engine speed, and duplicate or incomplete rows are flagged when the data are applied.

## Engine Idle Speed (RPM)
Idle speed of the engine. *(New option; not documented in the previous manual.)*

## Apply
Validates the data grid entries and redraws the chart using the current table.

## Print...
Prints the engine chart.

## Transmission...
Displays the [Transmission Data Dialog Box](TransDataDlg.md).

## Differential...
Displays the [Differential Data Dialog Box](DiffDataDlg.md).

## TCS/YSC...
Displays the Electronic Stability System dialog, used to indicate whether Traction Control (TCS) and/or Yaw Stability Control (YSC) are installed, and to edit their activation thresholds (velocity, yaw velocity error, wheel spin velocity error, wheel side-to-side difference, axle-to-axle difference, drive torque and brake pressure) and activation rates (drive torque change and brake pressure change). *(New option; not documented in the previous manual.)*

## Drivetrain Inertia (lb-sec^2-in)
Rotational inertia of drivetrain components.

---
*Source topic: DriveTraDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Disk Brake Dialog Box](DiskBreakDlg.md)  |  [Index](README.md)  |  Next: [Dual Piston Brake Dialog Box](DualPistBrkDlg.md) →

<!-- /NAV -->
