# Brake Designer Material Properties Dialog Box

In HVE this dialog displays the material properties used by the Brake Designer for thermal calculations, and is opened by the **Material ...** button of any Brake Designer dialog. The properties are divided into two groups, Rotor/Drum and Lining, each with a density, a specific heat, a conduction coefficient, a convection coefficient and the velocity dependence of the convection.

!!! warning "Not in HVE 2027"
    The Brake Designer in HVE 2027 has no material properties and no **Material ...** button. These values serve HVE's brake thermal calculations; no engine reads them and HVE 2027's Brake Designer does not use them, so HVE 2027 does not keep them.

## Brake Material Properties (Vehicle menu)

**Vehicle › Brake Material Props...** opens a different window, **Brake Material Properties**, that has no HVE counterpart. It holds a list of named brake friction materials (it starts with Standard Organic, Semi-Metallic, Ceramic Composite and Sintered Metal) with **Name**, **Dry**, **Wet** and **Hot (fade)** friction coefficients, **Heat Capacity (J/kg·K)** and **Wear Rate**, and **Add** and **Delete** buttons.

![Brake Material Properties window](images/hvn-brake-material-properties.png)

!!! warning "Not in HVE 2027"
    The Brake Material Properties list is not saved with the case and is not used by the Brake Designer, any other dialog or any engine, so the window is shown greyed and says so. The lining friction a wheel's brake design uses is in the Brake Designer's **Lining Friction Properties** section.

<!-- NAV -->

---

← Previous: [Brake Assembly Dialog Box](BrkAsmblyDlg.md)  |  [Index](README.md)  |  Next: [Brake Designer Single Piston Dialog Box](BrkSingPistDlg.md) →

<!-- /NAV -->
