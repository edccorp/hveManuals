# Section Eleven: HVE Brake Designer

*Updated Markdown edition of the HVE User's Manual (HVE Version 5, Seventh Edition, January 2006), Section Eleven "HVE Brake Designer" (Section Ten / Chapter 28 of the original manual is reserved for future use), adapted for HVE 2027.*

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

!!! warning "Not in HVE 2027"
    In HVE 2027 the Brake Designer works as in HVE: it computes a wheel's brake torque ratio and pushout pressure from the brake's geometry and lining friction and writes the design to the wheel, and during a simulation a designed brake recomputes its torque from that design at every step, with the lining friction at the simulated temperature and sliding speed and, for air brakes, the stroke factor; the brake temperature model runs on every pedal-braked wheel, so **brake fade is simulated** for a designed brake. A Generic wheel keeps a constant torque ratio. The ABS model runs as in HVE. See [Chapter 29](29-brake-designer.md) and [Chapter 30](30-brake-temperature.md).

## General Procedure

To use the Brake Designer in HVE 2027, perform the following steps:

1. Select the **Vehicle (F3)** editor.
2. Select the vehicle (in the vehicle list, or with the vehicle selector at the top of each brake dialog).
3. Choose **Vehicle › Editors › Brakes › Brake System Pressure…** and confirm or edit the **Pedal Ratio** and the pressure vs pedal force curve.
4. If the vehicle is fitted with ABS, choose **Vehicle › Editors › Brakes › ABS / Brake Design…**, press **ABS System…** and tick **ABS Installed**, then edit the ABS System and ABS Designer (wheel) properties. Tick **Antilock (ABS)** in **Vehicle › Editors › Brakes › Brake Assembly…** for the wheels that have it.
5. Choose **Vehicle › Editors › Brakes › Brake Designer…**, select the **Axle** and **Side**, and choose the **Brake Design** (e.g., Disc, Duo-Servo Drum, S-Cam).
6. Edit the design parameters; the brake factor, actuation factor and torque ratio are recalculated as you type.
7. Press **Apply to Wheel** (or **Apply to All Wheels**) to write the torque ratio and pushout pressure into the Brake Assembly.
8. Design the remaining wheels as desired, and check the result in **Vehicle › Editors › Brakes › Brake Assembly…**.
9. Execute the desired suite of simulations to test the effectiveness of the design.
10. Edit the design as required to obtain optimum braking performance.

!!! note "HVE 2027"
    **ABS Installed** is in **Vehicle › Editors › Brakes › ABS / Brake Design… › ABS System…**, not in Brake System Pressure. SIMON reads it: SIMON regulates **every** wheel when ABS Installed, or any wheel's **Antilock (ABS)** box in Brake Assembly, is ticked. EDSVS and EDVTS read only the per-wheel boxes, and EDVDS has no ABS model. Brake System Pressure's **System Type** reaches SIMON's input report only, and the disc/drum choice is each wheel's **Brake Type** in Brake Assembly.

## Overview of Section Eleven

This section provides a detailed explanation of the modeling techniques used
by the HVE Brake Designer, and also presents an overview of the Brake
Designer's interface.

- [Chapter 29 — HVE Brake Designer](29-brake-designer.md) describes in
  detail the process of using the Brake Designer, and the brake torque model.
- [Chapter 30 — Brake Temperature Model](30-brake-temperature.md) provides a
  detailed overview of the Brake Temperature Model.
- [Chapter 31 — Antilock Braking Systems](31-abs.md) provides a detailed
  overview of the HVE Antilock Brake System Model.

## Related Dialog Reference Pages

The individual brake dialogs (HVE's) are documented in detail in the
[Brakes and Powertrain reference](../../04-brakes-powertrain/README.md):

- [Brake Assembly dialog](../../04-brakes-powertrain/BrkAsmblyDlg.md)
- [Disc Brake designer dialog](../../04-brakes-powertrain/DiskBreakDlg.md)
- [Duo-Servo Drum Brake designer dialog](../../04-brakes-powertrain/DueServoBrkDlg.md)
- [Duplex Drum Brake designer dialog](../../04-brakes-powertrain/DuplexBrkDlg.md)
- [Single Piston Drum Brake designer dialog](../../04-brakes-powertrain/BrkSingPistDlg.md)
- [Dual Piston Drum Brake designer dialog](../../04-brakes-powertrain/DualPistBrkDlg.md)
- [Dual Wedge Drum Brake designer dialog](../../04-brakes-powertrain/DualWedgeBrkDlg.md)
- [Brake Designer Material Properties dialog](../../04-brakes-powertrain/BrkMatPropDlg.md) (HVE only; not in HVE 2027)
- [Brake System Pressure vs Pedal Force dialog](../../04-brakes-powertrain/BrkSysVsPedFrcDlg.md)

<!-- NAV -->

---

Next: [Chapter 29 — HVE Brake Designer](29-brake-designer.md) →

<!-- /NAV -->
