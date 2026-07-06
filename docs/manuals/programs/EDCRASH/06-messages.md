# Chapter 6 — Messages

Messages may be issued by the operating system, HVE-2D or HVE, or by EDCRASH. Some of the more common operating system messages are described in the Appendix. A more thorough discussion of operating system messages may be found in the operating system manual. Messages produced by HVE-2D or HVE are described in the User's Manual, Appendix II.

Errors issued by EDCRASH appear in the EDCRASH output and may be one of three types:

- **Fatal Messages (Level 1)** — These messages halt execution and are caused by the program's inability to continue the calculation procedure based on intermediate results which are inconsistent or incompatible with basic program assumptions.
- **Diagnostic Messages (Level 2)** — These messages do not halt execution, but are the result of the internal consistency checks performed by the program and suggest inconsistencies in the results of which the user should be aware. These inconsistencies may be the result of bad or suspicious data.
- **Informative Messages (Level 3)** — These messages do not halt execution, and provide information about execution not affecting accuracy, but suggestive of something the user may want to review to ensure data were as intended.

All messages issued by EDCRASH are listed below. Each message includes a description or nature of the cause, the level of the message (Informative, Diagnostic or Fatal), and the recommended action to eliminate the problem. If you receive an error message not listed below, first check to see if it is an HVE-2D or operating system message by referring to the HVE-2D Appendix or your computer's operating system manual. If the message is not listed in either place, please contact EDC immediately with the offending error message and the case file that caused the error.

---

## COMMON VELOCITY WARNING

> *An adjustment of vehicle separation velocities was performed in order to be consistent with the assumption that the contact interface reached a common velocity. The adjustment did not exceed 10 percent.*

**(Level 2 — Diagnostic)**

The separation velocity of each vehicle is computed independently, based totally on user-entered data. The damage-based calculations require the velocity at the damage centroids for each vehicle to be equal (the CG velocities may not be equal). If the user-entered data results in a small discrepancy (up to 10%), the separation velocities are adjusted and the above message is issued.

No response by the user is necessary. However, refer to the information below (COMMON VELOCITY ERROR) for data affecting this message.

---

## COMMON VELOCITY ERROR

> \*\*\* COMMON VELOCITY ERROR \*\*\* *The vehicle contact interface failed to reach a common velocity, based on user-supplied data for impact-to-rest path length and rolling resistance. Impact Speed calculations were not performed.*

**(Level 1 — Fatal)**

The earth-fixed velocity at the damage centroid is computed for each vehicle separately, based on user-entered scene data and the PDOF. If this velocity differs between vehicles by more than allowed (typically 10 percent), an adjustment of the separation conditions is performed (see Common Velocity Warning, above). For collinear collisions, if, after this adjustment, the velocities at the damage centroid still differ by more than 10 percent, the common velocity assumption cannot be satisfied and EDCRASH aborts.

**What To Do:**

1. Check first to see that all accident site path data (impact, rest, EOR and POC) were entered correctly. Make sure that you entered the heading angles correctly. Then see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics.
2. Scrutinize the path data. Is it possible the impact positions and headings or the rest positions and headings were not what you thought? Were there pre-impact sideslip angles? Was there an EOR that you did not enter? Was the POC valid? Are you sure about the rotation direction? Scrutinize your path data.
3. Scrutinize the Wheel Data. Check the tire/road friction. Were the wheels really locked? Free rolling? In between? (If so, how did you arrive at your entries?) Scrutinize your Wheel Data.
4. Scrutinize the PDOFs. Is it possible they were greater (or less) than the values you entered? Try entering a range of possible values, checking the effect on your results. Scrutinize your PDOFs.
5. Finally, make sure the collision was not a sideswipe collision, which violates the common velocity assumption (see Assumptions).

---

## Newton's Third Law Warning

> *WARNING: Damage-based estimates for Magnitude of Principal Force grossly violate Newton's Third Law of motion. Review the output to determine required corrections to Damage Data and adjust as necessary. The Magnitudes of Principal Force should be approximately equal.*

**(Level 3 — Informative)**

An analysis of the vehicle damage data is performed using CDC-generated data or user-entered damage dimensions. This analysis results in the damage-based Delta-V, the energy absorbed by damage and the magnitude of the principal force. This fact serves as an excellent check on the validity of the damage-based results. If the results are reasonable, then the independently-calculated forces should be approximately equal as well. If these forces differ by more than allowed (typically 100 percent), the above message is displayed.

**What To Do:**

1. Check to see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics.
2. Scrutinize the Damage Data. Check the damage dimensions (width, crush depths, and damage offset) to be sure they were accurately measured. Remember to include induced damage, especially for narrow impact widths (less than 16 inches). Scrutinize your Damage Data.
3. Scrutinize the PDOFs. If scene data were entered, you may be able to compare the PDOF with the angle of the impulse (see PDOF Compatibility warning message). Remember: as the PDOF angle decreases (becomes less perpendicular) to the damaged surface, the Magnitude of Principal Force increases. Scrutinize your PDOFs (see Energy Magnification Factor).
4. Scrutinize the Crush Stiffness Coefficients. Default data are assigned according to the selected vehicle, but may be changed by the user. The Crush Stiffness coefficients are the result of test data [22]. Higher coefficients increase the Magnitude of Principal Force; the coefficients may be higher than assigned by the Stiffness Category if the damage region was primarily in a stiff region, such as a wheel or frame area. Lower coefficients decrease the Magnitude of Principal Force; the coefficients may be lower than assigned by the Stiffness Category if the damage region was primarily in a soft region, such as a fender or grill (above the bumper) area.

---

## SPINOUT ERROR

> \*\*\* SPINOUT ERROR DETECTED \*\*\* *The position and heading entered for the end of rotation or rest of the vehicle, and/or the specified direction of rotation are not compatible with the submitted rolling resistances and the total path length from separation to rest. User should carefully review this physical evidence for adjustment and rerun.*
>
> - Relative error figure =
> - Wheel lock-up =
> - Sep. to EOR path length =
> - Sep. to EOR heading change =
> - EOR to rest path length =

**(Level 1 — Fatal)**

A negative (−) relative error figure indicates the vehicle had insufficient separation velocity to reach the specified rest position given the rolling resistance; a positive (+) figure indicates the vehicle translated an insufficient distance for the specified rotation from separation to rest.

This message will only result if the rotating/lateral skidding option was selected (see Program Input, Setting Up an Event; Wheel Data). This option calculates the separation velocities using the empirical method developed by McHenry (see references 2, 15 and 16). If the results of the empirical calculations conflict with the laws of motion, the above message is issued and EDCRASH aborts.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Use the Graphics.
2. Use the Relative Error Figure. Compare the value shown in the present run with the next run to see if your adjustments had a positive effect. If the relative error figure is negative, the vehicle had insufficient velocity at separation to reach the rest position given the EOR-to-rest path length; an adjustment in the correct direction will make this figure closer to zero. If the relative error figure is positive, the separation-to-EOR path length is probably too short to allow the indicated heading change to take place.
3. Scrutinize the Path Data. Is it possible the impact positions and headings or the rest positions and headings were not what you think they were? Were there pre-impact sideslip angles? Was there an EOR that you did not enter? Was the EOR entered accurately? Was the POC valid? Are you sure about the direction of rotation? Scrutinize your Path Data.
4. Scrutinize the Wheel Data. Check the tire/road friction. Were the wheels really locked? Free rolling? In between? (If so, how did you arrive at your entries?) Scrutinize your Wheel Data.

---

## Separation Velocity Warning

> *WARNING: The separation velocity of the striking vehicle is greater than the separation velocity of the struck vehicle along a line between the vehicle CGs.*

**(Level 3 — Informative)**

This condition implies the striking vehicle is driving through the struck vehicle after the impact! This is obviously not possible within the assumptions of the program (especially that the vehicle does not break into two pieces!).

The coefficient of restitution should be positive. Check this value. The value will increase (i.e., become positive) by reducing the separation velocity of the striking vehicle or increasing the separation velocity of the struck vehicle.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Use the Graphics.
2. Scrutinize the path data. Even though the graphics shows the data were entered properly, is it possible that any of the path data are off by a few feet? Try modifying these parameters to identify how they affect the coefficient of restitution.
3. Scrutinize the rolling resistances and friction coefficients. Are the percent lock-ups assigned correctly? Have you assigned a higher coefficient of friction for the striking vehicle? Try modifying these parameters to identify how they affect the coefficient of restitution (it should be a small positive number).

---

## Point-on-Curve Warning

> *WARNING: User-entered Point-on-Curve was discarded because the position was practically on a straight line between impact and rest or it was too far away from other path coordinates to make sense. If the post-impact path was curved and your Point-on-Curve was rejected, the results may be erroneous. Check your data.*

**(Level 2 — Diagnostic)**

EDCRASH checks the validity of a point on curve if one is entered. Two conditions are possible which will cause it to be rejected: if the point on curve is on a straight line, or if the point on curve is outside of the smallest possible circle connecting the impact and rest (or EOR) positions. In the former case, there is no problem; the message serves only to remind the user why the point on curve is not displayed in the output listing. In the latter case, the results may be substantially affected. This is particularly true if the separation angle determined by the circular arc defined by the point on curve is substantially different from the separation angle determined by the straight line between impact and rest (or EOR) positions.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Use the Graphics.
2. Scrutinize the POC. Check to see if the POC is on a straight line between impact and rest positions (this should not occur if you are using a site drawing as a tool for analysis). If the point is not on a straight line, check the possible range of points on curve using a compass to draw the smallest circle connecting the impact and rest (or EOR) positions. The point on curve must lie within the circle. Scrutinize your POC.

---

## PDOF Adjustment Warning

> *WARNING: User-entered Principal Directions of Force have been adjusted to be 180 degrees apart.*

**(Level 3 — Informative)**

This message serves only as a reminder that the PDOFs were adjusted. No response by the user is necessary. However, if the adjusted values are not correct, use the Damage Profile dialog to re-enter either or both vehicles' PDOFs.

---

## Sideslip Angle Adjustment Warning

> *WARNING: User-entered sideslip angle BETA was adjusted for compatibility with components of separation velocity and specified Principal Direction of Force. If adjusted value of BETA is not consistent with available physical evidence, basis of PDOF should be reviewed for possible adjustment and rerun.*

**(Level 3 — Informative)**

The user-entered pre-impact sideslip angle BETA may result in lateral separation velocities not compatible with the PDOFs. To remedy this anomaly, the sideslip angle is adjusted. This message only occurs for collinear collisions when the user enters an impact sideslip angle.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Use the Graphics.
2. Scrutinize the sideslip angles. Do you have a firm basis for your estimates? Are they entered correctly (according to the vehicle-fixed coordinate system)? Are the signs correct? Scrutinize your sideslip angles.
3. Scrutinize the PDOFs. Make changes and observe the results. The PDOFs of both vehicles must be perfectly compatible with the sideslip angles and separation velocity components. Scrutinize your PDOFs.

---

## Sustained Contact Note

> *NOTE: Sustained contact solution form.*

**(Level 3 — Informative)**

The above message is displayed to remind the user that this option was selected. Certain analyses which normally follow, such as the trajectory simulation, are not allowed with this option. No response by the user is necessary; this is simply a reminder.

---

## Barrier Collision Note

> *NOTE: Barrier Collision Analysis — Common Velocity Check not performed.*

**(Level 3 — Informative)**

The above message is displayed as a reminder to the user that when the collision involves a barrier, the common velocity check is not performed.

---

## Rotation Direction Warning

> *WARNING: The direction of angular velocity change from SCENE DATA for vehicle is not compatible with moment arm of principal force from user-entered PDOF. Review damage data if results are questionable. Most likely, this requires either a change in the rotation direction or the PDOF.*

**(Level 3 — Informative)**

The user assigns the direction of rotation by entering heading angles for each path position. If the heading angle increases as the vehicle travels along its path, a positive rotation is indicated; if the angle decreases, a negative rotation is indicated; otherwise there is no rotation. EDCRASH does not allow for the condition whereby either vehicle is spinning prior to impact. Thus, any post-impact spinning must be due to the force of impact. The moment (torque) exerted on the vehicle as a result of the impact force must be consistent with the user-entered direction of rotation.

**What To Do:**

1. Check to see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics. Carefully note the distance from the PDOF vector to the CG (the actual moment arm distance is displayed in the Damage Data output report; see Chapter 3, Program Output) and determine if the force would tend to cause clockwise or counterclockwise rotation about the CG.
2. Scrutinize the crush stiffness coefficients. Determine if a hard spot, such as a wheel, exists that may have caused the principal force not to go through the damage centroid as normally modeled. (Note that the principal force is assumed to go through the damage centroid.) If this was not the case, you can override this assumption by supplying different crush stiffness coefficients for each crush zone, or by moving the impulse center (see Chapter 2, Program Input, Setting Up an Event; see also the User's Manual, Vehicle Damage).

---

## PDOF Compatibility Warning

> *WARNING: The user-entered PDOFs are not consistent with the angles computed by the momentum analysis. Check the Accident History report. The user-entered PDOFs should be approximately equal to the values computed using Linear Momentum (scene data).*

**(Level 3 — Informative)**

The impact phase is always analyzed using the damage data. If the collision was oblique, the impact phase is also analyzed using linear momentum. Therefore, the angle of the impulse is computed. This provides an excellent opportunity to confirm (or refute) the user's estimate for PDOFs. If the user's PDOFs differ from the PDOFs computed by the momentum analysis by more than about 10 degrees (user-editable; see Calculation Options), the above message is issued.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Then see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics.
2. Scrutinize the Path Data. Is it possible the impact positions and headings or the rest positions and headings were not what you think they were? Were there pre-impact sideslip angles? Was there an EOR that you did not enter? Was the POC valid? Are you sure about the direction of rotation? The angle calculated by the momentum analysis is only as good as the scene data. Scrutinize your Path Data.
3. Scrutinize the angle between the pre-impact velocity vectors. If they are just slightly more than 10 degrees from being parallel, the results calculated by the momentum analysis may be extremely sensitive to small changes in scene data; in particular, the impact heading and sideslip angles, and point on curve. If your results are afflicted with this problem, it will be obvious by observing the angle of the impulse (refer to the values of PDOF displayed in the Accident History output report). These angles will be vastly different from your estimate of the PDOFs. Impact speeds based on these angles will probably be preposterous. The major purpose of this error message is to provide the reason why. Scrutinize the angle between the pre-impact velocity vectors.
4. Make the right decision. If you have great confidence in your scene data and the momentum-based values of the PDOF seem reasonable, change the PDOF of each vehicle to be equal to the calculated PDOFs. Otherwise, do not change the PDOFs. Instead, locate and change the errant scene data. Make the right decision.

---

## Delta-V Compatibility Note

> *NOTE: The Damage-based Delta-V(s) differ from the Momentum-based Delta-V(s). Check for bumper over-ride or errant scene data, particularly for nearly collinear collisions.*

**(Level 2 — Diagnostic)**

The delta-V is always analyzed using the damage data. If the collision was oblique, the delta-V is also analyzed using linear momentum. This provides an excellent opportunity to confirm (or refute) the delta-V(s). If the momentum- and damage-based delta-Vs differ by more than about 10 percent (user-editable; see Calculation Options), the above message is issued.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Then see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics.
2. Scrutinize the momentum-based delta-V(s). The delta-V calculated by the momentum analysis is only as good as the scene data. Scrutinize your delta-V(s).
3. Scrutinize the Path Data. Is it possible the impact positions and headings or the rest positions and headings were not what you think they were? Were there pre-impact sideslip angles? Was there an EOR that you did not enter? Was the POC valid? Are you sure about the direction of rotation? Scrutinize your Path Data.
4. Scrutinize the angle between the pre-impact velocity vectors (see the PDOF compatibility check above). If they are just slightly more than 10 degrees from being parallel, the results calculated by the momentum analysis may be extremely sensitive to small changes in scene data; in particular, the impact heading and sideslip angles. If your results are afflicted with this problem, it will be obvious by observing the angle of the impulse (refer to the calculated values for PDOF displayed in the Accident History). These angles will be vastly different from your estimate of the PDOFs, also displayed in the Accident History. Impact speeds based on these angles will probably be preposterous because the reported impact speeds will be based on the errant momentum analysis. The major purpose of this error message is to provide the reason why. Scrutinize the angle between the pre-impact velocity vectors.

---

## Coefficient of Restitution Warnings

> *WARNING: The coefficient of restitution is negative. This implies the striking vehicle traveled through the struck vehicle during impact.*

**(Level 3 — Informative)**

> *WARNING: The coefficient of restitution is greater than 1.0. This implies the crash created energy. The normal range is ~0 to 0.25, perhaps slightly greater for low-speed impacts.*

**(Level 3 — Informative)**

The classic definition of coefficient of restitution, $r$, is the ratio of the rebound velocity to the approach velocity. In the case of vehicle collisions, we define the coefficient of restitution as the ratio of the difference in vehicle separation velocities to the difference in impact velocities,

$$r = \frac{-(v_1 - v_2)_{sep}}{(v_1 - v_2)_{imp}}$$

For most collisions, the value should lie in the range $0.0 < r < 0.25$, although for some low-speed impacts the value may be higher due to springback of energy-absorbing bumper systems.

A value of $r < 0.0$ is only possible if the vehicles pass through each other. For example, consider an axial rear-end collision that involves a moving vehicle striking the rear of a stationary vehicle. Consider the possibility that, following impact, the striking vehicle has a larger (forward) separation velocity than the struck vehicle. If you can visualize this, you will quickly see this is not possible — unless the striking vehicle actually goes through the struck vehicle. This condition is revealed by a negative restitution coefficient.

Of course, it is also possible that the struck vehicle's separation velocity is much higher than the striking vehicle's. This implies the vehicles are bouncing off of each other like super balls. This is clearly not possible in vehicle collisions. In the extreme case, in fact, the system energy would actually be higher after impact than before impact. This condition is revealed by a coefficient of restitution greater than 1.0.

**What To Do:**

1. Inspection of the equation above reveals that its denominator can never be negative (a negative denominator would imply the vehicles never collided). Thus, if $r$ is less than 0.0, the problem must lie in the numerator. Note the numerator includes only the separation velocities. These velocities are calculated from scene data (path length, tire-road friction) and wheel lock-ups. So, focus on the scene data and the wheel lock-ups.
2. The classic coefficient of restitution is derived from particle kinematics in which the colliding objects have a point mass and zero size. This is not true for vehicles, which are basically large rectangles. Thus, the equation cited earlier uses the components of the impact and separation velocities along a line drawn between the vehicle centers of gravity at their impact positions. These velocity components change as the vehicle impact positions are moved relative to each other. Therefore, confirm the relative impact positions.

*(updated: the current physics engine also issues an intermediate "restitution too high" warning (`PHYS_MSG_RESTITUTION_TOO_HIGH`) when the computed restitution exceeds the normally expected range without exceeding 1.0, and a "negative approach velocity" message when the impact geometry implies the vehicles were separating at impact. The guidance above applies to these variants as well.)*

---

## Closing Velocity Error

> *ERROR: The closing velocity is less than zero, indicating a calculation error has occurred. Two vehicles cannot collide if their closing velocity is less than zero.*

**(Level 1 — Fatal)**

This is the error-level form of the "negative approach velocity" condition referenced above. The closing (approach) velocity is the component of the difference in impact velocities along the line between the vehicle centers of gravity; it must be positive for the vehicles to have collided. If the impact geometry derived from the entered data implies the vehicles were separating (a negative closing velocity), EDCRASH cannot compute an impact speed and issues this message.

**What To Do:**

1. Re-examine the impact positions, heading angles, and PDOFs. A negative closing velocity usually indicates one of these is inconsistent with the intended collision geometry.

---

## Conservation of Energy Warning

> *WARNING: The Damage-based estimates for damage energy grossly violate the conservation of energy.*

**(Level 2 — Diagnostic)**

The energy dissipated by damage is computed when damage data are entered. If no scene data were entered, the damage analysis is the only way to compute damage energy. However, if scene data were entered, the impact and separation velocities of each vehicle are computed. The loss in kinetic energy which occurs between impact and separation should be equal to the damage energy.

This compatibility check can be performed whether the impact phase was based on Damage or Linear Momentum. If the variation between estimates exceeds the allowable limit (typically 50 percent) the above message is issued.

**What To Do:**

1. Check first to see that all accident site Path Data (impact, rest, EOR and POC) were entered correctly. Then see if the damage data (damage profiles and PDOFs) were entered correctly. Use the Graphics.
2. Scrutinize the Damage Data. Check the damage dimensions (width, crush depths, and damage offset) to be sure they were accurately measured. Remember to include induced damage, especially for narrow impact widths (less than 16 inches). Scrutinize your Damage Data.
3. Scrutinize the PDOFs. For oblique collisions, you can compare the PDOFs with the angles of the impulse (see PDOF Compatibility warning message). Remember: as the PDOF angle decreases (becomes less perpendicular) to the damaged surface, the energy dissipated by damage increases. Scrutinize your PDOFs.
4. Scrutinize the Crush Stiffness coefficients. Default coefficients are assigned when the vehicle is selected, but can be changed by the user during Event mode. The best coefficients are obtained from crash test data [25]. Higher coefficients increase the Energy Dissipated by Damage; the coefficients may be higher than assigned by the Stiffness Category if the damage region was primarily in a stiff region, such as a wheel or frame area. Lower coefficients decrease the Energy Dissipated by Damage; the coefficients may be lower than assigned by the Stiffness Category if the damage region was primarily in a soft region, such as a fender or grill (above the bumper) area. Scrutinize the Crush Stiffness Coefficients.

---

## Angular Momentum PDOF Note

> *NOTE: The user-entered PDOFs are not consistent with the angles computed by the angular momentum analysis. Check the Accident History report. The user-entered PDOFs should be approximately equal to the values computed using Angular Momentum (scene data).*

**(Level 3 — Informative)**

This message is the angular-momentum counterpart of the PDOF Compatibility Warning (above). When the collision is oblique and the PDOF does not act through the vehicle's center of gravity, the angle of the impulse can also be computed from an angular momentum analysis, providing an additional check on the user's estimate for PDOFs. If the user's PDOFs differ from the angular-momentum-derived values by more than the allowed range, the above message is issued.

> **NOTE:** The Angular Momentum solution has not been implemented in this release of EDCRASH; this message will not occur. *(updated: this remains true in the current version — the message is set only inside currently commented-out code, and the Include Angular Momentum Solution check box in the Calculation Options dialog is disabled.)*

---

## Angular Momentum Delta-V Note

> *NOTE: The Damage-based Delta-V(s) differ from the Angular Momentum-based Delta-V(s) by more than 10 percent. Check for bumper over-ride or errant scene data, particularly for nearly collinear collisions.*

**(Level 2 — Diagnostic)**

The delta-V is always analyzed using the damage data. If the collision was oblique and the PDOF does not act through the vehicle's center of gravity, the delta-V is also analyzed using angular momentum. This provides an excellent opportunity to confirm (or refute) the delta-V(s). If the momentum- and damage-based delta-Vs differ by more than 10 percent, the above message is issued.

> **NOTE:** The Angular Momentum solution has not been implemented in this release of EDCRASH; this message will not occur. *(updated: this remains true in the current version — the Include Angular Momentum Solution check box in the Calculation Options dialog is disabled.)*

---

## Collinear Collision Needs Damage Error

> \*\*\* ERROR \*\*\* *Impact Velocity and Delta-V were not computed because the collision type was collinear and damage profiles were not assigned. Collinear collisions require that damage profiles be assigned so that a damage-based Delta-V may be calculated for each vehicle.*

**(Level 1 — Fatal)**

For oblique collisions, EDCRASH requires that the user enter only scene data for the calculation of impact speed and delta-V. Damage profiles, if entered, are used as an internal consistency check. However, collinear collisions require that damage data be entered for both vehicles in order to perform the calculation of impact speed and delta-V. If damage data are not entered for collinear collisions, the above message is issued.

**What To Do:**

1. Confirm the collision type. The collision type is defined by the relative directions of the velocity vectors at impact.

   > **NOTE:** The definition is based on the direction of the velocity vectors — not the heading vectors!

   If the angle between the velocity vectors at impact is equal to or less than 10 degrees and you did not enter damage data, simply supply damage profiles for both vehicles (rigid barriers are an exception; they do not require damage profiles because they do not absorb energy).

---

## Both PDOFs Requested Error

> \*\*\* ERROR \*\*\* *The user requested EDCRASH to calculate the PDOFs for both vehicles. It is only possible to calculate the PDOF for one vehicle given the PDOF of the other. It is not possible to calculate the PDOFs for both vehicles.*

**(Level 1 — Fatal)**

The Damage Profile dialog includes an option, called Use Newton's 3rd Law, that will tell EDCRASH to calculate the PDOF of one vehicle based on the impact heading angles and the user-entered PDOF for the other vehicle. If the user asks EDCRASH to calculate the PDOF for both vehicles (i.e., the user chooses the Use Newton's 3rd Law option for both vehicles), this message will be issued.

**What To Do:**

1. Choose the Damage Profiles dialog for one of the vehicles and deselect the Use Newton's 3rd Law option.

When deselecting the Use Newton's 3rd Law option, which vehicle should you choose? Choose the vehicle for which you have the most confidence in your estimated PDOF entry. EDCRASH will then calculate the PDOF for the other vehicle based on your estimated PDOF.

---

## Automatic PDOF Note

> *NOTE: The PDOF for the vehicle was automatically calculated by EDCRASH to be consistent with Newton's 3rd Law based on the user-entered impact heading angles and the PDOF of the other vehicle.*

**(Level 3 — Informative)**

The Damage Profile dialog includes an option, called Use Newton's 3rd Law, that will tell EDCRASH to calculate the PDOF of one vehicle based on the impact heading angles and the user-entered PDOF for the other vehicle. This message simply documents that this option was selected. No action by the user is necessary.

---

## PDOF Split-Adjustment Note

> *NOTE: The user-entered PDOFs were adjusted to be compatible with the user-entered impact heading angles and Newton's 3rd Law, i.e., PDOF1 + PSI1 = PDOF2 + PSI2 +/− 180. The adjustment was performed by splitting the difference between the vehicles. The Damage Data report displays the original, user-entered values. The Accident History report displays the adjusted values.*

**(Level 3 — Informative)**

If damage profiles are entered for both vehicles, PDOFs are assigned by the user as well. These PDOFs must be compatible with Newton's 3rd Law (that is, they must be in opposite directions with respect to the earth-fixed coordinate system).

If the error does not exceed the PDOF Range consistency-check value (default ±10 degrees, user-editable; see Calculation Options), EDCRASH will automatically adjust the user-entered PDOFs, adding (or subtracting) half the difference to the assigned PDOF for each vehicle. If the error exceeds the PDOF Range, the event is terminated instead (see PDOF Incompatibility Error, below).

**What To Do:**

1. No action by the user is necessary. However, if you do not wish to have EDCRASH perform this adjustment, you have two options: the simplest is to use the AutoCalc PDOF option for one of the vehicles (choose the one you have the least confidence in); the other option is to re-enter valid PDOFs (i.e., those that satisfy the equation PDOF1 + PSI1 = PDOF2 + PSI2 ± 180).

---

## PDOF Incompatibility Error

> \*\*\* ERROR \*\*\* *The event was terminated because the user-entered PDOFs and impact heading angles were not compatible with Newton's 3rd Law, i.e., PDOF1 + PSI1 = PDOF2 + PSI2 +/− 180.*

**(Level 1 — Fatal)**

If damage profiles are entered for both vehicles, PDOFs are assigned by the user as well. These PDOFs must be compatible with Newton's 3rd Law (that is, they must be in opposite directions with respect to the earth-fixed coordinate system). This message was issued and must be corrected because the error exceeds the allowed range.

**What To Do:**

1. Re-enter valid PDOFs (i.e., those that satisfy the equation PDOF1 + PSI1 = PDOF2 + PSI2 ± 180).
2. If desired, use the AutoCalc PDOF option to automatically assign the PDOF for one of the vehicles.

---

## Missing Damage Data Note

> *NOTE: Damage data were not entered for one of the vehicles. Any damage energy absorbed by that vehicle is not included in the Damage-Based solution. This may lead to errant damage-based results and related compatibility checks between Damage- and Momentum-based results.*

**(Level 2 — Diagnostic)**

If damage profiles are assigned, damage-based delta-Vs will be computed for each vehicle. The calculation of damage-based delta-V is based on the system energy, that is, the sum of the damage energies for each vehicle. If a damage profile is entered for only one vehicle, the damage-based delta-Vs will still be computed, but they will probably under-estimate the true delta-Vs because a portion of the system energy is missing from the calculation. The exception is if one of the vehicles is a rigid barrier (because rigid barriers absorb no energy); in this case, EDCRASH will not issue this message.

**What To Do:**

1. Confirm that damage profiles are entered for both vehicles.

---

## Trajectory Simulation Time-out Note

> *NOTE: The Trajectory Simulation for Vehicle 'n' failed to converge because the vehicle timed out. Increase the Maximum Simulation Time (see Simulation Controls dialog).*

**(Level 2 — Diagnostic)**

If the Trajectory Simulation option is chosen (see EDCRASH Calculation Options), the vehicle paths are simulated using a basic trajectory simulation analysis. By default, the maximum simulation time is 5.0 seconds. If the vehicle is still moving when the maximum simulation time is reached, this message is issued. The resulting path error calculated for the rest position is probably larger than it would be if the vehicle had been allowed to continue uninterrupted to its natural rest position.

**What To Do:**

1. The solution is to simply increase the Maximum Simulation Time using the Simulation Controls dialog and rerun the EDCRASH event.

---

## Iterate on Sideslip Error

*(updated: added — not in the original manual)*

If the Separation Velocity Basis in the Calculation Options dialog is set to *Iterate on Sideslip*, the event terminates with an error before any calculations are performed, because the iterative sideslip solution is not supported by the current EDCRASH physics engine (see `Crainput.cpp`, which returns `ERROR_TIRE_MODEL_NOT_SUPPORTED`).

**What To Do:**

1. Open the EDCRASH Calculation Options dialog and choose *Normal*, *Trajectory Simulation* or *Sustained Contact* as the Separation Velocity Basis, then re-execute the event.

---

*Previous: [Chapter 5 — EDCRASH Tutorial](05-tutorial.md) · Next: [Chapter 7 — Technical References](07-technical-references.md)*

<!-- NAV -->

---

← Previous: [Chapter 5 — EDCRASH Tutorial](05-tutorial.md)  |  [Index](README.md)  |  Next: [Chapter 7 — Technical References](07-technical-references.md) →

<!-- /NAV -->
