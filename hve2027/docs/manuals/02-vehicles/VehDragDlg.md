# Vehicle Drag Dialog

**Aerodynamic Drag Dialog**

The vehicle drag associated with aerodynamic pressure. The Aerodynamic Drag dialog allows the user to view or edit these properties for each of the vehicle's aerodynamic surfaces. Each surface stores its own complete set of coefficients and center-of-pressure data.

Open it in the Vehicle Editor with **Vehicle › Editors › Aerodynamic Drag...**, or with **Aerodynamic Drag...** under **Components** in the Vehicles panel. The **Vehicle** list at the top selects the vehicle. Lengths and areas are shown in the units set in Preferences. Values take effect as they are typed; **Close** closes the dialog.

## Surfaces
The four surfaces are the table's columns, side by side, and each row below is a property of every surface:

- Front
- Rear
- Left
- Right

There is no surface selector.

## Drag Device Installed
Switch that activates the surface in its column. When unchecked, the surface produces no aerodynamic force. In HVE 2027 the other fields stay editable whether or not the box is checked.

## Coefficients

### Drag Coef
Assigns the properties resisting motion due to dynamic air pressure acting on the selected surface in the direction of the vehicle's total velocity vector. The force associated with this pressure is proportional to the velocity squared.

### Lift Coef
> **Sign.** A positive Lift Coef presses the vehicle DOWN onto its tires (the force is +Cl·q·A along the vehicle's z axis, which points down): it is a downforce coefficient. This is HVE's own convention and the opposite of the SAE one, where a positive C_L unloads the tires. A production car's SAE lift of about +0.3 is entered here as -0.3.

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
