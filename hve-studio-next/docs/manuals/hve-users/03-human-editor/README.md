# Section Three: Human Editor

*Adapted for HVE Studio from the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Section Three "Human Editor".*

The purpose of the Human Editor is to provide anthropomorphically correct
3-D human models for use in dynamic reconstructions and simulations involving
motor vehicle occupants and pedestrians. This section describes how to create
and edit these human models in HVE Studio, and gives a detailed description of
the human model parameters.

The basic physical/mathematical model of the human is HVE's 15-segment,
14-joint model. Each segment has dimensional and inertial properties that may
be edited by the user. In addition, each segment may have attached to it one
or more contact ellipsoids (up to three per segment), which are physical
surfaces used by simulations to detect interaction with other objects and to
calculate the resulting forces. The details of the human model are provided
in Chapter 9.

!!! note "HVE Studio"
    HVE Studio uses HVE's own human model and HVE's own GEBOD body generator,
    so the model described in Chapter 9 is unchanged. The editor around it is
    new: the Human Editor is the **Human (F2)** tab under the menu bar, and
    the humans of the case are managed in its **Humans** panel.

## General Procedure

To use the Human Editor, perform the following steps:

1. Select the **Human (F2)** tab (or press F2).
2. In the Humans panel, press **Add Human**. HVE Studio generates a body
   with GEBOD from the subject type, age group and weight and height
   percentiles (see Chapter 8). Humans also arrive with an HVE case file
   (`.hve`) or an HVE Studio case opened with **File › Open Case...**.
3. If desired, modify the properties of the selected human to suit the
   needs of the current case. Properties which may be modified are:
   - Inertial Properties
   - Segment Color
   - Contact Ellipsoid Properties
   - Injury Tolerances
   - Joint Properties

## Overview of Section Three

- [Chapter 8 — Creating and Editing Humans](08-creating-editing-humans.md)
  describes the process of creating and editing humans.
- [Chapter 9 — Human Model Definition](09-human-model-definition.md) provides
  a detailed overview of the human model.

## Related Dialog Reference Pages

The individual human dialogs are documented in the
[Human Dialog Reference](../../07-humans/README.md):

- [Human Information Dialog (classic and GEBOD)](../../07-humans/HumanInfoDlg.md)
- [Human CG (segment popup) Dialog](../../07-humans/HumCGDlg.md)
- [Inertial Data Dialog](../../07-humans/Human.md)
- [Contact Ellipsoids Dialog](../../07-humans/Human1.md)
- [Human Material Properties Dialog](../../07-humans/HumMatProp.md)
- [Injury Tolerance Data Dialog](../../07-humans/Human2.md)
- [Joint Data Dialog](../../07-humans/Human3.md)
- [Joint Properties Dialog](../../07-humans/HumJntPropDlg.md)
- [Selected Humans & Vehicles Dialog](../../07-humans/SelHumVehDlg.md)

<!-- NAV -->

---

Next: [Chapter 8 — Creating and Editing Humans](08-creating-editing-humans.md) →

<!-- /NAV -->
