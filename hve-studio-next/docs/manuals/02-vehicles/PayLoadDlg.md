# Payload Dialog Box

**Payload Dialog**

The Payload dialog allows the user to add a payload to a vehicle. The payload may be any object adding inertia to a vehicle that is not accounted for in the vehicle's inertial properties. As in HVE, the payload belongs to the **event**: each vehicle in each event has its own.

Open it in the Event Editor (**Event (F5)**) with **Event › Payload...**. The menu item is enabled when the active event's method reads a payload: **SIMON**, **EDSMAC4**, **EDSVS**, **EDVDS** or **EDVTS**; for other methods it is grayed and an open Payload dialog closes. The **Vehicle** list at the top selects which of the event's vehicles is edited; a line under it names the event. If the event has no vehicles the dialog says so and shows no fields. While the event's results are on screen the fields are locked; reset the run to edit them.

All lengths, weights and inertias are shown in the units set in Preferences.

## Payload Exists
Check this box if the vehicle has a payload. When unchecked, all remaining fields are disabled and the payload is ignored.

## Location

### X, Y, Z
The X, Y and Z distances from the vehicle's center of gravity to the payload's center of gravity, in the SAE vehicle frame: +X forward, +Y right and **+Z down** (the field reads **Z down**), as in HVE. A load above the CG has a negative Z.

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

As in HVE, the start position you enter is where the loaded CG goes. So before a run, a vehicle with a payload (or with occupants under SIMON) is drawn with its body offset from that position by the CG shift, which is exactly where SIMON or EDVDS places it when the run starts. A trailer coupled behind it moves with its tow's hitch.

!!! note "HVE Studio"
    Results saved by a build before 2026-10-28 (SIMON) or 2026-10-29 (EDVDS) do not record the loaded CG. Such a vehicle is drawn displaced by the CG shift (a loaded trailer drawn forward of its king pin) until the event is run again.

!!! note "HVE Studio"
    Both **Mass** and **Weight** are editable (HVE's mass field is read-only). The dialog is offered for the methods whose program reads a payload (SIMON, EDSMAC4, EDSVS, EDVDS, EDVTS); HVE enables or disables individual fields according to the calculation method instead. There is no payload orientation: no engine reads one.

!!! tip "New in HVE Studio"
    The point-mass warning. A vehicle can also carry occupants and cargo into every event on its own **Aboard** list (**Inertia / Mass** dialog). In SIMON and EDVDS such a load can be handed over as payload, and is then combined with the payload entered here when the event runs; this dialog shows only the event's own payload. See [Aboard: occupants and cargo on the vehicle](../new-features/12-case-intake-and-vehicle-data.md#aboard-occupants-and-cargo-on-the-vehicle).

<!-- NAV -->

---

← Previous: [Moving CG](MoveCGDlg.md)  |  [Index](README.md)  |  Next: [Sprung Mass Dialog](SprungMassDlg.md) →

<!-- /NAV -->
