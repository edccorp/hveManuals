# Section Nine: Video Output

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Section Nine "Video Output", adapted for HVE Studio.*

HVE has an integrated video output interface that records a simulation as a movie file. This section of the manual describes that interface and what HVE Studio offers in its place.

!!! note "HVE Studio"
    **File › Record Animation…** records the 3-D playback of a solved event (or playback sequence) to a Motion-JPEG AVI file — through the camera you choose, between the start and end times you choose, in real time or slow motion, with the [Results HUD](../../new-features/11-results-hud.md) burned in if you wish — and **File › Play Video…** plays such a file. HVE's compressor choice, single-frame output and recording to devices are not offered. For a rendered movie, export the solved scene to **Blender** (**File › Export Scene for Blender**, or **File › Blender Live Link…**) and render it there. See [Chapter 27](27-video-interface.md).

Users new to the subject of video output will find this section both informative and important. Producing high-quality video requires knowledge and experience. This section includes several tips aimed at improving the resulting output.

## General Procedure

To make a movie of an HVE Studio simulation, perform the following steps:

1. Use the Event editor to create and run one or more simulation events.
2. Optionally combine several events on one timeline in the **Playback (F6)** editor, save cameras with **Tools › Cameras…** (fixed, following, onboard or keyframed), and set up the numbers to show in **View › Results HUD**.
3. Choose **File › Record Animation…**, set the output file, size, frame rate and quality, the camera and the start and end times, tick **Burn in key results (Results HUD)** if wanted, and press **Record**.

For a rendered movie instead, export the solved scene with **File › Export Scene for Blender** (or start **File › Blender Live Link…** and connect from Blender), then in Blender choose the camera, frame rate, resolution and output format and render the animation.

## Overview of Section Nine

- [Chapter 26 — Video Basics](26-video-basics.md) provides an overview of video basics. This is an informative chapter for those new to the subject of computer-generated video. Much of its broadcast/tape material is legacy reference, but the tips on composing and recording simulation video remain useful.
- [Chapter 27 — Using The HVE Video Interface](27-video-interface.md) describes HVE's video interface, HVE Studio's Record Animation and Play Video, and the export to Blender.

See also Lesson 4 (Creating a Video) of the [HVE Tutorial](../11-appendices/32-tutorial.md).

<!-- NAV -->

---

Next: [Chapter 26 — Video Basics](26-video-basics.md) →

<!-- /NAV -->
