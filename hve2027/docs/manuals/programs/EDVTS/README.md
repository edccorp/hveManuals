# EDVTS — Vehicle-Trailer Simulator

**Engineering Dynamics Corporation Vehicle-Trailer Simulator, Version 7**

Updated Markdown edition, converted from the Sixth Edition (January 2006) printed manual and brought into line with the current HVE software (July 2026).

## EDVTS in HVE 2027

HVE 2027 compiles HVE's own EDVTS source, so the model described in this manual — the equations of motion, tire model, load transfer and messages — is the model HVE 2027 runs. On EDC's tutorial case (`EdvtsTutorialEDC.hve`) and validation cases, HVE 2027's runs reproduce the trajectories HVE saved in those files. The **[HVE]** passages of this manual apply to HVE 2027, which, like HVE, uses a 3-D environment. What differs is the user interface, and a short list of set-up details:

- **Selecting EDVTS.** In the **Event (F5)** editor, choose **EDVTS** in **Event Information › Calculation Method**. An EDVTS event has exactly two vehicles: slot V1 is the tow vehicle and V2 the trailer.
- **No Calculation Options dialog.** The roll couple distribution is the tow vehicle's front-axle **Roll Couple Dist** in **Vehicle › Suspension Data…**; the surface search is **Event Information › Road Surface Search**.
- **Trailer position.** The trailer's position is derived from the tow vehicle and the hitch; only its **Articulation** angle is entered.
- **Payload.** **Event › Payload…** is not available for EDVTS events in this version; a payload stored in an imported HVE case is used.
- **Connections.** Edited in the Vehicle editor (**Vehicles** panel › **Components** › **Connections…**). The hitch must be a matched pair at the same height above ground; HVE 2027 checks both before running.
- **Output.** A solved event plays back in the Event editor's own viewport (the **Playback** editor, F6, plays several events in sequence), and **Output › HVE Reports** shows the report pages EDVTS itself builds.

HVE-2D is not part of HVE 2027; read the **[HVE]** passages and ignore the HVE-2D ones. See also [Differences from HVE](../../getting-started/05-differences-from-hve.md).

## How to Use This Manual

This manual is the user's manual for the EDVTS simulation model. The manual describes the model features and use. Input parameters and output reports are described at a high level. This manual is intended to be used in conjunction with the HVE-2D or HVE User's Manual. The User's Manual provides in-depth coverage of the human, vehicle and environment models, as well as the Event Editor and Playback Editor. For specific model definitions, the user is referred to the User's Manual.

EDVTS is compatible with both HVE-2D and HVE. If you are using EDVTS within the HVE environment, the Human, Vehicle, and Environment Editors will have additional features that are not available in HVE-2D. These features are described in great detail in the HVE User's Manual. While some dialogs do look different, the required input for EDVTS is found in both. Where there are differences related to the use of EDVTS, these differences are noted in this manual. Information specific to HVE is designated with a **[HVE]** marker throughout this manual (grey background in the original printed edition).

## If You Have Questions

Engineering Dynamics Corporation provides technical assistance for supported users. The questions may relate to general usage or to specific engineering applications. When you call, you should have the following information available:

- Your user ID number
- Your System Hardware Profile report (available from EDC)
- HVE-2D or HVE Version Information (available from the HVE Help System)
- EDVTS Version Information (available from the EDVTS Program Data report)

!!! note "HVE 2027"
    EDC supports HVE and its physics programs. HVE 2027 is a separate program built from HVE's physics source; EDC does not support it, and the version and hardware-profile items above refer to HVE.

## Contents

1. [Chapter 1 — EDVTS Program Description](01-program-description.md)
2. [Chapter 2 — EDVTS Program Input](02-program-input.md)
3. [Chapter 3 — EDVTS Program Output](03-program-output.md)
4. [Chapter 4 — Calculation Method](04-calculation-method.md)
5. [Chapter 5 — EDVTS Tutorial](05-tutorial.md)
6. [Chapter 6 — Messages](06-messages.md)
7. [Chapter 7 — Technical References](07-technical-references.md)

*The printed manual's Chapter 8 (Index) is omitted; use text search in this Markdown edition.*

See also: [EDVTS Calculation Options](../../10-calculation-options/CalcOptEDVTS.md).

<!-- NAV -->

---

Next: [Chapter 1 — EDVTS Program Description](01-program-description.md) →

<!-- /NAV -->
