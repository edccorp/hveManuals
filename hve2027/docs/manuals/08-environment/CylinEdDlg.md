# Cylinder Editor Dialog

In HVE the Cylinder Object Tool creates and edits 3-D cylinders — telephone poles, signposts and similar objects — with a Cylinder Editor dialog for the selected cylinder's position, orientation, radius, height and material binding.

!!! warning "Not in HVE 2027"
    HVE 2027 has no Cylinder Editor and no tool for drawing
    primitive objects in the environment. Instead:

    - For **display**, a box can be placed with **Environment › Scene Box
      Editor...** (see [Box Editor](BoxEdDlg.md)). Scene boxes are drawn only;
      no physics program sees them.
    - For an object the vehicles **interact with** — a pole, post, curb or
      barrier — build it in a CAD or modelling program and import it as part
      of the environment's terrain geometry (Environment › Environment...,
      Terrain: DXF, `.h3d`, `.iv`, `.wrl`, OBJ or glTF), then set its surface
      type on its material (see
      [Environment Material Properties](EnvrMatPropDlg.md)).
    - Cube, cylinder, sphere and cone primitives in an imported Inventor
      (`.iv`) or `.h3d` geometry file are converted to ordinary surfaces; they
      cannot be edited as objects afterwards.

<!-- NAV -->

---

← Previous: [Contact Surfaces Dialog](ContSurfDlg.md)  |  [Index](README.md)  |  Next: [Environment Material Properties Dialog](EnvrMatPropDlg.md) →

<!-- /NAV -->
