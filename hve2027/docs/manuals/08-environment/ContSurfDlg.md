# Contact Surfaces Dialog

A vehicle may include contact surfaces, used for simulating the interaction
forces between the vehicle and its occupants (interior surfaces) or pedestrians
(exterior surfaces). Each surface is a plane panel defined by three corners; the
fourth is assigned by assuming a parallelogram.

!!! note "HVE 2027"
    In the Vehicle editor (F3) choose **Vehicle › Contact Surfaces...**. The
    **Contact Surfaces** window lists the vehicle's surfaces on the left and
    edits the selected one on the right. While it is open the panels are drawn
    in the 3-D view — in the Vehicle editor, and in the Event editor where they
    ride with the vehicle to its event position — with an arrow showing each
    panel's normal; click a panel there to select it. Lengths follow the units
    set in Tools › Preferences. While a solved run is on screen the window is
    read-only.

![Contact Surfaces window](images/hvn-contact-surfaces.png)

## Surface list

Select a surface to edit it. Ctrl+click adds or removes a surface from a
multiple selection and Shift+click selects a range, for **Delete**. HVE's
*Contact Surface* list.

## Name

The surface's name.

## Material

The name of the material assigned to the surface. Its properties are in the
**Material Properties** section (see [Material Properties](MatPropDlg.md)).

## Classification

**Class** — **Vertex**, **Face** or **Group**: HVE's *Bind Material To*. Stored
with the surface; no physics program reads it (EDHIS treats every surface as a
plane).

**Side** — **Interior** (occupant simulation) or **Exterior** (pedestrian
simulation). HVE's *Location*.

## Geometry

The panel is edited as a **Centre** (X, Y, Z), a **Size** (**Width**,
**Height**) and **Angles** (**Yaw**, **Pitch**, **Roll** in degrees, applied
yaw, then pitch, then roll), relative to the vehicle CG. A panel whose edges are
not perpendicular is flagged as skewed; editing it in this form squares it up.

Check **Edit corner points instead** to enter the stored form, HVE's three
corners: **P2 (corner)**, **P3 (+width)** and **P1 (+height)**, each X, Y, Z in
the vehicle-fixed frame (x forward, y right, z down). This keeps a skewed panel
skewed.

**Normal** shows the panel's normal in that frame; **Flip** reverses it. A panel
whose edges are collinear is reported as degenerate (no normal and no area).

## Material Properties

The force–deflection law and friction of the surface; see
[Material Properties](MatPropDlg.md).

## Buttons

**Add** — Adds a surface ("Surface 1", "Surface 2", …) with the default
material.

**Delete** — Deletes the selected surface, or all the selected surfaces
("Delete (3)"). There is no confirmation; **Edit › Undo** (Ctrl+Z) takes it
back.

**Select All** / **Select None** — Selects every surface, or clears the
selection.

!!! tip "New in HVE 2027"
    - **Derive from Mesh** builds panels from the flat regions of a named
      group of the vehicle's mesh (**group**, "interior" by default; "body" is
      the exterior shell), in the **region** **Whole vehicle**, **Forward of the
      CG** or **Behind the CG**. Only the ten largest regions are kept, so for
      a pedestrian impact use **Pedestrian preset** ("body", forward of the
      CG), which gives the windshield, hood, hood leading edge and bumper. It
      derives geometry only — check each panel's material — and appends to the
      list.
    - **Seed Standard Interior** replaces the list with a generic driver
      compartment (seat, floor, toe pan, instrument panel, wheel, glass, roof,
      doors), fitted to an occupant of the vehicle if there is one. It is
      marked as a generic interior, not measured for the vehicle.
    - An interior **template** list with **Use Template**.
    - **Save Interior...** and **Load Interior...** save the vehicle's surfaces
      to a `.json` file and load them back.

!!! warning "Not in HVE 2027"
    - The limit of 25 surfaces is not enforced when adding.
    - **OK / Cancel**: edits apply immediately.

<!-- NAV -->

---

← Previous: [Cone Editor Dialog](ConeEdtDlg.md)  |  [Index](README.md)  |  Next: [Cylinder Editor Dialog](CylinEdDlg.md) →

<!-- /NAV -->
