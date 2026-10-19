# Chapter 14 — Environment Designer

The Environment Designer is the Vehicle Designer's frame turned on the site:
a stage bar along the bottom, a **Key figures** strip on the left that
remembers what each number was, the site's panels hosted on the stage that
asks their question, and a **Warnings & Suggestions** panel on the right whose
rows name the fix and the stage that owns it. Open it with **Environment ›
Environment Designer...** in the Environment editor (F4), where it is the
first item.

One thing differs from the vehicle's frame: terrain needs the real renderer,
so with **Fill the window** on the designer takes the left of the editor's
work area and the 3-D view stays on the right. Off, it is a window of its own
size. Every panel it hosts is the same panel the **Environment** window draws,
so a field has one editor and nothing is reachable in one and not the other.

![Figure 14-1](../images/hvn-05-environment-designer.png)

*Figure 14-1: The Environment Designer on its Geometry stage, filling the left of the work area with the 3-D view beside it.*

## The stages

1. **Site**: Location (placement, address, coordinates) and **Aerial Image...**
   (the backdrop, in its own window). Scene description; nothing here reaches
   a solve.
2. **Geometry**: the scene geometry file, its import frame and the survey point
   cloud — the Terrain section. The drivable triangles here are what every
   vehicle runs on.
3. **Surfaces**: the Outliner's tree hosted on the stage (layers, surfaces and
   objects with their eye and Drive switches; **Open the Outliner** puts the
   same tree in its own window), the **Selected Surface** section for the
   surface picked in the tree or the 3-D view, **Edit Mode (Tab)** to pick
   faces in the viewport and give them a material or split a surface by them,
   and the Surface Generator. The Key figures strip's **Drivable patches** row
   counts the drivable surface's connected pieces: more than one means a wheel
   can run off an edge onto the default plane.

   ![Figure 14-2](../images/hvn-05-environment-designer-surfaces.png)

   *Figure 14-2: The Surfaces stage: the Outliner tree, Edit Mode, the
   Selected Surface section and the Surface Generator on one page.*

4. **Water & Weather**: gravity, rolling resistance, the ambient air and wind,
   and standing water — the Physical section.
5. **Sky & Lights**: the sun, the sky and the site's lights. Display only, and
   the stage says so.
6. **Objects**: **Scene Box Editor...** for the drawn boxes.
7. **Site Check**: not built yet. It will settle a probe vehicle on the current
   physics at each drivable surface and read back the settle height and the
   friction and water the engine found.
8. **Summary**: the site's name and file, **Set as baseline** (kept for this case
   across sessions), **Copy spec sheet** (tab-separated text on the clipboard),
   the spec sheet with its baseline and change, and every warning.

## Key figures

Site extent in x and y and the farthest point from the origin; the drivable
area, the drivable and scenery triangle counts, the surfaces and generated
surfaces; the lowest and highest friction multiplier among the drivable
materials; the water triangles; the maximum grade read from the drivable
triangles and the stated grade of a graded terrain; gravity, ambient
temperature, scene boxes and site lights. **Set as baseline** under the strip
keeps the current values as the "was" column for this case.

## Warnings & Suggestions

| Grade | Stage | Rule |
|---|---|---|
| Fix | Surfaces | A drivable surface's friction multiplier is 0, which every tire reads as no friction. |
| Fix | Geometry | The site names a geometry file but no triangle is drivable, so vehicles run on the default plane. |
| Note | Site | The site reaches more than 2 km from the origin, where single precision coarsens. |
| Note | Water & Weather | The stated gravity differs from 9.80665 m/s² by more than 1%. |
| Consider | Surfaces | The drivable surface is more than one patch and the smallest is under 2% of the area, so its edge drops a wheel onto the default plane. |
| Note | Surfaces | A palette entry owns no drawn or drivable triangle, so editing its friction changes nothing. |

A rule that lacks its input stays silent, and the count beside the panel's
title lists what is checked on hover.
