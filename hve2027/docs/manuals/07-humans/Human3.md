# Joint Data Dialog Box

The HVE Human Model has 14 joints. A segment may have up to 4 joints attached;
each joint's location is given in the coordinate system of each segment it
connects.

!!! note "HVE 2027"
    This is the **Joints** tab of the **Body Segments** window: in the Human
    editor (F2) open the **Occupants** panel (**Occupant › Human
    Information...**), select the human, press **Body Segments...**, choose the
    segment in the **Segment** list (or click it in the 3-D view) and open the
    **Joints** tab. Lengths follow the units set in Tools › Preferences.

The tab lists every joint attached to the selected segment, each under its own
heading (for example **Lumbar (Pelvis-Abdomen)**, **Rt Hip**, **Lt Elbow**),
instead of HVE's **Joint** drop-down list. A segment with no joints says so.

## I / J / K

The i, j and k coordinates of the joint relative to the selected segment's
principal axis system. HVE's *Coordinates i, j, k*.

## Joint Properties

The stiffness and damping of a joint are edited in the
[Joint Properties](HumJntPropDlg.md) window, opened with **Joint Properties...**
on the Occupants panel. HVE opens it with the **Properties** button here.

!!! note "HVE 2027"
    Coordinates are not range-checked when the window is closed; edits apply
    immediately and **Edit › Undo** (Ctrl+Z) takes one back.

<!-- NAV -->

---

← Previous: [Injury Tolerance Data Dialog Box](Human2.md)  |  [Index](README.md)  |  Next: [Human Information Dialog](HumanInfoDlg.md) →

<!-- /NAV -->
