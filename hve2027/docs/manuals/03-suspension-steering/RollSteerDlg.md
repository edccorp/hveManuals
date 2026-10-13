# Roll Steer Dialog

The roll steer properties of the wheels are displayed and edited in the **Roll Steer** dialog. Open it in the Vehicle Editor as the **Roll Steer** tab of **Vehicle › Suspension Data...**. The **Vehicle** list at the top selects the vehicle.

Where HVE edits one wheel at a time, and opens either this polynomial dialog (independent suspension) or the single-coefficient [Roll Steer Properties](RollSteerNewDlg.md) dialog (solid and tandem axles), HVE 2027 shows one table with a column per wheel (**A1 Right**, **A1 Left**, **A2 Right**, ...) holding both the polynomial and the solid-axle coefficient.

## Link Group

Four small buttons per wheel: **-**, **A**, **B** and **C**. Wheels in the same group share their values, as in the [Jounce and Rebound Stops Dialog](JouAndRebDlg.md).

## Constant
Initial steer angle at zero suspension deflection (constant term of the polynomial).

## Linear
Linear coefficient of roll steer vs. jounce/rebound deflection.

## Quadratic
Quadratic coefficient of roll steer vs. jounce/rebound deflection.

## Cubic
Cubic coefficient of roll steer vs. jounce/rebound deflection.

## Solid axle
The solid-axle roll steer coefficient; see [Roll Steer Properties](RollSteerNewDlg.md).

!!! warning "Not in HVE 2027"
    - The **Roll Steer vs. Jounce/Rebound** graph, **Apply** and **Print**.
    - Units on the coefficients: HVE 2027 shows plain numbers with no unit label and does not convert them with the Preferences units. HVE labels them deg, deg/in, deg/in² and deg/in³.

<!-- NAV -->

---

← Previous: [Jounce and Rebound Stops Dialog](JouAndRebDlg.md)  |  [Index](README.md)  |  Next: [Roll Steer Properties](RollSteerNewDlg.md) →

<!-- /NAV -->
