# Human Material Properties Dialog Box

In HVE this dialog edits the material assigned to one contact ellipsoid of a
human: a force–deflection law (constant, linear, quadratic and cubic stiffness,
damping, friction, maximum force and deflection, unloading slope and maximum
deflection per time step) with a graph, and New / Open / Save As for HVE
material files (`*.matl`).

!!! warning "Not in HVE 2027"
    HVE 2027 has no Human Material Properties dialog, and a contact ellipsoid
    has no material of its own (see [Contact Ellipsoids](Human1.md)).

    What the occupant programs use is the **combined** occupant–surface
    material carried with each occupant contact pair. When an HVE case
    (`.hve`) is opened, those pairs and their combined materials are imported
    and passed to EDHIS and GATB. The stated materials are edited under
    **Combined Contact Materials** in the
    [Event Information](../09-events-driver-controls/EventInfo.md#humans-in-event)
    panel of an EDHIS or GATB event; a surface with none stated uses that
    surface's own material with an edge constant of 0.5.

    The vehicle side of a contact — each interior or exterior contact surface's
    own force–deflection law — is edited in the vehicle's
    [Contact Surfaces](../08-environment/ContSurfDlg.md) window under
    **Material Properties**.

<!-- NAV -->

---

← Previous: [Human Joint Properties Dialog Box](HumJntPropDlg.md)  |  [Index](README.md)  |  Next: [Selected Humans & Vehicles Dialog Box](SelHumVehDlg.md) →

<!-- /NAV -->
