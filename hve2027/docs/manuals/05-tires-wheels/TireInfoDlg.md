# Tire Information Dialog

In HVE the Tire Information dialog selects a tire for one wheel position from
the tire databases (Type, Manufacturer, Model, Size, Source Database) and opens
the tire's physical-data and table dialogs. HVE 2027 has no tire database to
pick from; every tire parameter of every wheel is edited directly in one table,
the **Tire Properties** window.

!!! note "HVE 2027"
    Open it in the Vehicle editor (F3) with **Vehicle › Tire Data (Detailed)...**.
    The window shows the current vehicle (chosen in the **Vehicle** list at the
    top) with one column per wheel: **A1 Right**, **A1 Left**, **A2 Right**,
    **A2 Left**, and so on. All values are shown in the units set in
    Tools › Preferences. The same window holds the fields of HVE's
    [Tire Physical Data dialog](TirePhyDataDlg.md) and the scalar friction and
    cornering values; the load/speed tables are in **Vehicle › Tire Tables...**
    (see [Tire Friction Data](TireFrictDataDlg.md)).

![Tire Properties window](images/hvn-tire-properties.png)

While a solved run is on screen the window is read-only; reset the run to edit
it. A note at the top says when the vehicle shown is not in the active event.

## Build from Tire Size

HVE 2027's counterpart of choosing a tire by size. Type a size designation in
**Tire Size** (for example P215/65R15, 8R19.5 or 31x10.50R15LT), choose the tire
**Type** (Passenger Car, Light Truck, Heavy Truck, Mobile Home) and the wheels to
change in **Apply to** (All wheels, or one axle), then press **Apply Tire Size**.
The size string is parsed to fill the outer (unloaded) radius, maximum width,
tread width, tread depth and nominal pressure. Friction, cornering stiffness and
spring rates are left unchanged. An unrecognized string, or an obsolete
designation, is reported in the section and the button stays disabled.

The section starts from the size and type already stored on the vehicle's
first wheel.

## Link Group

The row of **–  A  B  C** buttons at the top of every column. Columns in the same
group (A, B or C) are edited together: changing a value in one changes it in all
the others of that group, and moving a column into a group copies that group's
current values into it. **–** makes a wheel independent. All wheels start in
group A.

!!! note "HVE 2027"
    The link groups replace HVE's **Copy to Other Side** and **Copy to Other
    Axles** check boxes.

## Size Designation and Tire Type

Shown read-only in the Physical part of the table when **View › Show Guidance
Text** is on. They are set by **Build from Tire Size**, not typed. The physics
re-parses the size itself: DyMESH builds a wheel's contact mesh from it, and
the soft-soil and radial-spring tire–terrain models take the tire width from
it. A wheel with no size is flagged "(none: P225/75R16)", the size the engine
falls back to.

## Dual Tires

Check box indicating that this wheel position uses dual tires.

## Dual Spacing

Lateral distance between the centerlines of the two tires of a dual pair.

!!! note "HVE 2027"
    Dual Spacing is not greyed when Dual Tires is unchecked.

## Fields that moved

The remaining rows of the table — friction, cornering stiffness, pneumatic trail,
spring rates, inertias, rolling resistance and dimensions — are described on the
[Tire Physical Data](TirePhyDataDlg.md) page.

The HVE buttons **Physical Data...**, **Friction...**, **Fy vs Slip Angle...**,
**Fy vs Inclination Angle...** and **Slip vs Roll-Off...** have no counterpart
in this window: the physical data are in the same table, and the four tables are
tabs of the **Tire Friction Data** window (Vehicle › Tire Tables...).

!!! warning "Not in HVE 2027"
    - **Name, Type, Manufacturer, Model, Size, Source Database, Mass**: there is
      no tire database to select from, so there is nothing to choose a tire by.
      A tire's data arrive with the vehicle when an HVE case (`.hve`) or HVE
      vehicle database is opened, and are edited here.
    - **Save As...** and **Delete**: there is no tire database to save a tire to
      or delete it from (see [Tire Save As](TireSaveAsDlg.md)).
    - **OK / Cancel**: edits apply as you make them; **Edit › Undo** (Ctrl+Z) or
      **Edit › Undo History...** takes one back.

<!-- NAV -->

---

← Previous: [Tire Friction Data Dialog](TireFrictDataDlg.md)  |  [Index](README.md)  |  Next: [Tire Physical Data Dialog](TirePhyDataDlg.md) →

<!-- /NAV -->
