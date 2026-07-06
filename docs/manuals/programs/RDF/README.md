# ReadDataFile — User's Manual

**Collision Engineering Associates, Inc. — for the HVE (Human Vehicle Environment) simulation environment**

Updated Markdown edition, converted from the legacy ReadDataFile manual (manual printed August 17, 2004) and verified against the current HVE source code (`Physics/Source/ReadDataFile/`, `Physics/Include/Hvedef.h`, `HVEINV-64/`).

*(updated: the 2004 manual documents data-file format version 3.500. The current ReadDataFile physics module reports program version 19.03 — `READDATA_VERSION` in `ReadDataFiledef.h` and `VersionNumber[] = "19.03"` in `ReadDataFileinput.cpp` — but still reads the version 3.200/3.500 data-file formats described in this manual. Within HVE, this manual is installed as `ReadDataFile.pdf` and opened from the Help > User Manuals menu.)*

*HVE is a trademark of Engineering Dynamics Corporation. ReadDataFile was written by Collision Engineering Associates, Inc. (source-code credits: Daniel J. Kuhn). Portions copyright Engineering Dynamics Corporation.*

## What is ReadDataFile?

ReadDataFile is an HVE-compatible physics program (calculation method) that imports time-based position and orientation data for vehicles and humans from a space-delimited ASCII data file, and turns that data into a normal HVE event. It is not a simulation: it interpolates externally generated motion data so that the standard HVE tools (Playback Editor, variable output tables, trajectory visualization) can be used with results from programs that have not been ported to HVE, from spreadsheets, or from any other calculation method.

## Contents

| Chapter | File |
|---|---|
| 1 — Program Description and 2 — Program Input | [01-program-description-and-input.md](01-program-description-and-input.md) |
| 3 — Calculation Method | [02-calculation-method.md](02-calculation-method.md) |
| 4 — Data File Format (with examples) | [03-data-file-format.md](03-data-file-format.md) |

<!-- NAV -->

---

Next: [Chapter 1 — Program Description](01-program-description-and-input.md) →

<!-- /NAV -->
