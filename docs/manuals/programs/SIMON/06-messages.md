# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE or SIMON. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE are described in the HVE User's Manual, Appendix II.

Messages issued by SIMON appear in the SIMON Messages output report and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by SIMON are listed below. Each message includes a description of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE or operating system message by referring to the HVE Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC with the offending error.

*(updated: this catalog is verified against the current message resource file, `Physics/Source/Simon/SIMON.rsc` (Msg1–Msg10, Msg21–Msg36). Messages present in the Fifth Edition manual are retained below with their original level designations; messages added since then are marked "(added)" and their level is inferred from the message prefix — WARNING/ERROR entries behave as diagnostics or fatal errors, NOTE entries are informative.)*

---

**Processing was interrupted by the user. At the time processing was interrupted, the vehicle(s) were still moving.** *(Level 3 — Informative; `Msg1`)*

This message is issued to indicate that at the time the user halted the simulation, at least one of the vehicles had not reached its rest position. No response by the user is necessary.

---

**The simulation was terminated because a unique solution for the coordinates of the tire-ground contact patch could not be calculated. Please send the offending case file to EDC for evaluation.** *(Level 1 — Fatal; `Msg2`)*

This message will be issued if a matrix describing the tire-ground contact patch is singular. This condition has never occurred in EDC's testing of SIMON. If you experience this problem, please contact EDC Technical Support.

---

**The simulation was terminated because the current deflection of a tire exceeded the user-specified Maximum Tire Deflection assigned for that tire.** *(Level 1 — Fatal; `Msg3`)*

A tire hit a tall curb or other significant elevation change (an elevation change greater than the maximum allowed tire deflection; see Vehicle Editor, Tire Physical Properties). This can also occur because of a defect (i.e., a hole) in the terrain beneath the tire. Carefully inspect the terrain beneath the tire. This condition also suggests that a wheel may have been broken during the event; SIMON does not model failed wheel rims.

The first step in calculating tire forces is to calculate the radial tire force from the current tire deflection (the change in the tire rolling radius compared to an unloaded tire). If the deflection of a tire exceeds the user-specified Maximum Tire Deflection assigned for that tire, the radial force could be substantial, leading to dynamic instability in the simulation. To prevent this from occurring, the run terminates.

This problem can sometimes be solved by increasing slightly the Maximum Tire Deflection (see Tire Physical Data parameters) and/or reducing the Vehicle Trajectory Integration Timestep (see Simulation Controls). *(updated: in the current resource file this message text is prefixed "WARNING:".)*

---

**The simulation was terminated due to an error in calculating the wheel spin acceleration. Check the tire spin inertia.** *(Level 1 — Fatal; `Msg4`)*

This message is issued when the wheel spin acceleration is so high that it causes a dynamic instability. If this occurs, try increasing tire spin inertia (see Vehicle Editor, Tire Physical Properties).

---

**The simulation was terminated because the current roll or pitch angle exceeded the allowable limit.** *(Fatal; `Msg5`, added)*

*(updated: this message is present in the current resource file but was not listed in the Fifth Edition manual. It indicates the vehicle attitude exceeded the model's allowable roll/pitch range.)*

---

**The simulation was terminated because the inertial matrix is singular. This condition usually suggests a defective inertial matrix. Please send the offending case file to EDC for evaluation.** *(Level 1 — Fatal; `Msg6`)*

The equations of motion are expressed in matrix form and solved by inverting the inertial matrix. A singular matrix cannot be inverted, so the equations of motion could not be solved. If this problem occurs, first check to see that no inertial elements of the vehicle (sprung mass, axles, wheels) have been assigned a zero mass or rotational moment of inertia. If the problem persists, please send your case file to EDC for evaluation.

---

**The simulation was terminated because the current engine speed (RPM) was greater than the maximum RPM specified for the engine (see Vehicle Editor, Drivetrain Data, Engine Power/Torque Table).** *(Level 1 — Fatal; `Msg7`)*

This problem might occur if the wheels leave the ground during a heavy throttle application; in this case the problem may be eliminated by reducing the throttle input (see Driver Controls, Throttle Table). The problem might also occur while driving in a low gear if the driver has a "lead foot." Engine RPM exceeded the highest value in the RPM vs. Power curve (see Drivetrain dialog). The solution is to shift into a higher gear.

---

**The HVE Driver Model predicted the maneuver required a steering wheel input rate that exceeded the user-defined Maximum Steering Velocity (see Driver Controls, HVE Path Follower dialog).** *(Level 2 — Diagnostic; `Msg8`)*

This diagnostic message alerts the user to the fact that the HVE Driver Model used a higher Maximum Steering Velocity than was specified in the Driver Controls, HVE Path Follower dialog. Steering Velocity as a function of time can be found in the Variable Output.

---

**The simulation was terminated by the HVE Driver Model because the maneuver resulted in a lateral acceleration that exceeded the user-defined Driver Lateral Acceleration Comfort Level (see Driver Controls, HVE Path Follower dialog).** *(Level 1 — Fatal; `Msg9`)*

In order to complete the required maneuver, the user should increase the Driver Lateral Acceleration Comfort Level (see Driver Controls, HVE Path Follower dialog). However, this suggests the attempted maneuver is beyond the comfort level of the typical driver.

---

**The simulation was terminated because GetSurfaceInfo() failed.** *(Level 1 — Fatal; `Msg10`)*

This message occurs if `GetSurfaceInfo()` failed to return a valid surface elevation. SIMON should not return this condition; contact EDC if it occurs.

---

**The simulation was terminated because the current articulation angle between a tow vehicle and its trailer exceeded the allowable range (see Vehicle Editor, Connections). This is normally the sign that a "Jackknife" has occurred.** *(Level 1 — Fatal; `Msg21`)*

This message is self-explanatory. The maximum articulation angle is defined in the Rear connections parameter (see Vehicle Editor). The value is established by the angle required to create pinching between the tow vehicle and trailer. Note that such pinching would cause forces modeled only by DyMESH, so the run terminates. *(updated: the current DyMESH Options dialog provides a Tow Vehicle / Trailer Contact option that enables mesh contact between connected vehicles; see Chapter 2.)*

---

**The simulation was terminated because a fatal error occurred while calculating derivatives (accelerations). This occurred due to excessively large forces or a general failure in the calculations that resulted in a non-numeric value. Please send the offending case file to EDC for evaluation.** *(Level 1 — Fatal; `Msg22`)*

This error should not occur. If it does, however, there is no easy solution for the user. Please send the case to EDC, where we can diagnose the cause of the problem.

---

**NOTE: The inter-vehicle connections for two connected vehicles have different elevations above ground. This is not an error condition, but it is unusual. CG Height + Connection z-coord are normally about equal for both vehicles.** *(Level 3 — Informative; `Msg23`)*

This message is self-explanatory. To confirm the difference in connection heights, go to the Vehicle Editor and choose Move CG to obtain the static CG height (it is displayed as a positive value; however, it is negative with respect to the earth-fixed coordinate system), then choose Connections to obtain the connection z-coordinate. Do this for both vehicles (note that you'll use the rear connection for the tow vehicle and the front connection for the trailer). The connection elevation is −CG Height + Connection z-coordinate. Adjust the connection z-coordinate for either or both vehicles if you wish to make the connection elevations the same.

---

## Messages Added Since the Fifth Edition

*(updated: the following messages exist in the current `SIMON.rsc` but were not documented in the Fifth Edition manual. Most relate to the DyMESH collision model and damage/restitution reporting.)*

---

**NOTE: One or more vehicles has (have) a negative crush depth.** *(Informative; `Msg24`, added)*

Refer to the Damage Data report's Crush Depth Tables to identify the specific vehicle(s). This may be the result of a vehicle geometry with reversed surface normals or missing polygons. It may also be the result of normal folding of the damaged surface. Inspect the vehicle geometry for these conditions.

---

**NOTE: The collision resulted in more than 10 impulses on one or more vehicles.** *(Informative; `Msg25`, added)*

This does not result in event termination. However, only the first 10 impulses will be included in the CollisionData report and DamageStudio window.

---

**An error occurred while calculating vehicle handling properties.** *(Diagnostic; `Msg26`, added)*

---

**NOTE: The simulation output interval (see Simulation Controls dialog) is rather large for a collision simulation.** *(Informative; `Msg27`, added)*

Peak collision forces and/or accelerations may be filtered from Key Results and Variable Output. This issue has no effect on the overall accuracy of the simulated trajectories or damage profiles. To avoid this issue, reduce the output interval to 0.02 seconds (or less).

---

**NOTE: At the time the simulation was terminated, one or more vehicles were still undergoing a collision.** *(Informative; `Msg28`, added)*

The CollisionData results (see Damage Data output report) are incomplete for the last recorded impulse.

---

**NOTE: One or more vehicles has a bad CDC (see Damage Data output report).** *(Informative; `Msg29`, added)*

This usually occurs while SIMON attempts to build the damage profile using the damaged vehicle geometry. There may be an insufficient number of damaged vertices to build the damage profile. Review the Damage Data report's Damage Width, Offset and Crush Depth tables.

---

**WARNING: The coefficient of restitution is negative.** *(Diagnostic; `Msg30`, added)*

This implies the striking vehicle traveled through the struck vehicle during impact. A negative restitution coefficient may also occur as a result of a large angular velocity (> 100 deg/sec) at separation, in which case this message may be ignored.

---

**WARNING: The coefficient of restitution is greater than 1.0.** *(Diagnostic; `Msg31`, added)*

This implies the crash created energy. The normal range is approximately 0 to 0.25, perhaps slightly greater for low-speed impacts.

---

**NOTE: The coefficient of restitution is larger than normally associated with vehicle collisions.** *(Informative; `Msg32`, added)*

The normal range is approximately 0 to 0.25, perhaps slightly greater for low-speed impacts.

---

**ERROR: The closing velocity is less than zero, indicating a calculation error has occurred.** *(Diagnostic; `Msg33`, added)*

Two vehicles cannot collide if their closing velocity is less than zero.

---

**NOTE: The method used to calculate the coefficient of restitution in the Event Data output report (see INTER-VEHICLE COLLISION DATA) assumes an instantaneous impact.** *(Informative; `Msg34`, added)*

One or more collisions resulted in sustained contact (more than 0.5 seconds). A coefficient of restitution was not calculated for those collisions.

---

**NOTE: One or more vehicles has (have) a manual transmission that is not in gear, but has the throttle applied.** *(Informative; `Msg35`, added)*

This is like revving the engine in neutral. Is this the intent?

---

**NOTE: The HVE Driver Model was turned off at impact for one or more vehicles because of a collision.** *(Informative; `Msg36`, added)*

The HVE Driver Model is not valid during or after impact.

<!-- NAV -->

---

← Previous: [Chapter 5 — SIMON Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-technical-references.md) →

<!-- /NAV -->
