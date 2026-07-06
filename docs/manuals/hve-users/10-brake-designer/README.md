# Section Eleven: HVE Brake Designer

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Section Eleven "HVE Brake Designer" (Section Ten / Chapter 28 of the original manual is reserved for future use). Verified against the current HVE application source (`HVEINV-64/HveBrakes.cpp`, `BrakeDesign*.cpp`, `BrakeAssemblyDlg.cpp`, `ABSDesignerDlg.cpp`, `ABSSystemDlg.cpp`).*

The HVE Brake Designer is a time-domain simulation model of user-defined
brake system components. The purpose of the HVE Brake Designer is to provide
a detailed brake design capability integrated directly within the HVE
simulation environment. The capability includes the design and evaluation of
wheel brake assemblies and ABS systems by engineers charged with fitting new
vehicles with properly designed brake system components, as well as the
evaluation of in-use service conditions. This section of the HVE User's
Manual describes how to create and edit various brake system designs. It also
provides an overview of the brake and ABS model parameters.

The HVE Brake Designer was developed by Engineering Dynamics Corporation, and
was based, in part, on previous work by Limpert [4.31], MacAdam [4.2], Flick
[4.32] and Robert Bosch [4.42].

Although the HVE Brake Designer is a very powerful tool based on widely
accepted scientific principles, brake design engineers know that brake torque
calculations are not exact, mainly because the precise friction value is
never known; it is always estimated. Therefore, brake design engineers and
safety researchers should use the HVE Brake Designer as they use other
modeling tools. The results are useful for matching measured dynamometer
data, extending existing designs, providing parametric comparisons and
estimating the behavior of a proposed design.

## General Procedure

To use the HVE Brake Designer, perform the following steps:

1. Select Vehicle Mode.
2. Select one or more vehicles from the Vehicle Database or from a previous
   HVE case.
3. Click on the Brake System icon and confirm or edit the Brake Pedal Ratio.
4. If the vehicle is fitted with ABS, click on the ABS Installed checkbox.
   Press Edit to view and edit the desired ABS system properties.
5. Click on a wheel and choose Brakes from the pop-up menu.
6. Click on the Brake Assembly Type option list and choose the desired brake
   design (e.g., Disc Brake, Duo-servo Drum Brake). The HVE Brake Designer
   dialog for the selected brake type is displayed.
7. Edit the desired properties.
8. Press OK to accept the current design.
9. Edit the remaining wheels as desired.
10. Execute the desired suite of simulations to test the effectiveness of the
    design.
11. Edit the design as required to obtain optimum braking performance.

## Overview of Section Eleven

This section provides a detailed explanation of the modeling techniques used
by the HVE Brake Designer, and also presents an overview of the Brake
Designer's interface.

- [Chapter 29 — HVE Brake Designer](29-brake-designer.md) describes in
  detail the process of using the HVE Brake Designer.
- [Chapter 30 — Brake Temperature Model](30-brake-temperature.md) provides a
  detailed overview of the Brake Temperature Model.
- [Chapter 31 — Antilock Braking Systems](31-abs.md) provides a detailed
  overview of the HVE Antilock Brake System Model.

## Related Dialog Reference Pages

The individual brake dialogs are documented in detail (verified against
current source code) in
[`docs/manuals/04-brakes-powertrain/`](../../04-brakes-powertrain/README.md):

- [Brake Assembly dialog](../../04-brakes-powertrain/BrkAsmblyDlg.md)
- [Disc Brake designer dialog](../../04-brakes-powertrain/DiskBreakDlg.md)
- [Duo-Servo Drum Brake designer dialog](../../04-brakes-powertrain/DueServoBrkDlg.md)
- [Duplex Drum Brake designer dialog](../../04-brakes-powertrain/DuplexBrkDlg.md)
- [Single Piston Drum Brake designer dialog](../../04-brakes-powertrain/BrkSingPistDlg.md)
- [Dual Piston Drum Brake designer dialog](../../04-brakes-powertrain/DualPistBrkDlg.md)
- [Dual Wedge Drum Brake designer dialog](../../04-brakes-powertrain/DualWedgeBrkDlg.md)
- [Brake Designer Material Properties dialog](../../04-brakes-powertrain/BrkMatPropDlg.md)
- [Brake System Pressure vs Pedal Force dialog](../../04-brakes-powertrain/BrkSysVsPedFrcDlg.md)

<!-- NAV -->

---

Next: [Chapter 29 — HVE Brake Designer](29-brake-designer.md) →

<!-- /NAV -->
