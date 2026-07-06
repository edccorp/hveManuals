# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE-2D or HVE, or by EDVTS. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE-2D or HVE are described in the User's Manual, Appendix II.

Errors issued by EDVTS appear in the EDVTS output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDVTS are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE-2D or operating system message by referring to the User's Manual Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC with the offending error.

*(updated: The message catalog below was verified against the current EDVTS message resources in `Physics/Source/Edvts/EDVTS.rsc`. The six messages from the printed manual — Msg1 through Msg6 — are unchanged. One message, Msg7, has been added since the printed edition; it is documented at the end of this chapter.)*

---

*The simulation was terminated because a wheel lifted off the ground. For more information, check the Variable Output Table to see where Fz (Wheel Number) became negative.*

**(Level 1 - Fatal)**

This message occurs when EDVTS calculates a negative vertical tire load, Fz. EDVTS is a quasi-2D analysis and cannot handle the condition where a wheel leaves the ground. This condition occurs during hard cornering maneuvers or extremely hard braking, normally coupled with a relatively high center of gravity. This condition might also occur at the start of the simulation if the event begins under extremely dynamic conditions, such as high sideslip or angular velocity.

---

*The simulation was terminated because the current roll or pitch angle exceeded 15 degrees. EDVTS is a quasi-3-D analysis. The small angle assumption is used.*

**(Level 1 - Fatal)**

This message occurs when the vehicle travels over a surface with a significant slope. At each timestep, EDVTS uses GetSurfaceInfo() to determine the current roll and pitch angles. If either of these angles exceeds the allowable value, the run terminates. The termination reflects the fact that the small angle assumption is used, and the error may become significant.

---

*The simulation was terminated because GetSurfaceInfo() failed.*

**(Level 1 - Fatal)**

This message occurs if GetSurfaceInfo() failed to return a valid surface elevation. EDVTS should not return this condition; contact EDC if it occurs.

---

*The simulation was terminated due to an integration error. The numerical integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: Velocity Convergence should be about 0.1 and Max Bisections should be about 10.*

**(Level 1 - Fatal)**

This condition indicates dynamic instability. Experience suggests if reasonable integration timesteps and maximum bisections are used, this condition should not occur. If you confirm reasonable simulation controls are used and the condition still occurs, please contact EDC.

---

*The simulation was terminated because the current articulation angle exceeded the allowable limit defined for the tow vehicle.*

**(Level 1 - Fatal)**

This message is self-explanatory. The maximum articulation angle is defined in the Rear connections parameters (see Vehicle Editor). The value is established by the angle required to create pinching between the tow vehicle and trailer. Note that such pinching would cause forces not modeled by EDVTS, so the run is terminated.

---

*The simulation terminated because of a failure in the simultaneous solutions routine. The matrix is singular. Send your offending case to EDC for evaluation.*

**(Level 1 - Fatal)**

The equations of motion are expressed in matrix form and solved by inverting the matrix. A singular matrix cannot be inverted, so the equations of motion could not be solved. This condition has never occurred for EDVTS; if it occurs in your case, please send your case file to EDC for evaluation.

---

*NOTE: The vehicle-fixed connection z-coordinate was automatically calculated to make the earth-fixed connection height equal on each tow vehicle/trailer pair. The updated connection z-coordinate is displayed in the Vehicle Data Report.*

**(Level 3 - Informative)**

*(updated: This message was added after the printed edition; it does not appear in the Sixth Edition manual.)* This message is issued during input processing when EDVTS automatically adjusts the vehicle-fixed connection z-coordinate so that the earth-fixed heights of the hitch connection on the tow vehicle and the trailer coincide. No action is required; the adjusted value can be reviewed in the Vehicle Data output report. *(Note: the current message resource text attributes the calculation to "EDSMAC4"; this is a leftover from a shared resource template — in an EDVTS event the adjustment is performed by EDVTS itself.)*

---

[Previous: Chapter 5 — EDVTS Tutorial](05-tutorial.md) | [Contents](README.md) | [Next: Chapter 7 — Technical References](07-technical-references.md)

<!-- NAV -->

---

← Previous: [Chapter 5 — EDVTS Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-technical-references.md) →

<!-- /NAV -->
