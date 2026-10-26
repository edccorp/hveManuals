# Position/Velocity Dialog Box

HVE's Position/Velocity dialog assigned positions and velocities to each human
and vehicle at up to eight named path locations. In HVE Studio that information is
split between a small **Position / Velocity** dialog for the starting state, the
initial-conditions section of the [Event Information](EventInfo.md) panel, and
the **Named Positions** list in the same section.

## The Position / Velocity dialog

Open it from **Event › Position / Velocity...**. It is enabled for every method
except EDCRASH and READDATAFILE.

![Position / Velocity dialog](images/hvn-pos-velocity.png)

The vehicle header at the top picks which of the event's vehicles to edit. The
dialog edits the same values as the event's **Vehicle Initial Conditions**
section, so a change in either place shows in both:

- **Initial Position** — **X**, **Y** (units set in Preferences) and
  **Heading (deg)**.
- **Initial Velocity** — **Speed** (units set in Preferences).

Everything else about the starting state — Z height, sideslip, yaw rate, roll,
pitch and their rates, Auto Position — is entered in the
[Event Information](EventInfo.md#vehicle-initial-conditions) panel. Vehicles can
also be placed with the viewport gizmo (G move, R rotate).

!!! note "HVE Studio"
    The starting velocity is entered as a **Speed** plus a **Sideslip β** angle
    (Event Information), not as Total / U / V components. There is no
    *Velocity is Assigned* check box and no **Apply** button: edits take effect
    immediately.

## Path locations

HVE's Path Location list is kept as the **Named Positions** list in each
vehicle's block of the [Event Information](EventInfo.md#named-positions) panel
(also on the Event Designer's Positions stage): one collapsible node per named
position, each with a **Set** check box, **X**, **Y**, **Heading (deg)**, **Auto
Position (on the ground)** with **Z Height**, **Roll (deg)** and **Pitch
(deg)**, and a *Read by* note saying what reads it under the event's
calculation method. Each position that is set is outlined in the viewport (View
› Scene Display › Scene Ghosts) and can be dragged there. What EDCRASH does
with each:

- **Initial** and **Begin Perception** — drawn only; they do not change a
  result.
- **Begin Braking** — EDCRASH back-calculates the speed at Begin Braking from
  this position and the pre-impact drag (Driver Controls › Wheel Data,
  *Total Lock-up*).
- **Impact** and **Final/Rest** — the scene the impact speeds are solved from.
  They are set together (ticking either sets both); without them the run is a
  damage-only reconstruction. **Impact sideslip (deg)** and **Velocity at
  rest** are entered below the list when they are set.
- **Separation** — the position where the vehicles separated (the separation
  velocity). Unset, EDCRASH assumes they separated where they met.
- **Point On Curve** — makes the post-impact path an arc through this point
  instead of a straight chord (see the *Curved Path* options in
  [Calculation Options for EDCRASH](../10-calculation-options/CalcOptEDCRASHDlg.md)).
- **End of Rotation** — ends the spinout at this position and treats the rest of
  the path to rest as a separate rollout.

EDSMAC4 reads **Final/Rest**; unset, it defaults a rest position and says so.
For every simulation method, EDGEN included (its path comes from the Path
Follower waypoints), the other named positions are drawn only, to compare with
the run. A simulation's **Initial** is the start of the run: the same values as
the Initial Position fields and the event's initial conditions, so editing one
edits the other.

Each position also has HVE's Z, roll and pitch, entered with **Auto Position (on
the ground)** off. Except at a simulation's Initial they are drawn only (they
place the outline). No velocity is offered for these positions except EDCRASH's
velocity at rest.

!!! warning "Not in HVE Studio"
    - Editing a **human's** positions and velocities, except for EDGEN: on an
      EDGEN event the human's eight named positions (position, orientation,
      sideslip and speed) are edited in Event Information, *Humans in Event*.

<!-- NAV -->

---

← Previous: [Inter-Vehicle Connections Dialog](IntrVehConnsDlg.md)  |  [Index](README.md)  |  Next: [Simulation Controls Dialog Box](SimuCtrlDlg.md) →

<!-- /NAV -->
