# Brake Assembly Dialog Box

The Brake Assembly properties for the selected wheel are displayed and edited using this dialog box.

This dialog box contains the following parameters.

## Time Lag (sec)
Time required before the driver's brake pedal inputs reach the wheel.

## Time Rise (sec)
Time required for the brake system pressure at the wheel to begin causing the maximum brake torque as specified by the Brake Torque Ratio.

## Brake Assembly Type
An option list displaying the type of brake assembly used at the selected wheel location. The default is Generic. In this case, the Brake Torque Ratio is defined directly by the user. The other types are Disc, Duo-Servo, Duplex, Single Piston, Dual Piston, S-Cam, Single Wedge, Dual Wedge and Air Disc.

## Edit ...
Opens the Brake Designer dialog for the currently selected Brake Assembly Type, allowing the physical brake components to be edited. This button is disabled when the Generic type is selected. When a specific brake design is used, the Push-out Pressure and Brake Torque Ratio are computed by the Brake Designer; selecting Disc or Air Disc also sets the wheel brake assembly type for the axle to Disc, while the drum-based designs set it to Drum.

## Push-out Pressure (psi)
Brake system pressure required to begin causing brake torque (any system pressure below this point is simply taking out the slack in the system). User-editable for the Generic type; computed by the Brake Designer for the other types.

## Brake Torque Ratio (in-lb/psi)
Wheel brake torque per unit of system pressure at the wheel. The actual braking torque at the wheel is the product of the current wheel system pressure and the Brake Torque Ratio. User-editable for the Generic type; computed by the Brake Designer for the other types.

## Proportion On
Click on the check box if the system pressure at the selected wheel is reduced by a proportioning value.

## Pstart (psi)
Beginning at this level of system pressure, any additional master cylinder pressure will be reduced.

## Ratio
At master cylinder pressure above the Proportioning Starting Pressure, additional pressure is reduced by this ratio.

## Simple Antilock On
Click on this check box if the selected wheel has a simple (functional) anti-lock device installed. Checking this option enables the Antilock Effectiveness control. The simple antilock controls are available when ABS Installed has been selected in the Brake System Pressure vs Pedal Force dialog.

## Antilock Effectiveness (%/100)
The ability of the anti-lock system to achieve and hold the selected wheel at its peak frictional force, even if the driver braking input exceeds the available frictional force. A 100% effective anti-lock system maintains a longitudinal wheel force associated with the peak coefficient of friction. A 0% effective system maintains a longitudinal wheel force associated with the slide coefficient of friction. A 50% effective system would maintain a longitudinal force halfway between that associated with peak and slide friction.

## ABS Designer...
Opens the ABS Designer dialog, used to edit the detailed ABS wheel data (wheel kinematics thresholds such as minimum velocity, tire slip range and spin acceleration range, and pressure modulation parameters such as cycle rate, apply/release delays and apply/release rates) for the selected wheel. This button is enabled only when ABS Installed has been selected in the Brake System Pressure vs Pedal Force dialog. *(New option; not documented in the previous manual.)*

## Copy to Other Side
Check this check box if you want all the properties set for this wheel to be copied to the wheel on the other side of the same axle.

## Copy to Other Axles
Check this check box if you want all the properties set for this wheel to be copied to the wheels on the other axles. *(New option; not documented in the previous manual.)*

---
*Source topic: BrkAsmblyDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Brakes & Powertrain](README.md)  |  [Index](README.md)  |  Next: [Brake Designer Material Properties Dialog Box](BrkMatPropDlg.md) →

<!-- /NAV -->
