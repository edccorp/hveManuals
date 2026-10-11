# Appendices VII, VIII and IX — Reserved

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Appendices VII–IX, adapted for HVE 2027.*

The following appendices were reserved (placeholder) sections in the
original edition and contained no substantive content:

## Appendix VII — Developer's Toolkit Overview

*(Reserved.)*

> **NOTE:** Contact EDC for information about receiving a copy of the HVE
> Developer's Toolkit.

The HVE Developer's Toolkit is documented separately; see also references
1.2 and 1.3 in [Appendix VI](appendix-06-references.md).

!!! warning "Not in HVE 2027"
    HVE 2027 has no Developer's Toolkit and does not load third-party calculation models; its models are built into the program.

## Appendix VIII — Databases

*(Reserved.)* HVE's human, vehicle and tire databases are discussed in
Chapter 2 (Using HVE) and in the Human and Vehicle Editor chapters. The
database files reside in the `supportFiles\db` directory (see
[Appendix I, HVE File System](appendix-01-installation.md)).

!!! note "HVE 2027"
    HVE 2027 reads HVE's vehicle databases (`.db`); see [Cases and Files](../../getting-started/04-cases-and-files.md#vehicle-databases) for where it looks for them. It reads no human database: a human is generated in the Human editor (GEBOD) or comes with an imported `.hve` case.

## Appendix IX — Quick Reference

*(Reserved.)*

!!! tip "New in HVE 2027"
    **Keyboard quick reference.**

    | Keys | Action |
    |---|---|
    | F2 / F3 / F4 / F5 / F6 | Human / Vehicle / Environment / Event / Playback editor |
    | Ctrl+N, Ctrl+O, Ctrl+S | New case, Open case, Save case |
    | Ctrl+R | Run Simulation (Event editor) |
    | Ctrl+P, Ctrl+D, Ctrl+M, Ctrl+U, Ctrl+W, Ctrl+T | Position / Velocity, Driver Controls, Damage Profiles, Collision Pulse, Wheels, Contacts (Event editor, when the item is offered for the method) |
    | Ctrl+Z; Ctrl+Y or Ctrl+Shift+Z | Undo; redo (not while a run's results are on screen, nor inside a text field) |
    | C / Shift+C | Look through the next / previous saved camera |
    | I | Insert a key on the camera being looked through |
    | Delete or X | Delete the selected path-follower waypoint in the 3-D view |

    With the pointer over the 3-D view:

    | Keys | Action |
    |---|---|
    | 1, 3, 7 (Ctrl for the opposite) | Front (rear), right (left), top (bottom) view |
    | 9 / 5 / . | Opposite view / perspective–orthographic / frame the selected vehicle |
    | 4, 6, 8, 2 | Orbit in 15° steps |
    | G, R | Move, rotate the selected vehicle (Event editor); then X, Y, Z to lock an axis, a number to type an exact value, Enter to apply, Esc to cancel, Ctrl to snap |
    | Tab | Edit Mode (Vehicle editor) |
    | Esc | Clear the environment surface selection |

    With the pointer over the Outliner: **H** hides the selection, **Alt+H** shows everything.

    Mouse in the 3-D view: left-drag orbits, right-drag pans, the wheel zooms; middle-drag orbits, Shift+middle pans, Ctrl+middle zooms; a left double-click resets the camera. See [Chapter 19](../08-3d-editor/19-using-3d-editor.md#navigating-the-3-d-view) and [Chapter 21](../08-3d-editor/21-manipulators.md).

<!-- NAV -->

---

← Previous: [Appendix VI — References](appendix-06-references.md)  |  [Index](README.md)  |  Next: [Appendix X — Index (Topic Locator)](appendix-10-index.md) →

<!-- /NAV -->
