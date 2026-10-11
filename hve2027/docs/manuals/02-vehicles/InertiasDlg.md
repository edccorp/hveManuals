# Inertia Dialog Box

**Axle Inertia**

HVE edits the solid-axle beam's weight and inertia in a separate Inertia dialog opened from the Suspension Data dialog. HVE 2027 has no separate dialog: the same values are two rows of the **Suspension Data** dialog (**Vehicle › Suspension Data...** in the Vehicle Editor, or **Suspension...** under Vehicle Properties), in its **Solid Axle** group, one column per axle. See the [Suspension Data Dialog](../03-suspension-steering/SuspDlg.md).

## Beam Mass, 0=default
Weight of the axle beam and spring (shown as a weight in US units and as a mass in SI units). Do not include the wheels; their mass is included with the tires. A value of 0 lets HVE 2027 use its own default, and the run status says that the default was used.

## Beam Inertia, 0=default
Inertia of the axle beam about its own center, used for both roll and yaw (HVE's single *Roll/Yaw Inertia*). A value of 0 lets HVE 2027 estimate it from the beam mass and the track width, and the run status says that the estimate was used. Do not include wheel inertias; they are included with the tires.

!!! warning "Not in HVE 2027"
    - A separate Axle Inertia dialog, and HVE's rule that enables it only for a non-independent suspension: the two rows are always editable.

<!-- NAV -->

---

← Previous: [CG To Bottom](CGsToAll5.md)  |  [Index](README.md)  |  Next: [Moving CG](MoveCGDlg.md) →

<!-- /NAV -->
