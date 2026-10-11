# Render Dialog Box

HVE's Render dialog sets various options that affect the visual appearance of all 3-D objects. HVE 2027 has no Render dialog; its rendering options are in the **Rendering** section of the **Scene Display** window (**View › Scene Display**), and the look of individual materials is set in the **Shader Editor** (**View › Shader Editor**).

## Render Method (View › Scene Display › Rendering)

- **Phong** — Smooth shading from the mesh's own vertex normals. The default.
- **Flat** — One normal per face, taken from the surface actually being drawn, so it shows the real tessellation. Useful for judging how coarse an imported mesh is. Unlike HVE's Flat, lighting is still applied.
- **Wireframe** — Edges only, with the depth test still on, which is also what HVE calls *Hidden*; so Hidden is not listed separately. (Wireframe is greyed in the browser build, which cannot draw it.)

## Light Sources On (View › Scene Display › Rendering)

When off, the sun stops contributing to the picture; the ambient light is raised so that shape and layout stay readable. In HVE 2027 the light sources are the sun and ambient light (see [Light Editor Dialog Box](LightEdDlg.md)).

## Shadows (View › Scene Display › Shadow Coverage)

**Vehicles (sharp)** fits the shadow-casting light to the vehicles, so their shadows are sharp; **Whole scene** fits it to the site as well.

!!! warning "Not in HVE 2027"
    - **Show As** (Actual / Simple) for humans and vehicles. A vehicle with no 3-D geometry file is drawn with a generic body built from its dimensions; one with a file is drawn with it.
    - **Complexity**, **Show Only Faces**, **Render Quality**, **Texture Quality** and **Anti-Aliasing Level**.

!!! tip "New in HVE 2027"
    Per-material appearance (color, roughness, metallic and other Principled-BSDF terms) in the Shader Editor, the **Vehicle › Vehicle Mesh...** shading and opacity controls, and **View › Scene Display › Scene Ghosts** for scene positions. All of these are display only; they do not change a result.

<!-- NAV -->

---

← Previous: [Report Window Dialog Box](PrevWnd.md)  |  [Index](README.md)  |  Next: [Select Object Dialog Box](SelObjDlg.md) →

<!-- /NAV -->
