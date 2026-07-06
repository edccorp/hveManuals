# Brake System Pressure vs Pedal Force Dialog Box

The Brake System parameters for the current vehicle are displayed and edited using this dialog box.

This dialog box contains the following items:

## Brake System Type
Radio buttons selecting the type of brake system installed on the vehicle: **Hydraulic** or **Air**. *(New option; not documented in the previous manual.)*

## Wheel Brake Assembly
This group displays and edits the brake assembly type installed on each axle. *(New group; not documented in the previous manual.)*

**Axle Number**
Drop-down list selecting the axle (1 up to 3, depending on the number of axles on the current vehicle) whose brake assembly type is displayed.

**Brake Assembly Type**
Radio buttons selecting **Disc** or **Drum** for the selected axle. Note that this setting is also updated automatically when a specific brake design is chosen in the Brake Assembly dialog (Disc and Air Disc designs set it to Disc; drum-based designs set it to Drum). A warning message is issued when the dialog opens if the right and left brake types on an axle are different, as this is probably a mistake.

## ABS Installed
Check this box if the vehicle is equipped with an anti-lock brake system. Checking this option enables the Edit... button and enables the antilock options in the Brake Assembly dialog. *(New option; not documented in the previous manual.)*

## Edit...
Opens the ABS System Data dialog, used to edit the system-level ABS parameters: control source, ABS algorithm, control method, cycle rate, ABS pressure threshold, ABS velocity threshold, low friction threshold, and delay parameters (delay method, apply delay and release delay). Enabled only when ABS Installed is checked. *(New option; not documented in the previous manual.)*

## Pedal Ratio (psl / lb) *(labeled "psl / lb" in the dialog — a UI typo for psi/lb)*
Ratio of master cylinder pressure per unit of brake pedal force. This control is disabled if the current vehicle has no driver.

---
*Source topic: BrkSysVsPedFrcDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md)  |  [Index](README.md)  |  Next: [Differential Data Dialog Box](DiffDataDlg.md) →

<!-- /NAV -->
