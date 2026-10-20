# Contacts Dialog Box

HVE's Contacts dialog selected which human ellipsoids may interact with which
vehicle contact surfaces, so that force calculations are performed only for
pairs that have a chance of interacting, and assigned combined material
properties to each pair.

!!! note "HVE Studio"
    **Event › Contacts...** (Ctrl+T) for an **EDHIS or GATB** event opens the
    **Occupant Contacts** dialog. In place of HVE's Object / Source(s) /
    Target(s) lists it shows a grid: one row per human segment (per ellipsoid
    where a segment has more than one), one column per vehicle contact surface,
    a ticked box for each armed pair. Edits apply at once and go into the undo
    history (there is no OK or Cancel).

    - An imported HVE case shows the pairs it states. An event with **no stored
      list** shows the default the run generates — every ellipsoid of the
      pelvis, abdomen, chest, neck, head and upper legs against every surface —
      and says so; the first click stores that default with the click applied.
    - **Arm All** (every ellipsoid of every segment against every surface, HVE's
      own starting selection), **Pelvis Only** and **Use Run-Time Default** set
      the whole list. The last armed pair cannot be removed.
    - EDHIS: dimmed rows are segments EDHIS does not test against the vehicle;
      an un-ticked pair is handed to EDHIS as explicitly un-armed, and the
      dialog warns when a surface has no pelvis pair (EDHIS stops, -5436).
    - GATB: **each occupant has its own list**, as in HVE. With more than one
      occupant an **Occupant** selector chooses whose list the grid edits, and
      each is armed for its own occupant only; an occupant with none is said to
      have nothing to strike, and **Create This Occupant's List** arms every
      ellipsoid against every surface of the vehicle it rides.
    - GATB: a second grid arms body **segment against segment** (self contact),
      row = base, column = target. A newly ticked pair copies the first stored
      pair's combined material; a human with none stored cannot have one added.
    - Contact blocks an imported case states against a vehicle the event does
      not select are listed read-only, each with its occupant.

What else HVE Studio offers:

- For an **EDSMAC4** event, **Event › Contacts...** opens a small
  **Contacts** window that lists the selected vehicle's contact surface names.
  It is read-only.
- **Combined material properties** for occupant events are edited in the
  [Event Information](EventInfo.md#humans-in-event) panel: under *Humans in
  Event*, an EDHIS or GATB event shows a **Combined Contact Materials** header
  with one entry per interior surface of vehicle slot 1 — force constant,
  linear, quadratic and cubic stiffness, damping rate, friction, maximum force
  (0 = infinite), maximum deflection, unloading stiffness, maximum penetration
  and edge constant (0–1, HVE default 0.5). A surface with no combined material
  stated uses that surface's own material with an edge constant of 0.5.
- The vehicle contact surfaces themselves are defined in **Vehicle › Editors › Contact
  Surfaces**.
- Imported **self-contact** pairs (one body segment against another, used by
  GATB) are also counted under the human in *Humans in Event*.

!!! note "HVE Studio"
    Only the first ellipsoid of a body segment takes part in contact, as in
    HVE's own GATB. A self-contact pair that names another ellipsoid is armed but
    not tested; the run status and Event Information say how many such pairs a
    case contains.

<!-- NAV -->

---

← Previous: [Events & Driver Controls](README.md)  |  [Index](README.md)  |  Next: [Driver Controls](DriverControls.md) →

<!-- /NAV -->
