# Light Editor Dialog Box

The Light Object Tool allows the user to create and edit light sources. Lights are objects that cast light on other objects, making them visible.

Lights are unique in several ways:

- You cannot see them, only the effects caused by them (i.e., other objects are lit up).
- Lights cannot be grouped like other objects can. This means you cannot create a streetlight that includes a light source that moves when you move the streetlight; instead, you must re-attach the light after you have positioned the pole.

The Light Editor dialog provides the following options:

## Coords (ft) — X, Y, Z

The coordinates of the light source. Used for *Point* and *Spot* lights; for *Directional* lights the position values are simply ignored (a directional light illuminates from a direction, not a location), although the fields remain enabled.

## Angle (deg) — Azimuth, Zenith

The direction in which the light points, entered as an azimuth (heading) angle and a zenith (angle from vertical). These fields are used for *Directional* and *Spot* lights. (Earlier versions of this dialog used Roll/Pitch/Yaw angles; the current dialog uses Azimuth/Zenith.)

## Global / Local

A combo box selecting whether the entered coordinates and angles are interpreted in the global (environment) coordinate system or the object's local coordinate system.

## Light Is On

Check box that activates and deactivates the light source.

## Type

- **Point** — The light source is located at user-specified coordinates and radiates light in all directions. An example is a light bulb.
- **Directional** — The light source illuminates uniformly along a specified direction. Its location is not used. An example is the sun.
- **Spot** — The light source is located at user-specified coordinates and radiates a beam of light. An example is a headlight on a car.

## Color...

Displays the Color dialog, used to specify the light's color.

## Intensity

The brightness of the light (slider and edit field).

## Drop-off Rate

For *Spot* lights only, the rate at which the light attenuates from the center of the beam to its edge.

## Cone (deg)

For *Spot* lights only, the included angle of the cone of light.

## Apply

Applies the current settings to the selected light.

---
*Source topic: LightEdDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Key Results Dialog Box](KeyResDlg.md)  |  [Index](README.md)  |  Next: [Object Attributes Dialog Box](ObjAttrDlg.md) →

<!-- /NAV -->
