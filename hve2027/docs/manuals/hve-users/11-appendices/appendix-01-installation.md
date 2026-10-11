# Appendix I — Installation & Setup

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Appendix I, pages I-1 through I-10, adapted for HVE 2027.*

HVE's Appendix I gives the hardware requirements, the CD-ROM installation procedure, the EDKEY and hard-disk license locks, and the layout of HVE's file system.

!!! note "HVE 2027"
    HVE 2027 is installed and started differently from HVE: see **[Installing and running HVE 2027](../../getting-started/02-installing-and-running.md)**. The sections below say, for each part of HVE's appendix, what applies to HVE 2027.

## System Requirements *(legacy)*

HVE's original edition required a Windows PC with an OpenGL graphics card, a 3-button mouse and a video output device.

!!! note "HVE 2027"
    HVE 2027 Preview runs on 64-bit Windows; a browser version and a read-only viewer exist as well (see [Installing and Running](../../getting-started/02-installing-and-running.md)). It needs a graphics driver with OpenGL 3.3. A 3-button mouse (or a wheel mouse) is recommended: the middle button orbits, pans and zooms the 3-D view ([Chapter 19](../08-3d-editor/19-using-3d-editor.md#navigating-the-3-d-view)). No video output device is used. The installation chapter gives the current requirements.

## HVE Software Installation *(legacy)*

HVE was installed from CD-ROM with a setup program, followed by the license lock described below.

!!! note "HVE 2027"
    Follow [Installing and running HVE 2027](../../getting-started/02-installing-and-running.md). There is no CD-ROM and no license step.

## Software Security and Protection *(legacy)*

HVE was protected by a license lock to the computer's hard disk or to an EDKEY hardware key on the parallel port.

!!! warning "Not in HVE 2027"
    HVE 2027 has no license lock, no EDKEY and no license tiers (for example, there is no separate HVE-CSI mode: the full editors are always available).

### Lock to Your Computer's Hard Disk

Not applicable to HVE 2027.

### Lock to Your EDKEY

Not applicable to HVE 2027.

## HVE File System

It is important that users of HVE know and understand its file system in order to perform system maintenance as well as to copy files between computer systems.

!!! note "HVE 2027"
    HVE 2027 does not need HVE's directory tree, but reads HVE's own files where they are:

    - **Cases** — **File › Open Case…** opens an HVE `.hve` case from any folder, as well as HVE 2027's own `.hvc` and `.json` cases. HVE 2027 does not write `.hve` files. A case refers to vehicle meshes and site geometry by file name; **File › Publish Bundle…** writes the case, the meshes it names and the solved results into one folder that opens on another computer, and **File › Embed the environment in the case** stores the site inside the case.
    - **Vehicle databases** — HVE's vehicle databases (the `.db` files of `supportFiles\db`) are listed in the vehicle picker when HVE 2027 finds them: beside its executable, in folders added from the picker, and in a folder of the user's own for vehicles saved from HVE 2027 (see [Cases and Files](../../getting-started/04-cases-and-files.md#vehicle-databases)). There are no human database files: humans are generated in the Human editor or come with an imported case.
    - **Geometry** — vehicle `.h3d` and `.iv` meshes and environment geometry are read from wherever the case or vehicle record points.
    - **System files** — HVE 2027 does not use `language.rsc`, `units.us`, `units.si` or `hve.cfg`. The unit system and other preferences are set in **Tools › Preferences…** and kept in HVE 2027's own preferences file.
    - **Movies** — **File › Record Animation…** writes a Motion-JPEG `.avi` wherever its Output File names; there is no movie directory ([Section Nine](../09-video-output/README.md)).

*Figure I-1 — HVE File System diagram.*

**Table I-1 — Directory Names and Descriptions**

| Directory Name | Description |
| --- | --- |
| `hve` | Main installation directory for HVE |
| `hve\supportFiles` | Root subdirectory for the various support file systems required by HVE |
| `hve\supportFiles\case` | Subdirectory containing all HVE case files |
| `hve\supportFiles\images` | Root subdirectory for all image files (2-D bitmaps and 3-D geometry) |
| `hve\supportFiles\images\humans` | Subdirectory containing 2-D bitmap and 3-D geometry files for humans |
| `hve\supportFiles\images\vehicles` | Subdirectory containing 2-D bitmap and 3-D geometry files for vehicles |
| `hve\supportFiles\images\environments` | Subdirectory containing 2-D bitmap and 3-D geometry files for environments |
| `hve\supportFiles\images\movies` | Subdirectory containing movie files (e.g., AVI) created using the Playback Editor, and (in a `frames` subdirectory) single-frame image output *(updated: the original table printed this as `supportFiles\movies`; HVE places movies under `supportFiles\images\movies` — in current installations under the public user directory, e.g. `C:\Users\Public\HVE\supportFiles\images\movies` — and the location may be overridden in the Video Options dialog)* |
| `hve\supportFiles\db` | Subdirectory containing human, vehicle and tire databases; also contains location and vehicle contact surface materials databases |
| `hve\supportFiles\colPulse` | Subdirectory containing user-saved collision pulse files |
| `hve\supportFiles\sys` | Subdirectory containing various HVE system and resource files |

**Table I-2 — Files in `\hve` directory**

| File Name | Description |
| --- | --- |
| `hve` (executable) | HVE executable |
| `hve*.lic` | HVE license file |

**Table I-3 — Files in `\hve\supportFiles\sys` subdirectory**

| File Name | Description |
| --- | --- |
| `language.rsc` | Resource file for HVE; contains text strings, unit name format and error/warning ranges for each parameter in the user interface. Also contains all units conversion factors (used for converting user units to program units) |
| `<phys_model>.rsc` | Resource file for each installed reconstruction or simulation model (contains text strings for all output report strings) |
| `units.si` | Resource file for SI (metric) units; contains user name string for each program unit |
| `units.us` | Resource file for US units; contains user name string for each program unit |
| `hve.cfg` | Configuration file; saves current user preferences and other parameters on HVE shutdown |

<!-- NAV -->

---

← Previous: [Chapter 32 — HVE Tutorial](32-tutorial.md)  |  [Index](README.md)  |  Next: [Appendix II — Messages](appendix-02-messages.md) →

<!-- /NAV -->
