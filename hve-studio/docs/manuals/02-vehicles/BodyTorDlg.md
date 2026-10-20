# Body Torsion Dialog

**Body Torsion Dialog**

The HVE Vehicle Model includes the capability to model torsional distortion of the body. By default, the body is assumed to be rigid. However, the user may wish to edit these default parameters, if the actual torsional stiffness of the body is known, to study the effect of torsional distortion on vehicle handling.

Open the dialog in the Vehicle Editor with **Vehicle › Editors › Body Torsion...**; it is also reached from the **Body Torsion...** button of the **Crush & Geometry** window (**Event › Crush Profile...**). The **Vehicle** list at the top selects the vehicle. Values are shown in the units set in Preferences, and take effect as they are typed; close the dialog with its close button.

The parameters of this dialog are as follows:

## Torsional Stiffness
Specify the torsional stiffness of the body.

## CG to Torsion Axis
Specify the vehicle-fixed z-distance from the CG to the torsional roll axis.

!!! note "HVE Studio"
    An orange note in the dialog states how the values are used: only an **articulated** vehicle uses them. SIMON applies the torsional stiffness as the torsional term of the tow/trailer constraint moment (the fifth-wheel roll path), and EDVDS reads it only for its report. A single vehicle ignores both values. In HVE Studio's tests the stiffness could not be made to change a result even on a coupled rig, because in a steady turn both units roll alike and the torque it scales is near zero.

!!! warning "Not in HVE Studio"
    HVE displays the CG to Torsion Axis distance relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

<!-- NAV -->

---

← Previous: [A Stiffness Coefficient Dialog](AStiffDlg.md)  |  [Index](README.md)  |  Next: [B Stiffness Coefficient Dialog](BStiffDlg.md) →

<!-- /NAV -->
