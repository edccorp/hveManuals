# Options Menu

This menu includes the following options (in menu order):

## Create DB

Rebuilds the HVE object database (ESNDB.db) from the database source files. All vehicle and human binary files are regenerated and the rebuilt database is reloaded. This may take a few moments; the cursor changes to an hourglass while the database is being created.

## Show Key Results

Choosing this option displays a [Key Results Dialog Box](KeyResDlg.md) for each object. Key Results dialog boxes display the user-specified results during Event and Playback modes. Key results are especially useful during Event mode to monitor the values of one or more variables at each time step. Use the Variable Selection dialog to select which variables are displayed in the Key Results dialog box.

See also: [Key Results Dialog Box](KeyResDlg.md), Event Mode, Playback Mode, Variable Selection Dialog Box.

## Show Axes

Choosing this option displays a set of vectors in the X,Y,Z directions for each human and vehicle as well as the environment. The origin of the axis system is at the origin of the object. The axes are displayed in all modes.

## Show Contacts

Choosing this option displays the physical contact surfaces used for generating forces between human ellipsoids and vehicle contact surface planes. Visualizing these planes can be very useful while creating the ellipsoids and surface planes, and also during Event mode when the interactions are being simulated. However, you may choose to hide contacts during Playback mode if you find them visually distracting.

## Show Belt Anchors

Choosing this option displays the vehicle-fixed belt anchor locations for each belt restraint system installed in the vehicle. The location of the icon can provide important visual cues during event set-up as well as during execution.

## Show Velocity Vectors

Choosing this option displays the current velocity vector during Event and Playback modes. Both relative magnitude and direction are shown. (The vector's length shortens as the vehicle slows.) This vector can provide important visual cues during event setup as well as during execution. (See also the *Long Velocity Vectors* option in the User Preferences dialog, which lengthens the displayed vectors.)

## Show Skidmarks

Choosing this option displays tire skid marks and scuff marks calculated by the simulation model. Simulated tire marks are displayed for each tire, including duals, and are displayed according to the tire's width (based on the tire size designation).

## Show Tracks

Toggles the display of the wheel track overlay — the path traced by each tire, whether or not the tire is skidding. Useful for comparing the simulated wheel paths against evidence at the scene.

## Show CGs

Toggles the display of a symbol at each vehicle's center of gravity.

## Show CG Paths

Toggles the display of the path traced by each vehicle's center of gravity during the event.

## Show Accelerometers

Toggles the display of a symbol at each vehicle's accelerometer location.

## Show Accelerometer Paths

Toggles the display of the path traced by each vehicle's accelerometer during the event.

## Show Position Sequences

Toggles the display of position sequence overlays — a series of vehicle positions displayed at selected times during the event.

## Show Targets

Choosing this option displays target humans and vehicles. Targets are positions you can enter during event setup that do not enter into simulation calculations (except for the HVE Path Follower), but allow you to visually compare how closely the simulated path matches the actual path represented by the targets. Simulation models may also perform error calculations based on the target positions and velocities to quantify the match between simulated and actual paths.

Target humans and vehicles are translucent to distinguish them from positions used by the calculation model.

## Show Connections

Toggles the display of the connections (e.g., hitches and articulation points) between connected vehicles, such as a tractor and its trailer(s).

## Distance Tool

Displays the modeless Distance Tool dialog, used for measuring distances in the viewer during Event mode. Available only when the case contains at least one event.

## Show Path

Displays the Show Curved Path dialog for the current event. Use it to display a smooth (spline) curved path in the viewer based on the event's path positions; the path display is updated when the dialog is closed with OK.

## Autoposition

Choosing this option causes vehicles to be positioned on top of the environment surface geometry. AutoPosition uses the current surface elevation beneath each wheel and the vehicle's tire radii and ride height to determine the earth-fixed Z coordinate of the vehicle CG which will place the vehicle in equilibrium at the start of a simulation. AutoPosition greatly simplifies initial positioning for 3-D simulations, which otherwise tend to take a while for the simulation to reach equilibrium.

AutoPosition does not include suspension and tire deflections. Therefore, a small disturbance may still be experienced, especially on 3-D terrain that does not form a plane beneath the tires.

AutoPosition is always used for 2-D reconstructions and simulations. Because these models do not include suspension effects, on severely non-planar surfaces tires may appear to come off the ground. This visual effect does not affect calculations.

## Grid

Choosing this option displays markers at user-defined intervals. These markers are used as spatial cues to help determine distances while creating and editing 3-D models of humans, vehicles and environments. It displays the [Set Grid Dialog Box](SetGridDlg.md).

## Units

Allows the user to switch between US, SI and user-defined systems of units. Choosing this option displays the [Units Dialog Box](UnitsDlg.md).

## Shadows

Displays the Shadow Options dialog. Options include *Show Shadows* (turns shadow rendering on/off) and user-editable *Radius*, *Quality*, *Precision* and *Intensity* values that control the size, smoothness and darkness of the rendered shadows.

## Render (Ctrl+R)

Choosing this option displays the [Render Dialog](RendOptDlg.md). This dialog includes several user-definable options which affect the visual quality of the objects displayed by HVE.

## Playback

Sets the playback time interval for the current playback window. It displays the Playback Options dialog box.

## Simulation Controls (Ctrl+Y)

Choosing this option displays the Simulation Controls dialog box.

## Calculation Options (Ctrl+J)

Choosing this option displays the Calculation Options dialog box for the calculation method currently selected for the event. The available dialogs include:

- EDCRASH — [EDCRASH Calculation Options](../10-calculation-options/CalcOptEDCRASHDlg.md)
- EDGEN — [EDGEN Calculation Options](../10-calculation-options/CalcOptEDGENDlg.md)
- EDHIS — [EDHIS Calculation Options](../10-calculation-options/CalcOptionsEDHIS.md)
- EDSMAC4 — [EDSMAC4 Calculation Options](../10-calculation-options/CalcOptEDSMAC4.md)
- EDSVS — [EDSVS Calculation Options](../10-calculation-options/CalcOptEDSVS.md)
- EDVDS — [EDVDS Calculation Options](../10-calculation-options/CalcOptEDVDS.md)
- EDVSM — [EDVSM Calculation Options](../10-calculation-options/CalcOptEDVSM.md)
- EDVTS — [EDVTS Calculation Options](../10-calculation-options/CalcOptEDVTS.md)

## DyMESH

Displays the DyMESH Options dialog, containing options for the DyMESH 3-D collision algorithm.

## Get Surface Info

Displays the Get Surface Information Options dialog for the current event. The selected options determine which surface information is retrieved beneath each tire; closing with OK re-tessellates the environment surfaces used by physics.

## Preferences (Ctrl+F)

Customizes HVE according to various user-selectable preferences. Displays the [User Preferences Dialog Box](PrefDlg.md).

> Note: The *Add Playback Window* command described in earlier versions of this help topic is no longer located in the Options menu. Playback windows are added from Playback mode (see the Playback Information dialog).

---
*Source topic: OptionsMenu.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Object Attributes Dialog Box](ObjAttrDlg.md)  |  [Index](README.md)  |  Next: [Overlays Dialog Box](OverLayDlg.md) →

<!-- /NAV -->
