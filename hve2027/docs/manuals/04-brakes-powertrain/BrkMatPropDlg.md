# Brake Designer Material Properties Dialog Box

In HVE this dialog displays the material properties used by the Brake Designer for thermal calculations, and is opened by the **Material ...** button of any Brake Designer dialog. The properties are divided into two groups, Rotor/Drum and Lining, each with a density, a specific heat, a conduction coefficient, a convection coefficient and the velocity dependence of the convection.

!!! note "In HVE 2027"
    These properties are the Brake Designer's **Material Properties** section
    (**Vehicle › Brakes › Brake Designer...**), with **Rotor / Drum** and
    **Pad / Lining** groups and the rotor, pad, drum and lining
    **Thicknesses** beside them, rather than a separate dialog behind a
    **Material ...** button. They are the inputs of SIMON's brake temperature
    model (the Drum, Lining, Rotor and Pad temperature output channels) and
    are kept with the vehicle; they do not change the brake torque. In the US
    unit system they are shown in HVE's own units (lb/in³, in-lb/lb-°F,
    in-lb/in-s-°F, in-lb/in²-s-°F).

    Earlier previews of HVE 2027 had a *Brake Material Props* item on the
    Vehicle menu: a list of named lining materials with friction, heat capacity and
    wear rate that no engine read and the case did not save. It has been
    removed. The lining friction a wheel's brake design uses is in the Brake
    Designer's **Lining Friction Properties** section (**Vehicle › Brakes ›
    Brake Designer...**).

<!-- NAV -->

---

← Previous: [Brake Assembly Dialog Box](BrkAsmblyDlg.md)  |  [Index](README.md)  |  Next: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md) →

<!-- /NAV -->
