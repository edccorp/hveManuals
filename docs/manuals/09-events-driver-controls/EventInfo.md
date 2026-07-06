# Event Information Dialog Box

This dialog box is used to create a new event or edit an existing one. It assigns the event's name, selects the humans and vehicles that participate in the event, and chooses the physics program (calculation method) used to execute the event.

## Event Name

Editable text field containing the name of the current event. HVE assigns a default name based on the selected objects and calculation method; the name may be edited by the user and is used to identify the event throughout the case.

## Humans List

A multiple-selection list containing all humans currently defined in the case. Click a human's name to add it to (or remove it from) the current event. Selected humans appear in the Event Humans and Vehicles list.

## Vehicles List

A multiple-selection list containing all vehicles currently defined in the case. Click a vehicle's name to add it to (or remove it from) the current event. Selected vehicles appear in the Event Humans and Vehicles list.

## Event Humans and Vehicles

A list displaying the humans and vehicles that have been selected for the current event, in the order they were selected. This order determines the object numbering used by the calculation method.

## Calculation Method

A drop-down list of the physics programs (calculation method executables) installed in the calcMethods directory. Select the simulation or reconstruction model to be used for this event. If no calculation methods are found, an error message is displayed. The calculation method cannot be changed after the event has been created.

A status line at the bottom of the dialog prompts the user (e.g., "Select any Human or Vehicle") and reports the current selection state.

> **Note:** The *Browse EXE* button described in earlier versions of this dialog has been removed; calculation methods are now located automatically in the calcMethods directory.

---
*Source topic: EventInfo.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Driver Controls Speed Follower](DriverControls8.md)  |  [Index](README.md)  |  Next: [Event Setup Menu](EventSetup.md) →

<!-- /NAV -->
