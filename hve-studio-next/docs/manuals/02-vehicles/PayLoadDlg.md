# Payload Dialog Box

**Payload Dialog**

The Payload dialog allows the user to add a payload to a vehicle. The payload may be any object adding inertia to a vehicle that is not accounted for in the vehicle's inertial properties. As in HVE, the payload belongs to the **event**: each vehicle in each event has its own.

Open it in the Event Editor (**Event (F5)**) with **Event › Payload...**. The menu item is enabled when the active event's method reads a payload: **SIMON**, **EDSMAC4**, **EDSVS**, **EDVDS** or **EDVTS**; for other methods it is grayed and an open Payload dialog closes. The **Vehicle** list at the top selects which of the event's vehicles is edited; a line under it names the event. If the event has no vehicles the dialog says so and shows no fields. An edit made while the event's results are on screen marks them out of date.

All lengths, weights and inertias are shown in the units set in Preferences.

## Payload Exists
Check this box if the vehicle has a payload. When unchecked, all remaining fields are disabled and the payload is ignored.

## Location

### X, Y, Z
The heading reads **Location from the sprung CG**. The X, Y and Z distances from the vehicle's sprung-mass center of gravity with nothing aboard (the vehicle's own origin, which every vehicle position in HVE Studio is measured from) to the payload's center of gravity, in the SAE vehicle frame: +X forward, +Y right and **+Z down** (the field reads **Z down**), as in HVE. A load above the CG has a negative Z.

## Mass / Weight

### Mass
The mass of the payload. Editing the mass updates the weight.

### Weight
The weight of the payload. Editing the weight updates the mass, using the gravity set in the Environment Editor.

## Rotational Inertia

### Roll (Ixx), Pitch (Iyy), Yaw (Izz)
The roll, pitch and yaw moments of inertia of the payload about its own CG. An engine that models the payload adds them to the vehicle's own inertia, together with the parallel-axis term for the CG shift the payload causes. If a payload exists and all three are zero, a note warns that the load will act as a point mass.

## The Loaded CG
A payload moves the vehicle's center of gravity toward it, by the payload's share of the combined mass. Under SIMON and EDVDS the vehicle's path is the path of that loaded CG, and the wheels and suspension (and under SIMON the connections and the DyMESH collision mesh) are measured from it, as in HVE. EDVDS moves the CG forward, back, up and down only: a payload off the vehicle's centerline moves none of its geometry sideways (its equations assume the payload is on the centerline). The body, wheels and connection markers are drawn where they are on the vehicle, so they do not move relative to the vehicle when a payload is added: only the CG does. A loaded trailer stays on its tractor's fifth wheel.

!!! note "HVE Studio"
    **Adding a payload does not move the vehicle.** The start position you enter is the vehicle's own origin, its sprung-mass CG with nothing aboard, where the editor draws it. SIMON and EDVDS integrate the loaded CG, so HVE Studio starts that CG at the entered position plus the CG shift; the vehicle, its wheels and a trailer coupled behind it stay exactly where they were placed. The run status says so for each vehicle a load moves (*V1: its load moves the CG 0.152 m, not the vehicle*). In HVE the entered position is where the loaded CG goes, so adding cargo slid the whole vehicle back along itself by the shift. The same holds for occupants under SIMON.

    The **CG X, Y and Z**, velocity and acceleration channels of a SIMON or EDVDS run are reported at that same origin, the unloaded sprung CG, so they start at the position you entered. The engine's own loaded-CG point is the reference the report pages print. EDSMAC4, EDSVS and EDVTS already reported X and Y there, as in HVE; HVE Studio also reads their CG Z and their velocities and accelerations at that origin (they integrate a point offset from it, and with a payload their CG Z was the loaded CG's height).

    The **Total CG (static)** group of Variable Output (CG X, Y and Z, the velocities and the accelerations) gives the same motion at the vehicle's whole-mass CG as loaded for the event: sprung and unsprung masses, the payload, and under SIMON the occupants it adds, with the wheels at their static places, fixed in the body. It is there for a comparison that needs the total CG; the vehicle's position stays the sprung CG's. A run opened from a saved file does not carry this point, and the group reads as absent until the event is run again.

    After a run the report gains a **Reference Points** page, after the program's own pages: for each vehicle, where its origin (the sprung CG with nothing aboard) and its static total CG were at the start, at impact and at rest, in meters and feet, and which point the program's own tables are about (for SIMON and EDVDS with a load, the loaded CG, and how far it sits from the origin).

    An **accelerometer** stays where it is mounted. SIMON and EDVDS place their accelerometers from the loaded CG they integrate, and HVE hands them the coordinate as entered, so with a payload every accelerometer read the motion of a point the CG shift away from its mount. EDSMAC4 does the same by a smaller amount (about 1.5 cm in a typical case). HVE Studio hands each program the coordinate it needs, so the device reports its own mounting point.

!!! note "HVE Studio"
    Results saved by a build before 2026-10-28 (SIMON) or 2026-10-29 (EDVDS) do not record the loaded CG. Such a vehicle is drawn displaced by the CG shift (a loaded trailer drawn forward of its king pin) until the event is run again.

!!! note "HVE Studio"
    Both **Mass** and **Weight** are editable (HVE's mass field is read-only). The dialog is offered for the methods whose program reads a payload (SIMON, EDSMAC4, EDSVS, EDVDS, EDVTS, GBF); HVE enables or disables individual fields according to the calculation method instead. There is no payload orientation: no engine reads one.

!!! tip "New in HVE Studio"
    The point-mass warning. A vehicle can also carry occupants and cargo into every event on its own **Aboard** list (**Inertia / Mass** dialog). In SIMON and EDVDS such a load can be handed over as payload, and is then combined with the payload entered here when the event runs; this dialog shows only the event's own payload. See [Aboard: occupants and cargo on the vehicle](../new-features/12-case-intake-and-vehicle-data.md#aboard-occupants-and-cargo-on-the-vehicle).

<!-- NAV -->

---

← Previous: [Moving CG](MoveCGDlg.md)  |  [Index](README.md)  |  Next: [Sprung Mass Dialog](SprungMassDlg.md) →

<!-- /NAV -->
