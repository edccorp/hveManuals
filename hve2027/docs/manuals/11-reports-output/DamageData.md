# Damage Data

HVE's Damage Data dialog assigned a measured damage profile to a vehicle for an
EDCRASH reconstruction. The damage profile is obtained by post-crash inspection
of the vehicle, and provides a significant amount of useful information about
the collision.

!!! note "HVE 2027"
    There is no separate Damage Data dialog. The same inputs are in each
    vehicle's block of the **Vehicle Impact Setup** section of the
    [Event Information](../09-events-driver-controls/EventInfo.md#vehicle-impact-setup-edcrash)
    panel, shown for an EDCRASH event. Lengths are in the vehicle length unit
    set in Preferences (inches in US units). Edits take effect immediately;
    there is no Apply, OK or Cancel.

![Vehicle Impact Setup for an EDCRASH event](../09-events-driver-controls/images/hvn-event-info-edcrash.png)

## CDC

The Collision Deformation Classification, a seven-character code describing the
vehicle damage (an SAE Recommended Practice). The case of the letters is kept as
entered; EDCRASH tests the code in upper case. The extent digit is last.

!!! warning "Not in HVE 2027"
    Entering a CDC does not fill in a default PDOF, damage profile or EBS, and
    an invalid CDC does not grey the profile fields. Enter the profile directly.

## PDOF (deg)

Simply stated, the PDOF is the direction of the impulse. This has physical significance, because the direction of the impulse is the same as the direction of the delta-V. Because the damage analysis has no way of computing the forward and lateral components of the delta-V, the user-entered PDOF is used for this purpose.

## Auto-calculate PDOF (from the other vehicle)

HVE's *Use Newton's 3rd Law*. When checked, the PDOF field is disabled and
EDCRASH calculates this vehicle's PDOF from the other vehicle's PDOF and the two
impact headings, so that the impulses on the two vehicles are equal and
opposite. Only one vehicle may have it checked.

!!! warning "Refused by the engine"
    If both vehicles have **Auto-calculate PDOF** checked, EDCRASH refuses the
    event (stop code −5443); the panel says so in red. A barrier always has its
    PDOF calculated, so in a barrier collision the vehicle must not.

## Impulse Center

**Derive impulse center from damage profile** (checked by default) computes the
impulse center from the damage profile geometry. Uncheck it to enter
**Impulse Center X** and **Impulse Center Y** (vehicle-fixed).

## Basis

**EES** / **Damage Profile**, and the **EES** speed when the basis is EES, are
shown **greyed**, with the stored value.

!!! warning "Not in HVE 2027"
    EDCRASH always reconstructs from the crush profile: no engine reads the
    basis or the EES (equivalent barrier speed), in HVE's own EDCRASH either.
    The values are kept as the case stores them.

## Measured Crush (Damage Profile)

Under **Measured Crush (drives Delta-V)**:

- **# crush depths** — the number of crush measurements (0 to 10). The number of
  zones is one less (up to 9). With fewer than 2 depths no profile is entered
  and delta-V stays 0.
- **C1** ... **Cn** — the crush depths, from the CDC's damaged side.
- **Damage width** — the width of the damage region. In most cases, include
  induced damage (non-contact damage adjacent to the area of actual contact) if
  the goal is to estimate delta-V.
- **Damage offset** — the distance from the CG to the midpoint of the damage
  profile.
- **Per-zone A/B** — an **A** and **B** stiffness for each zone, with **All same
  as zone 1**. All zero means the scalar A/B below applies to every zone.

## A Stiffness / B Stiffness

**A Stiffness** (lbf/in): the force per unit of damage width required to initiate
permanent damage. **B Stiffness** (lbf/in²): the force per unit of crush depth per
unit of damage width. Shown in N/m and N/m² in SI units. These apply to every
zone unless per-zone values are entered.

## Results

!!! warning "Not in HVE 2027"
    The read-only **Delta-V Total / Long / Lat**, **Damage Energy** and **Peak
    Force** fields, and the graphic pane drawing the profile, are not part of
    the panel. Run the event: the results are in **Key Results**, the
    **Variable Report** and the engine's own pages in **Output › HVE Reports**.

!!! note "HVE 2027"
    **Event › Damage Profiles...** opens a different dialog: the vehicle's crush
    **stiffness** per side (Distance, A, B and Kv for Front, Rear, Left and
    Right) used by the simulation programs, and the 3-D node stiffness used by
    DyMESH. It is not the measured damage.

<!-- NAV -->

---

← Previous: [Common Scene Report Dialog](CommSceDlg.md)  |  [Index](README.md)  |  Next: [Trajectory Report](TrajRepDlg.md) →

<!-- /NAV -->
