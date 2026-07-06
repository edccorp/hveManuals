# Tire Save As Dialog

The Tire Save As dialog saves the current tire, including all of its physical, friction, cornering, camber and roll-off data, to the user database (User.DB). The saved tire then becomes available for selection from the Tire Information dialog with User.DB as its Source Database.

This dialog contains the following items:

## Type

Tire type of the tire being saved (PassengerCar, LightTruck, HeavyTruck or MobileHome). This field is read-only; the type is inherited from the tire selected in the Tire Information dialog.

## Manufacturer

Manufacturer name under which the tire will be stored.

## Model

Model name under which the tire will be stored.

## Size

Tire size designation string. The string is parsed when OK is pressed; the resulting tire width and radius must fall within valid ranges, otherwise an error is displayed and the tire is not saved. The parsed width also updates the tire's Maximum Width physical parameter.

## Security Key

Optional security key stored with the tire record.

## Version Information

Version string stored with the tire record (initialized from the source tire's version number).

## OK / Cancel / Help

OK writes the tire to the user database. The combination of Type, Manufacturer, Model and Size forms the database key; if a tire with the same key already exists, you are asked whether to overwrite it. After saving, the vehicle database is rebuilt so the new tire is immediately available. Cancel closes the dialog without saving. Help displays this topic.

---
*Source topic: TireSaveAsDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Tire Physical Data Dialog](TirePhyDataDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Blow-out Page](WheelsDlg.md) →

<!-- /NAV -->
