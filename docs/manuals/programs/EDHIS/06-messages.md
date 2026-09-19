# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE, or by EDHIS. Some of the more common operating system messages are described in the HVE Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE are described in the HVE User's Manual, Appendix II.

Errors issued by EDHIS appear in the EDHIS output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results which are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDHIS are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE or operating system message by referring to the HVE Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC immediately with the offending error message and the input file that caused the error.

*(updated: this list has been checked against, and extended from, the messages carried by the current release. Messages 14–19 below are carried by the current release but were not listed in the original manual. Several entries are marked **not issued by the current release** — the text is still present in the program, but no condition in the current engine produces it. They are kept here so that a message seen in an older run can still be looked up.)*

---

**No Messages**

No messages were produced; no action is necessary.

---

***Integration Error*** *The simulation was terminated due to an integration error during initialization of the Runge-Kutta method because the integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: Velocity Convergence should be about 0.001 and Max Bisections should be about 10.*

(Level 1 - Fatal)

---

***Integration Error*** *The numerical integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: Velocity Convergence should be about 0.001 and Max Bisections should be about 10.*

(Level 1 - Fatal)

---

*The simulation was terminated during the initial timestep.*

(Level 1 - Fatal)

---

*The simulation was terminated because of a singular mass matrix in the equations of motion. Send your offending case to EDC for evaluation.*

(Level 1 - Fatal)

---

*The simulation was terminated in function Accel() because a joint angle exceeds the maximum allowed.*

(Level 2 - Diagnostic)

---

*The simulation was terminated in function Contact() because a problem was encountered calculating a human ellipsoid vs vehicle contact force.*

(Level 1 - Fatal)

---

*The simulation was terminated in function Belt() because a problem was encountered calculating a belt force.*

(Level 1 - Fatal)

---

*The simulation was terminated because a problem was encountered calculating an airbag force.*

(Level 1 - Fatal) *(updated: **not issued by the current release.** An airbag problem now produces one of the two airbag shut-off messages at the end of this chapter instead, and the run continues without the bag.)*

---

*The simulation was terminated because the selected integration timestep was too large. Reduce the value to 0.001 sec or less (Simulation Controls dialog, Human Collision Integration Timestep).*

(Level 1 - Fatal) *(updated: **not issued by the current release.** A timestep that is too large is now handled by the automatic halving described in [Chapter 4](04-calculation-method.md#numerical-integration); if it cannot be made to converge the run ends with an Integration Error instead.)*

---

*The simulation was terminated because the Get Surface Information terrain search failed.*

(Level 1 - Fatal) *(updated: **not issued by the current release**; not listed in the original manual either.)*

---

*The simulation terminated because an initial joint articulation angle was outside of the specified range of motion for the joint. (The range of motion is specified by the + and − joint stop angles in the HVE Human Editor.)*

(Level 3 - Informative)

---

***Integration Error*** *The velocity change for one integration timestep was greater than the user-entered maximum (see Simulation Controls dialog, Max Velocity Change). NOTE: This check may be turned off by setting Max Velocity Change equal to 0.0.*

(Level 1 - Fatal) *(updated: **not issued by the current release.** The Velocity Change Limit is still tested, but exceeding it halves the timestep and retries the step rather than terminating the run — see [Chapter 4](04-calculation-method.md#the-two-change-limits).)*

---

***Integration Error*** *The acceleration change for one integration timestep was greater than the user-entered maximum (see Simulation Controls dialog, Max Acceleration Change). NOTE: This check may be turned off by setting Max Acceleration Change equal to 0.0.*

(Level 1 - Fatal) *(updated: **not issued by the current release**, for the same reason as the message above — the limit halves the timestep rather than stopping the run.)*

---

*NOTE: The number of peaks exceeded the available number of peaks in the Injury Tolerance.*

(Informative) *(updated: present in current code; not listed in original manual)*

---

*Torso Restraint System Failure!*

(Informative — the torso belt force exceeded the belt breaking strength and the belt failed) *(updated: **not issued by the current release.** The text is present but no condition produces it. Exceeding the breaking strength now holds the tension at that value and unloads along the entered slope; the belt does not break. Check the belt tension in the Variable Output against the entered breaking strength to see whether the belt would have failed.)*

---

*Lap Restraint System Failure!*

(Informative — the lap belt force exceeded the belt breaking strength and the belt failed) *(updated: **not issued by the current release**, for the same reason as the message above.)*

---

*An Ellipsoid vs Contact Surface force exceeded the maximum allowable force.*

(Informative — the contact surface saturates and then unloads along the entered slope; see Contact Surface Maximum Force in Table 2-3) *(updated: **not issued by the current release.** The saturation and unloading still occur; only the message is silent, so compare the contact forces in the Variable Output against the entered maximum force to see which surfaces saturated.)*

---

*The airbag model was turned off because pressure became negative. Check the Vehicle Data Report (see Airbag) for more information.*

(Informative) *(updated: present in current code; not listed in original manual)*

---

*The airbag model was turned off because it became unstable. Check the Vehicle Data Report (see Airbag) for more information.*

(Informative) *(updated: present in current code; not listed in original manual)*

---
*Previous: [Chapter 5 — EDHIS Tutorial](05-tutorial.md) | Next: [Chapter 7 — References](07-references.md)*

<!-- NAV -->

---

← Previous: [Chapter 5 — EDHIS Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — References](07-references.md) →

<!-- /NAV -->
