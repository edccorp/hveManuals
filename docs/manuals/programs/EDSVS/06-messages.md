# Chapter 6 — EDSVS Messages

Messages can be issued by either the operating system, HVE-2D or HVE, or by EDSVS. Some of the more common operating system messages are described in the Appendix of the HVE-2D or HVE User's Manual. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE-2D or HVE are described in the User's Manual, Appendix II.

Errors issued by EDSVS appear in the EDSVS output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDSVS are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE-2D, HVE or operating system message by referring to the User's Manual Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC with the offending error.

*(updated: The message catalog below has been verified against the current source, `Physics/Source/Edsvs/EDSVS.rsc`. The current catalog contains exactly these four messages (`Msg1`–`Msg4`); no messages have been added or removed since the Sixth Edition, and all of the current messages are Level 1 (Fatal) run-termination messages — the Diagnostic and Informative levels are defined but presently unused by EDSVS.)*

## Message Catalog

### Wheel Lift-off

> *The simulation was terminated because a wheel lifted off the ground. For more information, check the Variable Output Table to see where Fz (Wheel Number) became negative.*

**(Level 1 — Fatal)**

This message occurs when EDSVS calculates a negative vertical tire load, Fz. EDSVS is a quasi-2D analysis and cannot handle the condition where a wheel leaves the ground. This condition occurs during hard cornering maneuvers or extremely hard braking, normally coupled with a relatively high center of gravity. This condition might also occur at the start of the simulation if the event begins under extremely dynamic conditions, such as high sideslip or angular velocity.

### Excessive Roll or Pitch Angle

> *The simulation was terminated because the current roll or pitch angle exceeded 15 degrees. EDSVS is a quasi-3-D analysis. The small angle assumption is used.*

**(Level 1 — Fatal)**

**HVE:** This message applies to the 3-D terrain capability available in the HVE environment.

This message occurs when the vehicle travels over a surface with a significant slope. At each timestep, EDSVS uses GetSurfaceInfo() to determine the current roll and pitch angles. If either of these angles exceeds the allowable value, the run terminates. The termination reflects the fact that the small angle assumption is used, and the error may become significant.

### GetSurfaceInfo Failure

> *The simulation was terminated because GetSurfaceInfo() failed.*

**(Level 1 — Fatal)**

This message occurs if GetSurfaceInfo() failed to return a valid surface elevation. EDSVS should not return this condition; contact EDC if it occurs.

*(updated: The surface search method used by GetSurfaceInfo() is now selected in the separate Get Surface Information Options dialog, not the EDSVS Calculation Options dialog; the By Elevation method is not supported. See the [EDSVS Calculation Options reference](../../10-calculation-options/CalcOptEDSVS.md).)*

### Integration Error

> *The simulation was terminated due to an integration error. The numerical integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: Velocity Convergence should be about 0.1 and Max Bisections should be about 10.*

**(Level 1 — Fatal)**

This condition indicates dynamic instability. Experience suggests if reasonable integration timesteps and maximum bisections are used, this condition should not occur. If you confirm reasonable simulation controls are used and the condition still occurs, please contact EDC.

---

Previous: [Chapter 5 — EDSVS Tutorial](05-tutorial.md) | Next: [Chapter 7 — Technical References](07-technical-references.md) | [Contents](README.md)

<!-- NAV -->

---

← Previous: [Chapter 5 — EDSVS Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-technical-references.md) →

<!-- /NAV -->
