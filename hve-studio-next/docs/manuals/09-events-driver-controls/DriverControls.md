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
rows in time order, the first and last values held beyond the ends. It is also a
curve editor, like Blender's Graph Editor: each row is a **key** on the curve.

- **Click** a key to select it; **Shift+click** adds it to or removes it from
  the selection. Selected keys are orange, and their rows are highlighted in
  the table (selecting rows in the table selects the keys).
- **Drag** a selected key to move every selected key in time and value. While
  dragging, **X** locks the move to time and **Y** to the value (press again to
  free it); hold **Ctrl** to snap the time to 0.01 s and the value to a round
  step. A value stays inside the column's allowed range. When you let go the
  rows are put in time order.
- **Drag on empty space** to select the keys inside a box (**Shift** adds to
  the selection).
- **Double-click empty space** to add a key there.
- **Delete** or **X** removes the selected keys (the last row stays).
- **Mouse wheel** zooms the time axis about the pointer, **Ctrl+wheel** zooms
  the value axis, a **middle-button drag** pans, and **Home** or **Fit** shows
  every key again.
- Faint lines mark the column's usual range. Hover a key to read its time and
  value.

Each row is a number (**#**), a **Time (s)** and a value. Click a cell to
type a value; drag to change it. **Add** appends a row at the table's own time
step after the last (half a second for a first step); **X** at the end of a row
deletes that row (the last remaining row cannot be deleted); **Sort by Time**
puts the rows in time order. A per-wheel table (one column per wheel, headed
*A1-R*, *A1-L*, ...) has its own **Add** and **Discard per-wheel table**
buttons. Side **R** is the right wheel.

The tables edit like a spreadsheet:

- **Paste** — copy the rows from a spreadsheet, a report (a CDR report's
  pre-crash table, for example) or a text file, and either press Ctrl+V while
  typing in a cell, which fills the table from that cell down and across, or
  click **Paste**, which replaces the whole table, first column first. Columns
  may be separated by tabs, commas, semicolons or spaces; a line with no number
  (a heading) is skipped, and a unit after a number (`30 deg`) is ignored. Rows
  are added as needed. Values are read in the units the columns show.
- **Tab** out of the last cell adds a row and moves into it, so a table can be
  typed row after row without the mouse.
- **Select rows** on their numbers: click one, Shift+click for a range,
  Ctrl+click to add one, or drag down the numbers. **Delete selected** or the
  Delete key removes them together.
- **Limits** — each value column has HVE's two ranges (Output Settings ›
  Limits). A value outside the **usual** range (a pedal force over 400 lb, a
  steering-wheel angle past ±900°) is accepted with a note under the table
  asking you to check it. A value outside the **allowed** range (0 to 1 for a
  throttle or brake fraction, over 1000 lb of pedal force, past ±3600° of
  steering-wheel angle) is not accepted: the cell keeps its value and the note
  says why. A pasted block with any such value is not pasted at all, and the
  note names the first one. Dragging stops at the allowed range's ends. Times
  have no limit. Right-click a value cell for **Edit limits...**.

!!! warning "Not in HVE Studio"
    HVE's **Copy Cell** and **Copy Row** buttons.

## Steer

Applies steer angles that attempt to steer the vehicle.

**Steering-wheel table** — *Time (s) → Angle (deg)*: steering-wheel angle, +right
(clockwise) / −left. HVE's ranges apply: usual ±900°, allowed ±3600°. The engine divides it by each
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
