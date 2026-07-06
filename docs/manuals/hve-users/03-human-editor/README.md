# Section Three: Human Editor

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Section Three "Human Editor". Verified against the current HVE application source (`HVEINV-64/`) and the physics human data structure (`Physics/Include/HUMAN.H`).*

The purpose of the HVE Human Editor is to provide anthropomorphically correct
3-D human models for use in dynamic reconstructions and simulations involving
motor vehicle occupants and pedestrians. This section of the HVE User's Manual
describes how to create and edit these human models. It also provides a
detailed description of the human model parameters.

The basic physical/mathematical model of the HVE human is a 15-segment,
14-joint model. Each of these segments has dimensional and inertial properties
that may be edited by the user. In addition, each segment may have attached to
it one or more contact ellipsoids (up to three per segment), which are
physical surfaces used by simulations to detect interaction with other objects
and to calculate the resulting forces. The details of the HVE Human Model are
provided in Chapter 9.

## General Procedure

To use the Human Editor, perform the following steps:

1. Select Human mode.
2. Select one or more humans, either from the Human Database (via the GEBOD
   body generator in current versions — see Chapter 8) or from a previous HVE
   case.
3. If desired, modify the properties of the selected human(s) to suit the
   needs of the current case. Properties which may be modified are:
   - Inertial Properties
   - Segment Color
   - Contact Ellipsoid Properties
   - Injury Tolerances
   - Joint Properties

## Overview of Section Three

This section of the HVE User's Manual provides a detailed explanation of the
process of creating and editing humans, and also presents a detailed overview
of the human model's physical properties:

- [Chapter 8 — Creating and Editing Humans](08-creating-editing-humans.md)
  describes the process of creating and editing humans.
- [Chapter 9 — Human Model Definition](09-human-model-definition.md) provides
  a detailed overview of the HVE Human Model.

## Related Dialog Reference Pages

The individual Human Editor dialogs are documented in detail (verified against
current source code) in [`docs/manuals/07-humans/`](../../07-humans/README.md):

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
