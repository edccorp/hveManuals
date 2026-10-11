# Sky Attributes Dialog Box

Sky attributes determine the appearance of the background and the lighting of the scene. In HVE 2027 the sky and its lighting are part of the scene's **world**, edited in the **Shader Editor** (**View › Shader Editor**). The Environment Editor's **Environment** panel has a **Sky** section that summarizes the sun (azimuth, elevation, whether it comes from the location and time or is set by hand, its strength) and the ambient light, with an **Edit the sun and sky...** button that opens the Shader Editor on the world.

## Ambient Light Intensity
**Ambient Light**, a slider from 0 to 1 in the Shader Editor's **Sun & Sky** section. It may be used for visualizing various levels of daylight, dusk/dawn and darkness.

## Set Sky Color
The sky's color and brightness come from the world's shader nodes (a sky texture or a background color) in the Shader Editor.

## The sun (Sun & Sky section)
Not in HVE's Sky Attributes dialog, but part of the sky in HVE 2027: **Set by hand** (**Sun Rotation**, **Sun Elevation**) or **From location and time** (latitude, longitude, date and time, UTC offset, daylight saving, north direction, with a choice of sun-position method and refraction), **Sun Light** (strength) and **Reset sun to default**.

!!! warning "Not in HVE 2027"
    **Fog Type** (None, Haze, Fog, Smoke), **Visibility** and **Set Fog Color**: there is no distance fog. (The sky texture node has a *Haze* setting, which changes the color of the sky, not the visibility of objects.)

!!! note "HVE 2027"
    The sky and the sun are display only: they change the picture, not a result.

<!-- NAV -->

---

← Previous: [Set Grid Dialog Box](SetGridDlg.md)  |  [Index](README.md)  |  Next: [Text Editor Dialog Box](TextEdDlg.md) →

<!-- /NAV -->
