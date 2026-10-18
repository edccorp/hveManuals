# Tire Save As Dialog

In HVE this dialog saves the current tire — its physical, friction, cornering,
camber and roll-off data — to the user tire database (User.DB) under a Type,
Manufacturer, Model and Size key, so it can be chosen later in the Tire
Information dialog.

!!! warning "Not in HVE 2027"
    HVE 2027 has no Tire Save As dialog: a tire cannot be saved to a database
    on its own. Each wheel's tire data are part of the vehicle and are edited
    in place in **Vehicle › Editors › Tires...**, in its per-wheel grid and its Load &
    Speed Tables panel (see [Tire Information](TireInfoDlg.md)). The tire data are
    saved with the case. A tire can be taken from HVE's databases in the
    **Tire Database** section of the Tire Properties window.

    To give several wheels the same tire, put their columns in the same link
    group in the Tire Properties table. To start a tire from a size
    designation, use **Build from Tire Size** in the same window.

<!-- NAV -->

---

← Previous: [Tire Physical Data Dialog](TirePhyDataDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Blow-out Page](WheelsDlg.md) →

<!-- /NAV -->
