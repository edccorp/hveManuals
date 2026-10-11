# Injury Tolerance Data Dialog Box

Injury tolerances may be defined for each human. They are used during the event
as guidelines to estimate when specific injuries might occur.

!!! note "HVE 2027"
    In the Human editor (F2), open the **Occupants** panel (**Occupant › Human
    Information...**), select the human and press **Injury Tolerances...**. The
    window is titled **Injury Tolerances**; the tolerances belong to the whole
    human, not to a segment. Forces follow the units set in Tools ›
    Preferences; accelerations are entered in g. While a solved run is on
    screen the window is read-only.

## Head

**HIC (dimensionless)** — Head Injury Criterion, an empirically derived index
used to estimate the probability of a closed head injury.

**Head Pitch Accel (rad/s²)** — Tolerance for angular acceleration of the head
about the pitch axis of the neck. HVE's *Head Pitch Concussion*.

!!! note "HVE 2027"
    HVE enters this tolerance in deg/sec²; HVE 2027 in rad/s².

**Head Side Accel (g)** — Tolerance for linear acceleration of the head along
the head-fixed side axis.

## Chest

**Chest Vertical Accel (g)** — HVE's *Chest SI*: the Chest Severity Index
tolerance, an index based on the maximum chest acceleration.

**Chest Forward Accel (g)** — Tolerance for peak chest acceleration along the
chest-fixed i-axis.

**Chest Contact Force** — Tolerance for peak force against the chest along the
chest-fixed i-axis. HVE's *Chest Force*.

## Lower Extremity

**Knee Contact Force** — Tolerance for peak force against the knee along the
knee-fixed i-axis (peak axial femur loading). HVE's *Max Knee Force*.

## Belt Loads

**Left Lap Belt Max**, **Left Torso Belt Max**, **Right Lap Belt Max**, **Right
Torso Belt Max** — Tolerances for lap and torso belt tension on each side, above
which injury is expected to occur. HVE's *Belt Injury Tolerance* group.

!!! note "HVE 2027"
    There is no OK/Cancel: edits apply immediately, and **Edit › Undo** (Ctrl+Z)
    takes one back.

<!-- NAV -->

---

← Previous: [Human Contact Ellipsoids Dialog Box](Human1.md)  |  [Index](README.md)  |  Next: [Joint Data Dialog Box](Human3.md) →

<!-- /NAV -->
