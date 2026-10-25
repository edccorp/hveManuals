# Transmission Data Dialog Box

The HVE vehicle transmission is modeled by a reverse gear, neutral and a number of forward gears. In HVE Studio the transmission is the **Transmission** section of the **Drivetrain** dialog (**Vehicle › Editors › Drivetrain...** in the Vehicle Editor); see [Drive Train Dialog Box](DriveTraDlg.md).

This section contains the following items:

## Automatic transmission
Check box selecting the transmission type: checked is **Automatic**, unchecked is **Standard** (manual). Checking it shows the shift-point fields below. With a manual transmission an orange note reminds that the gear comes from the driver's Gear table: with no gear entries the vehicle is in neutral, and with the pedal input method that means no drive torque however hard the throttle.

## Shift Points (automatic only)

### Shift RPM min, Shift RPM max
Low and high engine speeds bounding the shift schedule.

### Upshift lo/hi
Throttle positions, as a fraction of full throttle (0 to 1), at the low and high engine speeds above which an upshift occurs.

### Downshift lo/hi
Throttle positions, as a fraction of full throttle, at the low and high engine speeds below which a downshift occurs.

## Num Gears
The number of forward gears, 1 to 12 — HVE's own limit. (The engines are given at least two.) The driver's Gear table offers Neutral, Reverse and each of these gears, up to 12th.

## Gear table
A **Rev** row, then one row per forward gear: **Gear** (1, 2, ...) and **Ratio**.

**Rev** is the reverse ratio, entered **negative** as HVE stores it (every engine refuses a reverse that is not negative). A reverse of **0** means *unstated*: the engines are then given minus first gear, and a note under the table says so. SIMON uses the reverse ratio when the driver's Gear table selects Reverse (1), and when it starts an automatic vehicle that is rolling backwards. A vehicle read from an HVE vehicle or case carries HVE's own reverse ratio (before this was carried, every vehicle reversed on minus first gear; 201 of the 227 vehicles in the reference cases state a different one).

## Final Drive Ratio
The final drive (differential) ratio. HVE enters it in the Differential Data dialog.

## Efficiency
Shown grayed: there is no engine field it could be given to.

## Shift Time (s), Drive Type
Stored with the vehicle; no engine reads them. The drive axle(s) the engines use are set by **Drive Axle(s)** in the Vehicles panel's Configuration section.

!!! warning "Not in HVE Studio"
    - Upshift and downshift points entered in %WOT (HVE Studio uses fractions 0 to 1).
    - The **Shift Graph** and **Apply**.

<!-- NAV -->

---

← Previous: [Duplex Brake Dialog Box](DuplexBrkDlg.md)  |  [Index](README.md)

<!-- /NAV -->
