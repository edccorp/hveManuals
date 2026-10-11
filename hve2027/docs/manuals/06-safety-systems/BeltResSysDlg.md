# Belt Restraint System Dialog Box

In HVE the Belt Restraint System dialog places installed torso and lap belts in
use for an occupant in the event and sets where each belt end attaches to the
body and how much slack it has. The belt hardware (anchors and webbing) is
installed in the vehicle editor's Belt Restraints dialog.

!!! note "HVE 2027"
    Open the **Belt Restraint System** window from **Vehicle › Belt
    Restraint...** in the Vehicle editor (F3), or **Event › Restraints... › Belt
    Restraint...** in the Event editor (F5; available for the dynamic
    calculation methods). HVE 2027 puts HVE's vehicle-side belt hardware and
    event-side belt use in this one window. The belt geometry is stored with the
    vehicle, one set per occupant, so it applies to every event the vehicle
    appears in; the window warns when the vehicle shown is not in the active
    event. What the occupant wears is stated per event. Lengths, stiffness,
    damping and force follow the units set in Tools › Preferences. While a
    solved run is on screen the window is read-only.

![Belt Restraint System window](images/hvn-belt-restraint-system.png)

Each belt section is modelled as two belt segments (left and right). One end of
each is attached to a body segment; the other end is attached to an anchor
point on the vehicle.

## Occupant

HVE's *Belt Restraints For*. The list names each occupant of the vehicle by seat
and name. Occupants who ride in this vehicle in the active event come first;
below a separator are pedestrians, humans not in the event and humans in
another vehicle. Selecting an occupant also selects them in the Occupants panel.

## Restraint In Use

What the selected occupant wears **in the active event**: **None**, **Lap Belt**,
**3-Point Belt** or **Airbag + Belt**. This is what places the belts (and the
airbag) in use for the run: a lap belt is used for any choice but None, the
torso belt for 3-Point Belt and Airbag + Belt, and the airbag only for
Airbag + Belt — each only if it is installed below. The event's name is shown
beside the list. If the occupant is not in the active event the list is
replaced by a note; add the occupant in Event Information first.

!!! note "HVE 2027"
    This replaces HVE's per-belt **Device In Use** check boxes.

## Configuration

**Torso Belt Installed** / **Lap Belt Installed** — whether each belt section is
fitted at this occupant's seat.

## Belt Section

Choose **Torso (shoulder)** or **Lap**; the anchor, slack and webbing fields
below then apply to that section. HVE's *Belt Segment* list. The torso belt
attaches to the chest and the lap belt to the pelvis.

## Left Anchor / Right Anchor

For the left and right belt segments:

- **Slack L** / **Slack R** — the displacement allowed between the ends of the
  belt before it carries tension (a negative value implies pre-load).
- **I**, **J**, **K** — the belt attachment point on the body segment, in the
  segment's coordinate system. HVE's *Segment Coordinates*.

## Vehicle Anchor

**Veh I L**, **Veh J L**, **Veh K L**, **Veh I R**, **Veh J R**, **Veh K R** —
the vehicle end of the left and right webbing, relative to the vehicle CG
(HVE's anchor locations from the vehicle Belt Restraints dialog).

## Properties

The webbing force law of the selected section: **Stiffness**, **Damping** and
**Break Strength**.

!!! note "HVE 2027"
    EDHIS reads these. GATB does not: it uses ATB's own fixed webbing curve, as
    HVE's GATB does, so changing them leaves a GATB result unchanged. The window
    says so above the fields.

!!! warning "Not in HVE 2027"
    - **Belt Attached To** (Pelvis, Abdomen, Chest, Neck, Head): the torso belt
      always attaches to the chest and the lap belt to the pelvis. The window's
      **Segment** list (Shoulder, Chest, Lap) is stored but not used.
    - **Restraint Force** (Vehicle Frame, Ground Frame) is stored but not used.

<!-- NAV -->

---

← Previous: [Airbag Restraint System Dialog Box](AirBagSysDlg.md)  |  [Index](README.md)

<!-- /NAV -->
