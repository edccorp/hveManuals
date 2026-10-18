# Duo Servo Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE 2027 has a single **Brake Designer** dialog: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...**, choose the wheel with **Axle** and **Side**, and choose **Duo-Servo Drum** in the **Brake Design** list. The wheel selection, the **Lining Friction Properties** section, the **Results** (Brake Factor, Actuation Factor, Torque Ratio, recomputed continuously) and the **Apply to Wheel** / **Apply to All Wheels** buttons are the same for every type and are described on the [Disk Brake Dialog Box](DiskBreakDlg.md) page. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

The **Duo-Servo Drum** design parameters are:

The duo-servo design, in which the primary shoe drives the secondary shoe through a link, producing a self-energizing (servo) action.

**Wheel Cyl. Piston Dia**
Diameter of the wheel cylinder piston.

**Wheel Cylinder Distance**
Distance from the brake center to the wheel cylinder actuation point.

**Drum Diameter**
Inside diameter of the brake drum.

**Pri Lining Arc Length (Alpha0)**, **Sec Lining Arc Length (Alpha0)**
Length of the lining material along the arc of contact with the drum, entered as an angle.

**Pri Lining Beta**
Angle locating the primary lining relative to the shoe abutment (primary shoe only).

**Sec Lining Alpha1**
Angle locating the leading edge of the secondary lining relative to the shoe actuation axis (secondary shoe only).

**Shoe Pin Radius**
Radial distance from the center of the brake to the anchor pin for the pinned (secondary) shoe.

**Shoe Block Length**
Length of the shoe abutment block.

**Abutment Distance**
Distance from the brake center to the primary shoe abutment (the link between the shoes).

**Abutment Width**
The width of the shoe abutment (HVE enters half the width, *Abutment Width/2*).

**Pri Abutment Angle**, **Pri Abutment Friction**
Angle of the abutment contact surface, and the coefficient of friction at the abutment contact.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical losses.

**Pushout Pressure**
Pressure required to overcome force associated with return springs and begin developing brake torque.

!!! warning "Not in HVE 2027"
    - **Drum Lining Width**, **Drum Thickness**, **Lining Thickness** and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.
    - A separate mechanical efficiency for each shoe.
    - The schematic preview drawing.

<!-- NAV -->

---

← Previous: [Dual Wedge Brake Dialog Box](DualWedgeBrkDlg.md)  |  [Index](README.md)  |  Next: [Duplex Brake Dialog Box](DuplexBrkDlg.md) →

<!-- /NAV -->
