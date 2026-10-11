# Brake System Pressure vs Pedal Force Dialog Box

The brake system parameters for the current vehicle are displayed and edited using the **Brake System Pressure** dialog. Open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Brake System Pressure...**. The **Vehicle** list at the top selects the vehicle. Pressures and forces are shown in the units set in Preferences.

This dialog contains the following items:

## Axle
Selects the axle (Axle 1 up to the vehicle's number of axles) whose System Type and Assembly Type are displayed. Pedal Ratio is per vehicle and is shown only with Axle 1 selected.

## System Type
Radio buttons: **Hydraulic** or **Air (Pneumatic)**.

## Assembly Type
Radio buttons: **Disc** or **Drum**.

## Parameters

### Pedal Ratio
Ratio of master cylinder pressure per unit of brake pedal force (kPa/N in SI, psi/lbf in US units; the other unit is shown beside it). A vehicle read from an HVE file carries HVE's own ratio. A value of **0** means: derive the ratio from the curve below.

### Pressure Ratio
A ratio from 0 to 2. It is used as the pedal ratio only when Pedal Ratio is 0 and the curve below has no usable last row.

### ABS Installed
Check box recording whether the vehicle is equipped with an anti-lock brake system.

## Pressure vs Pedal Force

A table of **Pedal Force** against **Pressure**, with an **x** button to delete a row (at least two rows are kept) and **Add Point** to add one (up to 20). When Pedal Ratio is 0, only the **last** row is used: its pressure divided by its pedal force becomes the pedal ratio; the rows between are kept but not sampled. When Pedal Ratio is not 0, the curve is not used. If neither gives a ratio, 6.67 kPa/N is used.

**Close** closes the dialog.

!!! note "HVE 2027"
    Three of these controls are recorded with the case but **no engine reads them** (with **View › Show Guidance Text** on, the dialog says so beside each):

    - **System Type**. The hydraulic/air distinction reaches the engines through the per-wheel brake type in the [Brake Assembly](BrkAsmblyDlg.md) dialog.
    - **Assembly Type**. The disc/drum choice that reaches the engines is the per-wheel **Brake Type** in Brake Assembly; setting this one to Drum does not make the wheels drum-braked.
    - **ABS Installed**. Whether ABS runs is decided by the per-wheel **Antilock (ABS)** flag in Brake Assembly and the ABS System data; this box changes neither, and it does not enable or disable the antilock controls.

    The system-level ABS parameters (HVE's **Edit...** button) are in **Vehicle › ABS / Brake Design... › ABS System...**.

!!! warning "Not in HVE 2027"
    - HVE's rule that disables Pedal Ratio for a vehicle with no driver, and enables the ABS **Edit...** button only when ABS Installed is checked.
    - The warning HVE gives on opening when the right and left brake types on an axle differ.

!!! tip "New in HVE 2027"
    The editable pressure vs pedal force curve, and the Pressure Ratio.

<!-- NAV -->

---

← Previous: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md)  |  [Index](README.md)  |  Next: [Differential Data Dialog Box](DiffDataDlg.md) →

<!-- /NAV -->
