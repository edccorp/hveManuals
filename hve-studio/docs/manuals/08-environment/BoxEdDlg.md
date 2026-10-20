# Box Editor Dialog

In HVE the Box Object Tool creates and edits 3-D boxes in the environment —
buildings, sidewalks, curbs and other box-shaped objects — with a Box Editor
dialog for the selected box's position, orientation and size.

HVE's Box Editor sets the box's **position** and its **orientation** as
*Roll*, *Pitch* and *Yaw*, either in the **Global** or the **Local** frame,
and its **size** (length, width and height; HVE forces the height equal to
the length when the edit is applied). A box can be **bound** to another
object, face or vertex, and individual faces and vertices can be edited.
Changes take effect when **Apply** is pressed.

!!! warning "Not in HVE Studio"
    HVE Studio has no Box Editor and no tool for drawing boxes or other
    primitive objects in the environment. Instead:

    - Build curbs, walls, buildings and other box-shaped objects in a CAD or
      modelling program and import them as part of the site: a DXF, `.h3d`,
      `.iv`, OBJ or glTF file, with **Environment › Environment... › Terrain ›
      Scene Geometry**. Set the type of their surfaces on their material (see
      [Environment Material Properties](EnvrMatPropDlg.md)).
    - Draw a drivable region or a friction zone over the site with the
      **Surface Generator** (Environment window, *Surface Generator* section;
      see [Environment Information](EnvtInfoDlg.md#surface-generator)).
    - Boxes stored in a case saved by an earlier HVE Studio version are ignored
      when the case is opened.

<!-- NAV -->

---

← Previous: [Environment](README.md)  |  [Index](README.md)  |  Next: [Cone Editor Dialog](ConeEdtDlg.md) →

<!-- /NAV -->
