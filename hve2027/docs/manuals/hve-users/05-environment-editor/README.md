# Section Five — Environment Editor

The purpose of the HVE Environment Editor is to provide the physical and
visual environmental attributes which may interact with humans and vehicles
during the execution of a reconstruction or simulation model. This section
of the HVE User's Manual describes how to create and edit these environment
models. It also provides an overview of the environment model parameters.

The basic physical/mathematical model of the environment provides the
following information:

- An atmosphere, that may be used for modeling aerodynamic forces on humans
  and vehicles.
- Fog, haze or smoke in the atmosphere, that may be used to study
  visibility attenuation.
- A sun that is positioned according to the local latitude, longitude and
  time zone, along with the time and date and angle of the earth-fixed
  coordinate system.

!!! warning "Not in HVE 2027"
    Fog, haze and smoke visibility is not modelled; HVE 2027 cannot be used for HVE's
    visibility studies. See
    [Chapter 12](12-creating-editing-environments.md).
- The physical environment gravitational constant and surfaces that may be
  used to model interaction forces (i.e., tires and human and vehicle
  exteriors).

## General Procedure

To use the Environment Editor, perform the following steps:

1. Select Environment mode: click the **Environment (F4)** tab under the
   menu bar, or press F4.
2. Edit the case's environment in the **Environment** panel. Every case has
   one environment; a new case starts with a default one, and an HVE case
   (`.hve`) opened with File › Open brings its own site with it.
3. Import the site geometry — the roads, curbs, sidewalks and other surfaces
   with which the humans and vehicles may interact — from an `.h3d`, `.iv`,
   `.wrl`, `.obj`, glTF or DXF file, and set the contact material of each
   surface. These objects also provide an extremely important visual
   context for accident causation.
4. Optionally lay a scaled aerial photograph on the ground, add scene boxes,
   or show a survey point cloud, for visual context.

!!! note "HVE 2027"
    HVE 2027 has no 3-D Editor for building roads and objects; site geometry
    is made in another program (or comes with an HVE case) and imported.
    There is no "Previous" environment to add from another case. See
    [Chapter 12](12-creating-editing-environments.md).

## Overview of Section Five

This section provides a detailed explanation of the process of creating and
editing environments, and also presents a detailed overview of the
environment model's physical properties:

- [Chapter 12 — Creating & Editing Environments](12-creating-editing-environments.md)
  describes the process of creating and editing environments.
- [Chapter 13 — Environment Model Definition](13-environment-model-definition.md)
  provides a detailed overview of the HVE Environment Model.
- Chapter 14 (reserved — a RoadTools overview placeholder in the legacy
  edition).

Dialog references for this section are collected in the
[Environment Dialog Reference](../../08-environment/README.md).

<!-- NAV -->

---

Next: [Chapter 12 — Creating & Editing Environments](12-creating-editing-environments.md) →

<!-- /NAV -->
