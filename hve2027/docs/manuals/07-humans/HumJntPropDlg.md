# Human Joint Properties Dialog Box

Each joint is defined by a number of physical properties. Except for the joint
type, each property is entered separately for rotation about the joint's i, j
and k axes.

!!! note "HVE 2027"
    In the Human editor (F2), open the **Occupants** panel (**Occupant › Human
    Information...**), select the human and press **Joint Properties...**. The
    **Joint Properties** window has a **Joint** list of all 14 joints; it needs a
    body model (see [Inertial Data](Human.md)). The properties are a table with
    columns **I (roll)**, **J (pitch)** and **K (yaw)**; unit labels follow the
    units set in Tools › Preferences where the row has a unit. While a solved
    run is on screen the window is read-only.

## Joint type

**Ball-and-Socket** or **Hinge**.

## Rotation properties

**Stop Angle + (deg)** — The angle at which the joint stop is applied for
positive rotations.

**Stop Angle - (deg)** — The angle at which the joint stop is applied for
negative rotations.

**Stop Elasticity +** — Joint stop linear elastic property for positive
rotations.

**Stop Elasticity -** — Joint stop linear elastic property for negative
rotations.

**Stop Energy Dissipation** — Ratio of dissipated to total energy of the joint
stop.

**Linear Elastic** — Joint linear elastic property during the normal range of
motion.

**Quadratic Elastic** — Joint quadratic elastic property during the normal range
of motion.

**Cubic Elastic** — Joint cubic elastic property during the normal range of
motion.

**Damping Constant** — Joint damping property during the normal range of motion.

**Full Damping Vel (deg/s)** — Angular velocity required to achieve full joint
damping.

## Joint injury tolerance

**Tolerance Angle + (deg)** — The positive joint angle which, if exceeded, is
predicted to cause injury to the joint. HVE's *Max Angle For + Axis Rotation*.

**Tolerance Angle - (deg)** — The negative joint angle which, if exceeded, is
predicted to cause injury to the joint.

!!! note "HVE 2027"
    - GATB uses the I and K axes of the elastic and dissipation terms; the J
      values are kept so the data round-trip unchanged.
    - The Quadratic and Cubic Elastic rows are shown without a unit and are not
      converted between unit systems.
    - Values are not range-checked when the window is closed; edits apply
      immediately and **Edit › Undo** (Ctrl+Z) takes one back.

<!-- NAV -->

---

← Previous: [Human CG Dialog Box](HumCGDlg.md)  |  [Index](README.md)  |  Next: [Human Material Properties Dialog Box](HumMatProp.md) →

<!-- /NAV -->
