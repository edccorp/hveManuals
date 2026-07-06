# Chapter 26 — Video Basics

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh
Edition, January 2006), Chapter 26, pages 26-1 through 26-14. Verified against the current HVE application source
(`HVEINV-64/`).*

This chapter provides a general overview of the process of producing video
output from HVE (many sections of this chapter apply to any video device).
Beginners will learn a lot about the subject, while users with advanced
knowledge will find much of this chapter unnecessary. However, all users
should understand the information contained in this chapter before attempting
to produce their first video.

*(updated: Current HVE records video directly to compressed AVI/MPEG movie
files (or single-frame image files) using standard Windows codecs — it no
longer drives external video tape recorders. The sections below on tape
formats, broadcast standards, color encoding and recording media are retained
as **legacy reference** for users producing physical video media from their
rendered movies; the sections on recording methods, compression and the Tips
and Suggestions remain directly applicable.)*

## Overview

This chapter contains the following sections:

- Why Video
- Computer Graphics vs Video
- Typical System Layout *(legacy)*
- Basic Procedures
- Recording Methods
- Video Compression
- Video Communication Set-up *(legacy)*
- Preparation of Recording Media *(legacy)*
- Broadcast Standards *(legacy)*
- Color Encoding *(legacy)*
- Video Formats and Recording Quality *(legacy)*
- Tips and Suggestions

## Why Video?

Video is different from photographs or diagrams in that it shows motion. The
benefits from this fact are numerous:

- **Realism** — The life-like appearance and motion are easily understood by
  non-technical individuals, and also illustrate how the sequence appeared
  from any perspective.
- **Time vs Distance Studies** — The ability to visualize the motion allows
  the researcher to illustrate relative position vs time.
- **Visibility and Avoidability Studies** — The ability to visualize position
  vs time allows the user to understand more about a driver's opportunity to
  avoid a crash.

The fact that video motion is displayed at a fixed frame rate also makes it
possible to produce and confirm real-time output. Thus, video is useful as an
analytical tool as well.

Video is perhaps most useful because of its universal viewability: a movie
file sent to your clients may be viewed easily and conveniently. *(updated:
the original text emphasized the widespread availability of VCRs; today the
equivalent is that an AVI or MPEG file plays on any computer, and is easily
converted for DVD, web or courtroom presentation.)*

## Computer Graphics Vs Video

Computer-generated graphics differs from broadcast video in a number of ways.
Understanding these differences will help users produce better results using
the HVE Video Interface. Some of the differences include:

- **Interlacing** — In most video standards, each row of pixels is drawn
  every other time the monitor is refreshed. This is called *interlacing*.
  In contrast, computer graphics monitors typically draw every row of pixels
  every time the screen is refreshed. This is called *non-interlaced*
  (progressive).
- **Broadcast Standards** — The world historically employed three different
  analog video standards: NTSC, PAL and SECAM. These standards are described
  later in this chapter (see Broadcast Standards).
- **Tape Formats** — Several video tape recording formats existed, such as
  VHS, S-VHS and Betacam. These formats are described later in this chapter
  (see Video Formats).
- **Color Encoding** — Several color-encoding methods are used, including
  RGB (component), YUV (component), YIQ (component), YC (several types) and
  composite video. These methods are described later in this chapter (see
  Color Encoding).

## Typical System Layout *(legacy)*

A typical (legacy) video system layout included the computer, video hardware,
video interface software, simulation software, animation controller, video
recorder, VHS deck and television monitor.

*Figure 26-1 — Typical System Layout. The control signal from the serial port
is used for single-frame recorders and is not required for systems using a
video compressor.*

*(updated: a current HVE video "system" is simply the computer itself — HVE
renders the playback window to a movie file on disk. No external recorder or
serial control connection is used.)*

## Basic Procedures

No matter what system configuration is used, recording a simulation sequence
involves the same basic procedures:

1. Set up the video options (format, size, frame rate, compressor).

   > **NOTE:** You should only need to do this once; the settings are stored
   > in HVE's configuration file.

2. Using HVE, create the simulation sequence to be recorded.
3. Record the video (to a movie file in current HVE; to tape on legacy
   systems).
4. Replay the movie to confirm it is properly recorded.
5. Distribute copies to your clients (on legacy systems this meant copying
   the master tape from the professional video system to VHS).

Refer to [Chapter 27, Using the HVE Video Interface](27-video-interface.md),
for detailed, step-by-step procedures and examples.

## Recording Methods

The three basic methods of recording computer graphics on video are:

- Recording Live From Screen
- Single-frame Recording
- Real-time Recording

Each of these methods has advantages.

### Recording Live From Screen

Recording live from the computer screen is the simplest form of recording
(e.g., a screen-capture utility, or on legacy systems a VCR wired to the
display output). It requires no special recording interface: anything
displayed on the computer screen is transferred to the recording. However,
there is no control over frame rate; thus, there is no constant relationship
between the time domain in the recorded sequence and real time. Because of
this major limitation, recording live from screen is not generally useful for
recording real-time simulations.

### Single-frame Recording

Single-frame recording involves the controlled transfer of individual
computer-generated images to the recording medium one frame at a time. The
advantage of single-frame recording is that the frame rate is carefully
controlled (normally 25 or 30 frames per second, depending on the video
standard used for recording). Thus, when results recorded using single-frame
recording are played back, the sequence is shown in real time (i.e., 1.0
second of recorded simulation is exactly one second on a stopwatch).

*(legacy)* On tape-based systems this process required special video hardware
and software and a computer-controlled, frame-accurate video tape recorder
(VTR), and owing to the required pre-roll and post-roll it took about 10
seconds to record each frame (about 25 minutes to record a 5-second
simulation sequence).

*(updated: current HVE offers a **Single Frames** video format option in the
Video Options dialog which writes each rendered frame to an individual image
file — useful for producing frame-accurate stills or for assembling video in
an external editing package.)*

### Real-time Recording

Real-time recording also involves the controlled transfer of individual
computer-generated images, but the individually rendered frames are first
transferred to the computer's hard disk, where they are stored in a movie
file. After all the frames are rendered and stored, the file plays back in
real time. This is the method used by current HVE: each frame of the playback
sequence is rendered and appended to a compressed AVI (or MPEG) file at the
selected frame rate; the resulting movie is then played back in real time in
the Playback Window (or any media player). The sequence may be previewed on
the computer's monitor before it is distributed.

To achieve real-time frame rates for complex scenes, the frames are
compressed. A video compressor reduces the amount of storage required for
each frame by eliminating or reducing the number of pixels having the same
color and intensity. The trade-off is a slight loss of quality, although
modern video compression algorithms produce excellent results. Both hardware
and software compression are available; current HVE uses the software codecs
installed in Windows.

## Video Compression

Rendering a single frame of video takes a while. Even a powerful computer
graphics system cannot render a complex scene fast enough to display in real
time (i.e., 25–30 frames per second). One solution to this limitation is to
compress the data in each frame of video and store the result on the
computer's hard disk. Once this is done, the frames may be played back in
real time from the disk to the screen.

Several types of video compression exist. Two of the most popular families
are:

- **MPEG** (Moving Picture Experts Group)
- **JPEG** (Joint Photographic Experts Group)

> **NOTE:** An AVI (Video for Windows) type video compression system is
> standard equipment on Windows computers. *(updated: HVE enumerates the
> codecs installed in Windows through the standard compressor-selection
> dialog; "Full Frames (Uncompressed)" is used if no compressor is chosen.
> The legacy manual recommended the Cinepak codec, which is obsolete — use
> any modern codec installed on your system.)*

The selected compressor is chosen using HVE's Video Options dialog (see
[Chapter 27](27-video-interface.md)).

## Video Communication Set-up *(legacy)*

Before any video input or output could be performed on tape-based systems,
the computer's video hardware had to be configured to communicate with the
video device (e.g., video tape recorder). This process was called *video
communication set-up*, and the procedures were specific to the video output
device installed in the computer. *(updated: no such set-up is required in
current HVE — output goes directly to a disk file.)*

## Preparation of Recording Media *(legacy)*

The following procedures were recommended when recording to video tape:

- Use only high-quality tape. Be sure the correct type of medium is used.
  Never use regular VHS tape for S-VHS recording.
- Avoid the use of thin-based tape, such as tape longer than T-120.

  > **NOTE:** A typical simulation analysis requires less than 5 minutes of
  > tape; thus, it is convenient to use the shortest tape available.

- Prior to using the tape, pack the tape by running the VTR in fast forward
  to the end of the tape, then rewinding it.
- Start recording several minutes into the tape. Avoid recording in the
  leader area.
- Avoid reusing tapes that have already been used for recording. Use the
  tape only for limited playback, using it as a master copy for duplication
  onto regular VHS tapes for distribution to your clients.

  > **NOTE:** Legacy HVE video systems used special video formats requiring
  > professional broadcast video hardware. Because clients generally did not
  > possess such hardware, a consumer-quality VHS duplication of the master
  > tape was normally produced for distribution.

- Keep the VTR's mechanism clean and well maintained, according to the
  manufacturer's recommendations. If you suspect a tape is worn, do not
  insert it into the VTR; it may damage the mechanism.

## Broadcast Standards *(legacy)*

Broadcast standards, or video timing formats, are ways of encoding video
information for broadcast to television receivers. The three recognized
analog broadcast standards were:

- **NTSC (National Television Systems Committee)** — Used in all of North
  and South America, except Brazil, and much of East Asia.
- **PAL (Phase Alternated by Line)** — Used in the United Kingdom and
  Western Europe, except France, and in parts of East Asia, including
  Australia.
- **SECAM (Séquentiel Couleur avec Mémoire)** — Used in France, Eastern
  Europe, the Near East and Mideast, and in parts of Africa and the
  Caribbean.

NTSC uses a total of 525 horizontal lines per frame, with two fields of 262.5
lines each. Each field refreshes at 60 Hz (actually 59.94). NTSC encodes
brightness, color and synchronizing information in the same signal.

PAL uses a total of 625 horizontal lines per frame, with two fields of 312.5
lines each. Each field refreshes at 50 Hz. PAL encodes brightness, color and
synchronizing information in the same signal, but in a different way from
NTSC.

SECAM transmits the same number of lines at the same rate as PAL, but
transmits each color difference signal on alternating lines, using frequency
modulation for the subcarrier.

> **NOTE:** The actual lines of active video are fewer than the total lines
> noted above. Typically, NTSC displays 485 lines and PAL displays 575
> lines. The remainder are used for synchronizing and other information.

*(updated: analog broadcasting has been replaced by digital television; the
30 fps (NTSC) and 25 fps (PAL) frame-rate conventions survive in current
video work. HVE's Video Options dialog offers movie sizes from the default
window size through DVD, 480p, 720i, 1080i, 1080p and 4K, with a selectable frame
rate.)*

## Color Encoding *(legacy)*

Color encoding refers to how the video signal is generated and conducted
between devices (e.g., computer and recorder). The common methods are:

- RGB (3-component signal)
- YUV (3-component signal)
- YIQ (3-component signal)
- YC (2-component signal)
- Composite Video (1-component, single signal)

### RGB

RGB is the color encoding method used by most computers, as well as some
professional-quality video cameras. The three colors red, green and blue are
generated separately and carried on three separate wires.

### YUV

YUV is a 3-signal (and 3-wire) method used by PAL and some video cameras and
VCRs. Like RGB, YUV is also a component color-encoding method, but instead of
conducting individual colors, YUV carries the brightness, or *luminance*, on
the Y signal, and color, or *chrominance*, on the U and V signals. YUV color
encoding can be recorded digitally, according to the CCIR 601 standard. This
recording technique is referred to as D1.

### YIQ

YIQ is a 3-signal (and 3-wire) method typically used by the NTSC format.
Like YUV, it encodes luminance onto one signal, Y. It encodes color onto two
signals, called I and Q (intermodulation and quadrature, respectively), that
differ from the method used by YUV.

### YC (YC-358, YC-443, or S-Video)

YC is a two-wire signal that uses luminance (Y) and chrominance (C). YC
results when I and Q are combined into a single color signal, C. YC-358 is
the most common NTSC version of this format; YC-443 is the most common PAL
version. These formats are also known as S-Video, and are used in S-VHS
recorders.

### Composite Video

The composite color-encoding methods encode the brightness and color into a
single signal. There are NTSC and PAL versions of this format.

## Video Formats and Recording Quality *(legacy)*

Video recorders were available for analog and digital recording in a number
of formats. They were also informally classified according to Consumer,
Industrial/Professional and Broadcast market types, a measure of recording
quality (Consumer being the lowest quality and Broadcast being the highest
quality).

### Analog Formats

The following were the available analog videotape formats:

- **VHS** — Consumer quality format using a composite signal
- **S-VHS** — Consumer quality format using a YC or composite signal
- **S-Video** — Consumer and Industrial/Professional quality format using a
  YC-358 or YC-443 signal
- **Beta** — Consumer quality format using a composite signal
- **8mm** — Consumer quality format using a composite signal
- **Hi-8mm** — Consumer and Industrial/Professional quality format using a
  composite or YC signal
- **U-Matic** — Industrial/Professional quality format (SP) cassette, 3/4
  inch, using a composite signal
- **Type C** — Broadcast quality format, reel-to-reel, 1 inch tape, using a
  composite signal
- **Type B** — Broadcast quality format (Europe) using a composite signal
- **Betacam** — Broadcast quality format using a component (RGB) signal
- **Betacam SP** — Broadcast quality format using YUV, YIQ or composite
  signal
- **MII** — Broadcast quality format using YUV, YIQ or composite signal

*Figure 26-2 — Video Panel (Analog Video Input Source), used on legacy
systems when the video communication was set up.*

### Digital Formats

The available digital tape formats were D1 525 (YUV), D1 625 (YUV), D2 525
(NTSC) and D2 625 (PAL). All digital formats were used in post-production and
were typically not used for recording original information.

## Tips and Suggestions

Video differs from computer graphics in many ways. By being aware of these
differences, the video quality may be greatly improved. Some important issues
are addressed below.

### Color Saturation

Video recording devices do NOT record saturated colors well.

> **NOTE:** A saturated color is 100 percent red, blue or green (as defined
> by its RGB values).

Objects with saturated colors seem to have a halo and tend to glow. When
assigning any color value using an HVE color wheel editor or slider, choose
values less than 256 (move the hot spot slightly away from the edge of a
color wheel and the right end of the brightness slider).

### Anti-aliasing

Anti-aliasing significantly increases rendering time. There is really no
benefit to anti-aliasing until you want to produce a video. At this point,
use the Rendering Options dialog to increase the Anti-aliasing value to about
3 (on a scale of 1 to 10; the improvement becomes less and less visible as
anti-aliasing is increased).

### Keep Objects Close

This suggestion simply comes from experience. Closer objects look better and
tend to command your attention. Objects farther away lose their definition
and become lost in the environment.

### "Camera Car"

Pretend you are directing an action movie. As the vehicle moves through the
scene, you want to follow it! A single view from a distance would not focus
on the items of importance and would not connect with the viewer. The
solution is to move the camera along with the vehicle.

Using HVE, you can create a *Camera Car*. A camera car is a vehicle to which
you have attached a camera.

> **NOTE:** See View Menu, Camera Set-up (Object-based Cameras).

Set up an event that moves this camera through the scene and points towards
the desired action. This takes a little planning and practice, but has a huge
payback. You'll also know the exact position of the view at each timestep
(this information is available from the camera car's Variable Output Window).

### Sizing Issue (TV will crop)

Nearly all video display devices crop some information (in addition to issues
related to saturated colors, described earlier). View your results on the
actual presentation display (television, projector, courtroom monitor) before
you send anything to a client. By viewing the results on the target display,
you will confirm the quality as well as the actual information displayed on
the screen.

### Flicker

Horizontal white lines cause flicker! This is true of even the very best
broadcast video systems. (Have you ever seen the TV weatherman wear a tie
with horizontal white stripes? Probably not very often.)

Think about your environment when composing your view. If the viewer is
filled with pavement stripes or other information running horizontally across
the screen, adjust the viewer to a slightly oblique view. The result will be
significantly better.

### Computer to S-VHS to VHS, Not Computer to VHS *(legacy)*

On tape-based systems, although creating composite video directly on the VTR
might have seemed more efficient, the quality was not as good as creating an
S-VHS master first and using it for composite copies. *(updated: the modern
equivalent of this advice is to keep a high-quality, lightly compressed
master movie file, and produce more heavily compressed copies for
distribution from that master rather than re-recording.)*

### Tape Problems *(legacy)*

Use the tips listed under *Preparation of Recording Media*, earlier in this
chapter, to avoid problems that may occur during recording of real-time
simulations to video tape.

### Screen Saver, Other Windows on top of Playback Window

HVE's video sub-system reads the rendered contents of the playback window
region of the computer's frame buffer. As it turns out, a lot of objects can
draw into this area! To help prevent unexpected results, do the following:

- Turn off the screen saver. Otherwise, your video may turn black when the
  screen saver comes on!

  > **NOTE:** Remember, it can take up to 25 minutes or more to record a
  > 20-second simulation movie if you have used a highly detailed
  > environment model, a moving camera position and increased settings for
  > anti-aliasing and render quality. If you walk away and return when it's
  > done, you might be surprised about half-way through the sequence!

- Be sure there are no windows or dialogs lying within the limits of the
  Playback Window. These will appear in your video!
- Make sure the mouse cursor isn't sitting within the window!

<!-- NAV -->

---

← Previous: [Section Nine: Video Output](README.md)  |  [Index](README.md)  |  Next: [Chapter 27 — Using The HVE Video Interface](27-video-interface.md) →

<!-- /NAV -->
