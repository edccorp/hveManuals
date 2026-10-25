# Drive Train Dialog Box

The drivetrain parameters for the current vehicle are displayed and edited using the **Drivetrain** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Drivetrain...**. The **Vehicle** list at the top selects the vehicle. The drivetrain is composed of components that HVE edits in separate dialogs and HVE Studio shows as collapsible sections of one dialog:

- **Engine**
- **Transmission** — see [Transmission Data Dialog Box](TransDataDlg.md)
- **Differential** — see [Differential Data Dialog Box](DiffDataDlg.md)
- **Electronic Stability (ESS)** — HVE's TCS/YSC dialog

![Drivetrain dialog](images/hvn-drivetrain.png)

Torques and inertias are shown in the units set in Preferences. Values take effect as they are typed.

## Engine

### Name
User-editable description of the engine (drivetrain) for the current vehicle.

### Idle RPM
Idle speed of the engine.

### Redline RPM, Max Torque
Used only for a vehicle that has **no engine table**: HVE Studio then builds a simple three-point wide-open-throttle table from the idle speed, the redline and the maximum torque. A vehicle read from an HVE file carries HVE's own engine tables, which are used instead.

### Max Power
Stored with the vehicle. No engine reads it.

### Inertia
Rotational inertia of the drivetrain components (HVE's *Drivetrain Inertia*).

### Friction Torque
Used only for a vehicle that has **no closed-throttle table**: the closed-throttle (engine braking) torque is then this constant value at every speed.

### Engine Tables
HVE's engine tables, one for each **Throttle Position**:

- **Throttle Position** — **Wide Open** or **Closed**: which of the two tables the grid shows.
- The grid — one row per point: **Speed (RPM)**, **Torque** (in the torque units set in Preferences) and **Power** (hp or kW). Speed and torque are edited; **Power** is shown grayed and follows torque × speed, because no engine reads it (SIMON, EDVSM and EDVDS read the speed and torque columns only). **X** deletes a row, **Add Row** appends one (up to 15, HVE's limit).

A table needs at least two rows to be used; with fewer, the engines get the stand-in described under Redline RPM / Max Torque (wide open) or Friction Torque (closed), and a note under the grid says which applies. Speeds must increase down the table (the engines interpolate torque on engine speed); an orange note says so when they do not. The tables act only on the **Pedal** input method in Driver Controls: the %-friction method takes drive torque from tire friction and reads no engine curve.

The tables of a vehicle read from an HVE vehicle or case are imported as HVE stores them.

## Transmission, Differential

See [Transmission Data Dialog Box](TransDataDlg.md) and [Differential Data Dialog Box](DiffDataDlg.md).

## Electronic Stability (ESS)

HVE's TCS/YSC dialog. SIMON implements traction control (TCS) and yaw stability control (YSC).

### TCS Enabled, YSC Enabled
Whether traction control and yaw stability control are installed.

Each field is enabled by the system(s) that read it.

### Min Speed
Below this speed YSC stays inactive (enabled when YSC is on; TCS does not read it).

### Drive Torque Threshold, Drive Torque Rate, Side Spin Diff (rad/s)
Read by both TCS and YSC (enabled when either is on): they act on the drive torque only above the threshold; the rate is the torque moved per unit of spin error; the side spin difference is the left/right wheel-speed difference that triggers a side torque shift.

### Axle Spin Diff (rad/s)
TCS only (enabled when TCS is on): the axle-to-axle speed difference that triggers an axle torque shift.

### Yaw Vel Error (rad/s), Spin Vel Error (rad/s), Brake Press Threshold, Brake Press Rate
YSC only (enabled when YSC is on); the rate is the brake pressure applied per unit of yaw error.

!!! note "Changed in HVE Studio 2026-10-21"
    Min Speed used to be enabled by TCS too, and Drive Torque Threshold, Drive Torque Rate and Side Spin Diff by only one system, though both read them; each now follows the system that reads it.

An orange note in the section states the conditions under which these systems act: they require **Driver Controls › Input Method = At Driver** (TCS runs only when the throttle is driven by the driver model and YSC only when the brake is); TCS rebalances torque between drive axles, so it needs more than one; and YSC's pressure branch acts only while the driver is already braking. Both rates default to 0: if TCS or YSC is enabled with its rate at 0, an orange warning says that the system will report itself active and change nothing.

!!! warning "Not in HVE Studio"
    - The engine chart, **Apply** and **Print...**. (The engine tables themselves are edited in the grid above; the **Power** column cannot be edited, because no engine reads it.)
    - **Transmission...**, **Differential...** and **TCS/YSC...** buttons (the sections are in this dialog).

!!! tip "New in HVE Studio"
    Redline RPM, Max Torque and Friction Torque, which give a vehicle without engine tables a usable engine.

<!-- NAV -->

---

← Previous: [Disk Brake Dialog Box](DiskBreakDlg.md)  |  [Index](README.md)  |  Next: [Dual Piston Brake Dialog Box](DualPistBrkDlg.md) →

<!-- /NAV -->
