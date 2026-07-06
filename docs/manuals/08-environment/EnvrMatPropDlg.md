# Environment Material Properties Dialog

This dialog displays the properties of the selected environment (terrain) material. Most numeric parameters are edited either by dragging a slider or by typing directly into the adjacent edit field; the graph is updated when Apply is clicked.

This dialog contains the following items:

## Environment Material Graph
Graph showing the relation between force and deflection for the current material parameters.

## Material Name
User-editable material name for the terrain at X, Y.

## Friction Multiplier
Friction multiplier at X, Y. Dimensionless; valid range 0.0–2.0. Default is 1.0.

## Macrotexture
Surface macrotexture depth, in inches (range 0.0–1.0 in). Used by tire-road friction (e.g., wet-road) calculations. *This entry replaces the Clay Content field found in earlier versions of this dialog.*

## Force-Deflection Properties

### Constant
Force required to initiate deflection at X, Y (lb; range 0–10,000). Default is 5,000 lb.

### Linear Stiffness
Linear material deformation coefficient at X, Y (lb/in; range 0–1,000,000). Default is 50,000 lb/in.

### Quadratic Stiffness
Quadratic material deformation coefficient at X, Y (lb/in²; range -2,500 to 2,500). Default is 1,000 lb/in².

### Cubic Stiffness
Cubic material deformation coefficient at X, Y (lb/in³; range -100 to 3,500). Default is 1,000 lb/in³.

### Damping Constant
Material velocity-dependent deformation constant at X, Y (lb-sec/in; range 0.0–5.0). Default is 0.

### Unloading Slope
Linear unloading slope beginning at maximum deflection (lb/in; range 0–10,000,000). Default is 1,000,000 lb/in.

## Soil Properties

### Bekker Soil Exponent, N
Soil deformation exponent for sinkage calculations (dimensionless; range 0.0–1.0). Default is 0.

### Frictional Soil Mod, Kphi
Frictional soil modulus for sinkage calculations (lb/in^(N+1); range 0–150). Default is 0.

### Cohesive Soil Mod, Kc
Cohesive soil modulus for sinkage calculations (lb/in^(N+2); range 0–40). Default is 0.

### Moisture Content
Fraction of moisture in the soil (%/100; range 0.0–1.0). Default is 0.

## Buttons

### Print
Prints the currently displayed graph.

### Apply
Validates the entered values and redraws the graph with the modified values.

### New
Resets the dialog to the default environment material ("Default Environment Material") with the default values listed above.

### Open...
Opens an environment material from an HVE Material file (\*.matl) in the environment materials directory.

### Save As...
Saves the current material settings to an HVE Material file (\*.matl) for later reuse.

### OK / Cancel
OK validates and accepts the material; Cancel discards the changes.

---
*Source topic: EnvrMatPropDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Cylinder Editor Dialog](CylinEdDlg.md)  |  [Index](README.md)  |  Next: [Environment Information Dialog](EnvtInfoDlg.md) →

<!-- /NAV -->
