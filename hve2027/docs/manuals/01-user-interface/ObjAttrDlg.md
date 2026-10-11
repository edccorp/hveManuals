# Object Attributes Dialog Box

In HVE every object created with the 3-D Editor has attributes — name, type, overlay, material name and friction factor — edited in the Object Attributes dialog. HVE 2027 has no 3-D Editor (see [3-D Editor Menu](3dEditor.md)); the environment's surfaces come from an imported site file or HVE case, and their physical attributes are edited per surface:

- In the Environment Editor (**Environment (F4)**), **Environment** panel, **Terrain** section, **Surface Materials**: the site's surfaces grouped by layer, each with a draw switch (eye) and a drive switch (road). Click a surface to select it; the panel then shows *Selected: name -- type, friction* with **Edit in Shader Editor** and **Deselect** buttons.
- In the **Shader Editor** (**View › Shader Editor**, or **Edit in Shader Editor**), whose surface page holds the surface's physical properties beside its appearance.

## Type (Surface Type)

Every surface has a type, which reaches the engines (the surface search treats a curb or friction-zone hit differently from a road hit):

- **Road** — Road surfaces have physical properties (surface elevation, normal and friction) used by the current reconstruction or simulation model.
- **Friction Zone** — Like Road, used to create regions with different frictional properties from the base surface, such as gravel shoulders or oil slicks.
- **Curb** — Identifies the surface as a curb for calculation models that include curb impacts.
- **Water** — Identifies the surface as water.
- **Other** — A purely visual surface.

HVE's *Human* and *Vehicle* object types do not apply to environment surfaces in HVE 2027.

## Friction (Friction Multiplier)

The surface's friction factor. As in HVE, it multiplies the tire's own peak and slide friction, so 1.0 is dry pavement taking nothing away from the tire and anything below it is a reduction. A **Condition preset** list sets it to **Dry (1.00)**, **Wet (0.70)**, **Snow (0.30)** or **Ice (0.15)**.

## Other physical properties

The same page carries the surface's stiffness (Force Constant, Linear, Quadratic and Cubic Stiffness, Damping Rate, Unloading Stiffness) and soil properties (Bekker Constant, Kphi, Kc, Moisture (%)), and its standing water (Water Depth, Wet Friction, Texture Depth).

## Overlay

HVE 2027 groups surfaces into **layers**, shown in **View › Outliner** and in the Surface Materials list; see [Overlays Dialog Box](OverLayDlg.md). A surface is moved to another layer by dragging it onto the layer.

## Material Name, Material Edit...

The surface's name and its appearance (color, texture, roughness) are edited in the **Shader Editor**. Appearance is display only.

!!! warning "Not in HVE 2027"
    - **Dynamic** water depth (a water surface whose depth follows the terrain under it): standing water is a **static** depth per surface, on the surface's **HVE Surface** node (Shader Editor).
    - **Group / UnGroup / Load / Save** of objects, and the Highway Furnishings Library.
    - **Apply**: changes take effect as they are made (they are locked while results are on screen).

<!-- NAV -->

---

← Previous: [Light Editor Dialog Box](LightEdDlg.md)  |  [Index](README.md)  |  Next: [Options Menu](OptionsMenu.md) →

<!-- /NAV -->
