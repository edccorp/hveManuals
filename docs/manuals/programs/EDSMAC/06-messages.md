# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE-2D or by EDSMAC. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE-2D are described in the User's Manual, Appendix II.

Errors issued by EDSMAC appear in the EDSMAC output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDSMAC are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE-2D or operating system message by referring to the User's Manual Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC immediately with the offending error.

---

> *NOTE: A CDC and clock direction were not computed for vehicle 1.*
>
> *NOTE: A CDC and clock direction were not computed for vehicle 2.*

**(Level 3 — Informative)**

If execution is halted by the user prior to the end of calculations, the damage tables may not be complete. The last damage calculation to be performed is the CDC (Collision Deformation Classification). If all the information necessary to produce the CDC is not available, this message is produced.

No response by the user is necessary.

---

> *ERROR: An error occurred during the collision phase because RHOBIC became negative after restitution calculations.*

**(Level 1 — Fatal)**

During the collision phase, crush occurs along the vector, RHO, from the vehicle exterior towards the CG (refer to Chapter 4, Calculation Method). RHOBIC refers to the adjusted length of RHOBI (the length of the current RHO vector) which accounts for restitution. This message indicates that, while seeking equilibrium of the RHO vector lengths for both vehicles, one of their lengths became negative. PSIB is the clock angle of the defective vector.

Since this error occurs during the iterative adjustment phase, reducing the value of DELRHO (see Calculation Options) may eliminate the problem. If you continue to experience the problem, send the offending input file to EDC for evaluation.

---

> *ERROR: An error occurred during the collision phase because RHOBIT became negative.*

**(Level 1 — Fatal)**

During the collision phase, crush occurs along the vector, RHO, from the vehicle exterior towards the CG (refer to Chapter 4, Calculation Method). RHOBIT refers to the initial length of a RHO vector, computed from the vehicle's exterior dimensions before the restitution adjustment begins. This message indicates that the initial length of one of these vectors was zero or negative, which points to inconsistent or invalid vehicle exterior dimensions rather than a failure during the iterative adjustment phase.

Unlike the RHOBIC message above (which is issued when a vector length becomes negative *during* the restitution calculations), this error occurs at the outset of the collision phase. Check the vehicle exterior geometry for the reported vehicle. If the dimensions appear correct, send the offending input file to EDC for evaluation.

---

> *ERROR: An error occurred during the collision phase because the damage range spanned more than half the vehicle. If the damage spanned more than half the vehicle's exterior, the collision is beyond the scope of EDSMAC.*

**(Level 1 — Fatal)**

The damage range computed by EDSMAC spanned more than 180 degrees of vehicle \*'s outer surface. This error usually occurs in a very severe collision when the inter-vehicle forces go beyond the CG of one of the vehicles.

If the suspected damage did go beyond half of the vehicle's exterior, there is no correction for this error. The condition exceeds the capabilities of EDSMAC. However, if the results are questionable, increasing the stiffness coefficient for the vehicle may improve the results. (See Calculation Options.)

---

> *ERROR: An error occurred during the collision phase because the longitudinal and lateral components of damage were both equal to zero.*

**(Level 1 — Fatal)**

Execution was halted due to an internal error associated with the angle of the damage vector used during the collision phase.

This is a mathematical error which should be prevented by the editing done by EDSMAC during the input session. Thus, if this error occurs, it is a symptom of another problem. Send the offending input file to EDC for evaluation.

---

> *ERROR: An error occurred during the collision phase because the damage increment was too coarse.*

**(Level 1 — Fatal)**

Execution was halted due to an excessive increment of damage. This error is sometimes caused by the proximity of the vehicles at impact, particularly if they are overlapping. In this case, the integration subroutine has failed to stabilize during the simulation.

Check to ensure the vehicles are not overlapping at impact; if necessary, separate the vehicles at their initial positions.

This condition may also occur for some impact configurations when the angle between the RHO vectors for vehicle 1 and vehicle 2 approach 90 degrees. A slight adjustment of impact positions may help to solve the problem.

---

> *ERROR: An error occurred during the collision phase because the damage region required more than 100 collision vectors to span its width. To correct the error, try doubling the value of DELPSI (EDSMAC Program Options).*

**(Level 1 — Fatal)**

EDSMAC divides the damage region into a number of small, discrete angular intervals. Up to 100 discrete intervals are allowed for each damage region. The width of each interval is the user-entered value, DELPSI (see Calculation Model). If the value of DELPSI is too small, the number of intervals required to span the entire damage width will exceed 100 and the above error message is issued.

Increase the value of DELPSI (see Calculation Options).

---

> *ERROR: An error occurred during the collision phase because the difference in inter-vehicle contact pressure was greater than the user-entered maximum value of ALAMB after 200 bisections. To correct the error, try halving the value of DELRHO or doubling the value of ALAMB (EDSMAC Program Options).*

**(Level 1 — Fatal)**

During the collision phase, force equilibrium is sought between each of the vehicle crush vectors using an iterative adjustment of the vector lengths, RHO. Up to 200 adjustments are allowed. If, after 200 adjustments, the force equilibrium is not reached (i.e., the difference in the inter-vehicle contact force is greater than the user-entered acceptable limit, ALAMB), the above error is issued.

Increase the value of ALAMB or decrease the value of DELRHO (see Calculation Options).

---

> *At the time processing was interrupted, the vehicle(s) were still moving (see Accident History).*

**(Level 3 — Informative)**

If either vehicle is still moving at the end of the simulation, whether halted as a result of an interruption by the user, or as a result of reaching the maximum simulation time, this message is issued to indicate that both vehicles have not reached their rest positions.

No response by the user is necessary.

---

> *Processing was interrupted by the user.*

**(Level 3 — Informative)**

If the user terminates execution during processing, calculations will stop prior to reaching the termination velocities or maximum simulation time.

No response by the user is necessary.

---

> *NOTE: The collision resulted in more than 10 individual ranges. Only the first 10 ranges are stored. Additional peaks are ignored. The simulation results in Variable Output are not affected by this condition.*
>
> *NOTE: An error occurred while saving the acceleration or damage array maxima. Only the first 10 acceleration peaks are stored. Additional peaks are ignored. The simulation results in Variable Output are not affected by this condition.*

**(Level 3 — Informative)**

Rapid rotation during the collision may result in subsequent inter-vehicle contact. EDSMAC allows up to ten individual ranges of impact damage. If more than ten individual damage regions are detected, the analysis is beyond the scope of EDSMAC and the above error message is issued.

---

> *NOTE: The damage midpoint (PSIM) does not match the PDOF specified by the clock direction. This condition is fairly common for sideswipes and collisions involving secondary impact.*

**(Level 3 — Informative)**

During the collision phase, a clock direction of the PDOF is computed for each vehicle damage range. The angle at the midpoint of each damage range is also computed (see PSIM, Summary of Damage Ranges output report). If the angle of the PDOF is more than 60 degrees different from the associated damage midpoint, the above message is issued. This message reflects a failure in an EDSMAC post-processing routine; the simulation results are still valid.

---

> *NOTE: An error occurred while calculating column 3 or 4 of the CDC.*

**(Level 2 — Diagnostic)**

EDSMAC divides the vehicle exterior into specific damage regions. Each region is associated with a location of damage defined by the Collision Deformation Classification (CDC; see SAE J224 [8]). This message indicates a logical error occurred while assigning the 3rd or 4th character of the CDC. Please send the HVE case file to EDC for evaluation.

This message reflects a failure in an EDSMAC post-processing routine; the simulation results are still valid.

---

> *NOTE: A general error occurred while calculating the CDC. Please send the offending event to EDC for evaluation.*

**(Level 2 — Diagnostic)**

EDSMAC divides the vehicle exterior into specific damage regions. Each region is associated with a location of damage defined by the Collision Deformation Classification (CDC; see SAE J224 [8]). This message indicates a logical error occurred while assigning one or more characters of the CDC. Please send the HVE case file to EDC for evaluation.

This message reflects a failure in an EDSMAC post-processing routine; the simulation results are still valid.

---

[Previous: Chapter 5 — EDSMAC Tutorial](05-tutorial.md) | [Next: Chapter 7 — Technical References](07-technical-references.md)

<!-- NAV -->

---

← Previous: [Chapter 5 — EDSMAC Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-technical-references.md) →

<!-- /NAV -->
