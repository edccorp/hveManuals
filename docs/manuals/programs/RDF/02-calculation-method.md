# Chapter 3 — Calculation Method

## Overview

ReadDataFile uses linear interpolation to calculate the position and orientation of objects between the designated time steps contained in the data file. The data file must contain time-dependent position and orientation data (i.e. X, Y, Z, Yaw, Pitch, Roll).

In addition, ReadDataFile differentiates the position data to produce velocity and acceleration data. **BE EXTREMELY CAREFUL WITH VELOCITY AND ACCELERATION DATA.** This program uses the interpolated position data, based on the Output Time Interval contained in the Simulation Controls dialog, to calculate velocity and acceleration. Therefore, if the data file contains finely spaced time data and the Output Time Interval is large compared to the data file time increment, then the program may "miss" the acceleration.

For example, consider a data file that contains position data at time = 0.0 seconds and then data every 0.1 second up to 2.0 seconds. Further assume that the data describes a vehicle traveling in a circle and that the position and orientation data at 2.0 seconds is the same as at 0.0 seconds. Therefore, at 1.0 seconds the vehicle is half way around the circle. If the Output Time Interval is chosen to be 1.0 seconds, then the vehicle will move in a straight line across the circle and return. If the Output Time Interval is 2.0 seconds the vehicle will not move at all. Thus, the user must make sure that the Output Time Interval is small enough to generate the correct motion. If possible, use an Output Time Interval that is equal to the smallest time increment that appears in the data file.

The same potential error may occur with velocity and acceleration data. If the Output Time Interval is too large compared to the time increments in the data file, then the velocity and accelerations will probably not be correct. This feature is implemented in an effort to assist in producing "rough" acceleration pulse data, but as with all computer programs... CHECK ALL OF YOUR DATA CAREFULLY.

*(updated: implementation details verified in `ComputeData()` in `ReadDataFilemain.cpp`. The program keeps a two-entry interpolation buffer and steps the simulation clock from 0 to the Max Time from the Simulation Controls dialog in steps of the Output Time Interval. Velocities are computed by finite differences of the interpolated positions from one output step to the next, and accelerations by finite differences of those velocities; at the first output step velocity and acceleration are reported as zero, and at the second step acceleration is still zero. Angular data is screened between successive file entries for discontinuities caused by quaternion-to-roll/pitch/yaw conversions in the originating program, and adjusted (±180° with pitch mirrored) when a discontinuity is detected — see `transform_rpy()`. If the end of the data file is reached before Max Time, the event simply ends at the last file time.)*

In addition, use care when selecting the precision of the input data. The input data should be entered in INCHES and DEGREES. Select the decimal accuracy of the data depending on the time increment of the data. In other words, if the data is in 0.001 second intervals, then 0.001 inches may be the amount of accuracy you need in your positional data.

GREAT CARE MUST BE USED WITH THE ORIENTATION DATA. In other words, in HVE +180 degrees yaw and -180 degrees yaw may look the same but will result in different motion. The positive yaw angle will produce a clockwise yaw movement while the negative yaw angle will produce a counter-clockwise yaw movement. THIS IS VERY IMPORTANT AND IF THIS BEHAVIOR IS NOT FULLY UNDERSTOOD THEN INVALID MOTION MAY BE PRODUCED.

<!-- NAV -->

---

← Previous: [Chapter 1 — Program Description](01-program-description-and-input.md)  |  [Index](README.md)  |  Next: [Chapter 4 — Data File Format](03-data-file-format.md) →

<!-- /NAV -->
