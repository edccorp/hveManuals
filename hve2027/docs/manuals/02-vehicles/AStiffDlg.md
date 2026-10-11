# A Stiffness Coefficient Dialog

**Per-Zone A Stiffness**

The selected vehicle's stiffness coefficients are normally used for damage-based calculation methods. HVE shows the A-stiffness values for each crush zone in a separate *A Stiffness Coefficients* dialog. These coefficients are initially assigned from the vehicle's own stiffness and may be replaced by user-entered values for each crush zone.

HVE 2027 has no separate A Stiffness dialog. The per-zone A and B coefficients of an EDCRASH reconstruction are edited together, in the **Event Information** panel of the Event Editor (**Event (F5)**):

1. Make an EDCRASH event the active event.
2. In the **Vehicle Impact Setup** section, under the vehicle's name, open **Measured Crush (drives Delta-V)**.
3. Set **# crush depths** to 2 or more and enter the crush depths, damage width and offset.
4. Open **Per-zone A/B (*n* zones)**. There is one zone fewer than the number of crush depths, up to nine zones.

## Zone 1 - 9 A
Enter the A-stiffness coefficient for the zone, in the units set in Preferences. Each row also holds the zone's B coefficient (**Zone *n* B**). Only the zones defined by the entered crush profile are listed.

A zone left at zero uses the single **A Stiffness** / **B Stiffness** entered for the vehicle higher up in the same section, so leaving every zone at zero gives a uniform profile. A case read from an HVE file carries HVE's own per-zone values.

## All same as zone 1
Assigns zone 1's coefficients to all the zones. In HVE 2027 this button copies **both** the A and the B coefficient of zone 1.

!!! note "HVE 2027"
    The A and B coefficients of each zone are edited side by side in the Event Information panel, per event and per vehicle, rather than in two separate dialogs.

<!-- NAV -->

---

← Previous: [Vehicles](README.md)  |  [Index](README.md)  |  Next: [Body Torsion Dialog](BodyTorDlg.md) →

<!-- /NAV -->
