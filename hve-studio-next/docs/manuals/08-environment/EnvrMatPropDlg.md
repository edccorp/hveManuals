# Environment Material Properties Dialog

The properties of a terrain surface material: its friction, its force–deflection
law (for contact with the ground) and its soil properties (for sinkage).

!!! note "HVE Studio"
    A road surface's type and physical properties are edited on the **HVE
    Surface** node of the surface's material in the **Shader Editor**. Select
    the surface — click it in the 3-D view of the Environment editor (F4), or
    pick its row in **Environment › Environment...**, Terrain, **Surface
    Materials** — and press **Edit in Shader Editor**. The node, with an orange
    title bar reading **HVE Surface -- <surface name>**, sits on the material's
    canvas beside the nodes that set how the surface looks. Its upper rows are
    headed **PHYSICS -- these change the result**.

    The material applied to a drivable polygon that has no material of its own
    — HVE's *Default Environment Material* — is edited in the Environment window
    itself: select **Default surface material** in the Outliner (View ›
    Outliner).

    Forces, stiffnesses and damping follow the units set in Tools ›
    Preferences. While a solved run is on screen the physics rows are
    read-only.

## Surface Type

**Road**, **Friction Zone**, **Curb**, **Water** or **Other**. Friction Zone and
Curb reach the solver: the road database is searched in type order, and a hit on
a curb or friction zone ends the search where a road hit keeps searching. A
Water surface is run as Road; standing water comes from **Water Depth** below.
**Other** is scenery, as in HVE, which leaves an Other polygon out of its
physics: a surface of type Other comes in with **Drive** off, and choosing Other
switches Drive off (choosing another type switches it back on). The type is
also the **Type** column of the Outliner, where it can be changed for several
selected surfaces at once.

!!! note "HVE Studio"
    In HVE the type is set as the Default Type of an imported geometry file.
    Here it is set per surface.

## Material library

A list of HVE's own environment material files (`.matl`) and **Apply material**,
which fills the fields below from the chosen file. The fields stay editable.
When no material files are found, the node says where HVE keeps them and that
setting `HVE_MATERIAL_PATH` to that folder makes them available.

!!! note "HVE Studio"
    This replaces HVE's **Open...** and **New**. There is no **Save As...**.

## Condition preset

**Dry (1.00)**, **Wet (0.70)**, **Snow (0.30)** or **Ice (0.15)** — sets the
Friction Multiplier to that value.

!!! tip "New in HVE Studio"
    The condition presets.

## Friction Multiplier

Friction multiplier for the surface. 1.0 is the tire's own friction, unreduced:
it scales the tire friction tables (the Load & Speed Tables panel of
Vehicle › Editors › Tires).

## Force-deflection properties

**Force Constant** — Force required to initiate deflection. HVE's *Constant*.

**Linear Stiffness** — Linear material deformation coefficient.

**Quadratic Stiffness** — Quadratic material deformation coefficient.

**Cubic Stiffness** — Cubic material deformation coefficient.

**Damping Rate** — Material velocity-dependent deformation constant. HVE's
*Damping Constant*.

**Unloading Stiffness** — Linear unloading slope, beginning at maximum
deflection. HVE's *Unloading Slope*.

## Soil (Bekker) model

**Bekker Constant** — Soil deformation exponent *N* for sinkage calculations.

**Kphi** — Frictional soil modulus for sinkage calculations.

**Kc** — Cohesive soil modulus for sinkage calculations.

**Moisture (%)** — Moisture content of the soil.

These are read by SIMON's soft-soil tire–terrain model (event Wheels dialog,
Terrain Model tab).

## Standing water

**Water Depth**, **Wet Friction** and **Texture Depth** for this surface, read only by SIMON's hydroplaning models (Event Information › SIMON Options › Hydroplaning). A depth above 0 puts a layer of water over this surface — HVE's own water polygon, with the wet friction as its friction — and the texture depth is the pavement's, read wherever a tire is on this surface. A depth of 0 means no water here. Ground with no surface of its own takes these from the Environment panel's **Default surface material**.

A surface imported from an HVE case or `.h3d` arrives with its own **Texture Depth**: the twelfth term of HVE's environment material, which HVE's program reads as the pavement texture depth in inches (0.025 in for *Asphalt, New*). **Apply material** from the library fills it too, from the file's twelfth line — *Microtexture* on a pavement, and on a soil the line HVE labels *Clay Content*, which HVE hands its physics as the same texture depth.

!!! note "No Clay (%) row"
    HVE's dialog shows that twelfth term as *Clay Content*, but no physics program reads a clay fraction: the slot is the texture depth above. HVE Studio shows it once, as **Texture Depth**.

## Appearance

!!! tip "New in HVE Studio"
    The surface's look — its color, roughness and metallic — belongs to its
    material and is edited in the **Shader Editor** (**Edit in Shader
    Editor**). None of it reaches a physics program. A case saved by an
    earlier version that overrode a surface's base color keeps that color and
    says so under the physics rows, with **Clear Override** to drop it.

## Reset to File Value

Discards the edits to this surface and restores what the geometry file states.

!!! warning "Not in HVE Studio"
    - **Macrotexture** is not a separate field: the surface's **Texture Depth**,
      under **Standing water** on this node with **Water Depth** and **Wet
      Friction**, is the pavement texture SIMON's hydroplaning models read.
    - The **force–deflection graph**, **Print**, **Apply** and **OK / Cancel**:
      edits apply when a field is left, and **Edit › Undo** (Ctrl+Z) takes one
      back.

<!-- NAV -->

---

← Previous: [Cylinder Editor Dialog](CylinEdDlg.md)  |  [Index](README.md)  |  Next: [Environment Information Dialog](EnvtInfoDlg.md) →

<!-- /NAV -->
