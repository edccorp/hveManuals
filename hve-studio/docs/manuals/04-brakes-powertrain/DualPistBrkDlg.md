# Dual Piston Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE Studio has a single **Brake Designer** dialog: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...**, choose the wheel with the **Wheel:** buttons (**A1 Left**, **A1 Right**, ...), and choose **Dual-Piston Drum** in the **Brake Design** list. The wheel selection, the **Lining Friction Properties** section, the **Results** (Brake Factor, Actuation Factor, Torque Ratio, recomputed continuously) and the **Apply to Wheel** / **Apply to All Wheels** buttons are the same for every type and are described on the [Disk Brake Dialog Box](DiskBreakDlg.md) page. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

The **Dual-Piston Drum** design parameters are:

The Dual Piston (two leading shoes) design. HVE calculates its brake factor by assuming the primary and secondary shoes are each a pinned leading shoe. Its fields are the same as the Single Piston design's:

**Primary Piston Size**, **Secondary Piston Size**
The size of the wheel cylinder piston acting on the primary and on the secondary shoe, entered as lengths (HVE enters piston areas).

**Drum Diameter**
Inside diameter of the brake drum.

**Pri / Sec Lining Arc Length (Alpha0)**
Length of the lining material along the arc of contact with the drum, entered as an angle.

**Pri / Sec Lining Alpha1**
Angle locating the leading edge of the lining relative to the shoe actuation axis.

**Shoe Pin Radius**, **Shoe Block Length**
Radial distance from the center of the brake to the anchor pin, and length of the shoe abutment block. One value each, for both shoes.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical losses.

**Pushout Pressure**
Pressure required to overcome force associated with return springs and begin developing brake torque.

!!! warning "Not in HVE Studio"
    - **Drum Lining Width**, **Drum Thickness**, **Lining Thickness** and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.
    - Piston **areas**: HVE Studio enters piston sizes as lengths.
    - A separate mechanical efficiency for each shoe.
    - The schematic preview drawing.

<!-- NAV -->

---

← Previous: [Drive Train Dialog Box](DriveTraDlg.md)  |  [Index](README.md)  |  Next: [Dual Wedge Brake Dialog Box](DualWedgeBrkDlg.md) →

<!-- /NAV -->
