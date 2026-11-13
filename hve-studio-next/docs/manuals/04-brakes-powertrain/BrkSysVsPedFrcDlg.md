# Brake System Pressure vs Pedal Force Dialog Box

The brake system parameters for the current vehicle are displayed and edited using the **Brake System Pressure** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake System Pressure...**. The **Vehicle** list at the top selects the vehicle. Pressures and forces are shown in the units set in Preferences. In the Vehicle Designer's **Brakes** stage the same fields are drawn under **Brake System (whole vehicle)**, above the per-wheel **Assembly**, **Designer** and ABS tabs.

Both values belong to the **vehicle**: HVE stores one brake system per vehicle, and every engine reads that one.

This dialog contains the following items:

## System Type
Radio buttons: **Hydraulic** or **Air (Pneumatic)**, marked *(report only)*: see the note below.

## Parameters

### Pedal Ratio
Ratio of master cylinder pressure per unit of brake pedal force (kPa/N in SI, psi/lbf in US units; the other unit is shown beside it). A vehicle read from an HVE file carries HVE's own ratio. A value of **0** means: use the slope of the vehicle's own pressure vs pedal force table where its data has one (below), else 6.67 kPa/N (4.30 psi/lbf).

## Pressure vs Pedal Force

Not shown in HVE Studio. Only the **last** row of such a table was ever used: its pressure divided by its pedal force as the pedal ratio when Pedal Ratio is 0, and its pedal force as full pedal for **At Driver** braking. A vehicle whose data carries a table keeps it, saved with the vehicle; a vehicle without one has none, and uses 6.67 kPa/N and a full pedal of 600 N (135 lbf), the values the table every vehicle used to be given produced.

**Close** closes the dialog.

!!! note "HVE Studio"
    **System Type** reaches SIMON's input report only (its *Brake System* row); no engine's physics reads it. It is one choice for the vehicle (the case keeps a slot per axle from HVE's file layout, and a choice is written to all of them). The hydraulic/air distinction reaches the physics through the per-wheel brake type in the [Brake Assembly](BrkAsmblyDlg.md) dialog.

    HVE's Brake System dialog also has **Assembly Type** and **ABS Installed**. In HVE Studio they are elsewhere:

    - **Assembly Type**: the disc/drum choice is the per-wheel **Brake Type** in Brake Assembly.
    - **ABS Installed**: in **Vehicle › Editors › Brakes › ABS / Brake Design... › ABS System...**, with the system-level ABS parameters (HVE's **Edit...** button). SIMON regulates every wheel when it, or any wheel's **Antilock (ABS)** box in Brake Assembly, is ticked. EDSVS and EDVTS use the per-wheel boxes, and EDVDS has no ABS model.

!!! warning "Not in HVE Studio"
    - HVE's rule that disables Pedal Ratio for a vehicle with no driver.
    - The warning HVE gives on opening when the right and left brake types on an axle differ.

<!-- NAV -->

---

← Previous: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md)  |  [Index](README.md)  |  Next: [Differential Data Dialog Box](DiffDataDlg.md) →

<!-- /NAV -->
