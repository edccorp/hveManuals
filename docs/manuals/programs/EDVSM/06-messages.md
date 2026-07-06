# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE, or by EDVSM. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE are described in the HVE User's Manual, Appendix II.

Errors issued by EDVSM appear in the EDVSM output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results which are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDVSM are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE or operating system message by referring to the HVE Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC immediately with the offending error.

*(updated: This catalog has been verified against the current EDVSM message resources in `Physics/Source/Edvsm/EDVSM.rsc` (messages Msg1–Msg15). All messages from the original manual are still present. One message has been added since the Fifth Edition — the second Integration Error, concerning the Velocity Convergence Criterion — and the GetSurfaceInfo() Error text has been shortened; both are noted below.)*

---

### No Messages

This is the result of normal termination. No action by the user is necessary.

---

### \*\*\* Integration Error \*\*\* The simulation was terminated because of an integration error in the tire force calculations.

*(Level 1 - Fatal)*

This error occurs due to an error in the wheel spin equations of motion. The error suggests an excessive spin acceleration. This might result from excessive drive or brake torque or from an incorrect (small) wheel spin inertia. Confirm the wheel torques in the Key Results or Variable Output. Confirm the spin acceleration in the Vehicle Data output report.

---

### \*\*\* Integration Error \*\*\* The simulation was terminated due to an integration error. The numerical integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: Velocity Convergence should be about 0.1 and Max Bisections should be about 10.

*(Level 1 - Fatal)*

*(updated: This message was added after the Fifth Edition of the manual; it is present in the current message resources.)* It is issued when the integrator's velocity-convergence check cannot satisfy the user-assigned Velocity Convergence Criterion within the assigned Maximum Number of Bisections. (Note that EDVSM runs the Fixed Runge-Kutta integrator; the velocity-convergence bisection path applies only to the variable-timestep Adams-Moulton integrator.) Restore these Simulation Controls parameters to values near their defaults (Velocity Convergence approximately 0.1, Maximum Bisections approximately 10).

---

### \*\*\* Suspension Force Error \*\*\* The simulation was terminated because of a singular matrix in the suspension force equations. Send the offending case to EDC for evaluation.

*(Level 1 - Fatal)*

This error occurs due to excessive suspension force. This can be the result of an excessive integration timestep (see Simulation Controls, Trajectory Timestep). The problem might also occur during an excessively dynamic maneuver (such as crashing into the ground after falling several hundred feet). This type of event is beyond the scope of the EDVSM simulation model as it would probably result in catastrophic damage to the vehicle structure.

---

### \*\*\* Excessive Tire Force Error \*\*\* The simulation was terminated because an excessive tire deflection was encountered. A tire hit a tall curb or other significant elevation change (an elevation change greater than the maximum allowed tire deflection; see Vehicle Editor, Tire Physical Properties). If the elevation change is not instantaneous, reducing the integration timestep may solve the problem.

*(Level 1 - Fatal)*

The EDVSM tire model assumes a point contact between the tire and road. As the terrain elevation changes, the tire does not roll onto a curb or similar surface, rather it changes the contact point in a single timestep. This can result in an instantaneous tire deflection greater than the section height of the tire. Note that this also occurs in real events — causing rim damage and/or tire failure. This is beyond the scope of the EDVSM tire model. The user should understand the complexity of simulating rim failure. In general, such a simulation would require a non-linear finite element analysis.

---

### \*\*\* Singular Matrix Error \*\*\* The simulation was terminated because of a singular matrix in the sprung mass equations. Send your offending case to EDC for evaluation.

*(Level 1 - Fatal)*

This message indicates errant data, probably zero mass or rotational inertia for the sprung mass. Such a condition is normally prevented by the range checking that occurs in the HVE Vehicle Editor. However, a defective vehicle data file could also cause this problem. Carefully review the vehicle data report for suspicious data.

---

### \*\*\* Excessive Roll or Pitch \*\*\* The simulation was terminated by function Tmcnst() because the current roll or pitch angle exceeded the allowable limit.

*(Level 1 - Fatal)*

This is a debugging message and is not enabled in the production release of EDVSM.

---

### \*\*\* Derivative Error \*\*\* The simulation was terminated in function Tmcnst() because the current derivatives (accelerations) are too large. This usually indicates an excessive or unexpected force was applied to the vehicle sprung mass.

*(Level 1 - Fatal)*

This message is issued when the vehicle axis indexing scheme fails, normally the result of a sudden, large acceleration. The cause may be related to excessive tire and/or suspension forces. Check the Key Results or Variable Output report for the current tire and suspension results for a sudden and excessive force at one or more wheel locations.

---

### \*\*\* Radial Tire Model Error \*\*\* The simulation was terminated in the radial tire model because the number of deflection increments was too large.

*(Level 1 - Fatal)*

The Radial Tire Model is not implemented in this version of EDVSM. Thus, this message will not occur. *(updated: confirmed — the current physics rejects the Radial Spring tire model option; see the [EDVSM Calculation Options reference](../../10-calculation-options/CalcOptEDVSM.md).)*

---

### \*\*\* Excessive Integration Timestep \*\*\* The simulation was terminated because the selected integration timestep was too large. Reduce the value to 0.01 sec or less (Simulation Controls dialog).

*(Level 1 - Fatal)*

This message is self-explanatory. EDVSM uses the Trajectory Integration Timestep in the Simulation Controls dialog. The default value is 0.0025 sec.

---

### \*\*\* Excessive Vehicle Roll \*\*\* The simulation was terminated by function VsmMain() because the current roll angle exceeded the allowable limit.

*(Level 1 - Fatal)*

This is a debugging message and is not enabled in the production release of EDVSM.

---

### \*\*\* GetSurfaceInfo() Error \*\*\* The simulation was terminated because GetSurfaceInfo() failed.

*(Level 1 - Fatal)*

This is a debugging message and is not enabled in the production release of EDVSM. *(updated: the original manual quoted this message as "...because GetSurfaceInfo() failed to return a valid surface description."; the current resource text is shortened to "...because GetSurfaceInfo() failed.")*

---

### \*\*\* Excessive Engine Speed \*\*\* The simulation was terminated because the current engine speed (RPM) was greater than the maximum RPM specified for the engine (see Vehicle Editor, Drivetrain Data, Engine Power/Torque Table). This problem might occur if the wheels leave the ground during a heavy throttle application; in this case the problem may be eliminated by reducing the throttle input (see Driver Controls, Throttle Table). The problem might also occur while driving in a low gear if the driver has a 'lead foot'.

*(Level 1 - Fatal)*

If the vehicle is in gear (as determined by the Driver Controls, Gear Table), the current engine speed is calculated. The current engine speed must not exceed the maximum engine speed in the Drivetrain Data. The current engine speed is available in the Key Results or Variable Output report (see Drivetrain output group). A possible cause of this error is starting a vehicle in first gear at a speed of, say, 50 mph.

---

### \*\*\* No Terrain Exists Error \*\*\* The simulation was terminated because no terrain exists beneath the vehicle and a rollover is under way. To continue the rollover simulation, ensure that a terrain exists beneath the vehicle. Also, make sure the terrain has no small holes in it.

*(Level 1 - Fatal)*

If the rollover model is enabled, EDVSM searches the entire environment 3-D geometry for the terrain properties beneath each vehicle vertex. This message is issued when no terrain is found beneath a vertex. Although it may appear that a surface exists, it can sometimes be difficult to see small holes in the surface. Try zooming in for a closer inspection.

---

### \*\*\* Driver Model Error \*\*\* The simulation was terminated by the HVE Driver Model because the maneuver required a steering wheel input rate that exceeded the user-defined Maximum Steering Velocity (see HVE Path Follower dialog).

*(Level 1 - Fatal)*

The HVE Driver Model calculates the current steer velocity. If this value is greater than the allowable, the simulation is terminated. The error can be eliminated by increasing the user-defined Maximum Steer Velocity. However, the user should also consider the driver's ability when assigning this data.

---

### \*\*\* Driver Model Error \*\*\* The simulation was terminated by the HVE Driver Model because the maneuver resulted in a lateral acceleration that exceeded the user-defined Driver Lateral Acceleration Comfort Level (see HVE Path Follower dialog).

*(Level 1 - Fatal)*

The current lateral acceleration calculated by EDVSM is compared with the user-defined Driver Comfort Level (which is expressed as a lateral acceleration). If the current lateral acceleration is greater than the user-defined maximum, the simulation is terminated.

Note that the default value of Comfort Level is 0.4 g. This is not to be confused with vehicle/driver capability, which is much greater. The Comfort Level is a human factors issue and varies from driver to driver.

<!-- NAV -->

---

← Previous: [Chapter 5 — EDVSM Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — References](07-references.md) →

<!-- /NAV -->
