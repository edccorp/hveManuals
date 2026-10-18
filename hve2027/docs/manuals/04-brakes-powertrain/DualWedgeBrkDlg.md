# Dual Wedge Brake Dialog Box

HVE has one Brake Designer dialog per brake type. HVE 2027 has a single **Brake Designer** dialog: open it in the Vehicle Editor (**Vehicle (F3)**) with **Vehicle › Editors › Brakes › Brake Designer...**, choose the wheel with **Axle** and **Side**, and choose **Dual-Wedge (Air)** in the **Brake Design** list. The wheel selection, the **Lining Friction Properties** section, the **Results** (Brake Factor, Actuation Factor, Torque Ratio, recomputed continuously) and the **Apply to Wheel** / **Apply to All Wheels** buttons are the same for every type and are described on the [Disk Brake Dialog Box](DiskBreakDlg.md) page. Lengths, areas and pressures are shown in the units set in Preferences; angles are in degrees.

The **Dual-Wedge (Air)** design parameters are:

The air-actuated dual wedge drum brake, in which two air chambers drive wedges that spread the shoes against the drum.

**Air Chamber**
Drop-down list selecting the air chamber size by standard chamber type (Type 9, 12, 18, 20, 24, 30 or 36). Selecting a chamber type sets the Chamber Area to the corresponding nominal effective area.

**Chamber Area**
Effective diaphragm area of the air chamber. Set from the selected chamber type; may also be edited directly.

**Wedge Location**
Location of the wedge actuation point relative to the brake center.

**Pri Wedge Angle**, **Sec Wedge Angle**
Included angle of the wedge actuating the primary and the secondary shoe.

**Drum Diameter**
Inside diameter of the brake drum.

**Pri / Sec Lining Arc Length (Alpha0)**
Length of the lining material along the arc of contact with the drum, entered as an angle.

**Pri Lining Beta**, **Sec Lining Beta**
Angle locating each lining relative to the shoe abutment. (HVE's dual wedge dialog enters *Lining Alph 1* instead.)

**Abutment Distance**, **Abutment Width**
Distance from the brake center to the shoe abutment, and width of the shoe abutment. One value each, for both shoes.

**Pri / Sec Abutment Angle**, **Pri / Sec Abutment Friction**
Angle of each abutment contact surface and the coefficient of friction at it.

**Mechanical Efficiency**
Fraction of the actuation force actually delivered to the shoes after mechanical losses.

**Pushout Pressure**
Pressure required to overcome force associated with return springs and begin developing brake torque.

!!! warning "Not in HVE 2027"
    - **Drum Lining Width**, **Drum Thickness**, **Lining Thickness** and the **Material ...** dialog (see [Brake Designer Material Properties](BrkMatPropDlg.md)): no engine reads them and the Brake Designer's results do not use them.
    - **Maximum Stroke**, **Stroke @ 2ndary Defl**, **2ndary Defl. Factor** and **Expansion Coef**: HVE 2027 shows its *Stroke Factor* section (2nd Deflection Factor, Stroke at 2nd Deflection, Maximum Stroke, Thermal Expansion Coef) for the S-Cam, Single-Wedge and Air Disc designs, but not for the Dual-Wedge design.
    - A separate mechanical efficiency for each shoe.
    - The schematic preview drawing.

<!-- NAV -->

---

← Previous: [Dual Piston Brake Dialog Box](DualPistBrkDlg.md)  |  [Index](README.md)  |  Next: [Duo Servo Brake Dialog Box](DueServoBrkDlg.md) →

<!-- /NAV -->
