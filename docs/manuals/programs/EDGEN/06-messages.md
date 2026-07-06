# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE or HVE-2D, or by EDGEN. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE or HVE-2D are described in the User's Manual, Appendix II.

Errors issued by EDGEN appear in the EDGEN output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results which are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDGEN are listed below. Each message is followed by the level of the message (*Informative, Diagnostic* or *Fatal*), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE/HVE-2D or operating system message by referring to Appendix II (Messages) or your computer's operating system manual. If the message is not listed in either place, please contact EDC immediately with the offending error message and the input file that caused the error.

*(All message texts below verified against the current source, `Physics/Source/Edgen/EDGEN.rsc`.)*

---

*No Messages*

No messages were produced; no action is necessary.

---

*The event was terminated at t=0.0 sec because fewer than two positions were entered. EDGEN requires at least two positions (up to eight are allowed).*

**(Level 1 - Fatal)**

To solve the above problem, enter at least two positions for the human or vehicle.

---

*The simulation was terminated because the user assigned a zero velocity for two consecutive positions. EDGEN requires a non-zero velocity for at least one of the positions.*

**(Level 1 - Fatal)**

To solve the problem, identify which two consecutive positions have a zero velocity and enter a non-zero velocity.

---

*The simulation was terminated because the user assigned identical X,Y,Z coordinates for two consecutive positions. EDGEN requires the object's X,Y,Z coordinates be edited for at least one of the positions.*

**(Level 1 - Fatal)**

To solve the problem, identify which two consecutive positions have the same X,Y,Z coordinates and change the X,Y,Z coordinates for either position.

---

*The simulation was terminated before the object reached its final position because the velocity dropped below its user-assigned termination velocity.*

**(Level 3 - Informative)**

No action is necessary; the object simply stopped moving. However, you may choose to enter a zero (or very small) termination linear velocity if you need to simulate a slow-moving object.

---

*The simulation was terminated by the user before the object reached its final position.*

**(Level 3 - Informative)**

No action is necessary. This message simply explains why the Accident History report may not show results for one or more user-defined positions.

<!-- NAV -->

---

← Previous: [Chapter 5 — EDGEN Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-references.md) →

<!-- /NAV -->
