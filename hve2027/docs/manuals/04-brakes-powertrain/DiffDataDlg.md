# Differential Data Dialog Box

In HVE 2027 the differential is the **Differential** section of the **Drivetrain** dialog (**Vehicle › Editors › Drivetrain...** in the Vehicle Editor); see [Drive Train Dialog Box](DriveTraDlg.md). The final drive ratio is entered in the Transmission section as **Final Drive Ratio**.

This section contains the following items:

## Diff Type
**Open**, **Limited Slip** or **Locked**.

## Locking Coeff
For **Limited Slip** only (greyed otherwise): the fraction (0 to 1) of the axle's own torque the clutch pack can transfer to the slower wheel. Locked uses 1.0.

## Preload Torque
For **Limited Slip** and **Locked** (greyed for Open), in the torque units set in Preferences.

## Gears
**1-Speed**, **2-Speed** or **3-Speed**: HVE's multi-speed differential. Below it:

- **High** — shown greyed: it is the **Final Drive Ratio** of the Transmission section.
- **Low** (2-Speed), or **Medium** and **Low** (3-Speed) — the other ratios. Choosing more speeds starts a new ratio at the final drive.

The engines use one ratio at a time, chosen by the event's **Differential** schedule in [Driver Controls Gear](../09-events-driver-controls/DriverControls5.md). With no schedule they use High for the whole run, so Medium and Low change nothing. SIMON and EDVDS read the schedule; **EDVSM refuses a multi-speed differential** (an HVE engine check), and a note in the section says so. A vehicle read from an HVE vehicle or case carries its own number of speeds and ratios.

!!! tip "New in HVE 2027"
    **The differential type is an HVE 2027 extension.** HVE records the type but greys it, because its drivetrain model assumes an open differential. HVE 2027 implements Limited Slip and Locked and enables the control; a blue note in the section says so. **Open** reproduces HVE's behavior exactly (equal torque to both sides). Limited Slip and Locked send torque to the slower wheel, which matters only when the two sides have different grip; with equal grip the result is unchanged.


<!-- NAV -->

---

← Previous: [Brake System Pressure vs Pedal Force Dialog Box](BrkSysVsPedFrcDlg.md)  |  [Index](README.md)  |  Next: [Disk Brake Dialog Box](DiskBreakDlg.md) →

<!-- /NAV -->
