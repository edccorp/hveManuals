# Contacts Dialog Box

The Contacts dialog allows the user to select the allowable interaction between human ellipsoids and vehicle contact surfaces. For example, there is little chance of a human pedestrian's pelvis interacting with the vehicle's interior contact surfaces (e.g., the seat) during the simulation. Therefore, it makes little sense to perform force calculations for this ellipsoid/contact surface pair. By selecting only those contact surfaces having a chance of interaction, far fewer calculations need to be performed. As a result, the calculation time can be reduced significantly.

The contents of the Contacts dialog box are as follows.

## Object

A read-only field displaying the name of the source object (the currently selected human or vehicle), and a combo box listing all humans and vehicles in the current event. Select the target object from this combo box; the Target(s) list is refreshed for the chosen object.

## Source(s)

A multiple-selection list box containing all the contacts (human ellipsoids or vehicle contact surfaces) defined for the source object. **Select All** and **Deselect All** buttons below the list select or clear all source contacts.

## Target(s)

A multiple-selection list box containing all the contacts (human ellipsoids or vehicle contact surfaces) defined for the target object. **Select All** and **Deselect All** buttons below the list select or clear all target contacts.

## Combined Material Properties

Some simulation models define the human ellipsoid and vehicle contact surface material properties according to the sole properties of the ellipsoid or contact surface; other simulations define the material properties as a combined property shared by the two interacting objects. This group is enabled only for calculation methods that use combined material properties. It contains the following items:

- **For / And** — read-only fields identifying the source contact and target object for which the combined material is being assigned.
- **Segment(s)** — A multiple-selection list box containing the contacts defined for the target object; only those contacts selected in the Target(s) list are selectable in this list box. **Select All** and **Deselect All** buttons select or clear all segments.
- **Current Material** — A read-only field displaying the name of the combined material currently assigned to the selected source/target pair.
- **Edit ...** — Displays the Combined Material Properties dialog, used to view and edit the force-deflection and friction properties of the combined material for the selected pair.

## OK / Cancel

**OK** saves the contact selections to the current event; **Cancel** discards all changes.

---
*Source topic: ContactsDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Events & Driver Controls](README.md)  |  [Index](README.md)  |  Next: [Driver Controls](DriverControls.md) →

<!-- /NAV -->
