# Selected Humans & Vehicles Dialog Box

In HVE this modeless dialog shows the humans and vehicles selected for the
current event as a tree — tow vehicles with their trailers, vehicles with their
occupants, and independent humans such as pedestrians — and clicking an entry
makes it the current object of the event.

!!! note "HVE 2027"
    HVE 2027 has no separate dialog. The event's humans and vehicles are listed,
    and assigned, in the **Event Information** panel of the Event editor (F5;
    **Event › Event Information...**), in its **Vehicles in Event** and **Humans
    in Event** sections.

## Vehicles in Event

One row per vehicle slot (V1, V2, …). **Add Vehicle** adds a vehicle of the case
to the event, up to the number the calculation method accepts; the panel says
when the event has too few vehicles to run. Removing a vehicle asks for
confirmation, because it discards that slot's inputs (initial position and
speed, measured crush, tire blowout, wheel damage, tire terrain); to run a
different vehicle with the same inputs, change the slot's vehicle instead.

## Humans in Event

Shown for the occupant calculation methods (and for SIMON, where occupants are
bookkeeping only — SIMON does not solve occupant biomechanics). One row per human
slot (H1, H2, …):

- the **human** list — a human already in another slot is greyed;
  pedestrians are marked. "no body" warns that the human has no body model yet.
- **Remove** and **Pose** (opens the human's
  [Body Pose](HumanInfoDlg.md#body-pose) window for this event).
- **Occupies** — the vehicle the human rides in during this event, or
  **Pedestrian (no vehicle)**.
- the human's position: **Seat X / Y from CG** for an occupant, or the scene or
  vehicle-relative position for a pedestrian, depending on the method.
- **Restraint (this event)** — None, Lap Belt, 3-Point Belt or Airbag + Belt
  (see [Belt Restraint System](../06-safety-systems/BeltResSysDlg.md)).

**Add Human** adds a human of the case to the event.

## Selecting the current object

Selecting a vehicle — in the viewport or in the **Vehicle** list at the top
of the event dialogs — makes it the current vehicle for the event
dialogs. In the Event editor, clicking a human's body in the viewport selects
that human.

!!! warning "Not in HVE 2027"
    The tree view of tow vehicles, trailers and occupants.

<!-- NAV -->

---

← Previous: [Human Material Properties Dialog Box](HumMatProp.md)  |  [Index](README.md)

<!-- /NAV -->
