# Event Setup Menu

In HVE 2027 the HVE Event Set-up menu is the **Event** menu. It appears in the
menu bar only while the **Event** editor (F5) is active. Items are enabled or
disabled according to the capabilities of the active event's calculation
method; a few method-specific items appear only for the methods that use them.

!!! note "HVE 2027"
    HVE's shortcuts beside the Event menu items (Ctrl+P, Ctrl+D, Ctrl+M,
    Ctrl+U, Ctrl+W, Ctrl+T) and Ctrl+R (Run Simulation) work in the Event
    editor, each only while its menu item is offered for the event's
    calculation method. The file shortcuts are Ctrl+N, Ctrl+O, Ctrl+S.

**Event Information...**
Opens the [Event Information](EventInfo.md) panel (events, calculation method,
vehicles and humans in the event, initial conditions).

**Position / Velocity...**
Displays the [Position/Velocity](PosVelDlg.md) dialog. Enabled for the methods
that read initial conditions (every method except EDCRASH and READDATAFILE).

**Driver Controls...**
Displays the [Driver Controls](DriverControls.md) dialog. Enabled for the
simulation methods that read driver tables, and for EDCRASH, whose dialog shows
only the Wheel Data page.

**Damage Profiles...**
Opens EDCRASH's measured damage (CDC, PDOF, crush depths) in the Vehicle Impact
Setup section of [Event Information](EventInfo.md#vehicle-impact-setup-edcrash).
Enabled for EDCRASH only. A vehicle's crush stiffness (A, B, Kv and the 3-D node
stiffness) is **Vehicle › Crush Stiffness...** in the Vehicle editor.

**Collision Pulse...**
Displays the [Collision Pulse](../11-reports-output/ColPulse.md) dialog.
Enabled for EDCRASH, SIMON, EDHIS and GATB.

**Vehicle Mesh...**
Displays the Vehicle Mesh dialog. Always available. (**Advanced Mesh Options...**
at the bottom of the menu opens the same dialog.)

**DyMESH Options...**
Displays the DyMESH Options dialog for the active event. Always available; the
options are read by SIMON.

!!! tip "New in HVE 2027"
    **DyMESH Options** and **Path Follower** are Event-menu items in HVE 2027
    because both are stored per event. The path follower is described in
    [Driver Controls Path Follower](DriverControls7.md).

**Path Follower...**
Displays the [Path Follower](DriverControls7.md) dialog (HVE's HVE Driver page).

**Payload...**
Displays the Payload dialog. Enabled for the methods that read a payload: SIMON, EDSMAC4, EDSVS, EDVDS and EDVTS.

**Lights...**
Displays the event Lights window: which of each vehicle's lamps the run may
switch on, and how (see [Driver Controls](DriverControls.md#lights)). Enabled
for SIMON and EDSMAC4.

**Wheels...**
Displays the event Wheels dialog. Enabled for the simulation methods.

**Accelerometers...**
Displays the Accelerometers dialog. Enabled for the methods that compute accelerometer output: SIMON, EDSMAC4, EDVDS and EDVSM. (EDSMAC, EDSVS, EDVTS and EDGEN produce no accelerometer output, as in HVE.)

**Contacts...**
Displays the [Contacts](ContactsDlg.md) dialog: the Occupant Contacts dialog
for an EDHIS or GATB event, the Contacts window for EDSMAC4. Enabled for those
three methods.

**Restraints...**
A submenu with **Airbags...** and **Belt Restraint...**. Enabled for EDHIS and
GATB, the methods that read belts and airbags.

**Notes**
Displays the Event Notes dialog: free-form notes kept with the event and saved
with the case. They reach no calculation.

**Method-specific items**

- EDCRASH: **Impact Plane / Barrier...** (greyed — see below) and
  **Crush Profile...**.
- EDSMAC and EDSMAC4: **Handling Parameters...**, **Move CG...** and
  **Crush Profile...**.

!!! warning "Not in HVE 2027"
    **Impact Plane / Barrier** is shown greyed for EDCRASH events: the dialog is
    not implemented. Model a barrier as a vehicle whose type is Fixed Barrier
    (Vehicle Information).

<!-- NAV -->

---

← Previous: [Event Information Dialog Box](EventInfo.md)  |  [Index](README.md)  |  Next: [Inter-Vehicle Connections Dialog](IntrVehConnsDlg.md) →

<!-- /NAV -->
