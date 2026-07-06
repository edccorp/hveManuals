# Section Nine: Video Output

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Section Nine "Video Output". Verified against the current HVE application source (`HVEINV-64/`, in particular `AviWrite.cpp`, `VideoDlg.cpp`, `VideoOptionsDlg.cpp`, `CVideoWndPlay.cpp` and `PlayBackDlg.cpp`).*

HVE has an integrated video output interface. This interface makes it quick,
simple and convenient to record a simulation as a video. This section of the
manual describes HVE's video interface.

*(updated: The original edition of this section was written when HVE drove
external video tape recorders (VTRs) over a serial connection and through
add-in video-out hardware. Current HVE records simulation movies directly to
compressed **AVI** (or MPEG) files on disk using standard Windows codecs, and
can also write individual frame image files. The tape-deck-specific material
is retained below where it is still informative, but is clearly flagged as
legacy.)*

Users new to the subject of video output will find this section both
informative and important. Producing high-quality video requires knowledge
and experience. This section includes several tips aimed at improving the
resulting output.

## General Procedure

To use the HVE Video Interface, perform the following steps:

1. Use the Video Options (Video Set-up) dialog to select the video format
   (movie and/or single frames), movie size, frame rate and an optional video
   compressor (codec).
2. Use the HVE Event Editor to create one or more simulation events.
3. Use the HVE Playback Editor (Video Creator) to combine the events into a
   single Playback Window.
4. Use the Playback Controller to choose the Video Source (Playback Window or
   a previously recorded movie file) and Video Destination (Video File or
   Playback Window).
5. Use the Playback Controller to record the results from the selected Video
   Source to the selected Video Destination.

## Overview of Section Nine

This section provides a detailed explanation of the process of creating and
editing 3-D videos produced directly from HVE simulations:

- [Chapter 26 — Video Basics](26-video-basics.md) provides an overview of
  video basics. This is an informative chapter for those new to the subject
  of computer-generated video. Much of its broadcast/tape material is legacy
  reference, but the tips on composing and recording simulation video remain
  useful.
- [Chapter 27 — Using The HVE Video Interface](27-video-interface.md)
  provides a detailed overview of the HVE Video Interface.

See also Lesson 4 (Creating a Video) of the
[HVE Tutorial](../11-appendices/32-tutorial.md).

<!-- NAV -->

---

Next: [Chapter 26 — Video Basics](26-video-basics.md) →

<!-- /NAV -->
