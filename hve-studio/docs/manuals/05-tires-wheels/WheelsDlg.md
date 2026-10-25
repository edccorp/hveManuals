# Wheels — Blow-out Page

The event **Wheels** dialog holds the per-wheel options that belong to one event
rather than to the vehicle: tire blow-out, wheel damage, brake condition and the
tire–terrain model.

!!! note "HVE Studio"
    In the Event editor (F5) choose **Event › Wheels...** (Ctrl+W). The item is
    available for the dynamic calculation methods. The window is titled
    **Wheels** and shows the vehicle chosen in the **Vehicle** list at the top
    for the active event. It has four tabs, always shown:

    - **Tire Blowout** — this page
    - **Wheel Damage** — see [Wheels — Damage Page](WheelsDlg1.md)
    - **Brake** — see [Wheels — Brake Page](WheelsDlg2.md)
    - **Terrain Model** — the tire–terrain model (below)

    Instead of HVE's Axle No / Side / Location selectors, every tab is a table
    with **one column per wheel**: **A1-R**, **A1-L**, **A2-R**, … (R = right,
    L = left). When the vehicle has dual tires, the Tire Blowout and Terrain
    Model tabs have one column per tire, suffixed **o** (outer) and **i**
    (inner). The **Wheel Group** row (**– W1 W2 W3**) at the top of each table
    makes columns in the same group change together; **–** edits a wheel on its
    own.

    SIMON and EDSMAC4 read tire blow-out and wheel damage, and EDVSM reads the
    blow-out; a note at the top says when the event's calculation method does
    not read a tab. While a solved
    run is on screen the dialog is read-only.

![Wheels dialog, Tire Blowout tab](images/hvn-wheels.png)

## Tire Blowout

The HVE Tire Blow-out Model varies tire performance while the simulation is
running: the tire's cornering and camber stiffness are ramped to (cornering
stiffness factor) × intact, its radial stiffness to (radial stiffness factor) ×
intact, and its rolling resistance to (rolling factor) × intact, linearly over
the deflation time. A factor of 1.0 leaves the value unchanged.

### Blown

Check box indicating whether the tire blows out during the event. The remaining
rows of the column are enabled only when it is checked. HVE's *Tire is Blown*.

### Start at first contact

The blow-out starts automatically at the vehicle's first contact. When checked,
Blowout time is disabled. HVE's *Auto Start*.

### Blowout time (s)

Simulation time at which the blow-out starts. HVE's *Start Time*.

### Deflation time (s)

Duration over which the air loss occurs. HVE's *Duration*.

### Cornering stiffness factor

Multiplier applied to the tire's cornering and camber stiffness once the tire is
fully deflated. HVE's *Stiffness Factor*.

### Radial stiffness factor

Multiplier applied to the tire's radial (vertical) stiffness once the tire is
fully deflated. Only the inflation part of the stiffness is reduced, up to the
tire's second-stage deflection; past it the sidewall folded onto the rim keeps its
intact stiffness. A factor of 0 is a completely flat tire carried on its folded
sidewall.

!!! tip "New in HVE Studio"
    HVE has one *Stiffness Factor* for the cornering, camber and radial
    stiffness. HVE Studio separates them so that a **flat** (the air is gone: a
    low radial factor) and a **tread delamination** (the tread no longer grips
    the road while the carcass still holds air: a low cornering factor, a radial
    factor near 1) can be modeled apart. A case saved before the split, or
    imported from HVE, uses its one factor for both.

### Rolling resist. factor

Multiplier for the tire rolling resistance of the blown tire.

!!! note "HVE Studio"
    - HVE enables this field only for a calculation method that offers
      pedal-force braking; HVE Studio enables it whenever the tire is blown.
    - EDSMAC4 **divides** by the rolling factor, so a value above 1 reduces
      rolling drag there; SIMON multiplies. HVE feeds both the same number, and
      so does HVE Studio.
    - In SIMON the radial factor reaches every tire-terrain model: point
      contact, the radial spring, and a DyMESH wheel's tread and wheel mesh.
      HVE applied the blow-out to the radial stiffness only under point
      contact, so a blown tire on the radial spring model, or on a DyMESH
      wheel, carried its load fully inflated. HVE also stepped a DyMESH wheel
      mesh to the deflated stiffness at the blow-out time; HVE Studio ramps it
      over the deflation time like the tire.
    - EDVSM applies the radial factor to its tire spring rate, and EDSMAC4 to
      the drop in the tire's rolling radius (the factor's complement of the
      tire's maximum deflection); the cornering factor to their cornering
      stiffness.
    - With **HVE-reference** physics a radial factor different from the
      cornering factor is not applied, as in HVE, and the run status says so.

## Terrain Model

How each tire meets the ground. Only SIMON has a tire–terrain model; with any
other method the tires use point contact.

**Model** — **Point contact** (the default; a single contact patch), **Soft
soil** (adds Bekker sinkage and plow forces, with the soil properties taken
from the surface material — see
[Environment Material Properties](../08-environment/EnvrMatPropDlg.md)) or
**Radial spring** (a fan of springs around the tire, so it can climb a curb or
drop into a pothole).

Radial spring finds the ground by casting rays at real road polygons, so it
needs imported environment geometry marked as terrain; the dialog warns, and the
run is refused, when there is none. Its force–deflection table is derived from
the tire's own ride rates and dimensions. The remaining rows are enabled only
for a radial-spring tire:

- **Start time (s)**, **Deflection step**, **Fan half-span (deg)**, **Angle
  between springs (deg)** — when the model starts and how its fan of springs is
  laid out.
- **Sidewall Impact** — adds springs down the tire's side so the wheel can load
  against the face of a curb, not only ride over it. When checked it enables
  **Sidewall Slide Friction Coefficient**, **Impact Both Sidewalls (2 Sides)**,
  **Use Curb Polygons Only** and **Number Of Sidewall Springs**, and for each
  spring in use (**Sidewall Spring No 1**, **2**, …): **Radial Dist From Wheel
  Ctr**, **Lat Dist From Wheel Ctr**, **Stiffness Ratio (sidewall/radial)** and
  **Saturation Deflection**.

A sidewall with no spring geometry entered gets it derived from the tire (radii
spaced by one fifth of the maximum deflection about the unloaded radius, springs
at half the section width, saturating at the full width, stiffness ratio 1.0);
the dialog notes when that is happening.

!!! warning "Not in HVE Studio"
    HVE's **Apply To All Tires** button: use a wheel group instead.

<!-- NAV -->

---

← Previous: [Tire Save As Dialog](TireSaveAsDlg.md)  |  [Index](README.md)  |  Next: [Wheels — Damage (Displacement) Page](WheelsDlg1.md) →

<!-- /NAV -->
