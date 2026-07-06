# Damage Data

The Damage Data dialog allows the user to assign a damage profile to the selected vehicle. The damage profile is obtained by post-crash inspection of the vehicle, and provides a significant amount of useful information about the collision.

The right side of the dialog contains a graphic pane that draws the vehicle outline, the damage profile, the impulse center and the PDOF arrow; the drawing is updated as values are edited.

## CDC

HVE's Damage Data dialog requests the user for a Collision Deformation Classification (CDC), a seven-character code describing the vehicle damage. The CDC is an SAE Recommended Practice.

The entered CDC is used to define a default PDOF and damage profile, which includes damage width, depth and location. The default data provided by the CDC are used to fill in the fields in the Damage Data dialog. The resulting delta-V, damage energy and peak force are calculated and displayed in the dialog. The delta-V is used to assign a default value of equivalent barrier speed (EBS) for the selected vehicle. If an invalid CDC is entered, the damage profile fields are grayed out until it is corrected.

## PDOF (deg)

Simply stated, the PDOF is the direction of the impulse. This, of course, has physical significance, because the direction of the impulse is the same as the direction of the delta-V. In fact, because the damage analysis has no way of computing the forward and lateral components of the delta-V, the user-entered PDOF is used for this purpose.

The PDOF is assigned by the CDC as the closest hour angle (or clock direction). The Damage Data dialog displays the resulting PDOF in degrees. This value may be edited by the user if a more precise value is known (note that the precision of the clock direction is limited by the number of degrees in one hour, or 30 degrees).

## Use Newton's 3rd Law

Checkbox. When checked, the PDOF edit field is disabled and the PDOF is calculated automatically so that it is consistent with the damage data assigned to the other vehicle in the collision (the impulses on the two vehicles must be equal and opposite). Uncheck this option to enter the PDOF manually.

## Impulse Center (in) - x

Vehicle-fixed X coordinate of the impulse center.

## Impulse Center - y

Vehicle-fixed Y coordinate of the impulse center.

## Basis

Radio buttons selecting the basis used for the vehicle's damage data:

- **EES** — Select EES (equivalent energy speed; the radio button is captioned "EES" on screen) as the basis for the damage data. When selected, the EBS field below (the separate numeric edit, labeled "EBS") is enabled and the damage profile fields (zones, width, offset, crush depths, A Stiff, B Stiff) are disabled.
- **Damage Profile** — Select Damage Profile as the basis for the damage data. When selected, the damage profile fields are enabled and the EBS field is disabled.

## EBS (EES)

Equivalent Barrier Speed: the speed at which the vehicle would have sustained the same amount of damage if it had struck a fixed rigid barrier.

## Damage Profile (zones)

Drop-down list selecting the number of crush zones in the damage profile, from *1 zone* to *9 zones*. The number of zones determines the number of crush depth measurements (number of zones + 1) shown in the crush depth table.

## Width (in)

The Damage Width is the width of the damage region. The default value assigned by the CDC does not include induced damage (non-contact damage adjacent to the area of actual contact with another vehicle). In most cases, the user should include induced damage if the goal is to estimate delta-V.

## Offset (in)

The longitudinal or lateral distance from the CG to the midpoint of the damage profile.

## Crush Depth Table (Data Grid)

Table defining the damage profile. Each row is one crush measurement location (C1, C2, ... Cn, where n = number of zones + 1) with an editable **Crush Depth** (in) value. Default depths are assigned from the CDC and may be edited.

## Delta-V Total (mph)

Change in velocity during the collision; total magnitude. Read-only, calculated from the damage data.

## Delta-V Long (mph)

Change in velocity during the collision; longitudinal component. Read-only, calculated from the damage data.

## Delta-V Lat (mph)

Change in velocity during the collision; lateral component. Read-only, calculated from the damage data.

## Damage Energy (ft-lb)

Energy dissipated by crush during the collision. Read-only, calculated from the damage data.

## Peak Force (lb)

The peak collision force. Read-only, calculated from the damage data.

## A Stiff...

Displays the A Stiffness Coefficients dialog: the force per unit of damage width required to initiate measurable (permanent) damage, for each crush zone. Enabled only when the basis is Damage Profile. Default values come from the CDC's damaged side (front, back or side).

## B Stiff...

Displays the B Stiffness Coefficients dialog: the force per unit of crush depth per unit of damage width required to cause the measured damage, for each crush zone. Enabled only when the basis is Damage Profile.

## Apply

Validates the current entries, recalculates the delta-V, damage energy and peak force, and updates the damage profile drawing without closing the dialog.

## OK / Cancel

OK validates and saves the damage data and closes the dialog; Cancel discards the changes.

---
*Source topic: DamageData.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Common Scene Report Dialog](CommSceDlg.md)  |  [Index](README.md)  |  Next: [Trajectory Report](TrajRepDlg.md) →

<!-- /NAV -->
