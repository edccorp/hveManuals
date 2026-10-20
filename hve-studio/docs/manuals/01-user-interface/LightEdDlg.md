# Light Editor Dialog Box

HVE's Light Object Tool, in the 3-D Editor, creates and edits light sources placed in the environment: point, directional and spot lights with a position, a direction, a color, an intensity and, for a spot light, a cone and drop-off rate.

!!! warning "Not in HVE Studio"
    HVE Studio has no 3-D Editor, so there is no Light Editor. Lights placed in the environment are made in the Environment panel's **Lights** section instead (below).

The lights HVE Studio does have:

- **The sun and the ambient light.** **View › Shader Editor**, *Sun & Sky* section: the sun set by hand (**Sun Rotation**, **Sun Elevation**) or computed from the site's location, date and time, its strength (**Sun Light**), and **Ambient Light**. The Environment panel's **Sky** section summarizes them and has an **Edit the sun and sky...** button. **View › Scene Display › Rendering › Light Sources On** switches the sun's contribution off and on.
- **Vehicle lights.** **Vehicle › Editors › Vehicle Lights...** in the Vehicle Editor edits the lamps fixed to the selected vehicle on two tabs. **Lamp parts** lists the named parts of the vehicle's mesh (**Show every part** lists the parts that are not lamps too), each with its **Lamp** function, **Side**, **State** (Auto, On or Off), **Casts** (whether it lights the road, not only glows), **Color** and **Reset**; a row set here is kept in the case by part name. **Light sources** lists the vehicle's light sources, each with a **Name**, **Enabled** switch, under **Type & Intensity** its **Type** (Point or Spot; HVE's Directional draws exactly as a spot, so a light stored Directional keeps it until changed) and **Intensity**, **Color**, **Position** (X, Y, Z on the vehicle), **Direction** as **Azimuth (deg)** and **Zenith (deg)**, and for a spot light its **Cone Angle (deg)** and **Drop-Off**. Lights are added and removed with **Add** and **Delete**. Unlike a site light, a vehicle light moves with its vehicle.
- **Site lights** — HVE's environment lights. In the Environment Editor (F4), the Environment panel's **Lights** section: **Add Light**, **Duplicate** and **Delete**, and for the selected light its **Name**, **On**, **On in daylight too**, **Type** (Point or Spot — there is no directional site light; the sun is the directional light), position as **X (forward)**, **Y (right)** and **Height above the ground**, for a spot its **Aim**, **Tilt down**, **Cone (deg, half-angle)** and **Edge softness**, and **Color** and **Intensity**. They light the 3-D view, the ray-traced render and the glTF export, and no engine reads them. See [Environment Information](../08-environment/EnvtInfoDlg.md#lights).

<!-- NAV -->

---

← Previous: [Key Results Dialog Box](KeyResDlg.md)  |  [Index](README.md)  |  Next: [Object Attributes Dialog Box](ObjAttrDlg.md) →

<!-- /NAV -->
