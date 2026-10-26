# Airbag Restraint System Dialog Box

In HVE the Airbag Restraint System dialog places an installed airbag in use for
an occupant in the event, selects the body ellipsoids that may contact it, and
sets when it deploys.

!!! note "HVE Studio"
    HVE Studio has no separate Airbag Restraint System window. Its fields are
    in the vehicle's **Airbags** window — **Vehicle › Editors › Airbags...** in the
    Vehicle editor (F3), or **Event › Restraints... › Airbags...** in the
    Event editor (F5; EDHIS and GATB events) — beside the bag's own
    properties (see [Air Bag Restraints](AirBagDlg.md)). They are stored with
    the vehicle, one set per seat, so they apply to every event the vehicle
    appears in. While a solved run is on screen the window is read-only.

!!! warning "When the bag is used"
    A bag is deployed in a run only for an occupant who wears the **Airbag**
    in that event — its own switch, with or without belts, set under **Worn in
    the Active Event** in the [Belt Restraint System](BeltResSysDlg.md) window
    or beside the human in Event Information. The seat must have a bag
    installed (**Device Installed** in the Airbags window), or the run is
    refused.

## Begin Fill Time (s)

The simulation time at which the airbag begins to fill. Default 0.001 s. Read
by EDHIS and GATB.

## Fill Duration (s)

The length of time over which the airbag fills, limited to HVE's own range of
0.0001–0.20 s. Default 0.05 s. Read by EDHIS.

## Contact Segments (GATB)

A check box for each of the occupant's fifteen body segments — **Pelvis**,
**Abdomen**, **Chest**, **Neck**, **Head**, the right and left **Upper Leg**,
**Lower Leg** and **Foot**, and the right and left **Upper Arm** and **Lower
Arm** — the segments that may contact the bag. Only the selected segments
develop contact forces with the bag. Read by GATB, which takes at most ten per
bag: once ten are ticked the others grey, and a case that states more (an
imported one can) is refused for GATB, in words. With none selected, the run
status notes it. EDHIS reads none of them: its bag acts on its own torso.

!!! note "HVE Studio"
    HVE lists every contact ellipsoid of the occupant for individual selection;
    GATB reads the first ellipsoid of each segment, so HVE Studio offers the
    fifteen segments. An imported case keeps the file's own selection. Before
    v3.0.211 there were three groups (Head, Chest, Arm).

!!! warning "Not in HVE Studio"
    - **Airbag Restraints For**: the bag is chosen by seat in the Airbags
      window, and an occupant uses the bag at their seat.
    - **Device In Use**: the bag is in use for an occupant who wears the
      Airbag in the event (see above).
    - **AutoStart**: no physics program reads it. The fill times are always
      used as entered.

<!-- NAV -->

---

← Previous: [Air Bag Restraints Dialog Box](AirBagDlg.md)  |  [Index](README.md)  |  Next: [Belt Restraint System Dialog Box](BeltResSysDlg.md) →

<!-- /NAV -->
