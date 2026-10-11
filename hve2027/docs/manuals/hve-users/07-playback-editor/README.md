# Section Seven: Playback Editor

A motor vehicle crash sequence often includes several events involving many different vehicles, and any number of occupants and pedestrians. The purpose of HVE's Playback Editor is to combine simulations from several events into a single, coherent sequence involving multiple humans and vehicles, to produce video output, and to view and print the complete output reports for each event. This section of the HVE User's Manual describes how HVE 2027 does each of these.

!!! note "HVE 2027"
    HVE 2027 splits HVE's Playback Editor between two editors:

    - In **Event** mode (the **Event (F5)** tab) a solved event is **played
      back in the Viewport**, with the playback bar along its bottom and
      **Output › Playback Options...**, and the **reports, graphs and
      tables** for the current event are on the **Output** menu: Key
      Results, Output Graph, Timestep Data Table, Variable Selection,
      Variable Report, Accident History Report, HVE Reports, Damage Studio
      Report and Export Variables.
    - In **Playback** mode (the **Playback (F6)** tab) **several events are
      combined** into one timeline in the **Playback Sequence** panel, and
      that sequence is what the Viewport plays.

## General Procedure

To view, combine and export the results of events in HVE 2027, perform the following steps:

1. Select Event mode and run each event you need (**Run** on the playback bar), or in Playback mode press **Run All** to run every event of the sequence.
2. Open the output panels you need from the **Output** menu to view the results of the current event.
3. If desired, save a report or table to a file.
4. Use the **Playback (F6)** editor to combine several solved events into a single, coherent sequence involving multiple humans and vehicles.
5. Record the playback to an AVI video with **File › Record Animation...**, or export the scene to Blender (File › Export Scene for Blender, or File › Blender Live Link) to render a movie.

!!! warning "Not in HVE 2027"
    HVE 2027 does not print. See [Chapter 17](17-report-playback-windows.md).

## Overview of Section Seven

This section provides a detailed explanation of the process of viewing, combining and editing the results of events:

- [Chapter 17](17-report-playback-windows.md) describes the output panels, reports and playback.
- [Chapter 18](18-editing-event-sequence.md) describes combining and timing multiple events in a playback sequence.

## Related Reference Pages

- [Playback Controls (Toolbar)](../../01-user-interface/PlayBackControls.md)
- [Report Window Dialog Box](../../01-user-interface/PrevWnd.md)
- [Key Results Dialog Box](../../01-user-interface/KeyResDlg.md)
- Output report reference: [Section 11 — Reports and Output](../../11-reports-output/README.md)

---

<!-- NAV -->

---

Next: [Chapter 17 — Creating Report and Playback Windows](17-report-playback-windows.md) →

<!-- /NAV -->
