# Vehicle Inertia Dialog

**Inertia / Mass Dialog**

The inertial properties of the vehicle are displayed and edited in the **Inertia / Mass** dialog. Open it from the Vehicle Editor with the **Inertia / Mass...** button under **Vehicle Properties** (in the Vehicles panel, or in the Tools section of the [Vehicle Information dialog](VehicleInfoDlg.md)). The same weight and inertias, and the XZ product, can also be edited directly in the Vehicles panel under **Dimensions / Inertias › Inertia**.

The dialog displays two columns of values — **Total** (total vehicle) and **Sprung** (sprung mass only) — and keeps them consistent: editing a value in one column recalculates the other using the vehicle's unsprung (axle/wheel) masses and their locations. The unsprung masses come from the entered tire weights and, on an axle that is not independent, the axle beam; a line under the Mass rows shows the unsprung mass total and its front/rear split. All values are shown in the units set in Preferences.

This dialog contains the following parameters:

## Mass

### Weight (Total / Sprung)
Vehicle weight. Entering a Total weight updates the Sprung weight, and vice versa.

### Mass (Total / Sprung)
Vehicle mass (weight/g). In HVE 2027 the mass fields are editable as well; editing a mass updates the weight.

## CG Location

### CG to Front Axle / CG to Rear Axle / CG Height (Total / Sprung)
The longitudinal distances from the CG to the front and rear axles and the CG height, on each mass basis. The wheelbase does not depend on the basis, so editing one axle distance moves the other.

## Rotational Inertia

### Roll (Total / Sprung)
Rotational inertia about the X axis. The Sprung value is the value stored with the vehicle; the Total value includes the unsprung masses.

### Pitch (Total / Sprung)
Rotational inertia about the Y axis.

### Yaw (Total / Sprung)
Rotational inertia about the Z axis.

When a vehicle states no rotational inertia, HVE 2027 estimates it from the mass and the wheelbase and track, and a note under these rows names the estimated values. The solver uses the same estimate; type a measured value to replace it.

## Product of Inertia

### XZ Product (sprung)
Inertial product about the Y axis. This value represents the fact that the x-z plane is not a plane of symmetry for the vehicle sprung mass. It is edited on the sprung basis only.

## Aboard (occupants and cargo)

The people and loads this vehicle carries into every event and every engine.
The values above stay those of the **empty** vehicle; each run adds these to a
copy of the case as it starts, so the load is never counted twice. How each
engine receives the load is described in
[Aboard: occupants and cargo on the vehicle](../new-features/12-case-intake-and-vehicle-data.md#aboard-occupants-and-cargo-on-the-vehicle).
**Tools › Vehicle Package** can fill this list.

### Applied
- **Added to the vehicle (every engine)** — the vehicle's weight, CG and rotational inertia are combined with the load before any engine runs, the same way in every engine.
- **As payload in SIMON and EDVDS (the suspension sags)** — SIMON and EDVDS receive the load as the event's payload, combined with any payload the event states; every other engine gets it added to the vehicle, and the run status says so.

### On the centreline (ignore sideways offsets)
Counts each item's weight and its fore-and-aft and height position, but not its sideways offset, so that a lone driver does not pull the vehicle off a straight line.

### The list
One row per item, shown once there is one:

- **Name**.
- **Kind** — **Occupant** or **Cargo**. A label only: both count as a weight at a position.
- **Weight**.
- **x / y / z** — the item's position from the vehicle's CG (its sprung-mass CG): x forward, y right, **z up**.
- **Remove** — deletes the item.

**Add occupant** and **Add cargo** add a row (named *Occupant n* or *Cargo n*). Each item is a point mass. A line under the list gives the number of items and their weight, the **loaded** weight, and how far the CG moves (x, y and z, z up) when the load is added to the vehicle.

## OK / Cancel

**OK** closes the dialog, keeping the changes. **Cancel** discards every change made since the dialog was opened and closes it. Values take effect as they are typed, so there is no separate Apply button.

If the sprung mass comes out zero or negative (the total mass is less than the tire weights), the dialog says so in orange and the Total columns show the sprung values until it is corrected.

!!! warning "Not in HVE 2027"
    - **Basic... / Complex...**: both columns are always shown.
    - **Auto Update When Weight Changes**: inertias are not rescaled when the weight changes. A vehicle without stated inertias uses the estimate described above, which follows the mass.
    - Weight and mass are converted with standard gravity (9.80665 m/s²), not with the gravity set in the Environment Editor.

!!! tip "New in HVE 2027"
    The CG location rows (front axle, rear axle, height) on both bases, editable mass fields, the unsprung-mass read-out, and the **Aboard** list (HVE adds occupants and payloads per event only).

<!-- NAV -->

---

← Previous: [Getting Information about the Vehicle](VehicleInfoDlg.md)  |  [Index](README.md)  |  Next: [Saving Vehicles](VehSaveAs.md) →

<!-- /NAV -->
