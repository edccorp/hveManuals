# Vehicle Inertia Dialog

**Inertia / Mass Dialog**

The inertial properties of the vehicle are displayed and edited in the **Inertia / Mass** dialog. Open it from the Vehicle Editor with the **Edit...** button in the Vehicles panel's **Inertia** section, which itself shows the total weight and the yaw, pitch and roll inertias on one line.

The dialog displays two columns of values — **Total** (total vehicle) and **Sprung** (sprung mass only) — and keeps them consistent: editing a value in one column recalculates the other using the vehicle's unsprung (axle/wheel) masses and their locations. The unsprung masses come from the entered tire weights and, on an axle that is not independent, the axle beam; a line under the Mass rows shows the unsprung mass total and its front/rear split. All values are shown in the units set in Preferences.

This dialog contains the following parameters:

## Mass

### Weight (Total / Sprung)
Vehicle weight. Entering a Total weight updates the Sprung weight, and vice versa.

### Mass (Total / Sprung)
Vehicle mass (weight/g). In HVE Studio the mass fields are editable as well; editing a mass updates the weight.

## CG Location

### CG to Front Axle / CG to Rear Axle / CG Height (Total / Sprung)
The longitudinal distances from the CG to the front and rear axles and the CG height, on each mass basis. Editing one **moves the CG within the vehicle**, exactly as [Move CG](MoveCGDlg.md) does: the body, wheels and equipment stay where they are, the wheelbase is unchanged and the other axle distance follows. The **Sprung** column moves the sprung-mass CG by the change typed. The **Total** column is where the sprung mass and the wheels, tires and axles together balance; since those unsprung masses stay with the body, moving the total CG by a distance moves the sprung CG by that distance times total mass over sprung mass. A move that would put the CG at or below the ground, or at or past an axle, is refused and the reason is shown under the rows.

The total CG is computed from every wheel's own position (including per-wheel positions and every axle of a tandem) and its tire, wheel and axle-beam weight. Changing an unsprung weight (tire weight, dual tires, a solid axle's beam mass) leaves the sprung CG where it is and the total weight unchanged; the sprung weight and the total CG move.

## Rotational Inertia

### Roll (Total / Sprung)
Rotational inertia about the X axis. The Sprung value is the value stored with the vehicle; the Total value includes the unsprung masses.

### Pitch (Total / Sprung)
Rotational inertia about the Y axis.

### Yaw (Total / Sprung)
Rotational inertia about the Z axis.

When a vehicle states no rotational inertia, HVE Studio estimates it from the mass and the wheelbase and track, and a note under these rows names the estimated values. The solver uses the same estimate; type a measured value to replace it.

## Product of Inertia

### XZ Product (sprung)
Inertial product about the Y axis. This value represents the fact that the x-z plane is not a plane of symmetry for the vehicle sprung mass. It is edited on the sprung basis only.

## Aboard (occupants and cargo)

The people and loads this vehicle carries into every event and every engine.
The values above stay those of the **empty** vehicle; each run adds these to a
copy of the case as it starts, so the load is never counted twice. How each
engine receives the load is described in
[Aboard: occupants and cargo on the vehicle](../new-features/12-case-intake-and-vehicle-data.md#aboard-occupants-and-cargo-on-the-vehicle).
**Tools › Automatic Tools › Vehicle Package** can fill this list.

### Applied
- **Added to the vehicle (every engine)** — the vehicle's weight, CG and rotational inertia are combined with the load before any engine runs, the same way in every engine.
- **As payload in SIMON and EDVDS (the suspension sags)** — SIMON and EDVDS receive the load as the event's payload, combined with any payload the event states; every other engine gets it added to the vehicle, and the run status says so.

### On the centerline (ignore sideways offsets)
Counts each item's weight and its fore-and-aft and height position, but not its sideways offset, so that a lone driver does not pull the vehicle off a straight line.

### The list
One row per item, shown once there is one:

- **Name**.
- **Kind** — **Occupant** or **Cargo**. A label only: both count as a weight at a position.
- **Human** — for an occupant, a human from the **Human** editor, or **(none)** for a plain weight. See [A human in the seat](#a-human-in-the-seat) below.
- **Seat** — for a linked human only: their seat location (Front Left (driver) … Back Left).
- **Weight**.
- **x / y / z** — the item's position from the vehicle's CG (its sprung-mass CG): x forward, y right, **z up**.
- **Remove** — deletes the item.

**Add occupant** and **Add cargo** add a row (named *Occupant n* or *Cargo n*). Each item is a point mass. A line under the list gives the number of items and their weight, the **loaded** weight, and how far the CG moves (x, y and z, z down) when the load is added to the vehicle.

When the load is added to the vehicle and the CG moves, everything the case measures from that CG moves with it for the run: each event's payload for this vehicle, and the seat (and pose) of every occupant it carries, so an occupant stays in the seat.

### A human in the seat

Pick a human in an occupant row's **Human** column and the row becomes that person, seated in this vehicle:

- **Weight** is the human's own and cannot be typed while linked: the sum of their body's segment masses, or their stated weight when the body has not been built (it then counts as a point at the seat). The weight is added at the seated body's own center of mass, which is ahead of and above the seat.
- **Seat** and **x / y / z** are the human's own seat location and seat position (where the pelvis sits). Editing them here edits the human, so the belts and airbag of that seat apply to them and every event that does not state its own seating puts them there. When you link a human who was not already in this vehicle, they take the row's position.
- The human is **drawn seated in the vehicle**: in the Vehicle editor and in every event that shows the vehicle, riding with it through a run. An event that lists the human draws them itself instead, once.

What each program does with the row:

- **SIMON, EDSMAC4, EDSMAC, EDCRASH, EDVSM, EDVDS, EDSVS, EDVTS** and the other vehicle programs add the human's weight at their seat, exactly as a plain item of that weight at that place, by the **Applied** setting above.
- **SIMON** adds an occupant's weight itself when the **event** lists that human (Event › Humans in Event). In such an event the row adds nothing, so the person is counted once.
- **EDHIS** and **GATB** seat the human in this vehicle by default and add **no** weight to the vehicle: they solve the occupant, and their vehicle carries no occupant mass.
- An event that seats the human in another vehicle (or as a pedestrian) wins: the row adds nothing in that event. A human whose own seat is in another vehicle (linked there too) adds nothing here; the row says so in orange, with a **Seat here** button.

Every run says, per linked row, which of these happened. Removing the human from the case leaves the row as a plain occupant at the last weight and position.

## Close

Values take effect as they are typed, so the dialog has a single **Close** button. To take a change back, use **Edit › Undo** (Ctrl+Z); each edited field is one undo step.

If the sprung mass comes out zero or negative (the total mass is less than the tire weights), the dialog says so in orange and the Total columns show the sprung values until it is corrected.

**Auto Update Inertia When Weight Changes** (a checkbox under **Rotational Inertia**, off by default and kept as your own setting, not the vehicle's, as in HVE): a typed weight or mass, total or sprung, here or in **Size & Weight**, multiplies the **total** roll, pitch and yaw inertias by the new total mass over the old one; the sprung values follow by the parallel axis theorem and the XZ product is kept. An axis with nothing stated uses the estimate, which follows the mass anyway.

!!! warning "Not in HVE Studio"
    - **Basic... / Complex...**: both columns are always shown.
    - Weight and mass are converted with standard gravity (9.80665 m/s²), not with the gravity set in the Environment Editor.

!!! tip "New in HVE Studio"
    The CG location rows (front axle, rear axle, height) on both bases, editable mass fields, the unsprung-mass read-out, and the **Aboard** list (HVE adds occupants and payloads per event only).

<!-- NAV -->

---

← Previous: [Getting Information about the Vehicle](VehicleInfoDlg.md)  |  [Index](README.md)  |  Next: [Saving Vehicles](VehSaveAs.md) →

<!-- /NAV -->
