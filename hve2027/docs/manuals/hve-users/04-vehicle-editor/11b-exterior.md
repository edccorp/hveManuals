# Chapter 11 — Vehicle Model Definition (Part B: Exterior)

*Adapted for HVE 2027 from the HVE User's Manual (Version 5, Seventh
Edition, Jan 2006), Chapter 11.*

This part covers the vehicle exterior: the exterior dimensions (CG to
Front, Right Side, Back, Left Side, Top and Bottom) and the exterior
structural stiffness coefficients. In HVE these properties are edited by
clicking on the exterior spheres displayed on the vehicle in the Vehicle
Viewer.

!!! note "HVE 2027"
    HVE 2027 has no exterior spheres. The dimensions are edited in the
    **Dimensions / Inertias** section of the Vehicles panel, and the
    stiffness coefficients with **Vehicle › Crush Stiffness...** (see below).

## Vehicle Exterior Dimensions

The vehicle's exterior dimensions are defined by its overall length and
overall width. In HVE they are edited with the Vehicle Dimensions dialogs
(CG to Front, Right Side, Back, Left Side, Top, Bottom).

In HVE 2027 they are edited in the Vehicles panel's **Dimensions / Inertias**
section (Figure 11-19), which is HVE's Vehicle Wizard: Overall Length,
Overall Width, Overall Height, CG Height, Wheelbase, Front Overhang, Rear
Overhang (from the rearmost axle), and CG to Axle 1 / Axle 2. The
**Exterior Extents** table below them shows the result — the CG to front,
back, right, left, top and bottom distances the solver receives, with the
overall length, width and height — and, when a 3-D model is loaded, the
model's own extents for comparison.

![Figure 11-19](../images/hvn-04-vehicles-panel.png)
*Figure 11-19: The Vehicles panel. Its Dimensions / Inertias section edits the overall dimensions; the Exterior Extents table shows the CG-to-exterior distances derived from them.*

!!! note "HVE 2027"
    - The CG-to-exterior distances are **derived** from the overall
      dimensions, overhangs, wheelbase and CG location; they are not typed
      directly. Edits apply as you type, and Edit › Undo reverses them.
    - The dimensions are measured from the sprung-mass CG. The **Dimensions
      From CG** part of the section shows the CG to axle distances and CG
      height on both the total and the sprung basis. HVE 2027 has no Vehicle
      Dimensions Basis preference.

The Exterior Dimension parameters are described below.

- **CG to Front** — Assigns the distance from the CG to the front of the
  current vehicle.
- **CG to Right Side** — Assigns the distance from the CG to the right side
  of the current vehicle.
- **CG to Back** — Assigns the distance from the CG to the back of the
  current vehicle (the value will be negative, indicating it is behind the
  CG).
- **CG to Left Side** — Assigns the distance from the CG to the left side
  of the current vehicle (in the SAE coordinate system the value will be
  negative, indicating it is to the left of the CG).
- **CG to Top** — Assigns the distance from the CG to the top of the
  current vehicle (the value will be negative, indicating the roof is above
  the CG).
- **CG to Bottom** — Assigns the distance from the CG to the bottom side of
  the current vehicle.

**Table 11-10: Vehicle Exterior Dimension Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| CG to Front/Back/Side/Top/Bottom | UtVehDispLength | Vehicle-fixed distance from the CG to the front, right side, back, left side, top or bottom |

See also the HVE reference pages:
[CG to Front](../../02-vehicles/CGsToAll.md),
[CG to Right Side](../../02-vehicles/CGsToAll1.md),
[CG to Back](../../02-vehicles/CGsToAll2.md),
[CG to Left Side](../../02-vehicles/CGsToAll3.md),
[CG to Top](../../02-vehicles/CGsToAll4.md),
[CG to Bottom](../../02-vehicles/CGsToAll5.md).

## Vehicle Exterior Stiffness Coefficients

The vehicle's structural properties are defined by its stiffness
coefficients. The user may choose to edit these coefficients for the front,
back or sides of the vehicle.

!!! note "HVE 2027"
    The stiffness coefficients are vehicle data, edited in the Vehicle editor
    with **Vehicle › Crush Stiffness...**. The dialog shows the Front, Rear,
    Left and Right sides, each with its **A**, **B** and **Kv** Stiffness, and
    below them HVE's 3-D stiffness: **3-D Node Stiffness** — Constant, Linear,
    Quadratic and Cubic for the Front, Right, Back, Left, Top and
    Undercarriage zones — with the Conversion Height, Saturation Crush and Max
    Crush. It says which engine reads each part: A and B are read by EDSMAC4,
    Kv by EDSMAC (and by EDVSM for the body against the ground), and the 3-D
    node stiffness by SIMON (DyMESH); EDCRASH takes its A and B from the
    event's damage profile (Event Information › Vehicle Impact Setup).
    **From crash tests...** computes CRASH3 A and B from staged barrier tests.

    The four sides are also reached from **Event › Crush Profile** (EDCRASH,
    EDSMAC and EDSMAC4 events), whose **Crush & Geometry** window has **CG to
    Front…**, **CG to Rear…**, **CG to Left…** and **CG to Right…** buttons.

    There is no stiffness for the top and bottom in the A/B/Kv form, as in
    HVE. Coefficients are shown in the units set in Preferences (A in lb/in
    and B in lb/in² in US units).

To display or edit the current vehicle's A, B and Kv stiffness
coefficients, perform the following steps:

1. In the Vehicle editor (F3), select the vehicle.
2. Choose **Vehicle › Crush Stiffness...**. The Crush Stiffness dialog is
   displayed.
3. View and/or edit the stiffness properties of each side. Changes apply as
   they are made.

The Exterior Stiffness parameters are described below.

- **'A' Stiffness Coefficient** — Assigns the force per unit of damage
  width required to initiate permanent crush (see Figures 11-20 and 11-21).
- **'B' Stiffness Coefficient** — Assigns the linear spring rate (force vs
  deflection constant) per unit of damage width required to produce
  permanent crush (see Figures 11-20 and 11-21).
- **'Kv' Stiffness Coefficient** — Assigns the linear spring rate (force vs
  deflection constant) per unit of damage width required to produce
  permanent crush. This value differs from the B constant in that it
  assumes the force vs deflection graph goes through zero (i.e., A = 0).

![Figure 11-21](../images/p381-figB11-21.png)
*Figure 11-21: Force vs Deflection characteristics of a vehicle, and their relationship to the A, B and Kv stiffness coefficients (see also references 2.8–2.14, 4.20, 4.29).*

**Table 11-11: Vehicle Exterior Stiffness Coefficients Parameters**

| Parameter | Unit Name | Description |
| --- | --- | --- |
| A Stiffness | UtVehAStiff | Vehicle 'A' stiffness coefficient |
| B Stiffness | UtVehBStiff | Vehicle 'B' stiffness coefficient |
| Kv Stiffness | UtVehKStiff | Vehicle 'Kv' stiffness coefficient |

See also the HVE reference pages:
[Stiffness Coefficients dialog (2-D)](../../02-vehicles/StiffCoeffDlg.md),
[A Stiffness](../../02-vehicles/AStiffDlg.md),
[B Stiffness](../../02-vehicles/BStiffDlg.md).


<!-- NAV -->

---

← Previous: [Chapter 11 — Vehicle Model Definition (Part A: Sprung Mass)](11a-sprung-mass.md)  |  [Index](README.md)  |  Next: [Chapter 11 — Vehicle Model Definition (Part C: Suspension)](11c-suspension.md) →

<!-- /NAV -->
