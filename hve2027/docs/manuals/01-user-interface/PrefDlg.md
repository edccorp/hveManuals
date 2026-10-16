# User Preferences Dialog Box

Choosing **Tools › Preferences...** displays the **Preferences** window. Settings take effect as they are changed; close the window with its close button.

![Preferences window](images/hvn-preferences.png)

## Display

### Date Format
**US (MM/DD/YYYY)** or **ISO (YYYY-MM-DD)**.

### Units
**Metric (m, km/h, kg, N)** or **Imperial (ft/in, mph, lb, lbf)**. Every dialog and output that shows a converted value follows this setting at once; see [Units Dialog Box](UnitsDlg.md). A note says that fields still carrying a fixed SI label are being converted.

### Background Color
The color behind the 3-D scene. Click the swatch for a color picker, or type the values.

## Diagnostics

### Diagnostic Level
**Off**, **Level 1** or **Level 2**.

## Auto-Save

### Enable Auto-Save, Interval (min)
A switch and an interval in minutes (at least 1).

!!! note "HVE 2027"
    - **Date Format** sets how dates are shown in the Audit Log, the file browser and the run report.
    - **Enable Auto-Save** (on by default) and **Interval (min)** write a recovery copy of the case, `<case>.autosave.hvex` beside it, while there are unsaved changes; the case file itself is never written. Saving the case removes the copy, and opening a case whose recovery copy is newer offers to open the copy.
    - These settings are saved between sessions.

!!! warning "Not in HVE 2027"
    - **Diagnostic Level** is greyed: it has nothing to control in HVE 2027, where what a run assumed or repaired is always in its run status.
    - **Hide Date/Time From Printed Reports**, **Key Results** (Use Default / Use Previous / Use Custom, Copy to Variable Output), **Vehicle Dimensions Basis** (the Vehicles panel and the Inertia / Mass dialog show the sprung and total bases side by side instead; in HVE it changes no result, because every engine that reads it overwrites it with the total-mass basis), **Skidmark Height**, **Font Size**, **Physical Monitor Width**, **Long Velocity Vectors**, **Cycle Vehicle Colors**, **Resolution Setting** and **Reload language.rsc file on dialog exit**.
    - **Store Vehicle Geometries in case file**: not a preference in HVE 2027. **File › Embed vehicle meshes in the case** (off by default) stores each vehicle's own mesh inside the case at the next save; EDC's licensed meshes are never stored. A saved case also carries the site's geometry and photograph inside it (**File › Embed the environment in the case**, on by default), and **File › Publish Bundle...** writes the case, the meshes it names and its results into one folder.

!!! tip "New in HVE 2027"
    Related settings live elsewhere: **Tools › Style Editor...** sets the look of the interface; **View › Show Guidance Text** shows or hides the long explanatory notes in the dialogs (off by default; a message about a problem with the open case is always shown); **View › Panels Outside the Main Window** lets panels float as separate windows.

<!-- NAV -->

---

← Previous: [Playback Controls (Toolbar)](PlayBackControls.md)  |  [Index](README.md)  |  Next: [Report Window Dialog Box](PrevWnd.md) →

<!-- /NAV -->
