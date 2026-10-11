# Vehicle Drag Dialog

**Aerodynamic Drag Dialog**

The vehicle drag associated with aerodynamic pressure. The Aerodynamic Drag dialog allows the user to view or edit these properties for each of the vehicle's aerodynamic surfaces. Each surface stores its own complete set of coefficients and center-of-pressure data.

Open it in the Vehicle Editor with **Vehicle › Aero Dynamic Drag...**, or with **Aerodynamic Drag...** under **Vehicle Properties** (in the Vehicles panel or the [Vehicle Information dialog](VehicleInfoDlg.md)). The **Vehicle** list at the top selects the vehicle. Lengths and areas are shown in the units set in Preferences. Values take effect as they are typed; **Close** closes the dialog.

## Surface
Selects the surface whose data is displayed. The available surfaces are:

- Front
- Rear
- Left
- Right

## Drag Device Installed
Switch that activates the selected surface. When unchecked, the surface produces no aerodynamic force. In HVE 2027 the other fields stay editable whether or not the box is checked.

## Coefficients

### Drag Coef
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the direction of the vehicle's total velocity vector. The force associated with this pressure is proportional to the velocity squared.

### Lift Coef
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the direction normal (vertical) to the vehicle's total velocity vector.

### Side Coef
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the lateral direction, normal to the vehicle's total velocity vector.

### Surface Area
Assigns the projected area parallel to the selected surface.

## Center of Pressure

### X, Y, Z
Vehicle-fixed X, Y and Z coordinates where the effective force from aerodynamic pressure is applied.

!!! warning "Not in HVE 2027"
    - The **Top**, **Bottom**, **FrontDevice** and **BackDevice** surfaces. HVE 2027 carries the four surfaces listed above; the engines receive the other four as unused.
    - HVE's rule that greys the coefficients and center of pressure when Device Installed is unchecked.
    - HVE displays the center-of-pressure coordinates relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE 2027 has no such preference. HVE 2027 shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

<!-- NAV -->

---

← Previous: [Stiffness Coefficient Dialog](StiffCoeffDlg.md)  |  [Index](README.md)  |  Next: [Getting Information about the Vehicle](VehicleInfoDlg.md) →

<!-- /NAV -->
