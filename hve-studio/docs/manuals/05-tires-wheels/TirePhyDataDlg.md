# Tire Physical Data Dialog

In HVE the Tire Physical Data dialog edits one tire's physical parameters. In
HVE Studio the same parameters are rows of the **Tire Properties** table (Vehicle
editor, **Vehicle › Editors › Tires...**), with one column per wheel, so
every wheel of the vehicle is visible and editable at once. Each value is a
drag field: drag it, or double-click (Ctrl+click) and type. Values follow the
units set in Tools › Preferences; the unit is shown in each row label.

!!! note "HVE Studio"
    Columns that share a link group (the **– A B C** buttons at the top of the
    table) change together. See [Tire Information](TireInfoDlg.md) for the link
    groups and the **Build from Tire Size** section, which fills the radius,
    widths, tread depth and pressure from a size designation.

![Tire Properties window](images/hvn-tire-properties.png)

The rows, in table order:

## Friction rows

These are the tire's scalar friction values. They are used when the tire has no
load/speed friction table of its own (the **Load & Speed Tables** panel below
the grid; see [Tire Friction Data](TireFrictDataDlg.md)), and they seed the table when one is created there.

- **Peak Long. Friction** — maximum F<sub>x</sub>/F<sub>z</sub>.
- **Peak Lat. Friction** — maximum F<sub>y</sub>/F<sub>z</sub>.
- **Slide Friction** — F<sub>x</sub>/F<sub>z</sub> at 100 percent longitudinal slip.
- **Slip at Peak (frac)** — longitudinal slip at which the peak occurs.

When every wheel has a friction table, these rows show each wheel's table
values read-only, at the table's middle load row and lowest speed (the values
EDSMAC4 and the other single-value programs use), each with its table's
row count beside it ("3 rows"); hover a value for the row's load.
Edit them in the table. When only some wheels have a table, the row stays
editable and is greyed on those wheels.

**Velocity Dependence** — the change in friction per unit speed (s/in or s/m).
It is the field of HVE's 2-D Tire Data dialog, and as in HVE a non-zero value
is turned into a second speed column of the friction table, moving peak and
slide friction together; HVE Studio does this when the event is run. It is
greyed for a wheel whose friction table already has two or more speeds, and
not shown when every wheel's table does.

## Cornering Stiffness

Slope of the F<sub>y</sub> vs slip-angle curve at zero slip, entered per degree
in US units. It is used when the tire has no cornering table, and seeds one
when it is created. When every wheel has a cornering table, the row shows each
wheel's table value read-only, at its middle load row and middle speed.

Camber stiffness has no scalar field: it exists only as the load × speed table
on the **Camber** tab of the **Load & Speed Tables** panel below the grid.

## Min Skid Fz

Minimum vertical tire force required to leave a visible tire mark on the road.

## Pneumatic Trail

Longitudinal distance from the center of the tire contact patch to the center of
pressure. Pneumatic trail increases the self-aligning tendency of a steerable
wheel. The value is signed; HVE's own vehicle data usually carry a negative
trail, and it is kept with its sign.

## Align Torque Coeff

Self-aligning torque coefficient due to mechanical and pneumatic trail.

## Relaxation Length

Read by SIMON only: the rolling distance over which a slip angle builds the
tire's side force, in the length units set in Preferences. Each wheel has a
**default** checkbox; ticked (the default), the relaxation length is one
unloaded radius of that tire (car tires measure about one to two radii), and
the field shows that value greyed. Untick it to enter a length. **0** gives
HVE's own instant side force for that tire.

!!! tip "New in HVE Studio"
    HVE's tire data has no relaxation length, and HVE's SIMON applies the side
    force at once. Set the length to 0 to reproduce that.

## TMeasy rows

Three rows, read by SIMON only, and only when the event's **Tire Model** is
**TMeasy (Rill)** (SIMON Options, opened with **Method Options...** in Event
Information; see [SIMON Calculation Options](../10-calculation-options/CalcOptSIMON.md#tire-model)).
TMeasy builds each tire's force curve, in each direction, from an initial
slope, a peak and a sliding level. It takes them from the tire's existing
data at its current load and speed — the longitudinal stiffness and cornering
stiffness for the slopes, peak and slide friction for the peak and sliding
forces, **Slip at Peak** for the longitudinal peak — and from these three rows
for the shape that HVE's tire data does not describe:

- **TMeasy Lateral Peak Slip (tan a)** — the lateral slip, as the tangent of
  the slip angle, at which the side force reaches its peak.
- **TMeasy Long. Sliding Slip** — the longitudinal slip ratio from which the
  tire is fully sliding, at slide friction.
- **TMeasy Lateral Sliding Slip (tan a)** — the tangent of the slip angle from
  which the tire is fully sliding.

Each wheel has an **auto** checkbox, ticked by default, and the field then
shows *auto*. With **auto** ticked:

- the lateral peak slip is twice the slip at which the cornering stiffness
  alone would reach peak friction (2 × μ × F<sub>z</sub> / C<sub>α</sub>, at
  the tire's load);
- the longitudinal sliding slip is 1, a locked wheel, where HVE's own friction
  curve reaches slide friction;
- the lateral sliding slip is 1 (45°).

Untick **auto** to enter a value (0.01 to 5). The semi-empirical tire models
do not read these rows.

!!! tip "New in HVE Studio"
    HVE has no TMeasy tire model, and its tire data has no lateral peak slip
    or sliding slips.

## Unloaded Radius

Undeflected tire radius (no-load condition).

## Static Deflection

Shown read-only. It is not an input:
as in HVE, the static deflection is computed from the wheel's share of the
vehicle weight and the initial deflection rate.

## Dual Tires / Dual Spacing

See [Tire Information](TireInfoDlg.md).

## Spring Initial Rate

The initial tire spring rate (vertical tire load per unit of tire deflection).
HVE's *Initial Deflection Rate*.

## Spring Second Rate

The spring rate under conditions of excessive tire vertical load. HVE's
*Secondary Deflection Rate*.

## Second Rate Deflect

Tire deflection at which the secondary rate begins. HVE's *Deflection at
Secondary Rate*.

## Max Deflection

Tire maximum deflection. This value is normally used to terminate execution,
indicating the probability of a damaged or broken wheel rim.

## Tire Inertia

Tire rotational inertia about its spin axis. HVE's *Spin Inertia*.

## Tire Weight

Total weight of the wheel assembly (tire plus rim). For an independent
suspension, the value reflects the total unsprung mass. For a solid axle
suspension system, the axle weight is added to the wheel weight to determine
unsprung mass.

## Steer Inertia

Tire rotational inertia about its steering axis.

## Rolling Resistance: Const Coeff

Tire rolling resistance constant force coefficient (a fraction of the vertical
load).

## Rolling Resistance: Linear Coeff

Tire rolling resistance linear, velocity-dependent force coefficient.

## Max Width

Maximum section width of the tire. Filled by **Build from Tire Size**; editable.

## Tread Width

Width of the tire tread.

## Tread Depth

Depth of the tire tread.

## Nominal Pressure

Nominal (rated) inflation pressure of the tire.

!!! note "HVE Studio"
    Each value is clamped to the range set for it in **Tools › Limits Editor**
    as you edit it, instead of being range-checked when the dialog is closed.
    There is no OK/Cancel: edits apply immediately, and **Edit › Undo** (Ctrl+Z)
    takes one back.

<!-- NAV -->

---

← Previous: [Tire Information Dialog](TireInfoDlg.md)  |  [Index](README.md)  |  Next: [Tire Save As Dialog](TireSaveAsDlg.md) →

<!-- /NAV -->
