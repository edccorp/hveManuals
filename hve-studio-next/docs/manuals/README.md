<img src="assets/edc-logo.png" alt="Engineering Dynamics Company, LLC" class="edc-hero">

# HVE Studio Manual

This is the manual for **HVE Studio**, the preview edition of the next
version of HVE (Human Vehicle Environment): HVE's own physics programs in a new
interface. It describes a preview release, which does not yet do everything
the current release of HVE does. For the current release of HVE, see the
[HVE manuals](https://manuals.edccorp.com/).

This manual set is built on HVE's own — the HVE on-line help, the HVE User's
Manual and the physics program manuals — adapted page by page to describe
HVE Studio. HVE Studio runs HVE's own physics programs, compiled from HVE's own
source code, so the program manuals' descriptions of the models, their
equations and their references still apply; where HVE Studio differs, the page
says so. The interface, the case files and the rendering are new, so every page
that tells you *how to do something* has been rewritten for HVE Studio and
illustrated with HVE Studio's own screens.

Differences are marked throughout:

!!! note "HVE Studio"
    Something that works differently in HVE Studio, and where to find it.

!!! warning "Not in HVE Studio"
    An HVE feature HVE Studio does not have, and why.

!!! tip "New in HVE Studio"
    A capability HVE does not have.

## Start here

New to HVE Studio? Read [HVE Studio](getting-started/README.md) first: what it is
and what "Preview" means, installing and running it, a tour of the interface,
case files (including opening HVE `.hve` cases directly) and a one-page list of
the differences from HVE, including what HVE Studio does not do yet.

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

HVE's program manuals, each reviewed against HVE Studio and marked where
HVE Studio differs:

- [EDCRASH](programs/EDCRASH/README.md)
- [EDGEN](programs/EDGEN/README.md)
- [EDHIS](programs/EDHIS/README.md)
- [EDSMAC](programs/EDSMAC/README.md)
- [EDSMAC4](programs/EDSMAC4/README.md)
- [EDSVS](programs/EDSVS/README.md)
- [EDVDS](programs/EDVDS/README.md)
- [EDVSM](programs/EDVSM/README.md)
- [EDVTS](programs/EDVTS/README.md)
- [SIMON](programs/SIMON/README.md)
- [DyMESH](programs/DyMESH/README.md)
- [GATB](programs/GATB/README.md)
- [RDF](programs/RDF/README.md)
- [GBF](programs/GBF/README.md)
- [Damage Studio](programs/DamageStudio/README.md)

## HVE User's Manual

The [HVE User's Manual](hve-users/README.md) (Version 5, Seventh Edition),
adapted for HVE Studio:

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

