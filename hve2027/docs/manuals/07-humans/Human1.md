# Human Contact Ellipsoids Dialog Box

Contact ellipsoids give each of the 15 segments of the HVE Human Model its
contact shape. Each segment may have up to 3 contact ellipsoids.

!!! note "HVE 2027"
    This is the **Ellipsoids** tab of the **Body Segments** window: in the Human
    editor (F2) open the **Occupants** panel (**Occupant › Human
    Information...**), select the human, press **Body Segments...**, choose the
    segment in the **Segment** list (or click it in the 3-D view) and open the
    **Ellipsoids** tab. Lengths follow the units set in Tools › Preferences.

## Ellipsoid

List of the selected segment's contact ellipsoids, by name. Select one to edit
it. HVE's *Current Ellipsoid*.

## Add

Adds an ellipsoid to the segment, named after the segment and its number (for
example "Head 2"). Disabled when the segment already has 3. Rename it in the
**Name** field.

!!! note "HVE 2027"
    HVE asks for the name first, in the
    [New Ellipsoid dialog](../08-environment/NewEllpDlg.md).

## Delete

Removes the selected ellipsoid. Disabled when the segment has only one; there
is no confirmation (use **Edit › Undo**, Ctrl+Z).

## Name

The ellipsoid's name.

## Center (segment frame) I / J / K

Coordinates of the center of the ellipsoid relative to the segment principal
axis system. HVE's *Coordinates i, j, k*.

## Semi-Axis Lengths I / J / K

The i, j and k semi-axis lengths of the ellipsoid.

## Principal Axes (deg) Roll / Pitch / Yaw

The roll, pitch and yaw angles of the ellipsoid axis system relative to the
segment axis system.

!!! note "Additional ellipsoids"
    As in HVE, GATB uses only each segment's **first** ellipsoid when it builds
    its contacts. A segment-to-segment contact pair that names a later
    ellipsoid is not tested; the run status reports how many armed pairs were
    lost this way.

!!! warning "Not in HVE 2027"
    **Material Name** and the **Material** button: an ellipsoid has no material
    of its own in HVE 2027, and the
    [Human Material Properties](HumMatProp.md) dialog does not exist. The
    occupant contact material is the combined occupant–surface material
    carried with each contact pair, imported from an HVE case.

<!-- NAV -->

---

← Previous: [Inertial Data Dialog Box](Human.md)  |  [Index](README.md)  |  Next: [Injury Tolerance Data Dialog Box](Human2.md) →

<!-- /NAV -->
