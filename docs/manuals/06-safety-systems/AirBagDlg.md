# Air Bag Restraints Dialog Box

The airbag restraint systems of the vehicle are displayed and edited using the Air Bag dialog (title: *Air Bag: [vehicle name]*). Program units for vehicle airbag restraint properties are displayed with each field label. Values entered outside the typical range produce a warning; values outside the allowed range are rejected.

Note: Deploy coordinates are entered in the vehicle-fixed coordinate system. If the vehicle dimensions basis is set to Total (rather than Sprung) in the Options, the displayed coordinates are adjusted accordingly.

## Seat Position

A drop-down list used to select the occupant location of the airbag being edited. Nine positions are available: Front, Rear and Back rows, each with Right, Center and Left positions (e.g. "Front, Right"). All remaining fields in the dialog apply to the currently selected seat position.

## Device Installed

A checkbox indicating that the vehicle has an airbag installed at the current seat position. Default: not installed. (An airbag must be installed here before it can be placed in use in the event's Airbag Restraint System dialog.)

## Deploy Coords (in) - x, y, z

Assign the vehicle-fixed x, y and z coordinates where the airbag is installed and deployed. Defaults: x = 100, y = -40, z = -50 in. Typical range: x ±300 in, y and z ±60 in; allowed range ±500 in for each coordinate.

## Initial Bag Radius (in)

Assigns the initial (undeployed) radius of the airbag. Default: 0.05 in. Typical range 2.0-15.0 in; allowed range 0.1-30.0 in.

## Passenger Bag Length (in)

Assigns the length for non-driver-side (passenger) airbags. Default: 25 in. Typical range 10.0-48.0 in; allowed range 1.0-100.0 in.

## Initial Pressure (lb/in^2)

Assigns the initial pressure inside the airbag. Default: 10 lb/in². Typical range 0.0-15.0; allowed range 0.0-50.0.

## Bag Membrane Thickness (in)

Assigns the thickness of the airbag membrane (fabric) material. Default: 0.05 in. Typical range 0.001-0.05 in; allowed range 0.00001-0.1 in.

## Full Inflation Volume (in^3)

Assigns the volume inside the airbag when fully inflated. Default: 12000 in³. Typical range 10.0-5000.0 in³; allowed range 1.0-50000.0 in³.

## Discharge Coefficient

Assigns the thermodynamic discharge coefficient for the airbag vent hole (dimensionless). Default: 0.5. Typical range 0.25-1.0; allowed range 0.10-1.0.

## Discharge Vent Area (in^2)

Assigns the area of the airbag vent hole. Default: 10 in². Typical range 1.0-10.0 in²; allowed range 0.01-20.0 in².

## Pressure to Open Vent Hole (lb/in^2)

Assigns the airbag pressure required to cause the vent hole to open. Default: 0.5 lb/in². Typical range 0.0-10.0; allowed range 0.0-100.0.

## Maximum Penetration (in)

Assigns the penetration (deflection distance) required before any force is computed. Default: 25 in. Typical range 0.001-10.0 in; allowed range 0.0-100.0 in.

## Force Convergence Criterion (lb)

Assigns the permissible force imbalance between the airbag and contact surfaces. Default: 20 lb. Typical range 1.0-50.0 lb; allowed range 0.0001-200.0 lb.

## Backside Contact Surface

An option list containing all the vehicle interior contact surfaces. The selected surface is used to assign the material properties for the contact surface supporting the airbag. This option is disabled (grayed out) if the vehicle has no contact surfaces defined.

## Bag Elastic Modulus (lb/in^2)

Assigns the elastic modulus for the airbag material during airbag filling. Typical range 5000-20000 lb/in²; allowed range 1000-50000 lb/in².

## Bag Rebound Modulus (lb/in^2)

Assigns the elastic modulus for the airbag material during rebound. Typical range 10000-100000 lb/in²; allowed range 5000-500000 lb/in².

## Bag Bottom-out Modulus (lb/in^2)

Assigns the elastic modulus for the airbag material after it has bottomed out. Typical range 10-100 lb/in²; allowed range 1-5000 lb/in².

## Gas Density (lb/in^3)

Assigns the gas density for the airbag filling agent. Typical range 0.000005-0.001 lb/in³; allowed range 0.0-1.0 lb/in³.

## Gas Mass Flowrate (lb/sec)

Assigns the mass flow rate for the airbag filling gas. Typical range 1.0-100.0 lb/sec; allowed range 0.1-1000.0 lb/sec.

## Gas Specific Heat Ratio

Assigns the specific heat ratio for the airbag filling agent (dimensionless). Typical range 0.9-1.1; allowed range 0.05-20.0.

## Max. Column Collapse Dist (in)

Assigns the maximum distance the steering column is allowed to collapse (applies to driver-side airbags only). Typical range 1.0-20.0 in; allowed range 0.1-50.0 in.

## Column Collapse Load (lb)

Assigns the axial load on the steering column required to begin collapsing the column (applies to driver-side airbags only). Typical range 100-5000 lb; allowed range 1-50000 lb.

## Column Angle (deg)

Assigns the steering column angle, about the vehicle's pitch axis (normally a negative angle). Typical range ±45°; allowed range ±90°.

---
*Source topic: AirBagDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Accelerometers Dialog](AcclMtrsDlg.md)  |  [Index](README.md)  |  Next: [Airbag Restraint System Dialog Box](AirBagSysDlg.md) →

<!-- /NAV -->
