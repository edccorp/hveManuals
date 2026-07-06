# Vehicle Inertia Dialog

**Vehicle Inertia Dialog Box**

The inertial properties of the vehicle are displayed and edited using the Vehicle Inertia dialog. The dialog now displays two columns of values — **Total** (total vehicle) and **Sprung** (sprung mass only) — and keeps them consistent: editing a value in one column automatically recalculates the corresponding value in the other column using the vehicle's unsprung (axle/wheel) masses and their locations.

This dialog box contains the following parameters:

## Weight (Total / Sprung)
Vehicle weight. HVE calculates and stores mass by dividing the entered weight by the current acceleration of gravity (set in the Environment Editor). Entering a Total weight updates the Sprung weight, and vice versa.

## Mass (Total / Sprung)
Vehicle mass (weight/g), the value actually stored by the Vehicle Editor. These fields are read-only; they are recalculated whenever a weight is edited.

## Rotational Inertia — Roll (Total / Sprung)
Rotational inertia about the X axis. The Sprung value is the value stored with the vehicle; the Total value includes the unsprung masses.

## Rotational Inertia — Pitch (Total / Sprung)
Rotational inertia about the Y axis.

## Rotational Inertia — Yaw (Total / Sprung)
Rotational inertia about the Z axis.

## XZ Product of Inertia (Sprung only)
Inertial product about the Y axis. This value represents the fact that the x-z plane is not a plane of symmetry for the vehicle sprung mass.

## Basic... / Complex...
Toggles the dialog between the Basic view (Sprung column only, dialog narrowed) and the Complex view (both Total and Sprung columns). The last-used state is remembered between sessions.

## Auto Update When Weight Changes
When checked, the rotational inertias are automatically rescaled in proportion to the change whenever the vehicle weight is edited, so the inertias remain consistent with the new mass. The setting is remembered between sessions.

## Apply
Applies the current values to the vehicle without closing the dialog. OK applies the values and closes the dialog; Cancel discards unapplied changes.

**Note for HVE-2D users:** In HVE-2D the Roll, Pitch and XZ Product fields are read-only, the Total column and the Basic/Complex button are hidden, and only the Yaw inertia may be edited.

---
*Source topic: VehInerDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Getting Information about the Vehicle](VehicleInfoDlg.md)  |  [Index](README.md)  |  Next: [Saving Vehicles](VehSaveAs.md) →

<!-- /NAV -->
