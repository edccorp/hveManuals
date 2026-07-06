# Surface Editor Dialog

The Surface Editor is used for entering and editing 3-D surfaces. When the Surface tool is selected from the toolbar, the editor starts in Vertex mode so the vertices of a new surface can be entered.

Note: In HVE-2D, the Roll and Pitch angle fields are displayed read-only.

This dialog contains the following items:

## Coords (ft) — X, Y, Z
The coordinates of the current vertex (or of the surface object, in Object mode), in feet.

## Angle (deg) — Roll, Pitch, Yaw
The orientation of the current selection, in degrees. The angle fields are active only when an object (rather than an individual face or vertex) is being edited.

## Global/Local
A combo box selecting the coordinate reference used for the entered values: **Global** (earth-fixed) or **Local** (relative to the surface object). Global is the default.

## Mode
Radio buttons selecting the current pick/edit mode. Only the modes valid for the current selection are enabled:

- **Object** — pick and move/rotate the entire surface object. Enables the Add button so additional polygons can be added.
- **Face** — pick individual polygons of the surface. Enables the Rev Nrml button.
- **Vertex** — pick and edit individual vertices. This is the initial mode when creating a new surface.
- **Subdivide** — scissors mode used to split (subdivide) the surface; the split is performed when Apply is clicked. *This mode is new and was not documented in earlier help.*

*The "Bind To Object/Face/Vertex" radio buttons documented in earlier versions are no longer part of this dialog (they remain in the Cone/Cylinder editors).*

## Add
Begins adding a new polygon to the active surface. Enabled while in Object edit mode.

## End
Closes (ends) the polygon currently being entered. The button is disabled as soon as it is clicked; Add is re-enabled if the editor is in Object edit mode.

## Rev Nrml
Reverses the surface normal of the picked face. Enabled only in Face mode.

## Dec/Tes
Displays the Decimate/Tessellate dialog, used to reduce (decimate) or refine (tessellate) the surface mesh. *This button is new and was not documented in earlier help.*

## Apply
Selecting Apply causes the entered parameters to be accepted, and the first vertex will appear in the views at the specified X, Y and Z coordinate. A small, bright marker is displayed at the location of the first vertex. In Subdivide mode, Apply performs the surface split. Surface Editor actions applied this way are registered with the Undo/Redo manager.

---
*Source topic: SurfEdDlg.htm — updated from source code (HVEINV-64, Physics) 2026-07-05.*

<!-- NAV -->

---

← Previous: [Sphere Editor Dialog](SpereEdtDlg.md)  |  [Index](README.md)

<!-- /NAV -->
