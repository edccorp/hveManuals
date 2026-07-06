# Section Six — Event Editor

An event is defined as a single analysis involving the interactions between
human(s), vehicle(s) and their environment. The purpose of the HVE Event
Editor is to study these interactions through the use of reconstruction and
simulation models. This section of the HVE User's Manual describes how to
set up and execute these reconstruction and simulation models. This section
also provides a detailed overview of all the event-related options available
to the user.

The basic physical/mathematical model of an event provides the following
information:

- **Event Inputs** (the humans, vehicles and environment)
- **Event Set-up Parameters** (the positions, velocities, driver controls
  and other event-related parameters for each human and vehicle)
- **Event Calculation Model** (the reconstruction or simulation model used
  for studying the interactions between the humans, vehicles and
  environment)
- **Event Outputs** (the results of execution)

## General Procedure

To use the Event Editor, perform the following steps:

1. Select Event mode.
2. Select the desired humans and/or vehicles.
3. Choose a reconstruction or simulation model to study the interactions
   between the selected humans and/or vehicles.
4. Set up the event:
   - Position the human(s) and/or vehicle(s) in the environment at one or
     more desired locations. For simulations, supply an initial velocity.
   - Provide any other set-up options (Payload, Driver Controls, Damage
     Profiles, Collision Pulse, Restraint Systems, Contacts).
5. Execute the event.
6. Edit the event (by adjusting positions, velocities, driver controls and
   other set-up options) and re-execute the event.

Repeat the above steps for any number of additional events.

## Overview of Section Six

This section provides a detailed explanation of the process of setting up
and executing events, and also presents detailed definitions for the
available event-related options:

- [Chapter 15 — Creating & Editing Events](15-creating-editing-events.md)
  describes the process of setting up and executing events.
- [Chapter 16 — Event Model Definition](16-event-model-definition.md)
  provides detailed definitions for the Event set-up options and outputs.

Code-verified dialog references for this section — including the current
Driver Controls dialogs (Pedal Force brake tables, Wide-open Throttle
tables, Ackermann steering, neuro-muscular filter and the HVE Driver
path/speed follower) — are collected in
[docs/manuals/09-events-driver-controls](../../09-events-driver-controls/README.md).

<!-- NAV -->

---

Next: [Chapter 15 — Creating & Editing Events](15-creating-editing-events.md) →

<!-- /NAV -->
