# Duplex Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE Studio has a single **Brake Designer** dialog: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...**, choose the wheel with **Axle** and **Side**, and choose **Duplex Drum** in the **Brake Design** list. The wheel selection, the **Lining Friction Properties** section, the **Results** (Brake Factor, Actuation Factor, Torque Ratio, recomputed continuously) and the **Apply to Wheel** / **Apply to All Wheels** buttons are the same for every type and are described on the [Disk Brake Dialog Box](DiskBreakDlg.md) page. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

The **Duplex Drum** design parameters are:

The duplex design, in which each shoe is actuated by its own wheel cylinder and both shoes act as leading shoes.

**Wheel Cyl. Piston Dia**
Diameter of the wheel cylinder pistons.

**Wheel Cylinder Distance**
Distance from the brake center to the wheel cylinder actuation points.

**Drum Diameter**
Inside diameter of the brake drum.

**Pri / Sec Lining Arc Length (Alpha0)**
Arc length of the lining material in contact with the drum, entered as an angle.

**Pri Lining Beta**, **Sec Lining Beta**
Angle locating each lining relative to the shoe abutment.

**Abutment Distance**, **Abutment Width**
Distance from the brake center to the shoe abutment, and width of the abutment. One value each, for both shoes.

**Pri Abutment Angle**, **Pri Abutment Friction**, **Sec Abutment Angle**, **Sec Abutment Friction**
Angle of each abutment contact surface, and the coefficient of friction at each abutment contact. HVE Studio lets the secondary shoe's values differ from the primary's.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical losses.

**Pushout Pressure**
Pressure required to overcome force associated with return springs and begin developing brake torque.

!!! warning "Not in HVE Studio"
    - **Drum Lining Width**, **Drum Thickness**, **Lining Thickness** and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.
    - A separate mechanical efficiency for each shoe.
    - The schematic preview drawing.

<!-- NAV -->

---

← Previous: [Duo Servo Brake Dialog Box](DueServoBrkDlg.md)  |  [Index](README.md)  |  Next: [Transmission Data Dialog Box](TransDataDlg.md) →

<!-- /NAV -->
