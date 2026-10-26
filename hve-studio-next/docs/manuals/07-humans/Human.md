# Inertial Data Dialog Box

Inertial parameters of the HVE Human Model are defined for each of the 15
segments: Pelvis, Abdomen, Chest, Neck, Head, Rt/Lt Upper Leg, Rt/Lt Lower Leg,
Rt/Lt Foot, Rt/Lt Upper Arm and Rt/Lt Lower Arm.

!!! note "HVE Studio"
    In the Human editor (F2), open the **Humans** panel (**Occupant › Human
    Information...**), select the human and press **Body Segments...**. The
    **Body Segments** window shows the human's name, a **Segment** list and
    three tabs: **Inertia** (this page), **Ellipsoids**
    ([Contact Ellipsoids](Human1.md)) and **Joints** ([Joint Data](Human3.md)).
    Click a body part in the 3-D view to select that segment in the list.
    Values follow the units set in Tools › Preferences. While a solved run is on
    screen the window is read-only.

## Body model

A human needs a body model before its segments can be edited. When it has none,
the window offers **Seed GEBOD Body** (build the body from the occupant's
subject type, age and percentiles with the GEBOD regression, as HVE does) and
**Seed Standard Body** (a simple body scaled to the occupant's mass). Once a body
exists, **Re-seed GEBOD** and **Re-seed from occupant mass** rebuild it,
replacing any edits.

## Segment

The segment being edited. HVE selects it by clicking the segment's CG and
choosing Inertias from the popup.

## Segment Color

The color the segment is drawn in — HVE's **Color...** item of the segment
popup — with **Apply to all segments** to give the whole body that color.
Display only. The color stored in an HVE case is imported.

!!! tip "New in HVE Studio"
    A segment can also wear a node material (View › Shader Editor); it is then
    drawn in that material instead of this color.

## Segment Weight

Weight of the selected segment. As the weight changes, the segment mass is
recalculated by dividing the weight by the acceleration of gravity of the
current environment (Environment › Environment..., Physical).

## Segment Mass

Segment mass: weight divided by gravity. Display only.

## Inertia Roll / Pitch / Yaw

Rotational inertia of the segment about its i (roll), j (pitch) and k (yaw)
axes.

## Total Body Weight

Total weight of the whole human — the sum of the 15 segment masses times
gravity — with the total mass beside it. Display only.

!!! note "HVE Studio"
    Values are not range-checked when the window is closed; there is no OK
    button. Edits apply immediately and **Edit › Undo** (Ctrl+Z) takes one back.

<!-- NAV -->

---

← Previous: [Humans](README.md)  |  [Index](README.md)  |  Next: [Human Contact Ellipsoids Dialog Box](Human1.md) →

<!-- /NAV -->
