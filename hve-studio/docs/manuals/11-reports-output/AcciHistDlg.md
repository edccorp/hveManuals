# Accident History

The Accident History is a table of positions and velocities describing the
motion of each vehicle at the key phases of the event.

In HVE Studio there is one Accident History: the engine's own page, as HVE
prints it.

- It is the **ACCIDENT HISTORY** page of **Output › HVE Reports...**: click its
  tab, or find the page wherever you have placed it (see
  [Common Reports](CommRepDlg.md)).
- The page is built by the engine itself at the end of the run, from HVE's own
  report resources, in the US or SI units set in Preferences. Its phases, rows and
  columns are the engine's — for example SIM START, IMPACT, SEPARATION and
  FINAL/REST for EDSMAC4 and SIMON, or one row per user-entered path position
  for EDGEN.
- Before a run, or for an engine that builds no Accident History page, HVE
  Reports says so (SINGLETRACK, HVE Studio's motorcycle model, builds no pages).

## Saving the Accident History

At the bottom of the HVE Reports window, with **ACCIDENT HISTORY** as *this
page* (click its tab or inside the page; the window then reads
*This page: ACCIDENT HISTORY*):

- **Save This Page** writes it as plain text to the file named in the first
  field (default `hve_report.txt`), laid out in spaces as the engine prints it.
- **Save Page as HTML** writes it to the file named in the second field
  (default `hve_report.html`), laid out as tables. Open it in a browser to
  print it, or print it to PDF.
- **Save All Pages** and **Save All Pages as HTML** write every page of the
  run instead, in the order and with the pages set in **Print Order...**.
- **Export Run Report (HTML)** writes `run_report.html`, HVE Studio's own printable
  summary of the run — its inputs, key results and a plan view of the
  trajectories. It is not an accident history.

A file name without a folder is saved beside the case file, and the window
shows the full path of the file written.

!!! note "HVE Studio"
    Earlier versions of HVE Studio had a separate accident history
    window: HVE Studio's own table, re-derived from the output track (Start / At
    Impact / At Separation / At Final/Rest), with its own **Save** button. It
    took its impact and separation instants from the run's recorded impact time
    and duration rather than from the engine's own collision history, so it
    could disagree with the engine's ACCIDENT HISTORY page for the same run.
    That window has been retired, and so has its menu item; the engine's
    page in HVE Reports is the one Accident History.

    For EDSMAC4 and SIMON, how the engine decides when a collision starts and
    ends is set by the **Accident History Basis** calculation option (see
    [EDSMAC4](../10-calculation-options/CalcOptEDSMAC4.md#accident-history) and
    [SIMON](../10-calculation-options/CalcOptSIMON.md#collision-history-and-connections));
    the two engines store that option with opposite meanings, and each options
    window is labeled for its own engine.

!!! note "HVE Studio"
    Delta-V and the other results in the units set in Preferences are in
    **Key Results** and the **Output Graph**, and **Output › Export
    Variables...** writes them to a file.

<!-- NAV -->

---

← Previous: [Reports & Output](README.md)  |  [Index](README.md)  |  Next: [Collision Pulse In-Use Factors Dialog Box](ColPulFact.md) →

<!-- /NAV -->
