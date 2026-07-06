# Injury Tolerance Data Dialog Box

Injury tolerances may be defined for the current human. These injury tolerances are used during the current event as guidelines to estimate when specific injuries might occur. Open the dialog by clicking on a segment CG and choosing Injury Tolerance from the segment popup menu. The dialog title bar shows the current human's name and the selected segment.

This dialog box contains the following parameters:

## HIC
Head Injury Criterion, an empirically derived index used to estimate the probability of a closed head injury.

## Head Pitch Concussion (deg/sec²)
Tolerance for angular acceleration of the head about the pitch axis of the neck.

## Head Side Acceleration (g)
Tolerance for linear acceleration of the head in the direction of the head-fixed side axis.

## Chest SI (g)
Chest Severity Index, an injury index indicating the maximum chest acceleration.

## Chest Force (lb)
The tolerance for peak force against the chest in the direction of the chest-fixed i-axis.

## Chest Forward Accel (g)
The tolerance for peak chest acceleration in the direction of the chest-fixed i-axis.

> Note: This field appeared in the old help as "Chest Forward Access" (a typographical error).

## Max Knee Force (lb)
The tolerance for peak force against the knee in the direction of the knee-fixed i-axis (peak axial femur loading).

## Belt Injury Tolerance
The belt tolerances are entered separately for the Left Belt and Right Belt in the Belt Injury Tolerance group:

**Max Lap Belt Force (lb) — Left Belt / Right Belt**
The tolerance for lap belt tension, above which injury is expected to occur. Separate values are entered for the left and right lap belt webbing.

**Max Torso Belt Force (lb) — Left Belt / Right Belt**
The tolerance for torso belt tension, above which injury is expected to occur to the torso. Separate values are entered for the left and right torso belt webbing.

> Note: The old help listed a single Max Lap Belt Force and a single Max Torso Belt Force; the current dialog provides separate left- and right-belt entries (stored as LeftLap, RightLap, LeftTorso and RightTorso in the human data structure). The old description of Max Lap Belt Force as "peak axial loading of the femur" was incorrect — femur axial loading is covered by Max Knee Force.

---
*Source topic: Human2.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Human Contact Ellipsoids Dialog Box](Human1.md)  |  [Index](README.md)  |  Next: [Joint Data Dialog Box](Human3.md) →

<!-- /NAV -->
