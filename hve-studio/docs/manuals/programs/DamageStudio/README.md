# HVE DamageStudio

**Section Twelve of the HVE User's Manual — Version 8**

Updated Markdown edition, converted from the legacy manual and revised to match the behavior of the current HVE release, with notes on what HVE Studio provides in its place.

DamageStudio is a graphical analysis tool that allows vehicle crash safety engineers to visualize collision data, and to correlate collision damage with the kinetics (force magnitude and direction), delta-V, acceleration and other important collision parameters. In HVE, DamageStudio is a component in the HVE Playback Editor.

DamageStudio may be used to study all types of collisions (e.g., barrier, single vehicle, multi-vehicle, secondary impact, rollover, ...) for all types of vehicles (e.g., passenger car, van, truck, trailer, dolly, ...).

There are many uses for the kind of detailed collision information produced by DamageStudio. One example is the ability to directly compare simulated crush dimensions with a measured damage profile. This kind of analysis may also be used to fine-tune stiffness coefficients from staged collision data.

DamageStudio can also be used to identify the magnitude and direction of individual impulses, peak collision forces and delta-Vs for vehicles undergoing multiple impacts, even if the impacts are simultaneous.

## DamageStudio in HVE Studio

!!! warning "Not in HVE Studio"
    HVE Studio has no DamageStudio window. Its 3-D viewer with the Simulated,
    None, From File and User-entered views, the Damage Profile group (impulse
    number, CDC, PDOF, width and offset, number of zones, elevations, crush
    table), the color-coded crush vectors, the impulse-center sphere and the
    *Prev* / *Next* vehicle buttons are not available.

The collision data DamageStudio displays is computed by the physics engine,
which HVE Studio compiles from HVE's own source, so the numbers are there. They
are reached as follows:

- **The crushed vehicle** is drawn in the 3-D viewport after a run and follows
  the playback time — undamaged before contact, deforming through the impact.
  **Smooth crush deformation** in **Event › Vehicle Mesh** (Display tab, *Damage Display*)
  changes how it is drawn, not what was computed.
- **A crush heat map** can be made in the **Shader Editor** (View › Shader
  Editor): the *HVE Simulation* node's **Crush** output is how far each vertex
  of the body was crushed, in meters.
- **The collision force direction** is drawn by **View › Scene Display › Vectors ›
  Collision force** while the vehicles are in contact.
- **The DyMESH contact meshes** are drawn by the DyMESH overlay table in
  **View › Scene Display** (Vehicle group): the **DyMESH Body** row draws the
  collided body as a wireframe deformed by the run, crushed edges in red, and
  the **DyMESH Wheel** row each wheel's contact mesh. Each row's **Nodes** box
  draws the mesh's vertices.
- **The Damage Data report** — collision kinetics, damage profiles with CDC,
  and crush depth tables, per impulse — is the *DAMAGE DATA* page of **Output ›
  HVE Reports**, built by the engine exactly as HVE builds it.
- **Output › Damage Studio Report** tabulates the key results chosen in
  **Output › Damage Studio Options** and each vehicle's maximum recorded crush;
  see [The DamageStudio Interface](01-interface.md#damage-studio-report-hve-studio).

## General Procedure

To review collision damage in HVE Studio:

1. Set up a collision event (SIMON with DyMESH, or EDSMAC4) and run it
   (**Output › Run Simulation**, or **Run** on the playback bar).
2. Use the playback bar under the viewport to move through the event. The
   vehicle bodies deform as the collision proceeds.
3. Turn on **View › Scene Display › Vectors › Collision force** to see the collision
   force on each vehicle while it is in contact.
4. Open **Output › HVE Reports** and select the *DAMAGE DATA* tab for each
   vehicle's impulses, CDCs, damage profiles and crush depth tables.
5. If wanted, give the vehicle a material in the Shader Editor that maps the
   *HVE Simulation* node's **Crush** output to color, to see the crush depth
   over the body.

A measured damage profile — what DamageStudio's *User-entered* view edits —
is entered for an EDCRASH event in **Event › Event Information**, under
*Measured Crush (drives Delta-V)* (number of crush depths, C1…, damage width
and offset, CDC); there is no 3-D view of it. See also the
[Damage Data dialog](../../11-reports-output/DamageData.md).

## Overview of Section Twelve

This section describes the background and use of DamageStudio.

- [Chapter 32](#contents) provides a description of the DamageStudio user interface and the process of using DamageStudio, with what HVE Studio provides in its place.
- Chapter 33 provides several tutorials showing the user how to accomplish various tasks using DamageStudio. *(Chapter 33 is not included in this edition.)*

## Contents

- [32 (part 1) — The DamageStudio Interface](01-interface.md)
- [32 (part 2) — Using DamageStudio](02-using-damagestudio.md)

## Related Pages

- [Damage Data dialog](../../11-reports-output/DamageData.md) — the Event Editor dialog used to assign a user-measured damage profile (CDC, PDOF, crush depths, stiffness) to a vehicle. The *User-entered* damage view in DamageStudio is closely related to this dialog.
- [DyMESH](../DyMESH/README.md) — the collision model that produces SIMON's crush.

<!-- NAV -->

---

Next: [Chapter 32 — The DamageStudio Interface](01-interface.md) →

<!-- /NAV -->
