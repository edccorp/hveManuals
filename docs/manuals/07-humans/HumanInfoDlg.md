# Human Information Dialog

This dialog is used to define the basic parameters (name, seating location and body description) for a human in the current case.

> Note: As of HVE Version 10, *new* humans are added to the case using the GEBOD Human Information dialog (described below), which generates the human data set from the GEBOD body generator. The classic Human Information dialog described first is still displayed when editing a human that was created from the older human database (pre-Version 10 humans). In both dialogs, the body-description controls are disabled if the human already has event output tracks.

## Classic Human Information Dialog

### Human Name
A user-editable field allowing the user to assign a name to the current human. By default the name is built from the current selections (e.g. "Male Adult Wt% 50 Ht% 50") and is updated automatically as selections change until the user types a custom name. The name must be unique within the case and may not exceed the maximum HVE name length.

### Location
Displays a list allowing the user to choose a seat position for the current human. The available positions are Front, Rear and Back rows, each with Right, Center and Left seats (nine positions total). The user may also choose Pedestrian.

### Sex
A combo box. The user may select either Male or Female (choices are limited to those available in the human database).

### Age
A combo box allowing the user to select Adult, or 12 Year, 9 Year, 6 Year and 3 Year child ages (choices are limited to those available in the database for the selected sex).

### Weight Percentile
A combo box containing the available weight percentiles: 2.5, 50 and 97.5 (choices depend on the selected sex and age).

### Height Percentile
A combo box containing the available height percentiles: 2.5, 5, 50, 95 and 97.5 (choices depend on the selected sex, age and weight percentile).

## GEBOD Human Information Dialog (Version 10 and later)

New humans are added to the current case using this dialog, which builds the human from GEBOD (GEnerator of BOdy Data) regression data rather than from a fixed database of body types.

### Human Name
A user-editable field allowing the user to assign a name to the current human.

### Location
Same seat-position list as the classic dialog: Front/Rear/Back rows with Right/Center/Left seats, or Pedestrian.

### Subject Type
A combo box used to select the GEBOD subject type: Child, Female or Male. A User-defined subject type is also listed but is not yet supported in the current build; selecting it produces a "not yet supported" message and reverts the selection to the previous type.

### Basis
A combo box selecting which body measurement(s) the GEBOD data set is based on: Age, Weight, Height or All.

### Age
A slider and edit field specifying the subject's age. The Options radio buttons select whether age is entered in Months or Years.

### Weight
A slider and edit field specifying the subject's weight. The Options radio buttons select whether the value is entered as a percentile (%-tile) or directly in weight units (e.g. lb).

### Standing Height
A slider and edit field specifying the subject's standing height. The Options radio buttons select whether the value is entered as a percentile (%-tile) or directly in length units (e.g. in).

### Filename / Select
Intended to display the name of the GEBOD data file used to create a User-defined subject. Because User-defined subjects are not yet supported in the current build, these controls are inactive: the Filename field and Select button are disabled on all code paths, and the Select button performs no action.

---
*Source topic: HumanInfoDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Joint Data Dialog Box](Human3.md)  |  [Index](README.md)  |  Next: [Human CG Dialog Box](HumCGDlg.md) →

<!-- /NAV -->
