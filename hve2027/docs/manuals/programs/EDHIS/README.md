# EDHIS — Human Impact Simulator

**Engineering Dynamics Corporation Human Impact Simulator, Version 3**

Updated Markdown edition, converted from the Fifth Edition manual (January 2006) and revised to match the current HVE release.

## EDHIS in HVE 2027

HVE 2027 compiles EDC's own EDHIS source, so the model this manual describes — the three-segment, twelve-degree-of-freedom occupant, its contact, belt and airbag models and its integrator — is HVE's. What differs is the program around it:

- **Running EDHIS.** Choose *EDHIS* as the event's **Calculation Method** in Event Information (Event editor, F5), then **Run** on the playback bar or **Output › Run Simulation**. There is no separate program to start: the solved event plays back in the same viewport, and reports, graphs and tables are on the **Output** menu.
- **Where the inputs are.** The body is edited in the **Human (F2)** editor (**Occupant › Human Information** opens the *Occupants* panel); belts, airbags and contact surfaces are vehicle equipment (**Vehicle (F3)** menu); which humans take part, where they sit, what they wear and how they are posed are set per event in **Event Information › Humans in Event**. [Chapter 2](02-program-input.md) gives the full map.
- **Restraint type and pose are per event.** The same occupant can be belted in one event and not in another, and posed differently in each.
- **Airbag inflation defaults are HVE's own**: Begin Fill Time 0.001 s and Fill Duration 0.05 s.
- **A pedestrian's walking speed is an input.** It is read from the case (or entered in Body Pose) and reaches the engine; an occupant's initial velocity is relative to the vehicle and is normally zero.
- **Contacts.** **Event › Contacts** chooses which body segments are armed against which vehicle surfaces. A case opened from an HVE `.hve` file keeps HVE's own list of armed ellipsoid/surface pairs; a case built in HVE 2027 arms every body ellipsoid EDHIS uses against every contact surface of the vehicle until you edit the list.
- **Validation status.** On HVE's EDHIS tutorial case the seated occupant reproduces HVE's saved run over the whole event. The pedestrian event matches to t = 0.14 s and then depends on the human integration step, in HVE's run as in ours.

!!! note "HVE 2027"
    HVE 2027 opens HVE's own `.hve` case files, including the EDHIS tutorial case `EdhisTutorialEDC.hve` used in [Chapter 5](05-tutorial.md). It does not write `.hve`; save as `.hvc` or `.json`.

## How to Use This Manual

This manual is the user's manual for the EDHIS simulation model. It describes the model's features and use. Input parameters and output reports are described at a high level. It is intended to be used in conjunction with the HVE User's Manual, which provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and the output of a run. For specific model definitions, the user is referred to the rest of this manual set (for the human, the [Humans pages](../../07-humans/README.md)).

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. When you call, have available: your user ID number, your System Hardware Profile report, HVE Version Information (HVE Help System), and EDHIS Version Information (EDHIS Program Data report).

!!! note "HVE 2027"
    The System Hardware Profile report and the HVE Help System are HVE's. In HVE 2027 the program version is under **Help › About HVE 2027**, and the EDHIS version number is printed on the *Program Data* page of **Output › HVE Reports** after a run.

## Contents

- [1 — EDHIS Program Description](01-program-description.md)
- [2 — EDHIS Program Input](02-program-input.md)
- [3 — EDHIS Program Output](03-program-output.md)
- [4 — Calculation Method](04-calculation-method.md)
- [5 — EDHIS Tutorial](05-tutorial.md)
- [6 — Messages](06-messages.md)
- [7 — References](07-references.md)

*The original manual's Chapter 8 (Index) is omitted; use text search in this Markdown edition instead.*

Related reference pages:

- [EDHIS Calculation Options](../../10-calculation-options/CalcOptionsEDHIS.md)
- [Humans (HVE Human Editor)](../../07-humans/Human.md)

<!-- NAV -->

---

Next: [Chapter 1 — EDHIS Program Description](01-program-description.md) →

<!-- /NAV -->
