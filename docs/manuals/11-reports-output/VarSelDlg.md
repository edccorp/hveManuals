# Selecting Variables

The Variable Selection dialog is used for selecting the variables to be displayed in the Key Results window (Event mode) and in the Variable Output table (Playback mode). The same dialog serves both purposes; the set of available groups and variables is supplied by the physics program for the current event.

This dialog contains the following items:

## Object Name

A combo box containing the names of all the humans and vehicles in the current event. Variables are selected per object; choose the object whose variables you wish to select.

## Current Group

Read-only display of the output group currently selected in the Output Groups list.

## Output Groups

List of the available variable groups (e.g. accelerations, velocities, positions, tire data, belt and airbag data) for the selected object. Choose the desired group from the list; the Variables list is filled with that group's variables.

## Variables

Displays all the variables available for the selected group. Choose the desired variables from the multiple-selection list box. Selected variables are highlighted. Click on any highlighted variable to deselect it.

## Clear Selection

Deselects all the selected variables in the current group.

## Clear All Selections

Deselects every selected variable in all groups for the current object. A confirmation dialog is displayed first (with a "don't ask again" option).

## Select All

Selects all the variables in the current group. This button (and All Groups/Vars) is shown only when the dialog is invoked for variable export; it is hidden for ordinary Key Results and Variable Output selection.

## All Groups/Vars

Selects every variable in every output group for the current object. Shown only when the dialog is invoked for variable export.

## OK / Cancel

OK accepts the selections and updates the Key Results window or Variable Output table; Cancel discards the changes.

---
*Source topic: VarSelDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Variable Output Report](VarOutRepDlg.md)  |  [Index](README.md)

<!-- /NAV -->
