# Brake Designer Single Piston Dialog Box

HVE has one Brake Designer dialog per brake type. HVE 2027 has a single **Brake Designer** dialog: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Brake Designer...**, choose the wheel with **Axle** and **Side**, and choose **Single-Piston Drum** in the **Brake Design** list. The wheel selection, the **Lining Friction Properties** section, the **Results** (Brake Factor, Actuation Factor, Torque Ratio, recomputed continuously) and the **Apply to Wheel** / **Apply to All Wheels** buttons are the same for every type and are described on the [Disk Brake Dialog Box](DiskBreakDlg.md) page. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

The **Single-Piston Drum** design parameters are:

The Single Piston (leading/trailing shoe) design: one wheel cylinder actuates a leading (primary) shoe and a trailing (secondary) shoe.

**Primary Piston Size**, **Secondary Piston Size**
The size of the wheel cylinder piston acting on the primary (leading) and on the secondary (trailing) shoe. HVE 2027 enters them as lengths, where HVE enters piston areas.

**Drum Diameter**
Inside diameter of the brake drum.

**Pri Lining Arc Length (Alpha0)**, **Sec Lining Arc Length (Alpha0)**
Length of the lining material along the arc of contact with the drum, for the primary and secondary shoe, entered as an angle.

**Pri Lining Alpha1**, **Sec Lining Alpha1**
Angle locating the leading edge of the lining relative to the shoe actuation axis.

**Shoe Pin Radius**
Radial distance from the center of the brake to the anchor pin for pinned brake shoes. One value for both shoes.

**Shoe Block Length**
Length of the shoe abutment block. One value for both shoes.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical (friction and linkage) losses. One value for the brake.

**Pushout Pressure**
Pressure required to overcome the force associated with the return springs and begin developing brake torque.

!!! warning "Not in HVE 2027"
    - **Drum Lining Width**, **Drum Thickness**, **Lining Thickness** and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.
    - Piston **areas**: HVE 2027 enters piston sizes as lengths.
    - A separate mechanical efficiency for each shoe: one value is entered.
    - The schematic preview drawing.

<!-- NAV -->

---

← Previous: [Brake Designer Material Properties Dialog Box](BrkMatPropDlg.md)  |  [Index](README.md)  |  Next: [Brake System Pressure vs Pedal Force Dialog Box](BrkSysVsPedFrcDlg.md) →

<!-- /NAV -->
