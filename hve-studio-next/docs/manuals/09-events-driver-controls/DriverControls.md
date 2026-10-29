# Driver Controls

The **Driver Controls** dialog holds the time tables that describe how the
driver attempted to control the vehicle: steering, braking, throttle and gear
selection. Open it from **Event › Driver Controls...** in the Event editor
(F5). It is enabled for the simulation methods and for EDCRASH.

![Driver Controls dialog for a SIMON event](images/hvn-driver-controls.png)

The vehicle header at the top picks which of the active event's vehicles to
edit; it offers only vehicles in the event. As in HVE, driver controls are
stored **per event per vehicle**, and the dialog says which event's tables are
being edited. The tables are locked while that event's results are on screen.

The tabs depend on the method:

- **EDCRASH** — a single **Wheel Data** tab. See
  [Driver Controls Wheel Data](DriverControls2.md).
- **Every other method** — **Throttle**, **Brake**, **Steer** and **Gear**
  tabs ([Throttle](DriverControls4.md), [Brake](DriverControls3.md),
  [Gear](DriverControls5.md); Steer is below).
- For a method that does not read driver tables (EDHIS, GATB) a note at
  the top says so.
- For SINGLETRACK the Gear tab is not shown. The **Throttle** tab is shown only when the event's
  **Dynamics model** is **Nonlinear**, which reads the throttle as a fraction of the rear tire's grip
  (see [Driver Controls Throttle](DriverControls4.md)); the Whipple model holds its speed and reads the
  Brake and Steer tables only.

!!! note "HVE Studio"
    The HVE Driver (path follower) is the **Path Follower** tab of this dialog,
    as in HVE; **Event › Path Follower...** opens Driver Controls on it. For EDGEN,
    which has no driver tables but walks the path's waypoints, it is the only tab.
    See [Driver Controls Path Follower](DriverControls7.md).

### Editing a table

A graph above each table draws it as the engines read it: straight lines between
rows in time order, the first and last values held beyond the ends. Hover a point
to read its time and value.

Each row is a **Time (s)** and a value. Double-click or Ctrl+click a cell to
type a value; drag to change it. **Add** appends a row half a second after the
last; **X** at the end of a row deletes that row (the last remaining row cannot
be deleted); **Sort by Time** puts the rows in time order. A per-wheel table
(one column per wheel, headed *A1-R*, *A1-L*, ...) has its own **Add** and
**Discard per-wheel table** buttons. Side **R** is the right wheel.

!!! warning "Not in HVE Studio"
    HVE's **Copy Cell** and **Copy Row** buttons.

## Steer

Applies steer angles that attempt to steer the vehicle.

**Steering-wheel table** — *Time (s) → Angle (deg)*: steering-wheel angle, +right
(clockwise) / −left, from −1800 to +1800 degrees (five turns each way; HVE states no limit). The engine divides it by each
axle's steering gear ratio to get the nominal road-wheel angle. This is HVE's
*At Steering Wheel* table.

**At the tires** — when the case carries an HVE *At Axle* table (one column per
wheel), it is shown above the steering-wheel table with a note that it
**overrides** it. These are road-wheel angles: the steering gear ratio and
Ackermann geometry are bypassed, and a non-steerable axle's entries are ignored
by the engines. **Discard per-wheel table** returns to the steering-wheel table.

!!! warning "Not in HVE Studio"
    - A new *At Axle* (at the tires) steer table cannot be created in the
      dialog; it comes from an imported HVE case.
    - The **Use Ackermann Steering** check box.

!!! note "HVE Studio"
    For a **motorcycle** -- a SINGLETRACK event, or a SIMON event with a
    Motorcycle in it -- the steer table is not a steering angle. **Table means**
    on the Steer tab (the same option as in Method Options) says what it is: the
    **steer torque** at the bars (N·m), or the **commanded lean** (deg, + =
    leaning right) that the rider countersteers into and holds, so the machine
    leans and turns. It is the motorcycle's one rider table: a case saved before
    this version with a separate **Lean** table has it moved into the SIMON
    event's steer table, read as a commanded lean, when it is opened. In SIMON the
    rider reads it while the single-track model carries the machine; SIMON itself
    never reads it as a steering angle, and after a hand-back it steers straight
    ahead (the run status says so).

## Lights

!!! note "HVE Studio"
    HVE's **Lights** page is a window of its own, **Event › Lights...**,
    enabled for SIMON and EDSMAC4, the methods that switch a vehicle's lamps.
    For each lamp the vehicle's body file defines it sets **Is Active** and the
    activation — **Use Driver Controls** or a **User-Entered** table of **Turn
    On (sec)** / **Turn Off (sec)** times — with **On/Off Cycle Time (sec)**
    and **Min Steer Angle (deg)** where they apply. The lamps themselves are
    defined in **Vehicle › Editors › Vehicle Lights...**.

<!-- NAV -->

---

← Previous: [Contacts Dialog Box](ContactsDlg.md)  |  [Index](README.md)  |  Next: [Driver Controls Path Follower Method](DriverControls1.md) →

<!-- /NAV -->
