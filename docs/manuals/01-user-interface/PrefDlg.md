# User Preferences Dialog Box

Choosing Preferences from the Options menu displays the User Preferences dialog box, which allows the user to customize HVE according to the following preferences.

> Note: Earlier versions of HVE displayed a smaller Preferences dialog containing a *Diagnostic Level* selection and *Set Window State* button. These options have been removed; the current dialog is described below.

## Auto Backup

Turns the automatic case backup feature **On** or **Off**. Only one backup method is supported, and it is always active while Auto Backup is On:

- **Only on mode change after *n* minutes** — The case is backed up when the user changes modes and the specified number of minutes has elapsed since the last save. Use the minutes field and its spinner to set the interval.

## Date Style

HVE allows the user to select from two date styles:

- **mm/dd/yy** — US Standard (month/day/year) format.
- **dd/mm/yy** — Military style (day/month/year). This style is also used in Europe and many other countries.

## Hide Date/Time From Printed Reports

When checked, the date and time are omitted from the header of printed reports.

## Key Results

Determines which set of key results variables is displayed in Key Results windows when a new event is created:

- **Use Default** — Uses the built-in default set of key results variables for the calculation method.
- **Use Previous** — Uses the same key results variables that were selected for the previous event.
- **Use Custom** — Uses a user-defined set of variables. Press **Edit...** to select the custom variable set (the Edit button is enabled only when the case contains at least one event with an object in it).
- **Copy to Variable Output** — When checked, the selected key results variables are also copied to the Variable Output report selections.

## Vehicle Dimensions Basis

Selects whether vehicle inertial/dimensional data are displayed on a **Sprung Mass** or **Total Mass** basis. (Not available in all run modes.)

## Set Background Color

Displays a color chooser used to set the background color of the viewers in the Human and Vehicle Editors.

## Skidmark Height (ft)

User-editable height (delta) at which simulated skidmarks are drawn above the surface. Raising this value can prevent skidmarks from being partially hidden by the underlying surface geometry.

## Font Size

Selects the font size (8, 10, 12, 14 or 16 points) used by numeric output reports. Changing the size immediately updates all open report windows.

## Physical Monitor Width (in)

The actual width of the display monitor. This value is used to compute true scale for 2-D (scaled) viewers; it is not used, and is therefore disabled, when a 3-D perspective camera is active.

## Long Velocity Vectors

When checked, velocity vectors displayed in the viewer (see Show Velocity Vectors in the Options menu) are drawn at increased length, making them easier to see in large environments.

## Cycle Vehicle Colors

When checked, HVE automatically assigns a different body color to each vehicle added to the case, cycling through a list of colors so that vehicles are easier to tell apart.

## Resolution Setting

Selects the size of the user interface (toolbar buttons and dialog scaling) to match the display resolution:

- **Auto Detect** — HVE chooses an appropriate size based on the current display.
- **Small**, **Medium**, **Large** — Force a specific UI size.

Changing the resolution setting displays a message; the new setting takes effect the next time HVE is started.

## Store Vehicle Geometries in case file

When checked, each vehicle's 3-D geometry is stored inside the case file, making the case self-contained (useful when moving a case to another computer). This option is available only when the vehicles in the case can be saved to the case file and the vehicles have geometry files.

## Reload language.rsc file on dialog exit

When checked, HVE reloads the language resource file (language.rsc) when the dialog is closed. This is primarily useful for checking edits to translated dialog labels without restarting HVE.

---
*Source topic: PrefDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Playback Controls (Toolbar)](PlayBackControls.md)  |  [Index](README.md)  |  Next: [Report Window Dialog Box](PrevWnd.md) →

<!-- /NAV -->
