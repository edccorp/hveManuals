# Surface Editor Dialog

In HVE the Surface Editor enters and edits 3-D surfaces in the environment
vertex by vertex: object, face, vertex and subdivide modes, global or local
coordinates, reversing a face normal, and decimating or tessellating the mesh.

!!! warning "Not in HVE 2027"
    HVE 2027 has no surface editor and does not edit environment geometry.
    Build or edit the site in a CAD or modelling program and import it in
    **Environment › Environment...**, Terrain (DXF, `.h3d`, `.iv`, `.wrl`, OBJ
    or glTF).

    What HVE 2027 does edit on imported surfaces:

    - whether each surface is **drawn** and whether it is **driven on** (the
      eye and road switches of the Outliner, View › Outliner);
    - each surface's **type, friction, stiffness and soil properties**, on the
      HVE Surface node of its material in the Shader Editor (see
      [Environment Material Properties](EnvrMatPropDlg.md));
    - how the site is **shaded** (Flat, Smooth, Auto Smooth) and how each
      surface **looks** (its node material in the Shader Editor).

    These edits are kept with the case and re-applied each time the geometry
    is read from its file.

<!-- NAV -->

---

← Previous: [Sphere Editor Dialog](SpereEdtDlg.md)  |  [Index](README.md)

<!-- /NAV -->
