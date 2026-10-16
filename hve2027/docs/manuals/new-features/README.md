# HVE 2027 Features

!!! tip "New in HVE 2027"
    This section describes capabilities HVE does not have, and three that go
    beyond what HVE does: the sun (chapter 2), cameras (chapter 5) and the
    Video Creator (chapter 7), which HVE has in simpler forms. Each chapter's
    box says what is new. These chapters are written from scratch for
    HVE 2027.

HVE 2027 runs HVE's own physics programs. What it adds sits *around* the
physics: how the scene looks, how it is filmed, how it leaves the program,
and a handful of analysis tools. None of the presentation features in this
section changes a result. A material, a sun position, a camera or a keyframe
changes what the viewport **shows**, never what an engine **solves**, and the
windows that edit them say so at the top.

The exceptions are stated where they occur: the HVE Surface node on a road
surface's material edits that surface's physics (its type and friction), the
analysis tools in chapter 8 run the engines, and the case-intake tools in
chapter 12 set vehicle, event and driver-control inputs.

## Contents

| Chapter | Covers |
| --- | --- |
| [1 — Materials and the Shader Editor](01-materials-and-shader-editor.md) | Node materials for vehicles, vehicle parts, road surfaces, humans, the ground plane and the world; Edit Mode; the crush heat map |
| [2 — Sun, Sky and World](02-sun-sky-and-world.md) | Placing the sun by hand or from the location, date and time; address search; the Sky Texture; shadows |
| [3 — Shading Vehicles and Sites](03-shading-vehicles-and-sites.md) | Shade As Loaded / Flat / Smooth / Auto Smooth for a vehicle body and for the site |
| [4 — Keyframes and the Dope Sheet](04-keyframes-and-dope-sheet.md) | Animating material values over playback time; interpolation, easing, extrapolation and cycles; the Dope Sheet and Curves view |
| [5 — Cameras](05-cameras.md) | Saved cameras, attaching a camera to a vehicle, lens settings, keyframed cameras |
| [6 — Exporting to Blender and glTF](06-exporting-to-blender-and-gltf.md) | The glTF export and the Blender Live Link, and what each carries |
| [7 — Video and Playback Sequences](07-video-and-playback-sequences.md) | Combining several solved events on one timeline; recording the playback to a video (camera, start and end times, slow motion, ray tracing, motion blur); playing a video; a ray-traced picture |
| [8 — Analysis Tools](08-analysis-tools.md) | Quick Case, Monte Carlo Analysis, Motorcycle Analysis, Audit Log, Limits Editor |
| [9 — Motorcycles](09-motorcycles.md) | The Motorcycle vehicle type and the SINGLETRACK method |
| [10 — Survey Point Clouds](10-point-clouds.md) | Showing a laser scan or photogrammetry cloud behind the simulation |
| [11 — Results HUD](11-results-hud.md) | Boxes of solved numbers (time, speed, heading, Delta-V, any output channel) over the viewport and burned into recorded videos, saved with the case |
| [12 — Case Intake and Vehicle Data](12-case-intake-and-vehicle-data.md) | Vehicle Package (VIN, database match, stated specifications, occupants and cargo), Case Intake, Provenance, the Aboard list, crush stiffness from crash tests and NHTSA test files, EDR Import |

## Where these features live

| Feature | Where |
| --- | --- |
| Shader Editor | **View › Shader Editor** (every editor mode) |
| Dope Sheet | **View › Dope Sheet** |
| Sun and sky | Shader Editor, **World**; or **Edit the sun and sky...** in Environment › Sky and in the Event editor's Lighting section |
| Edit Mode (materials per part) | **Vehicle › Edit Mode (materials per part)**, or **Tab** over the viewport in the Vehicle editor |
| Cameras | **Tools › Cameras...** |
| glTF export | **File › Export Scene for Blender** (after a run) |
| Blender Live Link | **File › Blender Live Link...** |
| Playback sequences | the **Playback (F6)** editor |
| Recording a video | **File › Record Animation...** (after a run) |
| Results HUD | **View › Results HUD** (every editor) |
| Quick Case, Monte Carlo, Motorcycle Analysis | **Tools** menu |
| Vehicle Package, Case Intake, Provenance, EDR Import | **Tools** menu |
| Aboard (occupants and cargo on a vehicle) | **Inertia / Mass** dialog (Vehicles panel › Vehicle Properties) |
| Crush stiffness from crash tests | **Vehicle › Crush Stiffness...**, **From crash tests...** |
| Point clouds | **Environment › Environment...**, *Terrain* section, *Survey Point Cloud (scan)* |

## What "display only" means here

A case stores its materials, sun, cameras, keyframes and Results HUD boxes alongside its physics
inputs, and saves them in both the `.hvex` and the `.json` format. They are
deliberately left out of the fingerprint HVE 2027 uses to decide whether a
solved result still matches its inputs, so editing a material, moving the sun,
keying a camera or editing a HUD box never discards a run, and none of them is
locked while results are on screen. A road surface's type and friction are physics inputs,
wherever you edit them: they are locked while results are on screen (reset the
run to edit them), and changing them means solving again.
