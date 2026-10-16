# Wheels — Damage (Displacement) Page

The **Wheel Damage** tab of the event Wheels dialog dynamically varies a wheel's
position and orientation during the simulation and, for physics models that
support wheel damage, models wheel lock-up and DyMESH-based wheel damage forces.

!!! note "HVE 2027"
    In the Event editor (F5) choose **Event › Wheels...** (Ctrl+W) and the
    **Wheel Damage** tab. Each wheel is a column (**A1-R**, **A1-L**, …) instead
    of HVE's Axle No / Side selectors; see
    [Wheels — Blow-out Page](WheelsDlg.md) for the layout and the link groups.
    Lengths, forces and moments follow the units set in Tools › Preferences.
    Only SIMON and EDSMAC4 read this tab. EDSMAC4 applies only the X/Y
    displacement and the camber change — no Z displacement and no lock-up
    torque.

The rows, in table order:

## Displaced / damaged

Check box indicating that the wheel is displaced or damaged during the event.
The rows below it are enabled only when it is checked (except Displacement
rate, see below). HVE's *Wheel is Damaged*.

## Start at first contact

The displacement starts automatically at the vehicle's first contact. When
checked, Damage time is disabled. HVE's *Auto Start*.

## Damage time (s)

Simulation time at which the wheel displacement starts. HVE's *Start Time*.

## Displacement time (s)

Duration over which the wheel displacement occurs. HVE's *Duration*.

## Displacement X / Y / Z

Vehicle-fixed wheel displacement in the X, Y and Z coordinates: +X forward,
+Y right, +Z down.

## Camber change (deg)

Vehicle-fixed wheel camber change angle.

## Lock-up (fraction of peak brake torque)

Peak wheel lock-up torque applied to the damaged wheel, as a fraction. HVE's
*Peak Lock-up Torque*.

## Use DyMESH (wheel contact mesh)

Gives the wheel its own DyMESH contact mesh. Enabled for a damaged wheel; it has
an effect only when DyMESH is on for the event (Event Information › **Method
Options...**, the SIMON Options window), and the dialog warns when a wheel asks for a mesh while DyMESH is
off. It enables the force and moment rows below.

## ...also contact the environment

Lets the wheel mesh contact the environment as well as other vehicles. Enabled
when Use DyMESH is checked. HVE's *Use Environment*.

## Max no-damage force

Maximum contact force the wheel can sustain without being displaced or damaged.

## Displacement rate (force)

Rate at which wheel displacement grows with contact force above the no-damage
threshold.

!!! note "HVE 2027"
    This row is always enabled, on every wheel. It sets each wheel mesh's
    contact stiffness, and HVE gives the two outer rings of every wheel contact
    the value from the **first** vehicle's front-right wheel in the event — so it
    matters even on wheels that do not enable a mesh. HVE derives the default
    from the vehicle weight: the weight rounded down to a whole 1000 lb, doubled,
    and divided by ten.

## Max force

Maximum contact force used by the wheel damage model.

## Max no-damage moment

Maximum contact moment the wheel can sustain without angular displacement or
damage.

## Moment displacement rate

Rate at which wheel angular displacement grows with contact moment above the
no-damage threshold.

## Max moment

Maximum contact moment used by the wheel damage model.

!!! tip "New in HVE 2027"
    The **Mesh** box of the **DyMESH Wheel** row (**View › Scene Display**, Vehicle
    group) draws the four-ring wheel contact body built
    from the tire's size and static loaded radius, deformed by the run, with the
    vertices the run crushed in red. It is available after a SIMON run with
    DyMESH enabled.

<!-- NAV -->

---

← Previous: [Wheels — Blow-out Page](WheelsDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Brake Page](WheelsDlg2.md) →

<!-- /NAV -->
