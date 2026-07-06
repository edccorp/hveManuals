# HVE DamageStudio

**Section Twelve of the HVE User's Manual — Version 8**

Updated Markdown edition, converted from the legacy manual and verified against the current HVE source code (`HVEINV-64/DamageStudioReportDlg.cpp`, `HVEINV-64/DamageStudioOptionsDlg.cpp`, `HVEINV-64/DamageStudioDataSource.cpp`, `HVEINV-64/KITS/DamageStudio*Kit.*`, `HVEINV-64/CalcStructs.h`, `Physics/Source/LibHve/CollisionData.cpp`).

Copyright Engineering Dynamics Corporation. All rights reserved.

DamageStudio is a graphical analysis tool that allows vehicle crash safety engineers to visualize collision data, and to correlate collision damage with the kinetics (force magnitude and direction), delta-V, acceleration and other important collision parameters. DamageStudio is a component in the HVE Playback Editor.

DamageStudio may be used to study all types of collisions (e.g., barrier, single vehicle, multi-vehicle, secondary impact, rollover, ...) for all types of vehicles (e.g., passenger car, van, truck, trailer, dolly, ...).

There are many uses for the kind of detailed collision information produced by DamageStudio. One example is the ability to directly compare simulated crush dimensions with a measured damage profile. This kind of analysis may also be used to fine-tune stiffness coefficients from staged collision data.

DamageStudio can also be used to identify the magnitude and direction of individual impulses, peak collision forces and delta-Vs for vehicles undergoing multiple impacts, even if the impacts are simultaneous.

## General Procedure

To use DamageStudio, perform the following steps:

1. Set up and execute a collision event.
2. Go to the Playback Editor.
3. Add a DamageStudio report. The DamageStudio window is displayed. *Simulated* damage is the current Viewer option *(updated: the current viewer dropdown uses the short name "Simulated" for the option the original manual called "Geometry, Simulated Damage")*.
4. Use the Playback Controller to play the event.
5. Watch DamageStudio's viewer as it displays the damage profile for the first vehicle. Note that the damage profile changes as the simulation progresses. If the event includes more than one impulse, each damage profile is displayed in sequence for each individual impulse.
6. Observe the Damage Profile numeric results (Impulse No., CDC, PDOF and damage profile dimensions) as the simulation progresses. The impulse number is initially *Auto*, and displays the individual impulse number and associated damage profile data as the event progresses.
7. Click on the Impulse Number dropdown list and choose an impulse number. The damage profile data for the selected impulse is displayed.
8. Click *Prev* or *Next* to switch vehicles.
9. Repeat the above steps for each vehicle in the simulation.
10. Change the current Viewer option to *User-entered* damage.
11. Enter a CDC, followed by `<Enter>` or *Apply*. The default damage profile for the CDC is displayed in the Damage Profile group and the associated damage profile is displayed in the viewer.
12. Edit the damage profile data (width, offset, elevation, crush table) and observe the changes to the vehicle damage profile in the viewer.

## Overview of Section Twelve

This section describes the background and use of DamageStudio.

- [Chapter 32](#contents) provides a description of the DamageStudio user interface and the process of using DamageStudio.
- Chapter 33 provides several tutorials showing the user how to accomplish various tasks using DamageStudio. *(Chapter 33 is not included in this edition.)*

## Contents

| Chapter | File |
|---|---|
| 32 (part 1) — The DamageStudio Interface | [01-interface.md](01-interface.md) |
| 32 (part 2) — Using DamageStudio | [02-using-damagestudio.md](02-using-damagestudio.md) |

## Related Pages

- [Damage Data dialog](../../11-reports-output/DamageData.md) — the Event Editor dialog used to assign a user-measured damage profile (CDC, PDOF, crush depths, stiffness) to a vehicle. The *User-entered* damage view in DamageStudio is closely related to this dialog.

<!-- NAV -->

---

Next: [Chapter 32 — The DamageStudio Interface](01-interface.md) →

<!-- /NAV -->
