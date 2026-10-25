# Vehicle Drag Dialog

**Aerodynamic Drag Dialog**

The vehicle drag associated with aerodynamic pressure. The Aerodynamic Drag dialog allows the user to view or edit these properties for each of the vehicle's aerodynamic surfaces. Each surface stores its own complete set of coefficients and center-of-pressure data.

Open it in the Vehicle Editor with **Vehicle › Editors › Aerodynamic Drag...**, or with **Aerodynamic Drag...** under **Components** in the Vehicles panel. The **Vehicle** list at the top selects the vehicle. Lengths and areas are shown in the units set in Preferences. Values take effect as they are typed; **Close** closes the dialog.

## Surfaces
HVE's eight aerodynamic surfaces are the columns of two tables, side by side, and each row is a property of every surface. The **Body Surfaces** table holds:

- Front
- Back
- Left
- Right

and the **Top, Bottom and Devices** table holds:

- Top
- Bottom
- Front Device
- Back Device

There is no surface selector. Two read-only rows head each table:

- **Read By** — which programs read the surface. SIMON applies every installed surface; EDVSM reads only the Front surface's Drag Coef and Surface Area (whether or not it is installed). No other program has aerodynamic forces.
- **Air From** — the air the surface answers to. SIMON takes each surface's force from one signed component of the air speed relative to the vehicle: Front and Front Device act on air from ahead (forward travel), Back and Back Device on air from behind (reversing), Left and Right on a crosswind from their own side, Top on air from above (the vehicle rising) and Bottom on air from below (the vehicle falling). On level ground Top and Bottom therefore do almost nothing.

A Front Device is a second front surface with its own coefficients and center of pressure (a front spoiler or wing, for example); a Back Device is the same at the back.

## Drag Device Installed
Switch that activates the surface in its column. When unchecked, the surface produces no aerodynamic force. In HVE Studio the other fields stay editable whether or not the box is checked.

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

!!! warning "Not in HVE Studio"
    - HVE's rule that grays the coefficients and center of pressure when Device Installed is unchecked.
    - HVE displays the center-of-pressure coordinates relative to the sprung-mass or total-mass CG according to the Vehicle Dimensions Basis preference; HVE Studio has no such preference. HVE Studio shows it from the sprung-mass CG, which is how the vehicle is stored. The preference never changes a result: EDCRASH, EDSMAC, EDSMAC4, EDSVS and EDVTS overwrite it with the total-mass basis when they read their input, in HVE's own source as well.

<!-- NAV -->

---

← Previous: [Stiffness Coefficient Dialog](StiffCoeffDlg.md)  |  [Index](README.md)  |  Next: [Getting Information about the Vehicle](VehicleInfoDlg.md) →

<!-- /NAV -->
