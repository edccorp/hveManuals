# Air Bag Restraints Dialog Box

In HVE the vehicle editor's Air Bag dialog installs an airbag at a seat position
and holds the bag's properties: deploy location, bag geometry, gas and vent
properties, membrane moduli, steering-column collapse and the backside contact
surface.

!!! note "HVE Studio"
    Open the **Airbags** window from **Vehicle › Editors › Airbags...** in the Vehicle
    editor (F3), or **Event › Restraints... › Airbags...** in the Event editor
    (F5; EDHIS and GATB events). As in HVE, a bag belongs to the vehicle, one
    per seat location. The same window also holds the deploy timing and
    contact segments of HVE's event
    [Airbag Restraint System](AirBagSysDlg.md) dialog. Lengths, areas,
    volumes, pressures, density and force follow the units set in Tools ›
    Preferences; the unit is shown in each label. While a solved run is on
    screen the window is read-only.

!!! warning "When the bag is used"
    An airbag reaches EDHIS or GATB only for an occupant whose restraint in the
    event is **Airbag + Belt** (the **Restraint In Use** list of the
    [Belt Restraint System](BeltResSysDlg.md) window, or Event Information).
    Such an occupant at a seat with no bag installed is refused at run time.
    For the active event the window says when nobody sits at the seat, when
    the occupant there is not Airbag + Belt, and when the run will be refused.

## Seat

HVE's *Seat Position*: the seat whose bag is edited, labelled with who sits
there in the active event and whether a bag is installed. The window opens on
the seat of the occupant selected in the Occupants panel, or of the vehicle's
first occupant.

## Device Installed

Check box saying the vehicle has a bag at this seat; it enables the fields
below. It does not by itself put a bag into a run — the occupant's restraint
type does (see above).

## Position (vehicle, from the CG)

**X**, **Y**, **Z** — HVE's *Deploy Coords*: the vehicle-fixed point, relative
to the CG, from which the bag deploys. Read by EDHIS.

The **Timing** and **Contact Segments** fields are described on the
[Airbag Restraint System](AirBagSysDlg.md) page.

## Reaction Panel

The vehicle contact surface the bag reacts against. **Primary (deploys from)**
is HVE's *Backside Contact Surface*. Up to three **Confining panel** 2–4 entries
name further surfaces that confine the bag (GATB); a confining panel equal to
the primary is ignored. The lists hold the vehicle's contact surfaces; with
none, the section warns that GATB will refuse the run.

## Offset on the Reaction Panel

X, Y, Z of the deploy point **in the reaction panel's frame** (0 = the panel's
centre). Used by GATB.

!!! note "HVE Studio"
    HVE's vehicle-fixed *Deploy Coords* — the point EDHIS deploys the bag from —
    are the **Position (vehicle, from the CG)** fields above.

## Bag Geometry

- **Full Inflated Volume** — volume inside the airbag when fully inflated.
- **Initial Radius** — initial (undeployed) radius of the airbag.
- **Passenger Bag Length** — length for non-driver-side (passenger) airbags.

## Gas Properties

- **Initial Pressure** — initial pressure inside the airbag.
- **Gas Density** — gas density of the filling agent.
- **Mass Flow Rate** — mass flow rate of the filling gas (kg/s or lb/s).
- **Specific Heat Ratio** — specific heat ratio of the filling agent
  (dimensionless). A value outside HVE's allowed 0.05–20 is replaced with
  HVE's 1.05 at run time, and the run status says so.

## Vent

- **Discharge Coef** — thermodynamic discharge coefficient for the vent hole.
- **Vent Area** — area of the vent hole.
- **Pressure Open Vent** — airbag pressure required to open the vent hole.

## Contact

- **Column Angle (deg)** — steering column angle about the vehicle's pitch axis
  (normally negative).
- **Col. Load** — axial load on the steering column required to begin
  collapsing it (driver-side bags).
- **Max Col. Disp** — maximum distance the steering column may collapse
  (driver-side bags).
- **Max Penetration** — penetration required before any force is computed.
- **Force Conv. Criterion** — permissible force imbalance between the airbag and
  the contact surfaces.

## Membrane (force-deflection law)

- **Bag Membrane Thickness** — thickness of the airbag fabric.
- **Bag Elastic Modulus** — modulus of the bag material while filling.
- **Bag Rebound Modulus** — modulus during rebound.
- **Bag Bottom-out Modulus** — modulus after the bag has bottomed out.

HVE's typical ranges and defaults are listed under the fields.

## ATB Gas Dynamics (GATB)

!!! tip "New in HVE Studio"
    A collapsed section of inputs GATB's airbag model needs and HVE's dialog
    does not offer: **Supply Gas Temperature (K)**, **Supply Volume**, **Sonic
    Discharge Coef**, **Specific Gas Const (J/kg·K)**, **Sonic Throat Area**,
    **Bag Mass (kg)**, **Panel Spring Rate (N/m)**, **Panel Friction Coef**,
    **Mass Multiplier**, **Bag Yaw (deg)** and **Bag Roll (deg)**. The defaults
    reproduce the values GATB used to have built in.

!!! warning "Not in HVE Studio"
    - **OK / Cancel**, and range warnings when a field is left: edits apply
      immediately; **Edit › Undo** (Ctrl+Z) takes one back.

<!-- NAV -->

---

← Previous: [Accelerometers Dialog](AcclMtrsDlg.md)  |  [Index](README.md)  |  Next: [Airbag Restraint System Dialog Box](AirBagSysDlg.md) →

<!-- /NAV -->
