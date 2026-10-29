# Render Dialog Box

HVE's Render dialog sets various options that affect the visual appearance of all 3-D objects. HVE Studio has no Render dialog; its rendering options are in the **Rendering** section of the **Scene Display** window (**View › Scene Display**), and the look of individual materials is set in the **Shader Editor** (**View › Shader Editor**).

## Render Method (View › Scene Display › Rendering)

- **Phong** — Smooth shading from the mesh's own vertex normals. The default.
- **Flat** — One normal per face, taken from the surface actually being drawn, so it shows the real tessellation. Useful for judging how coarse an imported mesh is. Unlike HVE's Flat, lighting is still applied.
- **Wireframe** — Edges only, with the depth test still on, which is also what HVE calls *Hidden*; so Hidden is not listed separately. (Wireframe is grayed in the browser build, which cannot draw it.)

## Light Sources On (View › Scene Display › Rendering)

When off, the sun stops contributing to the picture; the ambient light is raised so that shape and layout stay readable. In HVE Studio the light sources are the sun and ambient light (see [Light Editor Dialog Box](LightEdDlg.md)).

## Shadows (View › Scene Display › Light & Shadow)

**Shadow cascades** sets how many nested layers the sun's shadow is drawn in, from 1 to 4 (3 by default). The first layer is as tight around the vehicles as it can be, so their shadows are sharp; the last covers the whole site, so every pole and building casts one too; each point takes its shadow from the finest layer that holds it. One layer is a single shadow over everything, with softer edges. The panel shows the size of each layer's smallest detail as *Now: N cm per shadow texel*.

!!! warning "Not in HVE Studio"
    - **Show As** (Actual / Simple) for humans and vehicles. A vehicle with no 3-D geometry file is drawn with a generic body built from its dimensions; one with a file is drawn with it.
    - **Complexity**, **Show Only Faces**, **Render Quality**, **Texture Quality** and **Anti-Aliasing Level**.

!!! tip "New in HVE Studio"
    Per-material appearance (color, roughness, metallic and other Principled-BSDF terms) in the Shader Editor, the **Vehicle › Editors › Vehicle Mesh...** shading and opacity controls, and **View › Scene Display › Scene Ghosts** for scene positions. All of these are display only; they do not change a result.

<!-- NAV -->

---

← Previous: [Report Window Dialog Box](PrevWnd.md)  |  [Index](README.md)  |  Next: [Select Object Dialog Box](SelObjDlg.md) →

<!-- /NAV -->
