# Tire Information Dialog

In HVE the Tire Information dialog selects a tire for one wheel position from
the tire databases (Type, Manufacturer, Model, Size, Source Database) and opens
the tire's physical-data and table dialogs. In HVE Studio every tire parameter of
every wheel is edited directly in one table, the **Tire Properties** window,
and a tire is picked from HVE's databases in its **Tire Database** section.

!!! note "HVE Studio"
    Open it in the Vehicle editor (F3) with **Vehicle › Editors › Tires...**.
    The window shows the current vehicle (chosen in the **Vehicle** list at the
    top) with one column per wheel: **A1 Left**, **A1 Right**, **A2 Left**,
    **A2 Left**, and so on. All values are shown in the units set in
    Tools › Preferences. The same window holds the fields of HVE's
    [Tire Physical Data dialog](TirePhyDataDlg.md) and the scalar friction and
    cornering values; the load/speed tables are in the **Load & Speed Tables**
    panel under the grid (see [Tire Friction Data](TireFrictDataDlg.md)).

![Tire Properties window](images/hvn-tire-properties.png)

While a solved run is on screen the window is read-only; reset the run to edit
it. A note at the top says when the vehicle shown is not in the active event.

## Build from Tire Size

HVE Studio's counterpart of choosing a tire by size. Type a size designation in
**Tire Size** (for example P215/65R15, 8R19.5 or 31x10.50R15LT), choose the tire
**Type** (Passenger Car, Light Truck, Heavy Truck, Mobile Home) and the wheels to
change in **Apply to** (All wheels, or one axle), then press **Apply Tire Size**.
The size string is parsed to fill the outer (unloaded) radius, maximum width,
tread width, tread depth and nominal pressure. Friction, cornering stiffness and
spring rates are left unchanged. An unrecognized string, or an obsolete
designation, is reported in the section and the button stays disabled.

The section starts from the size and type already stored on the vehicle's
first wheel.

## Tire Database

HVE Studio's counterpart of choosing a tire by Type, Manufacturer, Model, Size and
Source Database. The collapsed **Tire Database** section lists the tires in the
HVE vehicle databases HVE Studio finds (the same folders the vehicle database
picker reads), each as manufacturer, model and size with its source database in
brackets. **Type** narrows the list, **Database** shows only the tires of one
database file (*All databases*, or a file with its tire count), and **Search**
filters it by manufacturer, model or size. While the list is narrowed, a line
under it reads *Showing N of M*. Selecting a tire shows its radius, ride rate and the size of its
tables. **Apply Tire** replaces the tire data and all four tables of the wheels
chosen in **Apply to** (All wheels, or one axle) with the database tire's; each
wheel keeps its own dual setup.

## Link Group

The row of **–  A  B  C** buttons at the top of every column. Columns in the same
group (A, B or C) are edited together: changing a value in one changes it in all
the others of that group, and moving a column into a group copies that group's
current values into it, its four **Load & Speed Tables** included. **–** makes a
wheel independent. All wheels start in group A. The tables panel below the grid
follows the same groups.

!!! note "HVE Studio"
    The link groups replace HVE's **Copy to Other Side** and **Copy to Other
    Axles** check boxes.

## Size Designation and Tire Type

Shown read-only in the Physical part of the table. They are set by **Build
from Tire Size** or the **Tire Database**, not typed. The physics
re-parses the size itself: DyMESH builds a wheel's contact mesh from it, and
the soft-soil and radial-spring tire–terrain models take the tire width from
it. A wheel with no size is flagged "(none: P225/75R16)", the size the engine
falls back to.

## Dual Tires

Check box indicating that this wheel position uses dual tires.

## Dual Spacing

Lateral distance between the centerlines of the two tires of a dual pair.
Greyed for a wheel whose Dual Tires box is unchecked.

## Tire Name, Manufacturer, Model

Text rows of the table's **Identity (report only)** section, with **HVE
Version**. They are filled when a vehicle is imported or a tire is applied from
the Tire Database; every engine's tire report prints them, and nothing else
reads them.

## Fields that moved

The remaining rows of the table — friction, cornering stiffness, pneumatic trail,
spring rates, inertias, rolling resistance and dimensions — are described on the
[Tire Physical Data](TirePhyDataDlg.md) page.

Where every wheel has a friction table, the friction rows (peak longitudinal
and lateral friction, slide friction, slip at peak, velocity dependence) are
not shown: those values are entered in the tables, even when a table has one
load and one speed, and the Friction section says so in one line. The same goes
for **Cornering Stiffness** when every wheel has a cornering table. When only
some wheels have a table, the row stays, greyed on those wheels.

The HVE buttons **Friction...**, **Fy vs Slip Angle...**, **Fy vs Inclination
Angle...** and **Slip vs Roll-Off...** are the **Friction Table**, **Cornering
Table**, **Camber Table** and **Fy Roll-off** rows of the table's **Load &
Speed Dependence** section: each wheel's button shows the size of its table
(hover it for the contents) and selects that wheel and that table's tab in the
**Load & Speed Tables** panel below the grid; the button for the table on
screen is highlighted. A drag bar between the grid and the panel resizes them.
**Physical Data...** has no counterpart: the physical data are in the same
table.

!!! warning "Not in HVE Studio"
    - **Mass**: the table shows the tire's **Tire Weight** instead.
    - **Save As...** and **Delete**: a tire cannot be saved to, or deleted from,
      a database on its own (see [Tire Save As](TireSaveAsDlg.md)).
    - **OK / Cancel**: edits apply as you make them; **Edit › Undo** (Ctrl+Z) or
      **Edit › Undo History...** takes one back.

<!-- NAV -->

---

← Previous: [Tire Friction Data Dialog](TireFrictDataDlg.md)  |  [Index](README.md)  |  Next: [Tire Physical Data Dialog](TirePhyDataDlg.md) →

<!-- /NAV -->
