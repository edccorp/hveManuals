# Air Bag Restraints Dialog Box

In HVE the vehicle editor's Air Bag dialog installs an airbag at a seat position
and holds the bag's properties: deploy location, bag geometry, gas and vent
properties, membrane moduli, steering-column collapse and the backside contact
surface.

!!! note "HVE 2027"
    In HVE 2027 the bag's properties belong to the **occupant** sitting in the
    seat, not to the vehicle. Open them in the Human editor (F2): **Occupant ›
    Human Information...** opens the **Occupants** panel; select the occupant and
    press **Airbag Properties...**. The window is titled **Airbag Restraints**
    and edits the bag at that occupant's seat (shown beside the name). A
    pedestrian has no seat and no airbag.

    When and where the bag deploys in an event, and which body segments it can
    strike, are set in the [Airbag Restraint System](AirBagSysDlg.md) window.
    Lengths, areas, volumes, pressures, density and force follow the units set
    in Tools › Preferences; the unit is shown in each label.

!!! warning "When the bag is used"
    An airbag reaches EDHIS or GATB only when the occupant's restraint in the
    event is **Airbag + Belt** (the **Restraint In Use** list of the
    [Belt Restraint System](BeltResSysDlg.md) window, or Event Information).
    The window says so in orange when the occupant is not in the active event or
    the restraint is something else.

## Device Installed

Check box enabling the fields below. It does not by itself put a bag into a run —
the occupant's restraint type does (see above).

## Reaction Panel

The vehicle contact surface the bag reacts against. **Primary (deploys from)**
is HVE's *Backside Contact Surface*. Up to three **Confining panel** 2–4 entries
name further surfaces that confine the bag (GATB); a confining panel equal to
the primary is ignored. The lists hold the contact surfaces of the occupant's
vehicle; with none, the section warns that GATB will refuse the run.

## Deploy Point

X, Y, Z of the deploy point **in the reaction panel's frame** (0 = the panel's
centre). Used by GATB.

!!! note "HVE 2027"
    HVE's vehicle-fixed *Deploy Coords* — the point EDHIS deploys the bag from —
    are the **Deploy Position** fields of the
    [Airbag Restraint System](AirBagSysDlg.md) window.

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

!!! tip "New in HVE 2027"
    A collapsed section of inputs GATB's airbag model needs and HVE's dialog
    does not offer: **Supply Gas Temperature (K)**, **Supply Volume**, **Sonic
    Discharge Coef**, **Specific Gas Const (J/kg·K)**, **Sonic Throat Area**,
    **Bag Mass (kg)**, **Panel Spring Rate (N/m)**, **Panel Friction Coef**,
    **Mass Multiplier**, **Bag Yaw (deg)** and **Bag Roll (deg)**. The defaults
    reproduce the values GATB used to have built in.

!!! warning "Not in HVE 2027"
    - **Seat Position** list: the window edits the bag at the selected
      occupant's seat. Choose another occupant in the Occupants panel to edit
      another seat.
    - **OK / Cancel**, and range warnings when a field is left: edits apply
      immediately; **Edit › Undo** (Ctrl+Z) takes one back.

<!-- NAV -->

---

← Previous: [Accelerometers Dialog](AcclMtrsDlg.md)  |  [Index](README.md)  |  Next: [Airbag Restraint System Dialog Box](AirBagSysDlg.md) →

<!-- /NAV -->
