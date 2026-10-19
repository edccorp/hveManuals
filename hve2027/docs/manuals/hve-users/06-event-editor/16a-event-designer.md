# Chapter 16a — Event Designer

The Event Designer is the Vehicle Designer's frame turned on the event: a stage
bar along the bottom, a **Key figures** strip on the left that remembers what
each number was, the event's own dialogs hosted on the stage that asks their
question, and a **Warnings & Suggestions** panel on the right whose rows name the
fix and the stage that owns it. Open it with **Event › Event Designer...** in the
Event editor (F5), where it is the first item.

Like the Environment Designer, with **Fill the window** on it takes the left of
the editor's work area and leaves the 3-D view on the right, where the vehicles
stand. Off, it is a window of its own size. A dialog on a stage is the same
dialog the Event menu opens, drawn in the stage instead of its own window, so a
field has one editor and nothing is reachable in one and not the other.

![Figure 16a-1](../images/hvn-06-event-designer.png)

*Figure 16a-1: The Event Designer on its Event stage, with Event Information
hosted and the 3-D view beside it.*

## The stages

1. **Event**: the **Event Information** panel: the events, the active event's
   name and start time, the calculation method and its options, the vehicles and
   humans in the event, and their initial conditions.
2. **Positions**: **Position / Velocity** for the vehicle chosen in its own
   **Vehicle** picker, which is the same selection as the 3-D view's.
3. **Driver Controls**: **Driver Controls** (throttle, brake, steer and gear
   against time) for the chosen vehicle.
4. **Collision**: a tab for each dialog the calculation method reads, as the
   Event menu greys the rest: **Collision Pulse**, **DyMESH Options**, **Vehicle
   Mesh**, **Contacts** (EDSMAC4's vehicle contacts, or EDHIS and GATB's occupant
   contacts) and **Crush Profile**. For EDCRASH, **Damage Profiles (Event stage)**
   opens Event Information's Vehicle Impact Setup on the Event stage.
5. **Equipment**: the same for what each vehicle carries and does: **Payload**,
   **Path Follower**, **Lights**, **Wheels**, **Accelerometers**, **Airbags**,
   **Belt Restraint**, and for EDSMAC and EDSMAC4 **Handling Parameters** and
   **Move CG**. The restraint tabs edit the occupant slot the Occupants panel has
   selected.
6. **Run**: **Run this event** starts the active event on the current physics,
   exactly as the Simulation panel's **Run** does, with **Cancel** while it runs.
   A solved event is locked until **Reset Run to Edit** in Event Information, and
   the stage says so. Fix warnings do not stop a run; the stage counts them.
7. **Summary**: the event's spec sheet with its was column, **Set as baseline**
   (kept for this case across sessions) and **Copy spec sheet**, the warnings,
   and the event's **Notes**.

Every item of the Event menu has a place on a stage. The one exception is
**Impact Plane / Barrier...**, which this port does not implement (model a
barrier as a Fixed Barrier vehicle). Each tab is the dialog the Event menu
opens, drawn in the stage, for the vehicle chosen in its own **Vehicle** picker.

## Key figures

The vehicles and humans in the active event; its duration and output step (--
when the event leaves them to the Simulation panel); the first and second
vehicles' start speeds; the distance between their CGs at the start; their
closing speed (positive when the gap shrinks); and when their CGs would meet at
those speeds.

## Warnings & Suggestions

| Grade | Stage | Rule |
|---|---|---|
| Fix | Event | The case has no event. |
| Fix | Event | The active event has no vehicle and no human. |
| Fix | Positions | Two of the event's vehicles start with their CGs closer than 1.5 m, so their bodies overlap at t = 0 (not EDCRASH, which states impact positions). |
| Consider | Event | SIMON, EDSMAC or EDSMAC4: at their start speeds the first two vehicles touch (CG gap less 5 m for the two bodies) after the run has ended. |
| Note | Positions | SIMON, EDSMAC or EDSMAC4: the first two vehicles' gap is not shrinking at the start, so they meet only if a driver input turns one toward the other. |
| Consider | Event | SIMON, EDSMAC or EDSMAC4 with two vehicles: the output step is over 0.02 s, a few samples through an impact at most. |
| Note | Driver Controls | SIMON: every vehicle starts at rest with no throttle, so the stopped-vehicle rule ends the run at 0.1 s. |

A rule that lacks its input stays silent, and the count beside the panel's
title lists what is checked on hover.
