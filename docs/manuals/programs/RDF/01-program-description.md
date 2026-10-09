# Chapter 1 — Program Description

## Overview

There are a number of computer simulation programs used in accident reconstruction analysis that have not yet been ported to the HVE computing environment. In an effort to assist the users of these programs, ReadDataFile has been produced. This HVE-compatible program accepts an ASCII data file that contains motion data for selected objects and loads the motion data into HVE. Once this has been accomplished, the standard HVE tools are available to generate a three-dimensional visualization of the data. The ReadDataFile event can also be combined with other HVE events in the Playback Editor.

This program is **not** a simulation, although it may be used to create visualizations of simulation results. The data file must contain time-dependent position data for the objects selected. ReadDataFile interpolates this data and produces an HVE event with the data. In addition, the program calculates the velocity and acceleration data for the objects and places this data in the variable output tables for easy viewing, printing, or graphing.

ReadDataFile can be used with vehicle and human objects. The data contained in the file does not have to be generated with a simulation program. The data may be generated with a spreadsheet or other calculation method, as determined by the requirements of the user.

<!-- NAV -->

---

← Previous: [ReadDataFile — User's Manual](README.md)  |  [Index](README.md)  |  Next: [Chapter 2 — Program Input](02-program-input.md) →

<!-- /NAV -->
