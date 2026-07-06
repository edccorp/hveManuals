# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE-2D or HVE, or by EDSMAC4. Some of the more common operating system messages are described in the Appendix (of the User's Manual). A more thorough discussion of operating system messages may be found in the operating system manual. Messages produced by HVE-2D or HVE are described in the User's Manual, Appendix II.

Errors issued by EDSMAC4 appear in the EDSMAC4 output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDSMAC4 are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE-2D/HVE or operating system message by referring to the User's Manual Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC with the offending error.

*(updated: the message texts below have been checked against the current message resource, `Physics/Source/Edsmac4/EDSMAC4.rsc`. Where the current wording or limits differ from the original manual, the code value is given with an italic note. Messages new to the current version are listed at the end of this chapter.)*

---

**A CDC and clock direction of force were not computed for vehicle \*, damage range \***

*(Level 3 — Informative)*

If execution is halted by the user prior to the end of calculations, the damage tables may not be complete. The last damage calculation to be performed is the CDC (Collision Deformation Classification). If all the information necessary to produce the CDC is not available, this message is produced.

No response by the user is necessary.

---

**Analysis for a single vehicle without a collision**

*(Level 3 — Informative)*

This message indicates EDSMAC4 is being used as a single vehicle trajectory simulator.

No response by the user is necessary.

---

**An error occurred during the collision phase at t=\*.\*\* sec. because RHOBIT became negative.**

*(Level 1 — Fatal)*

During the collision phase, crush occurs along the vector, RHO, from the vehicle exterior towards the CG (refer to [Chapter 4 — Calculation Method](04-calculation-method.md)). RHOBIT refers to the adjusted length of RHOBI (the length of the current RHO vector) which accounts for restitution. This message indicates that, while seeking equilibrium of the RHO vector lengths for both vehicles, one of their lengths became negative. PSIB is the clock angle of the defective vector.

Since this error occurs during the iterative adjustment phase, reducing the value of DELRHO (see Calculation Options) may eliminate the problem. If you continue to experience the problem, send the offending input file to EDC for evaluation. *(The current version issues a related message when RHOBIC becomes negative after restitution calculations.)*

---

**An error occurred during the collision phase at t=\*.\*\* sec. because the damage range spanned more than half of Vehicle \*.**

*(Level 1 — Fatal)*

The damage range computed by EDSMAC4 spanned more than 180 degrees of the vehicle's outer surface. This error usually occurs in a very severe collision when the inter-vehicle forces go beyond the CG of one of the vehicles.

If the suspected damage did go beyond half of the vehicle's exterior, there is no correction for this error. The condition exceeds the capabilities of EDSMAC4. However, if the results are questionable, increasing the stiffness coefficient for the vehicle may improve the results (see the Vehicle Editor, Exterior Stiffness).

---

**An error occurred during the collision phase because the longitudinal and lateral components of damage were equal to zero.**

*(Level 1 — Fatal)*

Execution was halted due to an internal error associated with the angle of the damage vector used during the collision phase.

This is a mathematical error which should be prevented by the editing done by EDSMAC4 during the input session. Thus, if this error occurs, it is a symptom of another problem. Send the offending input file to EDC for evaluation.

---

**An error occurred during the collision phase because the damage increment was too coarse.**

*(Level 1 — Fatal)*

Execution was halted due to an excessive increment of damage. This error is sometimes caused by the proximity of the vehicles at impact, particularly if they are overlapping. In this case, the integration subroutine has failed to stabilize during the simulation.

Check to ensure the vehicles are not overlapping at impact; if necessary, separate the vehicles at their initial positions. This condition may also occur for some impact configurations when the angle between the RHO vectors for vehicle 1 and vehicle 2 approaches 90 degrees. A slight adjustment of impact positions may help to solve the problem.

---

**An error occurred during the collision phase. The damage region required too many collision vectors to span its entire width. To correct the error, increase DELPSI (see Calculation Options).**

*(Level 1 — Fatal)*

EDSMAC4 divides the damage region into a number of small, discrete angular intervals. The width of each interval is the user-entered value, DELPSI (see Calculation Options). If the value of DELPSI is too small, the number of intervals required to span the entire damage width becomes too large and the above error message is issued.

Increase the value of DELPSI (see Calculation Options). *(updated: the original manual stated a limit of 360 discrete intervals per damage region; the current message reads "the damage region required more than 100 collision vectors to span its width. To correct the error, try doubling the value of DELPSI.")*

---

**An error occurred during the collision phase at t=\*.\*\* sec. The difference in inter-vehicle contact pressure was greater than the user-entered maximum (ALAMB) after 200 bisections.**

*(Level 1 — Fatal)*

During the collision phase, force equilibrium is sought between each of the vehicle crush vectors using an iterative adjustment of the vector lengths, RHO. If, after the maximum number of adjustments (200 bisections in the current code), the force equilibrium is not reached (i.e., the difference in the inter-vehicle contact force is greater than the user-entered acceptable limit, ALAMB), the above error is issued.

Increase the value of ALAMB or decrease the value of DELRHO (see Calculation Options). *(updated: the original manual said "after 3200 bisections"; the current message resource says 200 and suggests "try halving the value of DELRHO or doubling the value of ALAMB.")*

---

**An error occurred while saving the acceleration or damage array maxima.**

*(Level 2 — Diagnostic)*

As the run progresses, a history of accelerations and damage severity (delta-V) is accumulated. Certain logical computations are performed to meet this need. If the resulting history creates a logical error, the above error is issued. *(current wording: "Only the first 10 acceleration peaks are stored. Additional peaks are ignored. The simulation results in Variable Output are not affected by this condition.")*

Save the offending input file and send it to EDC for evaluation.

---

**At the time execution was halted, vehicle \* was still moving.**

*(Level 3 — Informative)*

If either vehicle is still moving at the end of the simulation, whether halted as a result of an interruption by the user, or as a result of reaching the maximum simulation time, this message is issued to indicate that both vehicles have not reached their rest positions.

No response by the user is necessary.

---

**At the time execution was halted, both vehicles were still moving with the following velocities: ...**

*(Level 3 — Informative)*

If both vehicles are still moving at the end of the simulation, this message is issued (with a table of each vehicle's linear and angular velocity) to remind the user that the vehicles have not come to rest.

No response by the user is necessary.

---

**NOTE: The simulation was terminated due to excessive articulation angle between a tow vehicle and its trailer. This is normally a sign that a 'jackknife' occurred.**

*(Level 3 — Informative)*

EDSMAC4 does not calculate the forces and moments produced between the body of a tow vehicle and the body of its trailer. Therefore the simulation terminates when the current articulation angle exceeds the user-entered maximum (see Vehicle Editor, Connections).

---

**An error occurred while calculating a CDC for vehicle \*. The error code is \*\*.**

*(Level 2 — Diagnostic)*

EDSMAC4 divides the vehicle exterior into specific damage regions. Each region is associated with a certain location of damage defined by the CDC (Collision Deformation Classification), columns 3, 4, 5, and 6 (see SAE J224 MAR80 or the HVE Operations Manual, Damage Profiles). This message indicates a logical error has occurred while assigning the damage regions. The error codes and the affected CDC columns are listed below:

**Table 6-1: CDC Error Codes**

| Error Code | CDC Column |
|---|---|
| 41 – 43 | 3 |
| 44 – 45 | 4 |
| 46 | 3 |
| 47 – 50 | 4 |
| 51 | 3 |
| 52 – 55 | 4 |
| 56 | 3 |
| 57 – 59 | 4 |
| 60 – 62 | General error |
| 63 | 3 |
| 64 – 66 | General error |

General errors usually refer to computations of the damage width, column 6. Column 5 is always set equal to E, since all damage is assumed to occur uniformly below the belt line (see SAE J224 MAR80 for an explanation).

If you encounter this error, please document the error code and send the offending input file to EDC for evaluation.

---

**During the examination of individual damage ranges, no match was found for damage range no. \*.**

*(Level 2 — Diagnostic)*

During the collision phase, a clock direction of the PDOF is computed for each damage range. The angle at the midpoint of each damage range is also computed. If the angle of the PDOF is more than 60 degrees different from the associated damage midpoint, the above warning is issued.

This condition suggests a sideswipe collision occurred. It does not indicate any error in the results.

---

**Processing was interrupted by the user at t=\*.\*\* seconds.**

*(Level 3 — Informative)*

If the user terminates execution during processing, calculations will stop prior to reaching the termination velocities or maximum simulation time.

No response by the user is necessary.

---

**The collision resulted in more than 10 individual regions of vehicle damage. EDSMAC4 limits the analysis of the collision to 10 regions.**

*(Level 3 — Informative)*

Rapid rotation during the collision may result in subsequent inter-vehicle contact. EDSMAC4 allows up to ten individual ranges of impact damage. If more than ten individual damage regions are detected, only the first 10 ranges are stored; additional peaks are ignored. The simulation results in Variable Output are not affected by this condition.

---

**NOTE: The assigned value of Vehicle Force Tolerance, Alamb (see Calculation Options dialog), was increased to ensure solution stability. The new value of Alamb is assigned such that Alamb = Bstiff(max) \* DelRho. The new value is displayed in the Program Data report.**

*(Level 2 — Diagnostic)*

During the collision phase, inter-vehicle force balance between impacting vehicles is achieved through an incremental adjustment of each RHO vector. The amount of the adjustment is DelRho, a value assigned in the EDSMAC4 Calculation Options dialog. Because the adjustment is discrete, an exact balance of forces between RHO vectors will never be achieved. Therefore, a test is performed after each adjustment to determine if the force balance is within an allowable tolerance, Alamb, the value of which is also assigned in the EDSMAC4 Calculation Options dialog. If Alamb is too small, it is possible that a force balance between RHO vectors will never be achieved and the solution for collision force will fail to converge, resulting in a fatal error. To ensure solution stability, the value of Alamb is automatically assigned (see `AlambTest()` in `Scompute.cpp`).

---

**NOTE: The damage midpoint (PSIM) does not match the PDOF specified by the clock direction. This condition is fairly common for sideswipes and collisions involving secondary impact.**

*(Level 3 — Informative)*

As part of its post-processing routine, EDSMAC4 attempts to match a CDC with each vehicle damage range. The procedure for accomplishing this task is based on the assumption that the PDOF for each damage range will be approximately equal to the PSIM for that damage range. This is not normally the case for sideswipes and some collisions involving secondary impact. It is important to note that this message has no reflection on the integrity of the simulation.

---

**The simulation was terminated by the HVE Driver Model because the maneuver resulted in a lateral acceleration that exceeded the user-defined Driver Lateral Acceleration Comfort Level (see Driver Controls, HVE Path Follower dialog).**

*(Level 1 — Fatal)*

In order to complete the required maneuver, the user should increase the Driver Lateral Acceleration Comfort Level. However, this suggests the attempted maneuver is beyond the comfort level of the typical driver.

---

**The inter-vehicle connections for two connected vehicles have different elevations above ground.**

*(Level 1 — Fatal in the original version)*

The original manual instructed: to confirm the difference in connection heights, go to the Vehicle Editor and choose Move CG to obtain the static CG height (it is displayed as a positive value; however, it is negative with respect to the earth-fixed coordinate system), then choose Connections to obtain the connection z-coordinate. Do this for both vehicles (note that you'll use the rear connection for the tow vehicle and the front connection for the trailer). The connection elevation is −CG Height + Connection z-coordinate. Adjust the connection z-coordinate for either or both vehicles if you wish to make the connection elevations the same.

*(updated: the current version can reconcile the mismatch automatically. Unless the **Inter-Vehicle Connection** calculation option is set to Manual, EDSMAC4 adjusts the connection z-coordinate(s) at event initialization and issues the informative message: "NOTE: The vehicle-fixed connection z-coordinate was automatically calculated by EDSMAC4 to make the earth-fixed connection height equal on each tow vehicle/trailer pair. The updated connection z-coordinate is displayed in the Vehicle Data Report." See [EDSMAC4 Calculation Options](../../10-calculation-options/CalcOptEDSMAC4.md#inter-vehicle-connection).)*

---

## Additional messages in the current version

The following messages were added after the Sixth Edition manual was printed (message resource `Physics/Source/Edsmac4/EDSMAC4.rsc`, Msg23–Msg40):

- **Connection z-coordinate automatically calculated** (Informative) — See the note under the inter-vehicle connections message above.
- **Negative crush depth** (Informative) — "One or more vehicles has (have) a negative crush depth. Refer to the Damage Data report's Crush Depth Tables to identify the specific vehicle(s). This may be the result of a vehicle geometry with reversed surface normals or missing polygons. It may also be the result of normal folding of the damaged surface. Inspect the vehicle geometry for these conditions."
- **More than 10 impulses** (Informative) — "The collision resulted in more than 10 impulses on one or more vehicles. This does not result in event termination. However, only the first 10 impulses will be included in the CollisionData report and DamageStudio window."
- **Vehicle handling properties error** — "An error occurred while calculating vehicle handling properties."
- **Integration timesteps reduced for trailers** (Informative) — "The assigned integration timestep(s) (see Simulation Controls dialog) were too large for an event with trailers. In order to help ensure solution stability, one or more integration timestep values were reduced. The modified values are displayed in the Program Data output report."
- **Output interval large for a collision simulation** (Informative) — "The simulation output interval (see Simulation Controls dialog) is rather large for a collision simulation. Peak collision forces and/or accelerations may be filtered from Key Results and Variable Output. This issue has no effect on the overall accuracy of the simulated trajectories or damage profiles. To avoid this issue, reduce the output interval to 0.02 seconds (or less)."
- **HVE Driver Model steering rate exceeded** — "The HVE Driver Model predicted the maneuver required a steering wheel input rate that exceeded the user-defined Maximum Steering Velocity (see Driver Controls, HVE Path Follower dialog)."
- **HVE Driver Model turned off at impact** (Informative) — "The HVE Driver Model was turned off at impact for one or more vehicles because of a collision. The HVE Driver Model is not valid during or after impact."
- **Negative coefficient of restitution** (Warning) — "The coefficient of restitution is negative. This implies the striking vehicle traveled through the struck vehicle during impact. A negative restitution coefficient may also occur as a result of a large angular velocity (> 100 deg/sec) at separation, in which case this message may be ignored."
- **Coefficient of restitution greater than 1.0** (Warning) — "This implies the crash created energy. The normal range is ~0 to 0.25, perhaps slightly greater for low-speed impacts."
- **Coefficient of restitution larger than normal** (Informative) — "The normal range is ~0 to 0.25, perhaps slightly greater for low-speed impacts."
- **Closing velocity less than zero** (Error) — "The closing velocity is less than zero, indicating a calculation error has occurred. Two vehicles cannot collide if their closing velocity is less than zero."
- **Restitution not calculated for sustained contact** (Informative) — "The method used to calculate the coefficient of restitution in the Event Data output report (see INTER-VEHICLE COLLISION DATA) assumes an instantaneous impact. One or more collisions resulted in sustained contact (more than 0.5 seconds). A coefficient of restitution was not calculated for those collisions."
- **Increased tessellation required** (Error) — "Increased tessellation of the vehicle geometry is required when using the option to initialize the Rho Vector lengths using the vehicle geometry. Use the Set-up, Vehicle Mesh dialog for this purpose." (Issued when the **Use Vehicle Geometry for Rho Vector Init** calculation option is checked but the vehicle mesh is too coarse.)
- **MakeProfile() vertex index error** (Error) — "An error occurred in MakeProfile() because the vertex index was not within the damage table range."
- **Mesh dimensions differ from overall dimensions** (Informative) — "One or more vehicle(s) have mesh exterior dimensions that differ from the vehicle overall dimensions (CG to Front, CG to Back, CG to Right or CG to Left) by more than 0.5 inches (12.7 mm). As a result, the Damage Data output report for the affected vehicle(s) is subject to errors."
- **Collision in progress at termination** (Informative) — "At the time the simulation was terminated, one or more vehicles were still undergoing a collision. The CollisionData results (see Damage Data output report) are incomplete for the last recorded impulse."
- **Bad CDC** (Informative) — "One or more vehicles has a bad CDC (see Damage Data output report). This usually occurs while EDSMAC4 attempts to build the damage profile using the damaged vehicle geometry. There may be an insufficient number of damaged vertices to build the damage profile. Review the Damage Data report's Damage Width, Offset and Crush Depth table."

---
*Previous: [Chapter 5 — EDSMAC4 Tutorial](05-tutorial.md) — Next: [Chapter 7 — Technical References](07-references.md)*

<!-- NAV -->

---

← Previous: [Chapter 5 — EDSMAC4 Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-references.md) →

<!-- /NAV -->
