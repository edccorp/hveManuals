# Key Results Dialog Box

This dialog box (whose title bar reads *Key Results-\<object name\>*; the internal resource is IDD_KEY_VARIABLES) displays user-specified results during Event and Playback modes. Key Results are especially useful during Event mode to monitor the values of one or more variables at each time step. Use the Variable Selection dialog to select which variables are displayed in the Key Results window. A separate Key Results window is displayed for each human and vehicle in the event.

The window is resizable, and its contents differ slightly between reconstruction events (which display a single set of results) and simulation events (which display values updated at each output time interval).

## Select Variable

Click this button to choose which variables are monitored. The [Variable Selection Dialog Box](../11-reports-output/VarSelDlg.md) is displayed, listing the available output groups and variables for the object. This button is enabled only for simulation events; in reconstruction events the variable set is fixed and the button is disabled.

## Key Variable Grid

A two-column grid showing the selected variables:

- **Variable** — The name of each variable selected in the [Variable Selection Dialog Box](../11-reports-output/VarSelDlg.md), grouped by output group.
- **Result** — The current value of the corresponding variable, displayed in the current user units. During a simulation the values update at the current simulation time; for a reconstruction the computed results are shown.

See also: Event Mode, Playback Mode, Variable Selection Dialog Box, and the *Key Results* preference in the [User Preferences Dialog Box](PrefDlg.md), which controls the initial variable selection for new events.

---
*Source topic: KeyResDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Camera Setup Dialog Box](CameraSetDlg.md)  |  [Index](README.md)  |  Next: [Light Editor Dialog Box](LightEdDlg.md) →

<!-- /NAV -->
