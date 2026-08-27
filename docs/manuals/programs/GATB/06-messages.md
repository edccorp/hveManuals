# Chapter 6 — Messages

*(This chapter was marked "to be added" in the printed Fifth Edition manual. The catalog below lists only the messages that a GATB event can raise, with the message code and the text as HVE displays it. The message catalog is shared across the HVE simulation models, so a given installation may show additional codes that do not apply to GATB.)*

GATB reports problems in two ways:

- **Event Termination / Fatal Errors** — the simulation cannot continue and stops. These are shown as a dialog and are also written to the **Message** output report (see [Chapter 3, Program Output](03-program-output.md)).
- **Warnings** — a possible inconsistency was detected but the run continues. You may inspect these and choose to accept them.

The verbosity of the Message report is governed by the diagnostic level set in the HVE user options (Fatal Errors only; Fatal Errors + Diagnostics; Fatal Errors + Diagnostics + Informative).

## GATB event set-up and termination messages

These are the codes GATB can report while setting up or running an event, together with the message text displayed for each.

| Code | Type | Message text |
|---|---|---|
| -6800 | Fatal | Event Termination: No Vehicle Position(s) Assigned! |
| -6810 | Fatal | Event Termination: No Vehicle Velocity(ies) Assigned! |
| -6820 | Fatal | Event Termination: No Human Position(s) Assigned! |
| -6830 | Fatal | Event Termination: No Human Velocity(ies) Assigned! |
| -6530 | Fatal | Event Termination: Bad Human vs Vehicle Contact Force |
| -6500 | Fatal | Event Termination: Excessive Joint Articulation Angle |
| -6510 | Fatal | Event Termination: Too Many Human Ellipsoids |
| -6520 | Fatal | Event Termination: Too Many Vehicle Contact Surfaces |
| -6700 | Fatal | Event Termination: Error in Derivative Calculations (excessive force). Try reducing integration timestep. |
| -6710 | Fatal | Event Termination: Singular Matrix (Bad News!) |
| -6182 | Fatal | Event Termination: Entered initial position is illegal |

**Notes on the common GATB messages:**

- **No Human Position / No Human Velocity** — Every human in the event must have an initial position and (if the Velocity is Assigned box is checked) a velocity. Return to Set-up → Position/Velocity for each human. See the Tutorial for the correct procedure.
- **No Vehicle Position / No Vehicle Velocity** — Same requirement for each vehicle carrying the collision pulse.
- **Bad Human vs Vehicle Contact Force** — Usually indicates a human ellipsoid that starts deeply embedded in a contact panel (for example, feet driven into the floor), producing a very large restoring force. Re-establish an initial equilibrium (Tutorial, "Establishing initial equilibrium") so that all segment accelerations are small before applying the crash pulse.
- **Excessive Joint Articulation Angle** — A joint has been driven past its allowable range of motion. Check the initial limb angles and the joint stop/torque data.
- **Too Many Human Ellipsoids / Too Many Vehicle Contact Surfaces** — The number of active contact ellipsoids or contact surfaces has exceeded the ATB model's internal limits. Reduce the number of designated contact interactions (Set-up → Contacts): specify only the ellipsoid-vs-surface pairs that are physically relevant rather than Select All. (Recall each human has 15 segments with up to 3 contact ellipsoids per segment — see [Chapter 2](02-program-input.md).)
- **Error in Derivative Calculations / Singular Matrix** — Numerical instability, typically from excessive forces or too large a time step. Reduce the integration time step or correct the offending contact/joint data.

## Vehicle-model warnings that can appear during a GATB event

Because a GATB event carries a vehicle (for the collision pulse and contact geometry), the shared vehicle-model messages may also appear. Those most relevant to GATB users:

| Code | Type | Message text |
|---|---|---|
| -6000 | Info | Done. |
| -6010 | Info | Simulation Interrupted By User |
| -6030 | Info | Maximum Simulation Time Reached |
| -6600 | Fatal | Event Termination: Excessive Inter-vehicle Articulation Angle |
| -6870 | Warning | Warning: The output interval is rather large for a collision simulation. Important collision pulse data may be missing. See Messages output report. |

> **NOTE:** As illustrated in the Tutorial, GATB may warn that an angular (e.g. yaw) acceleration is higher than normal when a collision pulse derived from EDSMAC4 is applied. These are informational and may be accepted.

For the complete HVE physics message catalog (all codes and their text), see the HVE Operations Manual, Appendix II (Messages).

<!-- NAV -->

---

← Previous: [Chapter 5 — Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-references.md) →

<!-- /NAV -->
