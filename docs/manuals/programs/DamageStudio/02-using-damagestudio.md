# Chapter 32 (continued) — Using DamageStudio

Using DamageStudio involves the following steps:

1. Set up and execute a collision event.
2. Go to the Playback Editor.
3. Add a DamageStudio report. The DamageStudio window is displayed.

> **NOTE:** Although not required, it is a great idea to add a Damage Data report as well. Remember: it contains a synopsis of the CollisionData!

The next steps depend on the type of event (reconstruction vs. simulation) and the currently selected viewer option.

## Geometry, Simulated Damage ("Simulated")

When a DamageStudio window is initially displayed, *Simulated* is the default viewer option for simulation events.

> **NOTE:** This option is not available for reconstruction events.

Because it is the default option, the *Show* checkbox is automatically checked. The viewer displays the event's first vehicle in its original condition (i.e., undamaged). The Damage Profile group information is initially blank or zero, except for the impulse number, which is *Auto*. When the impulse number is *Auto* and the user plays the simulation event, DamageStudio will automatically update the impulse number and associated damage information at the correct time as the simulation progresses.

*(updated: the Auto entry in the Impulse No. dropdown is only offered for the Simulated damage view; for the other views the dropdown lists impulse numbers only — see `ShowAutoImpulseOption()` in `DamageStudioReportDlg.cpp`.)*

4. Use the Playback Controller to play the event.

When the simulation time reaches the start time for the first impulse, the impulse number changes from *Auto* to *1*, indicating that the first collision is under way. The CDC, width, offset, elevation and crush table are updated dynamically as the simulation proceeds through the first collision. The viewer displays the damage profile crush vectors and PDOF. At the conclusion of the impulse, the impulse number will return to *Auto*, the damage profile data will return to blank or zero, and the crush vectors and PDOF will disappear from the viewer.

If the event includes more than one impulse, the impulse number will change to *2* when the simulation time reaches the start time for the second impulse, and the damage profile data and viewer will display the results for the second impulse. This process continues for each impulse, as its damage profile data and viewer are displayed in sequence for each individual impulse.

The user can also select a particular impulse to review its damage profile data. To view the results for a particular impulse, perform the following steps:

5. Click on the Impulse Number dropdown list and choose an impulse number. The damage profile data for the selected impulse are displayed.

The Damage Width and Offset are not editable because they are determined directly by the simulation. However, it is possible to determine the effect of changing the number of crush zones, as well as identify crush depths at specific elevations:

6. Click on the Number of Zones dropdown list and change it from its default value, 4, to a larger number to increase the resolution of the crush measurements. There is no change to the damage profile. However, the number of rows in the crush table and number of crush vectors in the viewer reflect the additional measurements.
7. Click on the Elevation/Dist dropdown list and change the elevation/distance number from 1 to 2, 3, 4 and 5. Observe the crush table and crush vectors update as they reflect the crush depth at the selected elevation.
8. Click in the Elevation/Dist field and edit the value associated with the selected elevation/distance number. The crush table and crush vectors will change to reflect the new elevation/distance value.
9. Click *Prev* or *Next* to switch vehicles.
10. Repeat the above steps for each vehicle in the simulation.

> **NOTE:** When an impulse number is specifically selected using the Impulse No. dropdown list, the data displayed come directly from the CollisionData, which is calculated at each integration timestep. When Auto is selected and the event is played, the results are displayed directly from the output tracks, which are available at each output timestep and possibly interpolated according to the Playback Interval. Thus, there may be small differences in the results when Auto is used to replay an event vs. the explicit selection of an impulse number. Setting the Simulation Output Interval and Playback Output Interval equal to the integration timestep eliminates this difference. However, this also may greatly increase the size of the case file.

## Damage, User-entered ("User-entered")

*User-entered* is the default viewer option for reconstruction events, and the *Show* checkbox is automatically checked. For simulation events, the *User-entered* view must be explicitly selected by checking the *Show* checkbox.

To use the *User-entered* viewer option, perform the following steps:

1. If the current event is a simulation, click the *Show* checkbox.

The viewer displays the event's first vehicle in its original condition (i.e., undamaged). The Damage Profile group information is initially blank or zero, except for the impulse number, which is *1*.

2. Enter a CDC, followed by `<Enter>` or *Apply*. The default damage profile for the CDC is displayed in the Damage Profile group and the associated damage profile is displayed in the viewer.
3. Edit the damage profile data (width, offset, elevation, crush table) and observe the changes to the vehicle damage profile in the viewer.
4. If desired, click on the Impulse No. dropdown list and select impulse number *2*.
5. Enter a CDC for the second impulse and, optionally, edit the associated damage profile data.
6. Repeat the above steps for up to 10 individual impulses (damage profiles).

The entry of user-measured damage profiles in DamageStudio parallels the Event Editor's [Damage Data dialog](../../11-reports-output/DamageData.md), where a CDC also assigns a default PDOF and damage profile that may then be edited.

## Geometry, Undamaged ("None")

Select *None* in the Damage dropdown and check *Show* to display the vehicle's original (undamaged) geometry. Adjust the *Transparency* slider to overlay the undamaged geometry over another view for comparison.

*(updated: the original manual stated "(Not implemented)"; this view is implemented in the current release.)*

## Geometry, From File ("From File")

Select *From File* in the Damage dropdown, check *Show*, and use the *Filename* field / *Open...* button to load a user-supplied geometry file (for example, a scanned or independently modeled damaged vehicle) into the viewer for comparison.

*(updated: the original manual stated "(Not implemented)"; this view is implemented in the current release.)*

## Damage Photograph ("Photograph(s)")

*(Not currently available: the Photograph(s) option is present in the source code but removed from the viewer dropdown in the current release.)*

## Some Notes About Damage Profiles

The general nature of quantifying and measuring an irregular damage profile leads to some interesting observations. The notes below are intended to help the user understand and interpret their results.

- Each damage profile has a single CDC describing the entire damage pattern. Therefore, a damage profile has a single width and width offset. The damage width does not vary according to elevation. In addition, a damage profile has a single height and height offset.
- It is likely that the crush depth will be zero at numerous points within the damage profile. These points typically occur above or below the elevation associated with the maximum damage width (where the damage width is, in fact, defined).
- It is not uncommon for the total crush depth at the endpoints of damage to be very large. This occurs because the vehicle is not truly rectangular. The vast majority of this damage (perhaps all of it) is free space. This can also occur at the top and/or bottom elevations (for the same reason).
- Anomalous crush depth values may occur for obscure reasons. For example: During a frontal collision the fender flares are crushed inward. As a result, the crush depth at that point on the profile is measured to the rear of the (undamaged) fender well, resulting in a very large crush depth. It is not free space, because free space is determined by the original (undamaged) vehicle shape, so the fender flare is the surface used for the free space calculation.
- If a vehicle geometry has gaps, the crush vectors can be very large, simply because the arrow never contacted the surface until it reached the other side of the vehicle. This often occurs as a result of surfaces with reversed surface normals.

> **NOTE:** See the Crush Depth Tables discussion in [Chapter 32, part 1](01-interface.md#crush-depth-tables) for more information about the procedure for calculating crush depth and free space.

<!-- NAV -->

---

← Previous: [Chapter 32 — The DamageStudio Interface](01-interface.md)  |  [Index](README.md)

<!-- /NAV -->
