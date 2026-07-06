# Tire Information Dialog

The tire parameters for the current vehicle are displayed and edited using the Tire Information dialog. The dialog title bar shows the name of the current vehicle and the wheel position being edited, e.g. *Tire Information: &lt;Vehicle Name&gt; (Axle 1, Left Side)*.

This dialog contains the following items:

## Name

Name of the currently selected tire. The name is editable; while it retains its default form, it is automatically rebuilt from the Type, Manufacturer, Model, Size and Source Database selections. The name must be unique within the case.

## Type

Tire type. The available types are Passenger Car, Light Truck, Heavy Truck and Mobile Home (only types present in the loaded tire databases are listed). Changing the type refreshes the Manufacturer, Model, Size and Source Database lists.

## Manufacturer

Manufacturer of the selected tire. The list contains all manufacturers available in the tire databases for the chosen Type.

## Model

Model of the selected tire, as available in the tire databases for the chosen Type and Manufacturer. (The dialog label reads "Modal" in some versions; it refers to the tire model.)

## Size

Size designation of the selected tire (e.g. P215/65R15). The size string is parsed to compute the tire's section width, rim radius and outside radius; an invalid or incompatible size string produces an error when the dialog is accepted.

## Source Database

Database file from which the selected tire's data are drawn (e.g. EDVDB.DB, User.DB). When more than one database contains the same tire, each source is listed. Use of the EDC custom vehicle database (Edc.db) requires the appropriate license.

## Mass

Mass of the selected tire, as stored in the selected source database. This field is display-only; it updates as the Type/Manufacturer/Model/Size/Source Database selections change. (New since the original help.)

## Dual Tires

Check box indicating that this wheel position uses dual tires. Checking it enables the Dual Tire Spacing field.

## Dual Tire Spacing

Lateral distance between the centerlines of the two tires of a dual pair. Enabled only when Dual Tires is checked.

## Physical Data...

Displays the [Tire Physical Data dialog](TirePhyDataDlg.md).

## Friction...

Displays the [Tire Friction Data dialog](TireFrictDataDlg.md).

## Fy vs Slip Angle...

Displays the Tire F<sub>y</sub> vs Slip Angle dialog (see FyVsSlipAngDlg).

## Fy vs Inclination Angle...

Displays the [F<sub>y</sub> vs Inclination Angle dialog](FyVsInclAngDlg.md).

## Slip vs Roll-Off...

Displays the [Slip vs Roll-Off dialog](SlipVsRollOffDlg.md).

## Copy to Other Side

Copies all the settings of the selected tire (including dual tire settings) to the tire on the other side of the same axle when the dialog is accepted.

## Copy to Other Axles

Copies the selected tire to the same side of all other axles of the vehicle when the dialog is accepted. If Copy to Other Side is also checked, the tire is copied to every wheel position on the vehicle. (New since the original help.)

## Save As...

Displays the [Tire Save As dialog](TireSaveAsDlg.md), which saves the current tire to the user database on disk.

## Delete

Removes the tire from the user database (User.DB) after confirmation, then rebuilds the vehicle database. This button is enabled only for tires that reside in the user database.

## OK / Cancel

OK validates the entries (dual tire spacing range, unique tire name, valid tire size string), stores the tire at the selected wheel position and applies any Copy to Other Side / Copy to Other Axles requests. Cancel discards all changes.

---
*Source topic: TireInfoDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Tire Friction Data Dialog](TireFrictDataDlg.md)  |  [Index](README.md)  |  Next: [Tire Physical Data Dialog](TirePhyDataDlg.md) →

<!-- /NAV -->
