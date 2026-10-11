# GATB — Graphical Articulated Total Body

**Collision Engineering Associates, Inc. — Version 5.56**

Updated Markdown edition, converted from the Fifth Edition manual (December 2013; manual printed December 30, 2013) and revised to match the behavior of the current HVE release.

Copyright Collision Engineering Associates, Inc. 1999. All rights reserved.

> Collision Engineering Associates, Inc.
> P.O. Box 31900
> Mesa, Arizona 85275-1900 USA
> phone (480) 655-0399 — fax (480) 655-0693
> e-mail wgrimes@cea-az.com

*GATB is a trademark of Collision Engineering Associates, Inc. All rights reserved. SGI, GL, Inventor and IRIX are trademarks of Silicon Graphics, Inc. X-Windows and Motif are trademarks of MIT. UNIX is a trademark of Unix International. HVE is a trademark of Engineering Dynamics Corporation. The HVE 9-cell matrix cube is a trademark of Engineering Dynamics Corporation.*

## GATB in HVE 2027

!!! note "HVE 2027"
    **HVE 2027's GATB is a C++ port of ATB.** HVE's GATB extracts the case into an ATB input deck (`gatb.ain`) and runs the ATB Fortran program on it. HVE 2027 compiles HVE's own GATB front end — the code that turns the human, vehicle and event into ATB's input — but the ATB solver it calls is a line-by-line C++ translation of the ATB-V.1 Fortran, fed from memory: no input deck is written or read and no Fortran runtime is needed. The original Fortran builds only as an optional *oracle* that the port is checked against, routine by routine; the two give the same answer. Everything this manual says about the physics is therefore ATB's, as in HVE.

    GATB is part of HVE 2027: a GATB event runs like any other.

What else is different in HVE 2027:

- **Running GATB.** Choose *GATB* as the event's **Calculation Method** in Event Information (Event editor, F5), then **Run** on the playback bar or **Output › Run Simulation**. There is no Playback Editor: the solved event plays back in the same viewport, and reports, graphs and tables are on the **Output** menu.
- **Where the inputs are.** The body is edited in the **Human (F2)** editor (**Occupant › Human Information** opens the *Occupants* panel, whose bodies are generated with GEBOD); belts, airbags and contact surfaces are vehicle equipment (**Vehicle (F3)** menu); which humans take part, where they sit, what they wear and how they are posed are set per event in **Event Information › Humans in Event**. [Chapter 2](02-program-input.md) gives the full map.
- **The ATB time step is fixed at 0.002 s**, as in HVE: GATB writes it itself and does not read the Simulation panel's steps.
- **Belt webbing**: GATB gives ATB its own fixed webbing stress/strain curve, as HVE's GATB does, so the belt *Stiffness*, *Damping* and *Break Strength* (which EDHIS reads) do not change a GATB run.
- **"Use external ATB input file" is not available** (greyed in the GATB options, with the reason): ATB is fed from the assembled data in memory, so an external `GATB.ain` cannot reach the solver.
- **Self contact**: only each segment's first ellipsoid takes part in segment-to-segment contact, exactly as in HVE's GATB; HVE 2027 reports any armed pair that names another ellipsoid.
- **Restraint type and pose are per event**, and a **pedestrian's walking speed** reaches GATB.
- **Airbag inflation defaults are HVE's own**: Begin Fill Time 0.001 s, Fill Duration 0.05 s.
- **Contacts.** **Event › Contacts** chooses which body segments are armed against which vehicle surfaces, and the body-to-body (self contact) pairs. A case opened from an HVE `.hve` file keeps HVE's own lists, including contact blocks against other vehicles, which are shown read-only; a case built in HVE 2027 arms every body ellipsoid against every contact surface until you edit the list.
- **Validation status.** On HVE's own saved GATB runs, the belted occupant of `ExpeditionTrip-WDG2.hve` and the unbelted driver of `GATB.hve` are reproduced on every segment; a pedestrian's late tumbling is chaotic in HVE and here alike, so it is compared only up to the first limb strike.

## License Summary

The original manual includes the Collision Engineering Associates, Inc. License Agreement, Software License, Limited Warranty and Trademarks sections. In brief: one copy of the software may be used on a single computer; the software may not be rented, leased, reverse engineered, decompiled or disassembled; the software is warranted for 90 days; CEA disclaims all other warranties and consequential damages; the agreement is governed by the laws of the State of Arizona.

## How to Use This Manual

This manual is the user's manual for the GATB simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE Operations Manual. The HVE Operations Manual provides in-depth coverage of the human, vehicle and environment models, as well as the HVE Event Editor and Playback Editor. For specific model definitions, the user is referred to the HVE Operations Manual (see also the [Humans](../../07-humans/README.md) section of the Dialog Reference).

## If You Have Questions

!!! note "HVE 2027"
    The support arrangements below are those of GATB in HVE. In HVE 2027 the program version is under **Help › About HVE 2027**, and the GATB version is printed on the *Program Data* page of **Output › HVE Reports** after a run.

Collision Engineering Associates, Inc. provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. When you call, you should have the following information available:

- Your user ID number
- HVE Version Information (available from the HVE Help System)
- GATB Version Information

## Contents

- [1 — Program Description](01-program-description.md)
- [2 — Program Input](02-program-input.md)
- [3 — Program Output](03-program-output.md)
- [4 — Calculation Method](04-calculation-method.md)
- [5 — Tutorial](05-tutorial.md)
- [6 — Messages](06-messages.md)
- [7 — Technical References](07-references.md)
- [GEBOD Data Pages](08-gebod-data-pages.md)

*(The original Chapter 8, Index, is omitted from this edition — Markdown files are text-searchable.)*

<!-- NAV -->

---

Next: [Chapter 1 — Program Description](01-program-description.md) →

<!-- /NAV -->
