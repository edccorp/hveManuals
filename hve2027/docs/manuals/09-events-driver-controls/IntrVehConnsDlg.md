# Inter-Vehicle Connections Dialog

The connections between tow vehicles and trailers are displayed and edited in the
**Vehicle Connections** dialog. It is a vehicle property, not an event one: in
the Vehicle editor (F3) press **Connections...** in the Vehicles panel's
**Components** section.

The dialog is a table with a **Front** and a **Rear** column, one for each
connection, and the rows **Type**, **X**, **Y**, **Z**, **Height above ground**
and **Properties**. Values are shown in the units set in Preferences and take
effect as they are made (**Edit › Undo** takes one back); **Close** closes the
dialog. The dialog is locked while the vehicle is part of results on screen.

## Front Connection

**Type** (Front column)
The type of connection on the front of the vehicle. A **towed** unit (trailer or
dolly) connects here:

- None
- Hitch (trailer)
- King Pin (trailer)
- Pintle Eye, Fixed (trailer) — HVE's *Fixed Drawbar*
- Pintle Eye, Hinged (trailer) — HVE's *Hinged Drawbar*

**X / Y / Z**
The vehicle-fixed coordinates of the front connection. For a connection other
than None, the **Height above ground** row gives its height.

## Rear Connection

**Type** (Rear column)
The type of connection on the rear of the vehicle. A **towing** unit connects
here:

- None
- Ball (tow)
- 5th Wheel (tow)
- Pintle Hook (tow)

**X / Y / Z**
The vehicle-fixed coordinates of the rear connection, with its height above
ground.

The engines accept the matched pairs Ball–Hitch, 5th Wheel–King Pin and Pintle
Hook–Pintle Eye; the Calculation Method list in
[Event Information](EventInfo.md#calculation-method) checks the whole rig and
says what is wrong. The two mating connection heights must agree to within about
0.1 in unless an automatic adjustment is chosen in the method's calculation
options (EDSMAC4 *Inter-Vehicle Connection*).

!!! note "HVE 2027"
    HVE 2027 offers all eight types in both lists, labelled *(trailer)* or
    *(tow)*. Choose a front type for a towed unit and a rear type for a towing
    unit.

## Properties...

The connection properties belong to the **towing** end, so **Properties...**
in the Rear column opens **Connection Properties** for the vehicle's rear
connection (the Front column says *set on the towing end*). Its edits also take
effect as they are made and undo with **Edit › Undo**; it has a single
**Close** button:

- **Radius** — the moment arm at which the frictional torque acts at the
  connection (HVE's *Radius*).
- **Friction** — the friction coefficient at the connection.
- **Linear** — **Free Play**, **Stiffness**, **Damping**, **Breakaway Force**
  (0 = cannot fail).
- **Angular** — **Max Articulation** **Roll (deg)**, **Pitch (deg)** and
  **Yaw (deg)**, then **Stiffness**, **Damping** and **Breakaway Torque**
  (0 = cannot fail).

Hover a field for what reads it. Notably:

- **Max Articulation Yaw** is HVE's *Max Articulation Angle*, the jackknife
  limit read by EDSMAC4, EDVDS, SIMON and EDVTS; exceeding it ends an EDVDS run.
  The roll and pitch limits are stored but not read.
- The linear and angular **Stiffness** and **Damping** are read by SIMON only
  when the event's connection model is *Use tow vehicle properties*; otherwise
  the constraint is built from the two units' masses and these values are inert.

!!! note "HVE 2027"
    The free play, stiffness, damping, breakaway and roll/pitch fields are those
    of HVE's own Connection Properties dialog, which this help page did not
    describe. HVE 2027 groups them as HVE does.

<!-- NAV -->

---

← Previous: [Event Setup Menu](EventSetup.md)  |  [Index](README.md)  |  Next: [Position/Velocity Dialog Box](PosVelDlg.md) →

<!-- /NAV -->
