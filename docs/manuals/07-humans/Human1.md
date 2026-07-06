# Human Contact Ellipsoids Dialog Box

Ellipsoid properties for the HVE Human Model are defined for each of the 15 segments. Each segment may have up to 3 contact ellipsoids. To view and edit the current human's ellipsoid parameters, click on the desired segment CG and choose Ellipsoids from the segment popup menu. The individual parameters are displayed in the Contact Ellipsoids dialog. The dialog title bar shows the current human's name and the selected segment.

## Current Ellipsoid
Drop-down list of the user-supplied names for each contact ellipsoid on the selected segment. Select an ellipsoid to display and edit its parameters.

## Coordinates i, j, k
The i, j and k coordinates of the center of the selected ellipsoid, defined relative to the segment principal axis system.

## Semi-axis Length i, j, k
The i, j and k semi-axis lengths of the selected ellipsoid.

## Principal Axes Roll, Pitch, Yaw
The roll, pitch and yaw angles of the ellipsoid axis system relative to the segment axis system.

## Material Name
Read-only display of the human material currently assigned to the selected ellipsoid. If no material has been assigned, "Default Human Material" is displayed. Use the Material button to change the assigned material.

## Add
Displays the New Ellipsoid dialog, which prompts for a name for the new ellipsoid. A segment may have at most 3 contact ellipsoids, and duplicate ellipsoid names on the same segment are not allowed; an error message is displayed in either case.

## Delete
Removes the current contact ellipsoid from the selected segment after a confirmation prompt. The button is disabled when no ellipsoids remain.

## Material
Displays the [Human Material Properties Dialog Box](HumMatProp.md), used to view, edit, open and save the human material assigned to the selected ellipsoid.

> Note: The old help linked the Material button to the (vehicle/environment) Material Properties dialog; the button actually opens the Human Material Properties dialog.

---
*Source topic: Human1.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Inertial Data Dialog Box](Human.md)  |  [Index](README.md)  |  Next: [Injury Tolerance Data Dialog Box](Human2.md) →

<!-- /NAV -->
