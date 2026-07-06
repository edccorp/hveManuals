# Belt Restraint System Dialog Box

The Belt Restraint System dialog (title: *Belt Restraint System Data: [vehicle name]*) is used in event mode to assign belt restraints to occupants. The belt hardware (torso and lap belt sections, anchor locations, webbing properties) must first be installed on the vehicle using the vehicle editor's Belt Restraints dialog; a belt segment can only be placed in use here if it is installed at the selected location. All controls are disabled unless at least one human in the event has an Initial Position human kit.

Each belt section is modeled as two belt segments (left and right). One end of each segment is attached to the human body segment selected below; the other end is attached to the anchor point on the vehicle.

## Belt Restraints For

A drop-down list used to select the occupant (and seat location) receiving the belt restraint. Each occupied position is listed by the human's name followed by an abbreviated seat position label — (F/R), (F/C), (F/L), (B/R), (B/C), (B/L), (R/R), (R/C), (R/L) — for the nine possible occupant locations. Unoccupied positions are not listed. A position can only be selected if the human at that position has an Initial Position human kit placed in the event; otherwise an error message is displayed and the previous selection is restored.

(Note: earlier versions of this help listed "Torso Belt Restraint, Lap Belt Restraint, Airbag Restraint" as the choices for this list. That is no longer correct — the belt type is now chosen with the Belt Segment list below, and airbags are assigned using the separate Airbag Restraint System dialog.)

## Belt Segment

A drop-down list used to select which belt section is being edited. The choices are:

- Torso Belt
- Lap Belt

## Device In Use

A checkbox indicating whether the selected belt segment is in use for this event. Default: not in use. The checkbox is enabled only if the corresponding belt section (torso or lap) is installed at the selected location on the vehicle. When unchecked, the attachment and slack fields are disabled.

## Belt Attached To

A drop-down list used to select the human body segment to which the ends of the belt segments are attached (the other ends attach to the anchor points on the vehicle). The choices are the five torso segments:

- Pelvis
- Abdomen
- Chest
- Neck
- Head

## Segment Coordinates (in) - i, j, k (Left and Right columns)

Enter the i, j and k coordinates of the belt attachment point on the selected body segment, for the left and right belt endpoints, in the human segment's coordinate system. Defaults: 0, 0, 0. Typical range ±20 in for each coordinate; allowed range ±100 in.

## Belt Slack (in) (Left and Right columns)

The amount of displacement between the ends of the belt allowed before creating belt tension, entered separately for the left and right belt segments (a negative value implies pre-load). Default: 0 in. Typical range -2.0 to 10.0 in; allowed range -4.0 to 100.0 in.

---
*Source topic: BeltResSysDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Airbag Restraint System Dialog Box](AirBagSysDlg.md)  |  [Index](README.md)

<!-- /NAV -->
