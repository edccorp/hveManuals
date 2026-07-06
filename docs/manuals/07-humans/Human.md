# Inertial Data Dialog Box

Inertial parameters for the HVE Human Model are defined for each of the 15 segments. To view and edit the current human's inertial parameters, click on the desired segment CG and choose Inertias from the segment popup menu. The individual parameters are displayed in the Inertial Data dialog. The dialog title bar shows the current human's name and the selected segment (e.g. Pelvis, Chest, Head).

## Weight
Weight of the selected segment. This field is editable; as the weight is changed, HVE recalculates the segment mass by dividing the entered weight by the current acceleration of gravity (taken from the current environment) and updates the Mass field immediately.

## Mass
Segment mass, calculated as Weight divided by the current acceleration of gravity. This field is read-only.

## Inertia

**Roll**
Rotational inertia about the segment i axis.

**Pitch**
Rotational inertia about the segment j axis.

**Yaw**
Rotational inertia about the segment k axis.

## Total Weight
Total weight of the entire human, calculated as the sum of the masses of all 15 segments multiplied by the current acceleration of gravity. This field is read-only.

> Note: The old help described this field as the "Total weight of the selected segment"; it is actually the total weight of the whole human.

Entered values are range-checked when OK is pressed; out-of-range values must be corrected before the dialog will close.

---
*Source topic: Human.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Humans](README.md)  |  [Index](README.md)  |  Next: [Human Contact Ellipsoids Dialog Box](Human1.md) →

<!-- /NAV -->
