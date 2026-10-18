# Airbag Restraint System Dialog Box

In HVE the Airbag Restraint System dialog places an installed airbag in use for
an occupant in the event, selects the body ellipsoids that may contact it, and
sets when it deploys.

!!! note "HVE 2027"
    HVE 2027 has no separate Airbag Restraint System window. Its fields are
    in the vehicle's **Airbags** window — **Vehicle › Editors › Airbags...** in the
    Vehicle editor (F3), or **Event › Restraints... › Airbags...** in the
    Event editor (F5; EDHIS and GATB events) — beside the bag's own
    properties (see [Air Bag Restraints](AirBagDlg.md)). They are stored with
    the vehicle, one set per seat, so they apply to every event the vehicle
    appears in. While a solved run is on screen the window is read-only.

!!! warning "When the bag is used"
    A bag is deployed in a run only for an occupant whose restraint in that
    event is **Airbag + Belt** — set with **Restraint In Use** in the
    [Belt Restraint System](BeltResSysDlg.md) window or in Event Information.
    The seat must have a bag installed (**Device Installed** in the Airbags
    window), or the run is refused.

## Begin Fill Time (s)

The simulation time at which the airbag begins to fill. Default 0.001 s. Read
by EDHIS and GATB.

## Fill Duration (s)

The length of time over which the airbag fills, limited to HVE's own range of
0.0001–0.20 s. Default 0.05 s. Read by EDHIS.

## Contact Segments

**Head**, **Chest**, **Arm** — the body segments that may contact the bag (Arm
covers both upper and lower arms on both sides). Only the selected segments
develop contact forces with the bag. Read by GATB. With none selected, the run
status notes it.

!!! note "HVE 2027"
    HVE lists every contact ellipsoid of the occupant for individual selection;
    HVE 2027 offers these three groups, each using the segment's first
    ellipsoid.

!!! warning "Not in HVE 2027"
    - **Airbag Restraints For**: the bag is chosen by seat in the Airbags
      window, and an occupant uses the bag at their seat.
    - **Device In Use**: the bag is in use for an occupant whose restraint in
      the event is Airbag + Belt (see above).
    - **AutoStart**: no physics program reads it. The fill times are always
      used as entered.

<!-- NAV -->

---

← Previous: [Air Bag Restraints Dialog Box](AirBagDlg.md)  |  [Index](README.md)  |  Next: [Belt Restraint System Dialog Box](BeltResSysDlg.md) →

<!-- /NAV -->
