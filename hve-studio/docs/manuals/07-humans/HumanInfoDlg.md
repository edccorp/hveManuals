# Human Information Dialog

This dialog defines the basic parameters of a human in the case: its name,
seating location and body description, from which the body model is generated.

!!! note "HVE Studio"
    In the Human editor (F2) choose **Human › Human Information...**. It opens
    the **Humans** panel, which lists the humans of the case and edits the
    selected one. It replaces both of HVE's dialogs — the classic Human
    Information dialog and the GEBOD Human Information dialog — and also holds
    the buttons that open the human's other windows. Weight and mass follow the
    units set in Tools › Preferences. While a solved run is on screen the panel
    is read-only (the buttons that open other windows stay available).

## Add Human / Remove

**Add Human** adds a human ("Human 1", "Human 2", …) and builds its body
with GEBOD at once. **Remove** deletes the selected human from the case and from
every event that holds it.

Which vehicle a human rides in, and where, is set per event in Event
Information under **Humans in Event** (see
[Selected Humans & Vehicles](SelHumVehDlg.md)); this panel is the body itself.

## Occupant

The human being edited.

## Identity

**Name** — A name for the human.

**Location** — The seat the occupant nominally occupies: Front, Rear and Back
rows with Right, Center and Left seats (Front Left is the driver), or
**Pedestrian**.

## Anthropometry

**Subject Type** — **Male** or **Female**.

**Age Group** — **Child (0-12)**, **Teen (13-17)**, **Adult (18-64)** or
**Senior (65+)**.

**Weight Percentile** / **Height Percentile** — **5th**, **25th**, **50th**,
**75th** or **95th**.

Changing any of these rebuilds the body with GEBOD, unless the human has been
posed in an event (the rebuild would discard the pose). **Regenerate GEBOD Body**
rebuilds it on demand and resets the human's pose in every event to the default
posture. "body: present" or "body: none" beside the button (with **View › Show
Guidance Text** on) says whether the human has a body model; a GEBOD message,
if any, is shown below.

!!! note "How GEBOD is driven"
    An adult or senior is generated from the weight **and** height percentiles
    (HVE's Basis = All). A child or teen is generated on the **age** basis —
    the 6-year and 12-year subjects respectively — because GEBOD's percentile
    tables cover adults only; the percentiles are not used for them. The
    subject type follows: Child for a child or teen, otherwise Male or Female.

## Anthropometric

**Weight** and **Mass** — the human's total weight and mass; editing either sets
the other through gravity. Once a body model exists this is the total of the 15
segment masses, best set through the percentiles above (GEBOD recomputes it).

## Injury Output

Placeholder for injury results; before a run it shows "Run simulation for
injury data" (with **View › Show Guidance Text** on), and after one it shows
"--". Use the Output menu for an occupant run's results.

## Buttons

- **Injury Tolerances...** — [Injury Tolerance Data](Human2.md)
- **Body Segments...** — [Inertial Data](Human.md), [Contact
  Ellipsoids](Human1.md) and [Joint Data](Human3.md)
- **Joint Properties...** — [Human Joint Properties](HumJntPropDlg.md)
- **Body Pose...** — the human's initial posture and initial velocity in the
  active event (below)

The airbag at an occupant's seat belongs to the vehicle: **Vehicle › Editors › Airbags...**
in the Vehicle editor (see [Air Bag Restraints](../06-safety-systems/AirBagDlg.md)).

## Body Pose

!!! tip "New in HVE Studio"
    The **Body Pose** window sets, for the **active event**, the initial
    orientation of each of the 15 segments (**Roll**, **Pitch**, **Yaw** in
    degrees, each relative to its parent segment) and the human's initial
    velocity (**u (fwd)**, **v (right)**, **w (down)**, in the segment frame).
    Check **Pose this body (use the angles below)** to use the angles; with it
    off the body is drawn and solved in its default posture (a seated occupant
    with the upper legs pitched 90° forward, a pedestrian standing). **Reset to
    default posture** and **Zero all angles** reset the table. The velocity is
    zero for an occupant riding in a vehicle (it is relative); a pedestrian's
    walking speed goes here, and EDHIS and GATB read it. A human not in the
    active event cannot be posed; the window lists the events that hold it.
    It can also be opened with the **Pose** button in Event Information's
    Humans in Event list.

!!! warning "Not in HVE Studio"
    - GEBOD's **Basis** selector, the **Age** value in months or years, and
      entering **Weight** or **Standing Height** as a value rather than a
      percentile: the body is built from the four lists above.
    - **User-defined** subject type and the **Filename / Select** controls
      (inactive in HVE as well).
    - Percentiles other than 5, 25, 50, 75 and 95.
    - The classic dialog's fixed human database; every human is generated
      with GEBOD.

<!-- NAV -->

---

← Previous: [Joint Data Dialog Box](Human3.md)  |  [Index](README.md)  |  Next: [Human CG Dialog Box](HumCGDlg.md) →

<!-- /NAV -->
