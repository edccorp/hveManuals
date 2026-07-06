# Chapter 6 — Messages

Messages can be issued by either the operating system, HVE, or by EDVDS. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual.

Messages produced by HVE are described in the HVE User's Manual, Appendix II.

Errors issued by EDVDS appear in the EDVDS output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results that are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, but provide information about execution, not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDVDS are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE or operating system message by referring to the HVE Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC with the offending error.

*(updated: this catalog has been verified against the current message resources in `Physics/Source/Edvds/EDVDS.rsc`. Messages 1–7 below appear in the original printed manual; messages 8–12 have been added to EDVDS since the Fourth Edition was printed and are documented here for completeness.)*

---

**Tire slip angle exceeded maximum value for linear tire. Run terminated!**

*(Level 1 - Fatal)*

This error occurs if the user selects the linear tire model (see Calculation Options), and the event includes a maneuver that results in significant lateral tire forces. If the tire slip angle exceeds a pre-defined limit for the linear tire model, normally 0.25 radians, the run terminates with this message.

To solve the problem the user must eliminate the cause of the lateral tire slip (normally substantial steering, often combined with braking), or change to a different tire model.

---

**Tire longitudinal slip exceeded maximum value for linear tire. Run terminated!**

*(Level 1 - Fatal)*

This error occurs if the user selects the linear tire model (see Calculation Options), and the event includes a maneuver that results in significant longitudinal tire forces. If the tire longitudinal slip exceeds a pre-defined limit for the linear tire model, normally 25 percent, the run terminates with this message.

To solve the problem the user must eliminate the cause of the longitudinal tire slip (normally substantial braking or accelerating), or change to a different tire model.

---

**The simulation was terminated because GetSurfaceInfo() failed to return a valid surface.**

*(Level 1 - Fatal)*

This message occurs if GetSurfaceInfo() failed to return a valid surface elevation. EDVDS should not return this condition; contact EDC if it occurs.

---

**The simulation was terminated because of an integration error. The numerical integration routine failed to converge to the specified Velocity Convergence Criterion after Maximum Bisections. These parameters are set in the Simulation Controls dialog. NOTE: The Velocity Convergence Criterion should be about 0.10 and Maximum Bisections should be about 10.**

*(Level 1 - Fatal)*

This condition indicates dynamic instability. Experience suggests if reasonable integration time steps and maximum bisections are used, this condition should not occur. If you confirm reasonable simulation controls are used and the condition still occurs, please contact EDC.

---

**The simulation was terminated because the user-specified maximum articulation angle between a tow vehicle and trailer was exceeded.**

*(Level 1 - Fatal)*

This message is self-explanatory. The maximum articulation angle is defined in the Rear Connections parameters (see Vehicle Editor). The value is established by the angle required to create pinching between the tow vehicle and trailer. Note that such pinching would cause forces not modeled by EDVDS, so the run is terminated.

---

**The simulation was terminated because the current deflection of a tire exceeded the user-specified Maximum Tire Deflection assigned for that tire. This problem can sometimes be solved by increasing slightly the Maximum Tire Deflection and/or reducing the Vehicle Trajectory Integration Timestep. This condition suggests that a wheel may have been broken during the event; EDVDS does not model failed wheel rims.**

*(Level 1 - Fatal)*

The first step in calculating tire forces is to calculate the radial tire force from the current tire deflection (the change in the tire rolling radius compared to an unloaded tire). If the deflection of a tire exceeds the user-specified Maximum Tire Deflection assigned for that tire the radial tire force could be substantial, leading to dynamic instability in the simulation. To prevent this from occurring, the run terminates.

This problem can sometimes be solved by increasing slightly the Maximum Tire Deflection (see Tire Physical Data parameters) and/or by reducing the Vehicle Trajectory Integration Timestep (see Simulation Controls). *(updated: the current message text additionally notes that this condition suggests a wheel may have been broken during the event, and that EDVDS does not model failed wheel rims.)*

---

**The simulation was terminated because of a singular matrix. This condition usually suggests a defective inertial matrix. Please send the offending case file to EDC for evaluation.**

*(Level 1 - Fatal)*

While solving the equations of motion, EDVDS creates a matrix of inertial parameters. To solve the equations, this matrix must be inverted. Not all matrices have an inverse and thus, cannot be inverted. However, for the types of equations solved by EDVDS, the matrix should be invertible. If a problem occurs first check to see that no inertial elements of the vehicle (sprung mass, axles, wheels) have been assigned a zero mass or rotational moment of inertia. If the problem persists, please send the offending case file to EDC for evaluation.

---

**The simulation was terminated because the current engine speed (RPM) was greater than the maximum RPM specified for the engine (see Vehicle Editor, Drivetrain Data, Engine Power/Torque Table).** *(added since the printed manual)*

*(Level 1 - Fatal)*

This problem might occur if the wheels leave the ground during a heavy throttle application; in this case the problem may be eliminated by reducing the throttle input (see Driver Controls, Throttle Table). The problem might also occur while driving in a low gear if the driver has a "lead foot."

---

**The simulation was terminated by the HVE Driver Model because the maneuver required a steering wheel input rate that exceeded the user-defined Maximum Steering Velocity (see HVE Path Follower dialog).** *(added since the printed manual)*

*(Level 1 - Fatal)*

The HVE Driver Model computed a steering wheel rate greater than the maximum rate the modeled driver is permitted to produce. Increase the Maximum Steering Velocity in the HVE Path Follower dialog, reduce the initial speed, or adjust the target path so the required steering input rate is achievable.

---

**The simulation was terminated by the HVE Driver Model because the maneuver resulted in a lateral acceleration that exceeded the user-defined Driver Lateral Acceleration Comfort Level (see HVE Path Follower dialog).** *(added since the printed manual)*

*(Level 1 - Fatal)*

The maneuver required by the target path produced a lateral acceleration greater than the comfort level assigned to the modeled driver. Increase the Driver Lateral Acceleration Comfort Level in the HVE Path Follower dialog, reduce the speed, or adjust the target path.

---

**NOTE: The inter-vehicle connections for two connected vehicles have different elevations above ground. This is not an error condition, but it is unusual. CG Height + Connection z-coord are normally about equal for both vehicles.** *(added since the printed manual)*

*(Level 3 - Informative)*

This informative message alerts the user that the earth-fixed heights of the mating connection points (e.g., fifth wheel and kingpin) differ between a tow vehicle and its trailer. Review the CG heights and connection z-coordinates for both vehicles to confirm the data are as intended.

---

**NOTE: The vehicle-fixed connection z-coordinate was automatically calculated to make the earth-fixed connection height equal on each tow vehicle/trailer pair. The updated connection z-coordinate is displayed in the Vehicle Data Report.** *(added since the printed manual)*

*(Level 3 - Informative)*

When the connection heights of a connected pair do not match, the physics program can automatically adjust the vehicle-fixed connection z-coordinate so the earth-fixed connection heights are equal. The adjusted value is reported in the Vehicle Data report; no user action is required unless the adjusted value is not as intended.

<!-- NAV -->

---

← Previous: [Chapter 5 — EDVDS Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — References](07-references.md) →

<!-- /NAV -->
