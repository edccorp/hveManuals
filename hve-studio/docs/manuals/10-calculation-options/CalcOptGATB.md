# GATB Calculation Options

!!! note "HVE Studio"
    HVE's dialog reference has no page for GATB's calculation options; this
    page documents HVE Studio's **GATB Options** window. GATB is HVE's
    15-segment ATB occupant and pedestrian model.

In Event Information, with a GATB event active, press **Method Options...**
under Calculation Method. The **GATB Options** window opens. Changes take
effect immediately and are locked while the event's results are on screen.

## Input Source

**Use external ATB input file** — shown grayed, with the reason.

!!! warning "Not in HVE Studio"
    In HVE this option makes GATB skip assembling its input deck and read an
    existing `GATB.ain` file instead. HVE Studio feeds ATB from the deck it
    assembles in memory, so an external deck cannot reach the solver. An
    imported case that has the option set runs exactly as if it were off.

**Use pulse file** — when checked, the collision pulse is read from the file
named in **Pulse File**, and **Type of Pulse** applies to it.

## Type of Pulse

**Position**, **Velocity** or **Acceleration** (default) — the kind of data in the
pulse file. Enabled only when *Use pulse file* is checked. (A pulse entered in
the [Collision Pulse](../11-reports-output/ColPulse.md) dialog carries its own
type; GATB accepts all three.)

## Belt Contacts

**All belts slide on segments**, **Some belts slide on segments** or **No belts
slide on segments** (default).

## Other settings GATB reads, and does not

- GATB's integration step is fixed (0.002 s) in HVE and in HVE Studio; there is
  no human-collision timestep for it to read.
- The belt webbing force law (stiffness, damping, unloading, break strength)
  entered in the Belt Restraint dialog is **not** used by GATB, which writes its
  own fixed belt table — as HVE's GATB does. EDHIS does use it.
- Contact pairs, self-contact pairs and combined materials come from the event
  — see [Contacts](../09-events-driver-controls/ContactsDlg.md).
