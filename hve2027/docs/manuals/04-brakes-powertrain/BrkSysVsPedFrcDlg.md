# Brake System Pressure vs Pedal Force Dialog Box

The brake system parameters for the current vehicle are displayed and edited using the **Brake System Pressure** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Brakes › Brake System Pressure...**. The **Vehicle** list at the top selects the vehicle. Pressures and forces are shown in the units set in Preferences.

This dialog contains the following items:

## Axle
Selects the axle (Axle 1 up to the vehicle's number of axles) whose System Type is displayed. Pedal Ratio is per vehicle and is shown only with Axle 1 selected.

## System Type
Radio buttons: **Hydraulic** or **Air (Pneumatic)**.

## Parameters

### Pedal Ratio
Ratio of master cylinder pressure per unit of brake pedal force (kPa/N in SI, psi/lbf in US units; the other unit is shown beside it). A vehicle read from an HVE file carries HVE's own ratio. A value of **0** means: derive the ratio from the curve below.

### Pressure Ratio
A ratio from 0 to 2. It is used as the pedal ratio only when Pedal Ratio is 0 and the curve below has no usable last row.

## Pressure vs Pedal Force

A table of **Pedal Force** against **Pressure**, with an **x** button to delete a row (at least two rows are kept) and **Add Point** to add one (up to 20). When Pedal Ratio is 0, only the **last** row is used: its pressure divided by its pedal force becomes the pedal ratio; the rows between are kept but not sampled. When Pedal Ratio is not 0, the curve is not used. If neither gives a ratio, 6.67 kPa/N is used.

**Close** closes the dialog.

!!! note "HVE 2027"
    **System Type** reaches SIMON's input report only (its *Brake System* row); no engine's physics reads it, and only Axle 1's entry is used, since HVE stores one per vehicle. The hydraulic/air distinction reaches the physics through the per-wheel brake type in the [Brake Assembly](BrkAsmblyDlg.md) dialog.

    HVE's Brake System dialog also has **Assembly Type** and **ABS Installed**. In HVE 2027 they are elsewhere:

    - **Assembly Type**: the disc/drum choice is the per-wheel **Brake Type** in Brake Assembly.
    - **ABS Installed**: in **Vehicle › Brakes › ABS / Brake Design... › ABS System...**, with the system-level ABS parameters (HVE's **Edit...** button). SIMON regulates every wheel when it, or any wheel's **Antilock (ABS)** box in Brake Assembly, is ticked. EDSVS and EDVTS use the per-wheel boxes, and EDVDS has no ABS model.

!!! warning "Not in HVE 2027"
    - HVE's rule that disables Pedal Ratio for a vehicle with no driver.
    - The warning HVE gives on opening when the right and left brake types on an axle differ.

!!! tip "New in HVE 2027"
    The editable pressure vs pedal force curve, and the Pressure Ratio.

<!-- NAV -->

---

← Previous: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md)  |  [Index](README.md)  |  Next: [Differential Data Dialog Box](DiffDataDlg.md) →

<!-- /NAV -->
