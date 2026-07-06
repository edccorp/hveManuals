<img src="assets/edc-logo.png" alt="Engineering Dynamics Company, LLC" class="edc-hero">

# HVE Software Manual (Markdown Edition)

This directory contains the HVE (Human Vehicle Environment) user manual in
Markdown form. It was produced by reviewing the legacy on-line help topics in
`HTMLHelp/HTMLFiles/` (the source of the compiled
`HVE.chm` manual) and updating each topic against the current source code:

- **`HVEINV-64/`** — the HVE application (dialogs, editors, reports)
- **`Physics/`** — the simulation engines (EDCRASH, EDGEN, EDHIS, EDSMAC,
  EDSMAC4, EDSVS, EDVDS, EDVSM, EDVTS, SIMON, DyMesh)

Each page notes the legacy help topic it was derived from. Options that were
missing or undocumented in the old help have been documented from the current
code; options that no longer exist in the code have been removed or flagged.

## Contents

| Section | Covers |
| --- | --- |
| [01 — User Interface](01-user-interface/README.md) | 3-D editor, preferences, units, playback, cameras, rendering, grids, lights, overlays, text |
| [02 — Vehicles](02-vehicles/README.md) | Vehicle information, inertias, sprung mass, payload, CG, stiffness coefficients (A/B), body torsion, aerodynamic drag |
| [03 — Suspension & Steering](03-suspension-steering/README.md) | Suspension data, springs/shocks, jounce/rebound, roll steer, camber, anti-pitch, spindle axis, steering system, wheel locations |
| [04 — Brakes & Powertrain](04-brakes-powertrain/README.md) | Brake assemblies and designer (disc, dual-piston, wedge, duo-servo, duplex), brake tables, drivetrain, transmission, differential |
| [05 — Tires & Wheels](05-tires-wheels/README.md) | Tire data, friction, physical data, Fy vs. inclination, slip vs. rolloff, wheels |
| [06 — Safety Systems](06-safety-systems/README.md) | Air bags, belt restraint systems, accelerometers |
| [07 — Humans](07-humans/README.md) | Human models, human information, CG, joint properties, material properties |
| [08 — Environment](08-environment/README.md) | Environment information, surfaces, contact surfaces, materials, friction, geometry primitives (box, cone, cylinder, sphere, ellipsoid) |
| [09 — Events & Driver Controls](09-events-driver-controls/README.md) | Event setup, position/velocity, driver controls (steering, braking, throttle), contacts, inter-vehicle connections, simulation controls |
| [10 — Calculation Options](10-calculation-options/README.md) | Per-model calculation options: EDCRASH, EDGEN, EDHIS, EDSMAC, EDSMAC4, EDSVS, EDVDS, EDVSM, EDVTS |
| [11 — Reports & Output](11-reports-output/README.md) | Accident history, damage data, collision pulse, trajectory and variable-output reports/graphs |

## Program Manuals

Updated Markdown editions of the HVE program manuals, each reviewed against the
current physics engine and application code:

| Manual |
| --- |
| [EDCRASH](programs/EDCRASH/README.md) |
| [EDGEN](programs/EDGEN/README.md) |
| [EDHIS](programs/EDHIS/README.md) |
| [EDSMAC](programs/EDSMAC/README.md) |
| [EDSMAC4](programs/EDSMAC4/README.md) |
| [EDSVS](programs/EDSVS/README.md) |
| [EDVDS](programs/EDVDS/README.md) |
| [EDVSM](programs/EDVSM/README.md) |
| [EDVTS](programs/EDVTS/README.md) |
| [SIMON](programs/SIMON/README.md) |
| [DyMESH](programs/DyMESH/README.md) |
| [GATB](programs/GATB/README.md) |
| [RDF](programs/RDF/README.md) |
| [Damage Studio](programs/DamageStudio/README.md) |

## HVE User's Manual

Updated Markdown edition of the HVE User's Manual (Version 5, Seventh
Edition), in [`hve-users/`](hve-users/README.md):

| Section | Covers |
| --- | --- |
| [01 — Overview](hve-users/01-overview/README.md) | Using HVE, What is HVE?, How to use HVE |
| [02 — Menu Reference](hve-users/02-menu-reference/README.md) | Files, Set-up, View, Options, Help menus |
| [03 — Human Editor](hve-users/03-human-editor/README.md) | Creating/editing humans, human model definition |
| [04 — Vehicle Editor](hve-users/04-vehicle-editor/README.md) | Creating/editing vehicles, vehicle model definition |
| [05 — Environment Editor](hve-users/05-environment-editor/README.md) | Creating/editing environments, environment model definition |
| [06 — Event Editor](hve-users/06-event-editor/README.md) | Creating/editing events, event model definition |
| [07 — Playback Editor](hve-users/07-playback-editor/README.md) | Report/playback windows, editing the event sequence |
| [08 — 3-D Editor](hve-users/08-3d-editor/README.md) | 3-D editor, object tools, manipulators, tutorial |
| [09 — Video Output](hve-users/09-video-output/README.md) | Video basics, HVE video interface |
| [10 — Brake Designer](hve-users/10-brake-designer/README.md) | HVE Brake Designer |
| [11 — Appendices](hve-users/11-appendices/README.md) | Back matter |

